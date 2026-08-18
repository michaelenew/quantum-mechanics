"""Curvature from the quantized 3+1 model: what the arithmetic gives.

The 2+1 quantum arc got its curvature as a Wilson-loop deficit
(0054).  In 3+1 curvature is richer: Riemann splits into Ricci and
Weyl, vacuum kills Ricci and leaves Weyl, and THAT SPLIT IS THE
GRAVITON.  This module builds the curvature operator over Z_N and
asks whether the quantized model reproduces it.  Two positives and
one sharp negative.

  s1  THE SPLIT IS EXACT IN FINITE ARITHMETIC.  Build the Riemann
      operator on bivectors over Z_N -- symmetric 6x6 plus the first
      Bianchi identity -- and decompose by the Kulkarni-Nomizu
      subtraction (needs 2 and 3 invertible, so N coprime to 6):

        n = 4:  dim Riemann 20, Ricci 10, Weyl 10   (N = 5 and 7)
        n = 3:  dim Riemann  6, Ricci  6, Weyl  0

      matching the continuum n^2(n^2-1)/12, n(n+1)/2 and
      n(n+1)(n+2)(n-3)/12 exactly.  WEYL EXISTS IN 3+1 AND VANISHES
      IDENTICALLY IN 2+1 -- the graviton's existence, and its
      absence one dimension down, as a statement of finite-field
      arithmetic rather than of analysis.

  s2  AND THE VACUUM EINSTEIN EQUATION IS ARITHMETIC TOO.  With the
      Hodge star on bivectors (Euclidean, star^2 = 1 over Z_N):

        [R, star] = 0   <=>   traceless Ricci = 0

      verified 3000/3000 on random curvatures at N = 5, and pure-Weyl
      curvatures commute with the star 300/300.  So "this curvature
      is Einstein" is expressible exactly in the quantized model's
      own arithmetic -- no continuum limit required to state it.

  s3  BUT THE MEASURE DOES NOT SELECT IT.  The honest negative.  Lift
      0055/0056's per-plaquette price (kernel codimension, 0/2/4 for
      flat/simple/non-simple) to a curvature operator by summing over
      its six plaquette columns, and test what the price is a
      function of:

        same Weyl, Ricci changed  ->  price CHANGED in 220/300
        same Ricci, Weyl changed  ->  price CHANGED in 209/300

      It factors through NEITHER.  And the Einstein sector is not the
      cheap one:

        sector                 mean price   fraction at the cheapest tier
        pure Weyl (Ricci = 0)     21.478        0.0087
        generic                   21.535        0.0002
        pure Ricci (Weyl = 0)     21.216        0.0605

      Both algebraically special sectors are far likelier to be cheap
      than generic (44x and 300x), so the measure does prefer special
      curvature -- but it prefers PURE RICCI over PURE WEYL, the
      opposite of vacuum selection.  THE SIMPLICITY PRICE IS NOT THE
      EINSTEIN EQUATION.  Whatever imposes vacuum in this theory is
      the action's variation, not the measure's weight.

      WHAT THE PRICE IS.  The weight comes from integrating the
      frame out of the action's eps.B.F term, B = e^e:
        K(F) = sum_{a,b} omega^{eps_IJKL a^I b^J F^KL}
      a sum of PHASES.  The exponent is linear in a, so the
      a-sum is a CHARACTER SUM: N^4 when eps_IJKL b^J F^KL
      vanishes, exactly 0 otherwise.  So
        K(F) = N^4 * #{ b : the curvature annihilates b }
      -- 0056's kernel count, now derived.  A tempting misreading,
      checked and REJECTED: K is not the count of frame pairs
      pairing to zero (2673 vs K = 729 at N = 3 simple); the
      surplus phases cancel among themselves.  So the tiers count
      HOW MANY INDEPENDENT PLANES THE CURVATURE ROTATES IN --
      none, one, or two.  It cannot be Einstein for two reasons:
      the price interrogates a SINGLE BIVECTOR's rank while
      Einstein interrogates the OPERATOR's commutator with the
      star; and A MEASURE IS NOT AN EQUATION OF MOTION --
      integrating out sums over every frame, varying selects
      stationary points.

  s4  AND AMBROSE-SINGER SAYS WHY.  A smooth metric whose holonomy
      group is FINITE is flat (the holonomy algebra is spanned by the
      curvature).  So a literal Z_N-holonomy lattice describes
      piecewise-flat geometry with conical defects -- exactly right in
      2+1, where that IS Deser-Jackiw-'t Hooft and 0054's deficit, and
      in 3+1 it gives STRING defects.  The Weyl sector exists in the
      arithmetic (s1) and a finite-holonomy sector cannot carry it.
      That is a structural reason the abelian quantum arc reached
      Newton (0057) and keeps not reaching polarizations.

      THREE CORRECTIONS to how this was first stated:
      (a) STRINGS RADIATE, and this repo measured it -- 0049 gets
          Gamma = P/(G mu^2) = 45.8 for an oscillating Kibble-Turok
          loop against GR's 40-100.  A STATIC straight string is flat
          outside itself and radiates nothing; an OSCILLATING one
          radiates strongly.  The correct claim is narrower: the
          finite sector holds the DEFECT but not the RADIATION FIELD.
      (b) QUANTUM DOES NOT MEAN FINITE.  Quantization discretizes
          spectra, not the group: lattice QCD keeps SU(3), loop
          quantum gravity keeps SU(2) and gets discrete areas from
          representation labels.  Z_N was a TRACTABILITY choice --
          it is what made 0053-0057 exactly enumerable.
      (c) "NONABELIAN" IS THE WRONG WORD for the fix.  A finite
          nonabelian group is still finite and still forced flat; and
          Lorentzian pp-waves have ABELIAN holonomy (null rotations)
          while being Ricci-flat and curved.  The operative property
          is CONTINUITY.  The classical lattice (0047) already uses
          SO(3,1) links; only the quantum sector shrank to Z_N.

Run directly for the verification suite.
"""

