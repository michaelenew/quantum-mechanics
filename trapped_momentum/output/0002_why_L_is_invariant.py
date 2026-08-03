"""
Why the trapped angular momentum does not fall under a boost.

The objection: the procession angle per wavelength must be the same after a
boost, so a longer wavelength means both slower procession and lower linear
momentum, hence less angular momentum.

Every step of that has a correct kernel. The conclusion is still blocked,
for a reason that turns out to BE the "mass is trapped momentum" claim:

  PART 1  the boost adds LONGITUDINAL momentum and leaves TRANSVERSE alone
  PART 2  the quantization condition constrains the transverse wavelength,
          which is exactly the invariant one -- so "n wavelengths per turn"
          survives the boost intact
  PART 3  L = I*Omega with I -> gamma*I and Omega -> Omega/gamma. Procession
          really does slow; the moment of inertia rises to match, exactly.
  PART 4  J^{xy} is untouched by a z-boost, as raw linear algebra
  PART 5  the payoff: E^2 = (mc^2)^2 + (pc)^2 is Pythagoras on the null ray's
          momentum, and m*c IS the transverse momentum. So "L is invariant"
          and "rest mass is invariant" are the same statement.

Pure stdlib. Run: python3 0002_why_L_is_invariant.py
"""

import math

H    = 6.62607015e-34
HBAR = H / (2.0 * math.pi)
C    = 2.99792458e8
M_E  = 9.1093837015e-31

PASS = []


def check(name, got, want, rtol=1e-12):
    ok = abs(got - want) <= rtol * max(abs(want), 1e-300)
    PASS.append((name, ok, got, want))
    return ok


def gamma(b):
    return 1.0 / math.sqrt(1.0 - b * b)


# ================================================================= PART 1
# Rest frame: null ray circulating in the xy-plane, spin along z.
# Photon 4-momentum k^mu = (E/c, p_x, p_y, 0), |p_perp| = E/c.
# Boost along z (the spin axis). Transverse components do not transform.

def boost_z(p4, b):
    """Lorentz-boost a 4-vector (E/c, px, py, pz) along z by beta = b."""
    g = gamma(b)
    e, px, py, pz = p4
    return (g * (e - b * pz), px, py, g * (pz - b * e))


# ================================================================= PART 4
# The angular momentum tensor J^{mu nu} under a z-boost, done as matrices.

def lorentz_z(b):
    g = gamma(b)
    return [[g, 0.0, 0.0, -g * b],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [-g * b, 0.0, 0.0, g]]


