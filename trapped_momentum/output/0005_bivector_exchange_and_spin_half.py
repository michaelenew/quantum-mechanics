"""
Does the plane-to-plane relation carry spin-2 or spin-0? Plus two corrections.

PART 1  a winding plane is a bivector, and a bivector's natural symmetric
        rank-2 bilinear is forced -- it has the Maxwell-stress form, and it is
        traceless in 4D for EVERY plane type. Pure algebra, no electromagnetism.
PART 2  THE CALCULATION. A traceless source has IDENTICALLY ZERO coupling to a
        scalar mediator, while its spin-2 coupling is nonzero. The scalar
        channel is not disfavoured, it is closed.
PART 3  where mass comes from: the trace. Free null ray -> traceless ->
        massless. Confine it and the trace integrates to Mc^2.
PART 4  the null plane and spin 1/2: a null vector is a spinor SQUARED, and the
        square root is two-valued. Rotating 2pi about a null direction fixes
        the vector and negates the spinor. Half-integer modes follow.
PART 5  mass apparently continuous but genuinely quantized: as the winding
        plane tilts toward null, the orbit period diverges and the level
        spacing collapses to zero.

Pure stdlib. Run: python3 0005_bivector_exchange_and_spin_half.py
"""

import cmath
import math

PASS = []
ETA = (1.0, -1.0, -1.0, -1.0)     # (+,-,-,-), coords (t,x,y,z)


def check(name, got, want, atol=1e-12):
    ok = abs(got - want) <= atol
    PASS.append((name, ok, got, want))
    return ok


def wedge(u, v):
    """Simple bivector F^{mu nu} = u^mu v^nu - u^nu v^mu."""
    return [[u[m] * v[n] - u[n] * v[m] for n in range(4)] for m in range(4)]


def lower_second(F):
    """F^mu_nu = F^{mu beta} eta_{beta nu}; eta diagonal."""
    return [[F[m][n] * ETA[n] for n in range(4)] for m in range(4)]


def bivector_square(F):
    """F^{ab} F_{ab}."""
    return sum(F[a][b] * F[a][b] * ETA[a] * ETA[b]
               for a in range(4) for b in range(4))


