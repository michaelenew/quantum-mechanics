"""
Stage 2b: does the light ring's quadrupole match Kerr's M2 = -J^2/M?

REGISTERED QUESTION (from exploration/0012, before any computation): the ring
at fixed (E, S) sits at r = S/E = Kerr's a = J/M; does its trace-free
quadrupole match Kerr's M2 = -J^2/M, and is the order-unity factor exactly 1?
Hazard registered there: fix the SSC/centroid explicitly. Here the source is
static, axisymmetric and reflection-symmetric, so the centroid is unambiguous
-- the factor below is physics, not convention.

EXPECTATIONS reasoned before running THIS script (recorded for honesty):
  E1  bare ring: M2 = -Ma^2/2 -- HALF of Kerr. The registered "exactly 1"
      hope should FAIL at the rigid-ring level.
  E2  Kerr's own weak field is the Appell potential (point mass at imaginary
      displacement ia), with the famous moment pattern M_l = M Re[(ia)^l]:
      M0 = M, M2 = -Ma^2, M4 = +Ma^4, odd = 0. Verify numerically.
  E3  the gap is carried by the STRESSES: with the Tolman effective source
      rho_eff = T^00 + T^kk, different confinement architectures give
      different M2 -- a computable ladder -- and the Kerr-matching condition
      is a clean functional of the confinement.
  E4  EXACT Kerr matching (all moments) requires the Israel disk: a NEGATIVE
      surface density interior with a positive rim ring. Derive it numerically
      from the Appell branch-cut jump; verify its mass and M2 limits.

Everything from scratch, pure stdlib. G = c = 1, M = E = 1, a = r = S/E = 1.
Run: python3 0012_stage2b_kerr_quadrupole.py
"""

import cmath
import math

PASS = []


def check(name, got, want, atol=1e-6):
    ok = abs(got - want) <= atol
    PASS.append((name, ok, got, want))
    return ok


def legendre(l, x):
    p0, p1 = 1.0, x
    if l == 0:
        return p0
    if l == 1:
        return p1
    for n in range(1, l):
        p0, p1 = p1, ((2 * n + 1) * x * p1 - n * p0) / (n + 1)
    return p1


def moments_from_potential(phi, R, lmax, nth=4000):
    """Phi(R, th) = -(1/R) sum_l M_l P_l(cos th) / R^l  =>
    M_l = -(2l+1)/2 * R^(l+1) * INT Phi P_l sin th dth."""
    out = []
    for l in range(lmax + 1):
        acc = 0.0
        dth = math.pi / nth
        for i in range(nth):
            th = (i + 0.5) * dth
            acc += phi(R, th) * legendre(l, math.cos(th)) * math.sin(th) * dth
        out.append(-(2 * l + 1) / 2.0 * R ** (l + 1) * acc)
    return out


M = 1.0
A = 1.0     # ring radius = S/E; Kerr parameter a = J/M -- same number


def phi_ring(R, th, nphi=512):
    """Newtonian potential of a unit-mass ring of radius A, field point in
    the xz-plane at (R sin th, 0, R cos th)."""
    fx, fz = R * math.sin(th), R * math.cos(th)
    acc = 0.0
    for k in range(nphi):
        p = 2.0 * math.pi * (k + 0.5) / nphi
        dx = fx - A * math.cos(p)
        dy = -A * math.sin(p)
        d = math.sqrt(dx * dx + dy * dy + fz * fz)
        acc += 1.0 / d
    return -M * acc / nphi


def phi_appell(R, th):
    """Weak-field Kerr mass potential: -M Re[1/sqrt(rho^2 + (z - ia)^2)]."""
    rho, z = R * math.sin(th), R * math.cos(th)
    return -M * (1.0 / cmath.sqrt(rho * rho + (z - 1j * A) ** 2)).real


