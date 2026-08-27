"""Does the web's construction solve Einstein at second order?

0059 named the two-body rule as the program's falsifiable surface and
framed it as a binary against Einstein-Infeld-Hoffmann.  That framing
was wrong, and this module both corrects it and runs the measurement
that IS available.

THE CORRECTION.  0046 identified the classical functional as
S = (1/2 kappa) int eps_IJKL e^e^F, and 0050 verified it: torsion
equation rank 24/24 (omega algebraic in e), 2 dof, Palatini route
reproducing the metric route's Ricci to 1e-6.  That is the PALATINI
ACTION OF GENERAL RELATIVITY.  If the action is GR's, the field
equations are Einstein's and the two-body dynamics is EIH
necessarily -- there is no binary and no classical falsifier of GR
anywhere in the program.  The only classical question with a real
failure mode is different: CAN THE WEB'S CONSTRUCTION (superposed
channels, plus the bond) ACTUALLY GENERATE EINSTEIN'S SOLUTIONS?

  s1  THE DIAGNOSTIC, VALIDATED.  Truncate harmonic-coordinate
      Schwarzschild -- exactly known -- at successive orders and
      measure the log-log slope of the off-source residual
      max|R_mn| against the mass:

        truncation      slope      expected
        first order     1.985      2   (h2 missing)
        second order    2.885      3   (h2 correct)
        exact           0.996      finite-difference floor, ~M^1

      So the slope DOES distinguish "second-order term correct"
      from "second-order term missing," and the exact solution's
      residual is a pure truncation floor scaling as M, not M^2.
      This is the instrument; s2 is the measurement.

  s2  NO POINTWISE CROSS TERM SUPPLIES THE SECOND ORDER.  0046
      found the frame-square cross term
      (w1 w2/4)(k1.k2)(k1 k2^T + k2 k1^T) reduces the two-body
      violation ~2x and conjectured the residual was "the genuine
      second-order bond iteration, which no pointwise ansatz
      supplies."  Scanning the cross-term coefficient c over
      [-2, +4] and measuring the slope at each:

        c            0.0 (superposition)   1.5 (optimum)
        max|R|       5.16e-3               2.51e-3
        slope        2.015                 2.042

      The minimum over c reduces the COEFFICIENT by 2x and leaves
      the ORDER untouched -- slope 2 everywhere, against the
      validated target of 3.  The two-body residual sits 2-3 orders
      above the single-mass floor throughout, so this is signal.
      0046's conjecture is confirmed, and the ansatz path is closed:
      no scalar multiple of the frame-dictated cross term is the
      second-order solution.

  s2b THE ORDER DIAGNOSTIC IS GAUGE-DEPENDENT (adversarial review,
      incorporated).  "Truncate at first order" is NOT a
      coordinate-independent notion: Kerr-Schild Schwarzschild
      TERMINATES at first order (it is exact, so its residual is
      the floor), while harmonic Schwarzschild does not (slope 2).
      Same spacetime, different slope.  An M-dependent diffeo with
      xi = O(M) shifts the truncated metric at O(M^2) -- exactly
      the order being measured -- so the leading residual
      coefficient is not an invariant and Stewart-Walker does not
      apply to a truncated series.  What survives:
        - "R_mn is nonzero at O(w1 w2)" IS gauge-invariant, since
          R_mn is a tensor.  Confirmed analytically off this
          module: on the axis outside both bodies the bilinear
          Ricci is exactly 4 w1 w2 d^2/(r1^3 r2^3) l_mu l_nu.
        - the measurement is about the WEB'S OWN construction in
          the WEB'S OWN coordinates, which is the object of
          interest -- not a claim that no gauge-equivalent repair
          exists;
        - the test certifies a candidate h2 only modulo ker R^(1)
          (pure gauge plus homogeneous linearized-vacuum
          solutions), which only boundary conditions exclude.
      The noise floor is separately checked to be
      finite-difference TRUNCATION (slope 1, ratio 2.00 per
      halving down to M = 6.25e-4 at 8.7e-8) and not roundoff
      (eps_mach/h^2 ~ 2.2e-10, some 400x below), so it cannot
      flatten the tail toward slope 0 in this range.

  s3  WHAT IS AND IS NOT SHOWN.  This is a CONFIRMATION of a stated
      expectation, not a falsifier.  It closes 0046's open item
      ("iterate the e-equation once to confirm the residual drops
      an order") with the answer: the pointwise ansatz does not
      drop an order, so a genuine field-equation iteration is
      required and has NOT been done.  The web's own claim is that
      the second order comes from the BOND (0040-0042), not from a
      metric ansatz -- and the bond is structurally the Weyl strut
      that GR requires to hold two static masses apart, with the
      virial law int S = -F*d matching a strut of tension
      F = G m1 m2 / d^2 over length d.  Whether the bond supplies
      the correct h2 is now the sharp open question, and s1 gives
      it a pass/fail criterion: slope 2 -> 3.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
_ff = importlib.import_module('0041_the_frame_functional')
ricci4, PTS, ETA = _ff.ricci4, _ff.PTS, _ff.ETA

MASSES = [0.02, 0.01, 0.005, 0.0025]


def log_slope(xs, ys):
    lx = [math.log(v) for v in xs]
    ly = [math.log(v) for v in ys]
    n = len(lx)
    mx, my = sum(lx) / n, sum(ly) / n
    return (sum((lx[i] - mx) * (ly[i] - my) for i in range(n))
            / sum((lx[i] - mx) ** 2 for i in range(n)))


def worst_residual(g):
    out = 0.0
    for x in PTS:
        R = ricci4(g, x, h=1e-3)
        out = max(out, max(abs(R[i][j])
                           for i in range(4) for j in range(4)))
    return out


# =====================================================================
# 1. the diagnostic, validated on harmonic Schwarzschild
# =====================================================================

def harmonic_schwarzschild(m, order):
    """Schwarzschild in harmonic coordinates, truncated.
    Exact:  g00 = -(r-m)/(r+m),
            gij = ((r+m)/r)^2 d_ij + m^2(r+m)/(r^2(r-m)) n_i n_j."""
    def g(x):
        r = math.dist(x[1:], (0.0, 0.0, 0.0))
        n = [x[1] / r, x[2] / r, x[3] / r]
        if order == 'exact':
            g00 = -(r - m) / (r + m)
            iso = ((r + m) / r) ** 2
            nn = m * m * (r + m) / (r * r * (r - m))
        elif order == 1:
            g00, iso, nn = -1 + 2 * m / r, 1 + 2 * m / r, 0.0
        else:
            g00 = -1 + 2 * m / r - 2 * m * m / (r * r)
            iso = 1 + 2 * m / r + m * m / (r * r)
            nn = m * m / (r * r)
        M = [[0.0] * 4 for _ in range(4)]
        M[0][0] = g00
        for i in range(3):
            for j in range(3):
                M[i + 1][j + 1] = (iso * (1.0 if i == j else 0.0)
                                   + nn * n[i] * n[j])
        return M
    return g


def verify_diagnostic() -> None:
    res = {}
    for order in (1, 2, 'exact'):
        res[order] = [worst_residual(harmonic_schwarzschild(m, order))
                      for m in MASSES]
    print(f"    {'M':>8} | {'1st order':>11} | {'2nd order':>11} | "
          f"{'exact':>11}")
    for i, m in enumerate(MASSES):
        print(f"    {m:8.4f} | {res[1][i]:11.4e} | {res[2][i]:11.4e} "
              f"| {res['exact'][i]:11.4e}")
    s1 = log_slope(MASSES, res[1])
    s2 = log_slope(MASSES, res[2])
    se = log_slope(MASSES, res['exact'])
    print()
    print(f"      1st-order truncation: slope {s1:.3f}  (expect 2 -- "
          f"h2 missing)")
    print(f"      2nd-order truncation: slope {s2:.3f}  (expect 3 -- "
          f"h2 correct)")
    print(f"      exact solution:       slope {se:.3f}  (finite-"
          f"difference floor, ~M^1)")
    assert 1.85 < s1 < 2.15, s1
    assert 2.6 < s2 < 3.3, s2
    assert se < 1.4, se
    assert s2 - s1 > 0.7, (s1, s2)
    # the floor must be FD truncation (slope 1), not roundoff
    # (slope 0) -- otherwise the small-M tail flattens and fakes
    # a slope change.  eps_mach/h^2 ~ 2.2e-10 here.
    deep = [worst_residual(harmonic_schwarzschild(m, 'exact'))
            for m in (0.0025, 0.00125, 0.000625)]
    for a, b in zip(deep, deep[1:]):
        assert 1.9 < a / b < 2.1, (a, b)
    assert deep[-1] > 100 * 2.22e-16 / 1e-6, deep[-1]
    print(f"      floor is FD truncation, not roundoff: halving M "
          f"halves it ({deep[0] / deep[1]:.2f}x, {deep[1] / deep[2]:.2f}x)")
    print(f"      and sits {deep[-1] / (2.22e-16 / 1e-6):.0f}x above "
          f"the roundoff floor eps/h^2")
    print()
    print("  THE SLOPE DISTINGUISHES A CORRECT SECOND-ORDER TERM FROM")
    print("  A MISSING ONE, on a case where the answer is known.  The")
    print("  exact solution's residual is a pure truncation floor that")
    print("  scales as M, not M^2, so it cannot masquerade as signal.")


# =====================================================================
# 2. no pointwise cross term supplies the second order
# =====================================================================

def two_body_residual(M, cc):
    _ff.M_S = M
    return worst_residual(_ff.g_frame_cross(cc))


def verify_no_pointwise_fix() -> None:
    print("    cross-term coefficient scan at M = 0.01:")
    scan = {}
    for tenths in range(-20, 45, 5):
        c = tenths / 10.0
        scan[c] = two_body_residual(0.01, c)
    best_c = min(scan, key=scan.get)
    for c in (-1.0, 0.0, 1.0, 1.5, 2.0, 3.0):
        tag = ""
        if c == 0.0:
            tag = "   <- superposition (0037)"
        elif c == best_c:
            tag = "   <- minimum"
        print(f"      c = {c:+.1f}: max|R| = {scan[c]:.4e}{tag}")
    assert best_c == 1.5, best_c
    assert scan[best_c] > 0.4 * scan[0.0], (scan[best_c], scan[0.0])
    print()
    print("    mass scaling at three coefficients:")
    slopes = {}
    for c in (0.0, 1.0, best_c):
        vals = [two_body_residual(m, c) for m in MASSES]
        slopes[c] = log_slope(MASSES, vals)
        print(f"      c = {c:+.1f}: slope = {slopes[c]:.3f}")
    for c, s in slopes.items():
        assert 1.9 < s < 2.2, (c, s)
    # signal must sit well above the single-mass floor
    floor = worst_residual(harmonic_schwarzschild(MASSES[-1], 'exact'))
    sig = two_body_residual(MASSES[-1], best_c)
    print(f"      at the smallest mass, signal {sig:.2e} vs floor "
          f"{floor:.2e}  (ratio {sig / floor:.0f}x)")
    assert sig / floor > 100, (sig, floor)
    print()
    print("  NO POINTWISE CROSS TERM SUPPLIES THE SECOND ORDER.  The")
    print("  optimum reduces the COEFFICIENT ~2x and leaves the ORDER")
    print("  untouched -- slope 2 everywhere against the validated")
    print("  target of 3.  0046's conjecture that 'no pointwise ansatz")
    print("  supplies it -- that is the field equation's own job' is")
    print("  confirmed, and the ansatz path is closed.")


# =====================================================================
# 3. what is and is not shown
# =====================================================================

def verify_scope() -> None:
    print("    This is a CONFIRMATION of a stated expectation, not a")
    print("    falsifier.  0059 s3's 'binary against EIH' was wrong:")
    print("    0046/0050 identify the classical action as Palatini")
    print("    gravity (torsion rank 24/24, 2 dof, Ricci matched to")
    print("    1e-6), which IS general relativity -- so the field")
    print("    equations are Einstein's and EIH follows necessarily.")
    print("    No classical falsifier of GR exists in the program.")
    print()
    print("    The question with a real failure mode is whether the")
    print("    WEB'S CONSTRUCTION can generate Einstein's solutions.")
    print("    Its own answer is the bond (0040-0042), which is")
    print("    structurally the Weyl strut GR needs to hold two static")
    print("    masses apart: virial int S = -F*d matches a strut of")
    print("    tension F = G m1 m2/d^2 over length d.")
    print()
    print("  THE SHARP OPEN QUESTION IS NOW WELL POSED WITH A PASS/")
    print("  FAIL CRITERION: does the bond's contribution move the")
    print("  two-body slope from 2 to 3?  s1 validates that the")
    print("  criterion can tell the difference; s2 shows no metric")
    print("  ansatz reaches it.  The bond has not been tested.")


def run_verification_suite() -> None:
    sections = [
        ("The diagnostic, validated on harmonic Schwarzschild",
         verify_diagnostic),
        ("No pointwise cross term supplies the second order",
         verify_no_pointwise_fix),
        ("What is and is not shown", verify_scope),
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
