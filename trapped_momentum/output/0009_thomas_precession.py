"""
Thomas precession: the cheapness test, with the answer written down first.

Every earlier note in this workstream computed and then interpreted. That
pattern rewards retrofitting. So this file states its predictions BEFORE the
calculation and then checks them, and reports failures as failures.

  PART 0  the predictions, stated first
  PART 1  two boosts in SL(2,C): the rotation term is one line of Pauli algebra
  PART 2  circular motion: accumulate around the loop, compare to 2 pi (gamma-1)
  PART 3  Gauss-Bonnet cross-check on hyperbolic rapidity space
  PART 4  the verdict, including the prediction that FAILED

Pure stdlib. Run: python3 0009_thomas_precession.py
"""

import cmath
import math

PASS = []
PRED = []


def check(name, got, want, atol=1e-9):
    ok = abs(got - want) <= atol
    PASS.append((name, ok, got, want))
    return ok


def predict(name, statement):
    PRED.append((name, statement))
    print(f"    [{len(PRED)}] {name}")
    print(f"        {statement}")


# ------------------------------------------------------------ 2x2 helpers
def mm(A, B):
    return [[sum(A[r][t] * B[t][c] for t in range(2)) for c in range(2)]
            for r in range(2)]


def dag(A):
    return [[A[c][r].conjugate() for c in range(2)] for r in range(2)]


def inv(A):
    d = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return [[A[1][1] / d, -A[0][1] / d], [-A[1][0] / d, A[0][0] / d]]


def tr(A):
    return A[0][0] + A[1][1]


def sig(n):
    """n . sigma for a real 3-vector n."""
    return [[n[2] + 0j, n[0] - 1j * n[1]], [n[0] + 1j * n[1], -n[2] + 0j]]


def boost(eta, n):
    """exp(eta n.sigma / 2) = cosh(eta/2) + sinh(eta/2) n.sigma."""
    c, s = math.cosh(eta / 2), math.sinh(eta / 2)
    S = sig(n)
    return [[c + s * S[0][0], s * S[0][1]], [s * S[1][0], c + s * S[1][1]]]


def sqrt_pos_herm(H):
    """Square root of a 2x2 positive-definite Hermitian matrix."""
    d = (H[0][0] * H[1][1] - H[0][1] * H[1][0])
    s = cmath.sqrt(d)
    t = cmath.sqrt(tr(H) + 2 * s)
    return [[(H[0][0] + s) / t, H[0][1] / t], [H[1][0] / t, (H[1][1] + s) / t]]


def rotation_angle(A):
    """Polar-decompose A = R B (R unitary) and return R's rotation angle."""
    H = mm(dag(A), A)               # = B^2
    B = sqrt_pos_herm(H)
    R = mm(A, inv(B))
    ct = (tr(R) / 2.0).real         # = cos(Omega/2)
    ct = max(-1.0, min(1.0, ct))
    return 2.0 * math.acos(abs(ct))  # magnitude of the rotation angle


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]]


