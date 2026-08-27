"""0114 -- the degree: why alternatives are SUMMED, from the budget.

lucid 0034 closed the composition rule (amplitudes multiply in C)
and named the one step it had assumed rather than measured: why
amplitudes for ALTERNATIVES are added. This module closes it on the
physics side, and the closure needs no new postulate -- it is the
band budget again.

THE BRIDGE. Sorkin's interference hierarchy: for a measure on
histories, I_k is the k-th finite difference over k disjoint
bundles. A measure that is a form of DEGREE d in the amplitude has
I_{d+1} = 0 and I_d != 0. So the hierarchy MEASURES THE DEGREE, and
"alternatives are summed" is exactly "the degree is 2":
mu(S) = (sum_{i in S} a_i)^2 is the sum rule, and nothing else is.

  s1  THE PROGRAM'S OWN LEDGER HAS I_3 = 0 POINTWISE. The Born
      weight W = A^2 with A = sum_{j<=5/2} chi_j. Split A into three
      parts any way at all; the third-order interference vanishes
      identically in theta, to machine precision -- not as a fit,
      as an algebraic identity of a quadratic form.
  s2  THE HIERARCHY MEASURES THE DEGREE. For mu = (sum a)^d, I_3 is
      the third finite difference: 0 for d = 2, 6 a1 a2 a3 for
      d = 3, and large for d = 10. Measured against the weight
      itself, a wrong degree is not a small correction.
  s3  THE BUDGET NARROWS THE DEGREE TO FOUR VALUES, AND THREE DIE.
      The record's band is B = 11 characters (measured here: the
      coefficients are 6,10,13,14,14,12,9,6,4,2,1 and then exactly
      0). A degree-d weight needs an amplitude of band M with
      d(M-1) + 1 = B, so d must divide B - 1 = 10: d in
      {1, 2, 5, 10}. Then
        d = 1  -> no interference AT ALL (I_2 = 0), excluded by
                  lucid 0033/0034's measured 0.302 nats/trial;
        d = 5  -> odd power of an amplitude that changes sign
                  (measured), so the weight goes negative: not a
                  measure;
        d = 10 -> nonnegative and in band, but a degree-10 form has
                  I_3 != 0 (measured here), and third-order
                  interference is absent;
        d = 2  -> survives.
      DEGREE 2 IS FORCED, AND DEGREE 2 IS THE SUM RULE. The last
      postulate in the source ledger is discharged by the same
      budget that fixed the band.
"""

import numpy as np

TH = np.linspace(1e-9, np.pi - 1e-9, 400001)
HAAR = (2 / np.pi) * np.sin(TH) ** 2
MMAX = 6                      # chi_1 .. chi_6  (j <= 5/2, N = 5)
rng = np.random.default_rng(114)


def chi(n):
    return np.sin(n * TH) / np.sin(TH)


def coef(f, n):
    return float(np.trapezoid(f * chi(n) * HAAR, TH))


def band(f, tol=1e-6):
    b = 0
    for n in range(1, 40):
        if abs(coef(f, n)) > tol:
            b = n
    return b


def I3(parts, d):
    """third finite difference of mu(S) = (sum_{i in S} a_i)^d"""
    a, b, c = parts
    return ((a + b + c) ** d - (a + b) ** d - (a + c) ** d
            - (b + c) ** d + a ** d + b ** d + c ** d)


def split3(nmax, key):
    """Decompose A = a1 + a2 + a3 as FUNCTIONS: each character's
    coefficient is divided among three alternatives. Alternatives
    are bundles of histories, not partitions of the character set,
    so this is the general decomposition -- and it exists for any
    band, including M = 2."""
    w = rng.dirichlet(np.ones(3), size=nmax)          # nmax x 3
    return [sum(w[n, g] * chi(n + 1) for n in range(nmax))
            for g in range(3)], np.round(w[:, 0], 2)


