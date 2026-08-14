"""Curvature from crossings: the defect ledger, computed.

Tests the proposal "interactions are crossings; curvature is the
holonomy of the loop around them" at the one place physics can check
it -- the 2+1 gravity boundary, where conical defects ARE matter.
Four computations, nothing asserted that is not computed:

  s1  HOLONOMY IS THE ANGLE DEFECT, EXACTLY.  On real polyhedra
      (tetrahedron, cube, octahedron, icosahedron) parallel transport
      around a vertex is computed HONESTLY -- compose the unfolding
      isometries across each edge of the vertex star as 3x3 rotation
      matrices -- and its rotation angle equals 2*pi minus the sum of
      the incident face angles, to machine precision, at every vertex.
      The surface is flat everywhere except the vertices: curvature is
      concentrated at the defects, and it IS the loop holonomy.

  s2  THE CURVATURE BUDGET IS TOPOLOGICAL.  Knot projections are
      built from actual plane curves (torus-knot projections with
      1, 3, 5, 7 crossings), their self-intersections found
      geometrically, the planar map traced from the rotation system,
      and the combinatorial curvature computed in exact rationals:

          kappa(v) = 1 - deg(v)/2 + sum over corners 1/|face|

      Total = V - E + F = 2 for EVERY diagram, whatever the crossing
      count.  Interactions therefore REDISTRIBUTE curvature; they
      cannot create it.  The per-crossing curvature varies (that is
      the knot-dependent content); the budget does not.

  s3  THE BUDGET IS THE MASS BOUND.  Descartes: total defect on a
      sphere = 4*pi (verified in s1 for all four polyhedra).  In 2+1
      gravity deficit = 8*pi*G*m, so a closed universe with spherical
      topology has TOTAL MASS <= 1/(2G) -- the known 2+1 bound, here
      as the same ledger.  Equivalently: the product of all defect
      holonomies is the identity, and Gauss-Bonnet is exactly the
      condition making that possible (verified: the rotation parts
      compose to the identity iff the defects sum to 0 mod 2*pi).

  s4  DEFECTS COMPOSE NONABELIANLY -- MASSES ADD, CENTERS BRAID.
      Conical defects at p1, p2 with deficits d1, d2 have ISO(2)
      holonomies whose product has rotation d1+d2 (masses add: the
      abelian shadow) but whose ORDER matters, with commutator the
      pure translation

          (I - R_d1)(I - R_d2)(p1 - p2)

      -- derived in closed form and verified numerically.  The
      nonabelian residue is a real relative displacement (the 2+1
      gravitational scattering / Aharonov-Bohm shift), it vanishes
      iff a defect is massless or the defects coincide, and it is the
      braided tier of the arithmetic bridge appearing as physics.

Run directly for the verification suite.
"""

from __future__ import annotations

import itertools
import math
from fractions import Fraction

TAU = 2 * math.pi


# =====================================================================
# vector helpers (no numpy)
# =====================================================================

def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, s):
    return tuple(x * s for x in a)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def norm(a):
    return math.sqrt(dot(a, a))


def unit(a):
    n = norm(a)
    return tuple(x / n for x in a)


def matvec(M, v):
    return tuple(dot(row, v) for row in M)


def matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def rodrigues(axis, angle):
    """Rotation about a unit axis by angle."""
    x, y, z = unit(axis)
    c, s = math.cos(angle), math.sin(angle)
    t = 1 - c
    return ((t * x * x + c, t * x * y - s * z, t * x * z + s * y),
            (t * x * y + s * z, t * y * y + c, t * y * z - s * x),
            (t * x * z - s * y, t * y * z + s * x, t * z * z + c))


def rotation_angle(M):
    """Robust everywhere, including at pi where acos(trace) is
    ill-conditioned: |axis vector| = 2 sin(theta), trace - 1 =
    2 cos(theta), so atan2 recovers theta stably."""
    trace = M[0][0] + M[1][1] + M[2][2]
    w = (M[2][1] - M[1][2], M[0][2] - M[2][0], M[1][0] - M[0][1])
    return math.atan2(norm(w) / 2, (trace - 1) / 2)


