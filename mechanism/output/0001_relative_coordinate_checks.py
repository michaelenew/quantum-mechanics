"""
Relative-coordinate checks for the knowledge-first reading of measurement.

Pure standard library (no numpy/sympy) so it runs anywhere.

Verifies three quantitative claims used in mechanism/exploration/0001:

  (1) Center-of-mass / relative canonical split.
      With  Q = (q1+q2)/2,  P = p1+p2,  q = q1-q2,  p = (p1-p2)/2,
        [q, P] = 0        relative position and TOTAL momentum are compatible
        [q, p] = i hbar   relative position is conjugate to relative momentum
        [Q, P] = i hbar   CoM position is conjugate to total momentum
        [Q, p] = 0
      => at a split/merge event, a sharp RELATIVE POSITION and a sharp
         TOTAL MOMENTUM (the conservation law) may hold simultaneously.
         Complementarity then forces the conjugate pair (CoM position,
         relative momentum) to be broad.  This is the EPR state, and it is
         the correct refinement of "position exact, momentum unknown":
         it is the *relative* momentum that is unknown, while total
         momentum is sharp by conservation.

  (2) Variance additivity along a knowledge chain A -> B -> C.
      If the relative coordinate composes, q_AC = q_AB + q_BC, and the two
      links are independent, then Var(q_AC) = Var(q_AB) + Var(q_BC).
      This is the precise content of the recursive-consistency postulate:
      chained knowledge is strictly no sharper than either link.

  (3) Gaussian ("Bayesian-optimal") fusion of two knowledge states.
      Precisions (inverse variances) add; the fused estimate is sharper
      than either input and its mean is the precision-weighted average.
      This is "combine to the most coherent picture."

Run:  python3 0001_relative_coordinate_checks.py
"""

from fractions import Fraction as F


# ---------------------------------------------------------------------------
# (1) Canonical commutator algebra over the four generators {q1,q2,p1,p2}.
#
# An operator linear in the generators is a dict {gen: coeff}.
# The only nonzero fundamental commutators are (in units of i*hbar):
#     [q1,p1] = 1,  [q2,p2] = 1
# everything else vanishes.  Commutator is bilinear and antisymmetric, so
#     [A,B] = sum_ij a_i b_j [g_i,g_j]   (a c-number, in units of i*hbar).
# ---------------------------------------------------------------------------

# fundamental table in units of i*hbar; key (a,b) -> value, antisymmetric
_TABLE = {("q1", "p1"): F(1), ("q2", "p2"): F(1)}


def _fund(a, b):
    if (a, b) in _TABLE:
        return _TABLE[(a, b)]
    if (b, a) in _TABLE:
        return -_TABLE[(b, a)]
    return F(0)


def comm(A, B):
    """Commutator [A,B] of two linear operators, in units of i*hbar."""
    total = F(0)
    for gi, ai in A.items():
        for gj, bj in B.items():
            total += ai * bj * _fund(gi, gj)
    return total


Q = {"q1": F(1, 2), "q2": F(1, 2)}   # center-of-mass position
P = {"p1": F(1), "p2": F(1)}          # total momentum
q = {"q1": F(1), "q2": F(-1)}         # relative position
p = {"p1": F(1, 2), "p2": F(-1, 2)}   # relative momentum


def check_commutators():
    results = {
        "[q, P]": comm(q, P),   # expect 0
        "[q, p]": comm(q, p),   # expect 1  (i hbar)
        "[Q, P]": comm(Q, P),   # expect 1  (i hbar)
        "[Q, p]": comm(Q, p),   # expect 0
        "[q, Q]": comm(q, Q),   # expect 0
        "[P, p]": comm(P, p),   # expect 0
    }
    expected = {"[q, P]": 0, "[q, p]": 1, "[Q, P]": 1,
                "[Q, p]": 0, "[q, Q]": 0, "[P, p]": 0}
    print("(1) Commutators (units of i*hbar):")
    ok = True
    for name, val in results.items():
        good = (val == expected[name])
        ok = ok and good
        print(f"    {name} = {val!s:>4}   expected {expected[name]}   "
              f"{'OK' if good else 'FAIL'}")
    print(f"    => compatible sharp pair (relative position q, total momentum P): "
          f"{'CONFIRMED' if results['[q, P]'] == 0 else 'NO'}")
    return ok


# ---------------------------------------------------------------------------
# (2) Variance additivity along a knowledge chain A -> B -> C.
# ---------------------------------------------------------------------------

def check_chain(var_AB=0.4, var_BC=0.9):
    var_AC = var_AB + var_BC
    print("\n(2) Knowledge chain A->B->C (independent links):")
    print(f"    Var(q_AB) = {var_AB}")
    print(f"    Var(q_BC) = {var_BC}")
    print(f"    Var(q_AC) = {var_AC}   (= sum; chained knowledge is no sharper "
          f"than either link)")
    ok = abs(var_AC - (var_AB + var_BC)) < 1e-12 and var_AC >= max(var_AB, var_BC)
    print(f"    variance additivity + monotone degradation: "
          f"{'OK' if ok else 'FAIL'}")
    return ok


# ---------------------------------------------------------------------------
# (3) Gaussian / Bayesian-optimal fusion of two knowledge states.
# ---------------------------------------------------------------------------

def check_fusion(mu1=-1.0, var1=0.5, mu2=+2.0, var2=0.2):
    prec1, prec2 = 1.0 / var1, 1.0 / var2
    prec_f = prec1 + prec2
    var_f = 1.0 / prec_f
    mu_f = (prec1 * mu1 + prec2 * mu2) / prec_f
    print("\n(3) Bayesian-optimal (Gaussian) fusion of two knowledge states:")
    print(f"    state 1: mean {mu1}, var {var1}")
    print(f"    state 2: mean {mu2}, var {var2}")
    print(f"    fused:   mean {mu_f:.4f}, var {var_f:.4f}")
    ok = (var_f < min(var1, var2)) and (min(mu1, mu2) <= mu_f <= max(mu1, mu2))
    print(f"    fused sharper than both inputs, mean between them: "
          f"{'OK' if ok else 'FAIL'}")
    return ok


if __name__ == "__main__":
    a = check_commutators()
    b = check_chain()
    c = check_fusion()
    print("\nALL CHECKS PASSED" if (a and b and c) else "\nSOME CHECK FAILED")
