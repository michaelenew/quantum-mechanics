"""What the theory actually predicts differently, and whether data kills it.

A theory is an interpretation until it is falsifiable.  This module
asks, for the one place the program looked like it deviated from
general relativity -- 0020's ambient screening, delta = pi w /
sqrt(det A0) -- exactly what the delta is and whether current data
already excludes it.  The answer is sharper than expected, and it
CORRECTS 0058 s3.1, which listed the screening law as a
modified-gravity prediction.

  s1  THE ONE-BODY SECTOR IS EXACTLY SCHWARZSCHILD; THE DELTA IS
      ZERO.  0037 measured a perihelion advance exceeding 6 pi M/p
      by a factor 1.053 at M/p = 0.011 and 1.021 at M/p = 0.0044,
      and flagged the excess as "the second-order term."  It is:
      integrating the exact Schwarzschild orbit equation
        (du/dphi)^2 = 2M (u-u1)(u2-u)(u3-u)
      at the same orbit (r_p = 0.3, a = 0.6, so e = 0.5, p = 0.45)
      gives ratios 1.0532 and 1.0205, excess coefficients 4.84 and
      4.67 against the module's measured ~4.8.  The model's excess
      IS general relativity's own second-order term.  There is no
      deviation in the one-body sector at all -- the Kerr-Schild
      point channel is Schwarzschild exactly, so beta = gamma = 1
      and every classical test is passed by construction, not by
      coincidence.

  s2  SO THE SCREENING CANNOT BE A PHYSICAL VARYING G -- AND IF IT
      WERE, IT IS ALREADY DEAD.  Read naively, delta = pi w /
      sqrt(det A0) with ambient a ~ 2 GM/(r c^2) says
        G_eff = G (1 + 2U)^(-1/2) ~ G (1 - U),   U = GM/(r c^2)
      i.e. the local coupling runs with the AMBIENT NEWTONIAN
      POTENTIAL.  That is a definite, testable claim, and lunar
      laser ranging refutes it: Earth's orbital eccentricity
      e = 0.0167 modulates U_sun by 3.30e-10 over a year, so the
      lunar semi-major axis would breathe by a * Delta G/G =
      127 mm against LLR's ~1 mm precision -- excluded by a factor
      of ~127.  An O(1) shift in the PPN parameter beta is
      independently excluded ~12500x (|beta-1| < 8e-5, LLR
      Nordtvedt).  Combined with s1, the conclusion is forced:
      **the screening is bookkeeping in the w-parameterization, not
      a physical modification of the coupling.**  Note the ambient
      A0 is a CONSTANT SPD metric, hence flat (0020 s1 step 5 says
      so itself), and a flat background cannot change a defect's
      Gauss-Bonnet deficit -- consistent with 0012's exact result
      that deficits ADD.

  s3  WHERE FALSIFIABILITY ACTUALLY LIVES: THE TWO-BODY RULE.  The
      program's only unfixed dynamical freedom is 0037's measured
      O(M1 M2) violation of the field equation by superposed
      channels (coefficient ~48, scaling exactly as M1 M2).  The
      theory currently makes NO two-body prediction -- 0037 lists
      the fix rule as open, with screening a candidate.  That is
      the whole falsifiable surface, and it is binary:
        - if the fixed two-body rule reproduces Einstein-Infeld-
          Hoffmann, the theory equals GR at 1PN and is not
          falsifiable there;
        - if it does not, the mismatch enters at |beta - 1| ~ O(1),
          which the same LLR/Cassini bounds exclude by ~10^4.
      There is no third option and no tunable parameter to absorb
      the difference.  So the single highest-value computation in
      the program is the two-body rule vs EIH.

Run directly for the verification suite.
"""

from __future__ import annotations

import math

C = 2.99792458e8
GM_SUN = 1.32712440018e20
GM_EARTH = 3.986004418e14
AU = 1.495978707e11
R_EARTH = 6.371e6
A_MOON = 3.844e8
ECC_EARTH = 0.0167
LLR_PRECISION_M = 1e-3

# 0037/output-0032 orbit: run_orbit(M, r_p=0.3, a_t=0.6)
R_P, A_T = 0.3, 0.6
MEASURED = {0.011: 1.053, 0.0044: 1.021}


# =====================================================================
# 1. the one-body sector is exactly Schwarzschild
# =====================================================================

def exact_advance(M, p, e, n=200000):
    """Perihelion advance per orbit for an exact Schwarzschild
    timelike geodesic, via (du/dphi)^2 = 2M (u-u1)(u2-u)(u3-u)."""
    u1, u2 = (1 - e) / p, (1 + e) / p
    u3 = 1 / (2 * M) - (u1 + u2)
    A, B = (u1 + u2) / 2, (u2 - u1) / 2
    total = 0.0
    for i in range(n):
        th = -math.pi / 2 + math.pi * (i + 0.5) / n
        total += 1.0 / math.sqrt(2 * M * (u3 - A - B * math.sin(th)))
    return 2 * total * math.pi / n - 2 * math.pi


