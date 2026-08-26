"""0135 -- the graviton propagator, at the statistics it needs.

0145 obstructed burndown item 2: the spin-2 correlator sat at the
shuffle floor with 170 configurations, and connected-correlator SNR
grows as sqrt(n). 0134's C kernel makes 25x affordable.

This is the run. Durable: the correlator accumulators and the RNG
state checkpoint to disk every block, so it resumes.
"""

import ctypes
import importlib.util
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "mc0135")
os.makedirs(DIR, exist_ok=True)


def _load(name, tag):
    s = importlib.util.spec_from_file_location(
        tag, os.path.join(HERE, name))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


K = _load("0134_the_spin4_kernel.py", "k134")
M132 = K.M132

L = 8
EVERY = 10
BLOCK = 250          # measurements per checkpoint
WIDTHS = (0.0, 1.0)


def site_tensors(Up, Um, lat):
    qp, qm = M132.all_plaq(Up, lat), M132.all_plaq(Um, lat)
    Bp, Bm = qp[..., 1:], qm[..., 1:]
    outer = np.einsum("vpi,vpj->vpij", Bp, Bm)
    tr = np.einsum("vpii->vp", outer)
    anti = 0.5 * (outer - np.swapaxes(outer, -1, -2))
    sym = 0.5 * (outer + np.swapaxes(outer, -1, -2))
    sym0 = sym - (tr / 3)[..., None, None] * np.eye(3)
    sh = (L,) * 4
    return (tr.mean(1).reshape(sh),
            anti.mean(1).reshape(sh + (3, 3)),
            sym0.mean(1).reshape(sh + (3, 3)))


_KER = {}


def ker(w):
    if w not in _KER:
        ax = 2 * np.pi * np.fft.fftfreq(L)
        g = np.meshgrid(*([ax] * 4), indexing="ij")
        _KER[w] = np.exp(-(w ** 2) * sum(gi ** 2 for gi in g))
    return _KER[w]


def cs(f, w):
    P = np.abs(np.fft.fftn(f - f.mean())) ** 2
    if w > 0:
        P = P * ker(w)
    return np.real(np.fft.ifftn(P)) / f.size


def ct(T, w):
    return sum(cs(T[..., a, b], w) for a in range(3)
               for b in range(3))


KEYS = [f"{k}_{w}" for w in WIDTHS
        for k in ("s0", "s1", "s2", "shuf")]
CK = os.path.join(DIR, f"run_L{L}.npz")


def run(target=5000):
    lat, up, dn = K.lat_arrays(L)
    V = lat["V"]
    rng = np.random.default_rng(135)
    if os.path.exists(CK):
        z = np.load(CK)
        lp, lm = z["lp"].copy(), z["lm"].copy()
        rs = z["rs"].copy()
        acc = {k: z[k].copy() for k in KEYS}
        n, sig = int(z["n"]), float(z["sig"])
        print(f"  resumed at {n} measurements")
    else:
        lp, lm = K.fresh(L)
        rs = K.seed(2024)
        sig = 0.08
        a = t = 0
        for s in range(900):                      # burn + tune
            aa, tt = K.csweeps(lp, lm, up, dn, V, 1, sig, rs)
            if s < 500:
                r = aa / max(tt, 1)
                sig *= 1.06 if r > 0.45 else (0.94 if r < 0.35 else 1)
                sig = float(np.clip(sig, 0.005, 1.0))
        acc = {k: None for k in KEYS}
        n = 0
    t0 = time.time()
    while n < target:
        for _ in range(BLOCK):
            K.csweeps(lp, lm, up, dn, V, EVERY, sig, rs)
            Up, Um = K.as_links(lp, V), K.as_links(lm, V)
            s0, s1, s2 = site_tensors(Up, Um, lat)
            flat = s2.reshape(-1, 3, 3)[
                rng.permutation(V)].reshape(s2.shape)
            for w in WIDTHS:
                for k, v in ((f"s0_{w}", cs(s0, w)),
                             (f"s1_{w}", ct(s1, w)),
                             (f"s2_{w}", ct(s2, w)),
                             (f"shuf_{w}", ct(flat, w))):
                    acc[k] = v if acc[k] is None else acc[k] + v
            n += 1
        np.savez(CK + ".tmp.npz", lp=lp, lm=lm, rs=rs, n=n,
                 sig=sig, **acc)
        os.replace(CK + ".tmp.npz", CK)
        print(f"    {n} measurements, {time.time() - t0:.0f}s",
              flush=True)
    return {k: acc[k] / n for k in KEYS}, n, sig


def report(C, n):
    print(f"\n== the spin-2 correlator, {n} configurations ==")
    rr = np.arange(1, L // 2 + 1)
    resolved = False
    for w in WIDTHS:
        nrm = {k: abs(C[f"{k}_{w}"][0, 0, 0, 0])
               for k in ("s0", "s1", "s2", "shuf")}
        floor = max(abs(C[f"shuf_{w}"][r, 0, 0, 0]) / nrm["s2"]
                    for r in rr[1:])
        print(f"\n  --- w = {w} ---   shuffle floor {floor:.6f}")
        print("     r     spin 0       spin 1       spin 2      "
              "|s2|/floor")
        for r in rr:
            v = [C[f"{k}_{w}"][r, 0, 0, 0] / nrm[k]
                 for k in ("s0", "s1", "s2")]
            print(f"    {r:2d}   {v[0]:+.6f}   {v[1]:+.6f}   "
                  f"{v[2]:+.6f}    {abs(v[2]) / max(floor, 1e-12):6.1f}x")
        best = max(abs(C[f"s2_{w}"][r, 0, 0, 0]) / nrm["s2"]
                   for r in rr[1:])
        if best > 5 * floor:
            resolved = True
    print()
    if resolved:
        print("  THE SPIN-2 CORRELATOR IS RESOLVED above the "
              "shuffle floor at r >= 2.")
        print("  That is the graviton propagator on the derived "
              "measure, measured.")
    else:
        print("  STILL AT THE FLOOR. With ~30x the statistics of "
              "0145 the spin-2 connected")
        print("  correlator does not separate from a shuffled "
              "control. The obstruction is")
        print("  therefore NOT throughput -- it is that at "
              "kappa ~ 17 the connected signal is")
        print("  genuinely below what this estimator can reach, and "
              "the next move is a")
        print("  different estimator (multilevel / link "
              "integration), not more sweeps.")
    return resolved


if __name__ == "__main__":
    C, n, sig = run()
    report(C, n)
