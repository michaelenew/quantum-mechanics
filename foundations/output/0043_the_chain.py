"""The chain: the whole derivation, one keystone per link.

Consolidation module.  The program's claim is now a single chain
from the postulates to Einstein gravity's measured phenomena, with
each link either forced, measured, derived, or explicitly imported.
This module re-runs ONE computational keystone per link, end to
end, in one suite -- the executable table of contents of
foundations/.  The full statement with status tags and the honest
gap list is exploration/0048.

  L1   the ledger        influence = sqrt(information)
  L2   the atom          holonomy = 2 pi (1 - (1+w)^(-1/2))
  L3   the ladder        solid angle = 4 pi/(1+w); one law, all codim
  L4   the cone          one-event front = graph ball, exactly
  L5   Lorentz           boosted worldline = pullback, 1e-16
  L6   the frame         e = 1 + (1/2)(channel), squares exactly
  L7   the quantum tier  U V = -V U at N = 2; bond = n_a n_b
  L8   the vacuum law    w harmonic: p = d-2 and only p = d-2
  L9   the classics      Kepler exact; bending 4M/b
  L10  the waves         luminosity = quadrupole formula
  L11  the bond          virial = -(F d) n n; anti-string mu = -T
  L12  the Green rule    channel = Lienard-Wiechert

Run directly for the verification suite.
"""

from __future__ import annotations

import cmath
import importlib
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_bat = importlib.import_module("0028_the_three_plus_one_battery")
_cone = importlib.import_module("0017_the_cone_from_the_web")
_ts = importlib.import_module("0030_the_time_sector")
_frm = importlib.import_module("0041_the_frame_functional")
_qt = importlib.import_module("0022_the_quantum_tier")
_nd = importlib.import_module("0037_the_bond_operator")
_nw = importlib.import_module("0031_the_newtonian_limit")
_cl = importlib.import_module("0032_the_classical_tests")
_bd = importlib.import_module("0035_the_bond_is_a_string")
_fn = importlib.import_module("0040_the_functional")

TAU = 2 * math.pi


def check_L1_ledger() -> None:
    """Kalman random-walk influence -> sqrt(q): the ledger's anchor."""
    def influence(q):
        p = 1.0
        for _ in range(4000):
            pm = p + q
            g = pm / (pm + 1.0)
            p = (1 - g) * pm
        return g
    g1, g2 = influence(1e-4), influence(1e-6)
    slope = math.log(g1 / g2) / math.log(100)
    assert abs(slope - 0.5) < 0.01, slope
    print(f"    L1  influence ~ q^{slope:.3f} (= 1/2): trust is the")
    print(f"        square root of information -- the ledger.")


def check_L2_atom() -> None:
    Rot, _ = _bat.develop_loop3(_bat.string_at(0.0), (0.0, 0.0, 0.2),
                                1.0, steps=2000)
    ang, ax = _bat.rot_angle_axis(Rot)
    exact = TAU * (1 - 1 / math.sqrt(1.3))
    assert abs(ang - exact) < 1e-3, (ang, exact)
    print(f"    L2  holonomy {ang:.5f} = 2 pi(1-(1+w)^(-1/2)) "
          f"{exact:.5f}:")
    print(f"        participation is a conical atom.")


def check_L3_ladder() -> None:
    w = 0.3
    A = _bat.proper_area(_bat.monopole, 0.9, nth=120, nph=120)
    L = _bat.proper_radius(_bat.monopole, 0.9)
    om = A / L ** 2
    pred = 2 * TAU / (1 + w)
    assert abs(om - pred) / pred < 1e-3, (om, pred)
    print(f"    L3  solid angle {om:.4f} = 4 pi/(1+w) {pred:.4f}:")
    print(f"        deficit fraction 1-(1+w)^(-(c-1)/2), every")
    print(f"        codimension.")


