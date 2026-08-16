"""The Newtonian limit: the vacuum principle selects the profile.

0035 ended on the sharpest gap between the web and observed
gravity: the web's constant-w point channel is a global monopole --
g_00 = -1 + w constant, hence NO ATTRACTION -- while GR's point
mass is the same Kerr-Schild form with the profile w = 2M/(u.ell).
This module shows the gap closes from the web's own field law.

THE PRINCIPLE.  The 2+1 web's measured field equation was
K = pi s / det g: curvature lives exactly where participation is,
and the field is FLAT OFF-SOURCE (0020, machine-checked).  Lift
that principle to the 4D null-channel metric: off-source, the
implied matter G_mu_nu must vanish.  That single demand selects the
strength profile.

  s1  THE VACUUM SELECTION.  For w(rho) = w0 (r0/rho)^p, the
      off-source Ricci vanishes at p = 1 (8e-7) and at NO other
      exponent tested (p = 0, 0.5, 1.5, 2 all fail by 4-5 orders).
      Within power laws, the web's flat-off-participation law
      forces w = 2M/rho -- the Schwarzschild profile.  (Full
      uniqueness beyond power laws is Birkhoff's theorem,
      imported.)

  s2  NO FORCE WITHOUT THE PROFILE; NEWTON WITH IT.  Geodesics:
      a test particle at rest near the constant-w point stays at
      rest (radial acceleration 0 to machine precision -- the 2+1
      "no pair force" lifted); with w = 2M/rho the acceleration is
      -M/r^2 to six digits at two radii.  ATTRACTION IS THE
      PROFILE, and the profile is the vacuum principle.

  s3  KEPLER.  Circular-geodesic angular velocity from the
      Christoffels: omega^2 r^3 = M to six digits at two radii --
      the third law, exact (in Kerr-Schild coordinates the areal
      radius and time make it exact, not merely weak-field).

  s4  THE LEDGER'S FIFTH HALF-EXPONENT (theory registration, no
      assert).  In 3D an isotropically diluting information flux
      falls as 1/rho^2; a strength that runs as the SQUARE ROOT of
      flux runs as 1/rho -- exactly the selected profile.  The 1/2
      exponent now appears five times: trust = sqrt(information),
      amplitude = sqrt(probability), loop-tier screening
      det^(-1/2), the codim ladder's (1+w)^(-1/2) per transverse
      dimension, and strength = sqrt(flux) => Newton.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_t = importlib.import_module("0030_the_time_sector")
ks_metric = _t.ks_metric
ricci4 = _t.ricci4
christ4 = _t.christ4

M_N = 0.005


def g_profile(w0, p, r0=1.0):
    """Static point channel with strength profile w = w0 (r0/r)^p."""
    def k(x):
        r = math.dist(x[1:], (0, 0, 0))
        return (-1.0, x[1] / r, x[2] / r, x[3] / r)

    def w(x):
        r = math.dist(x[1:], (0, 0, 0))
        return w0 * (r0 / r) ** p
    return ks_metric(k, w)


def rest_accel(g, r):
    """Radial acceleration of a particle at rest at radius r."""
    pt = (0.0, r, 0.0, 0.0)
    G = christ4(g, pt, 1e-4)
    g00 = g(pt)[0][0]
    return -G[1][0][0] / (-g00)


def omega_circ(g, r):
    """Circular-geodesic angular velocity at radius r (xy-plane)."""
    pt = (0.0, r, 0.0, 0.0)
    G = christ4(g, pt, 1e-4)
    om = math.sqrt(max(G[1][0][0] / r, 1e-30))
    for _ in range(60):
        v = r * om
        rhs = G[1][0][0] + 2 * G[1][0][2] * v + G[1][2][2] * v * v
        om = math.sqrt(max(rhs / r, 1e-30))
    return om


# =====================================================================
# 1. the vacuum selection
# =====================================================================

def verify_vacuum_selection() -> None:
    print("    off-source max|R_mn| for w = w0 (r0/rho)^p "
          "(r = 0.9, 1.4):")
    results = {}
    for p in (0.0, 0.5, 1.0, 1.5, 2.0):
        g = g_profile(0.1, p)
        ms = []
        for r in (0.9, 1.4):
            pt = (0.0, r * 0.6, r * 0.64, r * 0.48)
            Ric = ricci4(g, pt, h=1e-3)
            ms.append(max(abs(Ric[i][j])
                          for i in range(4) for j in range(4)))
        results[p] = ms
        tag = "  <-- VACUUM" if max(ms) < 1e-5 else ""
        print(f"      p = {p}: {ms[0]:.1e}  {ms[1]:.1e}{tag}")
    assert max(results[1.0]) < 1e-5
    for p in (0.0, 0.5, 1.5, 2.0):
        assert min(results[p]) > 1e-3, (p, results[p])
    print()
    print("  THE WEB'S OWN LAW SELECTS THE PROFILE: flat-off-")
    print("  participation (2+1: K = pi s, measured) lifted to 4D")
    print("  (G_mn = 0 off-source) forces w = 2M/rho within power")
    print("  laws -- the Schwarzschild profile.  (Uniqueness beyond")
    print("  power laws is Birkhoff, imported.)")


# =====================================================================
# 2. no force without the profile; Newton with it
# =====================================================================

def verify_newton() -> None:
    gM = g_profile(0.1, 0.0)
    gS = g_profile(2 * M_N, 1.0)
    for r in (1.0, 2.0):
        aM = rest_accel(gM, r)
        aS = rest_accel(gS, r)
        newton = -M_N / r ** 2
        assert abs(aM) < 1e-8, aM
        assert abs(aS - newton) / abs(newton) < 1e-3, (aS, newton)
        print(f"    r = {r}: constant-w a_r = {aM:+.2e};  "
              f"w = 2M/rho a_r = {aS:+.6f}")
        print(f"           (Newton -M/r^2 = {newton:+.6f})")
    print()
    print("  THE BARE WEB POINT DOES NOT ATTRACT (the 2+1 no-pair-")
    print("  force, lifted); with the vacuum-selected profile the")
    print("  attraction is Newton's, exactly.  Gravity's pull is the")
    print("  strength profile, and the profile is the field law.")


# =====================================================================
# 3. Kepler
# =====================================================================

def verify_kepler() -> None:
    gS = g_profile(2 * M_N, 1.0)
    for r in (1.0, 2.0):
        om = omega_circ(gS, r)
        k3 = om * om * r ** 3
        assert abs(k3 - M_N) / M_N < 1e-3, (k3, M_N)
        print(f"    r = {r}: omega^2 r^3 = {k3:.6f} vs M = {M_N:.6f}")
    print()
    print("  KEPLER'S THIRD LAW, exact -- circular geodesics of the")
    print("  selected profile orbit like planets.")


# =====================================================================
# 4. the ledger's fifth half-exponent
# =====================================================================

def verify_ledger() -> None:
    print("  Registration (no assert): in 3D, diluting information")
    print("  flux ~ 1/rho^2; strength = sqrt(flux) ~ 1/rho -- the")
    print("  selected profile.  The 1/2 exponent's five appearances:")
    print("    trust = sqrt(information)        (stat-tracker)")
    print("    amplitude = sqrt(probability)    (Born)")
    print("    loop screening = det^(-1/2)      (0029)")
    print("    codim ladder step = (1+w)^(-1/2) (0033/0035)")
    print("    strength = sqrt(flux) => Newton  (here)")
    print("  Whether the web derives the profile this way (channel")
    print("  strength as amplitude of diluted participation flux) is")
    print("  the open derivation; the selection itself is measured.")


def run_verification_suite() -> None:
    sections = [
        ("The vacuum selection", verify_vacuum_selection),
        ("No force without the profile; Newton with it",
         verify_newton),
        ("Kepler", verify_kepler),
        ("The ledger's fifth half-exponent", verify_ledger),
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
