"""Cocycle localization: the surface invariant is forced to live at
the interactions.

The movie synthesis says all recoverable knowledge concentrates on
the singular set (double curves, triple points) of the projection.
This module derives the cohomological version from the axioms alone
-- no recalled cocycles, everything solved by elimination:

  s1  QUANDLE MACHINERY, VALIDATED.  The dihedral quandle R3
      (x <| y = 2y - x mod 3) passes the quandle axioms, and quandle
      colorings of Gauss codes reproduce the Fox coloring counts of
      exploration 0011 (trefoil 9, figure-eight 3 at p = 3).

  s2  THE COHOMOLOGY LADDER, SOLVED.  The quandle coboundary
      operator is implemented generically; delta o delta = 0 is
      verified exhaustively.  For R3 with Z3 coefficients, exact
      elimination gives

          H^2_Q(R3; Z3)  =  0        (no double-point invariant)
          H^3_Q(R3; Z3)  /=  0       (a triple-point invariant exists)

      For 2-knots, 2-cocycles weight DOUBLE CURVES and 3-cocycles
      weight TRIPLE POINTS (CJKLS state sums).  So for the dihedral
      color structure the invariant CANNOT be seen at double curves
      and CAN at triple points: "the knowledge lives at the
      interactions" is a computed statement about where nontrivial
      cohomology sits.

  s3  THE LEVEL-1 STATE SUM WORKS, AND DEGENERACY IS WHY.  With the
      4-element Alexander quandle over GF(4), H^2_Q is computed
      nonzero; the derived nontrivial 2-cocycle gives a state sum
      that is unchanged by adding a kink (Reidemeister I) and
      separates the trefoil from the unknot.  A RACK cocycle that
      violates the degeneracy condition (constant 1) satisfies the
      cocycle equation yet CHANGES under a kink -- the quandle
      degeneracy axiom is precisely the R1 invariance, demonstrated
      by measurement.

  s4  LEVEL 2, REGISTERED.  The published state-sum value for the
      2-twist-spun trefoil (CJKLS; Satoh-Shima) uses exactly the
      H^3 class whose existence s2 derives, and distinguishes the
      2-knot from its orientation reverse via triple points.
      Recomputing it needs an explicit broken surface diagram --
      cited, not recomputed; s2 supplies the engine, not the value.

Run directly for the verification suite.
"""

from __future__ import annotations

import itertools
from collections import Counter


# =====================================================================
# generic finite quandles and mod-p linear algebra
# =====================================================================

def dihedral_quandle(p):
    elems = list(range(p))
    op = {(x, y): (2 * y - x) % p for x in elems for y in elems}
    return elems, op


def alexander_gf4_quandle():
    """GF(4) = {0,1,t,t+1} with x <| y = t*x + (1+t)*y, t^2 = t+1.
    Elements encoded 0..3 as bit pairs (lo = 1-part, hi = t-part)."""
    TAB = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]
    t, one = 2, 1
    elems = [0, 1, 2, 3]
    op = {}
    for x in elems:
        for y in elems:
            op[(x, y)] = TAB[t][x] ^ TAB[t ^ one][y]   # t*x + (1+t)*y
    return elems, op


def check_quandle(elems, op):
    for x in elems:
        assert op[(x, x)] == x                        # idempotent
    for x in elems:
        for y in elems:
            solutions = [z for z in elems if op[(z, y)] == x]
            assert len(solutions) == 1                # right-invertible
    for x in elems:
        for y in elems:
            for z in elems:
                left = op[(op[(x, y)], z)]
                right = op[(op[(x, z)], op[(y, z)])]
                assert left == right                  # self-distributive