from __future__ import annotations

import itertools
import random

PAIRS4 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def pairs(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


class Curv:
    """Riemann operator on bivectors over Z_N, Euclidean internal
    metric.  Indices are bivector pairs; M[a][b] = R_{(a)(b)}."""

    def __init__(self, n, N):
        self.n, self.N = n, N
        self.P = pairs(n)
        self.idx = {p: i for i, p in enumerate(self.P)}

    def comp(self, M, I, J, K, L):
        if I == J or K == L:
            return 0
        s = 1
        if I > J:
            I, J, s = J, I, -s
        if K > L:
            K, L, s = L, K, -s
        return (s * M[self.idx[(I, J)]][self.idx[(K, L)]]) % self.N

    def ricci(self, M):
        n, N = self.n, self.N
        return [[sum(self.comp(M, I, J, I, L) for I in range(n)) % N
                 for L in range(n)] for J in range(n)]

    def scal(self, M):
        R = self.ricci(M)
        return sum(R[j][j] for j in range(self.n)) % self.N

    def weyl(self, M):
        """C = R - (1/(n-2))(g o Ric) + (S/((n-1)(n-2)))(g o g)."""
        n, N = self.n, self.N
        a = pow(n - 2, -1, N)
        b = (self.scal(M) * pow((n - 1) * (n - 2), -1, N)) % N
        Ric = self.ricci(M)
        d = lambda i, j: 1 if i == j else 0
        m = len(self.P)
        C = [[0] * m for _ in range(m)]
        for (I, J) in self.P:
            for (K, L) in self.P:
                v = self.comp(M, I, J, K, L)
                v -= a * (d(I, K) * Ric[J][L] - d(I, L) * Ric[J][K]
                          - d(J, K) * Ric[I][L] + d(J, L) * Ric[I][K])
                v += b * (d(I, K) * d(J, L) - d(I, L) * d(J, K))
                C[self.idx[(I, J)]][self.idx[(K, L)]] = v % N
        return C


def rank_modp(rows, N):
    A = [r[:] for r in rows]
    r = 0
    cols = len(A[0]) if A else 0
    for c in range(cols):
        piv = None
        for i in range(r, len(A)):
            if A[i][c] % N:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], -1, N)
        A[r] = [(x * inv) % N for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] % N:
                f = A[i][c]
                A[i] = [(A[i][k] - f * A[r][k]) % N for k in range(cols)]
        r += 1
    return r


