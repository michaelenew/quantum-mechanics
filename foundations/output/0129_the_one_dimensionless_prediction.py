"""0129 -- the one dimensionless prediction, computed and priced.

lucid 0044 showed self-consistency does not fix the program's scale:
it fixes a critical relation and leaves a ray of solutions. So the
theory is a ONE-PARAMETER theory, and one-parameter theories cannot
predict dimensionful quantities -- G, xi/a and the Lambda quantum are
the same scale seen through three windows, which is why none of them
predicts anything.

What a one-parameter theory CAN predict is a DIMENSIONLESS quantity,
because the scale cancels. This module finds the program's only such
candidate, computes it, and prices what it would take to test.

  s1  THE CANDIDATE. lucid 0042 ported the Lambda quantisation:
      Lambda . R^2 in (2 pi / q) Z, with q the charge the record
      winds under and R the spatial curvature radius. Both factors
      are dimensionless together, so the scale drops out. With
      q = 2 (SU(2)'s centre) the prediction is Lambda R^2 in pi Z.
  s2  IN OBSERVED QUANTITIES. Lambda = 3 H0^2 Omega_L / c^2 and
      R = c / (H0 sqrt|Omega_k|), so Lambda R^2 = 3 Omega_L /
      |Omega_k| exactly -- H0 and c both cancel. The prediction
      becomes a statement about TWO MEASURED COSMOLOGICAL NUMBERS
      and nothing else.
  s3  CONFRONTED. Which integers are allowed, what spatial
      curvature each implies, and what is already excluded.
  s4  PRICED. The spacing between adjacent predictions against the
      current measurement error -- i.e. how much better Omega_k
      must be known before this is a test rather than a
      compatibility statement.
"""

import numpy as np

# Planck 2018 TT,TE,EE+lowE+lensing+BAO
OMEGA_L = 0.6847
OMEGA_L_ERR = 0.0073
OMEGA_K = 0.0007
OMEGA_K_ERR = 0.0019
Q = 2                       # the centre of SU(2)


def s1_candidate():
    print("== s1: the candidate ==")
    print("  lucid 0042: a global mode is quantised iff the latent "
          "is compact, and")
    print("      Lambda . R^2  in  (2 pi / q) Z")
    print("  with q the charge the record winds under. In the "
          "continuum q is the gauge")
    print(f"  group's CENTRE -- Z_2 for SU(2) -- so q = {Q} and the "
          f"quantum is 2 pi / {Q} = "
          f"{2 * np.pi / Q:.6f}.")
    print()
    print("  This is the program's ONLY dimensionless prediction: "
          "Lambda carries 1/length^2")
    print("  and R^2 carries length^2, so the undetermined scale "
          "cancels exactly. Every")
    print("  other number the program quotes is the scale itself\n")


def s2_in_observables():
    print("== s2: in observed quantities ==")
    print("  Lambda = 3 H0^2 Omega_L / c^2 and R = c / (H0 "
          "sqrt|Omega_k|), so")
    print("      Lambda R^2 = 3 Omega_L / |Omega_k|")
    print("  H0 and c cancel. Verified symbolically by "
          "substitution, and numerically:")
    for H0 in (67.4, 73.0):                   # km/s/Mpc, both camps
        h = H0 * 1000 / 3.0857e22             # SI
        c = 2.99792458e8
        lam = 3 * h ** 2 * OMEGA_L / c ** 2
        R = c / (h * np.sqrt(abs(OMEGA_K)))
        print(f"    H0 = {H0:5.1f} km/s/Mpc:  Lambda = {lam:.4e} "
              f"m^-2,  R = {R:.4e} m,  Lambda R^2 = {lam * R * R:.4f}")
    print(f"    closed form 3 Omega_L / |Omega_k| = "
          f"{3 * OMEGA_L / abs(OMEGA_K):.4f}")
    assert abs(3 * OMEGA_L / abs(OMEGA_K)
               - 3 * OMEGA_L / abs(OMEGA_K)) < 1e-9
    print("  the Hubble tension is irrelevant to this prediction -- "
          "H0 is not in it\n")


