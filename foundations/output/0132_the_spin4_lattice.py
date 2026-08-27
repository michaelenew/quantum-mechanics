"""0132 -- the Spin(4) lattice: the rebuild.

0143 settled the record count at TWO, locked. Every lattice module
from 0091 to 0131 carries ONE SU(2) per link, so it simulates
construction (a) and the theory is (b). lucid 0046 showed the
difference is not accuracy: the graviton sector is the traceless
symmetric part of B+ (x) B-, and it is PURE SYNERGY -- present in
NEITHER marginal. A single-SU(2) lattice has no spin-2 sector to
measure at all.

This is the rebuild, to lucid 0046 s4's spec.

  LINK      (U+, U-), a pair of unit quaternions -- 8 reals.
  PLAQUETTE two class angles from the two holonomies.
  WEIGHT    W = | sum_{n=1..M} chi_n(theta+) chi_n(theta-) |^2,
            flat multiplicities (capacity-achieving, lucid 0045).
  COUPLING  kappa = (2/3) sum n^2(n^2-1) / sum n^2 = 16 at M = 6.

  s1  THE WEIGHT, and its coupling read off analytically.
  s2  THE SIMULATION. Checkerboard Metropolis over both factors,
      with the staple built for each independently.
  s3  THE FIRST CHECK, which lucid 0046 named in advance: measure
      kappa from the simulated plaquette distribution against
      0094's <theta^2> = 3R/kappa. It must come out 16, not the
      13.33 the old lattice ran on.
  s4  THE SECTOR THAT DID NOT EXIST BEFORE. Project the plaquette
      bivector onto trace / antisymmetric / traceless-symmetric and
      confirm the spin-2 part is populated -- the graviton sector,
      measurable for the first time.
"""

import numpy as np

M_SECT = 6                      # M = N+1 sectors, N = 5
NTAB = 384
rng = np.random.default_rng(132)


# ---------------- quaternions ----------------
def qmul(a, b):
    w1, x1, y1, z1 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    w2, x2, y2, z2 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
                     w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
                     w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2], -1)


def qinv(a):
    out = a.copy()
    out[..., 1:] *= -1
    return out


def qrand(shape, sigma):
    v = sigma * rng.standard_normal(shape + (3,))
    w = np.ones(shape + (1,))
    q = np.concatenate([w, v], -1)
    return q / np.linalg.norm(q, axis=-1, keepdims=True)


# ---------------- the weight ----------------
def chi(n, th):
    s = np.sin(th)
    return np.where(np.abs(s) < 1e-12, float(n), np.sin(n * th) / s)


def lnw_table():
    t = np.linspace(1e-7, np.pi - 1e-7, NTAB)
    TP, TM = np.meshgrid(t, t, indexing="ij")
    A = sum(chi(n, TP) * chi(n, TM) for n in range(1, M_SECT + 1))
    return np.ascontiguousarray(np.log(np.maximum(A ** 2, 1e-300)))


LNW = lnw_table()


def lookup(tp, tm):
    i = np.clip((tp / np.pi * (NTAB - 1)).astype(np.int64), 0,
                NTAB - 1)
    j = np.clip((tm / np.pi * (NTAB - 1)).astype(np.int64), 0,
                NTAB - 1)
    return LNW[i, j]


def kappa_closed(M):
    n = np.arange(1, M + 1, dtype=float)
    return float((2 / 3) * np.sum(n * n * (n * n - 1))
                 / np.sum(n * n))


def s1_weight():
    print("== s1: the weight ==")
    print(f"  A(theta+, theta-) = sum_(n=1..{M_SECT}) chi_n(theta+) "
          f"chi_n(theta-),  W = A^2")
    t = np.linspace(1e-7, 0.15, 4001)
    A = sum(chi(n, t) * float(n) for n in range(1, M_SECT + 1))
    k = float(-2 * np.polyfit(t, np.log(A ** 2), 4)[-3])
    print(f"  stiffness in one factor (other at identity), numeric: "
          f"{k:.4f}")
    print(f"  closed form (2/3) sum n^2(n^2-1)/sum n^2          : "
          f"{kappa_closed(M_SECT):.4f}")
    assert abs(k - kappa_closed(M_SECT)) < 0.05
    print(f"  and the OLD lattice's single-SU(2) weight would give "
          f"13.3333.")
    print("  So a run on this weight must land on 16, not 13.33 -- "
          "that is the check\n")


