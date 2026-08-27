"""0115 -- the continuum probe: the program has no dial, and the
branch ambiguity controls the hierarchy.

First stone of the continuity front -- 0127's last open conjunct of
0069's wall ("the interacting, CONTINUOUS, 3+1 quantum measure").

THE REFRAMING, WHICH COMES FIRST BECAUSE IT CHANGES THE TARGET. A
lattice theory usually reaches the continuum by TUNING a coupling to
a critical point where xi/a diverges. This program cannot do that:
its weight is DERIVED, so its coupling is a fixed number -- the Born
weight's local precision kappa = 13.34 (tau is a heat-flow probe,
not a dial; the physical theory sits at tau = 0). There is nothing
to tune.

So "continuous" here cannot mean a tuned limit. It must mean the
other thing: does the theory, AT ITS OWN DERIVED COUPLING, already
have a correlation length enormously larger than its lattice
spacing -- so that the lattice is invisible without anyone tuning
anything? For a nonabelian gauge measure that is not a hope, it is
what asymptotic freedom does. The question is quantitative.

  s1  THE DERIVED POINT IS AT WEAK COUPLING, AND THE PREDICTION
      HOLDS. kappa = 13.34 is exactly a Wilson beta in this
      program's own plaquette-angle convention (S = beta sum
      (1 - cos theta), and 0092's theta has cos theta = (1/2) tr
      U_p). 0094's Gaussian bank predicts <theta^2> = 3R/kappa with
      R = 1/2 in 4D: 0.1125. Measured, equilibrated: reported here.
      Weak coupling confirmed independently of the flow.
  s2  THE BRANCH IS REAL -- AND ONE CERTIFICATION FAILED. The
      intended positive control was the family's deconfinement
      line, located by a Polyakov susceptibility peak growing with
      volume. IT DID NOT CERTIFY: at 3000 sweeps the peak lands at
      inconsistent tau across L and |<P>| is not monotonic in L.
      Recorded as a failure, not smoothed over -- the scan needs
      an order of magnitude more statistics and a protocol that
      does not start every point hot. What DID work is the direct
      question: relax a hot start at tau = 0 and watch. It falls
      1.94 -> 0.83 -> 0.52 and then PLATEAUS at 0.51 through 40k
      sweeps, nowhere near the ordered branch's 0.0995. The
      disordered branch is a real state, not a slow transient.
      (And the corollary matters: the L = 12 hot run in s1 sits at
      1.41 because 3000 sweeps is not relaxed -- it is a point on
      this curve, not a branch value.)
  s3  THE DERIVED POINT NEVER DISORDERS. At tau = 0 the Polyakov
      loop stays ordered at every volume reachable here, so the
      correlation length exceeds the box at every box. That is a
      lower bound, not a measurement; the two-loop lattice beta
      function turns the measured coupling into a number, and the
      number is ~10^15-10^17.
  s4  AND THE BRANCH AMBIGUITY NOW CONTROLS THE HIERARCHY. 0092
      found that the Born weight's exact zeros are impassable
      barriers, so ordered and disordered starts do not mix, and
      filed it as an ergodicity nuisance. It is not a nuisance. The
      two branches sit at beta_eff ~ 15.5 and ~ 2.9, and asymptotic
      freedom turns that into xi/a ~ 10^17 versus ~10^3 -- FOURTEEN
      ORDERS OF MAGNITUDE. Which branch the tau -> 0+ equilibrium
      selects is therefore not a technical question about Monte
      Carlo. It is the scale hierarchy.
"""

import importlib.util
import json
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "mc0115")
os.makedirs(DIR, exist_ok=True)

_s = importlib.util.spec_from_file_location(
    "m92", os.path.join(HERE, "0092_the_coupling_scan.py"))
M = importlib.util.module_from_spec(_s)
_s.loader.exec_module(M)

KAPPA = 13.337                 # the Born weight's local precision
B0 = 11 / (24 * np.pi ** 2)    # SU(2) one- and two-loop coefficients
B1 = 17 / (96 * np.pi ** 4)


def xi_over_a(beta):
    """two-loop lattice scale: 1/(a Lambda_L) for SU(2), g^2 = 4/beta"""
    g2 = 4.0 / beta
    aL = (B0 * g2) ** (-B1 / (2 * B0 ** 2)) * np.exp(-1 / (2 * B0 * g2))
    return 1.0 / aL


def polyakov(links, L):
    q = links[0].reshape(L, L, L, L, 4)
    acc = q[0].copy()
    for t in range(1, L):
        a, b = acc, q[t]
        w = a[..., 0] * b[..., 0] - (a[..., 1:] * b[..., 1:]).sum(-1)
        v = (a[..., 0:1] * b[..., 1:] + b[..., 0:1] * a[..., 1:]
             + np.cross(a[..., 1:], b[..., 1:]))
        acc = np.concatenate([w[..., None], v], -1)
    return acc[..., 0]                       # (1/2) tr, real


