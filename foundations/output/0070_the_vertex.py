"""The vertex: shared frames, emergent simplicity, and the honest non-flip.

The wall's last standing stone (0075/0077's vertex open).  At a
lattice site six plaquettes meet, and the frame integral that made
the one-plaquette kernel (0072) must there be done JOINTLY -- the
same four tetrad columns couple to all six curvatures.  That is a
16-dimensional Gaussian integral, and it closes:

    W_vertex({F}) = const * PROD_k (eps' + s_k^2)^(-1/2)

with s_k the 16 eigenvalues of the joint coupling matrix
S({F_munu}) (blocks M_munu/2 = (star F_munu)/2 between columns mu
and nu).  The program's own vertex amplitude, derived and
closed-form.  Four results, two of them the answers the last stone
owed, one an honest refusal.

  s1  THE CLOSED FORM, ANCHORED.  Single-plaquette reduction: the
      16 eigenvalues collapse to +/- lam1/2, +/- lam2/2 (each
      fourfold) with lam invariants matching 0072's kernel exactly
      (sum (2s)^2 = |F|^2, prod = Pf^2); the identity
      sum s_k^2 = sum |F_p|^2 holds on random six-packs to 1e-9;
      and a seeded 16D Monte-Carlo bridge confirms the Gaussian
      integral on a generic configuration.

  s2  CROSS-SIMPLICITY EMERGES.  Six plaquettes each INDIVIDUALLY
      simple, matched norms: if they come from a COMMON tetrad the
      vertex price is ~14-16 nats; if they are unrelated simples it
      is ~22-24 -- a mean extra price of +8.6 nats for
      incompatibility, while the product of one-plaquette weights is
      EXACTLY BLIND to the difference (verified to 1e-9).  The
      shared-frame integral enforces the cross-simplicity and
      closure constraints -- Plebanski's off-diagonal conditions --
      that no per-plaquette weight can see.

  s3  THE INSERTION LADDER: THE SUPPRESSION 0075 ORDERED.  Replace
      one plaquette of a tetrad-compatible six-pack:

        insert:            in context     isolated
        geometric (own)      +0.000        +0.000
        foreign simple       +4.96         +0.000
        non-simple           +5.42         +1.82

      Context amplifies the constraint tier ~3x and charges
      COMPATIBILITY ITSELF ~5 nats.  At the vertex, being simple but
      foreign is nearly as expensive as being non-simple; what is
      cheap is being geometric TOGETHER.  This is the vertex-level
      suppression whose absence 0075 measured at the bare chain.

  s4  THE HONEST NON-FLIP.  Weyl-part vs Ricci-part curvature
      operators at matched norm: Ricci is still cheaper in the large
      majority of trials (Weyl cheaper in ~1/8) -- no systematic
      reversal: the vertex does not make the measure select vacuum.
      0061 s3's lesson survives where it should: a measure is not an
      equation of motion.  What the vertex DOES establish is the
      operational sense of "the graviton rides": the measure
      concentrates on tetrad-geometric curvature, so the gapless
      (1,1) carrier's favored content IS metric fluctuation; WHICH
      metric configurations dominate remains the action's job.

Run directly for the verification suite.
"""

from __future__ import annotations

import cmath
import math
import random

PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
IDX = {p: i for i, p in enumerate(PAIRS)}


def eps4(i, j, k, l):
    p = [i, j, k, l]
    if len(set(p)) < 4:
        return 0
    s = 1
    for a in range(4):
        for b in range(a + 1, 4):
            if p[a] > p[b]:
                s = -s
    return s


def starM(F):
    d = dict(zip(PAIRS, F))
    return [[sum(eps4(i, j, k, l) * d[(k, l)] for (k, l) in PAIRS)
             for j in range(4)] for i in range(4)]


def pf(F):
    d = dict(zip(PAIRS, F))
    return (d[(0, 1)] * d[(2, 3)] - d[(0, 2)] * d[(1, 3)]
            + d[(0, 3)] * d[(1, 2)])


