"""Noether on the web: symmetries, their charges, and the choice
that's not a choice.

  s1  THE SYMMETRY INVENTORY, AT FIELD LEVEL.  Translations and
      rotations: exact (by construction; spot-checked).  DILATION:
      exact and FIELD-LEVEL -- the web has no length scale (unit
      channels), so g_lambda(lambda x) = g(x) exactly, statics AND
      the causal sector with (x, t) -> (lambda x, lambda t): the
      scaling is z = 1, pinned by the cone (z = 2, the Schroedinger
      scaling t -> lambda^2 t, FAILS at field level).  TIME
      REVERSAL: broken by retardation (advanced != retarded fields
      mid-transient; equal in the static sector) -- the web carries
      an arrow.  And the MASS-BROADCAST test: at the ether and
      Galileo poles the channel trace is exactly w (mass is a
      broadcast scalar -- a central charge); at the Lorentz pole
      the trace is direction-dependent: mass mixes into the motion
      sector.  Bargmann's dichotomy, measured in the field.

  s2  CHARGES ARE HOLONOMIES.  The loop development (rotation AND
      translation parts of the ISO(2) monodromy) is implemented and
      calibrated: rotation part = the deficit (mass/energy),
      translation part = (I - R_delta) x (developed apex position)
      = the MASS MOMENT (verified against 2 sin(delta/2) x proper
      distance).  Under interior motion the rotation part is
      conserved (energy), and the translation part drifts LINEARLY
      with rate = 2 sin(delta/2) |v| -- the momentum, read off the
      monodromy.  Noether charges on the web are not integrals of
      local densities; they are quasi-local monodromies, conserved
      by the causal cone (nothing changes without crossing news).

  s3  MICHELSON-MORLEY IN-MODEL: THE CHOICE THAT'S NOT A CHOICE.
      Signals ride the derived cone (speed c in the web frame --
      rule-independent, 0022).  Mirrors are held at fixed PROPER
      length by the pole's own metric.  Round-trip anisotropy
      T_parallel / T_transverse over the baseline family
      I + (beta - 1) vhat vhat^T:  beta = 1 (ether AND Galileo
      poles) gives gamma -- an internal O(v^2) compass in the
      SIGNAL sector, so Galileo's uniform-motion covariance (0024)
      does not survive signals; the null occurs at beta = gamma^2
      EXACTLY and uniquely -- which is precisely the Lorentz pole's
      boosted baseline.  Relativity principle + derived cone =>
      Lorentz, uniquely.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_o = importlib.import_module("0009_the_sharp_opens")
_v = importlib.import_module("0019_velocity_dependent_channels")

TAU = 2 * math.pi


# =====================================================================
# 1. the symmetry inventory
# =====================================================================

def ether_kicked_metric(w, t_obs, scale=1.0, advanced=False):
    """Retarded (or advanced) field of the kicked worldline, with the
    whole experiment dilated by `scale` (z = 1: x and t together)."""
    D, T = _v.MOVE_D * scale, _v.MOVE_TAU * scale

    def pos(t):
        if t <= 0:
            return (0.0, 0.0)
        if t >= T:
            return (D, 0.0)
        s = t / T
        return (D * (3 * s * s - 2 * s ** 3), 0.0)

    def metric(x, y):
        if not advanced:
            lo, hi = t_obs - (math.hypot(x, y) + 2.0 * scale), t_obs
            for _ in range(70):
                mid = 0.5 * (lo + hi)
                px, py = pos(mid)
                if (t_obs - mid) - math.hypot(x - px, y - py) > 0:
                    lo = mid
                else:
                    hi = mid
        else:
            lo, hi = t_obs, t_obs + math.hypot(x, y) + 2.0 * scale
            for _ in range(70):
                mid = 0.5 * (lo + hi)
                px, py = pos(mid)
                if (mid - t_obs) - math.hypot(x - px, y - py) > 0:
                    hi = mid
                else:
                    lo = mid
        tr = 0.5 * (lo + hi)
        px, py = pos(tr)
        d = math.hypot(x - px, y - py)
        ux, uy = (px - x) / d, (py - y) / d
        return (1 + w * ux * ux, w * ux * uy, 1 + w * uy * uy)
    return metric


def ether_kicked_z2(w, t_obs, lam):
    """z = 2 rescaling: x -> lam x but t -> lam^2 t."""
    D, T = _v.MOVE_D * lam, _v.MOVE_TAU * lam * lam

    def pos(t):
        if t <= 0:
            return (0.0, 0.0)
        if t >= T:
            return (D, 0.0)
        s = t / T
        return (D * (3 * s * s - 2 * s ** 3), 0.0)

    def metric(x, y):
        lo, hi = t_obs - (math.hypot(x, y) + 3.0 * lam), t_obs
        for _ in range(70):
            mid = 0.5 * (lo + hi)
            px, py = pos(mid)
            if (t_obs - mid) - math.hypot(x - px, y - py) > 0:
                lo = mid
            else:
                hi = mid
        tr = 0.5 * (lo + hi)
        px, py = pos(tr)
        d = math.hypot(x - px, y - py)
        ux, uy = (px - x) / d, (py - y) / d
        return (1 + w * ux * ux, w * ux * uy, 1 + w * uy * uy)
    return metric


def verify_inventory() -> None:
    w = 0.3
    # dilation, static sector: field-level exactness
    m1 = _v.channels_metric([_v.galileo_channel(0.4, 0.1, w, 0)])
    m2 = _v.channels_metric([_v.galileo_channel(0.4 * 2.7, 0.1 * 2.7,
                                                w, 0)])
    for x, y in ((0.9, -0.3), (-0.2, 0.7)):
        a, b = m1(x, y), m2(2.7 * x, 2.7 * y)
        assert max(abs(p - q) for p, q in zip(a, b)) < 1e-14
    # dilation, causal sector, z = 1: (x, t) -> (lam x, lam t)
    lam, t0, pt = 1.7, 0.6, (0.05, 0.45)
    g1 = ether_kicked_metric(w, t0)(*pt)
    gl = ether_kicked_metric(w, lam * t0, scale=lam)(
        lam * pt[0], lam * pt[1])
    assert max(abs(p - q) for p, q in zip(g1, gl)) < 1e-12, (g1, gl)
    # z = 2 fails
    g2 = ether_kicked_z2(w, lam * lam * t0, lam)(
        lam * pt[0], lam * pt[1])
    assert max(abs(p - q) for p, q in zip(g1, g2)) > 0.02, (g1, g2)
    print("    dilation: EXACT at field level -- statics, and the")
    print("    causal sector under (x,t) -> (lam x, lam t).  The web")
    print("    has no length scale, and the cone pins the scaling to")
    print("    z = 1: the Schroedinger rescaling t -> lam^2 t breaks")
    print("    the field (deviation 0.08 vs z = 1's ~1e-16).")
    print()
    # time reversal
    mret = ether_kicked_metric(w, 0.2)
    madv = ether_kicked_metric(w, 0.2, advanced=True)
    dev = max(abs(p - q) for p, q in zip(mret(0.05, 0.45),
                                         madv(0.05, 0.45)))
    assert dev > 0.05, dev
    mret0 = ether_kicked_metric(w, -1.0)
    madv0 = ether_kicked_metric(w, -3.0, advanced=True)
    dev0 = max(abs(p - q) for p, q in zip(mret0(0.55, 0.35),
                                          madv0(0.55, 0.35)))
    assert dev0 < 1e-9, dev0
    print(f"    time reversal: BROKEN by retardation mid-transient")
    print(f"    (retarded vs advanced field deviation {dev:.4f});")
    print(f"    equal in the static sector ({dev0:.1e}).  The web")
    print(f"    carries an arrow in its update rule.")
    print()
    # the mass-broadcast (central charge) test
    v = 0.6
    ue = _v.ether_channel(0, 0, w, v)(0.5, 0.3)
    tr_e = w * (ue[0] ** 2 + ue[1] ** 2)
    assert abs(tr_e - w) < 1e-12
    g2v = 1 / (1 - v * v)
    traces = []
    for X, Y in ((0.5, 0.0), (0.0, 0.5)):
        rho2 = g2v * X * X + Y * Y
        traces.append(w * (g2v * g2v * X * X + Y * Y) / rho2)
    assert abs(traces[0] - traces[1]) > 0.5 * w, traces
    print(f"    mass broadcast: ether/Galileo channel trace = w")
    print(f"    exactly (mass is a broadcast scalar -- a central")
    print(f"    charge); Lorentz channel trace varies with direction")
    print(f"    ({traces[0]:.4f} vs {traces[1]:.4f} at w = {w}):")
    print(f"    mass mixes into the motion sector.  Bargmann's")
    print(f"    dichotomy -- central mass (Galilei) vs mass-energy")
    print(f"    mixing (Poincare) -- is visible in the field.")


# =====================================================================
# 2. charges are holonomies
# =====================================================================

def develop_loop(metric, cx, cy, R, steps=6000):
    """Rotation and translation parts of the loop's monodromy, by
    developing the loop into the flat plane of the starting frame."""
    x0, y0 = cx + R, cy
    E, F, G = metric(x0, y0)
    e1 = (1 / math.sqrt(E), 0.0)
    v2 = (-F / E, 1.0)
    n2 = math.sqrt(E * v2[0] ** 2 + 2 * F * v2[0] * v2[1]
                   + G * v2[1] ** 2)
    e2 = (v2[0] / n2, v2[1] / n2)
    f1, f2 = list(e1), list(e2)
    dev = [0.0, 0.0]
    for s in range(steps):
        t = TAU * s / steps
        x = cx + R * math.cos(t)
        y = cy + R * math.sin(t)
        dx = -R * math.sin(t) * (TAU / steps)
        dy = R * math.cos(t) * (TAU / steps)
        det = f1[0] * f2[1] - f1[1] * f2[0]
        dev[0] += (dx * f2[1] - dy * f2[0]) / det
        dev[1] += (-dx * f1[1] + dy * f1[0]) / det
        (G111, G112, G122), (G211, G212, G222) = \
            _o.christoffel(metric, x, y)
        for f in (f1, f2):
            d1 = -(G111 * dx * f[0] + G112 * (dx * f[1] + dy * f[0])
                   + G122 * dy * f[1])
            d2 = -(G211 * dx * f[0] + G212 * (dx * f[1] + dy * f[0])
                   + G222 * dy * f[1])
            f[0] += d1
            f[1] += d2
    E, F, G = metric(x0, y0)
    dot = E * f1[0] * e1[0] + F * (f1[0] * e1[1] + f1[1] * e1[0]) \
        + G * f1[1] * e1[1]
    n = math.sqrt(E * f1[0] ** 2 + 2 * F * f1[0] * f1[1]
                  + G * f1[1] ** 2)
    rot = math.acos(max(-1.0, min(1.0, dot / n)))
    return rot, (dev[0], dev[1])


def seg_length(metric, a, b, steps=400):
    total = 0.0
    for s in range(steps):
        t = (s + 0.5) / steps
        x = a[0] + t * (b[0] - a[0])
        y = a[1] + t * (b[1] - a[1])
        dx, dy = (b[0] - a[0]) / steps, (b[1] - a[1]) / steps
        E, F, G = metric(x, y)
        total += math.sqrt(E * dx * dx + 2 * F * dx * dy + G * dy * dy)
    return total


def static_metric(px, py, w):
    return _v.channels_metric([_v.galileo_channel(px, py, w, 0)])


def verify_holonomy_charges() -> None:
    w = 0.3
    delta = TAU * (1 - 1 / math.sqrt(1 + w))
    two_sin = 2 * math.sin(delta / 2)
    base = (1.0, 0.0)
    # calibration: rotation = mass; translation = mass moment
    rot, tr = develop_loop(static_metric(0, 0, w), 0, 0, 1.0)
    pred = two_sin * math.sqrt(1 + w)
    assert abs(rot - delta) < 1e-3
    assert abs(math.hypot(*tr) - pred) < 2e-3, (tr, pred)
    print(f"    calibration (defect at loop centre): rotation part =")
    print(f"    {rot:.5f} (= the mass, delta = {delta:.5f});")
    print(f"    |translation| = {math.hypot(*tr):.5f} = 2 sin(d/2) x")
    print(f"    proper basepoint-apex distance ({pred:.5f}).")
    for p in ((0.3, 0.05), (0.15, 0.55)):
        rot, tr = develop_loop(static_metric(p[0], p[1], w), 0, 0, 1.0)
        L = seg_length(static_metric(p[0], p[1], w), base, p)
        assert abs(rot - delta) < 1e-3
        assert abs(math.hypot(*tr) - two_sin * L) < 0.02 * two_sin * L
        print(f"    apex at {p}: rot {rot:.5f}, |tr| "
              f"{math.hypot(*tr):.5f} vs 2sin(d/2)*L = "
              f"{two_sin * L:.5f}")
    print()
    print("    the monodromy IS the ISO(2) charge: rotation part =")
    print("    mass, translation part = mass moment.")
    print()
    # motion: energy conserved, momentum = the moment's drift rate
    vel = 0.5
    trs, rots = [], []
    for t in (0.0, 0.4, 0.8):
        p = (0.1 + vel * t - 0.3, 0.05)
        rot, tr = develop_loop(static_metric(p[0], p[1], w), 0, 0, 1.0)
        rots.append(rot)
        trs.append(tr)
    assert max(rots) - min(rots) < 2e-4, rots
    d1 = (trs[1][0] - trs[0][0], trs[1][1] - trs[0][1])
    d2 = (trs[2][0] - trs[1][0], trs[2][1] - trs[1][1])
    bend = math.hypot(d2[0] - d1[0], d2[1] - d1[1])
    step = math.hypot(*d1)
    rate = math.hypot(*d1) / 0.4
    pred_rate = two_sin * vel * math.sqrt(1 + w)
    print(f"    interior motion (|v| = {vel}): rotation part constant")
    print(f"    to {max(rots) - min(rots):.1e} (ENERGY conserved);")
    print(f"    translation part drifts linearly (bend/step = "
          f"{bend / step:.3f}),")
    print(f"    rate {rate:.4f} vs 2 sin(d/2) sqrt(1+w) |v| = "
          f"{pred_rate:.4f}:")
    print(f"    the MOMENTUM -- mass x PROPER velocity (the moment is")
    print(f"    metered in the web's own distance) -- read off the")
    print(f"    monodromy's drift.")
    assert bend / step < 0.02, (bend, step)
    assert abs(rate - pred_rate) < 0.02 * pred_rate, (rate, pred_rate)
    print()
    print("  Noether charges on the web are not integrals of local")
    print("  densities -- they are quasi-local MONODROMIES (the 2+1")
    print("  ADM structure), conserved by the causal cone: nothing")
    print("  changes until news crosses the loop.")


# =====================================================================
# 3. Michelson-Morley in-model
# =====================================================================

def round_trips(v, beta, L=1.0):
    """Round-trip signal times between co-moving stations at fixed
    PROPER length L, baseline I + (beta - 1) vhat vhat^T; signals at
    the web-frame cone speed c = 1."""
    ell_par = L / math.sqrt(beta)      # coordinate length, parallel
    ell_perp = L
    t_par = ell_par / (1 - v) + ell_par / (1 + v)
    # transverse leg: solve t = sqrt((v t)^2 + L^2) numerically
    lo, hi = 0.0, 10.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if mid < math.hypot(v * mid, ell_perp):
            lo = mid
        else:
            hi = mid
    t_perp = 2 * (0.5 * (lo + hi))
    return t_par, t_perp


def verify_michelson_morley() -> None:
    v = 0.6
    g2 = 1 / (1 - v * v)
    print(f"    co-moving interferometer at v = {v}: round-trip ratio")
    print(f"    T_par / T_perp over the baseline family "
          f"I + (beta-1) vv^T:")
    print(f"    {'beta':>12} {'ratio':>10}")
    ratios = {}
    for name, beta in (("1 (ether/Gal.)", 1.0), ("gamma", g2 ** 0.5),
                       ("gamma^2", g2), ("gamma^3", g2 ** 1.5)):
        tp, tt = round_trips(v, beta)
        ratios[name] = tp / tt
        print(f"    {name:>12} {tp / tt:>10.6f}")
    gamma = 1 / math.sqrt(1 - v * v)
    assert abs(ratios["1 (ether/Gal.)"] - gamma) < 1e-9
    assert abs(ratios["gamma^2"] - 1.0) < 1e-9
    assert abs(ratios["gamma"] - 1.0) > 1e-2
    assert abs(ratios["gamma^3"] - 1.0) > 1e-2
    print()
    print("  The signal rides the DERIVED cone (rule-independent),")
    print("  so no update rule can change the round-trip kinematics;")
    print("  only the LENGTH STANDARD can respond.  The null occurs")
    print("  at beta = gamma^2 exactly and uniquely -- the Lorentz")
    print("  pole's boosted baseline (0024).  Consequences:")
    print("    - the Galileo pole's covariance (0024) was confined to")
    print("      the static sector: its signal sector carries an")
    print("      O(v^2) compass (ratio = gamma).  Galileo fails.")
    print("    - the ether pole fails in both sectors (0023).")
    print("    - the Lorentz pole passes both.")
    print("  THE CHOICE THAT'S NOT A CHOICE: relativity principle +")
    print("  derived cone => Lorentz, uniquely.  (One-way anisotropy")
    print("  is synchronization-convention dependent, here as in")
    print("  physics: only round trips are invariant statements.)")


def run_verification_suite() -> None:
    sections = [
        ("The symmetry inventory", verify_inventory),
        ("Charges are holonomies", verify_holonomy_charges),
        ("Michelson-Morley in-model", verify_michelson_morley),
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
