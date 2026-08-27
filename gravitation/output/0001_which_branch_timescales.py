"""
Gravitational which-branch thought experiment: the three timescales.

Setup (user's apparatus, abstracted). A body of mass M sits at distance r from
us in a coherent superposition of two branches whose centre-of-mass positions
differ by dr. We hold a gravimeter of test mass mu at distance r and ask
whether reading it tells us the branch.

Three timescales decide everything:

  t_free   -- how long the two branches stay dynamically distinct before the
              apparatus's own Keplerian motion ends the experiment
  t_ent    -- when the gravimeter's quantum phase becomes branch-distinguishable
              (Delta phi = 1). This is when which-branch information has LEAKED.
  t_read   -- when the branch-dependent acceleration produces a displacement
              above the standard quantum limit. This is when we could READ it.

The paradox ("we learn the branch without disturbing it") requires
t_read < t_ent. Everything below is a check of whether that is achievable.

Pure stdlib. Run: python3 0001_which_branch_timescales.py
"""

import math

# ---------------------------------------------------------------- constants
G    = 6.67430e-11      # m^3 kg^-1 s^-2
HBAR = 1.054571817e-34  # J s
C    = 2.99792458e8     # m/s
KB   = 1.380649e-23     # J/K

PASS = []


def check(name, got, want, rtol=1e-9):
    ok = abs(got - want) <= rtol * max(abs(want), 1e-300)
    PASS.append((name, ok, got, want))
    return ok


# ================================================================= PART 1
# The Keplerian deadline: a pure number, independent of R and M.
#
# Exit branch      -> apparatus recoils, enters a circular orbit of radius R.
# No-exit branch   -> apparatus stays at rest, falls radially inward.
#
# Radial infall from rest at R is the degenerate ellipse of semi-major axis
# R/2, so by Kepler III its full period is T_orb * (1/2)^(3/2), and infall is
# half of that.

def fall_over_orbit_kepler():
    """t_fall / T_orb from Kepler III on the degenerate ellipse."""
    return 0.5 * (0.5 ** 1.5)


def fall_over_orbit_closed_form():
    """t_fall = (pi/2) sqrt(R^3 / (2 G M)),  T_orb = 2 pi sqrt(R^3 / (G M))."""
    R, M = 1.0, 1.0  # ratio is R,M-independent; fix them to check that claim
    t_fall = (math.pi / 2.0) * math.sqrt(R ** 3 / (2.0 * G * M))
    t_orb = 2.0 * math.pi * math.sqrt(R ** 3 / (G * M))
    return t_fall / t_orb


def fall_over_orbit_numeric(R=1.0, M=1.0e6, n=2_000_000):
    """Direct quadrature of the radial infall time, as an independent check.

    t_fall = int_0^R dr / v(r),  v(r) = sqrt(2GM(1/r - 1/R)).
    Substituting r = R sin^2(u) removes the endpoint singularity exactly.
    """
    # dr = 2R sin u cos u du ; v = sqrt(2GM/R) * cos u / sin u
    # => dr/v = 2 R sin^2(u) du / sqrt(2GM/R) = 2 R^{3/2} sin^2 u du /sqrt(2GM)
    total = 0.0
    du = (math.pi / 2.0) / n
    for i in range(n):
        u = (i + 0.5) * du
        total += math.sin(u) ** 2 * du
    t_fall = 2.0 * R ** 1.5 / math.sqrt(2.0 * G * M) * total
    t_orb = 2.0 * math.pi * math.sqrt(R ** 3 / (G * M))
    return t_fall / t_orb


# ================================================================= PART 2
# The two information timescales.

def t_entangle(M, mu, r, dr):
    """Time for the gravimeter's phase to become branch-distinguishable.

    Branch-dependent interaction energy  dU = G mu M dr / r^2.
    Accumulated relative phase           dphi = dU t / hbar.
    Set dphi = 1.  (This is the Bose / Marletto-Vedral entanglement criterion.)
    """
    dU = G * mu * M * dr / r ** 2
    return HBAR / dU