def build_S(Fs):
    S = [[0.0] * 16 for _ in range(16)]
    for idx, (mu, nu) in enumerate(PAIRS):
        M = starM(Fs[idx])
        for a in range(4):
            for b in range(4):
                S[4 * mu + a][4 * nu + b] += M[a][b] / 2
                S[4 * nu + b][4 * mu + a] += M[a][b] / 2
    return S


def jacobi_eig(Ain, iters=400):
    n = len(Ain)
    A = [row[:] for row in Ain]
    for _ in range(iters):
        mx, p, q = 0.0, 0, 1
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > mx:
                    mx, p, q = abs(A[i][j]), i, j
        if mx < 1e-12:
            break
        th = 0.5 * math.atan2(2 * A[p][q], A[q][q] - A[p][p])
        c, s = math.cos(th), math.sin(th)
        for k in range(n):
            akp, akq = A[k][p], A[k][q]
            A[k][p] = c * akp - s * akq
            A[k][q] = s * akp + c * akq
        for k in range(n):
            apk, aqk = A[p][k], A[q][k]
            A[p][k] = c * apk - s * aqk
            A[q][k] = s * apk + c * aqk
    return [A[i][i] for i in range(n)]


def vertex_price(Fs, epsp):
    ev = jacobi_eig(build_S(Fs))
    return 0.5 * sum(math.log(1 + s * s / epsp) for s in ev)


def rand_tetrad_config(rng):
    e = [[rng.gauss(0, 1) for _ in range(4)] for _ in range(4)]
    return [[e[mu][i] * e[nu][j] - e[mu][j] * e[nu][i]
             for (i, j) in PAIRS] for (mu, nu) in PAIRS]


def rand_simple(rng):
    a = [rng.gauss(0, 1) for _ in range(4)]
    b = [rng.gauss(0, 1) for _ in range(4)]
    return [a[i] * b[j] - a[j] * b[i] for (i, j) in PAIRS]


def normalize(Fs, target):
    out = []
    for F in Fs:
        n = math.sqrt(sum(x * x for x in F))
        out.append([x * target / n if n > 0 else 0.0 for x in F])
    return out


# =====================================================================
# 1. the closed form, anchored
# =====================================================================

def verify_closed_form() -> None:
    rng = random.Random(7)
    F = [rng.gauss(0, 1) for _ in range(6)]
    Fs = [F] + [[0.0] * 6] * 5
    ev = jacobi_eig(build_S(Fs))
    nz = sorted(abs(e) for e in ev if abs(e) > 1e-9)
    assert len(nz) == 8
    lam2 = sorted(set(round((2 * x) ** 2, 6) for x in nz))
    F2 = sum(x * x for x in F)
    assert abs(sum(lam2) - F2) < 1e-4
    assert abs(lam2[0] * lam2[1] - pf(F) ** 2) < 1e-4
    print(f"    single-plaquette reduction: eigenvalues = +/-lam/2")
    print(f"    fourfold, with sum lam^2 = |F|^2 ({F2:.4f}) and")
    print(f"    prod = Pf^2 ({pf(F) ** 2:.4f}) -- 0072's kernel")
    print(f"    invariants recovered")
    worst = 0.0
    for _ in range(20):
        Fs = [
            [rng.gauss(0, 1) for _ in range(6)] for _ in range(6)]
        ev = jacobi_eig(build_S(Fs))
        s2 = sum(e * e for e in ev)
        f2 = sum(sum(x * x for x in F) for F in Fs)
        worst = max(worst, abs(s2 - f2) / f2)
    assert worst < 1e-6
    print(f"    sum s_k^2 = sum |F_p|^2 on random six-packs: max dev"
          f" {worst:.1e}")
    # 16D MC bridge
    L = 0.9
    rng2 = random.Random(11)
    Fs = normalize([rand_simple(rng2) for _ in range(6)], 0.7)
    S = build_S(Fs)
    n = 300000
    acc = 0j
    for _ in range(n):
        e = [rng2.gauss(0, L) for _ in range(16)]
        q = sum(S[i][j] * e[i] * e[j] for i in range(16)
                for j in range(16))
        acc += cmath.exp(1j * q)
    est = abs(acc / n)
    ev = jacobi_eig(S)
    pred = 1.0
    for s in ev:
        pred *= (1 + (2 * L * L * s) ** 2) ** -0.25
    print(f"    16D MC bridge: |E e^(iQ)| = {est:.4f} vs closed "
          f"{pred:.4f}  ({abs(est - pred) / pred:.1%})")
    assert abs(est - pred) / pred < 0.05
    print()
    print("  W_vertex = PROD (eps' + s_k^2)^(-1/2): the joint frame")
    print("  integral closes on the 16x16 eigenvalue problem.")


