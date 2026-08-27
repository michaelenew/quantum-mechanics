"""0079 -- the vertex coupling: where the two ledgers meet.

0087 open 1: does the two-ledger split (source factor x record
factor, exact on the free/2D tiers) survive at the 4D vertex? The
test: shift one plaquette's curvature by a fixed source dF and ask
whether the price response depends on the OTHER five plaquettes (the
context). Factorization = locality of the response.

  s1  FREE TIER: exact locality. Under the per-plaquette product
      weight, the price response to a source shift depends only on
      the shifted plaquette -- identical across arbitrary contexts to
      1e-12. The reading theorem's precondition, verified in the
      vertex's own variables.
  s2  VERTEX: the split FAILS, by measurable nats. The same source
      shift on the same base plaquette costs systematically different
      amounts in different contexts (common-tetrad vs unrelated
      simples vs random packs). The context-spread is O(1) nat per
      O(1) source -- the shared-frame integral couples the source
      reading to the ambient record.
  s3  The coupling is first-order: Delta-price(t*dF)/t approaches a
      context-DEPENDENT linear coefficient as t -> 0. The
      non-factorization is not a large-source artifact; the vertex
      reads sources through the frame from the first order on.
  s4  Orientation lensing: with a geometric context, rotating the
      inserted source's plane from its own slot (e0^e1) toward a
      foreign slot (e0^e2) produces a smooth price curve -- the
      vertex charges the source's ORIENTATION relative to the ambient
      frame. Interaction = the frame reading the source's geometry.

Reading: the two-ledger separation (0086/0087) is a free-tier
theorem -- exact where gluing is character convolution (2D,
topological, no propagating interaction). The 4D vertex is precisely
the place where source and record couple, i.e. where gravity
gravitates: nonlinearity enters the measure as inter-ledger coupling.
This also names the mechanism for the decoherence-as-transfer
conjecture (0068/0085): the vertex is the operator that can move
entries between ledgers.
"""

import math
import random

import numpy as np

PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
EPSP = 0.01


def eps4(i, j, k, l):
    p = [i, j, k, l]
    if len(set(p)) < 4:
        return 0
    s = 1
    for a in range(4):
        for b in range(a + 1, 4):
            if p[a] > p[b]:
                s = -s
    return s


def starM(F):
    d = dict(zip(PAIRS, F))
    return [[sum(eps4(i, j, k, l) * d[(k, l)] for (k, l) in PAIRS)
             for j in range(4)] for i in range(4)]


def build_S(Fs):
    S = np.zeros((16, 16))
    for idx, (mu, nu) in enumerate(PAIRS):
        M = np.array(starM(Fs[idx])) / 2
        S[4 * mu:4 * mu + 4, 4 * nu:4 * nu + 4] += M
        S[4 * nu:4 * nu + 4, 4 * mu:4 * mu + 4] += M.T
    return S


def vertex_price(Fs):
    ev = np.linalg.eigvalsh(build_S(Fs))
    return float(0.5 * np.sum(np.log(1 + ev ** 2 / EPSP)))


def single_price(F):
    return vertex_price([list(F)] + [[0.0] * 6] * 5)


def product_price(Fs):
    return sum(single_price(F) for F in Fs)


def wedge(a, b):
    return [a[i] * b[j] - a[j] * b[i] for (i, j) in PAIRS]


def tetrad_pack(rng):
    e = [[rng.gauss(0, 1) for _ in range(4)] for _ in range(4)]
    return [wedge(e[mu], e[nu]) for (mu, nu) in PAIRS], e


def rand_simple(rng):
    return wedge([rng.gauss(0, 1) for _ in range(4)],
                 [rng.gauss(0, 1) for _ in range(4)])


def normalize(F, target=1.0):
    n = math.sqrt(sum(x * x for x in F))
    return [x * target / n for x in F]


def contexts(rng):
    """Three context types for the OTHER five plaquettes."""
    Ft, _ = tetrad_pack(rng)
    geo = [normalize(F) for F in Ft[1:]]
    sim = [normalize(rand_simple(rng)) for _ in range(5)]
    rnd = [normalize([rng.gauss(0, 1) for _ in range(6)])
           for _ in range(5)]
    return {"geometric": geo, "foreign-simple": sim, "random": rnd}


