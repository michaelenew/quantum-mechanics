"""0091 -- the lattice MC: the dressed vacuum's mixture, measured.

The catalogue's named discriminator (0100): the group-level and
algebra-level local models disagree about whether the derived vacuum
is a scale mixture. This module runs the real thing: 4D SU(2) lattice
gauge theory with the derived Born plaquette weight W = A^2,
A = sum_{j<=J} chi_j (flat counting, J = 2.5 -- the N = 5 stack's
cutoff), Metropolis over link variables, compactness intrinsic (no
box). It measures the DRESSED vacuum:

  o1  the dressed single-plaquette marginal: radial-mixture statistic
      SD(ln theta) and kurtosis proxy, against (a) the bare Born
      weight and (b) the second-moment-matched Gaussian radial law;
  o2  the per-site scale field rho_x (RMS of the six plaquette angles
      based at x): SD(ln rho) against a within-config shuffle control
      -- genuine spatial scale CLUSTERING (the lattice s_P);
  o3  the spatial autocorrelation of ln rho at distance 1, 2 (the
      lattice phi).

DURABILITY: map/reduce over independent chains. Each chain
checkpoints its full state (links, RNG state, samples) atomically to
output/mc0091/chain_<k>.npz every CKPT sweeps and is resumable from
the checkpoint; `reduce` combines whatever chains are complete.
Running the module executes any unfinished chains (resuming if
checkpoints exist), then reduces.

Correctness gates (run first): exact gauge invariance of plaquette
angles; the free (J = 0) theory reproduces the Haar class
distribution.
"""

import json
import os
import time

import numpy as np

# ----------------------------------------------------------------------
# configuration
# ----------------------------------------------------------------------

L = 4
V = L ** 4
JCUT = 2.5
SIG = 0.5
CHAINS = 4
SWEEPS = 4000
BURN = 800
MEAS_EVERY = 5
CKPT = 200
DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "mc0091")

COORD = np.array([[t, x, y, z] for t in range(L) for x in range(L)
                  for y in range(L) for z in range(L)])
SITES = np.arange(V)
PAR = COORD.sum(axis=1) % 2


def shift(s, mu, d=1):
    c = COORD[s].copy()
    c[:, mu] = (c[:, mu] + d) % L
    return c[:, 0] * L ** 3 + c[:, 1] * L ** 2 + c[:, 2] * L + c[:, 3]


SHIFT = {(mu, d): shift(SITES, mu, d) for mu in range(4)
         for d in (1, -1)}


def qmul(a, b):
    w1, x1, y1, z1 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    w2, x2, y2, z2 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
                     w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
                     w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2], axis=-1)


def qinv(a):
    b = a.copy()
    b[..., 1:] *= -1
    return b


def theta_class(q):
    return np.arccos(np.clip(q[..., 0], -1, 1))


JS = np.arange(0, JCUT + 0.1, 0.5)


def lnW(th, js=JS):
    th = np.clip(th, 1e-8, np.pi - 1e-8)
    A = np.zeros_like(th)
    for j in js:
        A += np.sin((2 * j + 1) * th) / np.sin(th)
    return 2 * np.log(np.maximum(np.abs(A), 1e-12))


def plaq_theta(links, b, mu, nu):
    a = links[mu][b]
    bb = links[nu][SHIFT[(mu, 1)][b]]
    c = qinv(links[mu][SHIFT[(nu, 1)][b]])
    d = qinv(links[nu][b])
    return theta_class(qmul(qmul(a, bb), qmul(c, d)))


CLS = [(mu, p) for mu in range(4) for p in (0, 1)]
NUS = {mu: [n for n in range(4) if n != mu] for mu in range(4)}


def sweep(links, rng, sig=SIG, js=JS):
    acc, tot = 0, 0
    for mu, p in CLS:
        s = SITES[PAR == p]
        old = links[mu][s].copy()
        ang = rng.normal(0, sig, len(s))
        ax = rng.normal(size=(len(s), 3))
        ax /= np.linalg.norm(ax, axis=1, keepdims=True)
        rot = np.concatenate([np.cos(ang / 2)[:, None],
                              np.sin(ang / 2)[:, None] * ax], axis=1)
        prop = qmul(rot, old)
        dln = np.zeros(len(s))
        for nu in NUS[mu]:
            for orient in ('up', 'down'):
                b = s if orient == 'up' else SHIFT[(nu, -1)][s]
                th_old = plaq_theta(links, b, mu, nu)
                links[mu][s] = prop
                th_new = plaq_theta(links, b, mu, nu)
                links[mu][s] = old
                dln += lnW(th_new, js) - lnW(th_old, js)
        accm = np.log(rng.random(len(s)) + 1e-300) < dln
        cur = links[mu][s]
        cur[accm] = prop[accm]
        links[mu][s] = cur
        acc += int(accm.sum())
        tot += len(s)
    return acc / tot


