"""0085 -- the assembled momentum: tree Maxwell, one-loop isotropy,
and where the sector physics actually lives.

The wall's last outstanding piece (A3: the momentum half of the
graviton propagator, with sector resolution) attacked perturbatively,
which 0078's identity sum s_k^2 = sum |F_p|^2 makes possible:

    price = sum|F_p|^2/(2 eps') - tr(S^4)/(4 eps'^2) + O(s^6)

  s1  The expansion, verified: the O(s^6) residual scales as amp^6.
  s2  TREE LEVEL IS SIX LATTICE MAXWELLS. The quadratic action is
      exactly sum|F_p|^2/(2 eps'): each bivector component is an
      independent massless lattice Maxwell field -- the momentum
      half's 1/k-hat^2 at tree level, with NO sector distinction:
      both polarization sectors (and everything else) massless.
  s3  THE ONE-LOOP ISOTROPY THEOREM (exact). The tadpole quadratic
      form of tr S^4 is EXACTLY isotropic: Q_ab = 4.75 delta_ab
      under a unit isotropic background (polarization matrix,
      machine-exact); and contracting with the TRUE same-site
      lattice covariance (computed with forward-difference phases;
      it has off-diagonal entries +-0.108) gives Q identical for
      SD / ASD / balanced test content to 1e-9 -- the off-diagonal
      covariance decouples from the tadpole EXACTLY (Q = 4.75 x
      T_diag). Consequences: at one loop the assembled vacuum has
      (i) no graviton mass -- masslessness protected, (ii) NO sector
      splitting -- the (1,0) lift is NOT a weak-coupling vacuum
      effect, (iii) the vertex's entire one-loop content is an
      isotropic field-strength renormalization whose sign matches
      0093's confining flow.
  s4  WHERE THE SECTOR PHYSICS LIVES: on backgrounds and at finite
      content. The finite-source split on a unit geometric
      background is +1.17 +- 0.12 nats (0089); the INFINITESIMAL
      (Hessian) split on the same backgrounds is pack-noisy and
      consistent with zero, and the finite-source split's sign
      crosses over near the regulator scale amp ~ sqrt(eps').
      Honest verdict: the lift is a finite-content background
      effect, absent from the weak-coupling vacuum propagator; its
      vacuum fate is a strong-coupling question (where 0093's flow
      runs anyway), needing the nonperturbative F-ensemble.
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


def wedge(a, b):
    return [a[i] * b[j] - a[j] * b[i] for (i, j) in PAIRS]


def tetrad_pack(rng):
    e = [[rng.gauss(0, 1) for _ in range(4)] for _ in range(4)]
    return [wedge(e[mu], e[nu]) for (mu, nu) in PAIRS]


def normalize(F):
    F = np.asarray(F, dtype=float)
    return list(F / np.linalg.norm(F))


def rand_sd_unit(rng, sign=+1):
    F = np.array([rng.gauss(0, 1) for _ in range(6)])
    G = (F + sign * STAR6 @ F) / 2
    return G / np.linalg.norm(G)


BAS = {}
for p in range(6):
    for a in range(6):
        Fs0 = [[0.0] * 6 for _ in range(6)]
        Fs0[p][a] = 1.0
        BAS[(p, a)] = build_S(Fs0)


def s1_expansion():
    print("== s1: the expansion ==")
    rng = random.Random(3)
    base = [[rng.gauss(0, 1) for _ in range(6)] for _ in range(6)]
    res = {}
    for amp in (0.01, 0.005):
        Fs = [[amp * x for x in F] for F in base]
        ev = np.linalg.eigvalsh(build_S(Fs))
        price = float(0.5 * np.sum(np.log(1 + ev ** 2 / EPSP)))
        q2 = sum(sum(x * x for x in F) for F in Fs) / (2 * EPSP)
        q4 = float(np.sum(ev ** 4)) / (4 * EPSP ** 2)
        res[amp] = abs(price - (q2 - q4))
        print(f"  amp={amp}: |price - (quad - quart)| = {res[amp]:.2e}")
    ratio = res[0.01] / res[0.005]
    assert 40 < ratio < 90, ratio
    print(f"  same configuration halved: residual ratio = {ratio:.0f} "
          f"(~2^6 = 64): O(s^6), verified\n")


def s2_tree():
    print("== s2: tree level is six lattice Maxwells ==")
    rng = random.Random(5)
    for _ in range(10):
        Fs = [[rng.gauss(0, 1) for _ in range(6)] for _ in range(6)]
        ev = np.linalg.eigvalsh(build_S(Fs))
        f2 = sum(sum(x * x for x in F) for F in Fs)
        assert abs(float(np.sum(ev ** 2)) - f2) < 1e-9 * f2
    print("  sum s_k^2 = sum |F_p|^2 (0078's identity, re-verified): "
          "the quadratic action is")
    print("  sum|F|^2/2eps' -- each bivector component an independent "
          "massless lattice Maxwell.")
    print("  The momentum half at tree level: 1/k-hat^2, massless, "
          "sector-blind\n")


def _lattice_T(L=16):
    ks = 2 * np.pi * np.arange(L) / L
    grid = np.meshgrid(ks, ks, ks, ks, indexing='ij')
    kt = [2 * np.sin(g / 2) * np.exp(1j * g / 2) for g in grid]
    k2 = sum(np.abs(x) ** 2 for x in kt)
    k2[0, 0, 0, 0] = 1.0
    inv = 1.0 / k2
    inv[0, 0, 0, 0] = 0.0
    T = np.zeros((6, 6))
    for i, (m, n) in enumerate(PAIRS):
        for j, (r, s) in enumerate(PAIRS):
            val = np.zeros_like(k2, dtype=complex)
            for (a, b, c, d, sgn) in ((m, r, n, s, 1), (m, s, n, r, -1),
                                      (n, r, m, s, -1), (n, s, m, r, 1)):
                if c == d:
                    val += sgn * kt[a] * np.conj(kt[b])
            T[i, j] = float(np.mean((val * inv).real))
    return T


def _Q_cov(F0, T):
    Fs = [[0.0] * 6 for _ in range(6)]
    Fs[0] = list(F0)
    S0 = build_S(Fs)
    S02 = S0 @ S0
    tot = 0.0
    for p in range(6):
        for q in range(6):
            if abs(T[p, q]) < 1e-12:
                continue
            for a in range(6):
                Bp, Bq = BAS[(p, a)], BAS[(q, a)]
                tot += T[p, q] * (2 * np.trace(S02 @ (Bp @ Bq))
                                  + np.trace(S0 @ Bp @ S0 @ Bq))
    return float(tot)


def s3_isotropy():
    print("== s3: the one-loop isotropy theorem ==")
    # polarization matrix under unit isotropic covariance
    I6 = np.eye(6)
    Qm = np.zeros((6, 6))
    for a in range(6):
        for b in range(6):
            ea = list(I6[a])
            eb = list(I6[b])
            fab = [x + y for x, y in zip(ea, eb)]
            Qm[a, b] = 0.5 * (_Q_cov(fab, I6) - _Q_cov(ea, I6)
                              - _Q_cov(eb, I6))
    assert np.allclose(Qm, 4.75 * np.eye(6), atol=1e-9)
    print("  isotropic covariance: Q_ab = 4.75 delta_ab exactly "
          "(polarization, machine-exact)")
    T = _lattice_T()
    off = np.abs(T - np.diag(np.diag(T))).max()
    print(f"  true lattice covariance: diag {T[0, 0]:.4f}, max "
          f"|offdiag| {off:.4f}")
    r2 = random.Random(100)
    sd = list(rand_sd_unit(r2, +1))
    asd = list(rand_sd_unit(r2, -1))
    Fp = rand_sd_unit(r2, +1)
    Fm = rand_sd_unit(r2, -1)
    bal = normalize(np.array(Fp) + np.array(Fm))
    qs = [_Q_cov(F, T) for F in (sd, asd, bal)]
    print(f"  Q with true covariance: SD {qs[0]:.6f}, ASD {qs[1]:.6f},"
          f" balanced {qs[2]:.6f}")
    assert max(qs) - min(qs) < 1e-9
    assert abs(qs[0] - 4.75 * T[0, 0]) < 1e-6
    print("  identical, and equal to 4.75 x T_diag: the off-diagonal "
          "covariance decouples EXACTLY.")
    print("  One loop, vacuum: no graviton mass, no sector splitting; "
          "the vertex's whole effect")
    print("  is isotropic field-strength renormalization "
          "(0093's confining sign, diagrammatic)\n")


def s4_background():
    print("== s4: where the sector physics lives ==")
    rng = random.Random(7)
    t = 1e-3
    outs = []
    for _ in range(16):
        pack = [normalize(F) for F in tetrad_pack(rng)]
        Fp = rand_sd_unit(rng, +1)
        Fm = rand_sd_unit(rng, -1)
        sdu = list(Fp)
        balu = normalize(np.array(Fp) + np.array(Fm))

        def D2(F0):
            Pp = [[a + t * b for a, b in zip(pack[0], F0)]] + pack[1:]
            Pm = [[a - t * b for a, b in zip(pack[0], F0)]] + pack[1:]
            return (vertex_price(Pp) + vertex_price(Pm)
                    - 2 * vertex_price(pack)) / t ** 2

        outs.append(D2(sdu) - D2(balu))
    o = np.array(outs)
    print(f"  infinitesimal (Hessian) split on unit geometric "
          f"backgrounds: {o.mean():+.2f} +- "
          f"{o.std() / np.sqrt(len(o)):.2f}  (pack-noisy, consistent "
          f"with 0)")
    print("  finite-source split on the same backgrounds: +1.17 +- "
          "0.12 nats (0089), with a")
    print("  sign crossover near amp ~ sqrt(eps') measured in the "
          "amplitude scan.")
    print("  Verdict: the (1,0) lift is a FINITE-CONTENT BACKGROUND "
          "effect -- absent from the")
    print("  weak-coupling vacuum propagator (s3's theorem), present "
          "for real content on real")
    print("  geometry. Its vacuum fate at strong coupling needs the "
          "nonperturbative F-ensemble\n")


if __name__ == "__main__":
    s1_expansion()
    s2_tree()
    s3_isotropy()
    s4_background()
    print("all assertions passed")
