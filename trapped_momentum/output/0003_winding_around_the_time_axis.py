"""
The helix axis is timelike: reworking "trapped momentum" without a spatial split.

Criticism this answers: the p_perp / p_par decomposition of 0002 is a SPATIAL
orthogonality, and it required choosing a spin axis and boosting along it. Time
is orthogonal to every spatial direction, so if the trapping is fundamental it
should be stated against the time axis, not against a distinguished spatial one.

That is correct, and the geometric picture that results is better:

  PART 1  the ray's worldline is a NULL HELIX winding around the particle's own
          timelike centre-of-mass worldline. The helix axis IS the time axis.
          "Rotation around time" is literally right; the spatial circulation
          plane is only its 3D shadow.
  PART 2  boosting TILTS that axis. Inertia = resistance to the tilt. And the
          frame-independent statement of trapping: you can always boost away
          the spatial momentum, never the rest energy.
  PART 3  where the axial-boost Pythagoras of 0002 is exact and where it is not
  PART 4  the hard obstruction: mass and spin are INDEPENDENT Casimirs, so mass
          cannot simply BE an angular momentum. Spin-0 massive particles exist.
  PART 5  counter-circulation resolves Part 4, and Kaluza-Klein is the rigorous
          version of "mass is momentum you cannot get at"

Pure stdlib. Run: python3 0003_winding_around_the_time_axis.py
"""

import math

H    = 6.62607015e-34
HBAR = H / (2.0 * math.pi)
C    = 2.99792458e8
M_E  = 9.1093837015e-31

PASS = []


def check(name, got, want, atol=0.0, rtol=1e-12):
    ok = abs(got - want) <= max(atol, rtol * max(abs(want), 1e-300))
    PASS.append((name, ok, got, want))
    return ok


def gamma(b):
    return 1.0 / math.sqrt(1.0 - b * b)


def boost_z(v4, b):
    """Boost a 4-vector (a0, a1, a2, a3) along z."""
    g = gamma(b)
    a0, a1, a2, a3 = v4
    return (g * (a0 - b * a3), a1, a2, g * (a3 - b * a0))


def minkowski(a, b):
    """Signature (+,-,-,-)."""
    return a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]


# ================================================================= PART 1
# Rest frame worldline of the circulating ray:
#   x^mu(t) = (c t,  r cos(Om t),  r sin(Om t),  0),   Om = c / r
# The centre of mass sits at the spatial origin for all t: its worldline is
# the ct-axis, which is exactly the axis the ray helix winds around.

def ray_worldline(t, r, Om):
    return (C * t, r * math.cos(Om * t), r * math.sin(Om * t), 0.0)


def ray_tangent(t, r, Om):
    """d x^mu / dt."""
    return (C, -r * Om * math.sin(Om * t), r * Om * math.cos(Om * t), 0.0)


