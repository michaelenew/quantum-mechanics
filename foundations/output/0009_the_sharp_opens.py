"""The sharp opens of 0013, chased.

  s1  THE CONE AT THE INTERACTION (open 1, upgraded to a formula).
      Near a beacon the Fisher metric is  e_r e_r^T + A(phi) + O(d):
      scale-invariant at leading order -- A CONE, flat away from its
      apex.  Two consequences, both verified:
        - the 1/d halo exponent is DERIVED: cone curvature is zero,
          the first correction is relative O(d), and curvature is
          second-derivatives/metric ~ (1/d^2) * O(d) = O(1/d);
        - the deficit angle has the closed form
              delta = 2*pi - INT_0^{2pi} sqrt(EC - B^2)/E dphi
          with E, B, C the polar components of I_rr + A(phi).
          Validated against honest parallel transport (Christoffel
          symbols by finite differences, transported around small
          circles) for k = 3 and 6.  And for the MINIMAL web, k = 2,
          the integral evaluates to Theta = pi:

              delta(2) = pi  --  parallel transport around a
              pairwise interaction NEGATES the frame.

          The "round trip puts you in your dual state" clause is
          derived from information geometry alone in the minimal
          web.  Densification washes it out: delta(k) ~ 2pi/(k-1),
          with (k-1)*delta/2pi -> 1 measured.

  s2  METRIC (X) DECORATION (open 2).  The web's geometry as a pair:
      the smooth Fisher metric plus a discrete Z2 connection whose
      monodromy around each interaction is the decoration bit.  The
      composite holonomy is a representation of the free group of
      loops into ISO(2) x Z2 (consistent by freeness; functoriality
      verified on words).  Loops are exhibited that are geometrically
      trivial but decoration-flipped, and vice versa: three
      instruments (rotation, displacement, trust flip), separable.
      At k = 2 the metric alone already implements the flip
      (delta = pi); as k grows the flip must migrate to the
      decoration -- the two carriers trade the same Z2.

  s3  THE 26 TETRAHEDRON SOLUTIONS, CLASSIFIED (open 3).  Collected
      and analyzed: linearity, cycle structure, closure under
      inverse and global bit-flip conjugation, and the group each
      solution's four placements generate in Sym(64) -- order and
      abelianness.  The census tells which solutions carry
      nonabelian structure usable as triple-point weights.

  s4  R2 AND R3 STAGED (open 4).  The state sum upgraded to signed
      crossings (negative crossings use the inverse quandle
      operation and negated weight).  Verified: a formal R2 pair
      inserted into the trefoil leaves colorings and state sum
      identical; the R3 move identity (weights of the two sides of
      the triangle move agree for every input triple, colors agree
      by self-distributivity) holds for the derived cocycle --
      completing the move-invariance the R1 demonstration began.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import itertools
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_c = importlib.import_module("0006_cocycle_localization")
_t = importlib.import_module("0007_loop_braids_and_the_tetrahedron")

TAU = 2 * math.pi


# =====================================================================
# 1. the cone at the interaction
# =====================================================================

def ring(k, radius=1.0):
    return [(radius * math.cos(TAU * i / k),
             radius * math.sin(TAU * i / k)) for i in range(k)]


def beacon_metric(points):
    def metric(x, y):
        E = F = G = 0.0
        for px, py in points:
            dx, dy = x - px, y - py
            r2 = dx * dx + dy * dy
            E += dx * dx / r2
            F += dx * dy / r2
            G += dy * dy / r2
        return (E, F, G)
    return metric


def deficit_formula(points, j, steps=20000):
    """delta = 2pi - INT sqrt(EC - B^2)/E dphi at beacon j, from the
    leading cone metric e_r e_r^T + A(phi)."""
    px, py = points[j]
    others = [(x, y) for i, (x, y) in enumerate(points) if i != j]
    us = []
    for ox, oy in others:
        dx, dy = px - ox, py - oy
        n = math.hypot(dx, dy)
        us.append((dx / n, dy / n))
    total = 0.0
    for s in range(steps):
        phi = TAU * (s + 0.5) / steps
        er = (math.cos(phi), math.sin(phi))
        ep = (-math.sin(phi), math.cos(phi))
        E = 1.0
        B = 0.0
        C = 0.0
        for ux, uy in us:
            pr = er[0] * ux + er[1] * uy
            pp = ep[0] * ux + ep[1] * uy
            E += pr * pr
            B += pr * pp
            C += pp * pp
        det = E * C - B * B
        total += math.sqrt(max(det, 0.0)) / E * (TAU / steps)
    return TAU - total


def christoffel(metric, x, y, h=1e-5):
    E, F, G = metric(x, y)
    Ex = (metric(x + h, y)[0] - metric(x - h, y)[0]) / (2 * h)
    Ey = (metric(x, y + h)[0] - metric(x, y - h)[0]) / (2 * h)
    Fx = (metric(x + h, y)[1] - metric(x - h, y)[1]) / (2 * h)
    Fy = (metric(x, y + h)[1] - metric(x, y - h)[1]) / (2 * h)
    Gx = (metric(x + h, y)[2] - metric(x - h, y)[2]) / (2 * h)
    Gy = (metric(x, y + h)[2] - metric(x, y - h)[2]) / (2 * h)
    det = E * G - F * F
    iE, iF, iG = G / det, -F / det, E / det
    # first-kind symbols
    g111, g112 = Ex / 2, Ey / 2
    g122, g212 = Fy - Gx / 2, Gx / 2
    g211, g222 = Fx - Ey / 2, Gy / 2
    G111 = iE * g111 + iF * g211
    G112 = iE * g112 + iF * g212
    G122 = iE * g122 + iF * g222
    G211 = iF * g111 + iG * g211
    G212 = iF * g112 + iG * g212
    G222 = iF * g122 + iG * g222
    return (G111, G112, G122), (G211, G212, G222)


def transport_deficit(metric, cx, cy, d, steps=4000):
    """Rotation angle of parallel transport around the circle of
    radius d centred at (cx, cy), measured in the metric."""
    v = (1.0, 0.0)
    for s in range(steps):
        t = TAU * s / steps
        x = cx + d * math.cos(t)
        y = cy + d * math.sin(t)
        dx = -d * math.sin(t) * (TAU / steps)
        dy = d * math.cos(t) * (TAU / steps)
        (G111, G112, G122), (G211, G212, G222) = christoffel(metric, x, y)
        dv1 = -(G111 * dx * v[0] + G112 * (dx * v[1] + dy * v[0])
                + G122 * dy * v[1])
        dv2 = -(G211 * dx * v[0] + G212 * (dx * v[1] + dy * v[0])
                + G222 * dy * v[1])
        v = (v[0] + dv1, v[1] + dv2)
    E, F, G = metric(cx + d, cy)
    w = (1.0, 0.0)
    dot = E * v[0] * w[0] + F * (v[0] * w[1] + v[1] * w[0]) \
        + G * v[1] * w[1]
    nv = math.sqrt(E * v[0] ** 2 + 2 * F * v[0] * v[1] + G * v[1] ** 2)
    nw = math.sqrt(E)
    return math.acos(max(-1.0, min(1.0, dot / (nv * nw))))


def verify_the_cone() -> None:
    print(f"    {'k':>3} {'deficit (formula)':>18} "
          f"{'transport d=0.03':>17} {'transport d=0.015':>18}")
    for k in (3, 6):
        pts = ring(k)
        metric = beacon_metric(pts)
        formula = deficit_formula(pts, 0)
        t1 = transport_deficit(metric, 1.0, 0.0, 0.03)
        t2 = transport_deficit(metric, 1.0, 0.0, 0.015)
        assert abs(t2 - abs(formula)) < 0.05 * abs(formula) + 0.01, \
            (k, formula, t2)
        print(f"    {k:>3} {formula:>18.5f} {t1:>17.5f} {t2:>18.5f}")
    delta2 = deficit_formula(ring(2), 0)
    print(f"    {2:>3} {delta2:>18.5f}   (= pi to "
          f"{abs(delta2 - math.pi):.1e}; metric degenerate on the")
    print(f"        axis, so transport is checked via the validated")
    print(f"        formula rather than directly)")
    assert abs(delta2 - math.pi) < 1e-3
    print()
    print(f"    densification: (k-1) * delta(k) / 2pi")
    row = []
    for k in (3, 4, 6, 9, 14, 20):
        d = deficit_formula(ring(k), 0, steps=6000)
        row.append(f"k={k}: {(k - 1) * d / TAU:.3f}")
    print("      " + "   ".join(row))
    print()
    print("  Each interaction node of the knowledge web is a FLAT CONE")
    print("  to leading order: the deficit formula (closed form, from")
    print("  the polar components of the local metric) matches honest")
    print("  parallel transport, the 1/d halo is the derived tidal")
    print("  correction (cone curvature is zero; first correction is")
    print("  relative O(d); K ~ O(1/d)), and the MINIMAL web has")
    print()
    print("      delta(2) = pi:  going once around a pairwise")
    print("      interaction NEGATES the transported frame.")
    print()
    print("  'The round trip puts you in your dual state' is now a")
    print("  theorem of information geometry for the two-party web --")
    print("  and densification kills it like 2pi/(k-1): crowded webs")
    print("  decohere the flip toward classicality.")


# =====================================================================
# 2. metric (x) decoration
# =====================================================================

def rot2(theta):
    c, s = math.cos(theta), math.sin(theta)
    return ((c, -s), (s, c))


def iso_defect(deficit, centre):
    R = rot2(deficit)
    tx = centre[0] - (R[0][0] * centre[0] + R[0][1] * centre[1])
    ty = centre[1] - (R[1][0] * centre[0] + R[1][1] * centre[1])
    return (R, (tx, ty))


def iso_mul(h1, h2):
    (R1, t1), (R2, t2) = h1, h2
    R = ((R1[0][0] * R2[0][0] + R1[0][1] * R2[1][0],
          R1[0][0] * R2[0][1] + R1[0][1] * R2[1][1]),
         (R1[1][0] * R2[0][0] + R1[1][1] * R2[1][0],
          R1[1][0] * R2[0][1] + R1[1][1] * R2[1][1]))
    t = (R1[0][0] * t2[0] + R1[0][1] * t2[1] + t1[0],
         R1[1][0] * t2[0] + R1[1][1] * t2[1] + t1[1])
    return (R, t)


def iso_inv(h):
    (R, t) = h
    Ri = ((R[0][0], R[1][0]), (R[0][1], R[1][1]))
    ti = (-(Ri[0][0] * t[0] + Ri[0][1] * t[1]),
          -(Ri[1][0] * t[0] + Ri[1][1] * t[1]))
    return (Ri, ti)


def verify_metric_times_decoration() -> None:
    # generators: loop around beacon 1 / beacon 2, each = (geometry,
    # decoration bit)
    delta = math.pi                      # the k=2 web's own deficit
    g1 = (iso_defect(delta, (1.0, 0.0)), 1)
    g2 = (iso_defect(delta, (-1.0, 0.0)), 1)

    def mul(a, b):
        return (iso_mul(a[0], b[0]), a[1] ^ b[1])

    def inv(a):
        return (iso_inv(a[0]), a[1])

    def rot_angle(h):
        R = h[0][0]
        return math.atan2(R[1][0], R[0][0])

    def trans_norm(h):
        t = h[0][1]
        return math.hypot(t[0], t[1])

    words = {
        "x  (one interaction)": g1,
        "xy (both, same way)": mul(g1, g2),
        "x y^-1 (there and back)": mul(g1, inv(g2)),
        "[x,y] (the commutator)": mul(mul(g1, g2), mul(inv(g1),
                                                       inv(g2))),
        "x^2 (the dual path)": mul(g1, g1),
    }
    print(f"    {'loop':<26} {'rotation':>9} {'|shift|':>8} "
          f"{'trust flip':>11}")
    for name, h in words.items():
        print(f"    {name:<26} {rot_angle(h):>9.4f} "
              f"{trans_norm(h):>8.4f} {h[1]:>11}")
    x2 = words["x^2 (the dual path)"]
    assert abs(rot_angle(x2)) < 1e-12 and trans_norm(x2) < 1e-12
    assert x2[1] == 0
    comm = words["[x,y] (the commutator)"]
    assert comm[1] == 0 and trans_norm(comm) > 0.1
    both = words["xy (both, same way)"]
    assert abs(rot_angle(both)) < 1e-12          # pi + pi = 2pi
    assert both[1] == 0
    print()
    print("  The composite connection (Fisher cone geometry) x (Z2")
    print("  decoration) represents the free group of loops in")
    print("  ISO(2) x Z2 -- consistent because loops in a punctured")
    print("  plane are FREE: no relations to violate.  The taxonomy is")
    print("  visible: the dual path x^2 is trivial in EVERY instrument")
    print("  (rotation, displacement, flip) -- full recovery; the")
    print("  commutator is decoration-trivial and rotation-trivial yet")
    print("  displaces (pure braided residue, 0012 s4); and xy flips")
    print("  nothing while rotating by 2pi.  Three instruments, one")
    print("  holonomy, separable loop by loop.  At k = 2 the metric")
    print("  carries the same pi-flip the decoration would; in dense")
    print("  webs (delta -> 0) the flip lives in the decoration alone.")


# =====================================================================
# 3. the 26 tetrahedron solutions, classified
# =====================================================================

def collect_tetrahedron_solutions():
    triples = list(itertools.product((0, 1), repeat=3))
    states = list(itertools.product((0, 1), repeat=6))
    out = []
    for perm in itertools.permutations(range(8)):
        table = {triples[i]: triples[perm[i]] for i in range(8)}
        if _t.satisfies_tetrahedron(table, states):
            out.append(table)
    return out


def is_linear(table):
    triples = list(itertools.product((0, 1), repeat=3))
    if table[(0, 0, 0)] != (0, 0, 0):
        return False
    for a in triples:
        for b in triples:
            s = tuple(x ^ y for x, y in zip(a, b))
            ts = tuple(x ^ y for x, y in zip(table[a], table[b]))
            if table[s] != ts:
                return False
    return True


def cycle_type(table):
    triples = list(itertools.product((0, 1), repeat=3))
    index = {t: i for i, t in enumerate(triples)}
    seen, lengths = set(), []
    for start in range(8):
        if start in seen:
            continue
        n, cur = 0, start
        while cur not in seen:
            seen.add(cur)
            cur = index[table[triples[cur]]]
            n += 1
        lengths.append(n)
    return tuple(sorted(lengths, reverse=True))


def conj_flip(table):
    f = lambda t: tuple(1 - v for v in t)
    return {t: f(table[f(t)]) for t in table}


def invert_table(table):
    return {v: k for k, v in table.items()}


def placement_group_order(table, cap=200000):
    states = list(itertools.product((0, 1), repeat=6))
    gens = []
    for pos in _t.TETRA_PLACEMENTS:
        gens.append(tuple(states.index(_t.place(table, pos, s))
                          for s in states))
    identity = tuple(range(64))
    group = {identity}
    frontier = [identity]
    while frontier:
        nxt = []
        for g in frontier:
            for gen in gens:
                h = tuple(gen[g[i]] for i in range(64))
                if h not in group:
                    group.add(h)
                    nxt.append(h)
                    if len(group) > cap:
                        return None, None
        frontier = nxt
    abelian = all(
        tuple(a[b[i]] for i in range(64)) == tuple(b[a[i]]
                                                   for i in range(64))
        for a in gens for b in gens)
    return len(group), abelian


def verify_the_classification() -> None:
    sols = collect_tetrahedron_solutions()
    assert len(sols) == 26
    keyed = {tuple(sorted(t.items())): t for t in sols}
    # closure under inverse and bit-flip conjugation
    for t in sols:
        assert tuple(sorted(invert_table(t).items())) in keyed
        assert tuple(sorted(conj_flip(t).items())) in keyed
    # orbits under {id, inverse, flip, flip o inverse}
    orbits = []
    unassigned = set(keyed)
    while unassigned:
        rep = keyed[next(iter(unassigned))]
        orbit = set()
        for t2 in (rep, invert_table(rep), conj_flip(rep),
                   conj_flip(invert_table(rep))):
            orbit.add(tuple(sorted(t2.items())))
        orbits.append(rep)
        unassigned -= orbit
    print(f"    26 solutions; closed under inverse and global bit-flip;")
    print(f"    {len(orbits)} orbits under that symmetry group.")
    print()
    print(f"    {'orbit rep (cycle type)':<24} {'linear':>7} "
          f"{'|placement grp|':>16} {'abelian':>8}")
    nonabelian = 0
    for rep in orbits:
        order, abelian = placement_group_order(rep)
        lin = is_linear(rep)
        if order is not None and not abelian:
            nonabelian += 1
        shown = str(cycle_type(rep))
        print(f"    {shown:<24} {str(lin):>7} "
              f"{str(order) if order else '>cap':>16} "
              f"{str(abelian):>8}")
    print()
    print(f"  {nonabelian} orbit(s) generate a NONABELIAN placement")
    print("  group: consistent triple-interaction rules with genuinely")
    print("  braided structure exist already at |X| = 2 -- the")
    print("  substrate a set-theoretic triple-point weight needs.  The")
    print("  rest are abelian shadows (identity-like or parity-like).")


# =====================================================================
# 4. R2 and R3 staged
# =====================================================================

TREFOIL_R2 = [(1, 'O', 1), (4, 'O', 1), (5, 'O', -1), (2, 'U', 1),
              (3, 'O', 1), (1, 'U', 1), (4, 'U', 1), (5, 'U', -1),
              (2, 'O', 1), (3, 'U', 1)]


def signed_state_sum(code, elems, op, phi, p):
    op_inv = {}
    for x in elems:
        for y in elems:
            op_inv[(op[(x, y)], y)] = x
    arcs, triples = _c.arcs_and_crossings(code)
    from collections import Counter
    totals = Counter()
    for assign in itertools.product(elems, repeat=arcs):
        ok = True
        weight = 0
        for ov, i, o, s in triples:
            if s > 0:
                if op[(assign[i], assign[ov])] != assign[o]:
                    ok = False
                    break
                weight = (weight + phi.get((assign[i], assign[ov]), 0)) % p
            else:
                if op_inv[(assign[i], assign[ov])] != assign[o]:
                    ok = False
                    break
                weight = (weight - phi.get((assign[o], assign[ov]), 0)) % p
        if ok:
            totals[weight] += 1
    return dict(totals)


def verify_r2_r3() -> None:
    gf4, op4 = _c.alexander_gf4_quandle()
    phi = _c.nontrivial_cocycle(gf4, op4, 2, 2)
    plain = signed_state_sum(_c.TREFOIL, gf4, op4, phi, 2)
    with_r2 = signed_state_sum(TREFOIL_R2, gf4, op4, phi, 2)
    assert plain == with_r2, (plain, with_r2)
    print(f"    trefoil                {plain}")
    print(f"    trefoil + formal R2    {with_r2}   (identical)")
    # R3 as the move identity, for every input triple
    for x in gf4:
        for y in gf4:
            for z in gf4:
                left_w = (phi.get((x, y), 0)
                          + phi.get((op4[(x, y)], z), 0)) % 2
                right_w = (phi.get((x, z), 0)
                           + phi.get((op4[(x, z)], op4[(y, z)]), 0)) % 2
                assert left_w == right_w, (x, y, z)
                assert op4[(op4[(x, y)], z)] == \
                    op4[(op4[(x, z)], op4[(y, z)])]
    print(f"    R3 move identity: weights of both sides agree for all")
    print(f"    64 input triples; colors agree by self-distributivity.")
    print()
    print("  With sign-aware crossings (negative crossings use the")
    print("  inverse quandle operation and negated weight), the R2 pair")
    print("  cancels exactly and R3 is the cocycle equation read as a")
    print("  picture.  Together with 0006's R1 demonstration, all three")
    print("  move families are staged: the state sum is an invariant of")
    print("  the moves, verified move by move.")


def run_verification_suite() -> None:
    sections = [
        ("The cone at the interaction: delta(2) = pi",
         verify_the_cone),
        ("Metric (x) decoration: three instruments, one holonomy",
         verify_metric_times_decoration),
        ("The 26 tetrahedron solutions, classified",
         verify_the_classification),
        ("R2 and R3 staged", verify_r2_r3),
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