def basis(cv):
    """Spanning set for the Riemann space: symmetric operators with
    the first Bianchi identity imposed."""
    n, N, P = cv.n, cv.N, cv.P
    m = len(P)
    out = []
    for a in range(m):
        for b in range(a, m):
            M = [[0] * m for _ in range(m)]
            M[a][b] = 1
            M[b][a] = 1
            out.append(M)
    if n < 4:
        return out
    bia = lambda M: (M[0][5] - M[1][4] + M[2][3]) % N
    keep = [M for M in out if bia(M) == 0]
    viol = [M for M in out if bia(M)]
    if len(viol) >= 2:
        base = viol[0]
        for M in viol[1:]:
            c = (bia(M) * pow(bia(base), -1, N)) % N
            keep.append([[(M[i][j] - c * base[i][j]) % N
                          for j in range(m)] for i in range(m)])
    return keep


def flat(M):
    return [x for row in M for x in row]


# =====================================================================
# 1. the split is exact in finite arithmetic
# =====================================================================

def verify_counting() -> None:
    expect = {4: (20, 10, 10), 3: (6, 6, 0)}
    for n, N in ((4, 5), (4, 7), (3, 5), (3, 7)):
        cv = Curv(n, N)
        B = basis(cv)
        dR = rank_modp([flat(M) for M in B], N)
        dW = rank_modp([flat(cv.weyl(M)) for M in B], N)
        rows = []
        for M in B:
            R = cv.ricci(M)
            rows.append([R[i][j] for i in range(n) for j in range(n)])
        dC = rank_modp(rows, N)
        print(f"    n = {n}, N = {N}: Riemann {dR:2d}, Ricci {dC:2d}, "
              f"Weyl {dW:2d}   (continuum: "
              f"{n * n * (n * n - 1) // 12}, {n * (n + 1) // 2}, "
              f"{n * (n + 1) * (n + 2) * (n - 3) // 12})")
        assert (dR, dC, dW) == expect[n], (n, N, dR, dC, dW)
    print()
    print("  WEYL EXISTS IN 3+1 AND VANISHES IDENTICALLY IN 2+1, as")
    print("  finite-field arithmetic.  The graviton's existence -- and")
    print("  its absence one dimension down -- without taking a")
    print("  continuum limit to say it.")


# =====================================================================
# 2. the vacuum Einstein equation is arithmetic too
# =====================================================================

def _eps4(I, J, K, L):
    p = [I, J, K, L]
    if len(set(p)) < 4:
        return 0
    s = 1
    for a in range(4):
        for b in range(a + 1, 4):
            if p[a] > p[b]:
                s = -s
    return s


def hodge_matrix(N):
    S = [[0] * 6 for _ in range(6)]
    idx = {p: i for i, p in enumerate(PAIRS4)}
    for (I, J) in PAIRS4:
        for (K, L) in PAIRS4:
            S[idx[(I, J)]][idx[(K, L)]] = _eps4(I, J, K, L) % N
    return S


def matmul(A, C, N):
    return [[sum(A[i][k] * C[k][j] for k in range(6)) % N
             for j in range(6)] for i in range(6)]


