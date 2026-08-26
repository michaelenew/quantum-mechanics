"""0130 -- the port: the coupling is a function of the level, and
"why is gravity weak" becomes a single number.

lucid 0045 resolved criticality item 1 on the filter side. The chain:

  - their bivector |a ^ b| IS the information volume of a record
    pair, sqrt(det J) -- verified exactly, so the port is legitimate;
  - the filter reproduces the 10^12 volatility as a QUANTISER-WIDTH
    problem, no geometry in it;
  - and equal-width binning is the wrong quantiser. A record spends
    its capacity, so at a fixed number of levels the entropy-
    maximising bins are EQUIPROBABLE -- which have EQUAL
    multiplicities. The profile is FLAT, uniquely. s0 was never a
    free parameter; it was a bad quantiser.

So 0091's flat counting was right, for a reason nobody had given,
and the coupling collapses to a closed form. This module ports that
and follows it where it goes.

  s1  THE CLOSED FORM, ON THIS SIDE. kappa = (M+2)(M-1)/3 with M
      the sector count, and M = N+1, so kappa = N(N+3)/3 and the
      band is 2N+1. Verified against the measured character
      coefficients of the actual weight.
  s2  THE (D) CHAIN, NOW SINGLE-VARIABLE. N -> kappa -> xi/a ->
      the strength of gravity. Every step is a function; there is
      no free parameter left between the level and the hierarchy.
  s3  INVERTED: WHAT N DOES THE OBSERVED WEAKNESS OF GRAVITY
      REQUIRE? This is the second, independent window on the scale
      that lucid 0044 said nobody had opened -- and it can be
      compared with 0096's n* = 58 route.
  s4  THE REMAINING BINARY. One record or two changes kappa by
      EXACTLY 12/5, so it shifts the required N by a computable
      amount rather than smearing it.
"""

import numpy as np

TH = np.linspace(1e-9, np.pi - 1e-9, 400001)
HAAR = (2 / np.pi) * np.sin(TH) ** 2
B0, B1 = 11 / (24 * np.pi ** 2), 17 / (96 * np.pi ** 4)


def chi(n):
    return np.sin(n * TH) / np.sin(TH)


def xi_over_a(beta):
    if not np.isfinite(beta) or beta <= 0:
        return float("nan")
    g2 = 4.0 / beta
    return 1.0 / ((B0 * g2) ** (-B1 / (2 * B0 ** 2))
                  * np.exp(-1 / (2 * B0 * g2)))


def kappa_closed(M):
    return (M + 2) * (M - 1) / 3.0


def s1_closed_form():
    print("== s1: the closed form, on this side ==")
    print("     M    measured kappa (from the weight)   "
          "(M+2)(M-1)/3   band")
    for M in (3, 4, 6, 8):
        A = sum(chi(n) for n in range(1, M + 1))
        W = np.maximum(A ** 2, 1e-300)
        sel = TH < 0.15
        k = float(-2 * np.polyfit(TH[sel], np.log(W[sel]), 4)[-3])
        band = 2 * M - 1
        print(f"    {M:2d}          {k:9.4f}                 "
              f"{kappa_closed(M):9.4f}     {band:3d}")
        assert abs(k - kappa_closed(M)) < 0.02
    print("  exact against the actual weight. With M = N + 1 "
          "sectors:")
    print("      kappa = N(N+3)/3 ,   band = 2N+1")
    print("  and for the program's N = 5: kappa = 13.333, band = 11 "
          "-- the numbers the")
    print("  lattice has been running on since 0091, now derived "
          "rather than chosen\n")


def s2_the_chain():
    print("== s2: the (D) chain, now single-variable ==")
    print("  N -> kappa -> xi/a -> how weak gravity is. No free "
          "parameter between them.")
    print("     N    kappa      xi/a          (a/xi)^2  "
          "[the coupling at the theory's own scale]")
    for N in (3, 4, 5, 6, 7, 9, 13):
        k = N * (N + 3) / 3
        x = xi_over_a(k)
        print(f"    {N:2d}   {k:8.3f}   {x:.3e}    {1 / x ** 2:.3e}")
    print()
    print("  THAT IS 'WHY IS GRAVITY WEAK' IN THE FULL THEORY: "
          "gravity is weak because the")
    print("  level is not small, and the hierarchy is DOUBLY "
          "exponential in it -- kappa")
    print("  grows like N^2 and xi/a grows like exp(c kappa). Two "
          "steps of the level buy")
    print("  eleven orders of magnitude\n")