# =====================================================================
# 2. cross-simplicity emerges
# =====================================================================

def verify_cross_simplicity() -> None:
    rng = random.Random(7)
    epsp = 0.01
    diffs = []
    for trial in range(8):
        Ft = normalize(rand_tetrad_config(rng), 1.0)
        Fi = normalize([rand_simple(rng) for _ in range(6)], 1.0)
        pt = vertex_price(Ft, epsp)
        pi = vertex_price(Fi, epsp)
        diffs.append(pi - pt)
        # product weight is blind: per-plaquette prices equal
        for F1, F2 in zip(Ft, Fi):
            p1 = vertex_price([F1] + [[0.0] * 6] * 5, epsp)
            p2 = vertex_price([F2] + [[0.0] * 6] * 5, epsp)
            assert abs(p1 - p2) < 1e-6
        if trial < 3:
            print(f"    trial {trial}: price(common tetrad) = "
                  f"{pt:.2f}, price(unrelated simples) = {pi:.2f}")
    mean = sum(diffs) / len(diffs)
    assert all(d > 3 for d in diffs)
    print(f"    mean extra price of incompatibility: +{mean:.2f}")
    print(f"    nats -- while the one-plaquette PRODUCT is exactly")
    print(f"    blind (per-plaquette prices equal to 1e-6)")
    print()
    print("  CROSS-SIMPLICITY EMERGES AT THE VERTEX: the shared-frame")
    print("  integral enforces the off-diagonal Plebanski constraints")
    print("  no per-plaquette weight can see.")


# =====================================================================
# 3. the insertion ladder
# =====================================================================

def verify_insertion_ladder() -> None:
    rng = random.Random(13)
    epsp = 0.01
    TR = 8
    lad = {'foreign': 0.0, 'nonsimple': 0.0}
    iso = {'foreign': 0.0, 'nonsimple': 0.0}
    for _ in range(TR):
        Ft = normalize(rand_tetrad_config(rng), 1.0)
        base = vertex_price(Ft, epsp)
        Bs = normalize([rand_simple(rng)], 1.0)[0]
        Bn = normalize([[rng.gauss(0, 1) for _ in range(6)]], 1.0)[0]
        lad['foreign'] += vertex_price(Ft[:5] + [Bs], epsp) - base
        lad['nonsimple'] += vertex_price(Ft[:5] + [Bn], epsp) - base
        pg = vertex_price([Ft[5]] + [[0.0] * 6] * 5, epsp)
        iso['foreign'] += vertex_price([Bs] + [[0.0] * 6] * 5,
                                       epsp) - pg
        iso['nonsimple'] += vertex_price([Bn] + [[0.0] * 6] * 5,
                                         epsp) - pg
    lf, ln = lad['foreign'] / TR, lad['nonsimple'] / TR
    isf, isn = iso['foreign'] / TR, iso['nonsimple'] / TR
    print(f"    insert into a tetrad six-pack (vs isolated):")
    print(f"      geometric (own):  +0.000        (+0.000)")
    print(f"      foreign simple:   {lf:+.2f}        ({isf:+.3f})")
    print(f"      non-simple:       {ln:+.2f}        ({isn:+.2f})")
    assert lf > 3 and abs(isf) < 0.01
    assert ln > lf and 1.4 < isn < 2.3
    print()
    print("  CONTEXT AMPLIFIES THE CONSTRAINT TIER ~3x AND CHARGES")
    print("  COMPATIBILITY ITSELF ~5 NATS.  Simple-but-foreign is")
    print("  nearly as expensive as non-simple; cheap means geometric")
    print("  TOGETHER.  The suppression 0075 found missing at the")
    print("  bare chain is supplied by the vertex.")


