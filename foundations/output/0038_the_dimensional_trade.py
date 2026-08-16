"""The dimensional trade: charge for force, and the atom recovered.

0042 measured that the web's vacuum principle selects the harmonic
profile in every dimension.  Running that ladder DOWN, to d = 2,
returns the program's own founding object -- and exposes what the
dimension is actually trading.

  s1  THE LADDER RUN DOWN: THE ATOM IS THE d = 2 VACUUM.  In two
      spatial dimensions the harmonic exponent is p = d - 2 = 0,
      i.e. CONSTANT channel strength.  Measured: vacuum at p = 0
      (2e-6) and nowhere else (p = 0.5, 1 fail at 1e-1); the test
      particle feels NO FORCE (machine zero at two radii -- 0020's
      2+1 no-pair-force, now derived from the vacuum principle);
      and the deficit is 0.772467 against the exact atom
      2 pi (1 - (1+w)^(-1/2)) = 0.772467.  The founding object of
      this program (0014's cone, 0019's atom) IS the d = 2 case of
      the same field law that gives Schwarzschild at d = 3.

  s2  TOPOLOGICAL VERSUS GEOMETRIC HOLONOMY.  The charge reader
      around a source, as a function of loop radius:
        codim 2 (string / 2+1 point): 0.772467 at R = 0.6, 1, 2, 4
          -- EXACTLY R-independent: topological;
        codim 3 (point in 3D):        0.4661, 0.2924, 0.1514,
          0.0771, tracking 2 pi M / R -- geometric, dilutes away.
      The codimension decides whether a charge is a topological
      invariant or a curvature integral.

  s3  THE TRADE.  Combining s1, s2 and 0041/0042:

        d = 2:  no force, topological deficit charge
        d = 3:  Newton's force, bond conically INVISIBLE
        d >= 4: force AND transverse bond charge

      Three spatial dimensions is where the bond has traded its
      charge for a force -- the unique dimension in which
      correlation acts without registering as participation.  This
      refines 0042's operator claim honestly: the braiding phase
      omega^(n_a n_b) is the 2+1 REALIZATION of the bond's product
      structure (the dimension where the bond is topological and
      forceless); in 3+1 the same bilinearity appears dynamically,
      as m_a m_b / d.  One product structure, two carriers, chosen
      by dimension.

  s4  THE HALF IS KINEMATICS, NOT GRAVITY.  0039's 50/50 split of
      I-ddot between the kinetic tensor and the bond holds for
      EVERY force law (ratio 1.000000 at p = 0.5, 1, 2, 3): it
      follows from m Omega^2 a = F alone, i.e. from circular
      motion, with no force law and no dimension entering.  The
      "missing half" was never a gravitational coincidence -- it
      is what binding means for a closed orbit.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_o = importlib.import_module("0037_the_bond_operator")
_b = importlib.import_module("0028_the_three_plus_one_battery")
ricci_nd, ks_point_nd, christ_nd = _o.ricci_nd, _o.ks_point_nd, \
    _o.christ_nd
develop_loop3, rot_angle_axis = _b.develop_loop3, _b.rot_angle_axis

TAU = 2 * math.pi
W_A = 0.3
M_P = 0.05


# =====================================================================
# 1. the ladder run down: the atom is the d = 2 vacuum
# =====================================================================

def d2_vacuum_scan():
    out = []
    for p in (0.0, 0.5, 1.0):
        g = ks_point_nd(2, W_A, p)
        worst = 0.0
        for s in (0.8, 1.5):
            R = ricci_nd(g, (0.0, s * 0.6, s * 0.8), h=1e-3)
            worst = max(worst, max(abs(R[i][j])
                                   for i in range(3) for j in range(3)))
        out.append((p, worst))
    return out


def d2_rest_accel(r):
    g = ks_point_nd(2, W_A, 0.0)
    G = christ_nd(g, (0.0, r, 0.0), 1e-4)
    return -G[1][0][0] / (-g((0.0, r, 0.0))[0][0])


def d2_deficit(r=1.0, nth=4000, nrad=2000):
    """Deficit of the d = 2 constant-w channel: 2 pi - C/L."""
    g = ks_point_nd(2, W_A, 0.0)
    C = 0.0
    for k in range(nth):
        th = TAU * (k + 0.5) / nth
        x = (0.0, r * math.cos(th), r * math.sin(th))
        t = (-r * math.sin(th), r * math.cos(th))
        gm = g(x)
        E = sum(t[i] * gm[1 + i][1 + j] * t[j]
                for i in range(2) for j in range(2))
        C += math.sqrt(E) * (TAU / nth)
    L = 0.0
    for k in range(nrad):
        s = r * (k + 0.5) / nrad
        L += math.sqrt(g((0.0, s, 0.0))[1][1]) * (r / nrad)
    return TAU - C / L


def verify_atom_is_d2_vacuum() -> None:
    print("    d = 2 vacuum scan (max|R_mn| off-source):")
    for p, v in d2_vacuum_scan():
        tag = "   <-- VACUUM (constant w)" if p == 0.0 else ""
        print(f"      p = {p}: {v:.1e}{tag}")
        if p == 0.0:
            assert v < 1e-5, v
        else:
            assert v > 1e-2, (p, v)
    for r in (1.0, 2.0):
        a = d2_rest_accel(r)
        assert abs(a) < 1e-10, a
        print(f"    radial acceleration at r = {r}: {a:+.1e} -- NO "
              f"FORCE")
    dfc = d2_deficit()
    exact = TAU * (1 - 1 / math.sqrt(1 + W_A))
    assert abs(dfc - exact) < 1e-4, (dfc, exact)
    print(f"    deficit {dfc:.6f} vs the exact atom "
          f"2 pi (1-(1+w)^(-1/2)) = {exact:.6f}")
    print()
    print("  THE ATOM IS THE d = 2 VACUUM.  The founding object of")
    print("  this program (0014's cone, 0019's atom) is the two-")
    print("  dimensional case of the same field law that gives")
    print("  Schwarzschild at d = 3 -- and 0020's measured 'no pair")
    print("  force in 2+1' is now derived from the vacuum principle,")
    print("  not observed as a curiosity.")


# =====================================================================
# 2. topological versus geometric holonomy
# =====================================================================

def string_metric(x):
    rho = math.hypot(x[0], x[1])
    u = (x[0] / rho, x[1] / rho, 0.0)
    return [[(1 if i == j else 0) + W_A * u[i] * u[j]
             for j in range(3)] for i in range(3)]


def point_metric(x):
    r = math.sqrt(sum(c * c for c in x))
    u = tuple(c / r for c in x)
    w = 2 * M_P / r
    return [[(1 if i == j else 0) + w * u[i] * u[j]
             for j in range(3)] for i in range(3)]


def verify_topological_vs_geometric() -> None:
    print("    codim 2 (string / a 2+1 point), holonomy vs radius:")
    vals = []
    for R in (0.6, 1.0, 2.0, 4.0):
        Rot, _ = develop_loop3(string_metric, (0.0, 0.0, 0.2), R,
                               steps=3000)
        ang, _ = rot_angle_axis(Rot)
        vals.append(ang)
        print(f"      R = {R}: {ang:.6f}")
    assert max(vals) - min(vals) < 1e-6, vals
    print(f"      spread {max(vals) - min(vals):.1e} -- EXACTLY")
    print(f"      R-independent: TOPOLOGICAL.")
    print("    codim 3 (a point in 3D), holonomy vs radius:")
    prev = None
    for R in (0.6, 1.0, 2.0, 4.0):
        Rot, _ = develop_loop3(point_metric, (0.0, 0.0, 0.0), R,
                               steps=3000)
        ang, _ = rot_angle_axis(Rot)
        print(f"      R = {R}: {ang:.6f}   (2 pi M/R = "
              f"{TAU * M_P / R:.6f})")
        if prev is not None:
            assert ang < 0.75 * prev, (ang, prev)
        prev = ang
    print("      dilutes as 1/R: GEOMETRIC.")
    print()
    print("  THE CODIMENSION DECIDES whether a charge is a")
    print("  topological invariant or a curvature integral.")


# =====================================================================
# 3. the trade
# =====================================================================

def verify_the_trade() -> None:
    rows = [
        ("d = 2", "constant w (the atom)", "none (measured 0)",
         "topological deficit"),
        ("d = 3", "w = 2M/rho", "Newton", "ZERO (0041)"),
        ("d >= 4", "w = 2M/rho^(d-2)", "yes", "nonzero (0042)"),
    ]
    print("    dim      vacuum profile          force        "
          "bond's charge")
    print("    " + "-" * 64)
    for a, b, c, e in rows:
        print(f"    {a:8s} {b:23s} {c:12s} {e}")
    print()
    print("  THREE SPATIAL DIMENSIONS IS WHERE THE BOND HAS TRADED")
    print("  ITS CHARGE FOR A FORCE -- the unique dimension in which")
    print("  correlation acts without registering as participation.")
    print("  This refines 0042's operator claim: the braiding phase")
    print("  omega^(n_a n_b) is the 2+1 REALIZATION of the bond's")
    print("  product structure -- the dimension where the bond is")
    print("  topological and forceless -- while in 3+1 the same")
    print("  bilinearity appears dynamically as m_a m_b / d.  One")
    print("  product structure, two carriers, chosen by dimension.")


# =====================================================================
# 4. the half is kinematics
# =====================================================================

M_O, A_O = 0.02, 0.125


def half_split(p, t=0.9):
    """Kinetic and bond tensors of an equal-mass circular binary
    under F = m^2/d^(p+1)."""
    d = 2 * A_O
    F = M_O * M_O / d ** (p + 1)
    om = math.sqrt(F / (M_O * A_O))
    v = om * A_O
    ph = om * t
    pdir = (-math.sin(ph), math.cos(ph), 0.0)
    ndir = (math.cos(ph), math.sin(ph), 0.0)
    K = [[2 * M_O * v * v * pdir[i] * pdir[j] for j in range(3)]
         for i in range(3)]
    S = [[-(F * d) * ndir[i] * ndir[j] for j in range(3)]
         for i in range(3)]
    nk = math.sqrt(sum(K[i][j] ** 2
                       for i in range(3) for j in range(3)))
    ns = math.sqrt(sum(S[i][j] ** 2
                       for i in range(3) for j in range(3)))
    return nk, ns


def verify_half_is_kinematics() -> None:
    for p in (0.5, 1.0, 2.0, 3.0):
        nk, ns = half_split(p)
        assert abs(nk / ns - 1) < 1e-12, (p, nk / ns)
        print(f"    p = {p}: |kinetic| = {nk:.6e}  |bond| = "
              f"{ns:.6e}  ratio {nk / ns:.6f}")
    print()
    print("  THE HALF IS KINEMATICS, NOT GRAVITY.  The identity is")
    print("  m Omega^2 a = F  =>  2 m v^2 = F d, which uses circular")
    print("  motion ALONE -- no force law, no dimension.  0039's")
    print("  'missing half' was never a gravitational coincidence:")
    print("  it is what binding means for a closed orbit.")


def run_verification_suite() -> None:
    sections = [
        ("The ladder run down: the atom is the d = 2 vacuum",
         verify_atom_is_d2_vacuum),
        ("Topological versus geometric holonomy",
         verify_topological_vs_geometric),
        ("The trade", verify_the_trade),
        ("The half is kinematics", verify_half_is_kinematics),
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
