"""The quantization audit: exactness, a theorem, and two corrections.

A model-switch audit of the quantized-curvature arc -- 0061 and its
revision, with spot-rechecks of 0057.  Everything substantive held.
One verification was weaker than claimed and is upgraded to exact;
one wording and one citation were wrong and are corrected in place;
and the audit produced a small theorem that resolves 0061's open
sub-question about the exactly-2 price ratio.

  s1  THE PROJECTORS ARE EXACT, NOT SAMPLED.  On every one of the 20
      basis elements (N = 5 and 7): the Weyl projector's output is
      symmetric, satisfies the first Bianchi identity, is annihilated
      by the Ricci contraction, and is idempotent; its image has rank
      10, the kernel of the rank-10 Ricci map.  0061's spot checks
      become identities.

  s2  THE EINSTEIN CRITERION IS PROVEN, AND SHARPENED.  0061 s2's
      "3000/3000 agree" contained ZERO positive cases -- a random
      curvature is essentially never Einstein (probability ~ N^-9) --
      so as shipped it tested only the generic direction.  Here the
      equivalence is exact linear algebra: the maps M -> [M, star]
      and M -> traceless Ricci(M) have IDENTICAL kernels on the
      20-dimensional Riemann space (rank 9 each, stacked rank 9, at
      N = 5 and 7).  Sharpened: [R, star] = 0 is EINSTEIN-WITH-LAMBDA
      (R_ab proportional to g_ab), not vacuum -- witness: Weyl + 2 Id
      commutes with the star and has Ricci != 0.  Vacuum is the pair
      [R, star] = 0 AND s = 0, equally arithmetic: its kernel equals
      the full Ricci map's kernel (rank 10 = 10 = stacked 10).

  s3  THE PRICE IS THE RANK -- a theorem, resolving the ratio-2 open.
      The kernel map b -> eps_IJKL b^J F^KL IS the alternating matrix
      (star F) acting on frame vectors (verified against the shipped
      m_of).  Hence |ker F| = N^(4 - rank star F) and

        price(F) = rank(F) x log N .

      Alternating forms have EVEN rank in every characteristic, so
      the only possible tiers are 0 / 2 / 4 -- the "exactly 2" cost
      ratio 0061 flagged as suspiciously clean is the parity theorem
      for alternating forms, not a coincidence.  Verified
      exhaustively: every F at N = 3 (729, with literal kernel
      counts), N = 5 (15625) and N = 7 (117649); tier <-> Pfaffian
      exact throughout (rank 4 <=> Pf != 0; rank 2 <=> Pf = 0 and
      F != 0; rank 0 <=> flat).

  s4  THE SECTOR ORDERING IS SEED-STABLE.  0061 s3's Monte Carlo
      conclusion (cheapest-tier fraction: pure Ricci > pure Weyl >>
      generic) reproduces at three fresh seeds.  The honest negative
      stands: the measure does not select the Einstein sector.

  s5  0057 SPOT-RECHECKS.  Pf(F) is a function of the self-dual
      imbalance |F+|^2 - |F-|^2 alone (re-verified over all N^6
      curvatures, N = 3 and 5), and the critical-dispersion
      arithmetic reproduces.

  Corrections applied in place by this audit: 0061's Gamma = 45.8
  loop-decay citation moved from 0049 (which built the loop and left
  decay power open) to 0050 (output/0045's loop_power, which measured
  it); and 0061 s2's "vacuum Einstein equation" wording sharpened to
  Einstein-with-Lambda, vacuum being the commute-and-scalar-free pair.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import itertools
import math
import os
import random
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
_qc = importlib.import_module('0055_the_quantized_curvature')
_mg = importlib.import_module('0051_the_massive_graviton')
_qn = importlib.import_module('0052_quantum_newton')

Curv, basis, rank_modp = _qc.Curv, _qc.basis, _qc.rank_modp
hodge_matrix, matmul, flat = _qc.hodge_matrix, _qc.matmul, _qc.flat
m_of, PAIRS, eps4 = _mg.m_of, _mg.PAIRS, _mg.eps4


def alt_matrix(F, N):
    """(star F)_IJ = sum_{(K,L)} eps_IJKL F_(KL): the alternating
    matrix whose action on frame vectors is the kernel map m_of."""
    d = dict(zip(PAIRS, F))
    return [[sum(eps4(I, J, K, L) * d[(K, L)] for (K, L) in PAIRS) % N
             for J in range(4)] for I in range(4)]


def pf(F, N):
    d = dict(zip(PAIRS, F))
    return (d[(0, 1)] * d[(2, 3)] - d[(0, 2)] * d[(1, 3)]
            + d[(0, 3)] * d[(1, 2)]) % N


def make_rand(cv, B, rng):
    def rand_op():
        M = [[0] * 6 for _ in range(6)]
        for Bi in B:
            c = rng.randrange(cv.N)
            for i in range(6):
                for j in range(6):
                    M[i][j] = (M[i][j] + c * Bi[i][j]) % cv.N
        return M
    return rand_op


# =====================================================================
# 1. the projectors are exact
# =====================================================================

def verify_exact_projectors() -> None:
    for N in (5, 7):
        cv = Curv(4, N)
        B = basis(cv)
        assert len(B) == 20
        assert rank_modp([flat(M) for M in B], N) == 20
        bia = lambda M: (M[0][5] - M[1][4] + M[2][3]) % N
        for M in B:
            W = cv.weyl(M)
            assert all(W[i][j] == W[j][i]
                       for i in range(6) for j in range(6))
            assert bia(W) == 0
            assert all(v == 0 for row in cv.ricci(W) for v in row)
            W2 = cv.weyl(W)
            assert all(W2[i][j] == W[i][j]
                       for i in range(6) for j in range(6))
        rW = rank_modp([flat(cv.weyl(M)) for M in B], N)
        rR = rank_modp([[cv.ricci(M)[i][j]
                         for i in range(4) for j in range(4)]
                        for M in B], N)
        assert rW == 10 and rR == 10
        print(f"    N = {N}: Weyl symmetric + Bianchi + idempotent + "
              f"Ricci-free on ALL 20 basis elements;")
        print(f"           image rank {rW} = kernel of the rank-{rR} "
              f"Ricci map")
    print()
    print("  0061's projector spot-checks are now identities on the")
    print("  full basis -- no sampling anywhere in this section.")


# =====================================================================
# 2. the Einstein criterion, proven and sharpened
# =====================================================================

def verify_kernel_identity() -> None:
    for N in (5, 7):
        cv = Curv(4, N)
        B = basis(cv)
        S = hodge_matrix(N)
        rows_c, rows_t, rows_s, rows_r = [], [], [], []
        for M in B:
            A1, A2 = matmul(M, S, N), matmul(S, M, N)
            rows_c.append([(A1[i][j] - A2[i][j]) % N
                           for i in range(6) for j in range(6)])
            R = cv.ricci(M)
            s = cv.scal(M)
            rows_t.append([(4 * R[i][j] - (s if i == j else 0)) % N
                           for i in range(4) for j in range(4)])
            rows_s.append([s % N])
            rows_r.append([R[i][j] for i in range(4) for j in range(4)])
        r1 = rank_modp(rows_c, N)
        r2 = rank_modp(rows_t, N)
        rs = rank_modp([rows_c[k] + rows_t[k] for k in range(20)], N)
        assert r1 == r2 == rs == 9, (r1, r2, rs)
        v1 = rank_modp([rows_c[k] + rows_s[k] for k in range(20)], N)
        v2 = rank_modp(rows_r, N)
        v3 = rank_modp([rows_c[k] + rows_s[k] + rows_r[k]
                        for k in range(20)], N)
        assert v1 == v2 == v3 == 10, (v1, v2, v3)
        print(f"    N = {N}: rank[.,star] = {r1} = rank(tlRic) = {r2} "
              f"= stacked {rs}  ->  KERNELS IDENTICAL")
        print(f"           rank([.,star] + scal) = {v1} = rank(Ricci) "
              f"= {v2} = stacked {v3}  ->  vacuum pair exact")
    # Einstein-but-not-vacuum witness
    N = 5
    cv = Curv(4, N)
    B = basis(cv)
    S = hodge_matrix(N)
    rng = random.Random(3)
    E = cv.weyl(make_rand(cv, B, rng)())
    for i in range(6):
        E[i][i] = (E[i][i] + 2) % N
    A1, A2 = matmul(E, S, N), matmul(S, E, N)
    assert all((A1[i][j] - A2[i][j]) % N == 0
               for i in range(6) for j in range(6))
    R, s = cv.ricci(E), cv.scal(E)
    assert s % N != 0 and any(v % N for row in R for v in row)
    assert all((4 * R[i][j] - (s if i == j else 0)) % N == 0
               for i in range(4) for j in range(4))
    print(f"    witness Weyl + 2*Id: commutes, Ricci = (s/4)delta != 0,"
          f" s = {s % N}")
    print()
    print("  0061 s2's 3000-sample check had ZERO positive cases (a")
    print("  random curvature is never Einstein), so it tested only the")
    print("  generic direction.  The equivalence is now EXACT: identical")
    print("  kernels.  And the criterion is EINSTEIN-WITH-LAMBDA, not")
    print("  vacuum -- vacuum is the pair [R,star] = 0 AND s = 0, whose")
    print("  kernel equals the full Ricci map's kernel exactly.")


# =====================================================================
# 3. the price is the rank
# =====================================================================

def verify_price_is_rank() -> None:
    rng = random.Random(9)
    for N in (3, 5):
        for _ in range(200):
            F = tuple(rng.randrange(N) for _ in range(6))
            b = tuple(rng.randrange(N) for _ in range(4))
            A = alt_matrix(F, N)
            mv = tuple(sum(A[I][J] * b[J] for J in range(4)) % N
                       for I in range(4))
            assert mv == m_of(b, F, N)
    print("    m_of(b, F) == (star F) . b  on 200 + 200 random pairs")
    print("    (N = 3, 5): the kernel map IS the alternating matrix")
    N = 3
    vecs = list(itertools.product(range(N), repeat=4))
    tiers = {}
    for F in itertools.product(range(N), repeat=6):
        A = alt_matrix(F, N)
        assert all(A[i][i] == 0 for i in range(4))
        r = rank_modp([row[:] for row in A], N)
        assert r % 2 == 0
        ker = sum(1 for b in vecs
                  if all(x == 0 for x in m_of(b, F, N)))
        assert ker == N ** (4 - r)
        if all(x == 0 for x in F):
            assert r == 0
        elif pf(F, N) == 0:
            assert r == 2
        else:
            assert r == 4
        tiers[r] = tiers.get(r, 0) + 1
    print(f"    N = 3, all 729 F: rank EVEN always; |ker| = N^(4-rank)")
    print(f"    exactly; tier <-> Pf exact; counts {tiers}")
    for N in (5, 7):
        cnt = {}
        for F in itertools.product(range(N), repeat=6):
            r = rank_modp([row[:] for row in alt_matrix(F, N)], N)
            assert r % 2 == 0
            if all(x == 0 for x in F):
                assert r == 0
            elif pf(F, N) == 0:
                assert r == 2
            else:
                assert r == 4
            cnt[r] = cnt.get(r, 0) + 1
        print(f"    N = {N}, all {N ** 6} F: rank even, tier <-> Pf "
              f"exact, counts {cnt}")
    print()
    print("  PRICE(F) = rank(F) x log N.  Alternating forms have even")
    print("  rank in every characteristic, so the tiers 0/2/4 are the")
    print("  even ranks of a 4x4 alternating form -- the exactly-2 cost")
    print("  ratio is the PARITY THEOREM, not a coincidence.  0061's")
    print("  open sub-question resolved.")


# =====================================================================
# 4. the sector ordering is seed-stable
# =====================================================================

def verify_seed_stability() -> None:
    N = 5
    cv = Curv(4, N)
    B = basis(cv)

    def sub(A, C):
        return [[(A[i][j] - C[i][j]) % N for j in range(6)]
                for i in range(6)]

    for seed in (7, 99, 12345):
        rng = random.Random(seed)
        rand_op = make_rand(cv, B, rng)
        n = 3000
        fw = sum(1 for _ in range(n)
                 if _qc.operator_price(cv.weyl(rand_op()), N) <= 12) / n
        fg = sum(1 for _ in range(n)
                 if _qc.operator_price(rand_op(), N) <= 12) / n
        cnt = 0
        for _ in range(n):
            M = rand_op()
            cnt += _qc.operator_price(sub(M, cv.weyl(M)), N) <= 12
        fr = cnt / n
        print(f"    seed {seed:5d}: cheapest-frac  pure Weyl {fw:.4f}"
              f"  generic {fg:.4f}  pure Ricci {fr:.4f}")
        assert fr > fw > fg, (seed, fr, fw, fg)
    print()
    print("  Pure Ricci cheaper than pure Weyl, both far above generic,")
    print("  at every seed.  0061 s3's negative -- the measure does not")
    print("  select the Einstein sector -- STANDS.")


# =====================================================================
# 5. 0057 spot-rechecks
# =====================================================================

def verify_0057_rechecks() -> None:
    for N in (3, 5):
        rel = {}
        for F in itertools.product(range(N), repeat=6):
            Fp, Fm = _qn.sd_asd(F, N)
            key = (sum(x * x for x in Fp)
                   - sum(x * x for x in Fm)) % N
            p = _qn.pfaffian(F, N)
            assert rel.setdefault(key, p) == p
        print(f"    N = {N}: Pf a function of |F+|^2 - |F-|^2 alone "
              f"({len(rel)} classes) -- CONFIRMED")
    V = 2 * math.log(3)
    t = V / 6
    for k, want in ((0.4, 0.9867), (0.05, 0.9998)):
        got = 2 * t * (1 - math.cos(k)) / (t * k * k)
        assert abs(got - want) < 5e-4, (k, got)
        print(f"    dispersion k = {k}: E/(t k^2) = {got:.4f}")
    print()
    print("  0057's self-dual reading and critical dispersion reproduce.")


def run_verification_suite() -> None:
    sections = [
        ("The projectors are exact, not sampled",
         verify_exact_projectors),
        ("The Einstein criterion, proven and sharpened",
         verify_kernel_identity),
        ("The price is the rank", verify_price_is_rank),
        ("The sector ordering is seed-stable", verify_seed_stability),
        ("0057 spot-rechecks", verify_0057_rechecks),
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
