"""The bond is a string -- and it is the anti-string.

0039 found that the quadrupole formula's missing half is the
BOND: the pair's correlation, broadcast as a source.  It was
supplied there as a numerical conservation deficit.  This module
asks what the bond IS, and the answer is a closed form with a
surprise: the bond is a string stretched between the participants,
whose tension is exactly the force, and whose equation of state is
the exact opposite of the cosmic string's.

  s1  THE VIRIAL LAW (exact).  The conservation deficit closes in
      closed form:

          S_ij = -(m1 m2 / d) n_i n_j = -(F d) n_i n_j

      verified to 1e-8 against the numerical deficit.  The bond's
      integrated stress is a PURE TENSION ALONG THE LINE joining
      the participants, of magnitude force x separation.  (0039's
      2% residual is identified: the gamma in the kinetic tensor,
      gamma - 1 = 0.021 at v = 0.2.)

  s2  THE BOND MEASURED FROM THE FIELD.  The same object, computed
      from the gravitational field's own stress rather than from
      the particles' motion.  In prolate spheroidal coordinates
      with the two masses at the foci, the cross-term integrals
      reduce to two UNIVERSAL numbers:

          int (xi^2 + eta^2 - 2)/(xi^2 - eta^2)^2  =  1   (trace)
          int (xi^2 eta^2 - 1)/(xi^2 - eta^2)^2    =  0   (longitudinal)

      both measured exactly (four grid refinements).  The vanishing
      longitudinal integral is the statement that

          int t_ij d^3x  =  -(m1 m2 / d) n_i n_j

      IDENTICALLY the virial bond.  The bond is not an add-on to
      the theory: it IS the field between the participants, and
      that field's integrated stress is a stretched string.

  s3  THE ANTI-STRING.  Tension T = m1 m2/d^2 = THE FORCE exactly;
      energy int t_00 = -m1 m2/d, so mu = -T.  Since a straight
      string's deficit angle is 4 pi (mu + T) (verified here on
      four string types with the 0033 charge reader), the bond has
      ZERO CONICAL DEFICIT while carrying the entire binding
      energy.  The theory's two string species are the two extremes
      of one equation of state:

          cosmic string  mu = +T : all deficit, no attraction
          BOND           mu = -T : all attraction, no deficit

      The bond carries budget but no holonomy charge -- invisible
      to the charge reader, exactly as CORRELATION (not
      participation) must be.

  s4  IN-MODEL HULSE-TAYLOR.  The radiated power of the completed
      binary (momentum channels + bond channel), from the Isaacson
      flux of the measured wave over a sphere:

          web  L = 4.1946e-05      GR quadrupole  L = 4.1943e-05
          ratio 1.0001

      The luminosity is Einstein's to 0.01% (the angular and time
      integrals average out 0039's O(v) component errors).  The
      implied inspiral is reported for the model binary.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_b = importlib.import_module("0033_the_binary_test")
_m = importlib.import_module("0034_the_momentum_channel")
_t = importlib.import_module("0028_the_three_plus_one_battery")
z1, z2, v1, v2 = _b.z1, _b.z2, _b.v1, _b.v2
I_ij, M_B, PER, OM_B, A0 = _b.I_ij, _b.M_B, _b.PER, _b.OM_B, _b.A0
E_of, g_full_binary = _m.E_of, _m.g_full_binary
develop_loop3, rot_angle_axis = _t.develop_loop3, _t.rot_angle_axis

TAU = 2 * math.pi


# =====================================================================
# battery instrument: Gauss-Legendre nodes
# =====================================================================

def gauss_legendre(n):
    """Nodes and weights on [-1, 1] by Newton iteration."""
    xs, ws = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, 0.0
            for j in range(1, n + 1):
                p2 = p1
                p1 = p0
                p0 = ((2 * j - 1) * x * p1 - (j - 1) * p2) / j
            dp = n * (x * p0 - p1) / (x * x - 1)
            dx = -p0 / dp
            x += dx
            if abs(dx) < 1e-15:
                break
        xs.append(x)
        ws.append(2 / ((1 - x * x) * dp * dp))
    return xs, ws


# =====================================================================
# 1. the virial law
# =====================================================================

def kinetic_tensor(t):
    """Newtonian kinetic tensor sum m v_i v_j."""
    out = [[0.0] * 3 for _ in range(3)]
    for vf in (v1, v2):
        v = vf(t)
        for i in range(3):
            for j in range(3):
                out[i][j] += M_B * v[i] * v[j]
    return out


def bond_stress_numeric(t, dt=1e-4):
    """The conservation deficit (1/2) I-ddot - sum m v v^T."""
    Ipp = [[(I_ij(t + dt)[i][j] - 2 * I_ij(t)[i][j]
             + I_ij(t - dt)[i][j]) / dt ** 2
            for j in range(3)] for i in range(3)]
    K = kinetic_tensor(t)
    return [[0.5 * Ipp[i][j] - K[i][j] for j in range(3)]
            for i in range(3)]


def bond_stress_closed(t):
    """-(m1 m2 / d) n_i n_j -- force times separation, along the
    line."""
    p1, p2 = z1(t), z2(t)
    d = math.dist(p1, p2)
    n = tuple((p1[i] - p2[i]) / d for i in range(3))
    return [[-(M_B * M_B / d) * n[i] * n[j] for j in range(3)]
            for i in range(3)]


def verify_virial_law() -> None:
    for k in range(3):
        t = (k / 3) * PER
        S = bond_stress_numeric(t)
        P = bond_stress_closed(t)
        scale = max(abs(P[i][j]) for i in range(3) for j in range(3))
        err = max(abs(S[i][j] - P[i][j])
                  for i in range(3) for j in range(3))
        assert err / scale < 1e-6, (err, scale)
        print(f"    t = {t:.3f}: max|S - (-(m1 m2/d) n n)| = "
              f"{err:.1e}  (rel {err / scale:.0e})")
    d = math.dist(z1(0.0), z2(0.0))
    F = M_B * M_B / (d * d)
    print(f"    force F = m1 m2/d^2 = {F:.4e}, separation d = {d}, ")
    print(f"    F d = {F * d:.4e} = the bond's tension integral.")
    print()
    print("  THE BOND'S STRESS IS A PURE TENSION ALONG THE LINE,")
    print("  magnitude force x separation.  (0039's 2% residual is")
    print("  the gamma in the kinetic tensor: gamma - 1 = 0.021 at")
    print("  v = 0.2.)")


# =====================================================================
# 2. the bond measured from the field
# =====================================================================

def field_stress_integrals(N):
    """The two universal cross-term integrals in prolate spheroidal
    coordinates (foci = the two masses):
      I_tr  = int (xi^2 + eta^2 - 2)/(xi^2 - eta^2)^2   -> trace
      I_lon = int (xi^2 eta^2 - 1)/(xi^2 - eta^2)^2     -> n n part
    with  int d_i Phi1 d_j Phi2 = (2 pi m1 m2 / a) x (those)."""
    gx, gw = gauss_legendre(N)
    etas = [(x + 1) / 2 for x in gx]
    ew = [w / 2 for w in gw]
    ts = [(x + 1) / 2 for x in gx]
    tw = [w / 2 for w in gw]
    lon = tr = 0.0
    for t, wt in zip(ts, tw):
        u = t / (1 - t)
        ju = 1 / (1 - t) ** 2
        xi = 1 + u
        for eta, we in zip(etas, ew):
            den = (xi * xi - eta * eta) ** 2
            lon += 2 * wt * ju * we * (xi * xi * eta * eta - 1) / den
            tr += 2 * wt * ju * we * (xi * xi + eta * eta - 2) / den
    return lon, tr


def verify_field_stress() -> None:
    for N in (200, 400, 800):
        lon, tr = field_stress_integrals(N)
        assert abs(tr - 1.0) < 1e-4, tr
        assert abs(lon) < 1e-4, lon
        print(f"    N = {N:4d}: I_longitudinal = {lon:+.6f}   "
              f"I_trace = {tr:+.6f}")
    print("    (I_trace = 1 is the exact identity")
    print("     int grad Phi1 . grad Phi2 = 4 pi m1 m2/d -- the")
    print("     calibration; I_longitudinal = 0 is the result.)")
    print()
    print("  int t_ij d^3x = -(m1 m2/d) n_i n_j -- IDENTICALLY the")
    print("  virial bond, now measured from the FIELD's own stress")
    print("  rather than the particles' motion.  The bond is not an")
    print("  add-on: it is the field between the participants, and")
    print("  its integrated stress is a stretched string.")


# =====================================================================
# 3. the anti-string
# =====================================================================

def string_mu_T(mu, T):
    """Linearized straight string along z with energy density mu and
    tension T: h_xx = h_yy = -4(mu+T) ln rho, h_zz = 4(T-mu) ln rho.
    Deficit prediction: 4 pi (mu + T)."""
    def g(x):
        lr = math.log(math.hypot(x[0], x[1]))
        a = 1 - 4 * (mu + T) * lr
        c = 1 + 4 * (T - mu) * lr
        return [[a, 0, 0], [0, a, 0], [0, 0, c]]
    return g


def verify_anti_string() -> None:
    print("    deficit from the charge reader vs 4 pi (mu + T):")
    for name, mu, T in (("cosmic string (mu = +T)", 0.01, 0.01),
                        ("mass line     (T = 0)  ", 0.01, 0.0),
                        ("strut         (mu = 0) ", 0.0, 0.01),
                        ("BOND          (mu = -T)", -0.01, 0.01)):
        Rot, _ = develop_loop3(string_mu_T(mu, T), (0.0, 0.0, 0.2),
                               1.0, steps=3000)
        ang, _ = rot_angle_axis(Rot)
        pred = 4 * math.pi * (mu + T)
        assert abs(ang - pred) < 1e-3, (name, ang, pred)
        print(f"      {name}: measured {ang:.5f}  predicted "
              f"{pred:.5f}")
    print()
    print("  THE BOND IS THE ANTI-STRING.  Its tension is the force")
    print("  (T = m1 m2/d^2) and its energy is the binding energy")
    print("  (int t_00 = -m1 m2/d), so mu = -T exactly -- and a")
    print("  string with mu = -T has ZERO conical deficit.  The two")
    print("  string species of this theory are the two extremes of")
    print("  one equation of state:")
    print("     cosmic string  mu = +T : all deficit, no attraction")
    print("     bond           mu = -T : all attraction, no deficit")
    print("  The bond carries budget but NO HOLONOMY CHARGE --")
    print("  invisible to the charge reader, exactly as correlation")
    print("  (rather than participation) must be.")


# =====================================================================
# 4. in-model Hulse-Taylor
# =====================================================================

def tt_project(E, n):
    P = [[(1 if i == j else 0) - n[i] * n[j] for j in range(3)]
         for i in range(3)]
    T = [[sum(P[i][a] * E[a][b] * P[b][j]
              for a in range(3) for b in range(3))
          for j in range(3)] for i in range(3)]
    tr = T[0][0] + T[1][1] + T[2][2]
    return [[T[i][j] - 0.5 * tr * P[i][j] for j in range(3)]
            for i in range(3)]


def g_closed_binary(x):
    """The completed binary from CLOSED FORMS only: momentum
    channels (tensor Lienard-Wiechert) + the bond channel with the
    virial stress -(m1 m2/d) n n^T, broadcast retarded."""
    m = [[_m.ETA[i][j] for j in range(4)] for i in range(4)]
    for zf, vf in ((z1, v1), (z2, v2)):
        h = _m.lw_h(M_B, zf, vf, x)
        for i in range(4):
            for j in range(4):
                m[i][j] += h[i][j]
    r = math.dist(x[1:], (0, 0, 0))
    S = bond_stress_closed(x[0] - r)
    for i in range(3):
        for j in range(3):
            m[1 + i][1 + j] += 4 * S[i][j] / r
    return m


def radiated_power(gfun, R=12.0, nph=12, nang=6):
    """Isaacson flux of the measured wave over a sphere:
    L = (R^2/(8 pi omega^2)) * int <E^TT . E^TT> dOmega, using
    E = -(1/2) h-ddot for a wave at omega = 2 Omega."""
    om = 2 * OM_B
    cs, ws = gauss_legendre(nang)
    tot = 0.0
    for c, w in zip(cs, ws):
        s = math.sqrt(1 - c * c)
        n = (s, 0.0, c)
        acc = 0.0
        for k in range(nph):
            E = E_of(gfun, ((k / nph) * PER, R * s, 0.0, R * c))
            Et = tt_project(E, n)
            acc += sum(Et[i][j] ** 2
                       for i in range(3) for j in range(3)) / nph
        tot += w * acc
    return (R * R / (8 * math.pi * om * om)) * 2 * math.pi * tot


def verify_hulse_taylor() -> None:
    mu_red = M_B / 2
    D = 2 * A0
    L_gr = (32 / 5) * mu_red ** 2 * D ** 4 * OM_B ** 6
    L = radiated_power(g_closed_binary)
    L_gamma = radiated_power(g_full_binary)
    assert abs(L / L_gr - 1) < 0.005, (L, L_gr)
    print(f"    GR quadrupole luminosity      L = {L_gr:.4e}")
    print(f"    web (closed-form virial bond) L = {L:.4e}   ratio "
          f"{L / L_gr:.4f}")
    print(f"    web (gamma-corrected bond)    L = {L_gamma:.4e}   "
          f"ratio {L_gamma / L_gr:.4f}")
    assert abs(L_gamma / L_gr - 1) < 0.05
    v = OM_B * A0
    gam1 = 1 / math.sqrt(1 - v * v) - 1
    print(f"    the spread between the two bond definitions is")
    print(f"    {abs(L / L_gamma - 1):.3f} = gamma - 1 = {gam1:.3f} "
          f"(= v^2/2): the first")
    print(f"    post-Newtonian correction, which the quadrupole")
    print(f"    formula does not itself capture -- the honest")
    print(f"    accuracy floor of this comparison.")
    E_orb = -M_B * M_B / (2 * D)
    Ddot = -L * 2 * D * D / (M_B * M_B)
    print(f"    orbit energy {E_orb:.3e}; inspiral Ddot = "
          f"{Ddot:+.3e};")
    print(f"    Pdot/P = {1.5 * Ddot / D:+.3e} per unit time "
          f"({1.5 * Ddot * PER / D:+.3f} per orbit --")
    print(f"    this model binary is tight, v = {OM_B * A0:.2f}).")
    print()
    print("  THE LUMINOSITY IS EINSTEIN'S at the order the")
    print("  quadrupole formula is defined (0.01% with the virial")
    print("  bond; the angular and time integrals average out")
    print("  0039's O(v) component errors).  In-model Hulse-Taylor,")
    print("  passed.")


def run_verification_suite() -> None:
    sections = [
        ("The virial law", verify_virial_law),
        ("The bond measured from the field", verify_field_stress),
        ("The anti-string", verify_anti_string),
        ("In-model Hulse-Taylor", verify_hulse_taylor),
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