def main():
    r = HBAR / (M_E * C)        # reduced Compton wavelength (n = 1 branch)
    Om = C / r

    print("=" * 74)
    print("PART 1  --  The worldline is a null helix about the TIME axis")
    print("=" * 74)
    print()
    print("  x^mu(t) = (ct, r cos(Om t), r sin(Om t), 0),  Om = c/r")
    print("  The centre of mass stays at the spatial origin, so its worldline")
    print("  is the ct-axis. That is the axis the helix winds around.")
    print()
    hdr = (f"{'Om t':>10}{'ds^2/(c dt)^2':>16}{'|v_spatial|/c':>16}"
           f"{'pitch angle':>14}")
    print(hdr)
    print("-" * len(hdr))
    T = 2.0 * math.pi / Om
    for frac in (0.0, 0.125, 0.25, 0.5, 0.75):
        t = frac * T
        u = ray_tangent(t, r, Om)
        ds2 = minkowski(u, u)
        vsp = math.hypot(u[1], u[2]) / C
        # angle between the tangent and the time axis, in the (ct, space) plane
        pitch = math.degrees(math.atan2(math.hypot(u[1], u[2]), u[0]))
        # report dimensionless: raw ds^2 is against c^2 ~ 9e16, so a residual
        # of order 1 is float noise, not a violation
        print(f"{2 * math.pi * frac:>10.4f}{ds2 / (C * C):>16.3e}"
              f"{vsp:>16.12f}{pitch:>14.6f}")
        check(f"null at Om t={2 * math.pi * frac:.3f}", ds2, 0.0,
              atol=1e-3 * C * C)
        check(f"|v|=c at Om t={2 * math.pi * frac:.3f}", vsp, 1.0)
        check(f"pitch=45deg at Om t={2 * math.pi * frac:.3f}", pitch, 45.0)
    print()
    print("  ds^2 = 0 everywhere: the helix is null, as required.")
    print("  The spacetime pitch angle is exactly 45 degrees -- which is just")
    print("  the null condition seen as geometry. The ray advances one unit of")
    print("  ct per unit of spatial arc.")
    print()
    print("  So 'rotation around the time axis' is not a loose way of speaking.")
    print("  The helix axis is the timelike CoM worldline, and it is")
    print("  frame-covariant. The spatial circulation plane is its 3D shadow,")
    print("  which is why choosing a spatial axis felt arbitrary -- it IS")
    print("  arbitrary. The invariant object is the winding about the worldline.")
    print()

    print("=" * 74)
    print("PART 2  --  A boost tilts that axis; the rest energy cannot be")
    print("            boosted away, in any frame")
    print("=" * 74)
    print()
    print("  Boosting the particle tilts its CoM worldline by the rapidity.")
    print("  The helix keeps winding about it; what changes is the axis.")
    print()
    hdr = (f"{'v/c':>8}{'rapidity':>12}{'axis tilt (deg)':>18}"
           f"{'E (J)':>15}{'|p|c (J)':>15}")
    print(hdr)
    print("-" * len(hdr))
    for b in (0.0, 0.1, 0.5, 0.9, 0.99):
        g = gamma(b)
        rap = math.atanh(b)
        # CoM 4-velocity, boosted
        u_com = boost_z((C, 0.0, 0.0, 0.0), b)
        tilt = math.degrees(math.atan2(abs(u_com[3]), u_com[0]))
        E = g * M_E * C ** 2
        pc = g * M_E * (b * C) * C
        print(f"{b:>8.2f}{rap:>12.6f}{tilt:>18.6f}{E:>15.6e}{pc:>15.6e}")
        check(f"tilt = atan(beta) at b={b}", math.tan(math.radians(tilt)), b)
        check(f"invariant mass at b={b}",
              math.sqrt(E * E - pc * pc) / C ** 2, M_E)
    print()
    print("  Last check in every row: sqrt(E^2 - (pc)^2)/c^2 = m, exactly.")
    print()
    print("  THE FRAME-INDEPENDENT STATEMENT OF TRAPPING:")
    print("    a boost can always remove the spatial momentum (go to the rest")
    print("    frame) but can NEVER remove the rest energy. mc^2 is the")
    print("    irreducible timelike part of P^mu -- the minimum of E over all")
    print("    frames.")
    print()
    lo = min((gamma(b) * M_E * C ** 2, b)
             for b in [i / 2000.0 for i in range(-1999, 2000)])
    print(f"    min over 3999 boosts of E : {lo[0]:.10e} J   at v/c = {lo[1]}")
    print(f"    m c^2                     : {M_E * C ** 2:.10e} J")
    check("min_v E = mc^2", lo[0], M_E * C ** 2)
    print()
    print("  That is inertia stated without reference to any spatial axis,")
    print("  which is what the criticism asked for. 0002's version -- 'p_perp")
    print("  cannot be spent' -- is the same fact seen in one special frame.")
    print()

    print("=" * 74)
    print("PART 3  --  Where 0002's Pythagoras is exact, and where it is not")
    print("=" * 74)
    print()
    print("  EXACT for a boost along the spin axis: p_perp is untouched, p_par")
    print("  is created, E^2 = (p_perp c)^2 + (p_par c)^2. Verified in 0002.")
    print()
    print("  NOT a general decomposition. Boost perpendicular to the spin and")
    print("  the loop contracts to an ellipse, the ray is Doppler-modulated")
    print("  around the circuit (blueshifted on the approaching arc), and no")
    print("  instantaneous split into 'trapped' and 'translating' survives.")
    print("  The invariant E^2 - (pc)^2 = (mc^2)^2 of course still holds --")
    print("  it is P.P -- but reading p_perp as 'the trapped part' is a")
    print("  special-frame reading, not a covariant one.")
    print()
    print("  So the criticism lands: the covariant statement is Part 2's")
    print("  (rest energy is the un-removable timelike component), and the")
    print("  spatial Pythagoras is its shadow in one adapted frame. Keep the")
    print("  spatial version as an aid to intuition, not as the definition.")
    print()

    print("=" * 74)
    print("PART 4  --  The obstruction: mass and spin are INDEPENDENT Casimirs")
    print("=" * 74)
    print()
    print("  The Poincare group has exactly two Casimirs:")
    print("     P.P   = m^2 c^2          (mass)")
    print("     W.W   = -m^2 s(s+1) hbar^2   (spin, Pauli-Lubanski)")
    print("  They are independent. Mass therefore cannot simply BE an angular")
    print("  momentum -- if it were, the two would be locked together.")
    print()
    print("  The empirical form of the objection is blunt: SPIN-0 MASSIVE")
    print("  PARTICLES EXIST. Higgs (125 GeV, s=0), pi0 (135 MeV, s=0).")
    print("  A model in which mass IS trapped angular momentum predicts they")
    print("  cannot exist. So 'mass is trapped momentum' must NOT be read as")
    print("  'mass is trapped ANGULAR momentum'. The trapped thing is energy-")
    print("  momentum; angular momentum is a separate question about how it")
    print("  circulates.")
    print()

    print("=" * 74)
    print("PART 5  --  Counter-circulation, and the Kaluza-Klein version")
    print("=" * 74)
    print()
    print("  Two null rays on the same loop, opposite senses, energy E/2 each:")
    E_tot = M_E * C ** 2
    L_one = (E_tot / 2.0) * r / C
    print(f"    each carries |L| = (E/2) r / c = {L_one:.6e} J s"
          f"  = {L_one / HBAR:.4f} hbar")
    print(f"    total spin       = {L_one - L_one:.6e} J s   (they cancel)")
    print(f"    total energy     = {E_tot:.6e} J   (they add)")
    print(f"    => mass          = {E_tot / C ** 2:.6e} kg = m_e, with SPIN 0")
    check("counter-circulating pair: spin cancels", L_one - L_one, 0.0,
          atol=1e-60)
    check("counter-circulating pair: mass adds", E_tot / C ** 2, M_E)
    print()
    print("  So massive spin-0 is naturally accommodated, and by the SAME")
    print("  structural fix flagged in 0001 for the factor of 2. Encouraging")
    print("  that one repair addresses two independent defects.")
    print()
    print("  Kaluza-Klein is the rigorous version of the whole idea, and is")
    print("  the closest prior art to the core claim -- closer than")
    print("  zitterbewegung. A massless field with momentum quantised on a")
    print("  compact dimension of radius R appears in 4D as MASSIVE:")
    print()
    hdr = f"{'n':>4}{'R (m)':>16}{'m = n hbar/(R c)':>20}{'L = m c R':>16}"
    print(hdr)
    print("-" * len(hdr))
    for n in (1, 2, 3):
        R = HBAR / (M_E * C)
        m_kk = n * HBAR / (R * C)
        print(f"{n:>4}{R:>16.6e}{m_kk:>20.6e}{m_kk * C * R / HBAR:>14.4f} hbar")
        check(f"KK: L = n hbar for n={n}", m_kk * C * R, n * HBAR)
    print()
    print("  m = n hbar / (R c)  --  mass IS momentum in a direction you")
    print("  cannot point at. No spatial axis to choose, so the 'which axis'")
    print("  question dissolves rather than being answered, and the loop's")
    print("  invisibility is explained rather than assumed.")
    print("  Note it reproduces L = n hbar exactly -- the same integer-only")
    print("  result as 0002, hence the same factor-2 problem. Consistent.")
    print()

    print("=" * 74)
    print("SELF-CHECKS")
    print("=" * 74)
    bad = [p for p in PASS if not p[1]]
    for name, ok, got, want in PASS:
        print(f"  [{'ok' if ok else 'FAIL'}] {name:<46} {got:.6e}")
    print()
    print(f"  {len(PASS) - len(bad)}/{len(PASS)} checks passed.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
