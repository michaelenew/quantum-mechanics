"""
The confinement bound: which quadrupoles can a MATERIAL confinement reach?

0013 found the ladder (hoop 1/2, membrane 3/4, spokes 5/6 of Kerr) and called
Kerr "achievable but not automatic". That was too weak a statement. Reducing
the stress second moment to the transmitted radial force turns it into a
theorem with a sharp bound.

Setup. Axisymmetric static equilibrium of the WHOLE system (ring + whatever
confines it), thin in z. Define

    u(rho) = 2 pi rho S^{rho rho}(rho)   = net radial force crossing radius rho
                                           (negative = net inward pull)

Equilibrium of the total system (no external forces) gives
S^{phi phi} = d/drho (rho S^{rho rho}), i.e. u' = 2 pi S^{phi phi}, and the
stress second moment collapses to a single quadrature.

REGISTERED PREDICTIONS, before running:

  P1  IDENTITY: Y_tot = -2 INT_0^a u(rho) rho^2 drho, with no boundary term
      (u = 0 outside). Reproduces the three known architectures exactly:
      hoop 0, membrane Ea^2/2, spokes 2Ea^2/3.

  P2  THEOREM: if every stress is a TENSION (S^rr <= 0 and S^pp <= 0), then
      u is non-positive and non-increasing with u(0) = 0, so |u| <= E/a, hence
          0 <= Y_tot <= 2 E a^2 / 3    <=>    M2 fraction in [1/2, 5/6].
      KERR (fraction 1) IS UNREACHABLE BY ANY ALL-TENSION CONFINEMENT.
      The three known architectures are not a sample of a continuum -- 5/6
      (spokes) is the SUPREMUM. To be confirmed by random sampling.

  P3  WHAT KERR COSTS: reaching Y_tot = Ea^2 needs INT u rho^2 = -Ea^2/2,
      which forces |u| > E/a somewhere, which forces u' > 0 somewhere, which
      IS hoop compression. Minimum peak transmitted force = (3/2) E/a, i.e.
      50% pre-stress above the load. Approached by tension uniform in u over
      the whole disc.

  P4  ENERGY PRICE: the dominant energy condition bounds a hoop's linear
      energy density by its stress, lambda >= |C|. For the minimal Kerr
      structure this makes the confinement HEAVIER THAN THE RING IT CONFINES
      (extra energy of order pi E). Registered as an order-of-magnitude
      claim only -- it is a lower bound on a self-consistency problem this
      script does not solve.

  P5  GRAVITY EVADES IT. The bound constrains matter stresses. Gravitational
      confinement transmits force without any matter T^kk, so it is not
      bounded by P2 -- which is why 0014's f -> 1 could reach Kerr while no
      material structure in the ladder does.

Pure stdlib. G = c = E = a = 1. Run: python3 0014_confinement_bound.py
"""

import math

PASS = []
E = 1.0
A = 1.0
N = 200000


def check(name, got, want, atol=1e-6):
    ok = abs(got - want) <= atol
    PASS.append((name, ok, got, want))
    return ok


def Y_from_u(u, n=N):
    """Y_tot = -2 INT_0^a u(rho) rho^2 drho."""
    acc = 0.0
    h = A / n
    for k in range(n):
        rho = (k + 0.5) * h
        acc += u(rho) * rho * rho * h
    return -2.0 * acc


def frac(Y):
    """M2 as a fraction of Kerr: M2 = -(1/2)(Ea^2 + Y), Kerr = -Ea^2."""
    return (E * A * A + Y) / (2.0 * E * A * A)


# ---- the three known architectures, as transmitted-force profiles ----
def u_hoop(rho):
    return 0.0                      # all stress is hoop stress at rho = a


def u_spokes(rho):
    return -E / A                   # constant radial tension to the centre


def u_membrane(rho):
    return -E * rho / (A * A)       # uniform isotropic disc tension