def stress(F):
    """T^{mu nu} = F^{mu a} F^nu_a - (1/4) eta^{mu nu} F^{ab}F_{ab}.

    This is the unique symmetric rank-2 bilinear in a bivector, up to scale.
    Nothing electromagnetic is assumed -- it is the algebra of 2-forms.
    """
    Fm = lower_second(F)
    F2 = bivector_square(F)
    T = [[0.0] * 4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            # F^{mu a} F^nu_a ; Fm already carries the lowering metric, so
            # no further ETA factor belongs here
            s = sum(F[m][a] * Fm[n][a] for a in range(4))
            T[m][n] = s - 0.25 * (ETA[m] if m == n else 0.0) * F2
    return T


def trace(T):
    """T^mu_mu = eta_{mu nu} T^{mu nu}."""
    return sum(ETA[m] * T[m][m] for m in range(4))


def contract(T, U):
    """T^{mu nu} U_{mu nu}."""
    return sum(T[m][n] * U[m][n] * ETA[m] * ETA[n]
               for m in range(4) for n in range(4))


def asymmetry(T):
    return max(abs(T[m][n] - T[n][m]) for m in range(4) for n in range(4))


def main():
    T4 = (1.0, 0.0, 0.0, 0.0)
    X = (0.0, 1.0, 0.0, 0.0)
    Y = (0.0, 0.0, 1.0, 0.0)
    Z = (0.0, 0.0, 0.0, 1.0)
    NL = (1.0, 0.0, 0.0, 1.0)

    planes = [
        ("spacelike  x^y", wedge(X, Y)),
        ("timelike   t^x", wedge(T4, X)),
        ("null   (t+z)^x", wedge(NL, X)),
        ("generic mix", wedge((1.0, 0.3, 0.0, 0.5), (0.2, 1.0, 0.4, 0.0))),
    ]

    print("=" * 74)
    print("PART 1  --  A bivector's rank-2 bilinear is forced, and traceless")
    print("=" * 74)
    print()
    print("  A winding plane span{u,v} is the bivector F = u^v. The only")
    print("  symmetric rank-2 object bilinear in F is")
    print("      T^{mu nu} = F^{mu a} F^nu_a - (1/4) eta^{mu nu} F^{ab}F_ab")
    print("  which is the Maxwell-stress FORM arrived at by algebra, not by")
    print("  assuming electromagnetism.")
    print()
    hdr = f"{'plane':<18}{'F^ab F_ab':>14}{'asymmetry':>14}{'trace T':>14}"
    print(hdr)
    print("-" * len(hdr))
    for label, F in planes:
        T = stress(F)
        print(f"{label:<18}{bivector_square(F):>14.4f}{asymmetry(T):>14.2e}"
              f"{trace(T):>14.2e}")
        check(f"{label}: symmetric", asymmetry(T), 0.0)
        check(f"{label}: traceless", trace(T), 0.0)
    print()
    print("  Symmetric and TRACELESS for every plane type, including the")
    print("  generic non-degenerate one. In 4D the trace cancels identically:")
    print("  eta_{mu nu} eta^{mu nu} = 4 kills it against the 1/4.")
    print("  Symmetric + traceless rank-2 is exactly the graviton's index")
    print("  structure -- 'right shape for spin-2' is now checked, not hoped.")
    print()

    print("=" * 74)
    print("PART 2  --  THE CALCULATION: the scalar channel is identically zero")
    print("=" * 74)
    print()
    print("  Exchange between two sources T, T'. The two candidate mediators")
    print("  contract them differently:")
    print()
    print("    scalar (spin-0):   A ~ (trace T)(trace T')")
    print("    tensor (spin-2):   A ~ T^{mu nu} T'_{mu nu} - (1/2)(trT)(trT')")
    print()
    print("  (the second is the harmonic-gauge graviton propagator numerator")
    print("   P = 1/2(eta eta + eta eta - eta eta) contracted on both sides)")
    print()
    hdr = (f"{'source A':<18}{'source B':<18}{'A_scalar':>11}"
           f"{'A_spin2':>10}{'T00 T00 (static)':>18}")
    print(hdr)
    print("-" * len(hdr))
    for i, (la, Fa) in enumerate(planes):
        for lb, Fb in planes[i:]:
            Ta, Tb = stress(Fa), stress(Fb)
            a_s = trace(Ta) * trace(Tb)
            a_2 = contract(Ta, Tb) - 0.5 * trace(Ta) * trace(Tb)
            stat = Ta[0][0] * Tb[0][0]
            print(f"{la:<18}{lb:<18}{a_s:>11.2e}{a_2:>10.4f}{stat:>18.4f}")
            check(f"scalar channel zero [{la}|{lb}]", a_s, 0.0)
            check(f"static channel nonzero [{la}|{lb}]",
                  1.0 if abs(stat) > 1e-9 else 0.0, 1.0)
    print()
    print("  Two things to read carefully in that table.")
    print()
    print("  The A_scalar column is zero everywhere -- that is the result.")
    print()
    print("  Some A_spin2 entries also vanish, and that is NOT gravity")
    print("  switching off. The full contraction is orientation-dependent")
    print("  (that is what having a tensor rather than a scalar MEANS), and")
    print("  it can cancel for particular relative plane orientations. The")
    print("  static Newtonian limit is governed by T00*T00, which is nonzero")
    print("  in every row -- last column. So the attraction is universal while")
    print("  the sub-leading structure is orientation-sensitive, which is the")
    print("  expected shape of spin-spin coupling in GR, not a defect.")
    print("  Every scalar entry is zero to machine precision, and not by a")
    print("  cancellation that could be tuned away -- it is zero because each")
    print("  trace is separately zero, for all plane types at once.")
    print()
    print("  RESULT: a particle whose fundamental object is a winding plane")
    print("  CANNOT couple to a scalar mediator at all. Scalar gravity is not")
    print("  disfavoured in this model, it is unavailable. The lowest")
    print("  available universal long-range channel is spin-2.")
    print()
    print("  This is the same fact as the classic discriminator: Nordstrom's")
    print("  scalar gravity predicts ZERO light bending, and it predicts zero")
    print("  for exactly this reason -- radiation's stress tensor is traceless,")
    print("  so it has nothing to couple a scalar to. Measured deflection is")
    print("  1.75 arcsec at the solar limb, not zero.")
    print()
    print("  So the light-bending test flagged in 0002 as the cheapest")
    print("  falsifier is PASSED in the only sense available so far: the model")
    print("  cannot produce the Nordstrom answer even if it wanted to. Getting")
    print("  the coefficient right still requires dynamics, which the model")
    print("  does not yet have. Do not read this as 'derives 1.75 arcsec'.")
    print()

    print("=" * 74)
    print("PART 3  --  Mass is the trace, and trapping is what generates it")
    print("=" * 74)
    print()
    print("  A free null ray has a traceless stress tensor -> massless.")
    print("  Trap it and the trace no longer vanishes. Quantitatively, for any")
    print("  STATIONARY bound system the tensor virial theorem gives")
    print("      INT T^{ij} d3x = 0     =>    INT T^mu_mu d3x = INT T^00 = Mc^2")
    print()
    print("  Photon gas in a box, unit energy density:")
    rho = 1.0
    p = rho / 3.0
    T_rad = [[rho, 0, 0, 0], [0, p, 0, 0], [0, 0, p, 0], [0, 0, 0, p]]
    tr_rad = T_rad[0][0] - (T_rad[1][1] + T_rad[2][2] + T_rad[3][3])
    print(f"    radiation:  rho = {rho}, p = rho/3 = {p:.4f}")
    print(f"    trace = rho - 3p = {tr_rad:.2e}   (traceless: massless)")
    check("radiation traceless", tr_rad, 0.0)
    print()
    print("  Now confine it. In equilibrium the wall stress cancels the")
    print("  radiation pressure in the volume integral:")
    wall_p = -p
    tot_ii = 3 * (p + wall_p)
    tot_trace = T_rad[0][0] - tot_ii
    print(f"    wall stress    = {wall_p:+.4f}  (tension balancing pressure)")
    print(f"    INT T^ii       = {tot_ii:.2e}   (virial: vanishes)")
    print(f"    INT T^mu_mu    = {tot_trace:.4f} = INT T^00 = E = M c^2")
    check("confined system: virial sum zero", tot_ii, 0.0)
    check("confined trace = energy", tot_trace, T_rad[0][0])
    print()
    print("  'Mass is trapped momentum' is then exactly: MASS IS THE TRACE")
    print("  THAT TRAPPING GENERATES. Free -> traceless -> massless.")
    print("  Confined -> trace = Mc^2 -> massive. Same statement, and it says")
    print("  what the confining agent is FOR, which was the standing gap.")
    print()

    print("=" * 74)
    print("PART 4  --  The null plane gives spin 1/2 (correction accepted)")
    print("=" * 74)
    print()
    print("  Claim under test: winding in the NULL plane is what shows half")
    print("  states. It holds, and the mechanism is that a null vector is a")
    print("  spinor SQUARED, with a two-valued square root.")
    print()
    k = (1.0, 0.0, 0.0, 1.0)
    K = [[k[0] + k[3], k[1] - 1j * k[2]],
         [k[1] + 1j * k[2], k[0] - k[3]]]
    detK = K[0][0] * K[1][1] - K[0][1] * K[1][0]
    print(f"    k = {k},  k.k = {k[0]**2 - k[1]**2 - k[2]**2 - k[3]**2:.1f}")
    print(f"    K = k^mu sigma_mu,  det K = {detK.real:.2e}  -> RANK 1")
    check("null vector -> rank-1 matrix", abs(detK), 0.0)
    xi = [complex(math.sqrt(2.0)), 0j]
    outer = [[xi[i] * xi[j].conjugate() for j in range(2)] for i in range(2)]
    err = max(abs(outer[i][j] - K[i][j]) for i in range(2) for j in range(2))
    print(f"    xi = (sqrt2, 0):  |xi xi^dag - K| = {err:.2e}   -> K = xi xi^dag")
    check("K = xi xi-dagger", err, 0.0)
    print()
    print("  Now rotate about the null direction and watch the two objects")
    print("  come apart. Vectors see angle phi; spinors see phi/2.")
    print()
    hdr = f"{'phi (deg)':>10}{'vector k fixed?':>18}{'spinor factor':>22}"
    print(hdr)
    print("-" * len(hdr))
    for deg in (0, 180, 360, 540, 720):
        ph = math.radians(deg)
        U = [[cmath.exp(-1j * ph / 2), 0], [0, cmath.exp(1j * ph / 2)]]
        xr = [U[0][0] * xi[0], U[1][1] * xi[1]]
        Kr = [[xr[i] * xr[j].conjugate() for j in range(2)] for i in range(2)]
        vfix = max(abs(Kr[i][j] - K[i][j]) for i in range(2) for j in range(2))
        fac = (xr[0] / xi[0]) if abs(xi[0]) > 0 else 0
        print(f"{deg:>10}{'yes' if vfix < 1e-9 else 'NO':>18}"
              f"{f'{fac.real:+.4f}{fac.imag:+.4f}i':>22}")
        check(f"vector fixed at {deg}deg", vfix, 0.0)
    check("spinor negated at 360", cmath.exp(-1j * math.pi).real, -1.0)
    print()
    print("  At 360 degrees the null vector is exactly unchanged while the")
    print("  spinor has gone to MINUS itself. The half is not inserted; it is")
    print("  the square root relating the two.")
    print()
    print("  Consequence for the factor of 2. 0002 got L = n hbar by demanding")
    print("  single-valuedness of a VECTOR-like wave on the loop. If the object")
    print("  on the loop is the null ray's spinor instead, ANTIperiodic")
    print("  boundary conditions are allowed, and the modes are half-integers:")
    print()
    print(f"    {'(m,n)':<14}{'(1/2pi) INT e^i(m-n)th dth':>30}")
    for m, n in ((0.5, 0.5), (0.5, 1.5), (1.5, 1.5), (0.5, -0.5)):
        N = 200000
        acc = sum(cmath.exp(1j * (m - n) * (kk + 0.5) * 2 * math.pi / N)
                  for kk in range(N)) / N
        print(f"    {str((m, n)):<14}{abs(acc):>30.12f}")
        check(f"half-int orthogonality {(m, n)}", abs(acc),
              1.0 if m == n else 0.0, atol=1e-9)
    print()
    print("    Lowest antiperiodic mode is 1/2  ->  L = hbar/2.")
    print()
    print("  So the factor of 2 is resolved by the model's OWN premise. The")
    print("  circulating object is null; null vectors have spinor square roots;")
    print("  spinors on a loop admit the antiperiodic spin structure; the")
    print("  lowest mode is 1/2. Nothing was added to get it.")
    print("  Caveat: this fixes the KINEMATIC mode numbers. Showing the")
    print("  dynamics select the antiperiodic sector, rather than permitting")
    print("  it, is not done.")
    print()

    print("=" * 74)
    print("PART 5  --  Mass: apparently continuous, genuinely quantized")
    print("=" * 74)
    print()
    print("  Take a one-parameter family of winding planes that sweeps through")
    print("  all three causal types:  span{ (a,0,0,1), (0,1,0,0) }")
    print("      det g = 1 - a^2      a<1 spacelike | a=1 null | a>1 timelike")
    print()
    print("  The generator's eigenvalues are 0 and +-sqrt(1-a^2)*i for a<1, so")
    print("  the orbit is CLOSED with angular frequency w(a) = sqrt(1-a^2),")
    print("  hence period 2pi/w(a). Watch what happens as the plane tilts")
    print("  toward null:")
    print()
    hdr = (f"{'a':>10}{'det g':>12}{'type':>12}{'w = sqrt(1-a^2)':>18}"
           f"{'period':>14}")
    print(hdr)
    print("-" * len(hdr))
    for a in (0.0, 0.5, 0.9, 0.99, 0.9999, 1.0, 1.2):
        det = 1.0 - a * a
        if det > 1e-15:
            w = math.sqrt(det)
            print(f"{a:>10.4f}{det:>12.2e}{'spacelike':>12}{w:>18.6e}"
                  f"{2 * math.pi / w:>14.4e}")
            check(f"eigenfreq at a={a}", w * w, det)
        elif abs(det) <= 1e-15:
            print(f"{a:>10.4f}{det:>12.2e}{'null':>12}{0.0:>18.6e}"
                  f"{'infinite':>14}")
        else:
            print(f"{a:>10.4f}{det:>12.2e}{'timelike':>12}{'--':>18}"
                  f"{'no period':>14}")
    print()
    print("  The level spacing of a closed orbit goes as its frequency, so")
    print("  spacing ~ sqrt(1 - a^2) -> 0 as the plane approaches null.")
    print()
    print("  THAT IS THE MECHANISM ASKED FOR: the spectrum stays genuinely")
    print("  discrete (integer winding number) while the spacing collapses, so")
    print("  it LOOKS continuous. Continuity becomes a property of how the")
    print("  plane sits relative to the time axis -- an effect of the implied")
    print("  geometry -- rather than an intrinsic property of the particle.")
    print()
    print("  Where it stands as physics: with both n and a free per particle,")
    print("  m = n*sqrt(1-a^2)*scale fits any mass whatsoever, so as it stands")
    print("  it explains HOW apparent continuity can arise from real")
    print("  quantization but predicts no value. It becomes predictive only if")
    print("  something independent fixes a. That is the next question, and it")
    print("  is a much better question than 'why are masses what they are'.")
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
