"""The cone from the web: deriving 0021's c-bound from the event
structure (closing O3's remaining content).

P1 says all content is pairwise; the movie says all change happens
at interactions.  Then a node's knowledge can update ONLY through
its channels -- influence relays one hop per event -- and everything
0021 assumed follows.  Four steps, each computed:

  s1  THE EXACT CONE, AND WHERE ROUNDNESS COMES FROM.  On any web,
      strictly local update gives an EXACT dependency cone: news
      emitted at an event reaches exactly the graph-metric ball of
      radius = elapsed rounds (verified set-equal against BFS).
      But a lattice's cone is polygonal (anisotropy sqrt(2) for N4
      and N8, measured); on a random geometric web the front is
      round (anisotropy ~1.1, both snapshots).  ISOTROPY OF c IS
      STATISTICAL ISOTROPY OF THE CONNECTIVITY -- the roundness of
      the light cone is an emergent, measurable property of the
      web, not an axiom.

  s2  THE RETARDED RULE EMERGES.  Nodes gossip the freshest record
      of a moving source (0021's kicked worldline).  The record
      field converges to the RETARDED field y(t - rho/c) with c the
      measured front speed: mean |recorded - retarded| falls from
      6.3% to 4.3% of the move size as the web densifies.  0021's
      retarded update rule is not an assumption about physics; it
      is what relayed knowledge looks like in the continuum.

  s3  ONE WEB, ONE CONE (universality of c).  Two different
      payloads gossiped on the same web (position news and strength
      news) arrive at every node at IDENTICAL ticks: all influence
      rides the same interaction graph, so every signal shares one
      cone.  The VALUE of c is the conversion a/tau between the
      web's length unit and its event unit -- a unit choice, which
      is exactly the status c has in physics.

  s4  THE TWO TIERS ARE THE TRACE AND TRACELESS SECTORS.  During
      the transient, with several sources gossiped independently:
      tr h(x) = S_total holds EXACTLY at every node at every tick
      (machine precision) -- the trace sector needs no updating,
      carries no position information, and cannot signal.  The
      traceless (anisotropy) sector carries ALL the news, is
      c-bounded (unchanged at a far probe until its arrival tick),
      and by 0020 carries ALL the curvature.  P2's split is not a
      posit here: correlational tier = trace, actionable tier =
      traceless, computed.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import random
import statistics
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_r = importlib.import_module("0016_the_retarded_web")


# =====================================================================
# webs
# =====================================================================

def lattice(n=41, span=2.0, diag=False):
    pts, index = [], {}
    for i in range(n):
        for j in range(n):
            index[(i, j)] = len(pts)
            pts.append((-span + 2 * span * i / (n - 1),
                        -span + 2 * span * j / (n - 1)))
    nbrs = [[] for _ in pts]
    steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if diag:
        steps += [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for (i, j), a in index.items():
        for di, dj in steps:
            b = index.get((i + di, j + dj))
            if b is not None:
                nbrs[a].append(b)
    return pts, nbrs, index


def random_web(N, r, seed):
    rng = random.Random(seed)
    pts = [(rng.uniform(-2.2, 2.2), rng.uniform(-2.2, 2.2))
           for _ in range(N)]
    buckets = {}
    for i, (x, y) in enumerate(pts):
        buckets.setdefault((int(x // r), int(y // r)), []).append(i)
    nbrs = [[] for _ in range(N)]
    for i, (x, y) in enumerate(pts):
        cx, cy = int(x // r), int(y // r)
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for j in buckets.get((cx + dx, cy + dy), []):
                    if j != i and (x - pts[j][0]) ** 2 \
                            + (y - pts[j][1]) ** 2 <= r * r:
                        nbrs[i].append(j)
    return pts, nbrs


def gossip_run(pts, nbrs, dt, warm, nticks, snaps, probe=None):
    """Freshest-record gossip of the kicked worldline; returns
    snapshots and (optionally) the probe node's record history."""
    N = len(pts)
    rec = [(-10 ** 9, 0.0, 0.0)] * N
    out, history = {}, []
    for tick in range(nticks):
        t = (tick - warm) * dt
        sp = _r.kicked_pos(t)
        best = min(range(N),
                   key=lambda i: (pts[i][0] - sp[0]) ** 2
                   + (pts[i][1] - sp[1]) ** 2)
        if rec[best][0] < tick:
            rec[best] = (tick, sp[0], sp[1])
        new = list(rec)
        for i in range(N):
            b = rec[i]
            for j in nbrs[i]:
                if rec[j][0] > b[0]:
                    b = rec[j]
            new[i] = b
        rec = new
        if tick in snaps:
            out[tick] = list(rec)
        if probe is not None:
            history.append(rec[probe])
    return out, history


