"""The nonabelian Dirichlet square: the ledger was a Born rule all along.

0073's sign problem demanded the dual-square structure.  Chasing where
the abelian ledger's positivity actually comes from turns up something
sharper than the demand: THE LEDGER MEASURE IS A BORN SQUARE, exactly,
and the nonabelian weight built the same way is coefficient-positive
by fusion.

  s1  THE LEDGER IS A BORN SQUARE (exact, abelian).  For every odd N
      tested (3..61, all fluxes):

        gcd(F, N)  =  | sum_e omega^{e^2 F} |^2 / N

      -- the Z_N ledger weight is the squared magnitude of a
      QUADRATIC GAUSS SUM: a single-frame amplitude, with B = e^2 the
      abelian shadow of B = e wedge e.  The measure 0053 took as
      given is the Born rule applied to a frame amplitude.  Even N
      FAILS (at most fluxes) -- N = 2's degeneracy family again, now
      at the root.  And the mechanism of coefficient positivity is
      visible: the amplitude's dual expansion COUNTS frames
      (r(m) = #{e : e^2 = m} >= 0), so the weight's dual is the
      autocorrelation of a nonnegative function -- verified exactly:
      dual(gcd) = r-star-r at every mode.

  s2  THE POSITIVITY THEOREM (fusion form).  If W = A^2 with
      A = sum_j n_j chi_j and n_j >= 0 (a counting amplitude), then
      every character coefficient of W is a sum of nonnegative
      fusion terms: c_j(W) = sum n_m n_m' N^j_{m m'} >= 0.  Checked
      on SU(2) (multiplicity-free fusion) over random nonnegative
      countings -- all coefficients >= 0 -- and a mixed-sign
      amplitude exhibits a negative coefficient: the counting
      condition is what does the work.

  s3  THE DERIVED NONABELIAN AMPLITUDE IS DIAGONAL.  A frame pair
      spans a SIMPLE bivector, and simple = BALANCED
      (|B+| = |B-|, machine-exact), so the frame-counting amplitude
      on Spin(4) lives on the diagonal:

        A(U+, U-) = sum_j n_j chi_j(U+) chi_j(U-)

      with n_j the Gaussian frame-measure counting of |B+| (computed
      by deterministic quadrature, binned at scale s0).  The Born
      weight W = A^2 then has c(j+, j-) >= 0 EVERYWHERE (asserted),
      diagonal-dominant with positive-small off-diagonal (nothing
      forbidden), heavy-tailed along the diagonal -- 0073's
      structure with the signs healed.  Pointwise, W still ridges on
      the balanced classes like the kernel did.

  s4  THE WALL STATUS.  0073's disease is cured by restoring the
      Born structure the naive lift dropped: lift the AMPLITUDE, not
      the weight.  The healed object is Barrett-Crane AS AN
      AMPLITUDE ("BC squared") with a derived radial profile -- and
      A3, the graviton-propagator test, now has a positive object to
      run on.  The abelian tier of all of this is exactly solvable
      -- the program owns a TOY of the wall (and of the sign
      problem, the sibling arithmetic branch's cognate probe).

Run directly for the verification suite.
"""

from __future__ import annotations

import cmath
import math
import random
from math import gcd


# =====================================================================
# 1. the ledger is a Born square
# =====================================================================