# =====================================================================
# 4. the honest non-flip
# =====================================================================

def _sym_basis20():
    out = []
    for a in range(6):
        for b in range(a, 6):
            M = [[0.0] * 6 for _ in range(6)]
            M[a][b] = 1.0
            M[b][a] = 1.0
            out.append(M)
    bia = lambda M: M[0][5] - M[1][4] + M[2][3]
    keep = [M for M in out if abs(bia(M)) < 1e-12]
    viol = [M for M in out if abs(bia(M)) > 1e-12]
    base = viol[0]
    for M in viol[1:]:
        c = bia(M) / bia(base)
        keep.append([[M[i][j] - c * base[i][j] for j in range(6)]
                     for i in range(6)])
    return keep


def _comp(M, I, J, K, L):
    if I == J or K == L:
        return 0.0
    s = 1
    if I > J:
        I, J, s = J, I, -s
    if K > L:
        K, L, s = L, K, -s
    return s * M[IDX[(I, J)]][IDX[(K, L)]]


def _weyl(M):
    R = [[sum(_comp(M, I, J, I, L) for I in range(4))
          for L in range(4)] for J in range(4)]
    sc = sum(R[j][j] for j in range(4))
    d = lambda i, j: 1.0 if i == j else 0.0
    C = [[0.0] * 6 for _ in range(6)]
    for (I, J) in PAIRS:
        for (K, L) in PAIRS:
            v = _comp(M, I, J, K, L)
            v -= 0.5 * (d(I, K) * R[J][L] - d(I, L) * R[J][K]
                        - d(J, K) * R[I][L] + d(J, L) * R[I][K])
            v += (sc / 6.0) * (d(I, K) * d(J, L) - d(I, L) * d(J, K))
            C[IDX[(I, J)]][IDX[(K, L)]] = v
    return C


def verify_non_flip() -> None:
    rng = random.Random(7)
    B20 = _sym_basis20()
    epsp = 0.01
    wins = 0
    NTR = 24
    for trial in range(NTR):
        M = [[0.0] * 6 for _ in range(6)]
        for Bi in B20:
            c = rng.gauss(0, 1)
            for i in range(6):
                for j in range(6):
                    M[i][j] += c * Bi[i][j]
        W = _weyl(M)
        Ric = [[M[i][j] - W[i][j] for j in range(6)]
               for i in range(6)]

        def cols(X):
            tot = math.sqrt(sum(X[r][c] ** 2 for r in range(6)
                                for c in range(6)))
            return [[X[r][c] * 2.0 / tot for r in range(6)]
                    for c in range(6)]

        pw = vertex_price(cols(W), epsp)
        pr = vertex_price(cols(Ric), epsp)
        if pw < pr:
            wins += 1
        if trial < 3:
            print(f"    trial {trial}: price(Weyl) = {pw:.2f}, "
                  f"price(Ricci) = {pr:.2f}")
    print(f"    Weyl cheaper in {wins}/{NTR} trials")
    assert wins < NTR // 3          # majority Ricci: no reversal
    print()
    print("  THE VERTEX DOES NOT MAKE THE MEASURE SELECT VACUUM --")
    print("  Ricci-type curvature is still the cheaper deformation.")
    print("  0061 s3's lesson survives where it should: a measure is")
    print("  not an equation of motion.  What the vertex establishes")
    print("  is the operational riding: the measure concentrates on")
    print("  TETRAD-GEOMETRIC curvature, so the gapless (1,1)")
    print("  carrier's favored content is metric fluctuation; which")
    print("  metric configurations dominate is the action's job.")


def run_verification_suite() -> None:
    sections = [
        ("The closed form, anchored", verify_closed_form),
        ("Cross-simplicity emerges", verify_cross_simplicity),
        ("The insertion ladder", verify_insertion_ladder),
        ("The honest non-flip", verify_non_flip),
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
