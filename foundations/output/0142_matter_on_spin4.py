"""0142 -- item 3: the source (T = Fisher) as lattice code.

lucid 0049 corrected the scope. The masslessness of the trust channel
in 0113/0125 follows from a UNIFORM lambda shifting ln det by exactly
a constant -- a property of MATTER's determinant. A uniform lambda on
the gauge weight only rescales beta, and the free energy is not linear
in beta. So item 3 is not "insert an operator we already have"; it is
put matter on the Spin(4) lattice.

THE MATTER. The natural field for Spin(4) = SU(2)+ x SU(2)- is the
bifundamental (2,2) -- which is a real 4-vector of SO(4), i.e. a
QUATERNION per site, in the arithmetic this program already runs on:

    (D_mu phi)(x) = U+_mu(x) phi(x+mu) U-_mu(x)^dagger - phi(x)
                  = R_mu(x) phi(x+mu) - phi(x),   R in SO(4).

THE SOURCE. Weight the links, w_l = e^{2 lambda_l}, and integrate the
matter out: Gamma[lambda] = (1/2) ln det' (D^T W D). Then

    Gamma''[lambda] = sum_{l,m} ||B_lm||_F^2 (lambda_l - lambda_m)^2,
    B = D (D^T D)^+ D^T = the orthogonal projector onto range(D),

which is 0125's identity generalised to a multi-component field
(B_lm^2 -> the Frobenius norm of the 4x4 block). It is PSD with
kernel exactly the constants -- FOR ANY D. So masslessness survives
quantisation exactly, and that is checked here in a real gauge
background rather than argued.

  s1  THE FIELD, gated: the 4x4 rotation blocks must reproduce
      quaternion multiplication, and R must be in SO(4).
  s2  THE THEOREM IN A QUANTUM BACKGROUND: uniform lambda gives
      exactly zero. Not approximately.
  s3  THE STIFFNESS RATIO p_quantum / p_flat -- what the quantum
      background does to G.
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


K = _load("0134_the_spin4_kernel.py", "k142")
M = K.M132
L = 4
NCFG = 24


def Lmat(a):
    """matrix of q -> a*q"""
    a0, a1, a2, a3 = [a[..., i] for i in range(4)]
    z = np.stack
    return z([z([a0, -a1, -a2, -a3], -1),
              z([a1, a0, -a3, a2], -1),
              z([a2, a3, a0, -a1], -1),
              z([a3, -a2, a1, a0], -1)], -2)


def Rmat(b):
    """matrix of q -> q*b"""
    b0, b1, b2, b3 = [b[..., i] for i in range(4)]
    z = np.stack
    return z([z([b0, -b1, -b2, -b3], -1),
              z([b1, b0, b3, -b2], -1),
              z([b2, -b3, b0, b1], -1),
              z([b3, b2, -b1, b0], -1)], -2)


def rot(Up, Um):
    """R = L(U+) . R(conj(U-)) : the SO(4) block of a link"""
    return Lmat(Up) @ Rmat(M.qinv(Um))


def s1_gate():
    print("== s1: the bifundamental field, gated ==")
    rng = np.random.default_rng(142)
    a = rng.standard_normal((5, 4))
    a /= np.linalg.norm(a, axis=-1, keepdims=True)
    b = rng.standard_normal((5, 4))
    b /= np.linalg.norm(b, axis=-1, keepdims=True)
    q = rng.standard_normal((5, 4))
    direct = M.qmul(M.qmul(a, q), M.qinv(b))
    viamat = np.einsum("nij,nj->ni", rot(a, b), q)
    err = float(np.abs(direct - viamat).max())
    R = rot(a, b)
    orth = float(np.abs(np.einsum("nij,nkj->nik", R, R)
                        - np.eye(4)).max())
    det = np.linalg.det(R)
    print(f"  R phi  vs  U+ phi U-^dag :  max error {err:.2e}")
    print(f"  R R^T = I               :  max error {orth:.2e}")
    print(f"  det R                   :  "
          f"{det.min():.6f} .. {det.max():.6f}")
    assert err < 1e-12 and orth < 1e-12
    assert np.abs(det - 1).max() < 1e-12
    print("  the link acts on matter as an exact SO(4) rotation, "
          "which is what a")
    print("  (2,2) of Spin(4) must do")
    print()


def build_D(Up, Um, lat):
    """D : site-field (V,4) -> link-field (V,4,4). Dense, real."""
    V, up = lat["V"], lat["up"]
    D = np.zeros((4 * V * 4, V * 4))
    for mu in range(4):
        R = rot(Up[mu], Um[mu])                    # (V,4,4)
        for x in range(V):
            r0 = (mu * V + x) * 4
            D[r0:r0 + 4, x * 4:x * 4 + 4] -= np.eye(4)
            y = up[mu][x]
            D[r0:r0 + 4, y * 4:y * 4 + 4] += R[x]
    return D


def projector(D):
    """B = orthogonal projector onto range(D), via QR -- stable
    where forming (D^T D)^-1 is not."""
    Q, _ = np.linalg.qr(D)
    s = np.linalg.svd(D, compute_uv=False)
    rank = int((s > s.max() * 1e-10).sum())
    U, _, _ = np.linalg.svd(D, full_matrices=False)
    U = U[:, :rank]
    return U @ U.T


def cmat(B, V):
    """C_lm = ||B_lm||_F^2 over 4x4 blocks -> (4V, 4V)"""
    nl = 4 * V
    Bb = B.reshape(nl, 4, nl, 4)
    return np.einsum("libj->lb", Bb ** 2)


def quad(C, lam):
    """sum_lm C_lm (lam_l - lam_m)^2"""
    return float(2 * (lam @ (C.sum(1) * lam) - lam @ (C @ lam)))


def link_phase(lat, k, V):
    """plane wave on links, indexed by the link's base site"""
    co = np.array(np.unravel_index(np.arange(V), (L,) * 4)).T
    ph = np.cos(co @ k)
    return np.tile(ph, 4)