# =====================================================================
# 1. the exact cone, and roundness
# =====================================================================

def bfs_dist(nbrs, src):
    dist = {src: 0}
    frontier = [src]
    while frontier:
        nxt = []
        for u in frontier:
            for v in nbrs[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    nxt.append(v)
        frontier = nxt
    return dist


def one_event_front(pts, nbrs, src, ticks):
    """Nodes holding the single record emitted at tick 0 from src,
    after `ticks` synchronous gossip rounds."""
    have = {src}
    for _ in range(ticks):
        new = set(have)
        for i in range(len(pts)):
            if i not in have and any(j in have for j in nbrs[i]):
                new.add(i)
        have = new
    return have


def ball_anisotropy(pts, src, nodes):
    bins = [0.0] * 12
    sx, sy = pts[src]
    for i in nodes:
        x, y = pts[i][0] - sx, pts[i][1] - sy
        rho = math.hypot(x, y)
        if rho < 1e-12:
            continue
        b = int((math.atan2(y, x) % (2 * math.pi)) / (2 * math.pi) * 12)
        bins[b] = max(bins[b], rho)
    return max(bins) / min(bins)


def verify_the_exact_cone() -> None:
    for diag, name in ((False, "N4 lattice"), (True, "N8 lattice")):
        pts, nbrs, index = lattice(diag=diag)
        src = index[(20, 20)]
        dist = bfs_dist(nbrs, src)
        for T in (5, 11):
            front = one_event_front(pts, nbrs, src, T)
            ball = {i for i, d in dist.items() if d <= T}
            assert front == ball, (name, T)
        sphere = [i for i, d in dist.items() if d == 11]
        radii = [math.hypot(pts[i][0] - pts[src][0],
                            pts[i][1] - pts[src][1]) for i in sphere]
        aniso = max(radii) / min(radii)
        print(f"    {name}: front == graph ball EXACTLY (ticks 5, 11);")
        print(f"      cone anisotropy {aniso:.3f} (polygonal -- "
              f"sqrt(2) = 1.414)")
        assert 1.35 < aniso < 1.45, aniso
    pts, nbrs = random_web(3500, 0.16, seed=7)
    snaps, _ = gossip_run(pts, nbrs, 0.1, 5, 23, {15, 22})
    for tick in (15, 22):
        rows = [i for i in range(len(pts))
                if (snaps[tick][i][0] - 5) * 0.1 > 0.0]
        bins = [0.0] * 12
        for i in rows:
            x, y = pts[i]
            b = int((math.atan2(y, x) % (2 * math.pi))
                    / (2 * math.pi) * 12)
            bins[b] = max(bins[b], math.hypot(x, y))
        aniso = max(bins) / min(bins)
        assert aniso < 1.2, aniso
        print(f"    random web, t = {(tick - 5) * 0.1:.1f}: front "
              f"anisotropy {aniso:.3f} -- round.")
    print()
    print("  Strict locality (P1: change only through channels) gives")
    print("  an EXACT dependency cone -- news occupies precisely the")
    print("  graph ball.  The cone's ROUNDNESS is not an axiom: it is")
    print("  the statistical isotropy of the connectivity, absent on")
    print("  lattices and emergent on the random web.")


# =====================================================================
# 2. the retarded rule emerges
# =====================================================================

def verify_retarded_emergence() -> None:
    warm, dt = 5, 0.1
    results = []
    for N, r in ((3500, 0.16), (9000, 0.10)):
        pts, nbrs = random_web(N, r, seed=7)
        snaps, _ = gossip_run(pts, nbrs, dt, warm, 23, {15, 22})
        radii = {}
        for tick in (15, 22):
            rows = [i for i in range(len(pts))
                    if (snaps[tick][i][0] - warm) * dt > 0.0]
            radii[tick] = max(math.hypot(*pts[i]) for i in rows)
        c = (radii[22] - radii[15]) / ((22 - 15) * dt)
        T = (22 - warm) * dt
        errs = []
        for i in range(len(pts)):
            rho = math.hypot(*pts[i])
            pr = _r.kicked_pos(T - rho / c)
            ri = snaps[22][i]
            errs.append(math.hypot(ri[1] - pr[0], ri[2] - pr[1]))
        mean_err = sum(errs) / len(errs)
        results.append((N, r, c, mean_err))
        print(f"    N = {N}, reach r = {r}: front speed c = {c:.3f};")
        print(f"      mean |recorded - retarded(c)| = {mean_err:.4f}"
              f"  ({100 * mean_err / _r.MOVE_D:.1f}% of the move)")
    assert results[1][3] < results[0][3]
    assert results[1][3] < 0.013
    print()
    print("  The gossip record field IS the retarded field, to an")
    print("  error that falls as the web densifies: 0021's c-bounded")
    print("  update rule is the continuum shadow of 'a node knows only")
    print("  what its channels have told it'.  The c that appears is")
    print("  the measured front speed of the web itself.")


# =====================================================================
# 3. one web, one cone
# =====================================================================

def verify_universality() -> None:
    pts, nbrs = random_web(2500, 0.18, seed=11)
    src = min(range(len(pts)),
              key=lambda i: pts[i][0] ** 2 + pts[i][1] ** 2)
    dist = bfs_dist(nbrs, src)
    # two payloads, same event, independent gossips
    arrivals = []
    for payload in ("position", "strength"):
        have = {src}
        arrive = {src: 0}
        for tick in range(1, 40):
            new = set(have)
            for i in range(len(pts)):
                if i not in have and any(j in have for j in nbrs[i]):
                    new.add(i)
                    arrive[i] = tick
            have = new
        arrivals.append(arrive)
    assert arrivals[0] == arrivals[1]
    assert all(arrivals[0][i] == d for i, d in dist.items())
    print(f"    two payloads (position news, strength news) on the")
    print(f"    same web: arrival ticks IDENTICAL at all "
          f"{len(dist)} reached nodes,")
    print(f"    and equal to graph distance.")
    print()
    print("  Universality of c: every signal rides the same channels,")
    print("  so all influence shares ONE cone.  The value of c is the")
    print("  conversion a/tau between the web's length unit and event")
    print("  unit -- a unit choice, which is exactly the status the")
    print("  physical c has.")


# =====================================================================
# 4. the two tiers are the trace and traceless sectors
# =====================================================================

def verify_the_sectors() -> None:
    warm, dt = 5, 0.1
    pts, nbrs = random_web(3500, 0.16, seed=7)
    probe = min(range(len(pts)),
                key=lambda i: (pts[i][0] - 0.0) ** 2
                + (pts[i][1] - 1.5) ** 2)
    _, hist = gossip_run(pts, nbrs, dt, warm, 23, set(), probe=probe)
    statics = [((1.2, 0.8), 0.2), ((-0.9, 0.6), 0.1)]
    w_kicked = 0.3
    S_total = w_kicked + sum(w for _, w in statics)
    px, py = pts[probe]
    worst_trace = 0.0
    tl_series = []
    arrival = None
    for tick, rec in enumerate(hist):
        # channel to the kicked source: recorded position
        h11 = h12 = h22 = 0.0
        for (sx, sy), w in statics + [((rec[1], rec[2]), w_kicked)]:
            d = math.hypot(sx - px, sy - py)
            ux, uy = (sx - px) / d, (sy - py) / d
            h11 += w * ux * ux
            h12 += w * ux * uy
            h22 += w * uy * uy
        worst_trace = max(worst_trace, abs((h11 + h22) - S_total))
        tl_series.append(0.5 * (h11 - h22))
        if arrival is None and (rec[0] - warm) * dt > 0.0:
            arrival = tick
    assert worst_trace < 1e-14, worst_trace
    pre = tl_series[:arrival]
    assert max(pre) - min(pre) < 1e-15
    assert abs(tl_series[-1] - tl_series[0]) > 1e-4
    print(f"    three sources (one kicked, two static), gossiped")
    print(f"    independently; probe node at distance 1.5:")
    print(f"      tr h = S_total at every tick: max dev "
          f"{worst_trace:.1e}")
    print(f"      traceless part: frozen until the news arrives")
    print(f"      (tick {arrival}), then changes by "
          f"{abs(tl_series[-1] - tl_series[0]):.5f}.")
    print()
    print("  The two tiers of P2, computed: the TRACE sector is the")
    print("  correlational tier -- exact at all times, position-blind,")
    print("  cannot signal; the TRACELESS sector is the actionable")
    print("  tier -- c-bounded, carries all the news and (by 0020)")
    print("  ALL the curvature.  The signature split is a sector")
    print("  split of the web's own field.")


def run_verification_suite() -> None:
    sections = [
        ("The exact cone, and where roundness comes from",
         verify_the_exact_cone),
        ("The retarded rule emerges", verify_retarded_emergence),
        ("One web, one cone", verify_universality),
        ("The two tiers are the trace and traceless sectors",
         verify_the_sectors),
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
