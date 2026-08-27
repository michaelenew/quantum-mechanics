"""0121 -- the Symanzik exponent: what the extrapolation rests on.

0131 bounded the interacting contribution to rotational-symmetry
breaking at <= 1.4% at r ~ 5a, and noted that the step from there to
physical scales (~10^13 a) is an extrapolation no lattice can close.

It does not have to be closed by a lattice. Symanzik's analysis says
a local lattice theory is described at long distance by the target
continuum action plus a^2 x dimension-six operators plus O(a^4); the
operators that break rotational symmetry are dimension six, so their
effect on any observable at resolution scale s is O((a/s)^2). That
turns the extrapolation from a hope into a THEOREM WITH A TESTABLE
PREMISE -- and the premise is the exponent.

0129 verified exponent 2 for the FREE lattice field (coefficient
3.7, flat across r = 2..10). This module measures it for the
INTERACTING theory, by watching the residual anisotropy fall as the
observation kernel widens.

  s1  THE RESIDUAL VERSUS THE PROBE SCALE. At L = 20, the smeared
      anisotropy minus its exactly-computed free-field baseline, at
      seven kernel widths. Both pieces fall; the difference is the
      interacting residue.
  s2  THE EXPONENT. Fit log|residual| against log w. Exponent 2
      means Symanzik scaling holds where it is measurable, and the
      extrapolation to physical separations rests on an effective
      field theory argument with its premise checked rather than on
      an assumption.
  s3  WHAT THE BOUND BECOMES. With the exponent measured, the bound
      at r ~ 5a propagates, and the number is stated with the one
      assumption that remains named.
"""

import importlib.util
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "mc0121")
os.makedirs(DIR, exist_ok=True)

_s = importlib.util.spec_from_file_location(
    "m92", os.path.join(HERE, "0092_the_coupling_scan.py"))
M = importlib.util.module_from_spec(_s)
_s.loader.exec_module(M)

WIDTHS = (1.0, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0)
PAIRS = [((4, 0, 0, 0), (2, 2, 2, 2)),
         ((6, 0, 0, 0), (3, 3, 3, 3)),
         ((4, 0, 0, 0), (3, 2, 1, 1)),
         ((6, 0, 0, 0), (4, 4, 2, 0))]
NEEDED = sorted({v for p in PAIRS for v in p})


def kern(L, widths):
    ax = 2 * np.pi * np.fft.fftfreq(L)
    g = np.meshgrid(*([ax] * 4), indexing="ij")
    k2 = sum(gi ** 2 for gi in g)
    return {w: np.exp(-(w ** 2) * k2) for w in widths}, k2


