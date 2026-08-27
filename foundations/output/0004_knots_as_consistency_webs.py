"""Knots as consistency webs: interactions as crossings, curvature as
defect holonomy.

The proposal under test (from the arithmetic-bridge thread):
interactions are topological -- each interaction adds a crossing to a
knot-like structure -- and perceived curvature is the holonomy of
loops around those crossings.  Four computations:

  s1  A KNOT DIAGRAM *IS* A CONSISTENCY WEB.  Arcs = channels;
      each crossing = a three-channel interaction constraint
      (2*over = under_in + under_out mod p).  Global sections =
      Fox p-colorings = flat dihedral connections on the knot
      complement.  Computed from Gauss codes by exact elimination:
      the unknot admits only the p trivial sections at every p;
      the trefoil opens extra sections exactly at p = 3 (9), the
      figure-eight and cinquefoil at p = 5 (25 each), the granny at
      p = 3 (27, distinguishing it from the trefoil).

  s2  THE INVARIANT LIVES ON THE DOUBLE COVER.  The modulus where
      extra sections appear divides the knot determinant
      |Delta(-1)| = |H1(branched DOUBLE cover)| -- the knot's tax is
      counted on its second loop, exactly like the paradox tax of
      the arithmetic frame.  Verified against the torus-knot
      Alexander polynomial by exact polynomial division:
      det T(2,3) = 3, T(2,5) = 5, T(2,7) = 7 -- and det T(3,5) = 1:
      a NONTRIVIAL knot whose abelian holonomy shadow vanishes.
      Knot detection therefore NEEDS nonabelian holonomy (the
      braided tier); Kronheimer-Mrowka's theorem (every nontrivial
      knot admits irreducible SU(2) representations) is the
      literature statement that the nonabelian level never misses.

  s3  DISCRETE BIANCHI: CURVATURE CANCELS IN THE BULK.  On a closed
      surface every edge borders exactly two faces, so the product
      of all face holonomies of ANY Z2 connection is +1 -- the same
      two-ends cancellation as the knot counter's full loop and the
      chord diagram's built-in double cover.  Verified on the
      octahedron over random sign assignments.

  s4  FLAT BUT HOLONOMIED: TOPOLOGICAL "CURVATURE".  On a 3x3 torus
      grid, connections that are FLAT on every face still fall into
      |H1(T^2; Z2)| = 4 gauge classes (computed by exact GF(2)
      ranks): perceived curvature around non-contractible loops
      with zero local curvature everywhere -- the Aharonov-Bohm /
      conical-defect configuration.  "You must perceive curvature
      around the loop" is consistent with "no curvature anywhere
      you travel": holonomy is the primitive, curvature its local
      density -- and it can be entirely concentrated at defects
      (in 2+1 gravity: at the particles themselves).

Run directly for the verification suite.
"""

from __future__ import annotations

import itertools
import random


# ---------------------------------------------------------------------
# s1: Fox colorings straight from Gauss codes
# ---------------------------------------------------------------------

UNKNOT = [(1, 'O'), (1, 'U')]
TREFOIL = [(1, 'O'), (2, 'U'), (3, 'O'), (1, 'U'), (2, 'O'), (3, 'U')]
FIGURE8 = [(1, 'O'), (2, 'U'), (3, 'O'), (4, 'U'),
           (2, 'O'), (1, 'U'), (4, 'O'), (3, 'U')]
CINQUEFOIL = [(1, 'O'), (2, 'U'), (3, 'O'), (4, 'U'), (5, 'O'),
              (1, 'U'), (2, 'O'), (3, 'U'), (4, 'O'), (5, 'U')]
GRANNY = TREFOIL + [(c + 3, kind) for c, kind in TREFOIL]


def crossings_from_gauss(code):
    """Arcs are cut after each under-visit; each crossing yields the
    constraint triple (over_arc, in_arc, out_arc)."""
    n = len(code)
    arc_of = {}
    arc = 0
    for pos in range(n):
        arc_of[pos] = arc
        if code[pos][1] == 'U':
            arc += 1
    arcs = arc
    arc_map = {pos: arc_of[pos] % arcs for pos in range(n)}
    triples = []
    over_pos = {c: p for p, (c, k) in enumerate(code) if k == 'O'}
    for pos, (c, kind) in enumerate(code):
        if kind != 'U':
            continue
        incoming = arc_map[pos]
        outgoing = (arc_map[pos] + 1) % arcs
        triples.append((arc_map[over_pos[c]], incoming, outgoing))
    return arcs, triples