def transform_tensor(J, L):
    """J'^{mu nu} = L^mu_a L^nu_b J^{ab}."""
    out = [[0.0] * 4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            s = 0.0
            for a in range(4):
                for bb in range(4):
                    s += L[m][a] * L[n][bb] * J[a][bb]
            out[m][n] = s
    return out


def main():
    print("=" * 74)
    print("PART 1  --  A boost along the spin axis adds p_parallel only")
    print("=" * 74)
    print()
    print("  Rest frame: the circulating ray has p_perp = m c (all transverse),")
    print("  p_z = 0. Boost along z. Transverse components are untouched by a")
    print("  z-boost -- that is just what the Lorentz matrix does.")
    print()
    p_perp0 = M_E * C
    hdr = (f"{'v/c':>7}{'p_perp':>15}{'p_par':>15}"
           f"{'|p|':>15}{'gamma*m*c':>15}")
    print(hdr)
    print("-" * len(hdr))
    for b in (0.0, 0.1, 0.5, 0.9, 0.99):
        # rest-frame photon momentum: purely transverse, magnitude m c
        p4 = (p_perp0, p_perp0, 0.0, 0.0)   # E/c = |p| = m c
        e, px, py, pz = boost_z(p4, b)
        pmag = math.sqrt(px * px + py * py + pz * pz)
        print(f"{b:>7.2f}{abs(px):>15.6e}{abs(pz):>15.6e}"
              f"{pmag:>15.6e}{gamma(b) * M_E * C:>15.6e}")
        check(f"p_perp invariant at b={b}", abs(px), p_perp0)
        check(f"|p| = gamma m c at b={b}", pmag, gamma(b) * M_E * C)
    print()
    print("  p_perp is FLAT across the whole column. The boost pours momentum")
    print("  into p_parallel and takes none out of p_perp.")
    print()
    print("  So the total wavelength h/|p| gets SHORTER by gamma, not longer.")
    print("  The objection's 'longer wavelength' has the sign backwards: the")
    print("  ray's total energy rises to gamma*E0, as it must, since that is")
    print("  the particle's total energy.")
    print()

    print("=" * 74)
    print("PART 2  --  The quantization condition survives, untouched")
    print("=" * 74)
    print()
    print("  'n wavelengths fit around the loop' is a topological integer and")
    print("  cannot change continuously under a boost. It constrains the")
    print("  TRANSVERSE wavelength: n * lambda_perp = 2 pi r.")
    print()
    print("  And r is a transverse length, so a z-boost leaves it alone too.")
    print("  Both sides of the condition are invariant. Nothing to reconcile.")
    print()
    hdr = f"{'v/c':>7}{'lambda_perp':>16}{'2 pi r / n':>16}{'L = r p_perp':>16}"
    print(hdr)
    print("-" * len(hdr))
    n = 1
    r = n * HBAR / (M_E * C)          # from n*lambda_perp = 2 pi r, p_perp = mc
    for b in (0.0, 0.1, 0.5, 0.9, 0.99):
        p4 = (p_perp0, p_perp0, 0.0, 0.0)
        _, px, _, _ = boost_z(p4, b)
        lam_perp = H / abs(px)
        print(f"{b:>7.2f}{lam_perp:>16.8e}{2 * math.pi * r / n:>16.8e}"
              f"{r * abs(px):>16.8e}")
        check(f"n lambda_perp = 2 pi r at b={b}", lam_perp, 2 * math.pi * r / n)
        check(f"L = n hbar at b={b}", r * abs(px), n * HBAR)
    print()
    print("  L = r * p_perp = n * hbar at every speed.")
    print("  The wavelength that the quantization condition pins is precisely")
    print("  the wavelength the boost cannot touch. That is the whole answer.")
    print()

    print("=" * 74)
    print("PART 3  --  Procession DOES slow. The moment of inertia rises.")
    print("=" * 74)
    print()
    print("  This is the part of the objection that is simply correct, and it")
    print("  still does not reduce L, because L = I*Omega is not a fixed-I")
    print("  relation here. Transverse inertia is gamma*m, so I = gamma*m*r^2.")
    print()
    hdr = (f"{'v/c':>7}{'Omega':>15}{'I = g m r^2':>15}"
           f"{'L = I Omega':>16}{'m c r':>15}")
    print(hdr)
    print("-" * len(hdr))
    Omega0 = C / r
    for b in (0.0, 0.1, 0.5, 0.9, 0.99):
        g = gamma(b)
        Om = Omega0 / g               # verified in 0001 from the helix
        I = g * M_E * r * r
        print(f"{b:>7.2f}{Om:>15.6e}{I:>15.6e}{I * Om:>16.8e}"
              f"{M_E * C * r:>15.6e}")
        check(f"L = I Omega = m c r at b={b}", I * Om, M_E * C * r)
    print()
    print("    L = (gamma m r^2)(c / gamma r) = m c r     -- gammas cancel")
    print()
    print("  The objection reasons as though I were fixed, so that slower")
    print("  procession must mean less L. For a rigid body that is right.")
    print("  A null ray is not a rigid body: its speed is pinned at c, so")
    print("  what the boost changes is how that speed is SHARED between")
    print("  circulating and translating -- not how much transverse momentum")
    print("  there is. Angular frequency and angular momentum decouple.")
    print()

    print("=" * 74)
    print("PART 4  --  J^{xy} is the component a z-boost cannot reach")
    print("=" * 74)
    print()
    J = [[0.0] * 4 for _ in range(4)]
    Lz = HBAR / 2.0
    J[1][2], J[2][1] = Lz, -Lz        # pure spin about z
    K = [[0.0] * 4 for _ in range(4)]
    K[0][3], K[3][0] = 1.0, -1.0      # a boost-generator component, for contrast
    for b in (0.1, 0.5, 0.9, 0.99):
        Jp = transform_tensor(J, lorentz_z(b))
        check(f"J^xy invariant at b={b}", Jp[1][2], Lz)
        offdiag = max(abs(Jp[m][n]) for m in range(4) for n in range(4)
                      if (m, n) not in ((1, 2), (2, 1)))
        check(f"no other J component generated at b={b}", offdiag, 0.0,
              rtol=1e-30) if offdiag == 0.0 else PASS.append(
            (f"no other J component generated at b={b}", offdiag < 1e-50,
             offdiag, 0.0))
        print(f"  beta = {b:<5}  J'^xy = {Jp[1][2]:.10e}   "
              f"largest other component = {offdiag:.3e}")
    print()
    print("  J'^{mu nu} = L^mu_a L^nu_b J^{ab}, and a z-boost has")
    print("  L^x_a = delta^x_a, L^y_b = delta^y_b. So J^{xy} passes through")
    print("  untouched, identically, with nothing mixed in. Angular momentum")
    print("  about the boost axis is literally the component the boost does")
    print("  not act on.")
    print()
    print("  (The general statement is stronger: spin magnitude is the")
    print("   Pauli-Lubanski Casimir W.W = -m^2 s(s+1) hbar^2, invariant under")
    print("   the whole Poincare group. A model whose spin magnitude changed")
    print("   under boost would not be a relativistic model at all. The null")
    print("   ray is not getting lucky -- it is obeying a theorem.)")
    print()

    print("=" * 74)
    print("PART 5  --  The payoff: E^2 = (mc^2)^2 + (pc)^2 is Pythagoras")
    print("=" * 74)
    print()
    print("  Decompose the ray's momentum into transverse (trapped) and")
    print("  longitudinal (translating) parts. |p| is not fixed; p_perp is.")
    print()
    hdr = (f"{'v/c':>7}{'(p_perp c)':>16}{'(p_par c)':>16}"
           f"{'sqrt sum sq':>16}{'E = g m c^2':>16}")
    print(hdr)
    print("-" * len(hdr))
    for b in (0.0, 0.1, 0.5, 0.9, 0.99, 0.999):
        g = gamma(b)
        p4 = (p_perp0, p_perp0, 0.0, 0.0)
        _, px, _, pz = boost_z(p4, b)
        e_perp, e_par = abs(px) * C, abs(pz) * C
        tot = math.hypot(e_perp, e_par)
        print(f"{b:>7.3f}{e_perp:>16.6e}{e_par:>16.6e}"
              f"{tot:>16.6e}{g * M_E * C ** 2:>16.6e}")
        check(f"E^2 = (mc^2)^2 + (pc)^2 at b={b}", tot, g * M_E * C ** 2)
        check(f"p_par = gamma m v at b={b}", abs(pz), g * M_E * (b * C))
    print()
    print("  Read the columns: the first is CONSTANT and equals m c^2. The")
    print("  second is p c with p = gamma m v. The relativistic dispersion")
    print("  relation is the hypotenuse.")
    print()
    print("    m c  =  p_perp        mass IS the trapped transverse momentum")
    print("    p    =  p_parallel    momentum IS the untrapped part")
    print("    E^2  =  (p_perp c)^2 + (p_par c)^2")
    print()
    print("  So mass and momentum are one quantity resolved along two axes,")
    print("  which is the claim the whole reframing was built to support --")
    print("  here as an identity rather than an analogy.")
    print()
    print("  And this closes the original question. L = r * p_perp = r * m c.")
    print("  If L fell under a boost, the rest mass would fall under a boost.")
    print("  'Angular momentum is invariant' and 'rest mass is invariant' are")
    print("  not two facts. They are one fact, stated about one quantity.")
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
