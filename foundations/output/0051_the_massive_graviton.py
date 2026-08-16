"""The graviton's mass, the price as a kernel, and the shared frame.

0055's three opens.  The first turns up the quantum arc's most
consequential structural fact -- the lattice graviton is MASSIVE off
criticality, so the long-range (Newtonian) limit is a critical point
-- and the second gives the simplicity price a one-line geometric
meaning that supersedes the Pfaffian bookkeeping.

  s1  THE GRAVITON IS MASSIVE; NEWTON LIVES AT A CRITICAL POINT.
      The curvature quantum carries the price V per quantum (0055:
      V = 2 log N for geometric curvature) and hops with amplitude
      t (the electric term).  Its pair gap is Delta(t) = 2V - 4t,
      measured on a long ring:

        t/t_c      0.20    0.60    0.90    1.00    1.10
        gap       +3.52   +1.76   +0.44   +0.0005  -0.44     (N = 3)
        gap       +5.15   +2.58   +0.64   +0.0008  -0.64     (N = 5)

      giving three phases:
        t < t_c : GAPPED -- a massive quantum, so the force it
                  mediates is Yukawa, range 1/Delta;
        t = t_c : CRITICAL -- the gap closes, the quantum is
                  massless and the force becomes long-ranged;
        t > t_c : CONDENSED -- the flat vacuum is unstable to
                  curvature-pair creation.
      The critical coupling is exactly t_c = V/2 = log N.  So the
      theory has a Newtonian limit only AT CRITICALITY -- which is
      how a lattice theory acquires a continuum limit at all -- and
      the critical coupling is set by the level.  This is the
      honest quantum status of 0036's classical Newton: the
      classical chain gets 1/r because it already sits at the
      continuum point; the quantum model must be TUNED there.

  s2  THE PRICE COUNTS WHAT THE CURVATURE LEAVES ALONE.  The
      simplicity kernel of 0055 factorizes exactly:

        K(F) = N^4 * |ker F|,   ker F = { b : eps_IJKL b^J F^KL = 0 }

      -- the null space of the curvature viewed as a map on frame
      vectors.  Measured at N = 3:
        flat            |ker| = N^4   (leaves everything alone)
        simple (Pf = 0) |ker| = N^2   (acts in a plane, leaves 2)
        non-simple      |ker| = N^0   (acts on everything)
      So 0055's 0 / 2 log N / 4 log N hierarchy is the codimension
      of the kernel, and "geometric" means "acts in a plane."  The
      Pfaffian was the symptom; the rank is the cause.

  s3  THE SHARED FRAME CORRELATES NEIGHBOURS.  Two plaquettes
      sharing a frame vector have the joint weight

        K2(F1, F2) = N^8 * | ker F1  intersect  ker F2 |

      so their prices are NOT independent: measured mutual
      information 0.0265 bits between adjacent plaquette costs
      (independent plaquettes would give exactly 0).  Cheap-
      together means the two curvature planes share an untouched
      direction -- the lattice's version of "all the curvature
      2-forms come from one tetrad."  0053 s4 saw this correlation
      in the budgets; here it is resolved into its geometric cause.

Run directly for the verification suite.
"""

from __future__ import annotations

import itertools
import math
import random
from collections import Counter

PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


# =====================================================================
# 1. the graviton's mass
# =====================================================================

def pair_gap(V, t, L=200, iters=20000):
    """Ground energy of a +/- curvature pair at zero CoM momentum:
    a 1D chain in the relative coordinate with hopping -2t."""
    n = L - 1
    hop = -2 * t
    diag = [2 * V] * n
    shift = 4 * abs(hop) + 2 * V + 5.0
    v = [math.sin(math.pi * (i + 1) / (n + 1)) for i in range(n)]
    for _ in range(iters):
        w = [0.0] * n
        for i in range(n):
            w[i] += (shift - diag[i]) * v[i]
            if i > 0:
                w[i] += -hop * v[i - 1]
            if i < n - 1:
                w[i] += -hop * v[i + 1]
        nr = math.sqrt(sum(x * x for x in w))
        v = [x / nr for x in w]
    Hv = [0.0] * n
    for i in range(n):
        Hv[i] += diag[i] * v[i]
        if i > 0:
            Hv[i] += hop * v[i - 1]
        if i < n - 1:
            Hv[i] += hop * v[i + 1]
    return sum(v[i] * Hv[i] for i in range(n))


def verify_graviton_mass() -> None:
    for N in (3, 5):
        V = 2 * math.log(N)
        tc = V / 2
        print(f"    N = {N}: price V = 2 log N = {V:.4f}, "
              f"t_c = V/2 = {tc:.4f}")
        gaps = {}
        for ratio in (0.20, 0.60, 0.90, 1.00, 1.10):
            g = pair_gap(V, ratio * tc)
            gaps[ratio] = g
            if g > 1e-3:
                state = "GAPPED (massive, Yukawa range 1/gap)"
            elif abs(g) <= 1e-2:
                state = "CRITICAL (massless, long range)"
            else:
                state = "CONDENSED (flat vacuum unstable)"
            print(f"      t/t_c = {ratio:.2f}: gap = {g:+.5f}   "
                  f"{state}")
        assert gaps[0.20] > gaps[0.60] > gaps[0.90] > 0
        assert abs(gaps[1.00]) < 1e-2, gaps[1.00]
        assert gaps[1.10] < -1e-2, gaps[1.10]
    print()
    print("  THE LATTICE GRAVITON IS MASSIVE OFF CRITICALITY.  The")
    print("  force it mediates is Yukawa with range 1/gap; the")
    print("  long-range Newtonian limit exists only AT t_c = log N,")
    print("  where the gap closes.  That is how a lattice theory")
    print("  acquires a continuum limit -- and it is the honest")
    print("  quantum status of 0036's classical Newton: the")
    print("  classical chain already sits at the continuum point,")
    print("  the quantum model must be tuned there.")