def all_plaq_thetas(links):
    out = []
    for mu in range(4):
        for nu in range(mu + 1, 4):
            out.append(plaq_theta(links, SITES, mu, nu))
    return np.stack(out, axis=1)          # (V, 6)


# ----------------------------------------------------------------------
# correctness gates
# ----------------------------------------------------------------------

def gates():
    print("== correctness gates ==")
    rng = np.random.default_rng(0)
    links = [np.tile([1.0, 0, 0, 0], (V, 1)) for _ in range(4)]
    # free theory: J = 0 -> Haar links
    ths = []
    for it in range(120):
        sweep(links, rng, sig=1.2, js=np.array([0.0]))
        if it > 40 and it % 4 == 0:
            ths.append(all_plaq_thetas(links).ravel())
    th = np.concatenate(ths)
    grid = np.linspace(0, np.pi, 100001)
    haar = np.sin(grid) ** 2
    haar /= np.trapezoid(haar, grid)
    m2h = np.trapezoid(haar * grid ** 2, grid)
    dev = abs(np.mean(th ** 2) / m2h - 1)
    print(f"  free (J=0): <th^2> = {np.mean(th ** 2):.4f} vs Haar "
          f"{m2h:.4f}  ({100 * dev:.1f}%)")
    assert dev < 0.02
    # gauge invariance
    g_ang = rng.normal(0, 2.0, V)
    g_ax = rng.normal(size=(V, 3))
    g_ax /= np.linalg.norm(g_ax, axis=1, keepdims=True)
    g = np.concatenate([np.cos(g_ang / 2)[:, None],
                        np.sin(g_ang / 2)[:, None] * g_ax], axis=1)
    th1 = plaq_theta(links, SITES, 0, 1)
    links2 = [qmul(qmul(g[SITES], links[mu]),
                   qinv(g[SHIFT[(mu, 1)][SITES]])) for mu in range(4)]
    th2 = plaq_theta(links2, SITES, 0, 1)
    print(f"  gauge invariance: max |dtheta| = "
          f"{np.abs(th1 - th2).max():.1e}")
    assert np.abs(th1 - th2).max() < 1e-12
    print("  gates passed\n")


# ----------------------------------------------------------------------
# map: run a chain with atomic, resumable checkpoints
# ----------------------------------------------------------------------

def ckpt_path(k):
    return os.path.join(DIR, f"chain_{k}.npz")


def save_chain(k, links, rng, done, thetas):
    os.makedirs(DIR, exist_ok=True)
    tmp = ckpt_path(k) + ".tmp.npz"
    np.savez_compressed(
        tmp, links=np.stack(links), done=done,
        thetas=np.array(thetas, dtype=np.float16),
        rng_state=json.dumps(rng.bit_generator.state))
    os.replace(tmp, ckpt_path(k))


def load_chain(k):
    d = np.load(ckpt_path(k), allow_pickle=False)
    links = [d["links"][mu].copy() for mu in range(4)]
    rng = np.random.default_rng()
    rng.bit_generator.state = json.loads(str(d["rng_state"]))
    return links, rng, int(d["done"]), list(d["thetas"])


def run_chain(k):
    if os.path.exists(ckpt_path(k)):
        links, rng, done, thetas = load_chain(k)
        if done >= SWEEPS:
            print(f"  chain {k}: complete ({done} sweeps)")
            return
        print(f"  chain {k}: resuming at sweep {done}")
    else:
        rng = np.random.default_rng(1000 + k)
        links = [np.tile([1.0, 0, 0, 0], (V, 1)) for _ in range(4)]
        # hot start to decorrelate chains
        for _ in range(5):
            sweep(links, rng, sig=1.5)
        done, thetas = 0, []
    t0 = time.time()
    while done < SWEEPS:
        acc = sweep(links, rng)
        done += 1
        if done > BURN and done % MEAS_EVERY == 0:
            thetas.append(all_plaq_thetas(links).astype(np.float16))
        if done % CKPT == 0:
            save_chain(k, links, rng, done, thetas)
    save_chain(k, links, rng, done, thetas)
    print(f"  chain {k}: {SWEEPS} sweeps in {time.time() - t0:.0f}s, "
          f"final acc {acc:.2f}, {len(thetas)} measurements")


# ----------------------------------------------------------------------
# reduce
# ----------------------------------------------------------------------