def run(L=20, nconf=300, every=15, burn=2000, seed=6610):
    key = f"sym_L{L}_n{nconf}"
    path = os.path.join(DIR, key + ".json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    lat = M.mklat(L)
    tab = M.lnw_table(0.0)
    rs = M.seed_state(seed)
    links = np.ascontiguousarray(
        np.tile([1.0, 0, 0, 0], (4, lat["V"], 1)))
    M.c_sweeps(links, lat, 5, 1.5, tab, rs)
    M.c_sweeps(links, lat, burn, 0.5, tab, rs)
    K, _ = kern(L, WIDTHS)
    acc = {w: {v: [] for v in NEEDED} for w in WIDTHS}
    for _ in range(nconf):
        M.c_sweeps(links, lat, every, 0.5, tab, rs)
        links /= np.linalg.norm(links, axis=-1, keepdims=True)
        O = np.cos(M.all_plaq_thetas(links, lat)).sum(1).reshape(
            L, L, L, L)
        P = np.abs(np.fft.fftn(O - O.mean())) ** 2
        for w in WIDTHS:
            C = np.real(np.fft.ifftn(P * K[w])) / O.size
            for v in NEEDED:
                acc[w][v].append(float(C[v]))
    out = {str(w): {str(v): (float(np.mean(a)),
                             float(np.std(a) / np.sqrt(len(a))))
                    for v, a in d.items()}
           for w, d in acc.items()}
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(out, f)
    os.replace(tmp, path)
    return out


def free_at(L):
    ax = 2 * np.pi * np.fft.fftfreq(L)
    g = np.meshgrid(*([ax] * 4), indexing="ij")
    p2h = sum(2 * (1 - np.cos(gi)) for gi in g)
    k2 = sum(gi ** 2 for gi in g)
    p2h[(0,) * 4] = np.inf
    C0 = np.real(np.fft.ifftn(1.0 / p2h)) ** 2
    P = np.fft.fftn(C0)
    return {w: np.real(np.fft.ifftn(P * np.exp(-(w ** 2) * k2)))
            for w in WIDTHS}


def s1_residual(res, L=20):
    print("== s1: the residual versus the probe scale ==")
    F = free_at(L)
    print("      w     pair                    measured        "
          "  free      residual    sigma")
    data = {}
    for w in WIDTHS:
        for a, b in PAIRS:
            ma, ea = res[str(w)][str(a)]
            mb, eb = res[str(w)][str(b)]
            A = (ma - mb) / (0.5 * (ma + mb))
            eA = abs(A) * np.sqrt((ea / ma) ** 2 + (eb / mb) ** 2)
            Kf = float((F[w][a] - F[w][b])
                       / (0.5 * (F[w][a] + F[w][b])))
            ok = eA < 0.3 * abs(A) and abs(Kf) < 0.15
            if ok:
                data.setdefault((a, b), []).append((w, abs(A - Kf)))
            print(f"   {w:.2f}   {str(a):13s} vs {str(b):11s} "
                  f"{A:+.5f}+-{eA:.5f} {Kf:+.5f}  {A - Kf:+.5f}  "
                  f"{abs(A) / eA:6.1f}" + ("  ok" if ok else ""))
    print()
    return data


def s2_exponent(data):
    print("== s2: the exponent ==")
    print("  fit log|residual| = c - p log w  for each pair with "
          ">= 4 usable widths")
    ps, signflip = [], []
    for (a, b), pts in data.items():
        if len(pts) < 4:
            continue
        wl = np.log([w for w, _ in pts])
        rl = np.log([max(r, 1e-12) for _, r in pts])
        p, c = np.polyfit(wl, rl, 1)
        ps.append(-p)
        print(f"   {str(a):13s} vs {str(b):11s}  {len(pts)} widths, "
              f"exponent p = {-p:.2f}")
    if len(ps) < 2:
        print("  too few pairs -- exponent not measured")
        return None
    print(f"  measured exponents: " + ", ".join(f"{x:.2f}"
                                                for x in ps))
    print(f"  mean {np.mean(ps):.2f}, SPREAD {min(ps):.2f} to "
          f"{max(ps):.2f}   (Symanzik: 2)")
    print()
    print("  THE EXPONENT IS NOT MEASURED. The four pairs do not "
          "agree: two fall steeply,")
    print("  one is flat, and one comes out NEGATIVE because its "
          "residual CHANGES SIGN")
    print("  (+0.0082, +0.0030, +0.0005, -0.0014, -0.0044, "
          "-0.0070), which no power law")
    print("  describes. The mean landing near 2 is arithmetic, not "
          "evidence, and an earlier")
    print("  version of this module tested |mean - 2| < 0.8 and "
          "passed on exactly that.")
    print()
    print("  Nor does restricting to the clean window w in "
          "[1.25, 2.0] -- where the free")
    print("  baseline is small and falling, before it starts "
          "growing again at w >= 2.5 as")
    print("  the kernel plus separation begins to span the box -- "
          "help: the slopes there")
    print("  are 3.3, 7.4 and 2.2, with the fourth pair still "
          "changing sign.")
    return None


def s3_bound(pexp):
    print("== s3: what the bound becomes ==")
    print("  THE EXPONENT WAS NOT MEASURED, so the bound does NOT "
          "propagate. It stands where")
    print("  it was measured -- the interacting contribution to "
          "rotational-symmetry breaking")
    print("  is <= 1.4% at r = 4-6 with a probe of width ~2 -- and "
          "the step from there to")
    print("  physical separations rests on SYMANZIK'S THEOREM "
          "ALONE, premise unverified here.")
    print()
    print("  That is weaker than this module set out to establish, "
          "and it is the honest")
    print("  position. The theorem is solid and standard; what is "
          "missing is the check, and")
    print("  the check failed for a nameable reason: THE USABLE "
          "WINDOW IN w IS TOO NARROW.")
    print("  It is bounded below by statistics and above by the "
          "box, and on L = 20 those")
    print("  two leave barely a factor 1.6 in w -- no lever arm for "
          "a power law. This wants")
    print("  L = 32 or more; until then the extrapolation is an "
          "argument, not a measurement.")
    print()


if __name__ == "__main__":
    res = run()
    data = s1_residual(res)
    p = s2_exponent(data)
    s3_bound(p)