def start_links(lat, tab, rs, branch):
    links = np.ascontiguousarray(
        np.tile([1.0, 0, 0, 0], (4, lat["V"], 1)))
    if branch == "dis":                      # 0092's hot start
        M.c_sweeps(links, lat, 20, 1.5, np.zeros(M.NTAB), rs)
    else:                                    # 0091's ordered protocol
        M.c_sweeps(links, lat, 5, 1.5, tab, rs)
    return links


def run(L, tau, branch, sweeps, burn, seed, meas_every=10):
    """Durable: results cached per (L, tau, branch, sweeps)."""
    key = f"L{L}_t{tau:.3f}_{branch}_s{sweeps}"
    path = os.path.join(DIR, key + ".json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    lat = M.mklat(L)
    tab = M.lnw_table(tau)
    sig = 0.5 + 0.5 * tau
    rs = M.seed_state(seed)
    links = start_links(lat, tab, rs, branch)
    M.c_sweeps(links, lat, burn, sig, tab, rs)
    Ps, th2, acc, tot = [], [], 0, 0
    n = (sweeps - burn) // meas_every
    for _ in range(n):
        a, t_ = M.c_sweeps(links, lat, meas_every, sig, tab, rs)
        acc += a
        tot += t_
        Ps.append(float(polyakov(links, L).mean()))
        th2.append(float((M.all_plaq_thetas(links, lat) ** 2).mean()))
        links /= np.linalg.norm(links, axis=-1, keepdims=True)
    Ps = np.array(Ps)
    out = dict(L=L, tau=tau, branch=branch, n=len(Ps),
               absP=float(np.abs(Ps).mean()),
               chiP=float(L ** 3 * Ps.var()),
               th2=float(np.mean(th2)),
               th2_err=float(np.std(th2) / np.sqrt(max(len(th2), 1))),
               acc=float(acc / max(tot, 1)))
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(out, f)
    os.replace(tmp, path)
    return out


def s1_weak_coupling():
    print("== s1: the derived point is at weak coupling ==")
    print(f"  the weight's local precision kappa = {KAPPA:.3f}, "
          f"which IS a Wilson beta in this")
    print("  program's convention (cos theta = (1/2) tr U_p, so "
          "-d2 lnW/dtheta2 at 0 = beta)")
    pred = 3 * 0.5 / KAPPA
    print(f"  0094's Gaussian bank predicts <theta^2> = 3R/kappa "
          f"with R = 1/2:  {pred:.4f}")
    print("    L   branch   <theta^2>          beta_eff = 3R/<th2>"
          "   acc")
    got = {}
    for L in (6, 8, 12):
        for br in ("ord", "dis"):
            r = run(L, 0.0, br, 3000, 900, 6100 + 13 * L
                    + (7 if br == "dis" else 0))
            got[(L, br)] = r
            print(f"   {L:2d}   {br}      {r['th2']:.4f} +- "
                  f"{r['th2_err']:.4f}    {1.5 / r['th2']:7.2f}"
                  f"          {r['acc']:.3f}")
    o = got[(8, "ord")]["th2"]
    assert abs(o / pred - 1) < 0.25
    print(f"  the ordered branch lands within "
          f"{100 * abs(o / pred - 1):.0f}% of the Gaussian "
          f"prediction: weak coupling, confirmed")
    print("  independently of the flow. The disordered branch does "
          "NOT -- it is a different")
    print("  theory, and s4 prices the difference\n")
    return got


def relax_curve(L, marks=(1000, 4000, 10000, 20000, 40000)):
    key = f"relax_L{L}"
    path = os.path.join(DIR, key + ".json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    lat = M.mklat(L)
    tab = M.lnw_table(0.0)
    rs = M.seed_state(555 + L)
    links = np.ascontiguousarray(
        np.tile([1.0, 0, 0, 0], (4, lat["V"], 1)))
    M.c_sweeps(links, lat, 20, 1.5, np.zeros(M.NTAB), rs)   # hot
    out, done = [], 0
    for t in marks:
        M.c_sweeps(links, lat, t - done, 0.5, tab, rs)
        done = t
        links /= np.linalg.norm(links, axis=-1, keepdims=True)
        out.append(float((M.all_plaq_thetas(links, lat) ** 2).mean()))
    res = dict(L=L, marks=list(marks), th2=out)
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(res, f)
    os.replace(tmp, path)
    return res


def s2_branch_is_real():
    print("== s2: the branch is real -- and one certification "
          "failed ==")
    print("  INTENDED CONTROL (deconfinement line, susceptibility "
          "peak growing with volume):")
    print("    tau     L=6 |<P>|   chi     L=8 |<P>|   chi     "
          "L=10 |<P>|   chi")
    peaks = {6: (0, 0), 8: (0, 0), 10: (0, 0)}
    for tau in (0.05, 0.15, 0.25, 0.35, 0.45, 0.6, 0.8):
        row = []
        for L in (6, 8, 10):
            r = run(L, tau, "dis", 3000, 900,
                    7700 + int(1000 * tau) + 31 * L)
            row.append(r)
            if r["chiP"] > peaks[L][0]:
                peaks[L] = (r["chiP"], tau)
        print(f"   {tau:.2f}    " + "    ".join(
            f"{r['absP']:.4f}  {r['chiP']:6.2f}" for r in row))
    print("   peak chi:  " + "   ".join(
        f"L={L}: {peaks[L][0]:.2f} at tau={peaks[L][1]:.2f}"
        for L in (6, 8, 10)))
    print("  THIS DID NOT CERTIFY. The peak lands at inconsistent "
          "tau across L and |<P>| is")
    print("  not monotonic in L: at 3000 sweeps, every point "
          "started hot, this scan is not")
    print("  converged. Recorded as a failed control. It needs ~10x "
          "the statistics and a")
    print("  protocol that does not start each point from a hot "
          "configuration.\n")
    print("  WHAT DID WORK -- relax a hot start at tau = 0 and "
          "watch where it goes:")
    print("    L      " + "".join(f"{m:>8d}" for m in
                                  (1000, 4000, 10000, 20000, 40000))
          + "   | ordered branch")
    for L in (4, 6):
        r = relax_curve(L)
        o = run(L, 0.0, "ord", 3000, 900, 6100 + 13 * L)["th2"]
        print(f"    {L}   " + "".join(f"{v:8.3f}" for v in r["th2"])
              + f"   | {o:.4f}")
        assert abs(r["th2"][-1] / r["th2"][-2] - 1) < 0.10
        assert r["th2"][-1] > 4 * o
    print("  it falls fast, then PLATEAUS -- and the plateau is "
          "nowhere near the ordered")
    print("  branch. The disordered branch is a real state, not a "
          "slow transient.")
    print("  Corollary: s1's L = 12 hot run sits at 1.41 because "
          "3000 sweeps is a point")
    print("  ON THIS CURVE, not a branch value. The branch value "
          "is the plateau.\n")
    return float(relax_curve(4)["th2"][-1])


def s3_never_disorders(got):
    print("== s3: the derived point never disorders ==")
    print("    L      |<P>| (ord)    |<P>| (dis)")
    for L in (6, 8, 12):
        print(f"   {L:2d}      {got[(L, 'ord')]['absP']:.4f}"
              f"         {got[(L, 'dis')]['absP']:.4f}")
    assert got[(12, "ord")]["absP"] > 0.5
    print("  the ordered branch stays ordered at every volume "
          "reachable here, so its")
    print("  correlation length exceeds the box at every box: a "
          "LOWER BOUND, not a")
    print("  measurement. The two-loop lattice beta function turns "
          "the measured coupling")
    print("  into a number.\n")


def s4_the_hierarchy(got, th2_dis):
    print("== s4: the branch ambiguity controls the hierarchy ==")
    print("  two-loop SU(2): a Lambda_L = (b0 g^2)^(-b1/2b0^2) "
          "exp(-1/(2 b0 g^2)), g^2 = 4/beta")
    print("    source                          beta_eff     xi/a")
    rows = [("the weight's own kappa", KAPPA),
            ("ordered branch (0091 protocol)",
             1.5 / got[(12, "ord")]["th2"]),
            ("disordered branch (relaxed plateau)",
             1.5 / th2_dis)]
    vals = {}
    for lab, b in rows:
        x = xi_over_a(b)
        vals[lab] = x
        print(f"    {lab:30s}  {b:7.2f}   {x:.2e}")
    ratio = vals[rows[1][0]] / vals[rows[2][0]]
    print(f"  ratio between the branches: {ratio:.1e} -- "
          f"{np.log10(ratio):.0f} ORDERS OF MAGNITUDE")
    assert ratio > 1e8
    print()
    print("  0092 found the Born weight's exact zeros are "
          "impassable barriers and filed the")
    print("  branch split as an ergodicity nuisance. It is not a "
          "nuisance. WHICH BRANCH THE")
    print("  tau -> 0+ EQUILIBRIUM SELECTS IS THE SCALE HIERARCHY, "
          "and that is now the")
    print("  continuity front's first real question.")
    print()
    print("  Caveats, named: the two-loop formula is Wilson's, and "
          "the derived weight is")
    print("  band-limited with hard zeros -- universality fixes the "
          "continuum theory but not")
    print("  the Lambda-parameter ratio, which is an O(1)-to-O(10) "
          "multiplicative unknown on")
    print("  a number of order 10^15. The bound in s3 is what is "
          "measured; s4 is an estimate\n")


if __name__ == "__main__":
    t0 = time.time()
    got = s1_weak_coupling()
    th2_dis = s2_branch_is_real()
    s3_never_disorders(got)
    s4_the_hierarchy(got, th2_dis)
    print(f"all assertions passed  ({time.time() - t0:.0f}s)")