def bare_stats():
    grid = np.linspace(1e-7, np.pi - 1e-7, 200001)
    A = np.zeros_like(grid)
    for j in JS:
        A += np.sin((2 * j + 1) * grid) / np.sin(grid)
    p = A ** 2 * np.sin(grid) ** 2
    p /= np.trapezoid(p, grid)
    m2 = np.trapezoid(p * grid ** 2, grid)
    m4 = np.trapezoid(p * grid ** 4, grid)
    lt = np.trapezoid(p * np.log(grid), grid)
    l2 = np.trapezoid(p * np.log(grid) ** 2, grid)
    return m2, 9 / 5 * m4 / m2 ** 2, float(np.sqrt(l2 - lt ** 2))


def gauss_control(m2):
    grid = np.linspace(1e-7, np.pi - 1e-7, 200001)
    q = np.exp(-grid ** 2 / (2 * (m2 / 3))) * grid ** 2
    q /= np.trapezoid(q, grid)
    lt = np.trapezoid(q * np.log(grid), grid)
    l2 = np.trapezoid(q * np.log(grid) ** 2, grid)
    return float(np.sqrt(l2 - lt ** 2))


def reduce():
    print("== reduce ==")
    per_chain = []
    for k in range(CHAINS):
        links, rng, done, thetas = load_chain(k)
        assert done >= SWEEPS, f"chain {k} incomplete"
        T = np.array(thetas, dtype=np.float64)   # (nmeas, V, 6)
        th = T.ravel()
        m2 = np.mean(th ** 2)
        kurt = 9 / 5 * np.mean(th ** 4) / m2 ** 2
        sd_lnth = np.log(np.clip(th, 1e-6, None)).std()
        # per-site scale field
        rho = np.sqrt((T ** 2).mean(axis=2))      # (nmeas, V)
        lnr = np.log(rho)
        sP = lnr.std(axis=1).mean()
        # shuffle control (within config)
        rngs = np.random.default_rng(50 + k)
        Ts = T.copy()
        for i in range(len(Ts)):
            flat = Ts[i].ravel()
            rngs.shuffle(flat)
            Ts[i] = flat.reshape(V, 6)
        lnrs = np.log(np.sqrt((Ts ** 2).mean(axis=2)))
        sPs = lnrs.std(axis=1).mean()
        # spatial autocorrelation of ln rho at distance 1, 2
        cors = []
        for d in (1, 2):
            num, cnt = 0.0, 0
            for mu in range(4):
                sh = shift(SITES, mu, d)
                x = lnr - lnr.mean(axis=1, keepdims=True)
                num += (x * x[:, sh]).mean()
                cnt += 1
            var = ((lnr - lnr.mean(axis=1, keepdims=True)) ** 2).mean()
            cors.append(num / cnt / var)
        per_chain.append((m2, kurt, sd_lnth, sP, sPs,
                          cors[0], cors[1]))
    P = np.array(per_chain)
    mean = P.mean(axis=0)
    se = P.std(axis=0) / np.sqrt(len(P))
    m2b, kurtb, sdb = bare_stats()
    sdg = gauss_control(mean[0])
    print(f"  chains: {len(P)}, measurements/chain: "
          f"{(SWEEPS - BURN) // MEAS_EVERY}")
    print(f"  dressed <th^2> = {mean[0]:.4f} +- {se[0]:.4f}   "
          f"(bare Born: {m2b:.4f})")
    print(f"  dressed kurtosis proxy = {mean[1]:.2f} +- {se[1]:.2f}  "
          f"(bare: {kurtb:.2f}, Gaussian: 3)")
    print(f"  dressed SD(ln th) = {mean[2]:.3f} +- {se[2]:.3f}")
    print(f"  bare Born SD(ln th) = {sdb:.3f}; matched-Gaussian "
          f"control = {sdg:.3f}")
    verdict_mix = mean[2] > sdg + 3 * max(se[2], 1e-4)
    word = 'SURVIVES' if verdict_mix else 'DOES NOT SURVIVE'
    print(f"  RADIAL MIXTURE {word} dressing (dressed vs Gaussian "
          f"control)")
    print(f"  lattice s_P: SD_sites(ln rho) = {mean[3]:.4f} +- "
          f"{se[3]:.4f}  vs shuffle {mean[4]:.4f}")
    exc = mean[3] - mean[4]
    print(f"  scale clustering excess = {exc:+.4f}")
    print(f"  ln-rho spatial corr: d=1 {mean[5]:+.4f} +- {se[5]:.4f}, "
          f"d=2 {mean[6]:+.4f} +- {se[6]:.4f}")
    return dict(m2=mean[0], kurt=mean[1], sd=mean[2], sdb=sdb,
                sdg=sdg, sP=mean[3], sPsh=mean[4],
                c1=mean[5], c2=mean[6], mix=bool(verdict_mix))


if __name__ == "__main__":
    gates()
    print("== map: chains ==")
    for k in range(CHAINS):
        run_chain(k)
    print()
    out = reduce()
    print("\nall gates and chain assertions passed")
