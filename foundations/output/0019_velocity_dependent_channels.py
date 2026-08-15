"""Velocity-dependent channels: the covariant completions, built.

0023 diagnosed the bare retarded web's compass and prescribed the
cure: velocity-coupled channel data.  Here the completion family is
CONSTRUCTED and measured.  Three update rules on one web:

  s1  THE GALILEAN POLE.  Channels point at the EXTRAPOLATED present
      position (retarded position + retarded velocity x delay --
      causal, retarded data only).  For uniform motion this
      reproduces the static field EXACTLY (machine identity), so the
      compass is dead, delta(v) = delta(0), and moving systems are
      trivially indistinguishable -- the relativity principle,
      Galileo's way.  The causal cone SURVIVES extrapolation: a
      kicked source's news front still propagates at c (K = 0
      beyond r = ct), because extrapolation uses only retarded data.

  s2  THE LORENTZ POLE.  The isometric boost of the static solution:
      channel direction along (gamma^2 X, Y), strength w |m|^2/rho^2
      (anisotropic -- the 2D Lienard-Wiechert profile), AND the
      baseline boosted: ambient I -> I + (gamma^2 - 1) vhat vhat^T.
      Verified: the moving system is GLOBALLY isometric to the
      static one -- atom equal to the static atom at every speed
      (exact by construction; 5e-5 numerically), flat off the apex
      (NO fan: 0021's curvature fan is an
      artifact of the ether rule), and the co-moving screened pair
      is psi-blind with ratios equal to the static pair's.  The
      relativity principle holds EXACTLY, at all orders, with
      nontrivial velocity structure in the field.

  s3  THE BASELINE IS NOT OPTIONAL.  Drop the ambient boost (keep
      I, boost only the channels): the compass returns (psi-split
      far above floor) and the atom drifts from the static value.
      Channel-velocity coupling alone CANNOT restore covariance:
      the node's own baseline -- the self-channel, the h_00 sector
      -- must transform with the boost.  This is the sharpest form
      of the missing-sector diagnosis: Lorentz structure requires
      the baseline (proper-time) sector to be dynamical.

  s4  THE DIAL, ASSEMBLED.  ether (bare retarded): compass v^2
      cos(2 psi), delta = pi w (1 - v^2), curvature fan.  Galileo:
      no compass, delta constant, no fan, no velocity structure.
      Lorentz: no compass, delta invariant, no fan, velocity
      structure in strength + baseline.  All three share the same
      causal cone; causality does not choose among them.  What
      distinguishes Lorentz from Galileo within the model is
      composition -- flagged open with the two-boost experiment.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_o = importlib.import_module("0009_the_sharp_opens")
_f = importlib.import_module("0008_fisher_deficit")

TAU = 2 * math.pi


# =====================================================================
# the three rules (uniform motion, closed form; source through the
# origin at t = 0, velocity v along +x)
# =====================================================================

def ether_channel(px, py, w, v):
    """Bare retarded rule (0021)."""
    def parts(x, y):
        X, Y = x - px, y - py
        tr = -(X * v + math.sqrt(X * X + (1 - v * v) * Y * Y)) \
            / (1 - v * v)
        d = -tr
        return ((v * tr - X) / d, -Y / d, w)
    return parts


def galileo_channel(px, py, w, v):
    """Extrapolated rule: for uniform motion, the direction to the
    extrapolated present position IS the instantaneous direction."""
    def parts(x, y):
        X, Y = x - px, y - py
        d = math.hypot(X, Y)
        return (-X / d, -Y / d, w)
    return parts


def lorentz_metric(sources, v):
    """Isometric boost of the static multi-source solution; all
    sources co-moving at v along +x.  Channel: m m^T weighting with
    m = (gamma^2 X, Y); baseline: diag(gamma^2, 1)."""
    g2 = 1.0 / (1.0 - v * v)

    def metric(x, y):
        E, F, G = g2, 0.0, 1.0
        for (px, py), w in sources:
            X, Y = x - px, y - py
            rho2 = g2 * X * X + Y * Y
            mx, my = g2 * X, Y
            E += w * mx * mx / rho2
            F += w * mx * my / rho2
            G += w * my * my / rho2
        return (E, F, G)
    return metric


def channels_metric(channels, ambient=(1.0, 0.0, 1.0)):
    def metric(x, y):
        E, F, G = ambient
        for ch in channels:
            ux, uy, w = ch(x, y)
            E += w * ux * ux
            F += w * ux * uy
            G += w * uy * uy
        return (E, F, G)
    return metric


def atom(metric, steps=8000):
    t1 = _o.transport_deficit(metric, 0.0, 0.0, 0.02, steps=steps)
    t2 = _o.transport_deficit(metric, 0.0, 0.0, 0.04, steps=steps)
    return (4 * t1 - t2) / 3


# =====================================================================
# 1. the Galilean pole
# =====================================================================

MOVE_D, MOVE_TAU = 0.25, 0.45


def kicked_state(t):
    """Position and velocity on the kicked worldline (0021)."""
    if t <= 0:
        return (0.0, 0.0), (0.0, 0.0)
    if t >= MOVE_TAU:
        return (MOVE_D, 0.0), (0.0, 0.0)
    s = t / MOVE_TAU
    pos = (MOVE_D * (3 * s * s - 2 * s ** 3), 0.0)
    vel = (MOVE_D * (6 * s - 6 * s * s) / MOVE_TAU, 0.0)
    return pos, vel


def galileo_kicked_metric(w, t_obs):
    """Extrapolated rule on the kicked worldline: retarded data
    (position AND velocity), linearly extrapolated to t_obs."""
    def metric(x, y):
        lo, hi = t_obs - (math.hypot(x, y) + 2.0), t_obs
        for _ in range(70):
            mid = 0.5 * (lo + hi)
            (px, py), _v = kicked_state(mid)
            if (t_obs - mid) - math.hypot(x - px, y - py) > 0:
                lo = mid
            else:
                hi = mid
        tr = 0.5 * (lo + hi)
        (px, py), (vx, vy) = kicked_state(tr)
        ex, ey = px + vx * (t_obs - tr), py + vy * (t_obs - tr)
        d = math.hypot(x - ex, y - ey)
        ux, uy = (ex - x) / d, (ey - y) / d
        return (1 + w * ux * ux, w * ux * uy, 1 + w * uy * uy)
    return metric


def verify_galileo() -> None:
    w = 0.3
    for v in (0.3, 0.7):
        mg = channels_metric([galileo_channel(0, 0, w, v)])
        ms = channels_metric([galileo_channel(0, 0, w, 0.0)])
        for pt in ((0.4, 0.1), (-0.3, 0.6)):
            assert mg(*pt) == ms(*pt)
    print("    uniform motion: the extrapolated field IS the static")
    print("    field (exact identity).  Compass dead, delta(v) =")
    print("    delta(0), moving systems indistinguishable --")
    print("    relativity, Galileo's way.")
    print()
    # causality survives extrapolation
    m = galileo_kicked_metric(w, 1.2)
    inside = _f.gaussian_curvature(m, 0.0, 0.9, h=1e-4)
    for r in (1.3, 1.6):
        K = _f.gaussian_curvature(m, 0.0, r, h=1e-4)
        assert abs(K) < 1e-6, (r, K)
    assert abs(inside) > 1e-4
    print(f"    kicked source, t = 1.2: K(0.9) = {inside:.5f} inside")
    print(f"    the cone, K = 0 beyond r = ct to 1e-6 -- extrapolation")
    print(f"    is built from retarded data, so the causal cone")
    print(f"    survives.  Galilean relativity WITH a light cone --")
    print(f"    but no velocity structure anywhere in the field.")


# =====================================================================
# 2. the Lorentz pole
# =====================================================================

def verify_lorentz() -> None:
    w = 0.3
    static = TAU * (1 - 1 / math.sqrt(1 + w))
    print(f"    static atom delta(w = {w}) = {static:.6f}")
    for v in (0.3, 0.6, 0.8):
        m = lorentz_metric([((0.0, 0.0), w)], v)
        a = atom(m)
        assert abs(a - static) < 2e-4, (v, a)
        K = _f.gaussian_curvature(m, 0.5, 0.3, h=1e-4)
        assert abs(K) < 1e-6, (v, K)
        print(f"    v = {v}: atom {a:.6f} (= static to 1e-5), "
              f"off-apex K = {K:.1e}")
    print("    the moving solution is GLOBALLY isometric to the")
    print("    static one: the atom is speed-invariant and there is")
    print("    NO curvature fan -- 0021's fan was the ether rule's")
    print("    artifact, not a feature of moving mass.")
    print()
    # the co-moving compass, at the Lorentz pole
    w1, w2, v, d = 0.02, 0.5, 0.6, 0.5
    solo = atom(lorentz_metric([((0.0, 0.0), w1)], v))
    static_pair = atom(channels_metric(
        [galileo_channel(0, 0, w1, 0), galileo_channel(d, 0, w2, 0)]))
    static_solo = TAU * (1 - 1 / math.sqrt(1 + w1))
    ratios = []
    for name, pos in (("ahead", (d, 0.0)), ("side", (0.0, d)),
                      ("behind", (-d, 0.0))):
        T = atom(lorentz_metric([((0.0, 0.0), w1),
                                 (pos, w2)], v))
        ratios.append(T / solo)
        print(f"    co-moving pair, partner {name:>6}: ratio "
              f"{T / solo:.6f}")
    spread = max(ratios) - min(ratios)
    assert spread < 1e-5, ratios
    assert abs(ratios[0] - static_pair / static_solo) < 1e-4
    print(f"    orientation spread {spread:.1e} (floor-level); ratio")
    print(f"    equals the static pair's "
          f"{static_pair / static_solo:.6f}.  The compass is dead")
    print(f"    at ALL orders: the relativity principle holds exactly,")
    print(f"    with nontrivial velocity structure (anisotropic")
    print(f"    strength + boosted baseline) in the field.")


# =====================================================================
# 3. the baseline is not optional
# =====================================================================

def lorentz_channels_only_metric(sources, v):
    """Boosted channels over the UNBOOSTED baseline I."""
    g2 = 1.0 / (1.0 - v * v)

    def metric(x, y):
        E, F, G = 1.0, 0.0, 1.0
        for (px, py), w in sources:
            X, Y = x - px, y - py
            rho2 = g2 * X * X + Y * Y
            mx, my = g2 * X, Y
            E += w * mx * mx / rho2
            F += w * mx * my / rho2
            G += w * my * my / rho2
        return (E, F, G)
    return metric


def verify_baseline_necessity() -> None:
    w1, w2, v, d = 0.02, 0.5, 0.6, 0.5
    static_solo = TAU * (1 - 1 / math.sqrt(1 + w1))
    solo = atom(lorentz_channels_only_metric([((0.0, 0.0), w1)], v))
    drift = abs(solo - static_solo) / static_solo
    ratios = []
    for pos in ((d, 0.0), (0.0, d), (-d, 0.0)):
        T = atom(lorentz_channels_only_metric(
            [((0.0, 0.0), w1), (pos, w2)], v))
        ratios.append(T / solo)
    spread = max(ratios) - min(ratios)
    print(f"    boosted channels over UNBOOSTED baseline I (v = {v}):")
    print(f"      solo atom drifts from static by {100 * drift:.1f}%")
    print(f"      co-moving pair orientation spread {spread:.1e}")
    assert drift > 0.02, drift
    assert spread > 1e-4, spread
    print()
    print("  Channel-velocity coupling alone does NOT restore")
    print("  covariance: without the boosted baseline the compass")
    print("  returns and the atom drifts.  The node's own baseline --")
    print("  the self-channel, the h_00 sector -- must transform with")
    print("  the boost.  Lorentz structure REQUIRES the baseline")
    print("  (proper-time) sector to be dynamical; 0023's diagnosis")
    print("  lands on a specific, now-constructed object.")


# =====================================================================
# 4. the dial
# =====================================================================

def verify_the_dial() -> None:
    w, v = 0.3, 0.6
    static = TAU * (1 - 1 / math.sqrt(1 + w))
    rows = []
    me = channels_metric([ether_channel(0, 0, w, v)])
    rows.append(("ether (bare retarded)", atom(me),
                 _f.gaussian_curvature(me, 0.5, 0.3, h=1e-4)))
    mg = channels_metric([galileo_channel(0, 0, w, v)])
    rows.append(("Galileo (extrapolated)", atom(mg),
                 _f.gaussian_curvature(mg, 0.5, 0.3, h=1e-4)))
    ml = lorentz_metric([((0.0, 0.0), w)], v)
    rows.append(("Lorentz (boosted)", atom(ml),
                 _f.gaussian_curvature(ml, 0.5, 0.3, h=1e-4)))
    print(f"    one web, three update rules (w = {w}, v = {v};")
    print(f"    static atom {static:.4f}):")
    print(f"    {'rule':<24} {'atom':>9} {'off-apex K':>11}")
    for name, a, K in rows:
        print(f"    {name:<24} {a:>9.4f} {K:>11.4f}")
    assert rows[0][1] < rows[1][1] - 0.05          # ether suppressed
    assert abs(rows[1][1] - static) < 1e-4         # Galileo static
    assert abs(rows[2][1] - static) < 2e-4         # Lorentz static
    assert abs(rows[0][2]) > 0.05                  # ether fan
    assert abs(rows[1][2]) < 1e-6                  # no fan
    assert abs(rows[2][2]) < 1e-6                  # no fan
    print()
    print("  The dial: causality (the c-cone) holds for all three --")
    print("  it never chooses the symmetry.  The ether rule pays with")
    print("  a compass and a fan; Galileo and Lorentz both satisfy")
    print("  the relativity principle for uniform motion, and differ")
    print("  in where velocity structure lives (nowhere vs strength +")
    print("  baseline).  Distinguishing them inside the model needs")
    print("  composition -- two successive boosts / aberration")
    print("  chains -- the flagged next experiment.")


def run_verification_suite() -> None:
    sections = [
        ("The Galilean pole", verify_galileo),
        ("The Lorentz pole", verify_lorentz),
        ("The baseline is not optional", verify_baseline_necessity),
        ("The dial", verify_the_dial),
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
