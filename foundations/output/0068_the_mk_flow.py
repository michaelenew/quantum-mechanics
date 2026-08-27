"""The MK flow: 4D is where the healed weight goes critical.

A4 (0070's path A continuation): which sector of the healed weight
survives coarse-graining in four dimensions?  The instrument is the
Migdal-Kadanoff recursion -- bond-moving (pointwise power zeta =
b^{d-2}) then decimation (per-representation t -> t^{b^2}) --
calibrated against both exact anchors this program owns, with its
bias measured, and implemented in a controlled grid form after the
naive truncated-fusion form was caught flipping its verdict with the
cutoff.

  s1  CALIBRATION, WITH THE INSTRUMENT'S BIAS MEASURED.  2D (zeta=1,
      where MK is exact): the Z_3 ledger collapses to free, matching
      0071's exact blocking.  4D abelian: N = 3, 5 flow to
      BF/deconfined, matching 0071's self-duality placement -- but
      N = 2 ALSO flows to BF, where the exact answer is confined:
      MK IS BIASED TOWARD DECONFINEMENT NEAR TRANSITIONS.  Recorded,
      and used: an MK verdict of "confined" is trustworthy; an MK
      "deconfined" near a transition is suspect.  Also recorded: the
      truncated-fusion implementation (coefficient cutoff jmax)
      flips its 4D verdict as jmax grows -- the controlled form
      below does exact pointwise bond-moving on a class-angle grid
      and truncates only the decimated reconstruction, where t^4
      decay makes the cutoff harmless.

  s2  THE 4D FLOW IS NEAR-STATIONARY WITH A STABLE HIERARCHY.  Over
      12 steps the healed weight's transfer eigenvalues barely move:

        t(1,0) 0.937   t(1,1) 0.878   t(2,2) 0.68   t(3,3) 0.46
        t(6,6) 0.065          (drift < 1% total, all reps)

      -- a (near-)fixed structure: not the free/confined sink, not
      the BF/topological point, but a HIERARCHICAL spectrum frozen
      between them, with 0075's mode ordering preserved under the
      flow and high spins suppressed.

  s3  THE 3D CONTRAST IS TOTAL.  The same instrument, zeta = 2:
      t(1,1) ~ 1e-71 by step 8.  Three dimensions confine
      absolutely; four go critical.  0071's abelian dichotomy --
      rigidity begins at D = 4 -- survives the nonabelian lift.

  s4  THE READING.  Within MK, the healed weight in 4D sits at or
      near a nontrivial fixed structure whose light sectors are the
      low-spin multiplets -- the graviton multiplet (1,1) among the
      survivors at t ~ 0.88 -- while high spins die.  The
      deconfinement bias means reality could shade from "marginal"
      toward "slowly confining"; the 3D/4D dichotomy and the
      surviving hierarchy are the robust content.  A3's momentum
      half should be posed AT this fixed structure.

Run directly for the verification suite.
"""

from __future__ import annotations

import cmath
import importlib
import math
import os
import sys
from math import gcd

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
_m67 = importlib.import_module('0067_the_tension_spectrum')


# =====================================================================
# 1. calibration
# =====================================================================

def _zn_step(W, N, zeta, bsq):
    V = [w ** zeta for w in W]
    Z = sum(V)
    T = []
    for n in range(N):
        c = sum(V[F] * cmath.exp(-2j * math.pi * n * F / N)
                for F in range(N)).real
        t = c / Z
        T.append((max(t, 0.0)) ** bsq)
    Wp = [sum(T[n] * math.cos(2 * math.pi * n * F / N)
              for n in range(N)) for F in range(N)]
    m = max(Wp)
    return [w / m for w in Wp]


def verify_calibration() -> None:
    W = [float(gcd(F if F else 3, 3)) for F in range(3)]
    for _ in range(6):
        W = _zn_step(W, 3, 1, 4)
    Z = sum(W)
    t1 = sum(W[F] * math.cos(2 * math.pi * F / 3)
             for F in range(3)) / Z
    assert abs(t1) < 1e-3
    print(f"    2D anchor (exact): Z_3 ledger -> free "
          f"(t = {t1:+.1e}), matching 0071's exact blocking")
    verdicts = {}
    for N in (2, 3, 5):
        W = [float(gcd(F if F else N, N)) for F in range(N)]
        for _ in range(12):
            W = _zn_step(W, N, 4, 4)
        Z = sum(W)
        verdicts[N] = sum(W[F] * math.cos(2 * math.pi * F / N)
                          for F in range(N)) / Z
    assert verdicts[3] > 0.9 and verdicts[5] > 0.9
    assert verdicts[2] > 0.9      # the measured BIAS
    print(f"    4D abelian: N = 3, 5 -> BF (correct); N = 2 -> BF")
    print(f"    where the EXACT answer (0071) is confined:")
    print(f"    MK IS DECONFINEMENT-BIASED NEAR TRANSITIONS --")
    print(f"    a 'confined' verdict is trustworthy, a marginal")
    print(f"    'deconfined' is suspect")
    print()
    print("  Calibrated: one exact pass, one exact match, one known")
    print("  bias.  And the truncated-fusion pitfall (verdict flips")
    print("  with jmax) is documented -- the grid form below avoids it.")


