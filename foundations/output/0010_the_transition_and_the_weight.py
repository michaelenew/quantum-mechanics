"""The transition, the compensator, and the weight: 0014's opens.

  s1  NO THIRD CHANNEL PRESERVES THE FLIP.  The deficit depends only
      on the DIRECTIONS of the other channels (scale-invariant --
      verified by transport on a scaled configuration).  Sweeping
      all two-direction environments (angle theta between the two
      other channels, 0 < theta <= pi) and the coincident-channel
      case: delta stays strictly below pi everywhere -- the pi-flip
      is achieved by the two-party web ALONE.  Any third channel
      breaks it, and the residual pi - delta lies strictly between
      0 and pi: NEITHER discrete carrier (metric at delta = pi,
      decoration at delta = 0) can hold the flip at intermediate
      density.  If round-trip trust must stay binary, the
      compensator is forced to be CONTINUOUS -- a U(1) phase.  The
      amplitude tier enters exactly where densification pushes the
      geometry off the two endpoints.

  s2  THE COMPENSATOR AND THE LEDGER.  The forced compensator is
      phi_comp(k) = pi - delta(k), rising toward pi as the web
      densifies: sparse webs keep the flip in geometry, dense webs
      move it entirely into the phase.  And the web's curvature
      ledger closes: unwrapped parallel transport around a large
      loop equals the sum of the atomic deficits plus the integrated
      halo curvature (Gauss-Bonnet on the punctured disk), verified
      numerically for the 3-ring -- atoms + halo + nothing else.

  s3  TETRAHEDRAL WEIGHTS EXIST.  For each of the 21 tetrahedron-
      solution orbits, the linear system for a triple-point weight
      theta: X^3 -> Z_p (total weight of the two sides of the
      tetrahedron move equal on every 6-state) is solved exactly for
      p = 2, 3, 5.  Nonconstant weights exist for most orbits,
      including nonabelian ones; a witness is exhibited and its move
      identity verified on all 64 states.  The bridge from the
      census to a CJKLS-style level-2 invariant has a nonempty
      starting set.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import itertools
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_o = importlib.import_module("0009_the_sharp_opens")
_t = importlib.import_module("0007_loop_braids_and_the_tetrahedron")
_f = importlib.import_module("0008_fisher_deficit")

TAU = 2 * math.pi


# =====================================================================
# 1. no third channel preserves the flip
# =====================================================================

def deficit_from_directions(directions, steps=20000):
    total = 0.0
    for s in range(steps):
        phi = TAU * (s + 0.5) / steps
        er = (math.cos(phi), math.sin(phi))
        ep = (-math.sin(phi), math.cos(phi))
        E, B, C = 1.0, 0.0, 0.0
        for ux, uy in directions:
            pr = er[0] * ux + er[1] * uy
            pp = ep[0] * ux + ep[1] * uy
            E += pr * pr
            B += pr * pp
            C += pp * pp
        det = max(E * C - B * B, 0.0)
        total += math.sqrt(det) / E * (TAU / steps)
    return TAU - total


def verify_no_third_channel() -> None:
    # scale invariance of the deficit: transport around the same
    # beacon in a scaled configuration
    for scale in (1.0, 4.0):
        pts = [(scale * x, scale * y) for x, y in _o.ring(3)]
        metric = _o.beacon_metric(pts)
        t = _o.transport_deficit(metric, scale, 0.0, 0.015 * scale)
        assert abs(t - 1.9344) < 0.01, (scale, t)
    print("    scale invariance: transport deficit 1.934 at scale 1")
    print("    and at scale 4 -- the deficit is pure shape.")
    print()
    single = deficit_from_directions([(1.0, 0.0)])
    assert abs(single - math.pi) < 1e-3
    doubled = deficit_from_directions([(1.0, 0.0), (1.0, 0.0)])
    print(f"    one other channel:            delta = {single:.5f}"
          f"  (= pi: the flip)")
    print(f"    same channel, doubled:        delta = {doubled:.5f}")
    print()
    print("    two other channels at angle theta:")
    print(f"    {'theta/pi':>9} {'delta':>8} {'pi - delta':>11}")
    max_delta = 0.0
    for i in range(1, 21):
        theta = math.pi * i / 20
        us = [(1.0, 0.0), (math.cos(theta), math.sin(theta))]
        d = deficit_from_directions(us, steps=8000)
        max_delta = max(max_delta, d)
        if i in (2, 5, 10, 15, 20):
            print(f"    {theta / math.pi:>9.2f} {d:>8.4f} "
                  f"{math.pi - d:>11.4f}")
    assert max_delta < math.pi - 0.3, max_delta
    assert doubled < math.pi - 0.3
    print()
    print(f"    maximum over the sweep: {max_delta:.4f}  "
          f"(pi = {math.pi:.4f})")
    print()
    print("  The pi-flip belongs to the two-party web alone: every")
    print("  third channel -- at any angle, including coincident and")
    print("  opposite -- pulls the deficit strictly below pi, and the")
    print("  residual pi - delta sits strictly inside (0, pi).  A")
    print("  binary carrier cannot hold it: the metric carries the")
    print("  flip only at delta = pi, the decoration only at")
    print("  delta = 0, and every web between the endpoints needs a")
    print("  CONTINUOUS compensator.  If round-trip trust is to stay")
    print("  binary, densification FORCES a U(1) phase -- the")
    print("  amplitude tier, entering as geometry's change-maker.")


# =====================================================================
# 2. the compensator and the ledger
# =====================================================================

def transport_rotation_full(metric, cx, cy, radius, steps=6000):
    """Unwrapped rotation of parallel transport around the circle,
    accumulated step by step against the coordinate frame."""
    v = (1.0, 0.0)
    total = 0.0
    prev_angle = None
    for s in range(steps + 1):
        t = TAU * s / steps
        x = cx + radius * math.cos(t)
        y = cy + radius * math.sin(t)
        E, F, G = metric(x, y)
        # g-orthonormal frame: e1 ~ d/dx normalized, e2 ~ g-perp
        n1 = 1.0 / math.sqrt(E)
        # v in this frame: components (a, b) with v = a*e1 + b*e2
        # e2 = (-(F/E) , 1)/sqrt(G - F^2/E)
        det = G - F * F / E
        b = v[1] * math.sqrt(det) if det > 0 else 0.0
        a = (v[0] + v[1] * F / E) / n1
        angle = math.atan2(b, a)
        if prev_angle is not None:
            d = angle - prev_angle
            while d > math.pi:
                d -= TAU
            while d < -math.pi:
                d += TAU
            total += d
        prev_angle = angle
        if s == steps:
            break
        dx = -radius * math.sin(t) * (TAU / steps)
        dy = radius * math.cos(t) * (TAU / steps)
        (G111, G112, G122), (G211, G212, G222) = \
            _o.christoffel(metric, x, y)
        dv1 = -(G111 * dx * v[0] + G112 * (dx * v[1] + dy * v[0])
                + G122 * dy * v[1])
        dv2 = -(G211 * dx * v[0] + G212 * (dx * v[1] + dy * v[0])
                + G222 * dy * v[1])
        v = (v[0] + dv1, v[1] + dv2)
    return -total   # transport rotation is opposite the frame drift


def halo_integral(points, R, exclude, grid=0.02):
    metric = _o.beacon_metric(points)
    total = 0.0
    steps = int(2 * R / grid)
    for i in range(steps):
        x = -R + (i + 0.5) * grid
        for j in range(steps):
            y = -R + (j + 0.5) * grid
            if x * x + y * y > R * R:
                continue
            if any((x - px) ** 2 + (y - py) ** 2 < exclude ** 2
                   for px, py in points):
                continue
            d_near = min(math.hypot(x - px, y - py)
                         for px, py in points)
            h = min(1e-4, d_near / 80)
            E, F, G = metric(x, y)
            dA = math.sqrt(max(E * G - F * F, 0.0)) * grid * grid
            total += _f.gaussian_curvature(metric, x, y, h=h) * dA
    return total


def verify_the_ledger() -> None:
    print(f"    the forced compensator phi = pi - delta(k):")
    row = []
    for k in (2, 3, 6, 12, 20):
        d = _o.deficit_formula(_o.ring(k), 0, steps=6000)
        row.append(f"k={k}: {math.pi - d:+.3f}")
    print("      " + "   ".join(row))
    print()
    pts = _o.ring(3)
    metric = _o.beacon_metric(pts)
    big = transport_rotation_full(metric, 0.0, 0.0, 3.0)
    atoms = 3 * _o.deficit_formula(pts, 0, steps=8000)
    small_sum = 3 * _o.transport_deficit(metric, 1.0, 0.0, 0.02)
    halo = halo_integral(pts, 3.0, exclude=0.02)
    print(f"    ledger for the 3-ring, loop radius 3:")
    print(f"      unwrapped big-loop rotation   {abs(big):>9.4f}"
          f"   (sign = orientation convention)")
    print(f"      sum of atomic deficits        {atoms:>9.4f}"
          f"   (transport: {small_sum:.4f})")
    print(f"      integrated halo curvature     {halo:>9.4f}")
    print(f"      atoms + halo                  {atoms + halo:>9.4f}")
    gap = abs(abs(big) - (atoms + halo))
    assert gap < 0.02 * abs(big), (big, atoms, halo)
    print(f"      closure gap                   {gap:>9.4f}"
          f"   ({100 * gap / abs(big):.1f}%)")
    print()
    print("  Gauss-Bonnet closes on the web: the big loop's holonomy is")
    print("  the atomic deficits plus the halo integral -- nothing else")
    print("  carries curvature.  With s1, the two-carrier picture is")
    print("  complete and exclusive: atoms (cones) + halo (tidal) in")
    print("  geometry, the binary flip in the decoration, and the")
    print("  U(1) compensator phi(k) = pi - delta(k) bridging them,")
    print("  rising from 0 (sparse: geometry pays) toward pi (dense:")
    print("  the phase pays everything).")


# =====================================================================
# 3. tetrahedral weights
# =====================================================================

def weight_dims(table, p):
    """Solution space dim of: for every 6-state, total theta-weight of
    LHS placements equals RHS (arguments = incoming triples)."""
    triples = list(itertools.product((0, 1), repeat=3))
    tindex = {t: i for i, t in enumerate(triples)}
    states = list(itertools.product((0, 1), repeat=6))
    rows = []
    for s in states:
        row = [0] * 8
        cur = s
        for pos in _t.TETRA_PLACEMENTS:
            row[tindex[tuple(cur[q] for q in pos)]] += 1
            cur = _t.place(table, pos, cur)
        cur = s
        for pos in reversed(_t.TETRA_PLACEMENTS):
            row[tindex[tuple(cur[q] for q in pos)]] -= 1
            cur = _t.place(table, pos, cur)
        rows.append([v % p for v in row])
    rank = _c_rank(rows, p)
    return 8 - rank


def _c_rank(rows, p):
    rows = [r[:] for r in rows]
    n = len(rows[0])
    rank = 0
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
    return rank


def weight_witness(table, p):
    """A nonconstant weight, or None."""
    triples = list(itertools.product((0, 1), repeat=3))
    tindex = {t: i for i, t in enumerate(triples)}
    states = list(itertools.product((0, 1), repeat=6))
    rows = []
    for s in states:
        row = [0] * 8
        cur = s
        for pos in _t.TETRA_PLACEMENTS:
            row[tindex[tuple(cur[q] for q in pos)]] += 1
            cur = _t.place(table, pos, cur)
        cur = s
        for pos in reversed(_t.TETRA_PLACEMENTS):
            row[tindex[tuple(cur[q] for q in pos)]] -= 1
            cur = _t.place(table, pos, cur)
        rows.append([v % p for v in row])
    # solve kernel; return a kernel vector not constant
    rows2 = [r[:] for r in rows]
    rank, pivots = 0, []
    for col in range(8):
        piv = next((r for r in range(rank, len(rows2))
                    if rows2[r][col] % p), None)
        if piv is None:
            continue
        rows2[rank], rows2[piv] = rows2[piv], rows2[rank]
        inv = pow(rows2[rank][col], -1, p)
        rows2[rank] = [(v * inv) % p for v in rows2[rank]]
        for r in range(len(rows2)):
            if r != rank and rows2[r][col] % p:
                f = rows2[r][col]
                rows2[r] = [(a - f * b) % p
                            for a, b in zip(rows2[r], rows2[rank])]
        rank += 1
        pivots.append(col)
    free = [c for c in range(8) if c not in pivots]
    for fc in free:
        vec = [0] * 8
        vec[fc] = 1
        for r, col in enumerate(pivots):
            vec[col] = (-rows2[r][fc]) % p
        if len(set(vec)) > 1:
            return {t: vec[i] for i, t in
                    enumerate(triples)}
    return None


def verify_tetrahedral_weights() -> None:
    sols = _o.collect_tetrahedron_solutions()
    keyed = {tuple(sorted(t.items())): t for t in sols}
    orbits = []
    unassigned = set(keyed)
    while unassigned:
        rep = keyed[next(iter(unassigned))]
        orbit = set()
        for t2 in (rep, _o.invert_table(rep), _o.conj_flip(rep),
                   _o.conj_flip(_o.invert_table(rep))):
            orbit.add(tuple(sorted(t2.items())))
        orbits.append(rep)
        unassigned -= orbit
    print(f"    nonconstant weight-space dimension per orbit:")
    print(f"    {'cycle type':<22} {'nonab.':>7} "
          f"{'p=2':>5} {'p=3':>5} {'p=5':>5}")
    best = None
    for rep in orbits:
        order, abelian = _o.placement_group_order(rep)
        dims = [weight_dims(rep, p) - 1 for p in (2, 3, 5)]
        print(f"    {str(_o.cycle_type(rep)):<22} "
              f"{str(not abelian):>7} "
              f"{dims[0]:>5} {dims[1]:>5} {dims[2]:>5}")
        if not abelian and dims[0] > 0 and best is None:
            best = rep
    assert best is not None
    theta = weight_witness(best, 2)
    assert theta is not None
    # verify the move identity explicitly on all 64 states
    states = list(itertools.product((0, 1), repeat=6))
    for s in states:
        left, cur = 0, s
        for pos in _t.TETRA_PLACEMENTS:
            left += theta[tuple(cur[q] for q in pos)]
            cur = _t.place(best, pos, cur)
        right, cur = 0, s
        for pos in reversed(_t.TETRA_PLACEMENTS):
            right += theta[tuple(cur[q] for q in pos)]
            cur = _t.place(best, pos, cur)
        assert left % 2 == right % 2, s
    shown = {t: v for t, v in theta.items() if v}
    print()
    print(f"    witness: nonabelian orbit {_o.cycle_type(best)}, "
          f"placement group order "
          f"{_o.placement_group_order(best)[0]};")
    print(f"    nonconstant weight (support {sorted(shown)}),")
    print(f"    move identity verified on all 64 states.")
    print()
    print("  Triple-point weights exist for nonabelian tetrahedron")
    print("  solutions at |X| = 2: the census's braided rules support")
    print("  nonconstant invariant weights -- the set-theoretic")
    print("  starting set for a level-2 (surface) state sum is")
    print("  nonempty, and now enumerated by orbit and modulus.")


def run_verification_suite() -> None:
    sections = [
        ("No third channel preserves the flip",
         verify_no_third_channel),
        ("The compensator and the ledger", verify_the_ledger),
        ("Tetrahedral weights", verify_tetrahedral_weights),
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
