"""
The qubit information manifold: the Bloch sphere with the Fubini-Study metric.

The point of this script: illustrate that the "geometry of the web" is not
metaphor. For one qubit (a two-outcome knowledge target), the space of pure
knowledge states IS a Riemannian manifold - specifically the round sphere
S^2 - and the metric is fixed (Bures / Fubini-Study) without any freedom.

Concretely for a pure qubit |psi> = cos(theta/2)|0> + e^(i phi) sin(theta/2)|1>,
the Bloch vector r = (sin theta cos phi, sin theta sin phi, cos theta) is a
unit vector on S^2, and

    great-circle angle alpha(1,2) = arccos(r_1 . r_2)
    fidelity              F(1,2) = |<psi_1|psi_2>|^2 = (1 + r_1 . r_2)/2
                                 = cos^2(alpha/2)
    Fubini-Study distance d(1,2) = alpha / 2                (in [0, pi/2])

Curvature of S^2 (unit radius): K = 1. On a spherical triangle with interior
angles A, B, C and area Delta, GAUSS-BONNET gives

    A + B + C = pi + Delta

- the "angular excess" over pi is exactly the enclosed area. This is the
geometric statement that S^2 is positively curved, and it directly bounds how
much "orthogonal information" you can pack into a small region - a geometric
shadow of the Heisenberg / entropic uncertainty relations.

Pure stdlib.
Run:  python3 0001_qubit_geometry.py
"""

import math


def bloch(theta, phi):
    return (math.sin(theta) * math.cos(phi),
            math.sin(theta) * math.sin(phi),
            math.cos(theta))


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def norm(v):
    return math.sqrt(dot(v, v))


def clamp(x, lo=-1.0, hi=1.0):
    return max(lo, min(hi, x))


def great_circle_angle(a, b):
    return math.acos(clamp(dot(a, b)))


def fs_distance(a, b):
    return great_circle_angle(a, b) / 2


def fidelity(a, b):
    return (1 + dot(a, b)) / 2


def midpoint_on_sphere(a, b):
    m = (a[0] + b[0], a[1] + b[1], a[2] + b[2])
    n = norm(m)
    if n < 1e-12:
        raise ValueError("antipodal points; midpoint undefined")
    return (m[0] / n, m[1] / n, m[2] / n)


def spherical_triangle_area(a, b, c):
    """L'Huilier's / Van Oosterom-Strackee formula for area (steradians) of
    the spherical triangle with unit-vector vertices a, b, c."""
    num = abs(dot(a, cross(b, c)))
    den = 1 + dot(a, b) + dot(b, c) + dot(c, a)
    return 2 * math.atan2(num, den)


def spherical_triangle_angles(a, b, c):
    """Interior angles at vertices a, b, c of the spherical triangle,
    computed as the angles between the tangent great-circle arcs."""
    def angle_at(p, q, r):
        # tangent at p pointing along p->q
        tq = (q[0] - dot(p, q) * p[0],
              q[1] - dot(p, q) * p[1],
              q[2] - dot(p, q) * p[2])
        tr = (r[0] - dot(p, r) * r[0],
              r[1] - dot(p, r) * r[1],
              r[2] - dot(p, r) * r[2])
        nq, nr = norm(tq), norm(tr)
        return math.acos(clamp((tq[0] * tr[0] + tq[1] * tr[1] + tq[2] * tr[2]) / (nq * nr)))
    return angle_at(a, b, c), angle_at(b, c, a), angle_at(c, a, b)


if __name__ == "__main__":
    z_plus  = bloch(0,           0)              # |0>
    z_minus = bloch(math.pi,     0)              # |1>
    x_plus  = bloch(math.pi / 2, 0)              # |+>
    y_plus  = bloch(math.pi / 2, math.pi / 2)    # |+i>

    labels = [("|0>", z_plus), ("|1>", z_minus), ("|+>", x_plus), ("|+i>", y_plus)]

    print("(1) Pairwise Fubini-Study distances and fidelities on the Bloch sphere:\n")
    print(f"    {'':6}" + "".join(f"{n:>10}" for n, _ in labels))
    for n1, v1 in labels:
        row_d = "".join(f"{fs_distance(v1, v2):>10.4f}" for _, v2 in labels)
        print(f"    {n1:>6}" + row_d)
    print()
    print("    fidelities (upper triangle):")
    for i, (n1, v1) in enumerate(labels):
        for _, (n2, v2) in enumerate(labels[i + 1:], start=i + 1):
            print(f"        F({n1}, {n2}) = {fidelity(v1, v2):.4f}   (= cos^2(alpha/2))")
    print()

    print("(2) MRE-like fusion of two equally-weighted knowledge states = geodesic midpoint.\n")
    for (n1, v1), (n2, v2) in [((("|0>"), z_plus), ("|+>", x_plus)),
                                (("|+>", x_plus), ("|+i>", y_plus))]:
        mid = midpoint_on_sphere(v1, v2)
        d1 = fs_distance(mid, v1)
        d2 = fs_distance(mid, v2)
        print(f"    midpoint({n1}, {n2}) has Bloch vector {tuple(round(x, 4) for x in mid)}")
        print(f"        d(mid, {n1}) = {d1:.4f},  d(mid, {n2}) = {d2:.4f}   equal: {abs(d1-d2) < 1e-10}")
    print()

    print("(3) Triangle inequality on the manifold (a 'recursive consistency' statement):\n")
    triples = [(z_plus, x_plus, y_plus),
               (z_plus, x_plus, z_minus)]
    for a, b, c in triples:
        d_ab = fs_distance(a, b)
        d_bc = fs_distance(b, c)
        d_ac = fs_distance(a, c)
        print(f"    d(a,b) + d(b,c) = {d_ab + d_bc:.4f}   d(a,c) = {d_ac:.4f}   holds: {d_ab + d_bc >= d_ac - 1e-12}")
    print()

    print("(4) Gauss-Bonnet on a spherical triangle: A + B + C - pi = Area.\n")
    print("    (equivalently, angular excess = enclosed area = curvature x area).\n")
    for name, (a, b, c) in [("octant (|0>, |+>, |+i>)", (z_plus, x_plus, y_plus))]:
        angles = spherical_triangle_angles(a, b, c)
        angle_sum = sum(angles)
        excess = angle_sum - math.pi
        area = spherical_triangle_area(a, b, c)
        print(f"    {name}:")
        print(f"        interior angles: {[round(x, 4) for x in angles]}")
        print(f"        sum: {angle_sum:.6f}   pi/2 excess expected for octant: {math.pi/2:.6f}")
        print(f"        computed excess: {excess:.6f}")
        print(f"        computed area:   {area:.6f}   (should equal excess = pi/2 for an octant)")
        print(f"        match: {'OK' if abs(excess - area) < 1e-10 else 'FAIL'}")
    print()

    print("Reading:")
    print("  * The qubit information manifold is fixed by 'knowledge is a")
    print("    distribution' + Chentsov/Petz uniqueness: S^2 with the round metric.")
    print("    No axiomatic freedom in choosing the geometry.")
    print("  * Fidelity, Fubini-Study distance, geodesic midpoints, and triangle")
    print("    inequalities are all COMPUTATIONAL, engineering-usable quantities.")
    print("  * The positive curvature (Gauss-Bonnet excess) is the geometric")
    print("    origin of qubit uncertainty relations: the manifold's shape")
    print("    caps how much independent information you can pack into a region.")
    print("  * For an N-level system, the same story runs on CP^(N-1) with the")
    print("    Fubini-Study metric - also fixed, also computable.")