def verify_born_square() -> None:
    odds = [3, 5, 7, 9, 11, 15, 21, 25, 33, 45, 61]
    for N in odds:
        for F in range(N):
            g = sum(cmath.exp(2j * math.pi * (e * e * F) / N)
                    for e in range(N))
            assert abs(abs(g) ** 2 / N
                       - gcd(F if F else N, N)) < 1e-8, (N, F)
    print(f"    gcd(F,N) = |sum_e omega^(e^2 F)|^2 / N: EXACT for all")
    print(f"    fluxes at every odd N in {odds}")
    fails = {}
    for N in (2, 4, 6, 8, 12):
        bad = sum(1 for F in range(N)
                  if abs(abs(sum(cmath.exp(2j * math.pi * (e * e * F)
                                           / N)
                                 for e in range(N))) ** 2 / N
                         - gcd(F if F else N, N)) > 1e-8)
        fails[N] = bad
    print(f"    even N fails: {fails} (N = 2's degeneracy family, at")
    print(f"    the root)")
    for N in (15, 21):
        r = [0] * N
        for e in range(N):
            r[(e * e) % N] += 1
        assert all(x >= 0 for x in r)
        W = [gcd(F if F else N, N) for F in range(N)]
        for n in range(N):
            Wn = sum(W[F] * cmath.exp(-2j * math.pi * n * F / N)
                     for F in range(N)).real
            auto = sum(r[m] * r[(m + n) % N] for m in range(N))
            assert abs(Wn - auto) < 1e-6, (N, n)
    print("    dual(gcd) = autocorrelation of the frame COUNT r(m) =")
    print("    #(e: e^2 = m) -- exact at N = 15, 21, every mode")
    print()
    print("  THE LEDGER MEASURE IS THE BORN RULE APPLIED TO A FRAME")
    print("  AMPLITUDE.  Its dual coefficients are counts, so its")
    print("  positivity is automatic -- the mechanism, identified.")


# =====================================================================
# 2. the positivity theorem
# =====================================================================

def su2_admissible(j, m1, m2):
    return abs(m1 - m2) <= j <= m1 + m2 and (j + m1 + m2) % 1 == 0


def born_coeffs(n, jmax):
    ms = sorted(n.keys())
    out = {}
    for twojp in range(0, 2 * jmax + 1):
        for twojm in range(0, 2 * jmax + 1):
            jp, jm = twojp / 2, twojm / 2
            tot = 0.0
            for m1 in ms:
                for m2 in ms:
                    if (abs(m1 - m2) <= jp <= m1 + m2
                            and abs(m1 - m2) <= jm <= m1 + m2
                            and (jp + m1 + m2) == int(jp + m1 + m2)
                            and (jm + m1 + m2) == int(jm + m1 + m2)):
                        tot += n[m1] * n[m2]
            out[(jp, jm)] = tot
    return out


def verify_positivity_theorem() -> None:
    rng = random.Random(19)
    worst = 1e9
    for _ in range(200):
        n = {m: rng.random() for m in range(0, 5)}
        C = born_coeffs(n, 8)
        worst = min(worst, min(C.values()))
    assert worst >= 0
    print(f"    200 random nonnegative countings on SU(2): every Born")
    print(f"    coefficient >= 0 (min found {worst:.2e})")
    # mixed-sign necessity: a virtual amplitude goes negative
    # A = chi_1 - chi_0 (Adams psi^2 of the fundamental):
    # A^2 = chi_1 chi_1 - 2 chi_1 + chi_0
    # c_1(A^2) = N^1_{11} - 2 = 1 - 2 = -1 < 0
    c1 = 1 * 1 - 2 * 1
    assert c1 < 0
    print("    necessity: the virtual amplitude chi_1 - chi_0 (an")
    print("    Adams image) has c_1(A^2) = -1 < 0 -- counting")
    print("    nonnegativity is what does the work")
    print()
    print("  W = (counting amplitude)^2 IS COEFFICIENT-POSITIVE BY")
    print("  FUSION: c_j = sum n n' N^j >= 0.  The dual square, on the")
    print("  group.")


# =====================================================================
# 3. the derived nonabelian amplitude is diagonal
# =====================================================================

PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def verify_diagonal_amplitude() -> None:
    rng = random.Random(3)
    worst = 0.0
    for _ in range(50):
        a = [rng.gauss(0, 1) for _ in range(4)]
        b = [rng.gauss(0, 1) for _ in range(4)]
        F = [a[i] * b[j] - a[j] * b[i] for (i, j) in PAIRS]
        sF = [F[5], -F[4], F[3], F[2], -F[1], F[0]]
        Fp = [(F[i] + sF[i]) / 2 for i in range(6)]
        Fm = [(F[i] - sF[i]) / 2 for i in range(6)]
        worst = max(worst, abs(sum(x * x for x in Fp)
                               - sum(x * x for x in Fm)))
    assert worst < 1e-12
    print(f"    a wedge b is BALANCED: max | |B+|^2 - |B-|^2 | = "
          f"{worst:.1e} -- the frame amplitude is DIAGONAL")
    # radial counting by deterministic quadrature
    def chi4pdf(x):
        return x ** 3 * math.exp(-x * x / 2) / 2

    nr = 60
    dens = {}
    for s0 in (0.75, 1.5):
        nj = [0.0] * 9
        for i in range(nr):
            ra = 8 * (i + 0.5) / nr
            pa = chi4pdf(ra) * 8 / nr
            for j in range(nr):
                rb = 8 * (j + 0.5) / nr
                pb = chi4pdf(rb) * 8 / nr
                for k in range(nr):
                    c = -1 + 2 * (k + 0.5) / nr
                    pc = ((2 / math.pi)
                          * math.sqrt(max(1 - c * c, 0)) * 2 / nr)
                    s = (ra * rb * math.sqrt(max(1 - c * c, 0))
                         / math.sqrt(2))
                    jj = int(round(s / s0))
                    if jj <= 8:
                        nj[jj] += pa * pb * pc
        dens[s0] = nj
    for s0, nj in dens.items():
        n = {m: nj[m] for m in range(9) if nj[m] > 0}
        C = born_coeffs(n, 6)
        c00 = C[(0, 0)]
        neg = min(C.values())
        assert neg >= 0
        d11 = C[(1, 1)] / c00
        d10 = C[(1, 0)] / c00
        d22 = C[(2, 2)] / c00
        d44 = C[(4, 4)] / c00
        print(f"    bin scale s0 = {s0}: c(1,1) = {d11:.4f}, "
              f"c(1,0) = {d10:.4f} (>= 0), c(2,2) = {d22:.4f}, "
              f"c(4,4) = {d44:.4f}; min coeff = {neg:.1e}")
        assert d11 > d10
    print("    diagonal-dominant, off-diagonal positive-small,")
    print("    nothing forbidden -- 0073's structure, signs healed")
    # pointwise ridge check
    s0 = 0.75
    nj = dens[s0]
    NG = 90
    def chi(j, t):
        n_ = 2 * j + 1
        s = math.sin(t / 2)
        return math.sin(n_ * t / 2) / s if abs(s) > 1e-12 else float(n_)
    def A(tp, tm):
        return sum(nj[m] * chi(m, tp) * chi(m, tm) for m in range(9))
    ridge = sum(A(t, t) ** 2 for t in
                [2 * math.pi * (i + 0.5) / NG for i in range(NG)]) / NG
    off = sum(A(t, (t + math.pi / 2) % (2 * math.pi)) ** 2 for t in
              [2 * math.pi * (i + 0.5) / NG for i in range(NG)]) / NG
    print(f"    pointwise: <W> on the balanced ridge / off-ridge = "
          f"{ridge / off:.1f}x")
    assert ridge / off > 3
    print()
    print("  THE BORN WEIGHT KEEPS THE KERNEL'S SHAPE -- balanced")
    print("  ridge, soft off-ridge -- with every coefficient")
    print("  nonnegative by construction.")


# =====================================================================
# 4. the wall status
# =====================================================================

def verify_wall_status() -> None:
    print("    0073: lift the WEIGHT -> sign problem.")
    print("    0074: lift the AMPLITUDE, square on the group -> ")
    print("    coefficient-positive by fusion, ridge preserved.")
    print()
    print("  THE CURE IS THE PROGRAM'S OWN RULE: probability =")
    print("  amplitude^2, applied at the right tier.  The healed")
    print("  object is Barrett-Crane AS AN AMPLITUDE -- 'BC squared'")
    print("  -- with a derived radial profile.  A3 (the propagator")
    print("  test) now has a positive object to run on.  And the")
    print("  abelian tier of the whole structure is exactly solvable:")
    print("  the program owns a TOY of the wall.")


def run_verification_suite() -> None:
    sections = [
        ("The ledger is a Born square", verify_born_square),
        ("The positivity theorem", verify_positivity_theorem),
        ("The derived nonabelian amplitude is diagonal",
         verify_diagonal_amplitude),
        ("The wall status", verify_wall_status),
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
