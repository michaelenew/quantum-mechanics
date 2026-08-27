"""0160 -- the null space: where this theory sits among its own kin.

Not "what other theories exist" but the narrower and answerable
question: given everything this program forces, what is left free,
and what shape is the residual space?

The chain is: a level N, a band B = 2N+1, M = N+1 characters, flat
multiplicities (forced by capacity), the double copy (measured), and
kappa read off the weight's curvature. Everything in that chain is
forced EXCEPT N -- and 0127 scored that plainly: "No knob has been
derived", with the level reclassified as "the world's data, not the
law's".

So the space is parametrised by N. This prices it.

  s1  THE ADMISSIBLE LADDER. 0081: N odd with x^2 = -1 (mod N).
      Enumerate it, and check the classical characterisation.
  s2  KAPPA ALONG THE LADDER, in closed form, gated against the
      measured 16.0001.
  s3  THE HIERARCHY ALONG THE LADDER.
  s4  POINT, ISLAND, OR LINE?
"""

import numpy as np

B0 = 11.0 / (24 * np.pi ** 2)
B1 = 17.0 / (96 * np.pi ** 4)
BETA_OVER_KAPPA = 17.637 / 16.0     # 0155's non-perturbative match


def admissible(nmax=200):
    """N odd with a solution to x^2 = -1 (mod N)."""
    out = []
    for N in range(1, nmax + 1, 2):
        if any((x * x + 1) % N == 0 for x in range(N)):
            out.append(N)
    return out


def prime_factors(n):
    f, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            f.add(d)
            n //= d
        d += 1
    if n > 1:
        f.add(n)
    return f


def kappa_double(M):
    """(2/3) sum n^2(n^2-1) / sum n^2, in closed form."""
    n = np.arange(1, M + 1, dtype=float)
    exact = (2.0 / 3.0) * np.sum(n ** 2 * (n ** 2 - 1)) / np.sum(n ** 2)
    closed = (2.0 / 5.0) * (M + 2) * (M - 1)
    return exact, closed


def aLambda(beta):
    g2 = 4.0 / beta
    return (B0 * g2) ** (-B1 / (2 * B0 ** 2)) * np.exp(
        -1.0 / (2 * B0 * g2))


def s1_ladder():
    print("== s1: the admissible ladder ==")
    print("  0081: N odd, and x^2 = -1 (mod N) must be solvable.")
    lad = admissible(120)
    print(f"  ladder to 120: {lad}")
    print()
    print("  Classical characterisation: solvable exactly when every "
          "prime factor of N")
    print("  is 1 mod 4. Checked:")
    ok = True
    for N in lad:
        good = all(p % 4 == 1 for p in prime_factors(N)) or N == 1
        ok &= good
    for N in range(1, 121, 2):
        pred = all(p % 4 == 1 for p in prime_factors(N)) or N == 1
        ok &= (pred == (N in lad))
    print(f"    agrees on every odd N to 120: {ok}")
    assert ok
    print()
    print("  So the level is not free -- it is confined to a "
          "DISCRETE ARITHMETIC LADDER.")
    print("  That is a real constraint, and it is the program's "
          "own (0081).")
    print()
    return lad


def s2_kappa(lad):
    print("== s2: kappa along the ladder ==")
    print("  M = N + 1 characters, and the double copy gives")
    print("      kappa = (2/3) sum n^2(n^2-1) / sum n^2 "
          "= (2/5)(M+2)(M-1) = (2/5) N (N+3).")
    print()
    e6, c6 = kappa_double(6)
    print(f"  gate at N = 5 (M = 6):  exact {e6:.6f}, closed form "
          f"{c6:.6f}, measured 16.0001 (0141)")
    assert abs(e6 - c6) < 1e-9 and abs(e6 - 16.0) < 1e-9
    print()
    print("     N      M      kappa")
    for N in lad[:7]:
        e, c = kappa_double(N + 1)
        print(f"    {N:3d}    {N + 1:3d}    {e:10.3f}")
    print()
    print("  kappa is DERIVED GIVEN N. It is not derived.")
    print()