def s1_free_locality():
    print("== s1: free tier -- the response is exactly local ==")
    rng = random.Random(3)
    F0 = normalize(rand_simple(rng))
    dF = [0.5 * x for x in normalize(rand_simple(rng))]
    F0s = [a + b for a, b in zip(F0, dF)]
    responses = []
    for name, ctx in contexts(rng).items():
        d = product_price([F0s] + ctx) - product_price([F0] + ctx)
        responses.append(d)
        print(f"  context {name:15s}: product-weight response = "
              f"{d:.10f}")
    assert max(responses) - min(responses) < 1e-12
    print("  identical to 1e-12: under the product measure the source"
          " reading never sees the context\n")


def s2_vertex_coupling():
    print("== s2: the vertex -- the split fails, by measurable nats "
          "==")
    rng = random.Random(3)
    spreads = []
    for trial in range(6):
        F0 = normalize(rand_simple(rng))
        dF = [0.5 * x for x in normalize(rand_simple(rng))]
        F0s = [a + b for a, b in zip(F0, dF)]
        row = {}
        for name, ctx in contexts(rng).items():
            row[name] = vertex_price([F0s] + ctx) \
                - vertex_price([F0] + ctx)
        spread = max(row.values()) - min(row.values())
        spreads.append(spread)
        print(f"  trial {trial}: response by context "
              + "  ".join(f"{k} {v:+.3f}" for k, v in row.items())
              + f"   spread {spread:.3f}")
    mean_spread = sum(spreads) / len(spreads)
    print(f"  mean context-spread of the SAME source's price: "
          f"{mean_spread:.3f} nats")
    assert min(spreads) > 0.1 and mean_spread > 0.3
    print("  the vertex reads the source through the ambient record "
          "-- no factorization\n")
    return mean_spread


def s3_first_order():
    print("== s3: the coupling is first-order ==")
    rng = random.Random(5)
    F0 = normalize(rand_simple(rng))
    dF = normalize(rand_simple(rng))
    ctxs = contexts(rng)
    print("  central-difference d(price)/dt at t = 0 (converging in "
          "t), per context:")
    coefs = {}
    for name, ctx in ctxs.items():
        vals = []
        for t in (0.04, 0.02, 0.01, 0.005):
            Fp = [a + t * b for a, b in zip(F0, dF)]
            Fm = [a - t * b for a, b in zip(F0, dF)]
            vals.append((vertex_price([Fp] + ctx)
                         - vertex_price([Fm] + ctx)) / (2 * t))
        coefs[name] = vals[-1]
        # converged: last two agree to better than 1%
        assert abs(vals[-1] - vals[-2]) < 0.01 * max(abs(vals[-1]),
                                                     0.01)
        print(f"    {name:15s}: " + "  ".join(f"{v:+.4f}" for v in vals))
    cs = list(coefs.values())
    assert max(cs) - min(cs) > 0.05
    print("  converged linear coefficients differ by context "
          f"({', '.join(f'{c:+.3f}' for c in cs)}): the")
    print("  inter-ledger coupling is present from first order -- not "
          "a large-source artifact\n")


def s4_orientation_lensing():
    print("== s4: orientation lensing at a geometric vertex ==")
    rng = random.Random(11)
    Ft, e = tetrad_pack(rng)
    pack = [normalize(F) for F in Ft]
    base = vertex_price(pack)
    print("  source = 0.5 * (e0 ^ [cos phi e1 + sin phi e2]) inserted "
          "at slot (0,1):")
    prices = []
    for k in range(7):
        phi = k * math.pi / 12
        b = [math.cos(phi) * x + math.sin(phi) * y
             for x, y in zip(e[1], e[2])]
        dF = [0.5 * x for x in normalize(wedge(e[0], b))]
        Fs = [[a + d for a, d in zip(pack[0], dF)]] + pack[1:]
        dp = vertex_price(Fs) - base
        prices.append(dp)
        print(f"    phi = {phi:.3f}: Delta-price = {dp:+.4f}")
    assert abs(prices[0]) < abs(prices[-1]) or \
        (max(prices) - min(prices)) > 0.05
    print("  a smooth orientation curve: the vertex charges the "
          "source's plane relative to the")
    print("  ambient frame -- the measure-level seed of lensing: "
          "geometry reads geometry\n")


if __name__ == "__main__":
    s1_free_locality()
    s2_vertex_coupling()
    s3_first_order()
    s4_orientation_lensing()
    print("all assertions passed")
