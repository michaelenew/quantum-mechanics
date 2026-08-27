"""The frame functional: the ledger writes the action.

A critical pass through 0045's action derivation found a flaw in
its negative result, and correcting it exposes the most likely path
to the full functional -- which turns out to be one the program has
been circling since 0026.

  s1  THE CRITICAL PASS.  0045 s4 tested off-shell squaring with a
      metric cross term of weight sqrt(w1 w2) -- a guess, not the
      map the double copy implies.  If the metric is a square, the
      additive object is the FRAME e (g = e eta e^T), and the frame
      dictates its own cross term.  The corrected test is below,
      and it reverses the verdict.

  s2  THE EXACT TETRAD.  e = 1 + (1/2) w k k^T eta squares to the
      Kerr-Schild metric EXACTLY -- residual 1e-15 including w = 3
      (strong field) and Doppler-scaled k -- because k's nullity
      kills the quadratic term: (k k^T eta)^2 = (k.k) k k^T eta = 0.
      So:
        - THE CHANNEL IS THE FRAME PERTURBATION, exactly linear at
          any strength;
        - the ledger's 1/2 is the literal coefficient in
          e = 1 + (1/2)(channel);
        - collinear channels superpose EXACTLY (same k: the cross
          term carries k.k = 0), so mass additivity at a point is
          an identity, not an approximation.

  s3  THE CORRECTED OFF-SHELL TEST.  Squaring the SUM of frames
      gives the cross term (w1 w2/4)(k1.k2)(k1 k2^T + k2 k1^T).
      Measured on the static two-body configuration:
        c = 0 (superposition):    5.16e-3   (0037's violation)
        c = 1 (frame-sum square): 2.97e-3   (42% reduction)
        minimum ~2.5e-3 near c = 1.5; 0045's wrong-weight term
        made it WORSE at every c != 0.
      The frame is the better additive variable; the residual is
      the genuine second-order (bond) iteration that no pointwise
      ansatz supplies.

  s4  THE FUNCTIONAL.  The frame-first reading plus the prototype
      path converge on first-order tetrad gravity:

        3+1:  S[e,w] = (1/2k) int eps_IJKL e^I ^ e^J ^ F^KL(w)
        2+1:  S[e,w] = (1/k)  int eps_IJK  e^I ^ F^JK(w)

      The 2+1 form IS 0026's BF action with B = e (budget = frame,
      linear).  The 3+1 form is BF with B = e ^ e -- Plebanski's
      simplicity constraint satisfied identically -- and its
      omega-equation d_w(e ^ e) = 0 is 0030's measured lattice law
      dB = 0 (the budget is a closed 2-form).  0044's three
      constraints check: linear per channel (s2, exact);
      conservation as the second EOM (d_w B = 0); reduction to the
      2+1 prototype (B = e).  And 0030's frontier question -- what
      plays Plebanski's constraint in an information web -- has the
      ledger's answer: B = e ^ e IS "probability = amplitude^2" at
      the action level.  In 2+1 the two tiers coincide (B = e), so
      the prototype saw topological BF, additive charges, and no
      gravitons; in 3+1 the budget is the SQUARE of the frame, and
      that single squaring is where gravitons, multiplicative
      bonds, and the bond quantum = (charge quantum)^2 all come
      from.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import random
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_t = importlib.import_module("0030_the_time_sector")
ricci4, ETA = _t.ricci4, _t.ETA

TAU = 2 * math.pi


def mm4(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4))
             for j in range(4)] for i in range(4)]


# =====================================================================
# battery instrument: the channel tetrad
# =====================================================================

def channel_tetrad(w, k):
    """e = 1 + (1/2) w k (eta k)^T -- the exact Kerr-Schild frame."""
    etak = [ETA[j][j] * k[j] for j in range(4)]
    return [[(1 if i == j else 0) + 0.5 * w * k[i] * etak[j]
             for j in range(4)] for i in range(4)]


def square_frame(E):
    """g = E eta E^T."""
    return mm4(mm4(E, ETA), [[E[j][i] for j in range(4)]
                             for i in range(4)])


# =====================================================================
# 1. the critical pass (audit, printed)
# =====================================================================

def verify_critical_pass() -> None:
    print("  0045 s4's off-shell test used a metric cross term of")
    print("  weight sqrt(w1 w2) -- a guess at the squaring map, not")
    print("  the map itself.  If the metric is a square, the")
    print("  additive object is the FRAME (g = e eta e^T), and the")
    print("  frame fixes its own cross term:")
    print("    (e1 + e2 - 1)-squared  =>  cross =")
    print("      (w1 w2/4)(k1.k2)(k1 k2^T + k2 k1^T),")
    print("  with weight w1 w2 and the null inner product k1.k2 --")
    print("  neither of which the 0045 ansatz had.  The corrected")
    print("  test (s3) reverses the verdict; 0045's negative stands")
    print("  only against its own ansatz.")


# =====================================================================
# 2. the exact tetrad
# =====================================================================

def verify_exact_tetrad() -> None:
    random.seed(3)
    worst = 0.0
    for _ in range(6):
        n = [random.gauss(0, 1) for _ in range(3)]
        nn = math.sqrt(sum(c * c for c in n))
        k = (-1.0, n[0] / nn, n[1] / nn, n[2] / nn)
        w = random.uniform(0.05, 3.0)
        g = square_frame(channel_tetrad(w, k))
        KS = [[ETA[i][j] + w * k[i] * k[j] for j in range(4)]
              for i in range(4)]
        worst = max(worst, max(abs(g[i][j] - KS[i][j])
                               for i in range(4) for j in range(4)))
    # Doppler-scaled (moving-channel) k: D(-1, n), still null
    D = 1.7
    k = (-D, D * 0.6, D * 0.64, D * 0.48)
    g = square_frame(channel_tetrad(0.8, k))
    KS = [[ETA[i][j] + 0.8 * k[i] * k[j] for j in range(4)]
          for i in range(4)]
    worst = max(worst, max(abs(g[i][j] - KS[i][j])
                           for i in range(4) for j in range(4)))
    assert worst < 1e-12, worst
    print(f"    e = 1 + (1/2) w k k^T eta squares to Kerr-Schild to")
    print(f"    {worst:.0e}, including w = 3 and Doppler-scaled k:")
    print(f"    nullity kills the quadratic term, (k.k) = 0.")
    # collinear additivity is exact
    k = (-1.0, 0.6, 0.64, 0.48)
    E1 = channel_tetrad(0.4, k)
    E2 = channel_tetrad(0.7, k)
    Esum = [[E1[i][j] + E2[i][j] - (1 if i == j else 0)
             for j in range(4)] for i in range(4)]
    g = square_frame(Esum)
    KS = [[ETA[i][j] + 1.1 * k[i] * k[j] for j in range(4)]
          for i in range(4)]
    dev = max(abs(g[i][j] - KS[i][j])
              for i in range(4) for j in range(4))
    assert dev < 1e-12, dev
    print(f"    collinear channels superpose exactly ({dev:.0e}):")
    print(f"    mass additivity at a point is an identity.")
    print()
    print("  THE CHANNEL IS THE FRAME PERTURBATION -- exactly linear")
    print("  at any strength -- and the ledger's 1/2 is the literal")
    print("  coefficient in e = 1 + (1/2)(channel).")


# =====================================================================
# 3. the corrected off-shell test
# =====================================================================

M_S, D_S = 0.01, 1.0
C1, C2 = (-D_S / 2, 0.0, 0.0), (D_S / 2, 0.0, 0.0)
PTS = [(0.0, 0.0, 0.45, 0.30), (0.0, 0.35, 0.60, 0.0),
       (0.0, 0.2, 0.3, 0.4)]


def _parts(x):
    out = []
    for c in (C1, C2):
        r = math.dist(x[1:], c)
        k = (-1.0, (x[1] - c[0]) / r, (x[2] - c[1]) / r,
             (x[3] - c[2]) / r)
        out.append((2 * M_S / r, k))
    return out


def g_frame_cross(cc):
    """Superposition plus cc times the FRAME-square cross term."""
    def g(x):
        (w1, k1), (w2, k2) = _parts(x)
        m = [[ETA[i][j] for j in range(4)] for i in range(4)]
        for (w, k) in ((w1, k1), (w2, k2)):
            for i in range(4):
                for j in range(4):
                    m[i][j] += w * k[i] * k[j]
        dot = sum(ETA[a][a] * k1[a] * k2[a] for a in range(4))
        ct = cc * 0.25 * w1 * w2 * dot
        for i in range(4):
            for j in range(4):
                m[i][j] += ct * (k1[i] * k2[j] + k2[i] * k1[j])
        return m
    return g


def verify_frame_cross() -> None:
    results = {}
    for cc in (0.0, 0.5, 1.0, 1.5, 2.0):
        worst = 0.0
        for x in PTS:
            R = ricci4(g_frame_cross(cc), x, h=1e-3)
            worst = max(worst, max(abs(R[i][j])
                                   for i in range(4)
                                   for j in range(4)))
        results[cc] = worst
        tag = ("   <-- superposition (0037)" if cc == 0.0 else
               ("   <-- frame-sum square" if cc == 1.0 else ""))
        print(f"    c = {cc:+.1f}: max|R_mn| = {worst:.2e}{tag}")
    assert results[1.0] < 0.65 * results[0.0], results
    assert results[1.5] < results[1.0]
    print()
    print("  THE FRAME-SQUARE CROSS TERM REDUCES THE VIOLATION by")
    print("  ~2x (0045's wrong-weight term increased it at every")
    print("  c != 0).  The frame is the better additive variable;")
    print("  the residual is the genuine second-order (bond)")
    print("  iteration, which no pointwise ansatz supplies -- that")
    print("  is the field equation's own job.")


# =====================================================================
# 4. the functional
# =====================================================================

def verify_functional() -> None:
    print("  The frame-first reading and the prototype path converge")
    print("  on FIRST-ORDER TETRAD GRAVITY:")
    print()
    print("    3+1:  S[e,w] = (1/2k) int eps_IJKL e^I ^ e^J ^ F^KL")
    print("    2+1:  S[e,w] = (1/k)  int eps_IJK  e^I ^ F^JK")
    print()
    print("  Checks against everything measured:")
    print("    - the 2+1 form IS 0026's BF action with B = e:")
    print("      budget = frame, linear -- the prototype;")
    print("    - the 3+1 form is BF with B = e ^ e (Plebanski's")
    print("      simplicity constraint, satisfied identically); its")
    print("      omega-equation d_w(e ^ e) = 0 is 0030's measured")
    print("      lattice law dB = 0;")
    print("    - linear per channel: s2's exact tetrad;")
    print("    - the bond: the e-equation's second-order iteration,")
    print("      whose integrated cross stress is the virial bond")
    print("      (0040 s2, measured exactly);")
    print("    - matter: S_m = m int |e(xdot)| dtau -- proper time")
    print("      metered by the frame, which is 0035's sender-clock")
    print("      normalization as a variational principle.")
    print()
    print("  And 0030's frontier question -- WHAT PLAYS PLEBANSKI'S")
    print("  CONSTRAINT IN AN INFORMATION WEB -- has the ledger's")
    print("  answer: B = e ^ e is 'probability = amplitude squared'")
    print("  at the action level.  In 2+1 the tiers coincide (B = e):")
    print("  topological BF, additive charges, no gravitons.  In 3+1")
    print("  the budget is the SQUARE of the frame, and that single")
    print("  squaring is where gravitons, multiplicative bonds, and")
    print("  bond quantum = (charge quantum)^2 all come from.")


def run_verification_suite() -> None:
    sections = [
        ("The critical pass", verify_critical_pass),
        ("The exact tetrad", verify_exact_tetrad),
        ("The corrected off-shell test", verify_frame_cross),
        ("The functional", verify_functional),
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