def s3_invert():
    print("== s3: inverted -- what N does the observed weakness "
          "require? ==")
    # gravitational fine structure constant for a proton pair
    ALPHA_G = 5.9e-39
    LP_OVER_A = 2.27           # 0105, conditional on induced gravity
    print(f"  the gravitational coupling of a proton pair is "
          f"alpha_G = {ALPHA_G:.1e}.")
    print(f"  This program puts the Planck length at "
          f"{LP_OVER_A} lattice spacings (0105), and its own")
    print("  dynamical scale at xi. Taking the theory's scale as "
          "the one gravity is weak")
    print("  AT, alpha_G ~ (l_P / xi)^2 = "
          "(2.27 / (xi/a))^2, so:")
    need = LP_OVER_A / np.sqrt(ALPHA_G)
    print(f"      xi/a required = {LP_OVER_A} / sqrt(alpha_G) = "
          f"{need:.3e}")
    print()
    print("     N     xi/a          ratio to required")
    best, bd = None, 1e99
    for N in range(3, 12):
        k = N * (N + 3) / 3
        x = xi_over_a(k)
        r = x / need
        if abs(np.log10(r)) < bd:
            bd, best = abs(np.log10(r)), N
        print(f"    {N:2d}    {x:.3e}     {r:.2e}")
    print()
    print(f"  THE OBSERVED WEAKNESS OF GRAVITY REQUIRES N = {best} "
          f"(nearest integer level).")
    print(f"  0096's independent route -- pinning the level from "
          f"vacuum samples -- returns")
    print("  N = 5. The two windows differ by ONE LEVEL.")
    print()
    print("  That is the second independent determination lucid "
          "0044 said nobody had made,")
    print("  and it lands one step away from the first. Named "
          "honestly: this is an")
    print("  order-of-magnitude inversion, not a derivation -- it "
          "rests on l_P = 2.27a")
    print("  (conditional on the induced-gravity identification and "
          "its standing factor 20)")
    print("  and on identifying the scale gravity is weak AT with "
          "the theory's own xi.")
    print("  Both are named elsewhere as open. But the two windows "
          "agreeing to one level")
    print("  out of a range that spans forty orders of magnitude is "
          "not nothing\n")
    return best, need


def s4_binary(best, need):
    print("== s4: the remaining binary ==")
    print("  One record or two. Fusing self-dual and anti-self-dual "
          "streams multiplies")
    print("  kappa by EXACTLY 12/5 = 2.4 at every sector count "
          "(lucid 0045 s5), so:")
    print("     N     one record xi/a     two records xi/a    "
          "which matches the requirement")
    for N in range(3, 10):
        k1 = N * (N + 3) / 3
        k2 = 2.4 * k1
        x1, x2 = xi_over_a(k1), xi_over_a(k2)
        m = ("ONE" if abs(np.log10(x1 / need))
             < abs(np.log10(x2 / need)) else "two")
        print(f"    {N:2d}    {x1:.3e}        {x2:.3e}       {m}")
    print()
    print("  the two branches are far apart -- a factor 2.4 in "
          "kappa is many orders in xi --")
    print("  so the structural question is DECIDABLE against the "
          "requirement rather than")
    print("  degenerate with it. With two records the required "
          "level drops to N = 3-4.")
    print()
    print("  SO CRITICALITY ITEM 1 IS NO LONGER A FREE FUNCTION. It "
          "is: pick the level, pick")
    print("  one branch of a binary, and the coupling follows in "
          "closed form. Both remaining")
    print("  choices are the KIND of thing a theory can settle -- "
          "unlike a bin width\n")


if __name__ == "__main__":
    s1_closed_form()
    s2_the_chain()
    best, need = s3_invert()
    s4_binary(best, need)
    print("all assertions passed")
