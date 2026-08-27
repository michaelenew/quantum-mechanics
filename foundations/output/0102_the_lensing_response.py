"""0102 -- the lensing response: which vertex operator moves the
scale field.

0111 found the isotropic pairwise term S_iso = sum F_p.F_q leaves
the scale-field observables untouched: the measured ~10% deficit
below the Gaussian baseline selects among vertex operators. This
module runs the selection: linear response of {<th^2>, sP_exc,
c(1)} to FOUR site-local operators built from the curvature
bivectors F_p (theta * axis):

  S_iso   = sum_{p<q} F_p . F_q            (0111's reference)
  S_mag   = sum_{p<q} |F_p|^2 |F_q|^2      (pure scale-scale)
  S_align = sum_{p<q} (F_p . F_q)^2        (orientation, parity-even
                                            -- 0088's lensing at
                                            leading order)
  S_chern = eps^{mu nu rho sigma} F.F      (the topological density;
                                            parity-ODD: its linear
                                            response to parity-even
                                            observables must vanish
                                            by symmetry -- a built-in
                                            null check)

Same harness as 0111 (ordered branch, tau = 0, C kernel).
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
# PAIRS order: (01),(02),(03),(12),(13),(23); duals under eps4:
# (01)<->(23) +, (02)<->(13) -, (03)<->(12) +
DUAL = [(0, 5, 1.0), (1, 4, -1.0), (2, 3, 1.0)]


def plaq_F(links):
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
    return np.stack(out, axis=1)


def run_chain(k):
    tab = m92.lnw_table(0.0)
    rs = m92.seed_state(41000 + k)
    rsh = np.random.default_rng(170 + k)
    links = np.ascontiguousarray(np.tile([1.0, 0, 0, 0], (4, V, 1)))
    m92.c_sweeps(links, LAT, 5, 1.5, tab, rs)
    obs = []
    done = 0
    while done < SWEEPS:
        m92.c_sweeps(links, LAT, EVERY, 0.5, tab, rs)
        done += EVERY
        if done <= BURN:
            continue
        F = plaq_F(links)
        TH2 = np.linalg.norm(F, axis=2) ** 2
        th2 = float(TH2.mean())
        lnr = np.log(np.sqrt(TH2.mean(axis=1)))
        flat = TH2.ravel().copy()
        rsh.shuffle(flat)
        lnrs = np.log(np.sqrt(flat.reshape(V, 6).mean(axis=1)))
        sP = float(lnr.std() - lnrs.std())
        x = lnr - lnr.mean()
        c1 = float(np.mean([np.mean(x * x[LAT["sh"][(mu, 1)]])
                            for mu in range(4)]) / np.mean(x ** 2))
        G = np.einsum("vpa,vqa->vpq", F, F)
        offd = G.sum(axis=(1, 2)) - np.einsum("vpp->v", G)
        s_iso = float(offd.sum() / 2)
        M2 = TH2
        s_mag = float(((M2.sum(1) ** 2 - (M2 ** 2).sum(1)) / 2)
                      .sum())
        s_align = float(((G ** 2).sum(axis=(1, 2))
                         - np.einsum("vpp->v", G ** 2)).sum() / 2)
        s_chern = float(sum(sgn * (F[:, a] * F[:, b]).sum()
                            for a, b, sgn in DUAL))
        obs.append((th2, sP, c1, s_iso, s_mag, s_align, s_chern))
    return np.array(obs)


if __name__ == "__main__":
    print("== the lensing response: four operators vs three "
          "observables ==")
    onames = ["<th^2>", "sP_exc", "c(1)"]
    snames = ["S_iso", "S_mag", "S_align", "S_chern"]
    allS = []
    for k in range(CHAINS):
        O = run_chain(k)
        sl = np.array([[np.cov(O[:, i], O[:, 3 + j])[0, 1]
                        for j in range(4)] for i in range(3)])
        allS.append(sl)
    A = np.array(allS)
    mean, se = A.mean(0), A.std(0) / np.sqrt(CHAINS)
    deficits = {"sP_exc": -0.0014, "c(1)": -0.0041}
    print(f"  ({CHAINS} chains x {(SWEEPS - BURN) // EVERY} meas; "
          f"entries: slope +- se; * = >3 sigma)")
    hdr = "            " + "".join(f"{s:>18s}" for s in snames)
    print(hdr)
    for i, n in enumerate(onames):
        row = f"  {n:9s}"
        for j in range(4):
            star = "*" if abs(mean[i, j]) > 3 * se[i, j] else " "
            row += f"  {mean[i, j]:+.4f}({se[i, j]:.4f}){star}"
        print(row)
    # symmetry null: chern responses vanish
    for i in range(3):
        assert abs(mean[i, 3]) < 3 * se[i, 3]
    print("  S_chern: all responses null (parity symmetry) -- "
          "harness sanity confirmed")
    # which operator moves the scale field?
    movers = []
    for j, sn in enumerate(snames[:3]):
        if (abs(mean[1, j]) > 3 * se[1, j]
                or abs(mean[2, j]) > 3 * se[2, j]):
            movers.append(sn)
    if movers:
        for sn in movers:
            j = snames.index(sn)
            es = [deficits[n] / mean[i, j]
                  for i, n in [(1, "sP_exc"), (2, "c(1)")]
                  if abs(mean[i, j]) > 3 * se[i, j]]
            print(f"  {sn} MOVES the scale field: eps* = "
                  + ", ".join(f"{e:+.3f}" for e in es))
        print("  the deficit's operator is identified (or short-"
              "listed) among the movers")
    else:
        print("  NO site-local operator among these moves the scale "
              "field: the deficit is")
        print("  nonlocal or nonperturbative -- the obstruction "
              "sharpens")
    print("all assertions passed")
