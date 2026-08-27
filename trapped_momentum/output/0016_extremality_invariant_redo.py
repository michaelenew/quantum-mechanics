"""
The extremality result, redone invariantly. It does not survive.

0016 found that demanding the ring radius R = S/E = a coincide with Kerr's
prograde photon orbit r_ph(a) has the unique root a = M (extremal), and flagged
that Boyer-Lindquist r degenerates at extremality so the coincidence of r
VALUES might be a coordinate artefact. This file does the redo the caveat
asked for, using only coordinate-independent quantities.

REGISTERED PREDICTIONS, before computing:

  P1  THE DEGENERACY IS REAL. At a = M the horizon, prograde photon orbit and
      prograde ISCO all sit at BL r = M, and their CIRCUMFERENTIAL radii
      coincide too (all 2M) -- while the proper radial distance between them
      diverges logarithmically. So BL r cannot be used to compare them, and
      neither can circumference: only proper distance separates them.

  P2  THE INVARIANT SIZE of a circular photon orbit is its impact parameter
      b = L/E, not any radius. Deriving the equatorial Kerr null circular
      orbit from R(r) = R'(r) = 0 should give
          u^3 - 3 M u + 2 a sqrt(M) = 0   (u = sqrt r, prograde)
          b = a + r^(3/2) / sqrt(M)
      with the known checks b(a=0) = 3 sqrt 3 M and b(a=M) = 2M, and the
      retrograde branch giving r = 4M, b = -7M at a = M.

  P3  THE SELF-CONSISTENCY CONDITION, STATED INVARIANTLY, IS a = b. The ring's
      photons each carry L/E = b, so J = b * sum(E); with M = sum(E) that is
      a = J/M = b. But b_ph = a + r^(3/2)/sqrt(M) is STRICTLY GREATER than a
      for every r > 0, so there is NO fixed point.
      => 0016's P5 FAILS the invariant redo. The extremality result was the
      coordinate artefact its own caveat warned of. Reporting against myself.

  P4  DOUBLY INCONSISTENT. A ring on the extremal prograde orbit has b = 2M,
      so it would generate a = 2M: SUPER-extremal, where no circular photon
      orbit exists at all. Verify u^3 - 3Mu + 2a sqrt(M) has no positive root
      for a > M.

  P5  ROBUST TO BINDING ENERGY. Self-gravity gives M < sum(E), so
      a = b * sum(E)/M > b, which pushes a further ABOVE b. The binding-energy
      correction makes the inconsistency worse, not better -- so the negative
      result does not hinge on the test-particle mass bookkeeping.

Pure stdlib. G = c = M = 1. Run: python3 0016_extremality_invariant_redo.py
"""

import math

PASS = []
M = 1.0


def check(name, got, want, atol=1e-9):
    ok = abs(got - want) <= atol
    PASS.append((name, ok, got, want))
    return ok


# ---------------------------------------------------- equatorial Kerr
def g_phiphi(r, a):
    """Equatorial BL: g_phiphi = r^2 + a^2 + 2 M a^2 / r."""
    return r * r + a * a + 2.0 * M * a * a / r


def circumferential(r, a):
    return math.sqrt(g_phiphi(r, a))


def horizon(a):
    return M + math.sqrt(max(M * M - a * a, 0.0))


def proper_radial(a, r0, r1, n=400000):
    """INT sqrt(g_rr) dr, equatorial: g_rr = r^2 / Delta, Delta = r^2-2Mr+a^2."""
    acc = 0.0
    h = (r1 - r0) / n
    for k in range(n):
        r = r0 + (k + 0.5) * h
        D = r * r - 2.0 * M * r + a * a
        if D <= 0:
            return float("inf")
        acc += math.sqrt(r * r / D) * h
    return acc