def verify_einstein_is_arithmetic() -> None:
    N = 5
    cv = Curv(4, N)
    B = basis(cv)
    S = hodge_matrix(N)
    S2 = matmul(S, S, N)
    assert all(S2[i][j] % N == (1 if i == j else 0)
               for i in range(6) for j in range(6))
    print("    Hodge star on bivectors over Z_N: star^2 = 1 (Euclidean)")
    rng = random.Random(41)

    def randR():
        M = [[0] * 6 for _ in range(6)]
        for Bi in B:
            c = rng.randrange(N)
            if c:
                for i in range(6):
                    for j in range(6):
                        M[i][j] = (M[i][j] + c * Bi[i][j]) % N
        return M

    def commutes(M):
        A, C = matmul(M, S, N), matmul(S, M, N)
        return all((A[i][j] - C[i][j]) % N == 0
                   for i in range(6) for j in range(6))

    def tl_ricci_zero(M):
        R = cv.ricci(M)
        q = (cv.scal(M) * pow(4, -1, N)) % N
        return all((R[i][j] - (q if i == j else 0)) % N == 0
                   for i in range(4) for j in range(4))

    agree = sum(1 for _ in range(3000)
                if (lambda M: commutes(M) == tl_ricci_zero(M))(randR()))
    print(f"      [R, star] = 0  <=>  traceless Ricci = 0: "
          f"{agree}/3000 agree")
    assert agree == 3000, agree
    ok = sum(1 for _ in range(300)
             if (lambda W: commutes(W) and tl_ricci_zero(W))(
                 cv.weyl(randR())))
    print(f"      pure-Weyl curvatures commute with star: {ok}/300")
    assert ok == 300, ok
    print()
    print("  THE VACUUM EINSTEIN CONDITION IS AN ARITHMETIC IDENTITY:")
    print("  the curvature operator commutes with the Hodge star.  So")
    print("  'this curvature is Einstein' is sayable exactly inside the")
    print("  quantized model, with no limit taken.")


# =====================================================================
# 3. but the measure does not select it
# =====================================================================

def _pf(F, N):
    d = dict(zip(PAIRS4, F))
    return (d[(0, 1)] * d[(2, 3)] - d[(0, 2)] * d[(1, 3)]
            + d[(0, 3)] * d[(1, 2)]) % N


def column_price(F, N):
    """0055/0056's kernel codimension: 0 flat, 2 simple, 4 non-simple."""
    if all(x % N == 0 for x in F):
        return 0
    return 2 if _pf(F, N) == 0 else 4


def operator_price(M, N):
    return sum(column_price(tuple(M[r][c] % N for r in range(6)), N)
               for c in range(6))


def verify_measure_does_not_select() -> None:
    N = 5
    cv = Curv(4, N)
    B = basis(cv)
    rng = random.Random(23)

    def randR():
        M = [[0] * 6 for _ in range(6)]
        for Bi in B:
            c = rng.randrange(N)
            if c:
                for i in range(6):
                    for j in range(6):
                        M[i][j] = (M[i][j] + c * Bi[i][j]) % N
        return M

    def add(A, C):
        return [[(A[i][j] + C[i][j]) % N for j in range(6)]
                for i in range(6)]

    def sub(A, C):
        return [[(A[i][j] - C[i][j]) % N for j in range(6)]
                for i in range(6)]

    def same(A, C, k):
        return all(A[i][j] == C[i][j] for i in range(k)
                   for j in range(k))

    trials = 300
    a_diff = b_diff = 0
    for _ in range(trials):
        # A: shift by a pure-Ricci piece -> Weyl unchanged
        M = randR()
        X = randR()
        ricci_piece = sub(X, cv.weyl(X))
        Mb = add(M, ricci_piece)
        assert same(cv.weyl(Mb), cv.weyl(M), 6)
        if operator_price(M, N) != operator_price(Mb, N):
            a_diff += 1
        # B: shift by a pure-Weyl piece -> Ricci unchanged
        M3 = randR()
        Mc = add(M3, cv.weyl(randR()))
        assert same(cv.ricci(Mc), cv.ricci(M3), 4)
        if operator_price(M3, N) != operator_price(Mc, N):
            b_diff += 1
    print(f"    same Weyl, Ricci changed -> price CHANGED "
          f"{a_diff}/{trials}")
    print(f"    same Ricci, Weyl changed -> price CHANGED "
          f"{b_diff}/{trials}")
    assert a_diff > trials * 0.4 and b_diff > trials * 0.4
    n = 6000
    pw = [operator_price(cv.weyl(randR()), N) for _ in range(n)]
    gn = [operator_price(randR(), N) for _ in range(n)]
    pr = []
    for _ in range(n):
        M = randR()
        pr.append(operator_price(sub(M, cv.weyl(M)), N))
    print()
    print("    sector                 mean price   fraction cheapest")
    rows = [("pure Weyl (Ricci = 0)", pw), ("generic", gn),
            ("pure Ricci (Weyl = 0)", pr)]
    frac = {}
    for lab, v in rows:
        f = sum(1 for x in v if x <= 12) / len(v)
        frac[lab] = f
        print(f"    {lab:22s}    {sum(v) / len(v):6.3f}       {f:.4f}")
    # the Einstein sector is NOT the preferred one
    assert frac["pure Ricci (Weyl = 0)"] > frac["pure Weyl (Ricci = 0)"]
    assert frac["pure Weyl (Ricci = 0)"] > frac["generic"]
    print()
    print("  THE PRICE FACTORS THROUGH NEITHER Ricci NOR Weyl, and the")
    print("  Einstein sector is not the cheap one -- pure Ricci is")
    print("  cheaper than pure Weyl, the OPPOSITE of vacuum selection.")
    print("  The simplicity price is not the Einstein equation; what")
    print("  imposes vacuum here is the action's variation, not the")
    print("  measure's weight.")


