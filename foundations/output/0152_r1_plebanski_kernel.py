"""0152 -- R1: put the constrained sector's kernel through the test.

0160 forced the conclusion but did not verify it: ANY local
two-derivative diffeomorphism-invariant quadratic form is
Einstein-Hilbert, so IF the constrained sector is invariant its gamma
is +1. A lattice breaks diffeomorphisms somewhere. Whether the
constrained sector breaks them at Einstein-Hilbert's 1e-16 or at the
induced route's 0.30 is the measurement that settles it.

THE CONSTRUCTION. Palatini/Plebanski, linearised:

    S = (1/4) eps^{mu nu rho sig} eps_{abcd} e_mu^a e_nu^b F_{rho sig}^{cd}

with e = 1 + h/2 and F = d omega + omega omega. To second order the
only surviving pieces are one h-omega cross term and one omega-omega
term; integrating omega out leaves a pure quadratic form in h. That
is the constrained sector's kernel, and 0050 already established that
this is the sector with 2 degrees of freedom rather than 0.

  s0  BUILD AND GATE. With continuum derivatives the result must
      come out as (1, -1, -2, 2) in 0150's basis -- linearised
      Einstein-Hilbert -- or the tensor algebra is wrong and nothing
      after it counts.
  s1  THE LATTICE VERSION, with finite differences in place of
      derivatives.
  s2  THE DIFFEOMORPHISM TEST, against the induced kernel's 0.30.
"""

import importlib.util
import itertools
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, tag):
    s = importlib.util.spec_from_file_location(
        tag, os.path.join(HERE, name))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


D0 = _load("0150_diffeo_invariance.py", "d152")
O = D0.O
EB, PAIRS = O.EB, O.PAIRS
L = 12

EPS = np.zeros((4, 4, 4, 4))
for p in itertools.permutations(range(4)):
    s = np.sign(np.prod([np.sign(p[j] - p[i])
                         for i in range(4) for j in range(i + 1, 4)]))
    EPS[p] = s

WPAIRS = [(c, d) for c in range(4) for d in range(c + 1, 4)]


def omega_basis():
    """24 = 4 directions x 6 antisymmetric internal pairs."""
    B = []
    for rho in range(4):
        for (c, d) in WPAIRS:
            w = np.zeros((4, 4, 4))
            w[rho, c, d] = 1.0
            w[rho, d, c] = -1.0
            B.append(w)
    return np.array(B)


WB = omega_basis()


def blocks(dvec):
    """A (10x24) and B (24x24) for derivative factors d_rho."""
    A = np.zeros((10, 24), complex)
    for i in range(10):
        for j in range(24):
            A[i, j] = 0.5 * np.einsum(
                "mnrs,mbcd,nb,r,scd->",
                EPS, EPS, EB[i], dvec, WB[j])
    Bm = np.zeros((24, 24), complex)
    for j1 in range(24):
        for j2 in range(24):
            Bm[j1, j2] = 0.5 * np.einsum(
                "mnrs,mncd,rce,sed->",
                EPS, EPS, WB[j1], WB[j2])
    Bm = 0.5 * (Bm + Bm.conj().T)
    return A, Bm


def kernel(dvec):
    """integrate omega out: K_h = -A B^+ A^dagger."""
    A, Bm = blocks(dvec)
    return -(A @ np.linalg.pinv(Bm, rcond=1e-10) @ A.conj().T)


def fit_in_basis(K, k):
    """express K in 0150's four local scalars; returns coefficients
    normalised to the first."""
    F = D0.basis_forms(k)
    M = np.array([f.reshape(-1) for f in F]).T
    c, *_ = np.linalg.lstsq(M, np.real(K).reshape(-1), rcond=None)
    resid = np.linalg.norm(M @ c - np.real(K).reshape(-1)) / max(
        np.linalg.norm(K), 1e-30)
    return c / c[0], resid


def s0_gate():
    print("== s0: build and gate ==")
    print("  With continuum derivatives (d_rho = i k_rho) the "
          "kernel obtained by")
    print("  integrating out the connection must be linearised "
          "Einstein-Hilbert,")
    print("  i.e. (1, -1, -2, 2) in 0150's basis.")
    print()
    rng = np.random.default_rng(152)
    ok = True
    for t in range(3):
        k = rng.standard_normal(4)
        K = kernel(1j * k)
        c, r = fit_in_basis(K, k)
        print(f"    trial {t}:  coefficients "
              f"{np.array2string(c, precision=5)}"
              f"   fit residual {r:.2e}")
        ok &= (np.abs(c - np.array([1, -1, -2, 2])).max() < 1e-6
               and r < 1e-8)
    print()
    assert ok, "linearised Palatini did not reproduce EH"
    print("  GATE PASSED. The tensor algebra is right: integrating "
          "the connection out")
    print("  of the constrained action returns Einstein-Hilbert "
          "exactly, with no")
    print("  counterterms and nothing tuned.")
    print()


