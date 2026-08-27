"""0156 -- R7: matter content, and why the constrained sector can
carry fermions while the induced one cannot.

0127's bar, row (E): "coupling closed as a formula and measured;
fields and content still absent -- NO SPINORS." That has stood open
since. It closes here, and the reason it closes is the same structural
fact that decided item 6.

A spinor cannot be parallel transported by a metric. It needs an
element of the SPIN group. In the induced-matter formulation the only
geometric variable is W = sqrt(g) g^{mu nu} -- a symmetric tensor,
with nothing that acts on a spinor index. In the constrained sector
the variables are the tetrad and the connection, and the connection
acts on spinors directly.

And this program's lattice already has it: Spin(4) = SU(2)+ x SU(2)-
IS the spin group, and the link variables U+ and U- are its elements.
A left-handed Weyl spinor is the (2,1); the link U+ acts on it with no
new field introduced anywhere.

  s1  THE REPRESENTATION. Clifford algebra, and the check that the
      lattice's own links act on spinors as the spin connection --
      i.e. that the vector rep the plaquettes already use is the
      square of the spinor rep.
  s2  THE DIRAC OPERATOR: gauge covariance and the free dispersion.
  s3  WHAT THE INDUCED SECTOR CANNOT DO.
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


F = _load("0142_matter_on_spin4.py", "f156")
M = F.M

SIG = [np.eye(2, dtype=complex),
       np.array([[0, 1], [1, 0]], complex),
       np.array([[0, -1j], [1j, 0]], complex),
       np.array([[1, 0], [0, -1]], complex)]


def qmat(q):
    """unit quaternion -> SU(2) matrix"""
    return q[0] * SIG[0] - 1j * (q[1] * SIG[1] + q[2] * SIG[2]
                                 + q[3] * SIG[3])


def gamma():
    """Euclidean 4x4 gammas from the chiral blocks."""
    s = [SIG[0], -1j * SIG[1], -1j * SIG[2], -1j * SIG[3]]
    sb = [SIG[0], 1j * SIG[1], 1j * SIG[2], 1j * SIG[3]]
    G = []
    for m in range(4):
        g = np.zeros((4, 4), complex)
        g[:2, 2:] = s[m]
        g[2:, :2] = sb[m]
        G.append(g)
    return G


GAM = gamma()


def s1_representation():
    print("== s1: the representation ==")
    err = 0.0
    for a in range(4):
        for b in range(4):
            ac = GAM[a] @ GAM[b] + GAM[b] @ GAM[a]
            err = max(err, float(np.abs(
                ac - 2 * (a == b) * np.eye(4)).max()))
    print(f"  Clifford algebra {{gamma_a, gamma_b}} = 2 delta_ab :  "
          f"max error {err:.2e}")
    assert err < 1e-12
    print()
    print("  Now the fact that matters: the VECTOR representation "
          "the plaquettes")
    print("  already use is the SQUARE of the spinor one. For a "
          "link (U+, U-),")
    print("      R = L(U+) . R(conj(U-))  acting on a quaternion "
          "(0142's SO(4) block)")
    print("  must equal the vector rep built from the same U+, U- "
          "acting on spinors.")
    rng = np.random.default_rng(156)
    err2 = 0.0
    for _ in range(6):
        a = rng.standard_normal(4)
        a /= np.linalg.norm(a)
        b = rng.standard_normal(4)
        b /= np.linalg.norm(b)
        R = F.rot(a[None], b[None])[0]              # 4x4 real SO(4)
        Ua, Ub = qmat(a), qmat(b)
        # vector rep from spinors: v_mu -> tr(sigma_mu U v.sigmabar U'^dag)/2
        V = np.zeros((4, 4))
        sb = [SIG[0], 1j * SIG[1], 1j * SIG[2], 1j * SIG[3]]
        sf = [SIG[0], -1j * SIG[1], -1j * SIG[2], -1j * SIG[3]]
        for mu in range(4):
            for nu in range(4):
                V[mu, nu] = np.real(
                    0.5 * np.trace(sb[mu] @ Ua @ sf[nu]
                                   @ Ub.conj().T))
        err2 = max(err2, float(np.abs(V - R).max()))
    print(f"  max difference between the two constructions: "
          f"{err2:.2e}")
    assert err2 < 1e-12
    print()
    print("  THE LATTICE ALREADY CARRIES THE SPIN CONNECTION. The "
          "link variables are")
    print("  elements of Spin(4); the SO(4) rotation the "
          "plaquettes use is their image")
    print("  in the vector rep. A Weyl spinor is the (2,1) and U+ "
          "transports it. No new")
    print("  field is introduced anywhere -- the spin structure "
          "was there from 0132.")
    print()


def weyl_spectrum(L, mass=0.0):
    """free naive Weyl operator eigenvalues on an L^4 lattice, in
    momentum space."""
    ax = 2 * np.pi * np.fft.fftfreq(L)
    g = np.meshgrid(*([ax] * 4), indexing="ij")
    out = []
    sf = [SIG[0], -1j * SIG[1], -1j * SIG[2], -1j * SIG[3]]
    for idx in np.ndindex(*(L,) * 4):
        k = np.array([g[d][idx] for d in range(4)])
        D = sum(1j * np.sin(k[m]) * sf[m] for m in range(4))
        D = D + mass * SIG[0]
        out.append(np.linalg.svd(D, compute_uv=False))
    return np.array(out)


def spin_rep(qp, qm):
    """Spin(4) element in the Dirac (2,1)+(1,2) representation."""
    S = np.zeros((4, 4), complex)
    S[:2, :2] = qmat(qp)
    S[2:, 2:] = qmat(qm)
    return S


def s2_dirac():
    print("== s2: the Dirac operator ==")
    print("  THE INTERTWINER. The one identity everything rests "
          "on:")
    print("      S gamma^a S^dag = Lambda(S)^a_b gamma^b,")
    print("  i.e. rotating a spinor by a link and rotating a "
          "vector by the SAME link")
    print("  are the same operation. Without it the Dirac operator "
          "is not covariant.")
    rng = np.random.default_rng(1156)
    err = 0.0
    for _ in range(6):
        a = rng.standard_normal(4); a /= np.linalg.norm(a)
        b = rng.standard_normal(4); b /= np.linalg.norm(b)
        S = spin_rep(a, b)
        Lam = F.rot(a[None], b[None])[0]
        for m in range(4):
            lhs = S @ GAM[m] @ S.conj().T
            rhs = sum(Lam[n, m] * GAM[n] for n in range(4))
            err = max(err, float(np.abs(lhs - rhs).max()))
    print(f"  max error over random links and all gammas: "
          f"{err:.2e}")
    assert err < 1e-12
    print()
    print("  THE COVARIANCE TEST, and the instructive way it "
          "fails first.")
    L = 4
    lat = M.mklat(L)
    V = lat["V"]
    Up = [rng.standard_normal((V, 4)) for _ in range(4)]
    Up = [u / np.linalg.norm(u, axis=-1, keepdims=True) for u in Up]
    Um = [rng.standard_normal((V, 4)) for _ in range(4)]
    Um = [u / np.linalg.norm(u, axis=-1, keepdims=True) for u in Um]

    def dirac(e, Up, Um):
        """e[x, mu, a] : tetrad.  D maps site spinors to site
        spinors, hopping with the Spin(4) link."""
        D = np.zeros((4 * V, 4 * V), complex)
        for mu in range(4):
            for x in range(V):
                y = lat["up"][mu][x]
                gm = sum(e[x, mu, a] * GAM[a] for a in range(4))
                blk = 0.5 * gm @ spin_rep(Up[mu][x], Um[mu][x])
                D[4 * x:4 * x + 4, 4 * y:4 * y + 4] += blk
                D[4 * y:4 * y + 4, 4 * x:4 * x + 4] -= \
                    blk.conj().T
        return D

    e0 = np.zeros((V, 4, 4))
    for x in range(V):
        e0[x] = np.eye(4)
    w0 = np.linalg.svd(dirac(e0, Up, Um), compute_uv=False)

    G = [(lambda q: q / np.linalg.norm(q))(rng.standard_normal(4))
         for _ in range(V)]
    H = [(lambda q: q / np.linalg.norm(q))(rng.standard_normal(4))
         for _ in range(V)]

    def rot_links():
        UP, UM = [], []
        for mu in range(4):
            ap = np.zeros_like(Up[mu]); am = np.zeros_like(Um[mu])
            for x in range(V):
                y = lat["up"][mu][x]
                ap[x] = M.qmul(M.qmul(G[x][None], Up[mu][x][None]),
                               M.qinv(G[y][None]))[0]
                am[x] = M.qmul(M.qmul(H[x][None], Um[mu][x][None]),
                               M.qinv(H[y][None]))[0]
            UP.append(ap); UM.append(am)
        return UP, UM

    UPg, UMg = rot_links()
    w_bad = np.linalg.svd(dirac(e0, UPg, UMg), compute_uv=False)
    d_bad = float(np.abs(np.sort(w0) - np.sort(w_bad)).max())
    print(f"    links rotated, tetrad left flat:  spectrum moves "
          f"by {d_bad:.3e}")

    eg = np.zeros_like(e0)
    for x in range(V):
        Lam = F.rot(G[x][None], H[x][None])[0]
        eg[x] = e0[x] @ Lam.T
    w_ok = np.linalg.svd(dirac(eg, UPg, UMg), compute_uv=False)
    d_ok = float(np.abs(np.sort(w0) - np.sort(w_ok)).max())
    print(f"    links AND tetrad rotated:         spectrum moves "
          f"by {d_ok:.3e}")
    print("    (the index placement in the tetrad rotation is "
          "fixed by the intertwiner")
    print("     convention verified above, not chosen -- the "
          "other placement moves the")
    print("     spectrum and is simply wrong)")
    assert d_bad > 1e-4 and d_ok < 1e-9
    print()
    print("  THAT CONTRAST IS R7's WHOLE POINT. Rotating the "
          "connection alone breaks the")
    print("  operator; rotating the connection together with the "
          "TETRAD leaves it exactly")
    print("  invariant. The tetrad is not a convenience -- it is "
          "the object that makes")
    print("  a spinor's index and a spacetime index commensurable, "
          "and only the")
    print("  constrained sector has one.")
    print()
    sp = weyl_spectrum(8)
    zero = int((sp.min(axis=1) < 1e-9).sum())
    print(f"  free spectrum on 8^4: {zero} exact zero modes -- the "
          f"naive discretisation's")
    print(f"  2^4 = 16 doublers. Nielsen-Ninomiya is a theorem and "
          f"applies here as")
    print(f"  anywhere; a Wilson or overlap term removes them and "
          f"is orthogonal to")
    print(f"  anything this program claims.")
    print()
    return zero


def s3_what_the_induced_sector_cannot_do():
    print("== s3: what the induced sector cannot do ==")
    print("  The induced formulation's only geometric variable is")
    print("      W_{mu nu} = sqrt(g) g^{mu nu},")
    print("  a symmetric tensor. Count what acts on a spinor "
          "index: nothing. A symmetric")
    print("  tensor has no action on the (2,1) of Spin(4) -- "
          "there is no product of")
    print("  W's that is an element of SU(2).")
    print()
    print("  That is not a difficulty to be worked around; it is "
          "the standard reason")
    print("  general relativity is written in first-order form "
          "when fermions are")
    print("  present. The metric formulation has to REINTRODUCE a "
          "tetrad to couple")
    print("  spinors, and once reintroduced, that tetrad is the "
          "constrained sector's")
    print("  variable.")
    print()
    print("  So R7 lands the same way item 6 did, and from the "
          "same structure:")
    print("    * induced sector: no diffeomorphism invariance "
          "(0150), gamma = -1,")
    print("      cannot carry spinors (here);")
    print("    * constrained sector: invariant to O(a^2) (0152), "
          "gamma = +1 (0153),")
    print("      carries spinors with the link variables it "
          "already had (s1).")
    print()
    print("  Bar row (E) moves from 'no spinors' to 'spinors "
          "constructed and gated, on")
    print("  the lattice's own spin structure'. What remains "
          "under (E) is content --")
    print("  which fermions, how many, and their charges -- not "
          "the ability to have any.")
    print()


if __name__ == "__main__":
    s1_representation()
    s2_dirac()
    s3_what_the_induced_sector_cannot_do()
    print("all assertions passed")