# =====================================================================
# 2. the price counts what the curvature leaves alone
# =====================================================================

def eps4(i, j, k, l):
    p = [i, j, k, l]
    if len(set(p)) < 4:
        return 0
    s = 1
    for x in range(4):
        for y in range(x + 1, 4):
            if p[x] > p[y]:
                s = -s
    return s


def m_of(b, F, N):
    """m^I = eps_IJKL b^J F^KL (mod N)."""
    d = dict(zip(PAIRS, F))
    out = []
    for I in range(4):
        v = 0
        for J in range(4):
            for (K, L) in PAIRS:
                e = eps4(I, J, K, L)
                if e:
                    v += e * b[J] * d[(K, L)]
        out.append(v % N)
    return tuple(out)


def kernel(F, N, vecs):
    return {b for b in vecs if all(x == 0 for x in m_of(b, F, N))}


def pfaffian(F, N):
    d = dict(zip(PAIRS, F))
    return (d[(0, 1)] * d[(2, 3)] - d[(0, 2)] * d[(1, 3)]
            + d[(0, 3)] * d[(1, 2)]) % N


def verify_kernel_price() -> None:
    N = 3
    vecs = list(itertools.product(range(N), repeat=4))
    tally = Counter()
    for F in itertools.product(range(N), repeat=6):
        k = len(kernel(F, N, vecs))
        lab = ("flat" if all(x == 0 for x in F)
               else ("simple (Pf = 0)" if pfaffian(F, N) == 0
                     else "non-simple"))
        tally[(lab, k)] += 1
    seen = {}
    for (lab, k), c in sorted(tally.items(), key=lambda x: -x[0][1]):
        dim = round(math.log(k) / math.log(N))
        seen[lab] = dim
        print(f"    {lab:16s}: |ker F| = {k:3d} = N^{dim}, count "
              f"{c:4d}  ->  K = N^{4 + dim}")
    assert seen["flat"] == 4
    assert seen["simple (Pf = 0)"] == 2
    assert seen["non-simple"] == 0
    print()
    print("  K(F) = N^4 * |ker F| EXACTLY, so 0055's 0 / 2 log N /")
    print("  4 log N hierarchy is the CODIMENSION OF THE KERNEL.")
    print("  Flat curvature leaves every direction alone; simple")
    print("  curvature acts in a plane and leaves two; non-simple")
    print("  curvature acts on everything and leaves none.  The")
    print("  price counts what the curvature leaves alone -- and")
    print("  'geometric' means 'acts in a plane'.  The Pfaffian was")
    print("  the symptom; the rank is the cause.")


# =====================================================================
# 3. the shared frame correlates neighbours
# =====================================================================

def verify_shared_frame() -> None:
    N = 3
    vecs = list(itertools.product(range(N), repeat=4))
    allF = list(itertools.product(range(N), repeat=6))
    random.seed(4)
    sample = random.sample(allF, 60)
    kers = {F: kernel(F, N, vecs) for F in sample}
    P, PA, PB = Counter(), Counter(), Counter()
    Z = 0.0
    for F1 in sample:
        for F2 in sample:
            w = len(kers[F1] & kers[F2])
            if w == 0:
                continue
            a, b = len(kers[F1]), len(kers[F2])
            Z += w
            P[(a, b)] += w
            PA[a] += w
            PB[b] += w
    mi = sum((v / Z) * math.log2((v / Z)
                                 / ((PA[a] / Z) * (PB[b] / Z)))
             for (a, b), v in P.items())
    assert mi > 0.01, mi
    print(f"    K2(F1,F2) = N^8 * |ker F1 ^ ker F2|")
    print(f"    mutual information between adjacent plaquette costs")
    print(f"    = {mi:.4f} bits (independent plaquettes: exactly 0)")
    simple = [F for F in sample if len(kers[F]) == N ** 2]
    hard = [F for F in sample if len(kers[F]) == 1]
    if len(simple) >= 2:
        print(f"      two simple curvatures: |ker ^ ker| = "
              f"{len(kers[simple[0]] & kers[simple[1]])} "
              f"(each alone {N ** 2})")
    if simple and hard:
        print(f"      simple + non-simple  : |ker ^ ker| = "
              f"{len(kers[simple[0]] & kers[hard[0]])}")
    print()
    print("  THE SHARED FRAME CORRELATES NEIGHBOURS.  Two plaquettes")
    print("  are cheap TOGETHER when their curvature planes share an")
    print("  untouched direction -- the lattice's version of 'all")
    print("  the curvature 2-forms come from one tetrad'.  0053 s4")
    print("  measured this correlation in the budgets; here it is")
    print("  resolved into its geometric cause.")


def run_verification_suite() -> None:
    sections = [
        ("The graviton is massive; Newton lives at a critical point",
         verify_graviton_mass),
        ("The price counts what the curvature leaves alone",
         verify_kernel_price),
        ("The shared frame correlates neighbours",
         verify_shared_frame),
    ]
    for index, (title, check) in enumerate(sections, start=1):
        print("=" * 70)
        print(f"{index}. {title}")
        print("=" * 70)
        check()
        print()
    print("=" * 70)
    print("suite complete")
    print("=" * 70)


if __name__ == "__main__":
    run_verification_suite()