def s3_hierarchy(lad):
    print("== s3: the hierarchy along the ladder ==")
    print("  Using 0155's non-perturbative matching ratio "
          f"beta/kappa = {BETA_OVER_KAPPA:.4f}")
    print("  (measured at N = 5 and assumed to carry along the "
          "ladder -- flagged, not")
    print("  established).")
    print()
    print("     N        kappa       beta_W        xi / a")
    vals = []
    for N in lad[:6]:
        k, _ = kappa_double(N + 1)
        b = k * BETA_OVER_KAPPA
        al = aLambda(b)
        lx = -np.log10(al) if al > 0 else (
            (1.0 / (2 * B0 * (4.0 / b))) / np.log(10))
        vals.append((N, k, b, lx))
        print(f"    {N:3d}   {k:10.3f}   {b:9.3f}    "
              f"10^{lx:.1f}")
    print()
    lo, hi = vals[1][3], vals[2][3]
    print(f"  ADJACENT RUNGS N = 5 AND N = 13 DIFFER BY "
          f"{hi - lo:.0f} ORDERS in the")
    print("  hierarchy. The observable the program calls its first "
          "derived-and-large")
    print("  number swings by that much between one rung and the "
          "next.")
    print()
    print("  AND THE FLIP SIDE, which is the interesting half. "
          "Observationally the")
    print("  hierarchy has to land near 10^19-10^20. Look at what "
          "the ladder offers:")
    print()
    print("     N = 1    10^1.6    -- no hierarchy at all")
    print("     N = 5    10^19.8   -- the observed ballpark")
    print("     N = 13   10^106    -- absurd")
    print()
    print("  ONLY ONE RUNG IS PHYSICAL. The arithmetic ladder plus "
          "the demand for a")
    print("  hierarchy anywhere near reality picks out N = 5 and "
          "nothing else -- the")
    print("  spacing between rungs is so violent that the "
          "selection is unambiguous.")
    print()
    print("  Whether that counts as a derivation or as a one-bit "
          "fit is exactly the")
    print("  question, and it is the same epistemic move as "
          "Weinberg's anthropic bound on")
    print("  Lambda: a constraint plus an observation, selecting a "
          "value nothing derives.")
    print("  Weinberg's got the number right before it was "
          "measured, and it is still the")
    print("  least-loved successful prediction in physics.")
    print()
    return vals


def s4_verdict(lad, vals):
    print("== s4: point, island, or line? ==")
    print()
    print("  NOT A LINE. The level is confined to N odd with "
          "x^2 = -1 (mod N) -- every")
    print("  prime factor 1 mod 4. That is a genuine arithmetic "
          "constraint and it kills a")
    print("  continuum.")
    print()
    print("  NOT A POINT. Nothing in the program selects a rung. "
          "0127 says so in its own")
    print("  words: the level is reclassified as \"the world's "
          "data, not the law's\", and")
    print("  \"No knob has been derived\". 0120 found the one "
          "argument that looked like it")
    print("  selected N = 5 to be a coincidence at a single point, "
          "with the ratio drifting")
    print("  7.2x across the ladder.")
    print()
    print("  IT IS AN ISLAND ARCHIPELAGO -- a discrete ladder with "
          "one rung occupied by")
    print("  fiat. And the price is now explicit:")
    print()
    print("    * kappa = 16.0001 is derived GIVEN N = 5, exactly "
          "and with no freedom.")
    print("    * N = 5 is chosen, not derived.")
    print(f"    * the hierarchy moves {vals[2][3] - vals[1][3]:.0f} "
          f"orders between adjacent rungs, so only")
    print("      N = 5 is observationally admissible at all.")
    print()
    print("  So the honest form of the program's headline claim is "
          "NOT 'a derived")
    print("  coupling'. It is:")
    print()
    print("    ONE INTEGER IN, EVERYTHING ELSE OUT.")
    print()
    print("  That is a much better claim than it sounds, and much "
          "weaker than 'derived'.")
    print("  Better, because the Standard Model takes nineteen "
          "real numbers and this")
    print("  takes one integer from a constrained ladder. Weaker, "
          "because one free")
    print("  integer that swings the answer by thirty orders is "
          "not a prediction, and")
    print("  0069's conversion bar asked for a derived knob, which "
          "this is not.")
    print()
    print("  AND IT NAMES THE ONE COMPUTATION THAT WOULD CHANGE "
          "EVERYTHING. Not a better")
    print("  lattice run. A reason for the rung. Every other open "
          "item in this program is")
    print("  worth less than that one.")
    print()


if __name__ == "__main__":
    lad = s1_ladder()
    s2_kappa(lad)
    v = s3_hierarchy(lad)
    s4_verdict(lad, v)
    print("all assertions passed")
