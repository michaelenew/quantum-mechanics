"""0101 -- the vertex response: the leading TC insertion, priced
against the measured deficit.

0107 proved the vertex is the total correlation the product measure
drops; 0104 measured the dressed vacuum sitting ~10% BELOW its
Gaussian-bank baseline in the scale-field observables. This module
connects them: the linear response of the dressed observables to the
leading TC insertion,

    dW -> W exp(+eps sum_sites sum_{p<q at site} F_p . F_q),

(F_p = theta_p * axis_p, the plaquette curvature bivectors; the
isotropic pairwise coupling is the Gaussian-leading form of any
TC-positive vertex). Linear response d<O>/d eps = Cov(O, S1) from
the ordered-branch lattice ensemble (C kernel, 4 chains), for
O in {<th^2>, SD_sites(ln rho), c(1)}. Deliverable (as measured): the marginal
responds cleanly to the insertion; both scale-field responses are
NULL at 8-chain precision -- the isotropic leading TC term is
DISFAVORED as the source of the measured ~10% deficit, which
therefore selects orientation-dependent vertex structure (0088's
lensing) or higher order. A discriminating negative.
"""

import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "m92", os.path.join(HERE, "0092_the_coupling_scan.py"))
m92 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m92)

L = 4
LAT = m92.mklat(L)
V = LAT["V"]
SWEEPS, BURN, EVERY = 12000, 800, 5
CHAINS = 8


def plaq_F(links):
    """Curvature bivectors F_p = theta * axis, (V, 6, 3)."""
    out = []
    for mu in range(4):
        for nu in range(mu + 1, 4):
            a = links[mu]
            b = links[nu][LAT["sh"][(mu, 1)]]
            c = m92.qinv_np(links[mu][LAT["sh"][(nu, 1)]])
            d = m92.qinv_np(links[nu])
            q = m92.qmul_np(m92.qmul_np(a, b), m92.qmul_np(c, d))
            th = np.arccos(np.clip(q[..., 0], -1, 1))
            vec = q[..., 1:]
            nrm = np.linalg.norm(vec, axis=-1, keepdims=True)
            out.append(th[..., None] * vec / np.maximum(nrm, 1e-12))
    return np.stack(out, axis=1)          # (V, 6, 3)


def run_chain(k):
    tab = m92.lnw_table(0.0)
    rs = m92.seed_state(31000 + k)
    rsh = np.random.default_rng(70 + k)
    links = np.ascontiguousarray(
        np.tile([1.0, 0, 0, 0], (4, V, 1)))
    m92.c_sweeps(links, LAT, 5, 1.5, tab, rs)     # ordered start
    obs = []
    done = 0
    while done < SWEEPS:
        m92.c_sweeps(links, LAT, EVERY, 0.5, tab, rs)
        done += EVERY
        if done <= BURN:
            continue
        F = plaq_F(links)
        TH2 = np.linalg.norm(F, axis=2) ** 2      # (V, 6)
        th2 = float(TH2.mean())
        # site scale field, with a within-config shuffle control
        lnr = np.log(np.sqrt(TH2.mean(axis=1)))
        flat = TH2.ravel().copy()
        rsh.shuffle(flat)
        lnrs = np.log(np.sqrt(flat.reshape(V, 6).mean(axis=1)))
        sP = float(lnr.std() - lnrs.std())        # the exc
        x = lnr - lnr.mean()
        c1 = float(np.mean([np.mean(x * x[LAT["sh"][(mu, 1)]])
                            for mu in range(4)]) / np.mean(x ** 2))
        # the insertion statistic: pairwise F_p . F_q within sites
        G = np.einsum("vpa,vqa->vpq", F, F)
        S1 = float((G.sum(axis=(1, 2)) - np.einsum("vpp->v", G))
                   .sum() / 2)
        obs.append((th2, sP, c1, S1))
    return np.array(obs)


if __name__ == "__main__":
    print("== the vertex response: leading TC insertion vs the "
          "measured deficit ==")
    names = ["<th^2>", "sP_exc", "c(1)"]
    slopes = []
    for k in range(CHAINS):
        O = run_chain(k)
        S1 = O[:, 3]
        sl = [np.cov(O[:, i], S1)[0, 1] for i in range(3)]
        slopes.append(sl)
    S = np.array(slopes)
    mean, se = S.mean(0), S.std(0) / np.sqrt(CHAINS)
    print(f"  ({CHAINS} chains x {(SWEEPS - BURN) // EVERY} "
          f"measurements, ordered branch, tau = 0)")
    # measured deficits vs the Gaussian bank (0104/0092):
    # measured minus Gaussian-bank baseline (0092 / 0094):
    deficits = {"sP_exc": 0.0120 - 0.0134,
                "c(1)": 0.0474 - 0.0515}
    for i, n in enumerate(names):
        line = f"  d<{n}>/d eps = {mean[i]:+.4f} +- {se[i]:.4f}"
        if n in deficits:
            eps_star = deficits[n] / mean[i]
            line += (f"   deficit {deficits[n]:+.4f} -> "
                     f"eps* = {eps_star:+.4f}")
        print(line)
    assert mean[0] > 3 * se[0]              # th^2 channel resolved
    sp_null = abs(mean[1]) < 3 * se[1]
    c1_null = abs(mean[2]) < 3 * se[2]
    print("  verdict: the marginal responds cleanly; BOTH "
          "scale-field responses are null")
    print(f"  at this precision (|d sP/deps| < {3 * se[1]:.4f}, "
          f"|d c1/deps| < {3 * se[2]:.4f}).")
    print("  Closing the measured deficits with this operator would "
          "need |eps| >~ 1-4 --")
    print("  outside linear response. THE ISOTROPIC LEADING TC TERM "
          "IS DISFAVORED as the")
    print("  deficit's source: the vertex correction to the scale "
          "field must enter through")
    print("  orientation-dependent structure (0088's lensing) or "
          "higher order. An honest")
    print("  discriminating negative -- the deficit now selects "
          "among vertex operators.")
    assert sp_null and c1_null
    print("all assertions passed")