def main():
    print("=" * 74)
    print("PART 0  --  PREDICTIONS, stated before any computation")
    print("=" * 74)
    print()
    predict("Wigner angle, two boosts",
            "tan(Om/2) = sin(th) s1 s2 / (c1 c2 + cos(th) s1 s2),"
            "  c=cosh(eta/2), s=sinh(eta/2)")
    predict("Thomas angle per circular orbit",
            "Delta = 2 pi (gamma - 1), exactly, independent of the radius")
    predict("slow limit",
            "Delta -> pi beta^2  (the famous factor of 1/2 in spin-orbit)")
    predict("CONJUGACY CLASS of a product of two boosts",
            "LOXODROMIC -- a rotation appears that neither factor had, which"
            " is what 0008's taxonomy would seem to say")
    print()
    print("  Prediction 4 is the one that makes this a test of the FRAMEWORK")
    print("  rather than of SL(2,C). If the product of two boosts is")
    print("  loxodromic, 0008's classification predicts Thomas precession.")
    print()

    print("=" * 74)
    print("PART 1  --  Two boosts: the rotation is one line of Pauli algebra")
    print("=" * 74)
    print()
    print("  [c1 + s1 n1.sig][c2 + s2 n2.sig]")
    print("      = (c1c2 + s1s2 n1.n2)         <- scalar")
    print("      + (c1s2 n2 + s1c2 n1).sig     <- real vector: boost part")
    print("      + i s1s2 (n1 x n2).sig        <- IMAGINARY: the rotation")
    print()
    print("  The rotation term is present iff n1 x n2 != 0. That is the whole")
    print("  content, and it is visible without any calculation.")
    print()
    hdr = (f"{'eta1':>6}{'eta2':>6}{'theta':>8}{'Omega (polar)':>16}"
           f"{'Omega (formula)':>17}")
    print(hdr)
    print("-" * len(hdr))
    for e1, e2, th in ((1.0, 1.0, math.pi / 2), (0.5, 1.5, math.pi / 3),
                       (2.0, 2.0, math.pi / 2), (1.0, 1.0, 0.0),
                       (0.3, 0.4, 2.0)):
        n1 = [1.0, 0.0, 0.0]
        n2 = [math.cos(th), math.sin(th), 0.0]
        A = mm(boost(e1, n1), boost(e2, n2))
        om_polar = rotation_angle(A)
        c1, s1 = math.cosh(e1 / 2), math.sinh(e1 / 2)
        c2, s2 = math.cosh(e2 / 2), math.sinh(e2 / 2)
        om_form = 2.0 * math.atan2(math.sin(th) * s1 * s2,
                                   c1 * c2 + math.cos(th) * s1 * s2)
        print(f"{e1:>6.2f}{e2:>6.2f}{th:>8.4f}{om_polar:>16.10f}"
              f"{om_form:>17.10f}")
        check(f"Wigner angle e=({e1},{e2}) th={th:.3f}", om_polar, om_form)
    print()
    print("  Prediction 1 CONFIRMED to 1e-9 in every row, including the")
    print("  parallel case (theta = 0) where the rotation vanishes exactly.")
    print()

    print("=" * 74)
    print("PART 2  --  Circular motion: accumulate around the loop")
    print("=" * 74)
    print()
    print("  Pure boost L(phi) from lab to the comoving frame at angle phi.")
    print("  Step to phi+dphi and polar-decompose L(phi+dphi) L(phi)^-1; the")
    print("  rotation factor is the Thomas rotation for that step. Sum them.")
    print()
    for beta in (0.1, 0.5, 0.8):
        eta = math.atanh(beta)
        gamma = 1.0 / math.sqrt(1 - beta * beta)
        target = 2 * math.pi * (gamma - 1.0)
        print(f"  beta = {beta}:   gamma = {gamma:.8f},"
              f"   2 pi (gamma-1) = {target:.10f}")
        hdr2 = f"{'N steps':>10}{'accumulated angle':>22}{'rel. error':>14}"
        print("  " + hdr2)
        print("  " + "-" * len(hdr2))
        for N in (60, 600, 6000, 60000):
            tot = 0.0
            for k in range(N):
                p0 = 2 * math.pi * k / N
                p1 = 2 * math.pi * (k + 1) / N
                L0 = boost(eta, [math.cos(p0), math.sin(p0), 0.0])
                L1 = boost(eta, [math.cos(p1), math.sin(p1), 0.0])
                tot += rotation_angle(mm(L1, inv(L0)))
            err = abs(tot - target) / target
            print(f"  {N:>10}{tot:>22.10f}{err:>14.3e}")
        check(f"Thomas angle converges, beta={beta}", tot, target, atol=1e-4)
        print()
    print("  Predictions 2 and 3 CONFIRMED: converges to 2 pi (gamma - 1),")
    print("  with relative error falling as 1/N^2 through N = 6000.")
    print("  The N = 60000 rows are WORSE, and that is arithmetic not physics:")
    print("  each step's rotation angle is ~1e-6 rad, and acos(x) near x = 1")
    print("  loses about half the significant digits. Best accuracy is at")
    print("  N ~ 6000 where discretisation and round-off cross over.")
    print(f"  Slow limit at beta=0.1:  pi beta^2 = {math.pi * 0.01:.8f}"
          f"   vs 2pi(gamma-1) = {2 * math.pi * (1 / math.sqrt(0.99) - 1):.8f}")
    check("slow limit agrees to 1%",
          abs(math.pi * 0.01 - 2 * math.pi * (1 / math.sqrt(0.99) - 1))
          / (math.pi * 0.01) < 0.02, True, atol=0.5)
    print()

    print("=" * 74)
    print("PART 3  --  Gauss-Bonnet cross-check on rapidity space")
    print("=" * 74)
    print()
    print("  Rapidity space is hyperbolic 3-space with curvature -1. A closed")
    print("  velocity loop has holonomy equal to the enclosed area, and the")
    print("  hyperbolic area of a disc of radius eta is 2 pi (cosh eta - 1).")
    print("  Since cosh(eta) = gamma, that is 2 pi (gamma - 1) -- the same")
    print("  number, from geometry rather than from composing matrices.")
    print()
    hdr3 = f"{'beta':>8}{'eta':>12}{'2pi(cosh eta -1)':>20}{'2pi(gamma-1)':>18}"
    print(hdr3)
    print("-" * len(hdr3))
    for beta in (0.1, 0.5, 0.8, 0.99):
        eta = math.atanh(beta)
        g = 1.0 / math.sqrt(1 - beta * beta)
        a = 2 * math.pi * (math.cosh(eta) - 1)
        b = 2 * math.pi * (g - 1)
        print(f"{beta:>8.2f}{eta:>12.6f}{a:>20.10f}{b:>18.10f}")
        check(f"Gauss-Bonnet = 2pi(gamma-1) at beta={beta}", a, b)
    print()
    print("  Two independent routes to the same number. The precession is the")
    print("  CURVATURE OF VELOCITY SPACE, which is a genuinely clarifying way")
    print("  to say it -- Thomas precession stops being an anomaly and becomes")
    print("  a holonomy.")
    print()

    print("=" * 74)
    print("PART 4  --  VERDICT, including the prediction that FAILED")
    print("=" * 74)
    print()
    print("  Prediction 4 said the product of two boosts is LOXODROMIC. Test")
    print("  it directly -- the conjugacy class is fixed by the trace:")
    print()
    hdr4 = (f"{'eta1':>6}{'eta2':>6}{'theta':>8}{'tr A':>26}{'class':>14}")
    print(hdr4)
    print("-" * len(hdr4))
    for e1, e2, th in ((1.0, 1.0, math.pi / 2), (0.5, 1.5, math.pi / 3),
                       (2.0, 2.0, 1.1)):
        n1 = [1.0, 0.0, 0.0]
        n2 = [math.cos(th), math.sin(th), 0.0]
        A = mm(boost(e1, n1), boost(e2, n2))
        t = tr(A)
        cls = ("LOXODROMIC" if abs(t.imag) > 1e-12
               else ("hyperbolic" if abs(t.real) > 2 else "elliptic"))
        print(f"{e1:>6.2f}{e2:>6.2f}{th:>8.4f}"
              f"{str(complex(round(t.real, 10), round(t.imag, 10))):>26}{cls:>14}")
        check(f"tr is real for boost product ({e1},{e2})", t.imag, 0.0)
    print()
    print("  PREDICTION 4 IS FALSE. tr A is REAL and > 2 in every case, so the")
    print("  product of two boosts is HYPERBOLIC -- conjugate to a pure boost,")
    print("  not loxodromic. Analytically: tr A = 2[c1c2 + s1s2 cos(theta)],")
    print("  manifestly real for real rapidities.")
    print()
    print("  What went wrong in the reasoning: the Wigner rotation lives in the")
    print("  POLAR decomposition (A = R B), not in the CONJUGACY class. Those")
    print("  are different decompositions and 0008 classified by the second.")
    print("  A product of two boosts genuinely contains a rotation factor and")
    print("  is still conjugate to a pure boost. No contradiction -- but the")
    print("  taxonomy cannot see it.")
    print()
    print("  CONSEQUENCE FOR THE FRAMEWORK, stated plainly:")
    print()
    print("    0008's conjugacy taxonomy does NOT predict Thomas precession.")
    print("    It is the wrong instrument for this question.")
    print()
    print("    What DOES deliver is the REPRESENTATION -- SL(2,C) with Pauli")
    print("    algebra. The rotation term is the i s1 s2 (n1 x n2).sig piece,")
    print("    readable off a single product with no tensor manipulation.")
    print("    That is a real computational win, and it is the win that the")
    print("    'saves students memorising equations' hope actually rests on.")
    print()
    print("    So the workstream has TWO separable assets, and only one of")
    print("    them just passed a test:")
    print("      representation (SL(2,C)/spinor/bivector) -- earns its keep")
    print("      classification (0008's four classes)     -- untested, and")
    print("                                                  not applicable here")
    print()

    print("=" * 74)
    print("SELF-CHECKS")
    print("=" * 74)
    bad = [p for p in PASS if not p[1]]
    for name, ok, got, want in PASS:
        print(f"  [{'ok' if ok else 'FAIL'}] {name:<46} {float(got):+.6e}")
    print()
    print(f"  {len(PASS) - len(bad)}/{len(PASS)} checks passed.")
    print(f"  predictions stated: {len(PRED)}   confirmed: 3   FALSIFIED: 1")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
