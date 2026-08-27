"""0153 -- R2 and R3: source and response in the constrained sector.

R1 (0152) verified what 0160 could only force: the constrained
sector's kernel is Einstein-Hilbert exactly in the continuum, and on
the hypercubic lattice its diffeomorphism violation is an O(a^2)
artifact -- (khat^2)^{+1.12}, and exactly zero for momenta with at
most two distinct nonzero components -- against the induced kernel's
0.30, flat in k.

That retires 0162's conclusion. A fixed grid does NOT prevent
diffeomorphism invariance; it prevented it for the induced-matter
construction. So R4' is not the blocker, R2 and R3 are runnable on the
lattice we already have, and this runs them.

  R2  THE SOURCE. The constrained sector couples to matter the way
      GR does, T^{mu nu} h_{mu nu}, and the program's own matter
      supplies it through the map already built and gated in 0146.
  R3  THE RESPONSE. The static profile, read the same way item 4
      read it -- but in the sector where gravity lives.

  s1  the fast kernel, gated against 0152
  s2  R2: the source, and the gauge fixing it requires
  s3  R3: the static response profile, and gamma
"""

import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, tag):
    s = importlib.util.spec_from_file_location(
        tag, os.path.join(HERE, name))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


P = _load("0152_r1_plebanski_kernel.py", "p153")
S7 = _load("0147_the_missing_sign.py", "s153")
EPS, EB, WB, PAIRS = P.EPS, P.EB, P.WB, P.PAIRS
L = 24


def atens():
    """A[i,j] = Atens[i,j,rho] d_rho -- d enters linearly, so the
    whole k dependence is one contraction."""
    return 0.5 * np.einsum("mnrs,mbcd,inb,jscd->ijr",
                           EPS, EPS, EB, WB)


ATENS = atens()
_A, _B = P.blocks(np.array([1.0, 0, 0, 0]))
BPINV = np.linalg.pinv(_B, rcond=1e-10)


def kernel_fast(dvec):
    A = np.einsum("ijr,r->ij", ATENS, dvec)
    return -(A @ BPINV @ A.conj().T)


def dedonder(kv):
    """Hessian of sum_nu |k_mu h_{mu nu} - (1/2) k_nu tr h|^2."""
    def C(h):
        return kv @ h - 0.5 * kv * np.trace(h)
    H = np.zeros((10, 10))
    for a in range(10):
        for b in range(10):
            H[a, b] = float(C(EB[a]) @ C(EB[b])
                            + C(EB[b]) @ C(EB[a]))
    return H


def s1_gate():
    print("== s1: the fast kernel, gated ==")
    rng = np.random.default_rng(153)
    err = 0.0
    for _ in range(3):
        k = rng.standard_normal(4)
        err = max(err, float(np.abs(kernel_fast(1j * k)
                                    - P.kernel(1j * k)).max()))
    print(f"  fast vs 0152's construction: max difference "
          f"{err:.2e}")
    assert err < 1e-10
    c, r = P.fit_in_basis(kernel_fast(1j * np.array(
        [0.3, -0.7, 0.2, 0.5])), np.array([0.3, -0.7, 0.2, 0.5]))
    print(f"  and it is still Einstein-Hilbert: "
          f"{np.array2string(c, precision=5)}, residual {r:.1e}")
    print()


def s2_source():
    print("== R2: the source ==")
    print("  In the constrained sector the metric IS h, so matter "
          "couples the way GR")
    print("  says: T^{mu nu} h_{mu nu}. The program's own matter "
          "supplies that through")
    print("  the map built and gated in 0146 -- W = exp(2A), "
          "A = ((tr h) I - 2h)/2 --")
    print("  and a static mass is T = diag(1,0,0,0).")
    print()
    j = S7.source_h()
    print(f"  source vector in the EB basis: "
          f"{np.array2string(j, precision=3)}")
    print()
    print("  The kernel annihilates gauge modes (that is R1), so "
          "it is singular and the")
    print("  response is defined only modulo a gauge. Fixed the "
          "standard way, with a")
    print("  de Donder term. The source is conserved for a static "
          "mass -- k_mu T^{mu nu}")
    print("  = 0 when k_0 = 0 -- so the physics does not depend "
          "on that choice.")
    print()
    return j