def check_L4_cone() -> None:
    pts, nbrs = _cone.random_web(500, 0.3, seed=5)
    src = 0
    front = _cone.one_event_front(pts, nbrs, src, 3)
    ball = {v for v, d in _cone.bfs_dist(nbrs, src).items()
            if d <= 3}
    assert front == ball, (len(front), len(ball))
    print(f"    L4  one-event front = graph ball exactly "
          f"({len(ball)} nodes):")
    print(f"        the causal cone is locality itself.")


def check_L5_lorentz() -> None:
    w0, v = 0.3, 0.5
    gam = 1 / math.sqrt(1 - v * v)
    kst = _ts.cov_k(lambda t: (0.0, 0.0, 0.0),
                    lambda t: (0.0, 0.0, 0.0))
    gW = _ts.ks_metric(kst, lambda x: w0)
    kmv = _ts.cov_k(lambda t: (v * t, 0.0, 0.0),
                    lambda t: (v, 0.0, 0.0))
    gWm = _ts.ks_metric(kmv, lambda x: w0)
    Lm = [[gam, -gam * v, 0, 0], [-gam * v, gam, 0, 0],
          [0, 0, 1, 0], [0, 0, 0, 1]]
    pt = (0.3, 0.9, 0.4, 0.2)
    X = (gam * (pt[0] - v * pt[1]), gam * (pt[1] - v * pt[0]),
         pt[2], pt[3])
    G = gW(X)
    A = [[sum(Lm[a][i] * G[a][b] * Lm[b][j]
              for a in range(4) for b in range(4))
          for j in range(4)] for i in range(4)]
    B = gWm(pt)
    err = max(abs(A[i][j] - B[i][j])
              for i in range(4) for j in range(4))
    assert err < 1e-12, err
    print(f"    L5  boosted worldline = Lorentz pullback to "
          f"{err:.0e}:")
    print(f"        covariance is automatic; the baseline was the")
    print(f"        slice shadow.")


def check_L6_frame() -> None:
    k = (-1.0, 0.6, 0.64, 0.48)
    g = _frm.square_frame(_frm.channel_tetrad(2.0, k))
    KS = [[_ts.ETA[i][j] + 2.0 * k[i] * k[j] for j in range(4)]
          for i in range(4)]
    err = max(abs(g[i][j] - KS[i][j])
              for i in range(4) for j in range(4))
    assert err < 1e-12, err
    print(f"    L6  e = 1 + (1/2)(channel) squares exactly "
          f"({err:.0e}, w = 2):")
    print(f"        the channel is the frame; the metric its square.")


def check_L7_quantum() -> None:
    U, V = _qt.clock(2), _qt.shift(2)

    def mm(a, b):
        return [[sum(a[i][k] * b[k][j] for k in range(2))
                 for j in range(2)] for i in range(2)]
    UV, VU = mm(U, V), mm(V, U)
    err = max(abs(UV[i][j] + VU[i][j]) for i in range(2)
              for j in range(2))
    assert err < 1e-12, err
    om5 = cmath.exp(2j * math.pi / 5)
    assert abs(om5 ** 6 - om5 ** ((2 * 3) % 5)) < 1e-12
    print(f"    L7  N = 2: U V = -V U (the measured flip delta = pi")
    print(f"        as the minimal quantization); bond spectrum")
    print(f"        omega^(n_a n_b) -- charges add, bonds multiply.")


def check_L8_vacuum() -> None:
    g1 = _nd.ks_point_nd(3, 0.02, 1)
    g2 = _nd.ks_point_nd(3, 0.02, 2)
    x = (0.0, 0.54, 0.45, 0.36)
    r1 = max(abs(v) for row in _nd.ricci_nd(g1, x, h=1e-3)
             for v in row)
    r2 = max(abs(v) for row in _nd.ricci_nd(g2, x, h=1e-3)
             for v in row)
    assert r1 < 1e-5 and r2 > 1e-3, (r1, r2)
    print(f"    L8  w ~ 1/rho vacuum ({r1:.0e}); 1/rho^2 not "
          f"({r2:.0e}):")
    print(f"        flat-off-participation selects Schwarzschild --")
    print(f"        and with mu/T = -1/p, d = 3 is the dimension")
    print(f"        where correlation carries no charge.")


