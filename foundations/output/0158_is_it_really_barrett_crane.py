"""0158 -- is the derived weight actually intertwiner-blind?

0166 identified the derived weight as a Barrett-Crane amplitude
because it sums over BALANCED representations, j+ = j-, which is how
Barrett and Crane impose simplicity. lucid 0051 then showed what
intertwiner-blindness would cost -- up to ln 6 = 1.79 nats per node at
this band limit -- and argued the capacity principle forbids paying
it.

Before porting that, a prior question, and it is the one that
actually decides the matter:

    Balanced representations are BC's SIMPLICITY condition.
    Intertwiner-independence is BC's DEFECT.
    They are not the same property, and 0166 conflated them.

In a lattice gauge theory the face weight is not the whole amplitude.
Expanding Z in characters, the LINK integrals

    integral dU  (x)_i D^{j_i}(U)

appear on their own, and Haar integration projects onto the invariant
subspace. In four dimensions each link is shared by four plaquettes,
so that projector lives in Inv(j1 (x) j2 (x) j3 (x) j4) -- a 4-valent
node. Whether the theory is intertwiner-blind is therefore not a
choice made in the weight at all. It is settled by the RANK of that
projector.

  s1  BUILD THE REPRESENTATIONS, gated: D^j must be a homomorphism
      and unitary.
  s2  THE LINK PROJECTOR's rank, against dim Inv computed by
      recoupling.
  s3  THE SPIN(4) CASE, and the verdict.
"""

import importlib.util
import itertools
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(158)


def su2(q):
    """unit quaternion -> SU(2)"""
    a, b, c, d = q
    return np.array([[a + 1j * d, b + 1j * c],
                     [-b + 1j * c, a - 1j * d]])


def haar(n=1):
    q = rng.standard_normal((n, 4))
    q /= np.linalg.norm(q, axis=1, keepdims=True)
    return [su2(x) for x in q]


def wigner_D(U, j):
    """spin-j rep as the 2j-fold symmetric power of the fundamental.

    Basis index k <-> e1^(n-k) e2^k.  Under U the basis vectors go to
    e1 -> a e1 + c e2 and e2 -> b e1 + d e2 (the COLUMNS of U), so the
    image of basis k is (a e1 + c e2)^(n-k) (b e1 + d e2)^k, and the
    convolution coefficient at m is the e2^m component -- i.e. the row
    index is the power of e2, not of e1.  Getting that backwards is
    what broke the first attempt.
    """
    n = int(round(2 * j))
    dim = n + 1
    a, b = U[0, 0], U[0, 1]
    c, d = U[1, 0], U[1, 1]
    D = np.zeros((dim, dim), complex)
    for k in range(dim):
        p1 = np.array([1.0 + 0j])
        for _ in range(n - k):
            p1 = np.convolve(p1, np.array([a, c]))
        p2 = np.array([1.0 + 0j])
        for _ in range(k):
            p2 = np.convolve(p2, np.array([b, d]))
        poly = np.convolve(p1, p2)
        for m in range(dim):
            D[m, k] = poly[m]
    w = np.array([np.sqrt(float(math.comb(n, i))) for i in range(dim)])
    return D * (w[None, :] / w[:, None])


def dim_inv(js):
    cur = {0.0: 1}
    for j in js:
        nxt = {}
        for k, cnt in cur.items():
            x = abs(k - j)
            while x <= k + j + 1e-9:
                nxt[round(x, 1)] = nxt.get(round(x, 1), 0) + cnt
                x += 1.0
        cur = nxt
    return cur.get(0.0, 0)


def s1_gate():
    print("== s1: the representations, gated ==")
    Us = haar(3)
    err_h = err_u = 0.0
    for j in (0.5, 1.0, 1.5, 2.0):
        A, B = Us[0], Us[1]
        DA, DB, DAB = wigner_D(A, j), wigner_D(B, j), wigner_D(A @ B, j)
        err_h = max(err_h, float(np.abs(DA @ DB - DAB).max()))
        err_u = max(err_u, float(np.abs(
            DA.conj().T @ DA - np.eye(DA.shape[0])).max()))
    print(f"  homomorphism  D(A)D(B) = D(AB):  max error {err_h:.2e}")
    print(f"  unitarity     D^dag D = I    :  max error {err_u:.2e}")
    assert err_h < 1e-9 and err_u < 1e-9
    print("  representations are exact")
    print()