def verify_one_body() -> None:
    e = 1 - R_P / A_T
    p = A_T * (1 - e * e)
    print(f"    0037's orbit: r_p = {R_P}, a = {A_T} -> e = {e:.3f}, "
          f"p = {p:.4f}")
    for Mp, measured in sorted(MEASURED.items(), reverse=True):
        M = Mp * p
        adv = exact_advance(M, p, e)
        pred = 6 * math.pi * M / p
        ratio = adv / pred
        print(f"      M/p = {Mp:.4f}: exact GR ratio {ratio:.4f}, "
              f"0037 measured {measured:.4f}, "
              f"excess/(M/p) = {(ratio - 1) / Mp:.2f}")
        assert abs(ratio - measured) < 1e-3, (Mp, ratio, measured)
    print()
    print("  THE MODEL'S PERIHELION EXCESS IS GR'S OWN SECOND-ORDER")
    print("  TERM.  0037 flagged the 1.053/1.021 ratios as a gap to")
    print("  Einstein's formula; exact Schwarzschild gives the same")
    print("  numbers.  The Kerr-Schild point channel IS Schwarzschild,")
    print("  so beta = gamma = 1 and the one-body delta is ZERO.")


# =====================================================================
# 2. the naive varying-G reading, and its death certificate
# =====================================================================

def potential(GM, r):
    return GM / (r * C * C)


def verify_varying_g_excluded() -> None:
    rows = [
        ("Earth surface (Earth's own)", potential(GM_EARTH, R_EARTH)),
        ("Sun at Earth's orbit", potential(GM_SUN, AU)),
        ("Galaxy at the Sun (v = 220 km/s)", (220e3 / C) ** 2),
    ]
    print("    ambient potential U = GM/(r c^2):")
    for name, val in rows:
        print(f"      {name:34s} {val:.3e}")
    u_sun = potential(GM_SUN, AU)
    du = u_sun * 2 * ECC_EARTH
    breathe = A_MOON * du
    factor = breathe / LLR_PRECISION_M
    print(f"    if G_eff = G(1 - U): Earth's eccentricity modulates")
    print(f"      U_sun by {du:.3e} annually, so the lunar orbit")
    print(f"      breathes by a*dG/G = {breathe * 1e3:.1f} mm against")
    print(f"      LLR's ~1 mm -> EXCLUDED by {factor:.0f}x")
    assert factor > 50, factor
    beta_bound = 8e-5
    print(f"      and an O(1) shift in PPN beta is excluded "
          f"{1 / beta_bound:.0f}x (|beta-1| < {beta_bound:.0e})")
    print()
    print("  SO THE SCREENING IS NOT A PHYSICAL VARYING G.  Section 1")
    print("  shows the one-body sector is exactly GR; this section")
    print("  shows the naive varying-G reading is already dead.  The")
    print("  two together force the remaining reading: the screening")
    print("  is bookkeeping in the w-parameterization.  Consistent")
    print("  with 0020's own observation that a constant ambient is")
    print("  FLAT, and with 0012's exact result that deficits ADD --")
    print("  a flat background cannot change a Gauss-Bonnet deficit.")


# =====================================================================
# 3. the falsifiable surface is the two-body rule
# =====================================================================

def verify_falsifiable_surface() -> None:
    print("    0037 measured the superposition's field-equation")
    print("    violation scaling exactly as M1*M2 (48.7 / 48.3 / 48.2")
    print("    over a 4x range) -- the only unfixed dynamical freedom.")
    viol = [48.7, 48.3, 48.2]
    spread = (max(viol) - min(viol)) / (sum(viol) / len(viol))
    print(f"      coefficient spread over 4x in mass: {spread:.3%}")
    assert spread < 0.02, spread
    print("    The theory makes NO two-body prediction yet: 0037 lists")
    print("    the fix rule as open, with screening only a candidate.")
    print()
    print("  THE FALSIFIABLE SURFACE IS THE TWO-BODY RULE, AND IT IS")
    print("  BINARY.  Fix the rule; compare to Einstein-Infeld-")
    print("  Hoffmann.  Match => the theory equals GR at 1PN and is")
    print("  not falsifiable there.  Mismatch => |beta-1| ~ O(1),")
    print("  excluded by ~10^4.  No free parameter can absorb the")
    print("  difference, so this one computation decides it.")


def run_verification_suite() -> None:
    sections = [
        ("The one-body sector is exactly Schwarzschild",
         verify_one_body),
        ("The naive varying-G reading is already excluded",
         verify_varying_g_excluded),
        ("The falsifiable surface is the two-body rule",
         verify_falsifiable_surface),
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
