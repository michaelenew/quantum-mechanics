"""0087 -- the marginalized vacuum: the ridge tilts, and the tilted
coordinate is the scale.

Step 1 of the owner's plan: build the filter's marginalization move in
the physics, on analogy alone. Their move (lucid-filter oracle-gap):
the GPB1 collapse -- one shared covariance for the whole hypothesis
bank -- makes the likelihood exactly flat along a ridge; per-hypothesis
memory (IMM) tilts it; and the boundary is ill-posed for any point
estimator, so the spread parameter must be MARGINALIZED: "a hypothesis
set is not a point."

The physics ridge is 0095's exact theorem: expanding around the point
vacuum (F = 0, Gaussian summary), sector structure is EXACTLY flat --
no SD/balanced splitting at one loop. The experiment: replace the
point vacuum with hypothesis-set vacua, SECOND MOMENTS MATCHED (the
collapsed summaries are identical by construction), and measure the
sector split of a source probe.

  s1  Three background ensembles on the six-plaquette vertex, same
      36x36 covariance: H1 = geometric mixture (random tetrad packs;
      kurtosis ~ 5.9), H0 = the Gaussian collapse of H1 (Cholesky of
      H1's sample covariance; kurtosis 3), H2 = scale mixture of H0
      (two-point radial mixing; kurtosis ~ 6.0, no geometric
      structure).
  s2  THE RIDGE TILTS. Sector split of a t = 0.5 source on slot 0
      (paired SD vs balanced probes, common backgrounds):
        isolated (no background):        +1.71
        H0  collapsed Gaussian vacuum:   +0.004 +- 0.002   -- flat
        H1  geometric mixture:           +0.46  +- 0.005   -- ~90 sigma
        H2  scale mixture (no geometry): +0.52  +- 0.010   -- ~50 sigma
      Same second moments; the collapsed vacuum erases sector
      structure entirely (the bath screens at its mean strength); the
      marginalized vacua keep it alive.
  s3  THE ATTRIBUTION. H2 ~ H1: at this observable the sector
      information rides the RADIAL mixture -- epochs of weak bath
      where discrimination is strong -- not the tetrad orientation
      structure (which, if anything, screens slightly more:
      H1 - H2 = -0.06). The marginalized coordinate that matters is
      the SCALE. In the filter's own words: the sector physics lives
      in the wandering-scale channel (s_P > 0); the collapsed vacuum
      is their self-confirming s_P = 0; and their next design item --
      marginalize the (phi_P, s_P) grid -- is precisely what the
      physical vacuum needs.
  s4  Success criterion (set in advance): met. The flat direction of
      the collapsed treatment is an artifact of the collapse; the
      mixture the collapse deletes carries the sector structure. This
      also closes a loop with 0092: the ledger's high kurtosis -- the
      thing RG localization must kill for heat-kernel universality --
      is the same structure that carries sector information at the
      vertex. Universality and sector-blindness are one phenomenon;
      discrimination lives in the non-Gaussian remainder.
"""

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


def rand_sd_unit(rr, sign=+1):
    F = np.array([rr.gauss(0, 1) for _ in range(6)])
    G = (F + sign * STAR6 @ F) / 2
    return G / np.linalg.norm(G)


RNG = np.random.default_rng(3)
T = 0.5
NBG = 2000


def draw_h1():
    e = RNG.normal(size=(4, 4))
    Fs = np.array([[e[m][i] * e[n][j] - e[m][j] * e[n][i]
                    for (i, j) in PAIRS] for (m, n) in PAIRS], float)
    return 0.35 * Fs