def t_readout(M, mu, r, dr):
    """Time for the branch-dependent acceleration to clear the SQL.

    Differential acceleration at the gravimeter  a = 2 G M dr / r^3.
    Free-mass SQL displacement over time t       x_sql = sqrt(hbar t / mu).
    Signal displacement                          x_sig = a t^2 / 2.
    x_sig = x_sql  =>  t = (4 hbar / (mu a^2))^(1/3).
    """
    a = 2.0 * G * M * dr / r ** 3
    return (4.0 * HBAR / (mu * a ** 2)) ** (1.0 / 3.0)


def script_N(M, mu, dr):
    """t_read / t_ent in closed form -- note the absence of r."""
    return (G * M * mu ** 2 * dr / HBAR ** 2) ** (1.0 / 3.0)


# ================================================================= PART 3
# Thermal which-path leak, for the "can we shield it?" question.

def thermal_photon_rate(area, T):
    """Blackbody photon emission rate (photons/s). 1.5205e15 * A * T^3."""
    zeta3 = 1.2020569031595943
    return (2.0 * zeta3 / math.pi ** 2) * (KB * T / (HBAR * C)) ** 3 * C * area


def thermal_wavelength(T):
    """Wien peak wavelength for photon-number spectrum, ~3670 um.K / T."""
    return 3.6697e-3 / T


def thermal_decoherence_time(area, T, dr):
    """Long-wavelength-suppressed decoherence time from self-emission.

    Rate = Gamma_emit * min(1, (dr/lambda_th)^2).  The (dr/lambda)^2 factor is
    the standard Joos-Zeh suppression when the emitted photon's wavelength is
    too long to resolve the branch separation.
    """
    gamma = thermal_photon_rate(area, T)
    lam = thermal_wavelength(T)
    resolve = min(1.0, (dr / lam) ** 2)
    return float("inf") if gamma * resolve == 0 else 1.0 / (gamma * resolve)