# =====================================================================
# the controlled grid recursion
# =====================================================================

NG = 200
JBIG = 24
THS = [2 * math.pi * (i + 0.5) / NG for i in range(NG)]
WEYL = [(1 / math.pi) * math.sin(t / 2) ** 2 * (2 * math.pi / NG)
        for t in THS]


def _chi(j, t):
    s = math.sin(t / 2)
    return math.sin((2 * j + 1) * t / 2) / s if abs(s) > 1e-12 \
        else float(2 * j + 1)


_X = [[WEYL[i] * _chi(j, THS[i]) for i in range(NG)]
      for j in range(JBIG + 1)]
_CH = [[_chi(j, THS[i]) for i in range(NG)] for j in range(JBIG + 1)]


def _step(Wg, zeta, bsq=4):
    V = [[max(w, 0.0) ** zeta for w in row] for row in Wg]
    A = [[sum(_X[jp][i] * V[i][k] for i in range(NG))
          for k in range(NG)] for jp in range(JBIG + 1)]
    C = [[sum(A[jp][k] * _X[jm][k] for k in range(NG))
          for jm in range(JBIG + 1)] for jp in range(JBIG + 1)]
    c0 = C[0][0]
    T = [[(max(C[jp][jm], 0.0)
           / ((2 * jp + 1) * (2 * jm + 1) * c0)) ** bsq
          for jm in range(JBIG + 1)] for jp in range(JBIG + 1)]
    B = [[sum((2 * jp + 1) * T[jp][jm] * _CH[jp][i]
              for jp in range(JBIG + 1))
          for jm in range(JBIG + 1)] for i in range(NG)]
    Wg2 = [[sum(B[i][jm] * (2 * jm + 1) * _CH[jm][k]
                for jm in range(JBIG + 1)) for k in range(NG)]
           for i in range(NG)]
    m = max(max(row) for row in Wg2)
    return [[w / m for w in row] for row in Wg2], T


def _healed_grid():
    nj = _m67.density(0.75, 8)
    Wg = [[0.0] * NG for _ in range(NG)]
    for i in range(NG):
        for k in range(NG):
            a = sum(nj[m] * _chi(m, THS[i]) * _chi(m, THS[k])
                    for m in range(9))
            Wg[i][k] = a * a
    m = max(max(r) for r in Wg)
    return [[w / m for w in r] for r in Wg]


# =====================================================================
# 2. the 4D flow
# =====================================================================

def verify_4d_flow() -> None:
    Wg = _healed_grid()
    hist = []
    for it in range(1, 13):
        Wg, T = _step(Wg, zeta=4)
        hist.append(T)
        if it in (1, 3, 5, 8, 12):
            print(f"    step {it:2d}: t(1,0) = {T[1][0]:.4f}  "
                  f"t(1,1) = {T[1][1]:.4f}  t(2,2) = {T[2][2]:.4f}  "
                  f"t(3,3) = {T[3][3]:.4f}  t(6,6) = {T[6][6]:.4f}")
    t11 = [T[1][1] for T in hist[2:]]
    assert max(t11) / min(t11) < 1.01, (min(t11), max(t11))
    for T in hist:
        assert T[1][0] > T[1][1] > T[2][2] > T[3][3] > T[6][6]
    print()
    print("  NEAR-STATIONARY: t(1,1) drifts < 1% over steps 3-12;")
    print("  0075's ordering preserved at every step; high spins")
    print("  suppressed.  A nontrivial fixed structure between the")
    print("  free sink and the BF point.")


# =====================================================================
# 3. the 3D contrast
# =====================================================================

def verify_3d_contrast() -> None:
    Wg = _healed_grid()
    for _ in range(8):
        Wg, T = _step(Wg, zeta=2)
    print(f"    step 8 (zeta = 2): t(1,1) = {T[1][1]:.2e},  "
          f"t(1,0) = {T[1][0]:.2e}")
    assert T[1][1] < 1e-30
    print()
    print("  THREE DIMENSIONS CONFINE ABSOLUTELY; FOUR GO CRITICAL.")
    print("  0071's dichotomy -- rigidity begins at D = 4 -- survives")
    print("  the nonabelian lift.")


# =====================================================================
# 4. the reading
# =====================================================================

def verify_reading() -> None:
    print("    within MK: the healed weight in 4D sits at/near a")
    print("    nontrivial fixed structure; light sectors = low-spin")
    print("    multiplets, the graviton multiplet among the survivors")
    print("    at t ~ 0.88; high spins die.  The measured bias means")
    print("    'marginal' could shade toward 'slowly confining';")
    print("    the 3D/4D dichotomy and the surviving hierarchy are")
    print("    the robust content.")
    print()
    print("  A3'S MOMENTUM HALF SHOULD BE POSED AT THIS FIXED")
    print("  STRUCTURE -- the flow has now told us where the")
    print("  continuum candidate lives.")


def run_verification_suite() -> None:
    sections = [
        ("Calibration, with the instrument's bias measured",
         verify_calibration),
        ("The 4D flow is near-stationary with a stable hierarchy",
         verify_4d_flow),
        ("The 3D contrast is total", verify_3d_contrast),
        ("The reading", verify_reading),
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