def solve_mod(rows, p):
    """Row-reduce over Z_p; returns (rank, pivots, reduced rows)."""
    rows = [r[:] for r in rows]
    n = len(rows[0]) if rows else 0
    rank, pivots = 0, []
    for col in range(n):
        piv = next((r for r in range(rank, len(rows))
                    if rows[r][col] % p), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        inv = pow(rows[rank][col], -1, p)
        rows[rank] = [(v * inv) % p for v in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][col] % p:
                f = rows[r][col]
                rows[r] = [(a - f * b) % p
                           for a, b in zip(rows[r], rows[rank])]
        rank += 1
        pivots.append(col)
    return rank, pivots, rows


# =====================================================================
# quandle cochain complex (degenerate = quandle, else rack)
# =====================================================================

def tuples_no_consecutive_equal(elems, n):
    out = []
    for t in itertools.product(elems, repeat=n):
        if all(t[i] != t[i + 1] for i in range(n - 1)):
            out.append(t)
    return out


def coboundary_matrix(elems, op, n, quandle=True):
    """Matrix of delta: C^n -> C^(n+1).
    (delta f)(x1..x_{n+1}) = sum_{i=2}^{n+1} (-1)^i [ f(..omit x_i..)
        - f(x1<|x_i, .., x_{i-1}<|x_i, x_{i+1}, ..) ]."""
    dom = tuples_no_consecutive_equal(elems, n) if quandle \
        else list(itertools.product(elems, repeat=n))
    cod = tuples_no_consecutive_equal(elems, n + 1) if quandle \
        else list(itertools.product(elems, repeat=n + 1))
    dom_index = {t: i for i, t in enumerate(dom)}
    rows = []
    for target in cod:
        row = [0] * len(dom)
        for i in range(2, n + 2):                     # position of x_i
            sign = 1 if i % 2 == 0 else -1
            omitted = target[:i - 1] + target[i:]
            acted = tuple(op[(target[j], target[i - 1])]
                          for j in range(i - 1)) + target[i:]
            for tup, s in ((omitted, sign), (acted, -sign)):
                if tup in dom_index:
                    row[dom_index[tup]] += s
        rows.append(row)
    return dom, cod, rows


def cohomology_dims(elems, op, n, p):
    """dim Z^n, dim B^n, dim H^n of the quandle complex mod p."""
    dom_n, _, delta_n = coboundary_matrix(elems, op, n)
    rank_n = solve_mod(delta_n, p)[0] if dom_n else 0
    z_dim = len(dom_n) - rank_n
    if n >= 2:
        dom_prev, _, delta_prev = coboundary_matrix(elems, op, n - 1)
        b_dim = solve_mod(delta_prev, p)[0] if dom_prev else 0
    else:
        b_dim = 0
    return z_dim, b_dim, z_dim - b_dim


def nontrivial_cocycle(elems, op, n, p):
    """A cocycle not in the coboundary image, as a dict, or None."""
    dom, _, delta_n = coboundary_matrix(elems, op, n)
    dom_prev, cod_prev, delta_prev = coboundary_matrix(elems, op, n - 1)
    assert cod_prev == dom
    # kernel basis of delta_n
    rank, pivots, reduced = solve_mod(delta_n, p)
    free = [c for c in range(len(dom)) if c not in pivots]
    kernel = []
    for fc in free:
        vec = [0] * len(dom)
        vec[fc] = 1
        for r, col in enumerate(pivots):
            vec[col] = (-reduced[r][fc]) % p
        kernel.append(vec)
    # image = column space of delta_prev (as vectors over cod_prev)
    image_rows = [[delta_prev[i][j] for i in range(len(dom))]
                  for j in range(len(dom_prev))]
    base_rank = solve_mod(image_rows, p)[0] if dom_prev else 0
    for vec in kernel:
        if solve_mod(image_rows + [vec], p)[0] > base_rank:
            return {t: vec[i] for i, t in enumerate(dom)}
    return None


# =====================================================================
# 1. machinery validation against 0011
# =====================================================================

TREFOIL = [(1, 'O', 1), (2, 'U', 1), (3, 'O', 1),
           (1, 'U', 1), (2, 'O', 1), (3, 'U', 1)]
FIGURE8 = [(1, 'O', 1), (2, 'U', -1), (3, 'O', 1), (4, 'U', -1),
           (2, 'O', -1), (1, 'U', 1), (4, 'O', -1), (3, 'U', 1)]
UNKNOT_KINK = [(1, 'O', 1), (1, 'U', 1)]
TREFOIL_KINK = TREFOIL + [(4, 'O', 1), (4, 'U', 1)]


def arcs_and_crossings(code):
    n = len(code)
    arc_of, arc = {}, 0
    for pos in range(n):
        arc_of[pos] = arc
        if code[pos][1] == 'U':
            arc += 1
    arcs = arc
    amap = {pos: arc_of[pos] % arcs for pos in range(n)}
    over_pos = {c: p for p, (c, k, s) in enumerate(code) if k == 'O'}
    triples = []
    for pos, (c, kind, sign) in enumerate(code):
        if kind != 'U':
            continue
        triples.append((amap[over_pos[c]], amap[pos],
                        (amap[pos] + 1) % arcs, sign))
    return arcs, triples


def colorings(code, elems, op):
    arcs, triples = arcs_and_crossings(code)
    out = []
    for assign in itertools.product(elems, repeat=arcs):
        if all(op[(assign[i], assign[ov])] == assign[o]
               for ov, i, o, s in triples):
            out.append(assign)
    return out


def verify_machinery() -> None:
    r3, op3 = dihedral_quandle(3)
    check_quandle(r3, op3)
    gf4, op4 = alexander_gf4_quandle()
    check_quandle(gf4, op4)
    tre = len(colorings(TREFOIL, r3, op3))
    fig = len(colorings(FIGURE8, r3, op3))
    assert tre == 9 and fig == 3, (tre, fig)
    print("    dihedral R3 and Alexander GF(4) pass the quandle axioms;")
    print("    quandle colorings reproduce 0011's Fox counts")
    print(f"    (trefoil {tre}, figure-eight {fig} at p = 3).")


# =====================================================================
# 2. the cohomology ladder
# =====================================================================

def verify_the_ladder() -> None:
    r3, op3 = dihedral_quandle(3)
    # implementation check: delta o delta = 0 on the quandle complex
    for n in (1, 2):
        dom, cod, d1 = coboundary_matrix(r3, op3, n)
        _, cod2, d2 = coboundary_matrix(r3, op3, n + 1)
        for j in range(len(dom)):
            vec = [d1[i][j] for i in range(len(cod))]
            image = [sum(d2[i][k] * vec[k] for k in range(len(cod))) % 3
                     for i in range(len(cod2))]
            assert all(v == 0 for v in image), n
    z2, b2, h2 = cohomology_dims(r3, op3, 2, 3)
    z3, b3, h3 = cohomology_dims(r3, op3, 3, 3)
    print(f"    delta o delta = 0 verified exhaustively (n = 1, 2)")
    print(f"    H^2_Q(R3; Z3):  dim Z = {z2}, dim B = {b2},  "
          f"dim H = {h2}")
    print(f"    H^3_Q(R3; Z3):  dim Z = {z3}, dim B = {b3},  "
          f"dim H = {h3}")
    assert h2 == 0 and h3 >= 1, (h2, h3)
    theta = nontrivial_cocycle(r3, op3, 3, 3)
    assert theta is not None
    shown = {t: v for t, v in theta.items() if v}
    print(f"    nontrivial 3-cocycle derived by elimination "
          f"({len(shown)} nonzero values)")
    print()
    print("  For 2-knot state sums, 2-cocycles weight DOUBLE CURVES and")
    print("  3-cocycles weight TRIPLE POINTS.  With dihedral colors the")
    print("  double-curve layer has NO invariant content (H^2 = 0) and")
    print("  the triple-point layer does (H^3 /= 0): the invariant is")
    print("  cohomologically FORCED onto the interactions.")


# =====================================================================
# 3. the level-1 state sum, and why degeneracy = R1
# =====================================================================

def state_sum(code, elems, op, phi, p):
    """Multiset of total weights sum(eps * phi(under_in, over)) mod p
    over all colorings."""
    arcs, triples = arcs_and_crossings(code)
    totals = Counter()
    for assign in itertools.product(elems, repeat=arcs):
        if not all(op[(assign[i], assign[ov])] == assign[o]
                   for ov, i, o, s in triples):
            continue
        w = 0
        for ov, i, o, s in triples:
            w = (w + s * phi.get((assign[i], assign[ov]), 0)) % p
        totals[w] += 1
    return dict(totals)


def verify_state_sum() -> None:
    gf4, op4 = alexander_gf4_quandle()
    z2, b2, h2 = cohomology_dims(gf4, op4, 2, 2)
    print(f"    H^2_Q(GF4 Alexander; Z2): dim Z = {z2}, dim B = {b2}, "
          f"dim H = {h2}")
    assert h2 >= 1
    phi = nontrivial_cocycle(gf4, op4, 2, 2)
    assert phi is not None
    plain = state_sum(TREFOIL, gf4, op4, phi, 2)
    kinked = state_sum(TREFOIL_KINK, gf4, op4, phi, 2)
    unknot = state_sum(UNKNOT_KINK, gf4, op4, phi, 2)
    assert plain == kinked, (plain, kinked)
    print(f"    trefoil state sum        {plain}")
    print(f"    trefoil + kink           {kinked}   (identical: R1-safe)")
    print(f"    unknot                   {unknot}")
    assert plain != unknot
    # a rack cocycle violating degeneracy breaks R1
    rack_phi = {(x, y): 1 for x in gf4 for y in gf4}
    r_plain = state_sum(TREFOIL, gf4, op4, rack_phi, 2)
    r_kink = state_sum(TREFOIL_KINK, gf4, op4, rack_phi, 2)
    assert r_plain != r_kink, (r_plain, r_kink)
    print(f"    with a rack cocycle (phi(x,x) /= 0): trefoil {r_plain}")
    print(f"      vs + kink {r_kink} -- DIFFERENT: the quandle")
    print(f"      degeneracy axiom is exactly Reidemeister-I safety,")
    print(f"      demonstrated by measurement.")
    print()
    print("  The derived (not recalled) nontrivial 2-cocycle separates")
    print("  the trefoil from the unknot and survives diagram moves;")
    print("  its level-2 sibling -- the H^3 class of s2 evaluated at")
    print("  triple points -- is the published invariant that")
    print("  distinguishes the 2-twist-spun trefoil from its reverse")
    print("  (CJKLS, Satoh-Shima; cited, not recomputed: it needs an")
    print("  explicit broken surface diagram).")


def run_verification_suite() -> None:
    sections = [
        ("Machinery validated against 0011", verify_machinery),
        ("The cohomology ladder: H^2 = 0, H^3 /= 0 for R3",
         verify_the_ladder),
        ("The state sum works, and degeneracy is R1",
         verify_state_sum),
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
