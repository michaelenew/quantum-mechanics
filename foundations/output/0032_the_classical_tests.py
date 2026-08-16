"""The classical tests: light bending, precession, and two bodies.

0036 selected the vacuum profile w = 2M/rho from the web's own
field law and got Newton and Kepler.  This module runs the
classical GR discriminators through the same metric, plus the first
two-body measurements -- where the web's nonlinearity lives.

  s1  LIGHT BENDING.  Null geodesics past the mass: deflection
      4M/b to 0.6% (b = 1) and 0.3% (b = 2) -- EINSTEIN'S FULL
      VALUE, cleanly twice the Newtonian 2M/b.  The factor 2 that
      made 1919 is in the web's selected metric.

  s2  PERIHELION PRECESSION.  Timelike orbits: prograde advance,
      exactly repeatable across successive orbits (+0.21527 thrice
      at M = 0.005), and CONVERGING TO GR's 6 pi M / (a(1-e^2)):
      the excess is linear in M/p with coefficient ~4.8 -- the
      second-order term -- so the ratio walks to 1 as M -> 0
      (1.053 at M/p = 0.011, 1.021 at M/p = 0.0044).

  s3  TWO BODIES.  Superposing two vacuum-profile channels:
      - the off-source Ricci violation scales EXACTLY as M1 M2
        (ratio to M^2: 48.7 / 48.3 / 48.2 over a 4x mass range) --
        the web's nonlinearity, localized and measured;
      - far-field attraction = -(M1+M2)/r^2 (0.4% at r = 10):
        masses add;
      - CHANNEL NULLITY: a single source's channel vector is
        exactly null in the metric it creates (2e-16; the
        Kerr-Schild identity g^ab k_a k_b = eta^ab k_a k_b = 0) --
        each channel rides the very cone it builds; with two
        sources each channel fails nullity at O(w1 w2):
        INTERACTION IS CONE-BENDING -- one channel's geometry
        deflects the other's causal structure.

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
inv4 = _t.inv4
ETA = _t.ETA


def g_point(M):
    """The vacuum-selected point metric (Kerr-Schild Schwarzschild)."""
    def k(x):
        r = math.dist(x[1:], (0, 0, 0))
        return (-1.0, x[1] / r, x[2] / r, x[3] / r)
    return ks_metric(k, lambda x: 2 * M / math.dist(x[1:], (0, 0, 0)))


# =====================================================================
# battery instrument: geodesic integrator
# =====================================================================

def geodesic_step(g, x, u, dl, h=1e-4):
    def acc(x_, u_):
        G = christ4(g, x_, h)
        return [-sum(G[m][a][b] * u_[a] * u_[b]
                     for a in range(4) for b in range(4))
                for m in range(4)]
    k1v = acc(x, u)
    k1x = u
    x2 = [x[i] + 0.5 * dl * k1x[i] for i in range(4)]
    u2 = [u[i] + 0.5 * dl * k1v[i] for i in range(4)]
    k2v = acc(tuple(x2), u2)
    k2x = u2
    x3 = [x[i] + 0.5 * dl * k2x[i] for i in range(4)]
    u3 = [u[i] + 0.5 * dl * k2v[i] for i in range(4)]
    k3v = acc(tuple(x3), u3)
    k3x = u3
    x4 = [x[i] + dl * k3x[i] for i in range(4)]
    u4 = [u[i] + dl * k3v[i] for i in range(4)]
    k4v = acc(tuple(x4), u4)
    k4x = u4
    xn = tuple(x[i] + dl / 6 * (k1x[i] + 2 * k2x[i] + 2 * k3x[i]
                                + k4x[i]) for i in range(4))
    un = [u[i] + dl / 6 * (k1v[i] + 2 * k2v[i] + 2 * k3v[i] + k4v[i])
          for i in range(4)]
    return xn, un


def future_u0(gm, sp, timelike):
    """Future-directed u^0 for spatial coordinate velocity sp
    (the metric's g_00 < 0 makes the smaller quadratic root the
    past-directed one -- choose max)."""
    A = gm[0][0]
    B = 2 * sum(gm[0][1 + i] * sp[i] for i in range(3))
    C = sum(sp[i] * gm[1 + i][1 + j] * sp[j]
            for i in range(3) for j in range(3)) \
        + (1.0 if timelike else 0.0)
    disc = math.sqrt(B * B - 4 * A * C)
    return max((-B + disc) / (2 * A), (-B - disc) / (2 * A))


def light_bending(M, b, X0=40.0, dl=0.05):
    g = g_point(M)
    x = (0.0, -X0, b, 0.0)
    u0 = future_u0(g(x), (1.0, 0.0, 0.0), False)
    u = [u0, u0, 0.0, 0.0]
    while x[1] < X0:
        r = math.dist(x[1:], (0, 0, 0))
        x, u = geodesic_step(g, x, u, dl if r < 5.0 else 4 * dl)
    return math.atan2(-u[2], u[1])


def run_orbit(M, r_p, a_t, dt=0.01, orbits=3):
    """Integrate a bound orbit from periapsis; return (mean apsidal
    advance per orbit, a, e) with parabolic periapsis interpolation."""
    g = g_point(M)
    v_p = math.sqrt(M * (2 / r_p - 1 / a_t))
    x = (0.0, r_p, 0.0, 0.0)
    u0 = future_u0(g(x), (0.0, v_p, 0.0), True)
    u = [u0, 0.0, u0 * v_p, 0.0]
    hist, peri, rs = [], [], []
    steps = 0
    while len(peri) < orbits + 1 and steps < 900000:
        x, u = geodesic_step(g, x, u, dt)
        r = math.hypot(x[1], x[2])
        phi = math.atan2(x[2], x[1])
        rs.append(r)
        hist.append((r, phi))
        if len(hist) >= 3 and hist[-2][0] < hist[-3][0] \
                and hist[-2][0] < hist[-1][0]:
            r0, p0 = hist[-3]
            r1, p1 = hist[-2]
            r2, p2 = hist[-1]

            def uw(p, ref):
                while p - ref > math.pi:
                    p -= 2 * math.pi
                while p - ref < -math.pi:
                    p += 2 * math.pi
                return p
            p0, p2 = uw(p0, p1), uw(p2, p1)
            den = r0 - 2 * r1 + r2
            frac = 0.5 * (r0 - r2) / den if abs(den) > 1e-30 else 0.0
            peri.append(p1 + frac * 0.5 * (p2 - p0))
        steps += 1
    advs = []
    for i in range(len(peri) - 1):
        d = (peri[i + 1] - peri[i]) % (2 * math.pi)
        if d > math.pi:
            d -= 2 * math.pi
        advs.append(d)
    a = (min(rs) + max(rs)) / 2
    e = (max(rs) - min(rs)) / (max(rs) + min(rs))
    return sum(advs) / len(advs), a, e, advs


def g_two(M1, M2, d):
    """Two vacuum-profile channels superposed, separation d on x."""
    c1, c2 = (-d / 2, 0.0, 0.0), (d / 2, 0.0, 0.0)

    def g(x):
        m = [[ETA[i][j] for j in range(4)] for i in range(4)]
        for (c, M) in ((c1, M1), (c2, M2)):
            r = math.dist(x[1:], c)
            k = (-1.0, (x[1] - c[0]) / r, (x[2] - c[1]) / r,
                 (x[3] - c[2]) / r)
            w = 2 * M / r
            for i in range(4):
                for j in range(4):
                    m[i][j] += w * k[i] * k[j]
        return m
    return g


# =====================================================================
# 1. light bending
# =====================================================================

def verify_light_bending() -> None:
    M = 0.002
    for b in (1.0, 2.0):
        d = light_bending(M, b)
        gr = 4 * M / b
        assert abs(d - gr) / gr < 0.02, (d, gr)
        assert abs(d - 2 * M / b) / (2 * M / b) > 0.9
        print(f"    b = {b}: deflection {d:.6f} vs GR 4M/b = {gr:.6f}"
              f" (Newtonian 2M/b = {2 * M / b:.6f})")
    print()
    print("  EINSTEIN'S FULL DEFLECTION -- twice Newton's -- from the")
    print("  web's vacuum-selected metric.  The 1919 factor of 2 is")
    print("  the null structure of the channel form.")


# =====================================================================
# 2. perihelion precession
# =====================================================================

def verify_precession() -> None:
    rows = []
    for M in (0.005, 0.002):
        adv, a, e, advs = run_orbit(M, 0.3, 0.6)
        p = a * (1 - e * e)
        pred = 6 * math.pi * M / p
        rows.append((M, adv, pred, M / p))
        spread = max(advs) - min(advs)
        assert adv > 0, adv
        assert spread < 1e-3, advs
        print(f"    M = {M}: advance {adv:+.5f}/orbit "
              f"(spread {spread:.1e}) vs")
        print(f"      6 pi M/p = {pred:+.5f}  ratio "
              f"{adv / pred:.4f}  (M/p = {M / p:.4f})")
    x1 = (rows[0][1] / rows[0][2] - 1) / rows[0][3]
    x2 = (rows[1][1] / rows[1][2] - 1) / rows[1][3]
    assert abs(x1 - x2) / x1 < 0.15, (x1, x2)
    assert rows[1][1] / rows[1][2] < rows[0][1] / rows[0][2]
    print(f"    excess/(M/p): {x1:.2f}, {x2:.2f} -- the same")
    print(f"    coefficient: the gap is the SECOND-ORDER term, and")
    print(f"    the advance converges to GR's formula as M -> 0.")
    print()
    print("  PROGRADE PRECESSION AT EINSTEIN'S RATE -- exactly")
    print("  repeatable orbit to orbit, converging to 6 pi M/p.")


# =====================================================================
# 3. two bodies
# =====================================================================

def verify_two_body() -> None:
    d = 1.0
    pt = (0.0, 0.0, 0.4, 0.3)
    ratios = []
    for M in (0.01, 0.005, 0.0025):
        g = g_two(M, M, d)
        Ric = ricci4(g, pt, h=1e-3)
        mx = max(abs(Ric[i][j]) for i in range(4) for j in range(4))
        ratios.append(mx / (M * M))
        print(f"    M1 = M2 = {M}: off-source max|R_mn| = {mx:.2e}"
              f"  /M^2 = {mx / (M * M):.1f}")
    assert max(ratios) / min(ratios) < 1.05, ratios
    print("    the superposition violation scales EXACTLY as M1 M2:")
    print("    the web's nonlinearity, localized (this is where the")
    print("    post-Newtonian sector lives).")
    M = 0.005
    g = g_two(M, M, d)
    for r in (6.0, 10.0):
        pt2 = (0.0, 0.0, r, 0.0)
        G = christ4(g, pt2, 1e-4)
        a_r = -G[2][0][0] / (-g(pt2)[0][0])
        newt = -(2 * M) / r ** 2
        assert abs(a_r / newt - 1) < 0.02, (a_r, newt)
        print(f"    far field r = {r}: a_r/(-(M1+M2)/r^2) = "
              f"{a_r / newt:.4f} -- masses add.")
    # channel nullity
    g1 = g_two(0.01, 0.0, d)
    r1 = math.dist(pt[1:], (-d / 2, 0, 0))
    k1 = (-1.0, (pt[1] + d / 2) / r1, pt[2] / r1, pt[3] / r1)
    gi1 = inv4(g1(pt))
    nn1 = sum(gi1[a][b] * k1[a] * k1[b]
              for a in range(4) for b in range(4))
    gi2 = inv4(g_two(0.01, 0.01, d)(pt))
    nn2 = sum(gi2[a][b] * k1[a] * k1[b]
              for a in range(4) for b in range(4))
    assert abs(nn1) < 1e-12, nn1
    assert abs(nn2) > 1e-3, nn2
    print(f"    channel nullity: single-source g^ab k_a k_b = "
          f"{nn1:.0e}")
    print(f"    (exact -- the Kerr-Schild identity: each channel")
    print(f"    rides the very cone it creates); two-source = "
          f"{nn2:.1e}:")
    print(f"    INTERACTION IS CONE-BENDING -- one channel's geometry")
    print(f"    deflects the other's causal structure, at O(w1 w2).")


def run_verification_suite() -> None:
    sections = [
        ("Light bending", verify_light_bending),
        ("Perihelion precession", verify_precession),
        ("Two bodies", verify_two_body),
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