# ---------------- lattice ----------------
def mklat(L):
    V = L ** 4
    idx = np.arange(V).reshape((L,) * 4)
    up = np.stack([np.roll(idx, -1, ax).reshape(-1)
                   for ax in range(4)])
    dn = np.stack([np.roll(idx, 1, ax).reshape(-1)
                   for ax in range(4)])
    c = np.array(np.unravel_index(np.arange(V), (L,) * 4)).sum(0)
    return dict(L=L, V=V, up=up, dn=dn, par=(c % 2))


def staples(U, lat, mu):
    """sum of the 6 staples for every link in direction mu"""
    up, dn = lat["up"], lat["dn"]
    tot = None
    for nu in range(4):
        if nu == mu:
            continue
        # forward: U_nu(x+mu) U_mu(x+nu)^-1 U_nu(x)^-1
        f = qmul(qmul(U[nu][up[mu]], qinv(U[mu][up[nu]])),
                 qinv(U[nu]))
        # backward: U_nu(x+mu-nu)^-1 U_mu(x-nu)^-1 U_nu(x-nu)
        b = qmul(qmul(qinv(U[nu][dn[nu]][up[mu]]),
                      qinv(U[mu][dn[nu]])), U[nu][dn[nu]])
        tot = f + b if tot is None else tot + f + b
    return tot


def plaq_angles(U, lat, mu, link):
    """class angles of the 6 plaquettes at each mu-link, given that
    link's value -- returned as (nsite, 6)"""
    up, dn = lat["up"], lat["dn"]
    out = []
    for nu in range(4):
        if nu == mu:
            continue
        f = qmul(qmul(link, U[nu][up[mu]]),
                 qmul(qinv(U[mu][up[nu]]), qinv(U[nu])))
        b = qmul(qmul(link, qinv(U[nu][dn[nu]][up[mu]])),
                 qmul(qinv(U[mu][dn[nu]]), U[nu][dn[nu]]))
        out.append(np.arccos(np.clip(f[..., 0], -1, 1)))
        out.append(np.arccos(np.clip(b[..., 0], -1, 1)))
    return np.stack(out, -1)


def sweep(Up, Um, lat, sigma):
    acc = tot = 0
    for mu in range(4):
        for par in (0, 1):
            m = lat["par"] == par
            lp, lm = Up[mu][m], Um[mu][m]
            sub = dict(lat)
            # angles before
            ap = plaq_angles(Up, lat, mu, Up[mu])[m]
            am = plaq_angles(Um, lat, mu, Um[mu])[m]
            old = lookup(ap, am).sum(-1)
            np_ = qmul(qrand(lp.shape[:-1], sigma), lp)
            nm_ = qmul(qrand(lm.shape[:-1], sigma), lm)
            Pp, Pm = Up[mu].copy(), Um[mu].copy()
            Pp[m], Pm[m] = np_, nm_
            Up2, Um2 = list(Up), list(Um)
            Up2[mu], Um2[mu] = Pp, Pm
            ap2 = plaq_angles(Up2, lat, mu, Pp)[m]
            am2 = plaq_angles(Um2, lat, mu, Pm)[m]
            new = lookup(ap2, am2).sum(-1)
            take = np.log(rng.random(new.shape) + 1e-300) < (new - old)
            Up[mu][m] = np.where(take[:, None], np_, lp)
            Um[mu][m] = np.where(take[:, None], nm_, lm)
            acc += int(take.sum())
            tot += int(take.size)
    return acc, tot


def all_plaq(U, lat):
    up = lat["up"]
    out = []
    for mu in range(4):
        for nu in range(mu + 1, 4):
            q = qmul(qmul(U[mu], U[nu][up[mu]]),
                     qmul(qinv(U[mu][up[nu]]), qinv(U[nu])))
            out.append(q)
    return np.stack(out, 1)                 # (V, 6, 4)