def make_ensembles():
    X = np.array([draw_h1().ravel() for _ in range(4000)])
    C = np.cov(X.T)
    Lc = np.linalg.cholesky(C + 1e-10 * np.eye(36))
    kurt1 = float((((X - X.mean(0)) ** 4).mean(0)
                   / (X.var(0) ** 2)).mean())

    def draw_h0():
        return (Lc @ RNG.normal(size=36)).reshape(6, 6)

    delta = 0.99

    def draw_h2():
        a2 = 1.0 + delta if RNG.random() < 0.5 else 1.0 - delta
        return np.sqrt(a2) * (Lc @ RNG.normal(size=36)).reshape(6, 6)

    # verify the moment matching
    X0 = np.array([draw_h0().ravel() for _ in range(4000)])
    X2 = np.array([draw_h2().ravel() for _ in range(4000)])
    sd1, sd0, sd2 = [np.sqrt(A.var(0)).mean() for A in (X, X0, X2)]
    kurt0 = float((((X0 - X0.mean(0)) ** 4).mean(0)
                   / (X0.var(0) ** 2)).mean())
    kurt2 = float((((X2 - X2.mean(0)) ** 4).mean(0)
                   / (X2.var(0) ** 2)).mean())
    print("== s1: three vacua, one collapsed summary ==")
    print(f"  per-component SD: H1 {sd1:.4f}  H0 {sd0:.4f}  "
          f"H2 {sd2:.4f}  (matched)")
    print(f"  kurtosis:         H1 {kurt1:.2f}   H0 {kurt0:.2f}   "
          f"H2 {kurt2:.2f}")
    assert abs(sd0 / sd1 - 1) < 0.05 and abs(sd2 / sd1 - 1) < 0.06
    assert kurt0 < 3.4 and kurt1 > 5 and kurt2 > 5
    print("  H0 is the GPB1 collapse of H1 by construction; H2 keeps "
          "the tails, drops the geometry\n")
    return draw_h0, draw_h2


PROBES = []
_r2 = random.Random(11)
for _ in range(4):
    Fp = rand_sd_unit(_r2, +1)
    Fm = rand_sd_unit(_r2, -1)
    bal = np.array(Fp) + np.array(Fm)
    PROBES.append((list(Fp), list(bal / np.linalg.norm(bal))))


def ens_split(draw, n):
    vals = []
    for _ in range(n):
        bg = draw()
        base = vertex_price([list(r) for r in bg])
        acc = 0.0
        for sd, balu in PROBES:
            b = [list(r) for r in bg]
            b[0] = [a + T * x for a, x in zip(bg[0], sd)]
            dsd = vertex_price(b) - base
            b = [list(r) for r in bg]
            b[0] = [a + T * x for a, x in zip(bg[0], balu)]
            dbal = vertex_price(b) - base
            acc += (dsd - dbal) / len(PROBES)
        vals.append(acc)
    v = np.array(vals)
    return float(v.mean()), float(v.std() / np.sqrt(n))


def main():
    draw_h0, draw_h2 = make_ensembles()
    iso = 0.0
    for sd, balu in PROBES:
        iso += (vertex_price([[T * x for x in sd]] + [[0.0] * 6] * 5)
                - vertex_price([[T * x for x in balu]]
                               + [[0.0] * 6] * 5)) / len(PROBES)
    print("== s2: the ridge tilts ==")
    print(f"  isolated split (no background): {iso:+.4f}")
    m1, e1 = ens_split(draw_h1, NBG)
    m0, e0 = ens_split(draw_h0, NBG)
    m2, e2 = ens_split(draw_h2, NBG)
    print(f"  H0 collapsed Gaussian : {m0:+.4f} +- {e0:.4f}   (flat)")
    print(f"  H1 geometric mixture  : {m1:+.4f} +- {e1:.4f}")
    print(f"  H2 scale mixture      : {m2:+.4f} +- {e2:.4f}")
    assert abs(m0) < max(5 * e0, 0.02)
    assert m1 > 20 * e1 and m2 > 20 * e2
    assert m1 > 10 * abs(m0) and m2 > 10 * abs(m0)
    print("  same second moments; the collapse erases the sector "
          "structure, the mixtures keep it\n")
    print("== s3: the attribution ==")
    print(f"  H1 - H2 = {m1 - m2:+.4f} +- {np.hypot(e1, e2):.4f}: "
          f"comparable -- the information rides the")
    print("  RADIAL mixture (weak-bath epochs), not the tetrad "
          "orientation. The marginalized")
    print("  coordinate that matters is the SCALE: the collapsed "
          "vacuum is the filter's")
    print("  self-confirming s_P = 0; their next design item "
          "(marginalize the scale grid) is")
    print("  what the physical vacuum needs\n")
    assert abs(m1 - m2) < 0.2
    print("== s4: criterion ==")
    print("  set in advance, met: the flat direction of the point-"
          "vacuum treatment is an")
    print("  artifact of the collapse; sector physics lives in the "
          "mixture the collapse")
    print("  deletes. (0092's coherence: the kurtosis RG localization "
          "kills for universality")
    print("  is the same structure carrying sector information -- "
          "universality and")
    print("  sector-blindness are one phenomenon)\n")


if __name__ == "__main__":
    main()
    print("all assertions passed")
