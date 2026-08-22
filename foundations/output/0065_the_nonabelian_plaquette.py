"""The nonabelian plaquette: the derived weight meets the sign problem.

Path A's third stone (0070's A2, first half).  0072's continuum
kernel K(F) = (2 pi)^4/(eps^2 + eps|F|^2 + Pf^2) is lifted to a class
function on Spin(4) = SU(2)+ x SU(2)- (Euclidean; class angles
theta+/-, curvature magnitudes f = 2 sin(theta/2) chord lift, or the
geodesic angle as sensitivity) and expanded in characters -- the
nonabelian analogue of 0064's dual weights.  Three findings, the
third with teeth.

  s1  THE CENTER IS BLIND.  Every half-integer-spin coefficient
      vanishes identically (machine zero): the weight is a function
      of f^2, invariant under theta -> 2pi - theta, so only INTEGER
      spins survive.  Vector frames see SO(4), not Spin(4): the
      derived vertex has no spinorial sector.  (Matter that needs
      spinors will need a spinorial B -- recorded, not lamented.)

  s2  THE SIMPLE REPRESENTATIONS DOMINATE, HEAVY-TAILED.  At small
      eps the balanced diagonal c(j,j) carries the weight (0.62,
      0.45, 0.34, 0.27 at j = 1..4, eps = 0.01) -- Barrett-Crane's
      simple representations emerging SOFTLY, as 0072 predicted --
      and the diagonal decays much slower than any heat kernel
      (matching e^{-x j(j+1)} on the first step predicts 0.14 at
      j = 4 where the actual is 0.27): the tau-lesson (heavy
      arithmetic tail, not Gaussian) at the nonabelian tier.

  s3  THE SIGN PROBLEM ARRIVES.  The weight is pointwise POSITIVE,
      but its character expansion is NOT: c(2,0) < 0 at every eps
      tested (down -0.008 even at eps = 1), and c(1,0) crosses zero
      near eps ~ 0.05, reaching -0.27 by eps = 0.003.  Both lifts
      (chord and angle) develop negative coefficients -- which
      coefficient differs, the negativity does not -- and the values
      are grid-stable to 5 decimals.  Character positivity is the
      standard Osterwalder-Seiler route to a positive transfer
      matrix; ITS FAILURE MEANS THE NAIVE ONE-PLAQUETTE LIFT DOES
      NOT OBVIOUSLY DEFINE A REFLECTION-POSITIVE THEORY.  This is
      the disease interacting quantum-gravity measures die of, met
      on schedule -- the wall, bleeding where 0071 predicted the
      bleed-line had moved.

  s4  AND THE CURE HAS THE LEDGER'S SHAPE.  The U(1) continuum
      ledger's dual weight was tau = 1 * 1 -- a DIRICHLET SQUARE,
      hence coefficient-positive automatically.  A nonabelian weight
      built as a dual square has character coefficients
      (amplitude)^2 >= 0 BY CONSTRUCTION.  The naive kernel lift is
      not that object -- and its negativity is evidence that the
      kernel alone was never the whole weight.  A2's disease
      independently demands exactly 0064 open 1: the nonabelian
      Dirichlet square.  The next stone is now forced, not chosen.
      (The sibling arithmetic branch's probe list names "the sign
      problem" -- a cognate wall, hit independently.)

Run directly for the verification suite.
"""

from __future__ import annotations

import math

NG = 400
THS = [2 * math.pi * (i + 0.5) / NG for i in range(NG)]
WEYL = [(1 / math.pi) * math.sin(t / 2) ** 2 * (2 * math.pi / NG)
        for t in THS]


def chi(j, t):
    n = int(round(2 * j)) + 1
    s = math.sin(t / 2)
    return math.sin(n * t / 2) / s if abs(s) > 1e-12 else float(n)


def dual_coeffs(eps, keys, lift="chord", ng=NG):
    ths = [2 * math.pi * (i + 0.5) / ng for i in range(ng)]
    weyl = [(1 / math.pi) * math.sin(t / 2) ** 2 * (2 * math.pi / ng)
            for t in ths]
    if lift == "chord":
        f = [2 * math.sin(t / 2) for t in ths]
    else:
        f = [min(t, 2 * math.pi - t) for t in ths]
    js = sorted(set(j for k in keys for j in k))
    ch = {j: [chi(j, t) for t in ths] for j in js}
    out = {}
    for (jp, jm) in keys:
        tot = 0.0
        for i in range(ng):
            a = f[i] * f[i]
            wi = weyl[i] * ch[jp][i]
            acc = 0.0
            for k in range(ng):
                b = f[k] * f[k]
                acc += (weyl[k] * ch[jm][k]
                        / (eps * eps + eps * (a + b)
                           + (a - b) ** 2 / 4))
            tot += wi * acc
        out[(jp, jm)] = tot
    return out


# =====================================================================
# 1. the center is blind
# =====================================================================

def verify_center_blind() -> None:
    keys = [(0, 0), (0.5, 0), (0.5, 0.5), (1.5, 0), (1.5, 1.5),
            (2.5, 0.5), (3.5, 1.5)]
    C = dual_coeffs(0.01, keys, ng=200)
    c00 = C[(0, 0)]
    for k in keys[1:]:
        assert abs(C[k] / c00) < 1e-10, (k, C[k] / c00)
    print("    every half-integer coefficient = 0 to machine")
    print("    precision (7 pairs checked at eps = 0.01)")
    print()
    print("  VECTOR FRAMES SEE SO(4), NOT Spin(4): the derived vertex")
    print("  carries integer spins only -- no spinorial sector.")
    print("  Matter that needs spinors will need a spinorial B.")