def main():
    print("=" * 74)
    print("P1  --  The identity, checked against known architectures")
    print("=" * 74)
    print()
    hdr = (f"  {'architecture':<14}{'Y_tot (identity)':>18}"
           f"{'Y_tot (0013)':>15}{'fraction':>11}{'0013':>8}")
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    for name, u, y0, f0 in (("hoop", u_hoop, 0.0, 0.5),
                            ("membrane", u_membrane, 0.5, 0.75),
                            ("spokes", u_spokes, 2.0 / 3.0, 5.0 / 6.0)):
        Y = Y_from_u(u)
        print(f"  {name:<14}{Y:>18.10f}{y0:>15.10f}{frac(Y):>11.6f}"
              f"{f0:>8.4f}")
        check(f"P1 identity reproduces {name}", Y, y0, atol=1e-8)
        check(f"P1 fraction for {name}", frac(Y), f0, atol=1e-8)
    print()
    print("  The whole stress second moment is one quadrature of the")
    print("  transmitted radial force. The three architectures of 0013 are")
    print("  three choices of u. (P1 CONFIRMED)")
    print()

    print("=" * 74)
    print("P2  --  THE BOUND: all-tension confinement cannot reach Kerr")
    print("=" * 74)
    print()
    print("  All stresses tension  =>  u <= 0 and u' <= 0, with u(0) = 0.")
    print("  So u decreases monotonically from 0, and the ring's own force")
    print("  balance caps it: |u(a)| <= E/a. Therefore")
    print()
    print("      |INT_0^a u rho^2| <= (E/a)(a^3/3) = E a^2 / 3")
    print("      0 <= Y_tot <= 2 E a^2 / 3   <=>   fraction in [1/2, 5/6]")
    print()
    print("  Random sampling over monotone tension profiles (u built as a")
    print("  cumulative sum of random non-positive increments, rescaled so")
    print("  |u(a)| <= E/a):")
    print()
    seed = 987654321
    lo, hi = 1e9, -1e9
    argmax = None
    NS = 4000
    for trial in range(NS):
        # random non-increasing u on a coarse grid, then interpolate
        m = 40
        incs = []
        s = seed + trial * 7919
        for i in range(m):
            s = (1103515245 * s + 12345) % 2147483648
            incs.append(-(s / 2147483648.0))
        tot = sum(incs)
        scale = (E / A) / abs(tot) if tot != 0 else 0.0
        prof = [0.0]
        for inc in incs:
            prof.append(prof[-1] + inc * scale)

        def u_rand(rho, prof=prof, m=m):
            t = rho / A * m
            i = min(int(t), m - 1)
            w = t - i
            return prof[i] * (1 - w) + prof[i + 1] * w

        Y = Y_from_u(u_rand, n=4000)
        f = frac(Y)
        if f < lo:
            lo = f
        if f > hi:
            hi = f
            argmax = prof
    print(f"    {NS} random tension profiles:")
    print(f"      min fraction = {lo:.6f}   max fraction = {hi:.6f}")
    print(f"      bound        = [0.500000, 0.833333]")
    check("P2 sampled max stays under 5/6", 1.0 if hi <= 5.0 / 6.0 + 1e-9
          else 0.0, 1.0)
    check("P2 sampled min stays above 1/2", 1.0 if lo >= 0.5 - 1e-9
          else 0.0, 1.0)
    print()
    print("  Nothing violates the bound -- but note the random family only")
    print("  spans [0.72, 0.78] and never approaches either edge, so on its")
    print("  own it is weak evidence that the bound is TIGHT. The power-law")
    print("  family u = -(E/a)(rho/a)^n does sweep the whole interval, with")
    print("  fraction = (1 + 2/(n+3))/2 -- an exact closed form:")
    print()
    hdr2 = f"  {'n':>8}{'fraction (numeric)':>20}{'(1+2/(n+3))/2':>16}{'':>6}"
    print(hdr2)
    print("  " + "-" * (len(hdr2) - 2))
    for n_p, tag in ((0.0, "spokes"), (1.0, "membrane"), (3.0, ""),
                     (10.0, ""), (100.0, "-> hoop")):
        def u_pow(rho, n_p=n_p):
            return -(E / A) * (rho / A) ** n_p

        Yp = Y_from_u(u_pow)
        closed = (1.0 + 2.0 / (n_p + 3.0)) / 2.0
        print(f"  {n_p:>8.0f}{frac(Yp):>20.6f}{closed:>16.6f}   {tag}")
        check(f"P2 power-law closed form n={n_p}", frac(Yp), closed,
              atol=1e-5)
    print()
    print("  The interval is swept and both edges are attained in the limits:")
    print("  supremum 5/6 at n = 0 (spokes -- all force transmitted from the")
    print("  very centre), infimum 1/2 as n -> infinity (hoop -- nothing")
    print("  transmitted radially at all). The bound is tight at both ends.")
    print()
    print("  THEOREM (P2 CONFIRMED): no all-tension material confinement can")
    print("  produce more than 5/6 of the Kerr quadrupole. Kerr is not merely")
    print("  'not automatic' as 0013 said -- it is OUTSIDE the reachable set.")
    print()

    print("=" * 74)
    print("P3  --  What Kerr costs: hoop compression, >= 50% pre-stress")
    print("=" * 74)
    print()
    print("  Kerr needs Y_tot = Ea^2, i.e. INT_0^a u rho^2 drho = -Ea^2/2.")
    print("  Write u = -(E/a) g(rho/a); the condition is INT_0^1 g x^2 dx =")
    print("  1/2, while all-tension gives g <= 1 hence INT <= 1/3.")
    print()
    print("  Minimising the peak of g subject to the constraint: put the")
    print("  weight where x^2 is largest. For g = G on [x0, 1] and 0 below,")
    print("  G = 3 / (2(1 - x0^3)), minimised as x0 -> 0 at G = 3/2.")
    print()
    hdr = f"  {'x0':>8}{'required G':>14}{'INT g x^2':>13}{'fraction':>11}"
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    for x0 in (0.0, 0.2, 0.4, 0.6):
        Gp = 3.0 / (2.0 * (1.0 - x0 ** 3))

        def u_box(rho, x0=x0, Gp=Gp):
            return -(E / A) * Gp if rho >= x0 * A else 0.0

        Y = Y_from_u(u_box)
        integ = -Y / 2.0 / (E * A * A) * -1.0
        print(f"  {x0:>8.2f}{Gp:>14.6f}{Y / (2 * E * A * A):>13.6f}"
              f"{frac(Y):>11.6f}")
        check(f"P3 box profile reaches Kerr at x0={x0}", frac(Y), 1.0,
              atol=1e-5)
    print()
    print("  Every row reaches fraction 1.000000 exactly, and the cheapest")
    print("  needs peak |u| = 1.5 E/a: the structure must carry 50% MORE")
    print("  internal tension than the load it transmits. That excess must")
    print("  be closed by compression (u' > 0 somewhere), i.e. HOOP")
    print("  COMPRESSION. (P3 CONFIRMED)")
    print()
    print("  So the Kerr condition is not a fine-tuning of a tension profile.")
    print("  It requires a qualitatively different object: a PRE-STRESSED")
    print("  structure with compression members -- a tensegrity, not a web.")
    print()

    print("=" * 74)
    print("P4  --  The energy price, as a lower bound")
    print("=" * 74)
    print()
    print("  DEC bounds a member's energy density by its stress. For a hoop")
    print("  of radius r carrying compression C, linear density lambda >= C,")
    print("  so its energy is at least C * 2 pi r.")
    print()
    C = 0.5 * E / A          # the excess that must be closed by compression
    for r in (1.0, 0.5, 0.25):
        print(f"    compression ring at r = {r:.2f} a:"
              f"   E_min >= {C * 2 * math.pi * r:.4f} E")
    print()
    print(f"  Minimum extra energy of order {C * 2 * math.pi:.2f} E at r = a,")
    print("  falling only linearly as the compression ring is moved inward")
    print("  -- but moving it inward reduces its lever arm and the profile")
    print("  no longer reaches Kerr. Order of magnitude: the confinement is")
    print("  COMPARABLE TO OR HEAVIER THAN the ring it confines.")
    print()
    print("  P4 stands only as a lower bound, and the self-consistency it")
    print("  raises is NOT solved here: the confinement's own energy adds to")
    print("  E, shifts a = S/E, and changes the target. Registered honestly")
    print("  as an obstruction of unknown severity, not a refutation.")
    print()

    print("=" * 74)
    print("P5  --  Why gravity is not bounded by any of this")
    print("=" * 74)
    print()
    print("  The bound is a statement about MATTER stresses: u(rho) is the")
    print("  radial force carried by T^{rho rho}. Gravitational binding")
    print("  transmits force with no matter stress at all -- in 0014 the")
    print("  self-force came from the field, and the hoop tension it replaced")
    print("  scaled away as (1 - f).")
    print()
    print("  That resolves what looked like a tension between 0013 and 0014:")
    print()
    print("    0013's ladder tops out at 5/6 -- now known to be a hard")
    print("    ceiling for material confinement, not a sampling artefact.")
    print("    0014's self-gravitating case reaches exactly 1 -- possible")
    print("    precisely because it removes matter stress rather than")
    print("    rearranging it.")
    print()
    print("  Sharpened conclusion, replacing 0013's 'achievable, not")
    print("  automatic':")
    print()
    print("    KERR'S QUADRUPOLE IS A SIGNATURE OF NON-MATERIAL CONFINEMENT.")
    print()
    print("  Any all-tension material scaffold is capped at 5/6; only")
    print("  pre-stressed structures (at an energy price comparable to the")
    print("  ring itself) or field binding reach 1. Combined with 0014's")
    print("  result that gravity supplies ~1e-44 of the electron's")
    print("  confinement, the electron -- IF it sits at Kerr, which rests on")
    print("  the unverified minimal-coupling claim [K] -- is confined by")
    print("  something that is neither ordinary material tension nor gravity.")
    print()

    print("=" * 74)
    print("SELF-CHECKS")
    print("=" * 74)
    bad = [p for p in PASS if not p[1]]
    for name, ok, got, want in PASS:
        print(f"  [{'ok' if ok else 'FAIL'}] {name:<44} {float(got):+.6e}")
    print()
    print(f"  {len(PASS) - len(bad)}/{len(PASS)} checks passed.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