def main():
    print("=" * 74)
    print("PART 1  --  The bare ring: M2 = -Ma^2/2  (E1)")
    print("=" * 74)
    print()
    # R close-in: moment extraction multiplies quadrature noise by R^(l+1),
    # so R = 8 turns 1e-8 noise into ~1e-3 at l = 4. R = 3 keeps it ~1e-6.
    R = 3.0
    ml = moments_from_potential(phi_ring, R, 4, nth=8000)
    direct = [M * A ** l * legendre(l, 0.0) for l in range(5)]
    hdr = f"  {'l':>3}{'from potential':>18}{'direct moment':>16}"
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    for l in range(5):
        print(f"  {l:>3}{ml[l]:>18.8f}{direct[l]:>16.8f}")
        check(f"ring M_{l}", ml[l], direct[l], atol=3e-5)
    print()
    print("  Two independent routes agree: far-field Legendre projection of")
    print("  the computed potential, and the direct moment integral")
    print("  M_l = M a^l P_l(0). The ring's quadrupole is M2 = -Ma^2/2.")
    print()

    print("=" * 74)
    print("PART 2  --  Kerr's weak field: M_l = M Re[(ia)^l]  (E2)")
    print("=" * 74)
    print()
    ml_k = moments_from_potential(phi_appell, R, 4, nth=8000)
    kerr = [M * ((1j * A) ** l).real for l in range(5)]
    hdr = f"  {'l':>3}{'Appell numeric':>18}{'M Re[(ia)^l]':>16}"
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    for l in range(5):
        print(f"  {l:>3}{ml_k[l]:>18.8f}{kerr[l]:>16.8f}")
        check(f"Kerr M_{l}", ml_k[l], kerr[l], atol=3e-5)
    print()
    print("  Confirmed: M0 = M, M2 = -Ma^2 = -J^2/M (J = Ma), M4 = +Ma^4,")
    print("  odd moments zero. The Kerr mass moments are a point mass at")
    print("  imaginary displacement ia -- verified from scratch.")
    print()
    print("  VERDICT ON THE REGISTERED QUESTION:")
    print(f"    ring M2 / Kerr M2 = {ml[2] / ml_k[2]:.6f}")
    check("factor is 1/2, not 1", ml[2] / ml_k[2], 0.5, atol=1e-4)
    print()
    print("  THE 'EXACTLY 1' HOPE FAILS. The rigid ring carries HALF the Kerr")
    print("  quadrupole. Sign correct, order-unity correct, factor = 1/2.")
    print("  Recorded as registered. The rest of this file is what the")
    print("  failure teaches.")
    print()

    print("=" * 74)
    print("PART 3  --  The stresses carry the gap: the confinement ladder (E3)")
    print("=" * 74)
    print()
    print("  Weak-field stationary mass moments are sourced by the Tolman")
    print("  effective density rho_eff = T^00 + T^kk. The photon ring itself")
    print("  has T^kk = +E at rho = a (null flow: pressure = energy density).")
    print("  Every confinement architecture adds its own stress distribution,")
    print("  constrained by equilibrium; the virial theorem forces")
    print("  INT T^kk_total = 0, so M0 = E always -- but the SECOND moment of")
    print("  stress, Y = INT T^kk_total rho^2 dA, is architecture-dependent:")
    print()
    print("      M2 = -(1/2) (E a^2 + Y)          Kerr  <=>  Y = +E a^2")
    print()
    rows = []
    # hoop: tension -E concentrated at rho = a
    Y_hoop = M * A * A + (-M * A * A)
    rows.append(("hoop at rim", Y_hoop))
    # membrane: uniform isotropic tension tau = E/(2 pi a^2), T^kk = -2 tau
    tau_m = M / (2.0 * math.pi * A * A)
    n = 200000
    acc = 0.0
    for i in range(n):
        rho = (i + 0.5) * A / n
        acc += (-2.0 * tau_m) * rho * rho * 2.0 * math.pi * rho * (A / n)
    rows.append(("spanning membrane", M * A * A + acc))
    # spokes: radial tension, total E/a crossing every radius
    acc = 0.0
    for i in range(n):
        rho = (i + 0.5) * A / n
        acc += (-M / A) * rho * rho * (A / n)
    rows.append(("radial spokes", M * A * A + acc))
    hdr = (f"  {'architecture':<20}{'Y / Ea^2':>10}{'M2 / (-Ea^2)':>14}"
           f"{'fraction of Kerr':>18}")
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    expect = {"hoop at rim": (0.0, 0.5), "spanning membrane": (0.5, 0.75),
              "radial spokes": (2.0 / 3.0, 5.0 / 6.0)}
    for name, Y in rows:
        m2 = -(0.5) * (M * A * A + Y)
        frac = m2 / (-M * A * A)
        print(f"  {name:<20}{Y / (M * A * A):>10.6f}{frac:>14.6f}"
              f"{frac:>18.6f}")
        check(f"Y for {name}", Y / (M * A * A), expect[name][0], atol=1e-4)
        check(f"M2 fraction for {name}", frac, expect[name][1], atol=1e-4)
    print()
    print("  The ladder 1/2, 3/4, 5/6 (= 1 - 1/2n for n = 1, 2, 3 -- noted,")
    print("  not explained). Kerr sits at the limit Y = +Ea^2, equivalently:")
    print()
    print("    THE CONFINEMENT'S OWN STRESS SECOND MOMENT MUST VANISH.")
    print()
    print("  The ring's null-flow pressure supplies +Ea^2 by itself; any")
    print("  tension distributed between hub and rim eats into it. Simple")
    print("  single-sign architectures cannot reach zero (tension must be")
    print("  transmitted across intermediate radii); PRE-STRESSED structures")
    print("  (self-equilibrated compression + tension, second moment of")
    print("  either sign) can. Matching Kerr is achievable, not automatic:")
    print("  it is a one-functional condition on structure the model does not")
    print("  yet fix from a principle.")
    print()

    print("=" * 74)
    print("PART 4  --  How exact Kerr does it: the Israel disk, from scratch")
    print("=" * 74)
    print()
    print("  The Appell potential's source is the branch-cut disk rho < a.")
    print("  Surface density from the jump: sigma = d(Phi)/dz|_{0+} / 2 pi.")
    print()
    hdr = (f"  {'rho/a':>8}{'sigma (numeric jump)':>22}"
           f"{'-Ma / 2pi u^3/2':>18}")
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    for frac_r in (0.3, 0.6, 0.9):
        rho = frac_r * A
        dz = 1e-6
        # d/dz of -M Re[ (rho^2+(z-ia)^2)^(-1/2) ] at z = +dz
        f1 = -M * (1.0 / cmath.sqrt(rho ** 2 + (2 * dz - 1j * A) ** 2)).real
        f0 = -M * (1.0 / cmath.sqrt(rho ** 2 + (0.0 - 1j * A) ** 2)).real
        sig = ((f1 - f0) / (2 * dz)) / (2.0 * math.pi)
        u = A * A - rho * rho
        ana = -M * A / (2.0 * math.pi * u ** 1.5)
        print(f"  {frac_r:>8.2f}{sig:>22.8f}{ana:>18.8f}")
        check(f"Israel sigma at rho={frac_r}a", sig, ana,
              atol=3e-4 * abs(ana))
    print()
    print("  sigma(rho) = -Ma / (2 pi (a^2 - rho^2)^(3/2)):  NEGATIVE")
    print("  everywhere inside, diverging toward the rim, with a positive")
    print("  rim ring carrying the balance. Check the distributional limits")
    print("  (interior integrated to rho_max = a sqrt(1 - eps), rim = rest):")
    print()
    hdr = (f"  {'eps':>10}{'interior mass':>16}{'rim mass':>12}"
           f"{'total M2':>12}")
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    last = None
    for eps in (1e-2, 1e-4, 1e-6):
        umin = A * A * eps
        m_in = -M * A * (1.0 / math.sqrt(umin) - 1.0 / A)
        m_rim = M - m_in
        # closed forms for the interior integrals (u = a^2 - rho^2 substitution)
        m2_tot = -0.5 * (-M * A * (A * A / math.sqrt(umin)
                                   + math.sqrt(umin) - 2.0 * A)) \
            - 0.5 * m_rim * A * A
        print(f"  {eps:>10.0e}{m_in:>16.4f}{m_rim:>12.4f}{m2_tot:>12.6f}")
        last = m2_tot
    check("Israel disk M2 limit", last, -M * A * A, atol=3e-3)
    print()
    print("  Interior mass -> -infinity, rim -> +infinity, their moments'")
    print("  sum -> exactly -Ma^2. Exact Kerr pays for its quadrupole with a")
    print("  NEGATIVE-energy interior sheet (Israel 1970's disk, recovered")
    print("  here from the branch cut) -- the structure Burinskii builds the")
    print("  Dirac-Kerr electron on. [attribution K: text unreachable]")
    print()

    print("=" * 74)
    print("VERDICT")
    print("=" * 74)
    print()
    print("  Registered question answered: the factor is 1/2, not 1. The")
    print("  tail-chasing ring alone is NOT Kerr at quadrupole order.")
    print()
    print("  What the failure extracted:")
    print("  - M2 is not fixed by (E, S): it reads the CONFINEMENT. The")
    print("    ladder 1/2 (hoop), 3/4 (membrane), 5/6 (spokes) measures")
    print("    architecture, and Kerr is the sharp condition Y = +Ea^2:")
    print("    the confinement's own stress second moment must vanish.")
    print("  - If minimal coupling = Kerr multipoles holds (modern amplitude")
    print("    result [K: unverified this session]), then the electron sits")
    print("    AT Kerr -- so gravity is telling us a structural fact about")
    print("    whatever confines the zitter motion: zero stress second")
    print("    moment. A concrete constraint on the unknown mechanism,")
    print("    extracted from a quadrupole.")
    print("  - Exact Kerr (all moments) requires the Israel disk's negative")
    print("    interior sheet. For an electron-scale object that is quantum-")
    print("    vacuum territory (Casimir-negative energies), not classical")
    print("    material. Registered, not resolved.")
    print()

    print("=" * 74)
    print("SELF-CHECKS")
    print("=" * 74)
    bad = [p for p in PASS if not p[1]]
    for name, ok, got, want in PASS:
        print(f"  [{'ok' if ok else 'FAIL'}] {name:<40} {float(got):+.6e}")
    print()
    print(f"  {len(PASS) - len(bad)}/{len(PASS)} checks passed.")
    print("  registered question: answered (factor 1/2; 'exactly 1' FAILS)")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