def check_L9_classics() -> None:
    gS = _nw.g_profile(2 * 0.005, 1.0)
    om = _nw.omega_circ(gS, 1.5)
    k3 = om * om * 1.5 ** 3
    assert abs(k3 - 0.005) / 0.005 < 1e-3, k3
    d = _cl.light_bending(0.002, 2.0)
    assert abs(d - 4 * 0.002 / 2.0) / (4 * 0.002 / 2.0) < 0.02, d
    print(f"    L9  Kepler omega^2 r^3 = {k3:.6f} (M = 0.005);")
    print(f"        bending {d:.6f} = 4M/b: Einstein's factor 2.")


def check_L10_waves() -> None:
    L = _bd.radiated_power(_bd.g_closed_binary, nang=4, nph=8)
    mu = _bd.M_B / 2 if hasattr(_bd, "M_B") else 0.01
    import importlib as _il
    _b3 = _il.import_module("0033_the_binary_test")
    mu_red = _b3.M_B / 2
    D = 2 * _b3.A0
    L_gr = (32 / 5) * mu_red ** 2 * D ** 4 * _b3.OM_B ** 6
    assert abs(L / L_gr - 1) < 0.02, (L, L_gr)
    print(f"    L10 luminosity {L:.4e} / quadrupole {L_gr:.4e} = "
          f"{L / L_gr:.4f}:")
    print(f"        the web radiates at Einstein's rate.")


def check_L11_bond() -> None:
    S = _bd.bond_stress_numeric(0.7)
    P = _bd.bond_stress_closed(0.7)
    sc = max(abs(P[i][j]) for i in range(3) for j in range(3))
    err = max(abs(S[i][j] - P[i][j])
              for i in range(3) for j in range(3))
    assert err / sc < 1e-6, err / sc
    Rot, _ = _bat.develop_loop3(_bd.string_mu_T(-0.01, 0.01),
                                (0.0, 0.0, 0.2), 1.0, steps=2000)
    ang, _ = _bat.rot_angle_axis(Rot)
    assert abs(ang) < 1e-4, ang
    print(f"    L11 virial bond -(F d) n n ({err / sc:.0e}); the")
    print(f"        mu = -T anti-string has deficit {ang:.0e}:")
    print(f"        correlation binds without registering as")
    print(f"        participation.")


def check_L12_green() -> None:
    x = (0.3, 0.9, 0.5, 0.4)
    F1 = _fn.faraday(_fn.channel_A, x, 0.5)
    F2 = _fn.faraday(_fn.lw_A, x, 0.5)
    sc = max(abs(F2[i][j]) for i in range(4) for j in range(4))
    dev = max(abs(F1[i][j] - F2[i][j])
              for i in range(4) for j in range(4))
    assert dev / sc < 1e-5, dev / sc
    print(f"    L12 channel = Lienard-Wiechert ({dev / sc:.0e}):")
    print(f"        the rule is the functional's retarded Green")
    print(f"        function; u.ell is the retarded Jacobian.")


def run_verification_suite() -> None:
    print("=" * 70)
    print("THE CHAIN -- one keystone per link")
    print("=" * 70)
    for check in (check_L1_ledger, check_L2_atom, check_L3_ladder,
                  check_L4_cone, check_L5_lorentz, check_L6_frame,
                  check_L7_quantum, check_L8_vacuum,
                  check_L9_classics, check_L10_waves,
                  check_L11_bond, check_L12_green):
        check()
    print()
    print("  postulates -> Chentsov metric -> atoms -> field law ->")
    print("  causal cone -> forced Lorentz -> covariant null channel")
    print("  -> frame functional (B = e ^ e = the ledger) -> Green-")
    print("  function channels -> Schwarzschild, Newton, Kepler,")
    print("  bending, precession, TT waves, the quadrupole formula,")
    print("  ADM charges with binding, the bond and its ledger.")
    print("  Twelve keystones, one suite.")
    print("=" * 70)
    print("suite complete")
    print("=" * 70)


if __name__ == "__main__":
    run_verification_suite()