def coloring_count(code, p):
    """Number of Fox p-colorings: solutions of 2*over = in + out."""
    arcs, triples = crossings_from_gauss(code)
    rows = []
    for over, inc, out in triples:
        row = [0] * arcs
        row[over] = (row[over] + 2) % p
        row[inc] = (row[inc] - 1) % p
        row[out] = (row[out] - 1) % p
        rows.append(row)
    rank = 0
    for col in range(arcs):
        piv = next((r for r in range(rank, len(rows)) if rows[r][col]),
                   None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        inv = pow(rows[rank][col], -1, p)
        rows[rank] = [(x * inv) % p for x in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][col]:
                f = rows[r][col]
                rows[r] = [(x - f * y) % p
                           for x, y in zip(rows[r], rows[rank])]
        rank += 1
    return p ** (arcs - rank)


def verify_the_web_reading() -> None:
    knots = [("unknot", UNKNOT), ("trefoil", TREFOIL),
             ("figure-eight", FIGURE8), ("cinquefoil", CINQUEFOIL),
             ("granny", GRANNY)]
    primes = (2, 3, 5, 7)
    expected_first = {"unknot": None, "trefoil": 3, "figure-eight": 5,
                      "cinquefoil": 5, "granny": 3}
    print(f"    {'knot':<14} " +
          " ".join(f"p={p:<4}" for p in primes) + "  first nontrivial")
    for name, code in knots:
        counts = [coloring_count(code, p) for p in primes]
        first = next((p for p, c in zip(primes, counts) if c > p), None)
        assert first == expected_first[name], name
        print(f"    {name:<14} " +
              " ".join(f"{c:<6}" for c in counts) +
              f"  {first if first else '—'}")
    assert coloring_count(TREFOIL, 3) == 9
    assert coloring_count(FIGURE8, 5) == 25
    assert coloring_count(CINQUEFOIL, 5) == 25
    assert coloring_count(GRANNY, 3) == 27       # ≠ trefoil's 9
    print()
    print("  A knot diagram is a consistency web in the arithmetic")
    print("  frame's exact sense: arcs are channels, each crossing an")
    print("  interaction constraint 2*over = in + out, and global")
    print("  sections are Fox colorings = flat dihedral connections on")
    print("  the knot complement.  Extra sections open exactly at the")
    print("  moduli of the knot's holonomy; the counts distinguish the")
    print("  granny from the trefoil.")


# ---------------------------------------------------------------------
# s2: the invariant lives on the double cover; abelian shadows vanish
# ---------------------------------------------------------------------

def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_div_exact(num, den):
    num = num[:]
    out = [0] * (len(num) - len(den) + 1)
    for shift in range(len(num) - len(den), -1, -1):
        coef = num[shift + len(den) - 1] // den[-1]
        out[shift] = coef
        for i, d in enumerate(den):
            num[shift + i] -= coef * d
    assert all(x == 0 for x in num), "non-exact division"
    return out


def torus_knot_determinant(p, q):
    """|Delta_{T(p,q)}(-1)| via exact polynomial arithmetic:
    Delta = (t^{pq}-1)(t-1) / ((t^p-1)(t^q-1))."""
    def cyc(n):
        return [-1] + [0] * (n - 1) + [1]        # t^n - 1
    numerator = poly_mul(cyc(p * q), cyc(1))
    delta = poly_div_exact(poly_div_exact(numerator, cyc(p)), cyc(q))
    value = sum(c * (-1) ** i for i, c in enumerate(delta))
    return abs(value)


def verify_the_double_cover_invariant() -> None:
    dets = {(2, 3): 3, (2, 5): 5, (2, 7): 7, (3, 5): 1}
    print(f"    {'torus knot':<12} {'det = |Delta(-1)|':>18}")
    for (p, q), expected in dets.items():
        d = torus_knot_determinant(p, q)
        assert d == expected, (p, q, d)
        print(f"    T({p},{q}){'':<6} {d:>18}")
    assert torus_knot_determinant(2, 3) == 3     # matches trefoil s1
    assert torus_knot_determinant(2, 5) == 5     # matches cinquefoil
    print()
    print("  The modulus where a knot's web gains extra sections")
    print("  divides det = |Delta(-1)| = |H1 of the BRANCHED DOUBLE")
    print("  COVER|: the knot's tax is counted on its second loop,")
    print("  like the paradox tax of the arithmetic frame.  And")
    print("  T(3,5) has det 1: a nontrivial knot whose entire abelian")
    print("  holonomy shadow vanishes.  Detecting every knot requires")
    print("  NONABELIAN holonomy -- the braided tier -- and the")
    print("  literature closes the loop: every nontrivial knot admits")
    print("  irreducible SU(2) representations (Kronheimer-Mrowka).")


# ---------------------------------------------------------------------
# s3: discrete Bianchi on a closed surface
# ---------------------------------------------------------------------

OCTA_FACES = [(0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1),
              (5, 2, 1), (5, 3, 2), (5, 4, 3), (5, 1, 4)]


def verify_discrete_bianchi(trials=300, seed=64001) -> None:
    edges = sorted({frozenset(e) for f in OCTA_FACES
                    for e in zip(f, f[1:] + f[:1])})
    incidence = {e: sum(e <= frozenset(f) for f in OCTA_FACES)
                 for e in edges}
    assert all(v == 2 for v in incidence.values())
    rng = random.Random(seed)
    for _ in range(trials):
        sign = {e: rng.choice((1, -1)) for e in edges}
        product = 1
        for f in OCTA_FACES:
            hol = 1
            for e in zip(f, f[1:] + f[:1]):
                hol *= sign[frozenset(e)]
            product *= hol
        assert product == 1
    print(f"    octahedron: every edge borders exactly 2 faces; over")
    print(f"    {trials} random Z2 connections the product of all face")
    print(f"    holonomies is +1, always.")
    print()
    print("  Discrete Bianchi identity: bulk curvature cancels because")
    print("  each edge is shared by two faces -- the same two-ends")
    print("  cancellation as the knot counter's full loop and the")
    print("  chord diagram's double cover.  Total curvature is a")
    print("  boundary/topology term, never a bulk sum.")


# ---------------------------------------------------------------------
# s4: flat but holonomied -- topological curvature on the torus
# ---------------------------------------------------------------------

def gf2_rank(rows):
    rows = [r[:] for r in rows]
    n = len(rows[0]) if rows else 0
    rank = 0
    for col in range(n):
        piv = next((r for r in range(rank, len(rows))
                    if rows[r][col]), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        for r in range(len(rows)):
            if r != rank and rows[r][col]:
                rows[r] = [x ^ y for x, y in zip(rows[r], rows[rank])]
        rank += 1
    return rank


def verify_topological_curvature(n=3) -> None:
    vertices = [(i, j) for i in range(n) for j in range(n)]
    edges = []
    for i, j in vertices:
        edges.append(((i, j), ((i + 1) % n, j)))
        edges.append(((i, j), (i, (j + 1) % n)))
    eidx = {e: k for k, e in enumerate(edges)}

    def edge(a, b):
        return eidx[(a, b)] if (a, b) in eidx else eidx[(b, a)]
    faces = []
    for i, j in vertices:
        a, b = (i, j), ((i + 1) % n, j)
        c, d = ((i + 1) % n, (j + 1) % n), (i, (j + 1) % n)
        row = [0] * len(edges)
        for u, v in ((a, b), (b, c), (d, c), (a, d)):
            row[edge(u, v)] ^= 1
        faces.append(row)
    gauge = []
    for v in vertices:
        row = [0] * len(edges)
        for k, (x, y) in enumerate(edges):
            if v in (x, y):
                row[k] ^= 1
        gauge.append(row)
    E = len(edges)
    face_rank = gf2_rank(faces)
    gauge_rank = gf2_rank(gauge)
    flat = 2 ** (E - face_rank)
    classes = flat // 2 ** gauge_rank
    assert face_rank == n * n - 1 and gauge_rank == n * n - 1
    assert classes == 4
    print(f"    {n}x{n} torus grid: {E} edges, {n * n} faces "
          f"(rank {face_rank}), gauge rank {gauge_rank}")
    print(f"    flat-on-every-face connections: 2^{E - face_rank}; "
          f"gauge classes: {classes} = |H1(T^2; Z2)|")
    print()
    print("  Four inequivalent connections are flat EVERYWHERE yet")
    print("  carry holonomy around the torus's two non-contractible")
    print("  loops: perceived curvature with zero local curvature --")
    print("  the Aharonov-Bohm / conical-defect configuration.")
    print("  Holonomy is the primitive; curvature is its local")
    print("  density; and it can vanish everywhere you travel while")
    print("  the loop still turns you.  In 2+1 gravity this is not an")
    print("  analogy: matter IS conical defects, spacetime is flat")
    print("  away from them, and gravity is pure loop holonomy")
    print("  (Deser-Jackiw-'t Hooft; Witten's Chern-Simons form).")


def run_verification_suite() -> None:
    sections = [
        ("A knot diagram is a consistency web", verify_the_web_reading),
        ("The invariant lives on the double cover; abelian shadows "
         "can vanish", verify_the_double_cover_invariant),
        ("Discrete Bianchi: bulk curvature cancels",
         verify_discrete_bianchi),
        ("Flat but holonomied: topological curvature",
         verify_topological_curvature),
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