# ================================================================= RUN
def main():
    print("=" * 74)
    print("PART 1  --  The Keplerian deadline")
    print("=" * 74)

    a = fall_over_orbit_kepler()
    b = fall_over_orbit_closed_form()
    c = fall_over_orbit_numeric()
    exact = 1.0 / (4.0 * math.sqrt(2.0))

    print(f"  Kepler III (degenerate ellipse) : {a:.12f}")
    print(f"  closed form  (pi/2)sqrt(R^3/2GM): {b:.12f}")
    print(f"  direct quadrature (2e6 panels)  : {c:.12f}")
    print(f"  exact 1/(4 sqrt 2)              : {exact:.12f}")
    check("kepler route", a, exact)
    check("closed form route", b, exact)
    check("quadrature route", c, exact, rtol=1e-11)
    print()
    print("  => the no-exit branch reaches us at t = T_orb / (4 sqrt 2)")
    print(f"     = {exact:.4f} T_orb, INDEPENDENT of R and of both masses.")
    print("     Waiting 'one orbital period' as specified is already 5.7x too")
    print("     long: that branch has collided before the first orbit closes.")
    print()

    print("=" * 74)
    print("PART 2  --  Leak time vs readout time")
    print("=" * 74)
    print()
    hdr = f"{'case':<26}{'t_ent (s)':>13}{'t_read (s)':>13}{'N=ratio':>13}"
    print(hdr)
    print("-" * len(hdr))

    cases = [
        # label,                     M(kg),    mu(kg),  r(m),  dr(m)
        ("macroscopic apparatus",    1.0,      1.0,     1.0,   1e-3),
        ("  same, detector 10x far", 1.0,      1.0,     10.0,  1e-3),
        ("  same, detector 1000x",   1.0,      1.0,     1e3,   1e-3),
        ("nanoparticle 1e-17 kg",    1e-17,    1e-6,    1e-3,  1e-7),
        ("C60 double slit",          1.2e-24,  1e-3,    1e-3,  1e-7),
        ("electron double slit",     9.11e-31, 1e-3,    1e-3,  1e-6),
    ]
    for label, M, mu, r, dr in cases:
        te = t_entangle(M, mu, r, dr)
        tr = t_readout(M, mu, r, dr)
        print(f"{label:<26}{te:>13.3e}{tr:>13.3e}{tr / te:>13.3e}")
        check(f"N closed form [{label.strip()}]", tr / te, script_N(M, mu, dr),
              rtol=1e-9)

    print()
    print("  Rows 1-3: r varies over 3 decades, N does not move at all.")
    print("  Closed form:  N = (G M mu^2 dr / hbar^2)^(1/3)  -- no r in it.")
    print("  t_ent ~ r^2 and t_read ~ r^2 identically, so backing the detector")
    print("  away buys exactly nothing. There is no 'far enough' escape.")
    print()
    print("  N > 1 in every row => the gravimeter's phase is already")
    print("  branch-distinguishable long before its needle is. The which-branch")
    print("  information has left the system before it is readable.")
    print()

    print("=" * 74)
    print("PART 3  --  What the paradox would require: N < 1")
    print("=" * 74)
    print()
    print("  N < 1  <=>  G M mu^2 dr < hbar^2")
    print(f"         <=>  M mu^2 dr < hbar^2/G = {HBAR ** 2 / G:.3e} kg^3 m")
    print()
    for dr in (1.0, 1e-3, 1e-6):
        m_eq = (HBAR ** 2 / (G * dr)) ** (1.0 / 3.0)  # M = mu case
        print(f"    dr = {dr:>7.0e} m  ->  M = mu must be below {m_eq:.3e} kg")
    print()
    print("  Notably this is NOT an absurd bound -- ~1e-19 kg is a real")
    print("  nanoparticle, within reach of levitated-optomechanics work.")
    print("  The coherence condition is satisfiable. The readout is not:")
    M = mu = 1e-19
    r, dr = 1e-3, 1e-6
    acc = 2.0 * G * M * dr / r ** 3
    tr = t_readout(M, mu, r, dr)
    print(f"    M = mu = 1e-19 kg, r = 1 mm, dr = 1 um")
    print(f"    differential acceleration a = {acc:.3e} m/s^2")
    print(f"    t_read (SQL)               = {tr:.3e} s"
          f"  = {tr / 3.156e7:.2e} yr")
    print()
    print("  The two failure modes are complementary and leave no window:")
    print("    heavy  -> readable in principle, but decohered first (N >> 1)")
    print("    light  -> coherent, but readout takes ~1e5 yr at the SQL")
    print()
    print("  -- and this is exactly why the double slit is safe. The user's")
    print("     objection to 'gravity is an information channel' was that we")
    print("     could then always locate the particle gravitationally. We")
    print("     cannot; compare against a ~1 ms interferometer transit:")
    for label, M, mu, r, dr in cases[-2:]:
        te, tr = t_entangle(M, mu, r, dr), t_readout(M, mu, r, dr)
        print(f"       {label:<22} t_ent/1ms = {te / 1e-3:>9.2e}"
              f"   t_read/1ms = {tr / 1e-3:>9.2e}")
    print("     Both >> 1: neither leak nor readout has time to act. Gravity")
    print("     is a channel, but a channel with a ~1e-7 s^-1 capacity here.")
    print()

    print("=" * 74)
    print("PART 4  --  Can we shield the secondary leak? (self-emission)")
    print("=" * 74)
    print()
    area, dr = 0.1, 1e-3  # 0.1 m^2 apparatus, 1 mm branch separation
    hdr2 = f"{'T (K)':>10}{'photons/s':>14}{'lambda_th (m)':>15}{'t_dec (s)':>14}"
    print(hdr2)
    print("-" * len(hdr2))
    for T in (300.0, 2.725, 1.0, 1e-3, 1e-6):
        print(f"{T:>10.3e}{thermal_photon_rate(area, T):>14.3e}"
              f"{thermal_wavelength(T):>15.3e}"
              f"{thermal_decoherence_time(area, T, dr):>14.3e}")
    print()
    print("  Cooling does buy real time -- self-emission is NOT the binding")
    print("  constraint at mK and below (t_dec there exceeds t_read).")
    print("  So the thought experiment cannot be dismissed as 'the apparatus")
    print("  is warm'. The binding constraint is the gravitational coupling")
    print("  itself (Part 2), which no amount of cooling removes.")
    print()

    print("=" * 74)
    print("SELF-CHECKS")
    print("=" * 74)
    bad = [p for p in PASS if not p[1]]
    for name, ok, got, want in PASS:
        print(f"  [{'ok' if ok else 'FAIL'}] {name:<44} {got:.10e}")
    print()
    print(f"  {len(PASS) - len(bad)}/{len(PASS)} checks passed.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
