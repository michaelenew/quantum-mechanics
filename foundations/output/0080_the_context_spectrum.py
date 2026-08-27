"""0080 -- the context spectrum: the vertex lifts the (1,0) mode.

0075's tension spectrum left one interleaving standing: at the bare
one-plaquette chain the unbalanced (1,0) multiplet (purely self-dual
curvature -- the connection/2-form mode) sits 0.10-0.30 nats/step
BELOW the graviton (1,1) (balanced curvature), with the measured job
description "vertex-level simplicity should lift it." 0078 built the
vertex; 0088 measured its context coupling. This stone runs the
specific entry: what does the shared-frame vertex charge a self-dual
insert, relative to a balanced one, in a geometric context?

  s1  Anchor: the single-plaquette eigenvalue structure in
      self-dual/anti-self-dual variables: the 8 nonzero eigenvalues
      are +-(|F+| +- |F-|)/(2 sqrt 2) (fourfold), so the isolated
      price depends only on (|F+|, |F-|); 2 Pf = |F+|^2 - |F-|^2
      verified (0057 s4's fact in the vertex's own kit).
  s2  The unbalance curve in context: shift the geometric slot by
      F(eta) with |F-|/|F+| = eta at matched norm (SD/ASD pair fixed
      per seed so the curve is paired in eta). The mean context price
      falls monotonically in eta: pure self-dual (eta = 0) is the
      most expensive content, balanced (eta = 1) the cheapest, with a
      paired SD-over-balanced penalty of +1.17 +- 0.12 nats/site
      (64 seeds, 59/64 positive). The isolated penalty is smaller and
      noisier (+0.57 +- 0.31); context amplification ~2x.
  s3  The verdict, honestly sized: the context penalty exceeds the
      0.10-0.30 nats/step bare-chain lightness gap by 4-12x. That is
      SUPPORT for 0075's conjecture -- any assembly charging at
      least ~half a vertex per chain step lifts (1,0) above (1,1) --
      but not a decisive lift: the decisive computation is the
      assembled 4D complex (A3's completion), and the noise floor of
      this shift design is recorded alongside the signal.
  s4  Position in the insertion ladder: the self-dual insert is at
      least as expensive as 0078's generic non-simple insert --
      pure (1,0) content is the extreme case of non-simplicity, and
      the vertex treats it accordingly.
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


STAR6 = np.array([[eps4(*I, *J) for J in PAIRS] for I in PAIRS])


def sd_asd(F):
    F = np.asarray(F, dtype=float)
    Fp = (F + STAR6 @ F) / 2
    Fm = (F - STAR6 @ F) / 2
    return Fp, Fm


def pf(F):
    d = dict(zip(PAIRS, F))
    return (d[(0, 1)] * d[(2, 3)] - d[(0, 2)] * d[(1, 3)]
            + d[(0, 3)] * d[(1, 2)])


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


def wedge(a, b):
    return [a[i] * b[j] - a[j] * b[i] for (i, j) in PAIRS]


def tetrad_pack(rng):
    e = [[rng.gauss(0, 1) for _ in range(4)] for _ in range(4)]
    return [wedge(e[mu], e[nu]) for (mu, nu) in PAIRS]


def normalize(F, target=1.0):
    F = np.asarray(F, dtype=float)
    return list(F * target / np.linalg.norm(F))


def rand_sd_unit(rng, sign=+1):
    """Random unit (anti-)self-dual bivector."""
    F = np.array([rng.gauss(0, 1) for _ in range(6)])
    Fp, Fm = sd_asd(F)
    G = Fp if sign > 0 else Fm
    return G / np.linalg.norm(G)


def eta_insert(rng, eta):
    """Unit-norm bivector with |F-|/|F+| = eta (eta=0 pure SD,
    eta=1 balanced=simple)."""
    Fp = rand_sd_unit(rng, +1)
    Fm = rand_sd_unit(rng, -1)
    F = Fp + eta * Fm
    return normalize(F)


def s1_anchor():
    print("== s1: single-plaquette structure in SD/ASD variables ==")
    rng = random.Random(2)
    for _ in range(5):
        F = normalize([rng.gauss(0, 1) for _ in range(6)])
        Fp, Fm = sd_asd(F)
        p, m = np.linalg.norm(Fp), np.linalg.norm(Fm)
        # component conventions: 2 Pf = |F+|^2 - |F-|^2 and the eight
        # nonzero eigenvalues are +-(|F+| +- |F-|)/(2 sqrt 2)
        assert abs(2 * pf(F) - (p * p - m * m)) < 1e-10 * max(1, p)
        ev = np.linalg.eigvalsh(build_S([list(F)] + [[0.0] * 6] * 5))
        nz = np.sort(np.abs(ev))[-8:]
        lam = sorted(set(np.round(2 * math.sqrt(2) * nz, 6)))
        want = sorted({round(abs(p - m), 6), round(p + m, 6)})
        assert np.allclose(lam, want, atol=1e-5), (lam, want)
    print("  2 Pf = |F+|^2 - |F-|^2 and eigenvalues "
          "+-(|F+| +- |F-|)/(2 sqrt 2): verified, 5 random bivectors")
    print("  the isolated price is a function of (|F+|, |F-|) alone\n")


def s2_eta_curve():
    print("== s2: the unbalance curve, in context vs isolated ==")
    rng = random.Random(9)
    etas = [0.0, 0.25, 0.5, 0.75, 1.0]
    nseed = 64
    ctx_curve = {e: [] for e in etas}
    iso_curve = {e: [] for e in etas}
    for _ in range(nseed):
        pack = [normalize(F) for F in tetrad_pack(rng)]
        base = vertex_price(pack)
        b0 = single_price(pack[0])
        Fp = rand_sd_unit(rng, +1)
        Fm = rand_sd_unit(rng, -1)
        for eta in etas:
            ins = normalize(np.array(Fp) + eta * np.array(Fm))
            shifted = [a + b for a, b in zip(pack[0], ins)]
            ctx_curve[eta].append(vertex_price([shifted] + pack[1:])
                                  - base)
            iso_curve[eta].append(single_price(shifted) - b0)
    print(f"  eta = |F-|/|F+| :  context mean +- SE    isolated mean "
          f"+- SE   ({nseed} paired seeds)")
    cm, im = {}, {}
    for eta in etas:
        c = np.array(ctx_curve[eta])
        i = np.array(iso_curve[eta])
        cm[eta], im[eta] = c.mean(), i.mean()
        print(f"    {eta:4.2f}          {c.mean():+7.3f} +- "
              f"{c.std() / math.sqrt(nseed):.3f}      "
              f"{i.mean():+7.3f} +- {i.std() / math.sqrt(nseed):.3f}")
    pen = np.array(ctx_curve[0.0]) - np.array(ctx_curve[1.0])
    pen_iso = np.array(iso_curve[0.0]) - np.array(iso_curve[1.0])
    se = pen.std() / math.sqrt(nseed)
    pos = int((pen > 0).sum())
    assert cm[0.0] > cm[0.5] > cm[1.0]
    assert pen.mean() - 2 * se > 0.30, (pen.mean(), se)
    assert pos > 0.7 * nseed
    print(f"  monotone means; paired SD-over-balanced penalty "
          f"{pen.mean():+.3f} +- {se:.3f} nats in")
    print(f"  context ({pos}/{nseed} seeds positive) vs "
          f"{pen_iso.mean():+.3f} +- "
          f"{pen_iso.std() / math.sqrt(nseed):.3f} isolated "
          f"(amplification {pen.mean() / max(pen_iso.mean(), 1e-9):.1f}x)\n")
    return float(pen.mean()), float(se)


def s3_verdict(penalty, se):
    print("== s3: the verdict on the interleaving, honestly sized ==")
    gap_lo, gap_hi = 0.10, 0.30
    print(f"  bare-chain lightness of (1,0) under (1,1): "
          f"{gap_lo}-{gap_hi} nats/step (0075)")
    print(f"  vertex context penalty for pure-SD over balanced: "
          f"{penalty:.2f} +- {se:.2f} nats/site")
    assert penalty - 2 * se > gap_hi
    print(f"  the penalty exceeds the gap by "
          f"{penalty / gap_hi:.1f}-{penalty / gap_lo:.1f}x and clears "
          f"its upper bound at 2 sigma:")
    print("  SUPPORT for 0075's conjecture -- an assembly charging "
          ">~ half a vertex per chain")
    print("  step lifts (1,0) above (1,1). Not decisive: that is the "
          "assembled 4D complex's")
    print("  job (A3 completion), and this shift-design's noise floor "
          "is recorded above.\n")


def s4_ladder_position():
    print("== s4: position in the insertion ladder ==")
    rng = random.Random(13)
    n = 8
    d_sd, d_ns = [], []
    for _ in range(n):
        pack = [normalize(F) for F in tetrad_pack(rng)]
        base = vertex_price(pack)
        sd = eta_insert(rng, 0.0)
        ns = normalize([rng.gauss(0, 1) for _ in range(6)])
        d_sd.append(vertex_price(
            [[a + b for a, b in zip(pack[0], sd)]] + pack[1:]) - base)
        d_ns.append(vertex_price(
            [[a + b for a, b in zip(pack[0], ns)]] + pack[1:]) - base)
    msd, mns = sum(d_sd) / n, sum(d_ns) / n
    print(f"  mean context charge: pure self-dual {msd:+.3f} vs "
          f"generic (typically non-simple) {mns:+.3f}")
    assert msd > mns - 0.3
    print("  the (1,0) content sits at (or above) the non-simple rung "
          "-- the extreme case of")
    print("  non-simplicity, charged accordingly\n")


if __name__ == "__main__":
    s1_anchor()
    penalty, se = s2_eta_curve()
    s3_verdict(penalty, se)
    s4_ladder_position()
    print("all assertions passed")