def configs(n=NCFG):
    lat, up, dn = K.lat_arrays(L)
    V = lat["V"]
    lp, lm = K.fresh(L)
    rs = K.seed(1142)
    sig = 0.08
    for s in range(600):
        a, t = K.csweeps(lp, lm, up, dn, V, 1, sig, rs)
        if s < 400:
            r = a / max(t, 1)
            sig *= 1.06 if r > 0.45 else (0.94 if r < 0.35 else 1)
            sig = float(np.clip(sig, 0.005, 1.0))
    out = []
    for _ in range(n):
        K.csweeps(lp, lm, up, dn, V, 12, sig, rs)
        # as_links returns VIEWS into the live buffer -- copy, or
        # every stored configuration is the last one
        out.append(([u.copy() for u in K.as_links(lp, V)],
                    [u.copy() for u in K.as_links(lm, V)]))
    return lat, out


def s2_s3(lat, cfgs):
    V = lat["V"]
    one = [np.tile([1.0, 0, 0, 0], (V, 1)) for _ in range(4)]
    Cf = cmat(projector(build_D(one, one, lat)), V)

    print("== s2: the masslessness theorem, in a quantum "
          "background ==")
    print("  A uniform lambda must give exactly zero -- not "
          "approximately zero.")
    uni = np.ones(4 * V)
    Cq0 = cmat(projector(build_D(*cfgs[0], lat)), V)
    print(f"    flat background      Q(uniform) = "
          f"{quad(Cf, uni):+.3e}")
    print(f"    quantum background   Q(uniform) = "
          f"{quad(Cq0, uni):+.3e}")
    assert abs(quad(Cq0, uni)) < 1e-8
    assert abs(quad(Cf, uni)) < 1e-8
    print("  Exactly zero in both. The kernel of the induced scale "
          "action is the")
    print("  constants, in a real gauge configuration. THE TRUST "
          "CHANNEL IS MASSLESS")
    print("  IN THE QUANTUM THEORY, not just in the free "
          "background -- which is what")
    print("  item 4's 1/r rests on.")
    print()

    print("== s3: the stiffness in the quantum background ==")
    ks = [np.array([2 * np.pi / L, 0, 0, 0]),
          np.array([0, 2 * np.pi / L, 0, 0]),
          np.array([0, 0, 2 * np.pi / L, 0])]
    rats = []
    for ci, cf in enumerate(cfgs):
        C = cmat(projector(build_D(*cf, lat)), V)
        r = [quad(C, link_phase(lat, k, V))
             / quad(Cf, link_phase(lat, k, V)) for k in ks]
        rats.append(np.mean(r))
    rats = np.array(rats)
    m, e = rats.mean(), rats.std(ddof=1) / np.sqrt(len(rats))
    assert rats.std() > 1e-12, (
        "every configuration gave the same ratio -- check that the "
        "stored configurations are copies, not views")
    print(f"  L = {L}, {len(cfgs)} configurations, lowest lattice "
          f"momentum, 3 directions")
    print(f"  p_quantum / p_flat = {m:.5f} +- {e:.5f}   (spread over configs {rats.std(ddof=1):.5f})")
    p_flat = 0.154932
    print(f"  p_flat  (0113, 1/L^2 extrapolated) = {p_flat:.6f} "
          f"per field")
    print(f"  p_quantum                          = "
          f"{m * p_flat:.6f} +- {e * p_flat:.6f}")
    print()
    if abs(m - 1) < 3 * e:
        print("  CONSISTENT WITH 1. The quantum background does "
              "not change the induced")
        print("  stiffness at this volume and coupling -- which is "
              "what a nearly frozen")
        print("  lattice (plaquette 0.957) should do, and is a "
              "consistency check rather")
        print("  than a new number.")
    else:
        d = 100 * (m - 1)
        print(f"  THE QUANTUM BACKGROUND MOVES THE STIFFNESS BY "
              f"{d:+.2f}%.")
        print(f"  G = 1/(4 pi p) therefore moves by "
              f"{100 * (1 / m - 1):+.2f}%, and l_P = sqrt(G) by "
              f"{100 * (m ** -0.5 - 1):+.2f}%.")
    print()
    return m, e


if __name__ == "__main__":
    s1_gate()
    lat, cfgs = configs()
    s2_s3(lat, cfgs)
    print("all assertions passed")