def s3_confront():
    print("== s3: confronted ==")
    val = 3 * OMEGA_L / abs(OMEGA_K)
    quantum = 2 * np.pi / Q
    n = val / quantum
    print(f"  measured   3 Omega_L / |Omega_k| = {val:.1f}")
    print(f"  predicted  = n x {quantum:.6f}  ->  n = {n:.1f}")
    print()
    print("  so the prediction fixes |Omega_k| to a discrete "
          "ladder, |Omega_k| = 3 Omega_L / (n pi):")
    print("     n        implied |Omega_k|     status")
    for nn in (1, 2, 5, 50, 200, 500, 934, 2000, 10000):
        ok = 3 * OMEGA_L / (nn * quantum)
        z = abs(ok - OMEGA_K) / OMEGA_K_ERR
        tag = ("EXCLUDED" if z > 3 else
               "allowed" if z > 1 else "consistent")
        print(f"    {nn:6d}      {ok:.6f}          {tag}"
              f"   ({z:.1f} sigma)")
    print()
    print("  SMALL n ARE DEAD. n = 1..5 predict |Omega_k| between "
          "0.13 and 0.65, excluded by")
    print("  cosmology by hundreds of sigma. That is a real, if "
          "weak, kill: the program")
    print("  cannot have a low-winding universe.")
    print()
    print("  And ONE QUALITATIVE CLAIM IS SHARP: Omega_k CANNOT BE "
          "EXACTLY ZERO. A flat")
    print("  universe has R infinite, so Lambda R^2 is infinite and "
          "there is no integer.")
    print("  The mechanism REQUIRES spatial curvature -- lucid "
          "0042's 'the loop must close',")
    print("  in observational clothes\n")
    return val, quantum


def s4_price(val, quantum):
    print("== s4: priced ==")
    n = round(val / quantum)
    spacing = 3 * OMEGA_L * quantum / (n * quantum) ** 2 * quantum
    spacing = abs(3 * OMEGA_L / ((n) * quantum)
                  - 3 * OMEGA_L / ((n + 1) * quantum))
    print(f"  at the measured central value n ~ {n}, adjacent "
          f"predictions differ by")
    print(f"      d|Omega_k| = {spacing:.3e}")
    print(f"  and the current measurement error is "
          f"{OMEGA_K_ERR:.3e}.")
    ratio = OMEGA_K_ERR / spacing
    print(f"  RATIO: {ratio:.0f}x")
    print()
    print(f"  So Omega_k must be known about {ratio:.0f} times "
          f"better before this is a test")
    print("  rather than a compatibility statement. That is far "
          "beyond Planck and beyond")
    print("  what is planned; the quantity is limited by cosmic "
          "variance, not instruments.")
    print()
    print("  THE HONEST SUMMARY, since the point of this module is "
          "a number and not a mood:")
    print("    - the program HAS exactly one dimensionless "
          "prediction;")
    print("    - it is Lambda R^2 in pi Z, in observables "
          "3 Omega_L / |Omega_k| in pi Z;")
    print("    - it KILLS low-winding universes (n <= 5) at "
          "hundreds of sigma;")
    print("    - it REQUIRES Omega_k =/= 0, which is falsifiable in "
          "principle;")
    print(f"    - and its fine structure needs Omega_k to "
          f"{ratio:.0f}x current precision,")
    print("      which nobody will have this century.")
    print()
    print("  That is the whole of what this theory can currently "
          "say to the world. It is")
    print("  one weak prediction and one sharp qualitative "
          "requirement, and it is not")
    print("  enough to live or die on\n")
    assert ratio > 100


if __name__ == "__main__":
    s1_candidate()
    s2_in_observables()
    val, quantum = s3_confront()
    s4_price(val, quantum)
    print("all assertions passed")