def s3_response(j):
    print("== R3: the static response, and gamma ==")
    resp = np.zeros((L, L, L, 10))
    scale = None
    for a in range(L):
        for b in range(L):
            for c in range(L):
                if a == b == c == 0:
                    continue
                kk = (0, a, b, c)
                kc = np.array([2 * np.pi * x / L for x in kk])
                kv = np.array([2 * np.sin(np.pi * x / L)
                               for x in kk])
                K = np.real(kernel_fast(np.exp(1j * kc) - 1.0))
                if scale is None:
                    scale = np.abs(K).max()
                Kg = K + 1.0 * dedonder(kv)
                try:
                    resp[a, b, c] = np.linalg.solve(Kg, -j)
                except np.linalg.LinAlgError:
                    resp[a, b, c] = np.linalg.lstsq(
                        Kg, -j, rcond=None)[0]
    h = np.einsum("abcz,zmn->abcmn", resp, EB)
    hx = np.real(np.fft.ifftn(h, axes=(0, 1, 2)))
    r = np.arange(1, L // 2)
    h0 = hx[r, 0, 0, 0, 0]
    hs = (hx[r, 0, 0, 1, 1] + hx[r, 0, 0, 2, 2]
          + hx[r, 0, 0, 3, 3]) / 3.0
    g = -hs / h0
    keep = np.abs(h0) > 0.02 * abs(h0[0])
    print("     r      h_00           h_spatial       gamma")
    for i in range(len(r)):
        tag = "" if keep[i] else "  (outside window)"
        print(f"    {r[i]:2d}   {h0[i]:+.5e}   {hs[i]:+.5e}   "
              f"{g[i]:+.5f}{tag}")
    gk = g[keep]
    print()
    print(f"  window r = {r[keep].min()}..{r[keep].max()}:  "
          f"gamma = {gk.mean():+.5f}, spread "
          f"{gk.max() - gk.min():.5f}")
    print()
    # the profile itself
    def fit_n(x, y):
        best, bn = np.inf, np.nan
        for n in np.linspace(0.2, 4.0, 761):
            X = np.vstack([x ** (-n), np.ones_like(x)]).T
            bb, *_ = np.linalg.lstsq(X, y, rcond=None)
            e = np.sum((X @ bb - y) ** 2)
            if e < best:
                best, bn = e, n
        return bn
    rr = r[keep].astype(float)
    n = fit_n(rr, h0[keep])
    print(f"  static profile h_00 ~ A/r^n + C :  n = {n:.4f}"
          f"   (Newton needs 1)")
    print()
    ok = abs(gk.mean() - 1) < 0.1 and abs(n - 1) < 0.15
    if ok:
        print("  R3 DONE. In the sector where gravity lives, the "
              "static response to a")
        print(f"  static mass is Newtonian (n = {n:.3f}) and "
              f"gamma = {gk.mean():+.4f}.")
        print("  Light deflection "
              f"(1+gamma)/2 = {(1 + gk.mean()) / 2:.4f} x GR, "
              f"with NO counterterms:")
        print("  no cosmological constant to cancel, no graviton "
              "mass to subtract. Both")
        print("  were artifacts of working in the induced sector, "
              "where diffeomorphism")
        print("  invariance was absent to forbid them.")
    else:
        print(f"  Recorded as measured: n = {n:.3f}, "
              f"gamma = {gk.mean():+.4f}.")
    print()
    return float(gk.mean()), float(n)


if __name__ == "__main__":
    s1_gate()
    j = s2_source()
    s3_response(j)
    print("all assertions passed")
