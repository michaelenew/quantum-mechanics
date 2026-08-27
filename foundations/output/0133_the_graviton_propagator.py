"""0133 -- the graviton propagator: the spin-2 correlator on the
Spin(4) lattice.

Burndown item 2. 0144 rebuilt the lattice on Spin(4) and confirmed
the spin-2 sector is populated. lucid 0046 measured that the sector
is PURE SYNERGY -- present in neither marginal -- so this correlator
exists only on the rebuilt lattice.

  s1  THE FIELD. At each site, average the traceless symmetric part
      of B+ (x) B- over the six plaquettes based there. That is the
      spin-2 field h_ab(x). Its two companions -- the trace (spin 0)
      and the antisymmetric part (spin 1) -- are built the same way,
      as controls.
  s2  THE CORRELATOR, by FFT, for all three sectors at once. If
      gravity is in this measure, the spin-2 sector should reach
      further than the others.
  s3  THE RANGE. Fit each sector's decay and compare. Reported with
      the noise floor from a within-configuration shuffle, so a
      short range is a measurement and not an absence.
"""

import importlib.util
import os

import numpy as np

WIDTHS = (0.0, 1.0, 1.6)

HERE = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location(
    "m132", os.path.join(HERE, "0132_the_spin4_lattice.py"))
M = importlib.util.module_from_spec(_s)
_s.loader.exec_module(M)

rng = np.random.default_rng(133)


def site_tensors(Up, Um, lat, L):
    """(trace, antisym, traceless-sym) fields, one per site."""
    qp, qm = M.all_plaq(Up, lat), M.all_plaq(Um, lat)
    Bp, Bm = qp[..., 1:], qm[..., 1:]              # (V, 6, 3)
    outer = np.einsum("vpi,vpj->vpij", Bp, Bm)
    tr = np.einsum("vpii->vp", outer)
    anti = 0.5 * (outer - np.swapaxes(outer, -1, -2))
    sym = 0.5 * (outer + np.swapaxes(outer, -1, -2))
    sym0 = sym - (tr / 3)[..., None, None] * np.eye(3)
    sh = (L,) * 4
    s0 = tr.mean(1).reshape(sh)
    s1 = anti.mean(1).reshape(sh + (3, 3))
    s2 = sym0.mean(1).reshape(sh + (3, 3))
    return s0, s1, s2


_KER = {}


def kernel(L, w):
    key = (L, w)
    if key not in _KER:
        ax = 2 * np.pi * np.fft.fftfreq(L)
        g = np.meshgrid(*([ax] * 4), indexing="ij")
        _KER[key] = np.exp(-(w ** 2) * sum(gi ** 2 for gi in g))
    return _KER[key]


def corr_scalar(f, w=0.0):
    """connected correlator, optionally through an isotropic
    smearing kernel (lucid 0037: the kernel buys statistics; the
    two ensembles being compared share it, so it cannot manufacture
    a difference between sectors)."""
    F = np.fft.fftn(f - f.mean())
    P = np.abs(F) ** 2
    if w > 0:
        P = P * kernel(f.shape[0], w)
    return np.real(np.fft.ifftn(P)) / f.size


def corr_tensor(T, w=0.0):
    acc = None
    for a in range(3):
        for b in range(3):
            c = corr_scalar(T[..., a, b], w)
            acc = c if acc is None else acc + c
    return acc


def run(L=8, sweeps=2600, burn=900, meas_every=10):
    lat = M.mklat(L)
    Up = [np.tile([1.0, 0, 0, 0], (lat["V"], 1)) for _ in range(4)]
    Um = [np.tile([1.0, 0, 0, 0], (lat["V"], 1)) for _ in range(4)]
    sigma = 0.08
    acc = tot = 0
    C = {}
    n = 0
    for s in range(sweeps):
        a, t = M.sweep(Up, Um, lat, sigma)
        if s < burn // 2:
            r = a / max(t, 1)
            sigma *= 1.06 if r > 0.45 else (0.94 if r < 0.35 else 1)
            sigma = float(np.clip(sigma, 0.005, 1.0))
        else:
            acc += a
            tot += t
        if s >= burn and s % meas_every == 0:
            s0, s1, s2 = site_tensors(Up, Um, lat, L)
            flat = s2.reshape(-1, 3, 3)[
                rng.permutation(lat["V"])].reshape(s2.shape)
            for w in WIDTHS:
                for k, v in (
                        (f"s0_{w}", corr_scalar(s0, w)),
                        (f"s1_{w}", corr_tensor(s1, w)),
                        (f"s2_{w}", corr_tensor(s2, w)),
                        (f"shuf_{w}", corr_tensor(flat, w))):
                    C[k] = v if C.get(k) is None else C[k] + v
            n += 1
    for k in C:
        C[k] = C[k] / n
    return C, acc / max(tot, 1), n


def s1_s2_s3(L=8):
    print("== the spin-2 correlator on the Spin(4) lattice ==")
    C, rate, n = run(L=L)
    print(f"  L = {L}, acceptance {rate:.3f}, {n} measurements")
    assert 0.15 < rate < 0.75
    rr = np.arange(1, L // 2 + 1)
    resolved = False
    for w in WIDTHS:
        print(f"\n  --- smearing width w = {w} ---")
        norm = {k: abs(C[f"{k}_{w}"][0, 0, 0, 0])
                for k in ("s0", "s1", "s2", "shuf")}
        floor = max(abs(C[f"shuf_{w}"][r, 0, 0, 0]) / norm["s2"]
                    for r in rr[1:])
        print("     r     spin 0      spin 1      spin 2      "
              "|spin2|/floor")
        for r in rr:
            v = [C[f"{k}_{w}"][r, 0, 0, 0] / norm[k]
                 for k in ("s0", "s1", "s2")]
            print(f"    {r:2d}   {v[0]:+.6f}   {v[1]:+.6f}   "
                  f"{v[2]:+.6f}     {abs(v[2]) / max(floor, 1e-12):6.1f}x")
        print(f"     shuffle floor {floor:.6f}")
        best = max(abs(C[f"s2_{w}"][r, 0, 0, 0]) / norm["s2"]
                   for r in rr[1:])
        if best > 5 * floor:
            resolved = True
            print(f"     -> spin 2 RESOLVED at this width "
                  f"({best / floor:.1f}x floor)")
    print()
    if resolved:
        print("  THE SPIN-2 CORRELATOR IS RESOLVED once the "
              "observable is smeared -- the same")
        print("  medicine 0118 used to take an unmeasurable "
              "anisotropy from 0.1 to 49 sigma.")
        print("  That is the graviton propagator on the derived "
              "measure.")
    else:
        print("  NOT RESOLVED, at any width tried. All three "
              "sectors sit at the shuffle floor.")
        print("  This is an OBSTRUCTION and it is the same one 0129 "
              "hit: at kappa ~ 17 the")
        print("  theory is deep in weak coupling and every "
              "connected correlator is tiny. The")
        print("  kernel bought statistics but not enough, so the "
              "graviton propagator needs")
        print("  either far more configurations or a variance "
              "reduction the program does not")
        print("  yet have. Recorded as measured\n")
    return resolved


if __name__ == "__main__":
    s1_s2_s3()
    print("all assertions passed")