# =====================================================================
# 4. Ambrose-Singer says why
# =====================================================================

def verify_ambrose_singer_reading() -> None:
    print("    Ambrose-Singer: the holonomy algebra is spanned by the")
    print("    curvature, so a smooth metric with FINITE holonomy is")
    print("    FLAT.  A literal Z_N-holonomy lattice therefore carries")
    print("    piecewise-flat geometry with conical defects.")
    print()
    for n, N in ((3, 5), (4, 5)):
        cv = Curv(n, N)
        dW = rank_modp([flat(cv.weyl(M)) for M in basis(cv)], N)
        reading = ("point defects -- exactly Deser-Jackiw-'t Hooft "
                   "and 0054" if n == 3 else
                   "STRING defects, but not their radiation field")
        print(f"      n = {n}: Weyl dimension {dW} -> {reading}")
    print()
    print("    Corrections to the first statement of this:")
    print("      (a) strings DO radiate -- 0049 measured Gamma = 45.8")
    print("          for an oscillating loop.  The finite sector holds")
    print("          the DEFECT, not the RADIATION FIELD.")
    print("      (b) quantum does NOT mean finite: lattice QCD keeps")
    print("          SU(3), loop quantum gravity keeps SU(2).  Z_N was")
    print("          a tractability choice, not a consequence.")
    print("      (c) the fix is CONTINUITY, not non-commutativity --")
    print("          a finite nonabelian group is still forced flat,")
    print("          and pp-waves have abelian holonomy while curved.")
    print()
    print("  THE WEYL SECTOR EXISTS IN THE ARITHMETIC (s1) BUT A")
    print("  FINITE-HOLONOMY SECTOR CANNOT CARRY IT.  That is a")
    print("  structural reason the abelian quantum arc reached Newton")
    print("  (0057) and keeps not reaching polarizations.  The 2+1")
    print("  success was not a warm-up for 3+1; it was the abelian")
    print("  sector doing the only job it can do -- and the finiteness")
    print("  that caps 3+1 is exactly what made 2+1 exactly solvable.")


def run_verification_suite() -> None:
    sections = [
        ("The Riemann/Ricci/Weyl split is exact in finite arithmetic",
         verify_counting),
        ("The vacuum Einstein equation is arithmetic too",
         verify_einstein_is_arithmetic),
        ("But the measure does not select it",
         verify_measure_does_not_select),
        ("Ambrose-Singer says why", verify_ambrose_singer_reading),
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
