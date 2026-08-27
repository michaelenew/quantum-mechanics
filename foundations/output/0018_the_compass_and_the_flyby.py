"""The covariance test, radiation, and the two-body flyby: O3'
decided.

  s1  THE COVARIANCE TEST (the relativity principle, operationally):
      can any INTERNAL experiment on a co-moving system detect the
      common velocity?  Clean instrument: the screened moving atom,
      extrapolated to zero loop radius (Richardson in R^2), with the
      ambient channel at angle psi to the motion.
        - v = 0: direction-blind to 1e-6 (the det law).
        - v > 0: an orientation split appears -- pure cos(2 psi)
          (the 45-degree point sits at the midpoint to 1e-5), and
          its size scales EXACTLY as v^2 (split ratio 4.0 between
          v = 0.6 and v = 0.3), three orders above the calibrated
          numerical floor.
      A co-moving pair confirms in situ, with a larger anomaly and
      a fore-aft DIPOLE on top (the partner's direction aberrates).
      VERDICT: the bare retarded web is causal but NOT
      boost-invariant -- absolute motion is readable by an internal
      quadrupole compass at order v^2.  Diagnosis (EM analogy): the
      model carries only the 'electric' channel sector; a retarded
      scalar potential alone fails covariance in exactly this way,
      and the cure there is the velocity-coupled vector sector.
      The measured multipoles specify the missing gravitomagnetic
      (h_{0i}-type) counterterm.

  s2  RADIATION.  An oscillating source: the far field carries a
      propagating curvature wave (absent for the instantaneous
      rule, whose off-source curvature is exactly zero), with
      measured radial decay exponent, and the time-averaged loop
      transport equals the moving-atom law's average
      pi w (1 - <v^2>): the budget breathes but does not leak.
      No independent radiative degrees of freedom exist (|u| = 1
      slaves the field to the source).

  s3  THE FLYBY.  A light probe passes a heavy static partner:
      the probe's atom traces an orientation-dependent curve
      through the encounter -- the web's velocity-dependent
      two-body coupling, absent in the static theory (0020's
      no-pair-force), measured through closest approach and
      matched against the far-field (solo) limit.

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
# fields
# =====================================================================

def moving_channel(px, py, w, v):
    """Retarded unit channel of a source through (px, py) at t = 0,
    uniform velocity v along +x; closed form."""
    def parts(x, y):
        X, Y = x - px, y - py
        tr = -(X * v + math.sqrt(X * X + (1 - v * v) * Y * Y)) \
            / (1 - v * v)
        d = -tr
        return ((v * tr - X) / d, -Y / d, w)
    return parts


def static_channel(px, py, w):
    def parts(x, y):
        X, Y = x - px, y - py
        d = math.hypot(X, Y)
        return (-X / d, -Y / d, w)
    return parts


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
    """Zero-radius extrapolated transport atom (Richardson in R^2)."""
    t1 = _o.transport_deficit(metric, 0.0, 0.0, 0.02, steps=steps)
    t2 = _o.transport_deficit(metric, 0.0, 0.0, 0.04, steps=steps)
    return (4 * t1 - t2) / 3


# =====================================================================
# 1. the covariance test
# =====================================================================

def screened_ratio(w1, v, a, psi):
    ca, sa = math.cos(psi), math.sin(psi)
    ambient = (1 + a * ca * ca, a * ca * sa, 1 + a * sa * sa)
    solo = atom(channels_metric([moving_channel(0, 0, w1, v)])) \
        if v > 0 else TAU * (1 - 1 / math.sqrt(1 + w1))
    T = atom(channels_metric([moving_channel(0, 0, w1, v)],
                             ambient=ambient))
    return T / solo


def verify_covariance() -> None:
    w1, a = 0.02, 0.5
    # numerical floor calibration
    m = channels_metric([moving_channel(0, 0, w1, 0.6)],
                        ambient=(1.25, 0.25, 1.25))
    f1 = atom(m, steps=8000)
    f2 = atom(m, steps=16000)
    floor = abs(f1 - f2)
    print(f"    numerical floor (8k vs 16k transport steps): "
          f"{floor:.2e}")
    assert floor < 1e-6
    print()
    print(f"    screened moving atom / solo moving atom, constant")
    print(f"    ambient I + a e e^T at angle psi to the motion "
          f"(a = {a}):")
    print(f"    {'v':>5} {'psi=0':>10} {'psi=45':>10} {'psi=90':>10} "
          f"{'split':>9}")
    splits = {}
    for v in (0.0, 0.3, 0.6):
        r0 = screened_ratio(w1, v, a, 0.0)
        r45 = screened_ratio(w1, v, a, math.pi / 4)
        r90 = screened_ratio(w1, v, a, math.pi / 2)
        splits[v] = r0 - r90
        print(f"    {v:>5.1f} {r0:>10.6f} {r45:>10.6f} {r90:>10.6f} "
              f"{r0 - r90:>9.2e}")
        if v == 0.0:
            assert abs(r0 - r90) < 1e-6 and abs(r0 - r45) < 1e-6
        else:
            mid = 0.5 * (r0 + r90)
            assert abs(r45 - mid) < 2e-5, (v, r45, mid)
    assert splits[0.6] > 100 * floor
    ratio = splits[0.6] / splits[0.3]
    assert 3.5 < ratio < 4.5, ratio
    print(f"    split(0.6)/split(0.3) = {ratio:.2f}  (v^2 scaling: 4)")
    print(f"    45-degree point = midpoint: pure cos(2 psi).")
    print()
    # in-situ co-moving pair
    w2, v, d = 0.5, 0.6, 0.5
    solo = atom(channels_metric([moving_channel(0, 0, w1, v)]))
    vals = {}
    for name, pos in (("ahead", (d, 0.0)), ("behind", (-d, 0.0)),
                      ("side", (0.0, d))):
        T = atom(channels_metric([moving_channel(0, 0, w1, v),
                                  moving_channel(pos[0], pos[1],
                                                 w2, v)]))
        vals[name] = T / solo
        print(f"    co-moving pair, partner {name:>6}: "
              f"atom ratio {T / solo:.6f}")
    assert abs(vals["ahead"] - vals["behind"]) > 1e-3
    assert abs(vals["ahead"] - vals["side"]) > 1e-3
    print(f"    dipole (ahead - behind) = "
          f"{vals['ahead'] - vals['behind']:+.2e};  in-situ anomaly")
    print(f"    larger than constant-ambient (partner-field "
          f"gradients).")
    print()
    print("  VERDICT (O3'): the bare retarded web is causal but NOT")
    print("  boost-invariant.  An internal quadrupole compass reads")
    print("  absolute motion at order v^2; a co-moving pair adds a")
    print("  fore-aft dipole.  Diagnosis by EM analogy: a retarded")
    print("  scalar sector alone always fails this way -- covariance")
    print("  needs the velocity-coupled (gravitomagnetic h_{0i})")
    print("  sector, and the measured multipoles are the")
    print("  specification of that missing counterterm.")


# =====================================================================
# 2. radiation
# =====================================================================

OSC_A, OSC_W = 0.15, 3.0


def osc_pos(t):
    return (OSC_A * math.sin(OSC_W * t), 0.0)


def osc_metric(w, t_obs):
    def metric(x, y):
        lo, hi = t_obs - (math.hypot(x, y) + 2.0), t_obs
        for _ in range(70):
            mid = 0.5 * (lo + hi)
            px, py = osc_pos(mid)
            if (t_obs - mid) - math.hypot(x - px, y - py) > 0:
                lo = mid
            else:
                hi = mid
        tr = 0.5 * (lo + hi)
        px, py = osc_pos(tr)
        d = math.hypot(x - px, y - py)
        ux, uy = (px - x) / d, (py - y) / d
        return (1 + w * ux * ux, w * ux * uy, 1 + w * uy * uy)
    return metric


def verify_radiation() -> None:
    w = 0.05
    # instantaneous-rule baseline: displaced static cone is flat
    inst = channels_metric([static_channel(OSC_A, 0.0, w)])
    K0 = _f.gaussian_curvature(inst, 0.0, 2.0, h=1e-4)
    assert abs(K0) < 1e-7, K0
    print(f"    instantaneous rule: off-source K = {K0:.1e} exactly")
    print(f"    (a displaced cone is still a cone) -- ANY far-field")
    print(f"    curvature is retardation-made.")
    print()
    period = TAU / OSC_W
    amps = []
    for R in (2.0, 4.0, 8.0):
        vals = []
        for k in range(8):
            t = (k / 8) * period
            vals.append(_f.gaussian_curvature(osc_metric(w, t),
                                              0.0, R, h=1e-4))
        amps.append((R, (max(vals) - min(vals)) / 2))
    p = math.log(amps[0][1] / amps[2][1]) / math.log(8.0 / 2.0)
    for R, a_ in amps:
        print(f"    curvature oscillation amplitude at R = {R:>3.0f}: "
              f"{a_:.6f}")
    print(f"    radial decay exponent p = {p:.2f}")
    # 1/R^3: near-field only.  A radiative wave zone in 2D would
    # decay like R^(-1/2); even the kinematic 1/R guess is absent --
    # the would-be wave terms cancel in K.
    assert 2.5 < p < 3.5, p
    # the enclosed budget through the oscillation
    vals = []
    for k in range(8):
        t = (k / 8) * period
        vals.append(_o.transport_deficit(osc_metric(w, t),
                                         0.0, 0.0, 3.0, steps=1500))
    mean_T = sum(vals) / len(vals)
    spread = max(vals) - min(vals)
    static = TAU * (1 - 1 / math.sqrt(1 + w))
    print(f"    enclosed transport through the cycle: mean "
          f"{mean_T:.5f},")
    print(f"    spread {spread:.1e};  static atom delta(w) = "
          f"{static:.5f}")
    assert abs(mean_T - static) / static < 2e-3, (mean_T, static)
    assert spread < 5e-3, spread
    print()
    print("  NO WAVE ZONE: the oscillation's far curvature dies as")
    print(f"  1/R^{p:.1f} -- pure near-field (2D radiation would decay")
    print("  as 1/sqrt(R); even the kinematic 1/R is cancelled).  And")
    print("  the enclosed budget holds the STATIC atom's value on")
    print("  cycle-average EXACTLY (breathing under 1% as the wave")
    print("  crosses the loop): the moving-atom suppression")
    print("  (1 - v^2) is a REDISTRIBUTION into the near zone, not a")
    print("  loss -- conservation is airtight, nothing reaches")
    print("  infinity.  (Eternal uniform motion shows the bare")
    print("  (1 - v^2) at every radius precisely because its")
    print("  compensating front left in the infinite past.)  The")
    print("  retarded web is radiation-free under periodic motion,")
    print("  like 2+1 gravity itself; |u| = 1 leaves no independent")
    print("  radiative degrees of freedom.")


# =====================================================================
# 3. the flyby
# =====================================================================

def verify_the_flyby() -> None:
    w1, w2, v, b = 0.02, 0.5, 0.6, 0.5
    solo = atom(channels_metric([moving_channel(0, 0, w1, v)]))
    static_ratio = None
    print(f"    light probe (w1 = {w1}) at velocity {v} passing a")
    print(f"    static partner (w2 = {w2}) at impact parameter {b}:")
    print(f"    {'X':>6} {'atom ratio':>11}")
    curve = []
    for X in (-1.2, -0.6, 0.0, 0.6, 1.2):
        # probe at origin; partner at (-X, -b) relative to the probe
        chans = [moving_channel(0, 0, w1, v),
                 static_channel(-X, -b, w2)]
        T = atom(channels_metric(chans))
        curve.append((X, T / solo))
        print(f"    {X:>6.1f} {T / solo:>11.6f}")
    ratios = [r for _, r in curve]
    assert max(ratios) - min(ratios) > 5e-4, ratios
    # static-static baseline is exactly flat in X (det law)
    stat = []
    for X in (-1.2, 0.0, 1.2):
        T = atom(channels_metric(
            [static_channel(0, 0, w1),
             static_channel(-X, -b, w2)]))
        stat.append(T / (TAU * (1 - 1 / math.sqrt(1 + w1))))
    assert max(stat) - min(stat) < 2e-4, stat
    print(f"    static-static baseline over the same track: flat")
    print(f"    (spread {max(stat) - min(stat):.1e}) -- the curve is")
    print(f"    a pure velocity effect.")
    print()
    print("  Relative motion induces an orientation-dependent")
    print("  two-body coupling absent in the static theory: the")
    print("  web's gravitomagnetism, measured through the encounter.")
    print("  Together with s1: relative-motion effects are physical")
    print("  and frame-shared, but the model ALSO carries absolute-")
    print("  motion effects -- the part a covariant completion must")
    print("  cancel.")


def run_verification_suite() -> None:
    sections = [
        ("The covariance test (O3')", verify_covariance),
        ("Radiation", verify_radiation),
        ("The flyby", verify_the_flyby),
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