# =====================================================================
# 2. the simple representations dominate, heavy-tailed
# =====================================================================

def verify_simple_dominance() -> None:
    keys = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (1, 0), (2, 0)]
    C = dual_coeffs(0.01, keys)
    c00 = C[(0, 0)]
    diag = [C[(j, j)] / c00 for j in (1, 2, 3, 4)]
    print("    diagonal (simple-rep) profile at eps = 0.01:")
    for j, v in zip((1, 2, 3, 4), diag):
        print(f"      c({j},{j})/c(0,0) = {v:+.5f}")
    assert all(v > 0 for v in diag)
    assert diag[0] > abs(C[(1, 0)] / c00)
    # heat-kernel contrast: match the first step, compare the last
    x = math.log(diag[0] / diag[1]) / (2 * 3 - 1 * 2)
    hk4 = diag[0] * math.exp(-x * (4 * 5 - 1 * 2))
    print(f"    heat kernel matched on j = 1 -> 2 predicts "
          f"c(4,4)/c00 = {hk4:.3f}; actual {diag[3]:.3f}")
    assert diag[3] > 1.5 * hk4
    print()
    print("  BARRETT-CRANE'S SIMPLE REPRESENTATIONS EMERGE SOFTLY --")
    print("  the balanced diagonal dominates -- with a HEAVY tail:")
    print("  slower than any heat kernel, the tau-lesson at the")
    print("  nonabelian tier.")


# =====================================================================
# 3. the sign problem arrives
# =====================================================================

def verify_sign_problem() -> None:
    keys = [(0, 0), (1, 0), (2, 0), (1, 1)]
    print("    chord lift, c(1,0)/c00 and c(2,0)/c00 vs eps:")
    tr = {}
    for eps in (1.0, 0.3, 0.1, 0.03, 0.01, 0.003):
        C = dual_coeffs(eps, keys)
        r10 = C[(1, 0)] / C[(0, 0)]
        r20 = C[(2, 0)] / C[(0, 0)]
        tr[eps] = (r10, r20)
        print(f"      eps = {eps:6.3f}: c(1,0) {r10:+.5f}   "
              f"c(2,0) {r20:+.5f}")
    assert tr[0.3][0] > 0 and tr[0.01][0] < 0        # crossing
    assert all(tr[e][1] < 0 for e in (1.0, 0.1, 0.01))
    Ca = dual_coeffs(0.01, keys, lift="angle", ng=300)
    ra10 = Ca[(1, 0)] / Ca[(0, 0)]
    ra20 = Ca[(2, 0)] / Ca[(0, 0)]
    print(f"    angle lift at eps = 0.01: c(1,0) {ra10:+.5f}, "
          f"c(2,0) {ra20:+.5f}")
    assert ra20 < 0
    C6 = dual_coeffs(0.01, [(0, 0), (1, 0)], ng=600)
    stab = abs(C6[(1, 0)] / C6[(0, 0)] - tr[0.01][0])
    print(f"    grid stability NG 400 -> 600: shift {stab:.1e}")
    assert stab < 1e-4
    print()
    print("  THE WEIGHT IS POINTWISE POSITIVE BUT NOT")
    print("  CHARACTER-POSITIVE, in both lifts, grid-stable: the")
    print("  Osterwalder-Seiler route to a positive transfer matrix")
    print("  fails for the naive one-plaquette lift.  The sign")
    print("  problem -- the disease interacting quantum-gravity")
    print("  measures die of -- met on schedule at the wall.")


# =====================================================================
# 4. the cure has the ledger's shape
# =====================================================================

def verify_cure_shape() -> None:
    # U(1) reference: the derived continuum ledger's dual is
    # tau = 1*1, a Dirichlet square, hence >= 0 -- recomputed here.
    def divisors(n):
        return [d for d in range(1, n + 1) if n % d == 0]
    taus = [len(divisors(n)) for n in range(1, 25)]
    assert all(t > 0 for t in taus)
    sq = [sum(1 for d in divisors(n)) for n in range(1, 25)]
    assert taus == sq
    print("    U(1) reference: dual ledger tau(n) = (1*1)(n) > 0 for")
    print("    all n -- a Dirichlet SQUARE is coefficient-positive by")
    print("    construction (checked n <= 24)")
    print()
    print("  A NONABELIAN WEIGHT BUILT AS A DUAL SQUARE HAS CHARACTER")
    print("  COEFFICIENTS (amplitude)^2 >= 0 AUTOMATICALLY.  The naive")
    print("  kernel lift is not that object, and its negativity says")
    print("  the kernel alone was never the whole weight: A2's disease")
    print("  independently demands 0064 open 1 -- the nonabelian")
    print("  Dirichlet square.  The next stone is forced, not chosen.")


def run_verification_suite() -> None:
    sections = [
        ("The center is blind", verify_center_blind),
        ("The simple representations dominate, heavy-tailed",
         verify_simple_dominance),
        ("The sign problem arrives", verify_sign_problem),
        ("The cure has the ledger's shape", verify_cure_shape),
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
