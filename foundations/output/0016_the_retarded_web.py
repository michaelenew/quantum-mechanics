"""The retarded web: where the light cone enters the geometry (O3).

Replace the quasi-static channel field (directions point at sources'
CURRENT positions) with the c-bounded rule: directions point at the
RETARDED position, t_obs - t_ret = |x - y(t_ret)| / c  (c = 1).

  s1  THE MOVING ATOM: delta = pi w (1 - v^2), EXACT.  For uniform
      motion the retarded time is homogeneous of degree 1, so the
      channel field is scale-free and the atom's linear weight is
      computed by the 0020 flux integral (R-independent to 1e-13).
      Measured at five speeds: the ratio is (1 - v^2) to 1e-4 --
      a discovered exact law.  Honest transport at weak w confirms.
      READING (stated, not proven): the Euclidean web suppresses a
      moving source's gravity by (1 - v^2); under the analytic
      continuation v -> iv this is (1 + v^2) -- a Lorentzian moving
      mass gravitates MORE.  The sign of the v^2 term is exactly
      where the signature lives, and the measured law puts the
      minus sign in the UPDATE RULE, not in the state space.

  s2  THE FAN, AND A CORRECTION TO 0014.  The moving source wears a
      scale-free curvature fan K = f(theta)/r^2 (verified: K r^2
      depends on angle only), negative ahead, positive behind, with
      VANISHING angular average (that is why transport is
      R-independent).  This exposes a subtlety: a generic conical
      metric does NOT develop into the flat plane (development
      requires B = E'/2), so 0014's cone formula
      2pi - INT sqrt(EC - B^2)/E is exact only for developable
      apexes.  For the aberrated atom it disagrees with honest
      transport (0.528 vs 0.475 at w = 0.3, v = 0.6) -- and 0014's
      own 0.04% formula-vs-transport gaps are hereby explained as
      real (the beacon apex is slightly non-developable), not
      numerical noise.  Transport and the flux integral are ground
      truth throughout.

  s3  THE LIGHT CONE, MEASURED.  A source at rest forever moves
      quickly (v ~ 0.83 < c) to a new spot inside a fixed loop and
      rests.  The loop's transport: unchanged BEFORE the news
      arrives (t = 0.5: |dT| < 1e-3 even though the move finished
      at t = 0.45), a curvature blip while the news shell crosses
      the loop radius, exact return after.  Scanning K along a ray:
      K = 0 beyond r = c t to 1e-6 -- a sharp domain of dependence
      -- and the front's edge tracks r = c t at two times (fitted
      speed ~ 1).  Geometry's response is c-bounded: the causal
      cone is IN the update dynamics while the state metric stays
      Riemannian -- the two-tier split, computed.

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
# retarded fields
# =====================================================================

def uniform_h(w, v):
    """Channel field h = w u u^T of a source moving uniformly through
    the origin at t_obs = 0, retarded directions, closed form."""
    def parts(x, y):
        tr = -(x * v + math.sqrt(x * x + (1 - v * v) * y * y)) \
            / (1 - v * v)
        d = -tr
        ux, uy = (v * tr - x) / d, -y / d
        return w * ux * ux, w * ux * uy, w * uy * uy
    return parts


def metric_of(parts):
    def metric(x, y):
        h11, h12, h22 = parts(x, y)
        return (1 + h11, h12, 1 + h22)
    return metric


def flux(parts, R, steps=6000, fd=1e-6):
    """The 0020 divergence-identity flux: the linearized atom."""
    total = 0.0
    for i in range(steps):
        t = TAU * (i + 0.5) / steps
        x, y = R * math.cos(t), R * math.sin(t)
        d2h12 = (parts(x, y + fd)[1] - parts(x, y - fd)[1]) / (2 * fd)
        d1h22 = (parts(x + fd, y)[2] - parts(x - fd, y)[2]) / (2 * fd)
        d2h11 = (parts(x, y + fd)[0] - parts(x, y - fd)[0]) / (2 * fd)
        v1 = d2h12 - 0.5 * d1h22
        v2 = -0.5 * d2h11
        total += (v1 * math.cos(t) + v2 * math.sin(t)) * R \
            * (TAU / steps)
    return total


MOVE_D, MOVE_TAU = 0.25, 0.45


def kicked_pos(t):
    """Rest at origin forever; smooth move to (MOVE_D, 0) during
    (0, MOVE_TAU) at peak speed 1.5 * D/tau ~ 0.83 < c; rest."""
    if t <= 0:
        return (0.0, 0.0)
    if t >= MOVE_TAU:
        return (MOVE_D, 0.0)
    s = t / MOVE_TAU
    return (MOVE_D * (3 * s * s - 2 * s ** 3), 0.0)


def kicked_metric(w, t_obs):
    def metric(x, y):
        lo, hi = t_obs - (math.hypot(x, y) + 2.0), t_obs
        for _ in range(70):
            mid = 0.5 * (lo + hi)
            px, py = kicked_pos(mid)
            if (t_obs - mid) - math.hypot(x - px, y - py) > 0:
                lo = mid
            else:
                hi = mid
        tr = 0.5 * (lo + hi)
        px, py = kicked_pos(tr)
        d = math.hypot(x - px, y - py)
        ux, uy = (px - x) / d, (py - y) / d
        return (1 + w * ux * ux, w * ux * uy, 1 + w * uy * uy)
    return metric


# =====================================================================
# 1. the moving atom
# =====================================================================

def verify_the_moving_atom() -> None:
    w = 1e-3
    print(f"    the linearized atom of a uniformly moving source")
    print(f"    (flux integral, R-independent):")
    print(f"    {'v':>5} {'delta/(pi w)':>13} {'1 - v^2':>9}")
    for v in (0.0, 0.2, 0.4, 0.6, 0.8):
        f1 = flux(uniform_h(w, v), 0.3)
        f2 = flux(uniform_h(w, v), 1.7)
        assert abs(f1 - f2) < 1e-10, (v, f1, f2)
        ratio = f1 / (math.pi * w)
        assert abs(ratio - (1 - v * v)) < 1e-4, (v, ratio)
        print(f"    {v:>5.1f} {ratio:>13.6f} {1 - v * v:>9.4f}")
    T = _o.transport_deficit(metric_of(uniform_h(w, 0.6)),
                             0.0, 0.0, 0.4, steps=4000)
    assert abs(T / (math.pi * w) - 0.64) < 5e-3, T
    print(f"    honest transport at v = 0.6: T/(pi w) = "
          f"{T / (math.pi * w):.4f}")
    print()
    print("  DISCOVERED EXACT LAW:  delta = pi w (1 - v^2).  In the")
    print("  Euclidean web, motion SUPPRESSES a source's gravity by")
    print("  (1 - v^2); under v -> i v the law continues to (1 + v^2)")
    print("  -- the Lorentzian moving mass gravitates more.  The v^2")
    print("  SIGN is where the signature lives, and it lives in the")
    print("  retarded update rule -- the state metric never changed.")


# =====================================================================
# 2. the fan and the corrected cone formula
# =====================================================================

def verify_the_fan() -> None:
    w, v = 0.3, 0.6
    parts = uniform_h(w, v)
    metric = metric_of(parts)
    # scale-freeness of the field
    for x, y in ((0.3, 0.2), (-0.4, 0.5)):
        a = parts(x, y)
        b = parts(3.7 * x, 3.7 * y)
        assert max(abs(p - q) for p, q in zip(a, b)) < 1e-12
    print("    the uniform-motion field is exactly scale-free")
    print("    (retarded time is homogeneous of degree 1), so its")
    print("    wake curvature is a FAN: K = f(theta)/r^2.")
    print()
    print(f"    {'direction':>12} {'K r^2 at r=0.4':>15} "
          f"{'K r^2 at r=0.8':>15}")
    for name, (cx, cy) in (("ahead", (1, 0)), ("behind", (-1, 0)),
                           ("side", (0, 1))):
        vals = []
        for r in (0.4, 0.8):
            K = _f.gaussian_curvature(metric, r * cx, r * cy, h=1e-4)
            vals.append(K * r * r)
        assert abs(vals[0] - vals[1]) < 0.02 * max(1e-9, abs(vals[0]))\
            + 5e-3, (name, vals)
        print(f"    {name:>12} {vals[0]:>15.4f} {vals[1]:>15.4f}")
    T1 = _o.transport_deficit(metric, 0.0, 0.0, 0.05, steps=4000)
    T2 = _o.transport_deficit(metric, 0.0, 0.0, 2.0, steps=4000)
    assert abs(T1 - T2) < 5e-4, (T1, T2)
    print(f"    angular average vanishes: T(R = 0.05) = {T1:.5f},")
    print(f"    T(R = 2.0) = {T2:.5f} -- negative ahead/side lobes")
    print(f"    exactly balance the positive wake astern.")
    print()
    # the correction to 0014's cone formula
    total = 0.0
    steps = 100000
    for i in range(steps):
        th = TAU * (i + 0.5) / steps
        c, s = math.cos(th), math.sin(th)
        E11, E12, E22 = metric(c, s)
        E = E11 * c * c + 2 * E12 * c * s + E22 * s * s
        B = (E22 - E11) * c * s + E12 * (c * c - s * s)
        C = E11 * s * s - 2 * E12 * c * s + E22 * c * c
        total += math.sqrt(max(E * C - B * B, 0.0)) / E * (TAU / steps)
    formula = TAU - total
    print(f"    0014's cone formula gives {formula:.4f}; honest")
    print(f"    transport gives {T1:.4f}.  The formula assumes the")
    print(f"    apex develops into the flat plane, which requires")
    print(f"    B = E'/2 -- true for the static radial cone, FALSE")
    print(f"    for the aberrated one (and slightly violated at 0014's")
    print(f"    beacon apexes: its 0.04% formula-vs-transport gaps")
    print(f"    were real, not numerical).  Transport and the flux")
    print(f"    integral are ground truth throughout this thread.")
    assert formula > T1 + 0.02


# =====================================================================
# 3. the light cone
# =====================================================================

def front_edge(w, t_obs, lo=0.5, hi=None):
    """Outermost radius (along +y) where |K| exceeds 1e-5."""
    metric = kicked_metric(w, t_obs)
    hi = hi if hi is not None else t_obs + 0.4
    for _ in range(22):
        mid = 0.5 * (lo + hi)
        K = _f.gaussian_curvature(metric, 0.0, mid, h=1e-4)
        if abs(K) > 1e-5:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def verify_the_light_cone() -> None:
    w = 0.3
    static = 2 * math.pi * (1 - 1 / math.sqrt(1 + w))
    print(f"    source rests at origin forever, moves to (0.25, 0)")
    print(f"    during t in (0, 0.45) at peak speed 0.83c, rests.")
    print(f"    transport around the fixed loop R = 0.8:")
    print(f"    {'t':>6} {'T':>9} {'T - static':>11}")
    curve = {}
    for t in (-0.2, 0.5, 0.9, 1.4, 2.5):
        T = _o.transport_deficit(kicked_metric(w, t), 0.0, 0.0, 0.8,
                                 steps=2000)
        curve[t] = T
        print(f"    {t:>6.1f} {T:>9.5f} {T - static:>+11.5f}")
    assert abs(curve[0.5] - curve[-0.2]) < 1e-3
    assert curve[0.9] - static > 0.02
    assert abs(curve[2.5] - static) < 1e-3
    print(f"    at t = 0.5 the move is DONE (finished t = 0.45) but")
    print(f"    the loop has not heard: T unchanged to <1e-3.  The")
    print(f"    news shell crosses at t ~ 0.8-1.2 (the blip), then T")
    print(f"    returns exactly: conservation through the transient.")
    print()
    m12 = kicked_metric(w, 1.2)
    for r in (1.1, 1.2, 1.3, 1.5):
        K = _f.gaussian_curvature(m12, 0.0, r, h=1e-4)
        if r > 1.2:
            assert abs(K) < 1e-6, (r, K)
    e1 = front_edge(w, 1.2)
    e2 = front_edge(w, 1.8)
    speed = (e2 - e1) / 0.6
    print(f"    the front, scanned along +y:  K = 0 beyond r = ct to")
    print(f"    1e-6.  edge(t = 1.2) = {e1:.3f}, edge(t = 1.8) = "
          f"{e2:.3f}:")
    print(f"    front speed = {speed:.3f} c.")
    assert abs(e1 - 1.2) < 0.12 and abs(e2 - 1.8) < 0.12
    assert 0.85 < speed < 1.15, speed
    print()
    print("  THE CAUSAL CONE IS IN THE GEOMETRY'S RESPONSE: a sharp")
    print("  domain of dependence expanding at c, unreachable early")
    print("  updates impossible, budget restored after passage.  The")
    print("  state-space metric stayed Riemannian; the minus sign")
    print("  entered through the c-bounded update rule -- P2's")
    print("  two-tier split (actionable is c-bounded), computed in")
    print("  curvature.")


def run_verification_suite() -> None:
    sections = [
        ("The moving atom: delta = pi w (1 - v^2)",
         verify_the_moving_atom),
        ("The fan, and the corrected cone formula", verify_the_fan),
        ("The light cone", verify_the_light_cone),
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