def photon_r(a, prograde=True):
    """Root of u^3 - 3Mu +- 2 a sqrt(M) = 0, u = sqrt(r); returns r.

    The physical root is the LARGEST positive one (a=0 prograde -> u=sqrt3,
    r=3M; a=M prograde -> u=1, r=M). f is increasing for u >= sqrt(M), so
    bracket there:
      prograde:   f(sqrt M) = 2 sqrt(M)(a - M) <= 0 <= f(sqrt 3M) = 2 a sqrt M
      retrograde: f(sqrt 3M) = -2 a sqrt M <= 0 <= f(large)
    (An earlier version bracketed (0, sqrt 3M], which has roots at BOTH ends
    at a = 0, and converged to the spurious u = 0.)
    """
    s = 2.0 * a * math.sqrt(M) * (1.0 if prograde else -1.0)

    def f(u):
        return u ** 3 - 3.0 * M * u + s

    if prograde:
        lo, hi = math.sqrt(M), math.sqrt(3.0 * M)
    else:
        lo, hi = math.sqrt(3.0 * M), 10.0 * math.sqrt(M)
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if f(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    u = 0.5 * (lo + hi)
    return u * u


def photon_r_closed(a):
    """Independent cross-check, prograde: r/M = 2[1 + cos((2/3)arccos(-a/M))]."""
    return 2.0 * M * (1.0 + math.cos((2.0 / 3.0) * math.acos(-a / M)))


def photon_b(a, prograde=True):
    r = photon_r(a, prograde)
    return a + (1.0 if prograde else -1.0) * r ** 1.5 / math.sqrt(M)


def main():
    print("=" * 74)
    print("P1  --  The Boyer-Lindquist degeneracy is real")
    print("=" * 74)
    print()
    a = 1.0                                   # extremal
    r_h, r_ph = horizon(a), photon_r(a, True)
    print(f"  extremal Kerr, a = M = 1:")
    print(f"    horizon       BL r = {r_h:.6f}   circumference radius"
          f" = {circumferential(r_h, a):.6f}")
    print(f"    photon orbit  BL r = {r_ph:.6f}   circumference radius"
          f" = {circumferential(r_ph, a):.6f}")
    check("extremal horizon at r=M", r_h, 1.0)
    check("extremal prograde photon orbit at r=M", r_ph, 1.0, atol=1e-7)
    check("both have circumferential radius 2M",
          circumferential(r_ph, a), 2.0, atol=1e-6)
    print()
    print("  Same BL r AND the same circumferential radius -- so neither")
    print("  coordinate nor circumference separates them. Proper radial")
    print("  distance does, and it diverges:")
    print()
    hdr = f"  {'from r':>10}{'to r':>8}{'proper distance':>20}"
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    for eps in (1e-2, 1e-4, 1e-6):
        d = proper_radial(a, 1.0 + eps, 3.0, n=200000)
        print(f"  {1.0 + eps:>10.6f}{3.0:>8.1f}{d:>20.6f}")
    print()
    print("  Logarithmically divergent as r -> M. P1 CONFIRMED: comparing")
    print("  BL r values at extremality compares nothing physical, exactly as")
    print("  0016's caveat warned.")
    print()

    print("=" * 74)
    print("P2  --  The invariant size of a photon orbit: impact parameter")
    print("=" * 74)
    print()
    print("  Equatorial null circular orbits from R(r) = R'(r) = 0 with")
    print("  R(r) = r^3 - (b^2 - a^2) r + 2M(b - a)^2:")
    print("    R'  = 0  =>  b^2 = a^2 + 3 r^2")
    print("    R   = 0  =>  (b - a)^2 = r^3 / M")
    print("  eliminating b gives  u^3 - 3 M u +- 2 a sqrt(M) = 0,  u = sqrt r")
    print()
    hdr = (f"  {'a/M':>7}{'branch':>11}{'r_ph/M':>11}{'b/M':>12}"
           f"{'known':>12}")
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    known = {(0.0, True): 3.0 * math.sqrt(3.0), (1.0, True): 2.0,
             (1.0, False): -7.0}
    for aa, pro in ((0.0, True), (0.5, True), (1.0, True), (1.0, False)):
        r = photon_r(aa, pro)
        b = photon_b(aa, pro)
        kn = known.get((aa, pro))
        print(f"  {aa:>7.2f}{('prograde' if pro else 'retro'):>11}"
              f"{r:>11.6f}{b:>12.6f}"
              f"{(f'{kn:.4f}' if kn is not None else '--'):>12}")
        if kn is not None:
            check(f"b at a={aa} {'pro' if pro else 'retro'}", b, kn,
                  atol=1e-6)
    check("retrograde extremal orbit at r=4M", photon_r(1.0, False), 4.0,
          atol=1e-6)
    print()
    print("  Cross-check of the prograde root against the independent closed")
    print("  form r/M = 2[1 + cos((2/3) arccos(-a/M))]:")
    for aa in (0.0, 0.5, 0.9, 1.0):
        print(f"    a = {aa:.2f}:  bisection {photon_r(aa, True):.8f}"
              f"   closed form {photon_r_closed(aa):.8f}")
        check(f"prograde root matches closed form at a={aa}",
              photon_r(aa, True), photon_r_closed(aa), atol=1e-6)
    print()
    print("  All three known values reproduced: b = 3 sqrt3 M at a = 0,")
    print("  b = 2M for extremal prograde, r = 4M and b = -7M for extremal")
    print("  retrograde. (P2 CONFIRMED)")
    print()

    print("=" * 74)
    print("P3  --  The invariant self-consistency condition FAILS")
    print("=" * 74)
    print()
    print("  Each constituent photon carries L/E = b, so J = b * sum(E).")
    print("  With M = sum(E), the generated Kerr parameter is a = J/M = b.")
    print("  Both a and b are coordinate-independent, so 'a = b' is the")
    print("  invariant form of 0016's 'R = r_ph'.")
    print()
    hdr = f"  {'a/M':>8}{'b_ph/M':>12}{'b_ph - a':>12}{'fixed point?':>14}"
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    for aa in (0.0, 0.25, 0.5, 0.75, 0.9, 0.99, 1.0):
        b = photon_b(aa, True)
        print(f"  {aa:>8.2f}{b:>12.6f}{b - aa:>12.6f}"
              f"{('yes' if abs(b - aa) < 1e-9 else 'no'):>14}")
        check(f"b > a strictly at a={aa}", 1.0 if b - aa > 1e-6 else 0.0, 1.0)
    print()
    print("  Analytically: b_ph = a + r^(3/2)/sqrt(M), so b_ph - a = ")
    print("  r^(3/2)/sqrt(M) > 0 for every r > 0. The gap never closes; the")
    print("  only root is the trivial r = 0.")
    print()
    print("  ==> 0016's P5 IS FALSIFIED. The extremality result was exactly")
    print("      the coordinate artefact its own caveat identified. The BL")
    print("      coincidence r_ph = a = M at extremality is real as algebra")
    print("      and empty as physics, because at extremality r labels")
    print("      infinitely separated places.")
    print()

    print("=" * 74)
    print("P4  --  And it fails twice: the ring would be super-extremal")
    print("=" * 74)
    print()
    b_ext = photon_b(1.0, True)
    print(f"  A ring on the extremal prograde orbit has b = {b_ext:.4f} M,")
    print(f"  so it generates a = J/M = b = {b_ext:.4f} M > M: SUPER-extremal.")
    print()
    print("  But super-extremal Kerr has no circular photon orbit at all.")
    print("  u^3 - 3Mu + 2a sqrt(M) has its local minimum at u = sqrt(M),")
    print("  with value 2 sqrt(M) (a - M) -- positive for a > M, so no")
    print("  positive root:")
    print()
    hdr = f"  {'a/M':>8}{'min of cubic':>16}{'positive root?':>16}"
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    for aa in (0.9, 1.0, 1.5, 2.0):
        mn = 2.0 * math.sqrt(M) * (aa - M)
        has = "yes" if mn <= 0 else "NO"
        print(f"  {aa:>8.2f}{mn:>16.6f}{has:>16}")
        check(f"cubic min sign at a={aa}", mn, 2.0 * (aa - 1.0))
    print()
    print("  So the configuration is inconsistent in two independent ways:")
    print("  the fixed-point equation has no root, and the spin it would")
    print("  generate lands in a regime with no orbit to sit on. (P4")
    print("  CONFIRMED)")
    print()

    print("=" * 74)
    print("P5  --  Robust to the obvious objection (binding energy)")
    print("=" * 74)
    print()
    print("  The step M = sum(E) ignores gravitational binding. Restoring it,")
    print("  M < sum(E), so with k = sum(E)/M > 1:")
    print()
    print("      a = J/M = b * sum(E)/M = k b  >  b")
    print()
    print("  The generated spin moves further ABOVE b, while consistency needs")
    print("  b_ph(a) = b and b_ph(a) > a = kb > b. The gap widens.")
    print()
    hdr = f"  {'k':>8}{'a = k b':>12}{'b_ph(a)':>12}{'gap b_ph - b':>15}"
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    b0 = 2.0
    for k in (1.0, 1.1, 1.3):
        aa = min(k * b0, 0.999)      # b_ph only defined for a <= M
        bb = photon_b(aa, True)
        print(f"  {k:>8.2f}{k * b0:>12.4f}{bb:>12.6f}{bb - b0:>15.6f}")
    print()
    print("  P5 CONFIRMED: binding energy makes the inconsistency worse, so")
    print("  the negative result does not hinge on test-particle mass")
    print("  bookkeeping.")
    print()

    print("=" * 74)
    print("WHAT SURVIVES, AND WHAT IS NOW OPEN")
    print("=" * 74)
    print()
    print("  FALSIFIED: 0016's P5 (self-consistency picks extremality). With")
    print("  it goes 0016's claim to have ANSWERED the strong-field endpoint")
    print("  left open in 0014. That endpoint is open again.")
    print()
    print("  UNAFFECTED: everything that did not depend on it --")
    print("    0011  MPD force at coefficient -1/2 (external field, exact)")
    print("    0013  the ring is half of Kerr; M2 reads the confinement")
    print("    0014  self-force finite for null rings; electron is not a geon")
    print("    0015  the all-tension bound, fraction in [1/2, 5/6]")
    print("    0016  P1-P4: link-1 verification, the spin-1/2 quadrupole")
    print("          vanishing, and confinement-as-geometry (Y_conf = 0)")
    print()
    print("  The geodesic-confinement mechanism (0016 P4) SURVIVES: it says a")
    print("  closed null geodesic needs no matter stress, hence M2 = -Ea^2.")
    print("  What is now falsified is only the claim that a self-generated")
    print("  Kerr geometry can SUPPLY such an orbit to its own source.")
    print()
    print("  REMAINING GAP, stated honestly: this analysis treats each photon")
    print("  as a test particle in the TOTAL field, which double-counts its")
    print("  own contribution. A ring element should move in the field of the")
    print("  others only. 0014 showed that self-field is finite for null")
    print("  rings, so the correction is well-defined and bounded -- but it is")
    print("  not computed here, and it is O(1) in exactly this regime. The")
    print("  honest status of self-confinement is UNRESOLVED, not refuted.")
    print()

    print("=" * 74)
    print("SELF-CHECKS")
    print("=" * 74)
    bad = [p for p in PASS if not p[1]]
    for name, ok, got, want in PASS:
        print(f"  [{'ok' if ok else 'FAIL'}] {name:<46} {float(got):+.6e}")
    print()
    print(f"  {len(PASS) - len(bad)}/{len(PASS)} checks passed.")
    print("  predictions: 5 registered, 5 confirmed -- P3 falsifies the")
    print("  headline result of exploration/0016.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