def link_projector(js, nsamp=4000):
    """P = <(x)_i D^{j_i}(U)>_Haar -- the projector onto invariants."""
    dims = [int(round(2 * j)) + 1 for j in js]
    tot = int(np.prod(dims))
    P = np.zeros((tot, tot), complex)
    for U in haar(nsamp):
        M = np.array([[1.0 + 0j]])
        for j in js:
            M = np.kron(M, wigner_D(U, j))
        P += M
    return P / nsamp


def s2_rank():
    print("== s2: the rank of the link projector ==")
    print("  In 4D each link is shared by FOUR plaquettes, so the "
          "Haar integral over that")
    print("  link is a projector onto Inv(j1 (x) j2 (x) j3 (x) j4). "
          "If its rank is 1 the")
    print("  theory is intertwiner-blind. If it is dim Inv, the "
          "whole intertwiner space")
    print("  survives.")
    print()
    print("     four faces at a link     rank of projector    "
          "dim Inv    verdict")
    ok = True
    for js in ([0.5] * 4, [1.0] * 4, [0.5, 0.5, 1.0, 1.0],
               [1.0, 1.0, 1.0, 2.0]):
        P = link_projector(js)
        s = np.linalg.svd(P, compute_uv=False)
        rank = int((s > 0.5).sum())
        di = dim_inv(js)
        good = (rank == di)
        ok &= good
        print(f"    {str(js):24s}    {rank:2d}                "
              f"{di:2d}       {'ok' if good else 'MISMATCH'}")
    assert ok, "Haar projector rank does not match dim Inv"
    print()
    print("  THE RANK IS dim Inv, NOT 1. Haar integration over a "
          "link retains the ENTIRE")
    print("  intertwiner space. Nothing in the face weight can "
          "remove it -- the projector")
    print("  is generated by the measure, not chosen by the "
          "amplitude.")
    print()


def s3_verdict():
    print("== s3: Spin(4), and the verdict ==")
    print("  For the double copy the link carries (U+, U-) and the "
          "balanced condition ties")
    print("  j+ = j- FACE BY FACE. The link integral then runs over "
          "SU(2)+ x SU(2)- and")
    print("  factorises, so the surviving intertwiner space is "
          "Inv+ (x) Inv-.")
    print()
    for js in ([0.5] * 4, [1.0] * 4, [2.5] * 4):
        d = dim_inv(js)
        print(f"    faces {js[0]:4.1f}:  dim Inv = {d}, so Spin(4) "
              f"retains {d} x {d} = {d * d} intertwiner states "
              f"per link")
    print()
    print("  BARRETT-CRANE DOES SOMETHING THIS DOES NOT. Its vertex "
          "additionally projects")
    print("  that space onto a SINGLE element -- the Barrett-Crane "
          "intertwiner -- which is")
    print("  what makes its amplitude depend on the face labels "
          "alone, and what Alesci and")
    print("  Rovelli traced the wrong graviton propagator to.")
    print()
    print("  The derived weight imposes simplicity at the FACE "
          "level (balanced reps) and")
    print("  imposes nothing at the node. The node's intertwiners "
          "come from the Haar")
    print("  measure at full rank.")
    print()
    print("    SO 0166's IDENTIFICATION WAS TOO QUICK. Balanced "
          "representations are")
    print("    Barrett-Crane's SIMPLICITY CONDITION; "
          "intertwiner-independence is")
    print("    Barrett-Crane's DEFECT. This construction has the "
          "first and NOT the second.")
    print()
    print("  That does not make the graviton propagator right -- "
          "it has never been measured")
    print("  here. It removes the specific reason to expect it to "
          "be wrong.")
    print()


if __name__ == "__main__":
    s1_gate()
    s2_rank()
    s3_verdict()
    print("all assertions passed")