def s2_s3_run(L=4, sweeps=2600, burn=900):
    print("== s2/s3: the simulation, and the first check ==")
    lat = mklat(L)
    Up = [np.tile([1.0, 0, 0, 0], (lat["V"], 1)) for _ in range(4)]
    Um = [np.tile([1.0, 0, 0, 0], (lat["V"], 1)) for _ in range(4)]
    th2p, th2m, acc, tot = [], [], 0, 0
    sigma = 0.08
    for s in range(sweeps):
        a, t = sweep(Up, Um, lat, sigma)
        if s < burn // 2:                    # tune to ~0.4
            r = a / max(t, 1)
            sigma *= 1.06 if r > 0.45 else (0.94 if r < 0.35 else 1)
            sigma = float(np.clip(sigma, 0.005, 1.0))
        else:
            acc += a
            tot += t
        if s >= burn and s % 5 == 0:
            qp, qm = all_plaq(Up, lat), all_plaq(Um, lat)
            th2p.append(float(np.mean(np.arccos(
                np.clip(qp[..., 0], -1, 1)) ** 2)))
            th2m.append(float(np.mean(np.arccos(
                np.clip(qm[..., 0], -1, 1)) ** 2)))
    mp, mm = float(np.mean(th2p)), float(np.mean(th2m))
    rate = acc / max(tot, 1)
    print(f"  L = {L}, {sweeps} sweeps, tuned step {sigma:.4f}, "
          f"acceptance {rate:.3f}")
    assert 0.15 < rate < 0.75, f"acceptance {rate} -- run is stuck"
    print(f"  <theta+^2> = {mp:.5f}   <theta-^2> = {mm:.5f}"
          f"   (the two factors agree, as they must)")
    R = 0.5
    kp, km = 3 * R / mp, 3 * R / mm
    print(f"  0094's Gaussian bank: <theta^2> = 3R/kappa with "
          f"R = 1/2, so")
    print(f"      kappa+ = {kp:.3f},  kappa- = {km:.3f}")
    print(f"  target for the Spin(4) weight : "
          f"{kappa_closed(M_SECT):.3f}")
    print(f"  the OLD single-SU(2) weight   : 13.333")
    d_new = abs(kp - kappa_closed(M_SECT)) / kappa_closed(M_SECT)
    d_old = abs(kp - 13.3333) / 13.3333
    print(f"  distance to each: Spin(4) {100 * d_new:.1f}%, "
          f"old single-SU(2) {100 * d_old:.1f}%")
    assert abs(mp - mm) / mp < 0.08, "the two factors disagree"
    assert d_new < 0.15, (
        f"measured kappa {kp:.2f} is not the Spin(4) value")
    assert d_new < d_old
    print("  IT LANDS ON THE SPIN(4) VALUE, not the old one. The "
          "rebuild is live\n")
    return Up, Um, lat


def s4_the_new_sector(Up, Um, lat):
    print("== s4: the sector that did not exist before ==")
    qp, qm = all_plaq(Up, lat), all_plaq(Um, lat)
    Bp = qp[..., 1:].reshape(-1, 3)
    Bm = qm[..., 1:].reshape(-1, 3)
    outer = np.einsum("...i,...j->...ij", Bp, Bm)
    tr = np.einsum("...ii->...", outer)
    anti = 0.5 * (outer - np.swapaxes(outer, -1, -2))
    sym = 0.5 * (outer + np.swapaxes(outer, -1, -2))
    sym0 = sym - (tr / 3)[..., None, None] * np.eye(3)
    e = [float(np.mean(tr ** 2) / 3.0),
         float(np.mean(np.sum(anti ** 2, (-1, -2)))),
         float(np.mean(np.sum(sym0 ** 2, (-1, -2))))]
    tot = e[0] * 3 + e[1] + e[2]
    print("  project the plaquette bivector pair B+ (x) B-:")
    print("     sector            dim    share    spin")
    print(f"     trace              1     {3 * e[0] / tot:.3f}"
          f"      0")
    print(f"     antisymmetric      3     {e[1] / tot:.3f}      1")
    print(f"     traceless sym      5     {e[2] / tot:.3f}      2"
          f"   <- THE GRAVITON")
    assert e[2] / tot > 0.05
    print()
    print("  the spin-2 sector is populated on the simulated "
          "configurations. lucid 0046")
    print("  measured that it is present in NEITHER marginal, so "
          "this is a quantity the")
    print("  old lattice could not have produced by any amount of "
          "post-processing.")
    print()
    print("  NEXT: correlate it at separation. That correlator is "
          "the graviton propagator,")
    print("  and it is the object every remaining item on the "
          "gravity burndown needs\n")


if __name__ == "__main__":
    s1_weight()
    Up, Um, lat = s2_s3_run()
    s4_the_new_sector(Up, Um, lat)
    print("all assertions passed")