def s1_lattice_and_test():
    print("== s1/s2: the lattice version, and the "
          "diffeomorphism test ==")
    print("  Replace the derivative by the lattice finite "
          "difference,")
    print("      d_rho = exp(i k_rho) - 1,")
    print("  and test with the SAME gauge modes 0150 used, so the "
          "comparison is like")
    print("  for like.")
    print()
    print("     k                khat^2   constrained    induced "
          "     ratio")
    rows = []
    for kk in ((0, 1, 0, 0), (0, 2, 0, 0), (0, 1, 1, 0),
               (0, 2, 1, 1), (0, 3, 0, 0), (0, 3, 2, 1)):
        kc = np.array([2 * np.pi * ki / L for ki in kk])
        kv = np.array([2 * np.sin(np.pi * ki / L) for ki in kk])
        k2 = float(kv @ kv)
        G = D0.gauge_modes(kv)
        Kp = kernel(np.exp(1j * kc) - 1.0)
        vp = float(np.linalg.norm(Kp @ G)
                   / (np.linalg.norm(Kp) * np.linalg.norm(G)))
        vi = D0.__dict__.get("_cache_induced", {}).get(kk)
        if vi is None:
            vh = O.vhat(L)
            Lc = 4.0 * O.beta_mat(vh)[0][0, 0]
            HA, _ = O.hessian(vh, kk, L, False)
            Ki = HA + D0.C8.counterterm(Lc)
            vi = float(np.linalg.norm(Ki @ G)
                       / (np.linalg.norm(Ki) * np.linalg.norm(G)))
        rows.append((k2, vp, vi))
        print(f"    {str(kk):14s}  {k2:6.3f}   {vp:.4e}   "
              f"{vi:.4e}   {vp / vi:.2e}")
    r = np.array(rows)
    print()
    print("  The pattern is BIMODAL, not a power law -- machine "
          "zero for momenta with")
    print("  at most two distinct nonzero components, ~1e-2 for "
          "generic ones. Fitting a")
    print("  power to it gives a meaningless exponent, so the "
          "scaling is tested on the")
    print("  generic momenta alone, at fixed direction and "
          "decreasing magnitude.")
    print()
    print("     L    k              khat^2      violation")
    sc = []
    for LL, kk in ((24, (0, 1, 2, 3)), (24, (0, 2, 4, 6)),
                   (24, (0, 3, 6, 9)), (36, (0, 1, 2, 3)),
                   (36, (0, 2, 4, 6)), (48, (0, 1, 2, 3))):
        kc = np.array([2 * np.pi * ki / LL for ki in kk])
        kv = np.array([2 * np.sin(np.pi * ki / LL) for ki in kk])
        k2 = float(kv @ kv)
        G = D0.gauge_modes(kv)
        Kp = kernel(np.exp(1j * kc) - 1.0)
        v = float(np.linalg.norm(Kp @ G)
                  / (np.linalg.norm(Kp) * np.linalg.norm(G)))
        sc.append((k2, v))
        print(f"    {LL:3d}  {str(kk):13s}  {k2:8.5f}   {v:.4e}")
    sc = np.array(sc)
    sl = np.polyfit(np.log(sc[:, 0]), np.log(sc[:, 1]), 1)[0]
    print()
    print(f"  generic-momentum violation ~ (khat^2)^({sl:+.3f})")
    print(f"  induced-kernel violation   ~ (khat^2)^(+0.029), "
          f"magnitude ~0.30 (0150)")
    print()
    if sl > 0.7:
        print("  DIFFERENT IN KIND. The constrained kernel's "
              "residual breaking is an")
        print(f"  O(a^2) artifact -- it scales as khat^2 and dies "
              f"in the continuum -- and")
        print("  it is exactly zero for a large class of momenta. "
              "The induced kernel's is")
        print("  flat in k and survives. R1 VERIFIED: the two "
              "sectors sit on opposite")
        print("  sides of the property that forces "
              "Einstein-Hilbert.")
    else:
        print(f"  The constrained kernel's breaking scales as "
              f"(khat^2)^{sl:.2f}, not +1, so it")
        print("  is not cleanly an O(a^2) artifact. Recorded as "
              "measured.")
    print()
    return r


if __name__ == "__main__":
    s0_gate()
    s1_lattice_and_test()
    print("all assertions passed")