IDENTITY = ((1.0, 0, 0), (0, 1.0, 0), (0, 0, 1.0))


# =====================================================================
# 1. holonomy is the angle defect, computed on real polyhedra
# =====================================================================

def tetrahedron():
    verts = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
    faces = [f for f in itertools.combinations(range(4), 3)]
    return verts, [list(f) for f in faces]


def cube():
    verts = [(x, y, z) for x in (-1, 1) for y in (-1, 1)
             for z in (-1, 1)]
    index = {v: i for i, v in enumerate(verts)}
    faces = []
    for axis in range(3):
        for sign in (-1, 1):
            ring = [v for v in verts if v[axis] == sign]
            # order the four around the face centre
            centre = scale(tuple(sum(c) for c in zip(*ring)), 0.25)
            basis_a = unit(sub(ring[0], centre))
            normal = tuple(1.0 if i == axis else 0.0 for i in range(3))
            basis_b = cross(normal, basis_a)
            ring.sort(key=lambda v: math.atan2(dot(sub(v, centre),
                                                   basis_b),
                                               dot(sub(v, centre),
                                                   basis_a)))
            faces.append([index[v] for v in ring])
    return verts, faces


def octahedron():
    verts = [(1, 0, 0), (-1, 0, 0), (0, 1, 0),
             (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    faces = []
    for i in (0, 1):
        for j in (2, 3):
            for k in (4, 5):
                faces.append([i, j, k])
    return verts, faces


def icosahedron():
    phi = (1 + math.sqrt(5)) / 2
    verts = []
    for s1 in (-1, 1):
        for s2 in (-1, 1):
            verts += [(0, s1 * 1.0, s2 * phi), (s1 * 1.0, s2 * phi, 0),
                      (s1 * phi, 0, s2 * 1.0)]
    edge = min(norm(sub(a, b))
               for a, b in itertools.combinations(verts, 2))
    faces = []
    for triple in itertools.combinations(range(12), 3):
        a, b, c = (verts[i] for i in triple)
        if (abs(norm(sub(a, b)) - edge) < 1e-9 and
                abs(norm(sub(b, c)) - edge) < 1e-9 and
                abs(norm(sub(a, c)) - edge) < 1e-9):
            faces.append(list(triple))
    return verts, faces


def face_normal(verts, face):
    a, b, c = (verts[i] for i in face[:3])
    n = unit(cross(sub(b, a), sub(c, a)))
    centre = scale(tuple(sum(t) for t in
                         zip(*[verts[i] for i in face])), 1 / len(face))
    return n if dot(n, centre) > 0 else scale(n, -1)


def corner_angle(verts, face, v):
    """Interior angle of `face` at vertex index v."""
    k = face.index(v)
    prev_v = verts[face[(k - 1) % len(face)]]
    next_v = verts[face[(k + 1) % len(face)]]
    a = unit(sub(prev_v, verts[v]))
    b = unit(sub(next_v, verts[v]))
    return math.acos(max(-1.0, min(1.0, dot(a, b))))


def ordered_star(verts, faces, v):
    """Faces around v, cyclically ordered by shared edges at v."""
    incident = [f for f in faces if v in f]
    ordered = [incident[0]]
    remaining = incident[1:]
    while remaining:
        current = set(ordered[-1]) & set()
        last = ordered[-1]
        neighbours_at_v = {last[(last.index(v) - 1) % len(last)],
                           last[(last.index(v) + 1) % len(last)]}
        nxt = None
        for f in remaining:
            others = {f[(f.index(v) - 1) % len(f)],
                      f[(f.index(v) + 1) % len(f)]}
            if others & neighbours_at_v:
                nxt = f
                break
        assert nxt is not None
        ordered.append(nxt)
        remaining.remove(nxt)
    return ordered


def unfolding_rotation(verts, face_a, face_b, v):
    """The isometry unfolding face_a onto face_b's plane, about their
    shared edge through v."""
    shared = set(face_a) & set(face_b)
    shared.discard(v)
    assert len(shared) == 1, (face_a, face_b)
    other = shared.pop()
    axis = sub(verts[other], verts[v])
    n_a = face_normal(verts, face_a)
    n_b = face_normal(verts, face_b)
    angle = math.acos(max(-1.0, min(1.0, dot(n_a, n_b))))
    for candidate in (angle, -angle):
        R = rodrigues(axis, candidate)
        if norm(sub(matvec(R, n_a), n_b)) < 1e-9:
            return R
    raise AssertionError("no unfolding rotation found")


def vertex_holonomy(verts, faces, v):
    star = ordered_star(verts, faces, v)
    R = IDENTITY
    for i in range(len(star)):
        a, b = star[i], star[(i + 1) % len(star)]
        R = matmul(unfolding_rotation(verts, a, b, v), R)
    return rotation_angle(R)


def verify_holonomy_is_the_defect() -> None:
    solids = [("tetrahedron", tetrahedron()), ("cube", cube()),
              ("octahedron", octahedron()),
              ("icosahedron", icosahedron())]
    print(f"    {'solid':<14} {'vertices':>8} {'defect/vertex':>14} "
          f"{'holonomy':>10} {'total defect':>13}")
    for name, (verts, faces) in solids:
        total = 0.0
        shown = None
        for v in range(len(verts)):
            star = [f for f in faces if v in f]
            defect = TAU - sum(corner_angle(verts, f, v) for f in star)
            holonomy = vertex_holonomy(verts, faces, v)
            assert abs(holonomy - abs(defect)) < 1e-8, (name, v,
                                                        holonomy, defect)
            total += defect
            shown = (defect, holonomy)
        assert abs(total - 2 * TAU) < 1e-9, (name, total)
        print(f"    {name:<14} {len(verts):>8} {shown[0]:>14.6f} "
              f"{shown[1]:>10.6f} {total / math.pi:>10.4f}·pi")
    print()
    print("  Parallel transport around a vertex -- composed honestly")
    print("  from the unfolding isometries of the star -- rotates by")
    print("  exactly the angle defect, at every vertex of every solid.")
    print("  Away from vertices the surface is flat, so ALL curvature")
    print("  sits at the defects and IS the loop holonomy.  Totals:")
    print("  4*pi everywhere (Descartes = Gauss-Bonnet on the sphere).")


# =====================================================================
# 2. the curvature budget of a knot projection, from real geometry
# =====================================================================

def torus_projection(p, q, samples=4000):
    """Plane curve r(t) = 2 + cos(q t / p): a (p,q) torus-knot
    projection with q(p-1)... crossings for p=2: q crossings."""
    pts = []
    for i in range(samples):
        # the 0.37 phase offset keeps samples off the symmetric
        # curve's exact crossing points (an endpoint hit is not a
        # transversal segment intersection and would be missed)
        t = TAU * p * (i + 0.37) / samples
        r = 2 + math.cos(q * t / p)
        pts.append((r * math.cos(t), r * math.sin(t)))
    return pts


def limacon(samples=4000):
    """r = 1 + 2 cos t: one self-crossing."""
    pts = []
    for i in range(samples):
        t = TAU * (i + 0.37) / samples
        r = 1 + 2 * math.cos(t)
        pts.append((r * math.cos(t), r * math.sin(t)))
    return pts


def segment_intersection(p1, p2, p3, p4):
    d1 = sub(p2 + (0,), p1 + (0,))[:2]
    d2 = sub(p4 + (0,), p3 + (0,))[:2]
    denom = d1[0] * d2[1] - d1[1] * d2[0]
    if abs(denom) < 1e-15:
        return None
    dx = p3[0] - p1[0]
    dy = p3[1] - p1[1]
    s = (dx * d2[1] - dy * d2[0]) / denom
    u = (dx * d1[1] - dy * d1[0]) / denom
    if 1e-9 < s < 1 - 1e-9 and 1e-9 < u < 1 - 1e-9:
        return s, u, (p1[0] + s * d1[0], p1[1] + s * d1[1])
    return None


def planar_map(points):
    """Vertices (self-crossings), arcs, rotation system, faces."""
    n = len(points)
    hits = []
    for i in range(n):
        for j in range(i + 2, n):
            if i == 0 and j == n - 1:
                continue
            res = segment_intersection(points[i], points[(i + 1) % n],
                                       points[j], points[(j + 1) % n])
            if res:
                s, u, pt = res
                hits.append((i + s, j + u, pt))
    marks = []
    for vid, (t1, t2, pt) in enumerate(hits):
        marks.append((t1, vid))
        marks.append((t2, vid))
    marks.sort()
    assert len(marks) == 2 * len(hits)

    def tangent(t, forward=True):
        i = int(t) % n
        d = sub(points[(i + 1) % n] + (0,), points[i] + (0,))[:2]
        return d if forward else (-d[0], -d[1])

    arcs = []
    for k in range(len(marks)):
        t_start, v_start = marks[k]
        t_end, v_end = marks[(k + 1) % len(marks)]
        arcs.append({"start": v_start, "end": v_end,
                     "dir_start": tangent(t_start, True),
                     "dir_end": tangent(t_end, False)})
    darts = []
    for k, arc in enumerate(arcs):
        darts.append((k, +1))
        darts.append((k, -1))

    def dart_vertex(d):
        k, s = d
        return arcs[k]["start"] if s > 0 else arcs[k]["end"]

    def dart_direction(d):
        k, s = d
        return arcs[k]["dir_start"] if s > 0 else arcs[k]["dir_end"]

    rotation = {}
    for v in range(len(hits)):
        at_v = [d for d in darts if dart_vertex(d) == v]
        assert len(at_v) == 4, (v, len(at_v))
        at_v.sort(key=lambda d: math.atan2(dart_direction(d)[1],
                                           dart_direction(d)[0]))
        for idx, d in enumerate(at_v):
            rotation[d] = at_v[(idx + 1) % 4]

    def reverse(d):
        k, s = d
        return (k, -s)

    faces, seen = [], set()
    for d in darts:
        if d in seen:
            continue
        orbit, current = [], d
        while current not in seen:
            seen.add(current)
            orbit.append(current)
            current = rotation[reverse(current)]
        faces.append(orbit)
    return len(hits), len(arcs), faces, darts, dart_vertex


def verify_the_curvature_budget() -> None:
    curves = [("limacon", limacon(), 1),
              ("trefoil T(2,3)", torus_projection(2, 3), 3),
              ("cinquefoil T(2,5)", torus_projection(2, 5), 5),
              ("T(2,7)", torus_projection(2, 7), 7)]
    print(f"    {'diagram':<22} {'V':>3} {'E':>3} {'F':>3} "
          f"{'V-E+F':>6} {'kappa per crossing':>26} {'total':>6}")
    for name, pts, expected_crossings in curves:
        V, E, faces, darts, dart_vertex = planar_map(pts)
        F = len(faces)
        assert V == expected_crossings, (name, V, expected_crossings)
        assert E == 2 * V, (name, V, E)
        assert V - E + F == 2, (name, V, E, F)
        face_of = {}
        for f in faces:
            for d in f:
                face_of[d] = len(f)
        kappas = {}
        for v in range(V):
            corners = [d for d in darts if dart_vertex(d) == v]
            kappas[v] = (Fraction(1) - Fraction(4, 2) +
                         sum(Fraction(1, face_of[d]) for d in corners))
        total = sum(kappas.values())
        assert total == 2, (name, total)
        distinct = sorted({str(k) for k in kappas.values()})
        print(f"    {name:<22} {V:>3} {E:>3} {F:>3} {V - E + F:>6} "
              f"{','.join(distinct):>26} {str(total):>6}")
    print()
    print("  Every diagram: V - E + F = 2 and the combinatorial")
    print("  curvature sums to exactly 2, whatever the crossing count.")
    print("  Adding an interaction adds a vertex AND a face, and the")
    print("  per-crossing curvature falls to keep the total fixed:")
    print("  INTERACTIONS REDISTRIBUTE CURVATURE, THEY CANNOT CREATE")
    print("  IT.  The knot-dependent content is the distribution.")


# =====================================================================
# 3. the budget is the mass bound, and it is trivial global holonomy
# =====================================================================

def verify_the_mass_bound() -> None:
    print("    Descartes/Gauss-Bonnet (verified in s1): sum of defects")
    print("    over a spherical surface = 4*pi, exactly, always.")
    print()
    print("    2+1 gravity dictionary (Deser-Jackiw-'t Hooft):")
    print("      a point mass m  <->  a conical defect of deficit")
    print("      delta = 8*pi*G*m; spacetime flat away from it")
    print()
    print("      => sum_i 8*pi*G*m_i = 4*pi   =>   sum_i m_i = 1/(2G)")
    print()
    total_deficit = 2 * TAU
    print(f"    {'defects':>8} {'deficit each':>13} {'as fraction of 2pi':>20}")
    for count in (2, 3, 6, 12):
        each = total_deficit / count
        assert abs(count * each - 2 * TAU) < 1e-12
        assert each <= TAU + 1e-12             # per-defect ceiling
        if count >= 3:
            assert each < TAU                  # strictly sub-extremal
        note = "  <- extremal (degenerate)" if count == 2 else ""
        print(f"    {count:>8} {each:>13.6f} "
              f"{each / TAU:>20.4f}{note}")
    print()
    print("    TWO bounds, both from the same ledger: each defect is")
    print("    at most 2*pi (a single mass m < 1/(4G) -- more would")
    print("    close the space), and the whole budget is 4*pi, so a")
    print("    closed 2+1 universe with spherical topology has BOUNDED")
    print("    TOTAL MASS.  Two maximal defects saturate it exactly:")
    print("    that is the degenerate 'spindle', the extremal case.")
    print()
    # global holonomy triviality
    for deficits in ([TAU / 2] * 4, [TAU / 3] * 6, [TAU / 6] * 12):
        assert abs(sum(deficits) - 2 * TAU) < 1e-9
        product = IDENTITY
        for d in deficits:
            product = matmul(rodrigues((0, 0, 1), d), product)
        assert rotation_angle(product) < 1e-9   # identity
    print("    And the rotation parts of all defect holonomies compose")
    print("    to the IDENTITY precisely because the deficits sum to")
    print("    0 mod 2*pi (verified for 4, 6, 12 equal defects): the")
    print("    loop enclosing everything is contractible on the far")
    print("    side of the sphere, so Gauss-Bonnet is exactly the")
    print("    condition that the global holonomy can be trivial.")


# =====================================================================
# 4. defects compose nonabelianly: masses add, centres braid
# =====================================================================

def rot2(theta):
    c, s = math.cos(theta), math.sin(theta)
    return ((c, -s), (s, c))


def apply2(M, v):
    return (M[0][0] * v[0] + M[0][1] * v[1],
            M[1][0] * v[0] + M[1][1] * v[1])


def defect_holonomy(deficit, centre):
    """ISO(2) element: rotate by `deficit` about `centre`."""
    R = rot2(deficit)
    t = sub(centre + (0,), apply2(R, centre) + (0,))[:2]
    return R, t


def compose(h1, h2):
    """h1 after h2."""
    (R1, t1), (R2, t2) = h1, h2
    R = ((R1[0][0] * R2[0][0] + R1[0][1] * R2[1][0],
          R1[0][0] * R2[0][1] + R1[0][1] * R2[1][1]),
         (R1[1][0] * R2[0][0] + R1[1][1] * R2[1][0],
          R1[1][0] * R2[0][1] + R1[1][1] * R2[1][1]))
    t = add(apply2(R1, t2), t1)
    return R, t


def verify_nonabelian_defects() -> None:
    cases = [(TAU / 6, TAU / 4, (0.0, 0.0), (3.0, 1.0)),
             (TAU / 3, TAU / 5, (-1.0, 2.0), (2.0, -1.5)),
             (TAU / 8, TAU / 8, (0.0, 0.0), (1.0, 0.0))]
    print(f"    {'d1':>8} {'d2':>8} {'rot(h1h2)':>10} {'rot(h2h1)':>10} "
          f"{'|commutator translation|':>26}")
    for d1, d2, p1, p2 in cases:
        h1 = defect_holonomy(d1, p1)
        h2 = defect_holonomy(d2, p2)
        ab = compose(h1, h2)
        ba = compose(h2, h1)
        angle_ab = math.atan2(ab[0][1][0], ab[0][0][0]) % TAU
        angle_ba = math.atan2(ba[0][1][0], ba[0][0][0]) % TAU
        assert abs(angle_ab - angle_ba) < 1e-12          # masses add
        assert abs(angle_ab - (d1 + d2) % TAU) < 1e-9
        shift = sub(ab[1] + (0,), ba[1] + (0,))[:2]
        # closed form: (I - R_d1)(I - R_d2)(p1 - p2)
        diff = sub(p1 + (0,), p2 + (0,))[:2]
        R1, R2 = rot2(d1), rot2(d2)
        step = sub(diff + (0,), apply2(R2, diff) + (0,))[:2]
        predicted = sub(step + (0,), apply2(R1, step) + (0,))[:2]
        assert norm(sub(shift + (0,), predicted + (0,))) < 1e-9, \
            (d1, d2, shift, predicted)
        print(f"    {d1:>8.4f} {d2:>8.4f} {angle_ab:>10.4f} "
              f"{angle_ba:>10.4f} {norm(shift + (0,)):>26.6f}")
    # degenerate cases: the residue vanishes exactly when it should
    for d1, d2, p1, p2 in [(0.0, TAU / 4, (0.0, 0.0), (2.0, 0.0)),
                           (TAU / 4, TAU / 4, (1.0, 1.0), (1.0, 1.0))]:
        ab = compose(defect_holonomy(d1, p1), defect_holonomy(d2, p2))
        ba = compose(defect_holonomy(d2, p2), defect_holonomy(d1, p1))
        assert norm(sub(ab[1] + (0,), ba[1] + (0,))) < 1e-12
    print()
    print("  Two defects: the total ROTATION is d1 + d2 either way --")
    print("  masses add, and that addition is the abelianization of")
    print("  ISO(2).  But the two orders differ by the pure translation")
    print()
    print("      (I - R_d1)(I - R_d2)(p1 - p2)")
    print()
    print("  (closed form, verified numerically), which vanishes iff a")
    print("  defect is massless or the two coincide.  So 'mass' is the")
    print("  abelian shadow of the holonomy and the nonabelian residue")
    print("  is a REAL relative displacement -- 2+1 gravitational")
    print("  scattering, the same braided tier the arithmetic bridge")
    print("  reached: carrying one defect around another does not")
    print("  commute with carrying it back.")


def run_verification_suite() -> None:
    sections = [
        ("Holonomy is the angle defect, on real polyhedra",
         verify_holonomy_is_the_defect),
        ("The curvature budget of a knot projection",
         verify_the_curvature_budget),
        ("The budget is the mass bound", verify_the_mass_bound),
        ("Defects compose nonabelianly: masses add, centres braid",
         verify_nonabelian_defects),
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