def s1_pointwise_zero():
    print("== s1: the program's own ledger has I_3 = 0 pointwise ==")
    A = sum(chi(n) for n in range(1, MMAX + 1))
    W = A ** 2
    print(f"  W = A^2, A = sum_{{j<=5/2}} chi_j;  max|W| = "
          f"{W.max():.1f}")
    for t in range(4):
        parts, lab = split3(MMAX, t)
        assert np.abs(sum(parts) - A).max() < 1e-9
        r = I3(parts, 2)
        print(f"  split (a1 weights {list(lab)}):  sup|I_3| = "
              f"{np.abs(r).max():.3e}   (relative to sup W: "
              f"{np.abs(r).max() / W.max():.2e})")
        assert np.abs(r).max() < 1e-9
    print("  identically zero in theta, for every partition: an "
          "algebraic identity of a")
    print("  quadratic form, not a fitted smallness\n")


def s2_hierarchy_measures_degree():
    print("== s2: the hierarchy measures the degree ==")
    parts, lab = split3(MMAX, 9)
    a, b, c = parts
    print("   d     sup|I_3|        sup|mu(123)|      ratio")
    for d in (1, 2, 3, 5, 10):
        r = I3(parts, d)
        mu = (a + b + c) ** d
        ratio = np.abs(r).max() / max(np.abs(mu).max(), 1e-30)
        print(f"  {d:3d}   {np.abs(r).max():12.4e}   "
              f"{np.abs(mu).max():12.4e}   {ratio:.3f}")
        if d in (1, 2):
            assert np.abs(r).max() < 1e-8
        else:
            assert ratio > 1e-3
    # the exact d = 3 identity
    r3 = I3(parts, 3)
    print(f"  (d = 3 is exactly 6 a1 a2 a3: max deviation "
          f"{np.abs(r3 - 6 * a * b * c).max():.2e})")
    assert np.abs(r3 - 6 * a * b * c).max() < 1e-8
    print("  d = 1 and d = 2 are the only degrees with no "
          "third-order interference, and")
    print("  d = 1 has no SECOND-order interference either -- it is "
          "the classical measure\n")


def s3_budget_narrows():
    print("== s3: the budget narrows the degree, and three die ==")
    A = sum(chi(n) for n in range(1, MMAX + 1))
    W = A ** 2
    B = band(W)
    cs = [round(coef(W, n), 6) for n in range(1, 14)]
    print(f"  measured band of the record weight: B = {B}   "
          f"coefficients {cs[:11]}")
    print(f"  then {cs[11:]}")
    assert B == 11
    divisors = [d for d in range(1, B) if (B - 1) % d == 0]
    print(f"  d(M-1) + 1 = B  =>  d | (B-1) = {B - 1}  =>  d in "
          f"{divisors}")
    print()
    print("   d    M    amplitude sign-changes?   weight "
          "nonneg?   I_2      I_3      verdict")
    for d in divisors:
        M = (B - 1) // d + 1
        Am = sum(chi(n) for n in range(1, M + 1))
        neg = bool(np.any(Am < -1e-9))
        Wd = Am ** d
        nonneg = bool(np.all(Wd > -1e-9))
        # interference orders for this degree, on a 3-way split of
        # the M-character amplitude (or a 2-way one when M = 2)
        parts, _ = split3(M, d)
        a, b, c = parts
        i2 = np.abs((a + b) ** d - a ** d - b ** d).max()
        i3 = np.abs(I3(parts, d)).max()
        scale = max(np.abs((a + b + c) ** d).max(), 1e-30)
        if d == 1:
            verdict = "no interference at all -- excluded by lucid 0033"
        elif d % 2 == 1:
            verdict = "weight goes negative -- not a measure"
        elif i3 / scale > 1e-3:
            verdict = "third-order interference -- absent in the record"
        else:
            verdict = "SURVIVES"
        print(f"  {d:3d}  {M:3d}         {str(neg):5s}"
              f"              {str(nonneg):5s}   "
              f"{i2 / scale:7.3f}  {i3 / scale:7.3f}   {verdict}")
        if d == 2:
            assert verdict == "SURVIVES"
        else:
            assert verdict != "SURVIVES"
    print()
    print("  DEGREE 2 IS FORCED. A degree-2 measure is "
          "mu(S) = (sum_{i in S} a_i)^2 --")
    print("  which IS the statement that amplitudes for "
          "alternatives are SUMMED.")
    print("  The band budget (0118) fixed the band; the band fixes "
          "the degree; the degree")
    print("  is the sum rule. No postulate was added\n")


if __name__ == "__main__":
    s1_pointwise_zero()
    s2_hierarchy_measures_degree()
    s3_budget_narrows()
    print("all assertions passed")
