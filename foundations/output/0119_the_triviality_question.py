"""0119 -- the triviality question, scoped and its premise tested.

0130 left "triviality" as the one untouched item on the continuity
front: is the continuum limit interacting, or free? Before measuring
anything it is worth being clear about what the threat actually is,
because the honest answer changes the work.

TRIVIALITY IS NOT THE SAME THREAT HERE. It afflicts theories that
are NOT asymptotically free -- phi^4 and U(1) in four dimensions,
where the renormalised coupling is driven to zero as the cutoff is
removed and the continuum theory is free. A four-dimensional
NONABELIAN gauge theory runs the other way: the coupling at the
cutoff goes to zero while the coupling at fixed physical distance
stays finite, which is why the continuum limit is expected to exist
and to interact. THE SAME ASYMPTOTIC FREEDOM THAT SUPPLIES THIS
PROGRAM'S HIERARCHY (0128-0130) IS WHAT REMOVES THE TRIVIALITY
THREAT. So the question reduces to a premise:

    IS THE DERIVED MEASURE IN THE ASYMPTOTICALLY FREE NONABELIAN
    UNIVERSALITY CLASS, OR ONLY SUPERFICIALLY SU(2)-SHAPED?

That premise is testable, and non-circularly, which is the point of
this module.

  s1  THE NON-CIRCULAR TEST. The weight's local precision
      kappa(tau) = -d^2 ln W_tau / dtheta^2 at 0 is computed FROM
      THE WEIGHT, with no Monte Carlo anywhere. SU(2) lattice
      perturbation theory then predicts <1 - (1/2) tr U_p> =
      3/(4 kappa) + O(kappa^-2) -- and in this program's convention
      (1/2) tr U_p = cos theta, so the prediction is on
      <1 - cos theta>, measured. Nothing on the left of that
      comparison came from the right.
  s2  THE APPROACH, ACROSS THE FAMILY -- AND A TREND I DID NOT
      EXPECT. The comparison over a range of kappa. The measure
      tracks 3/(4 kappa) to about 1% at the smoothed end and to 15%
      at the derived point. But the RELATIVE residual GROWS with
      kappa (-0.150, -0.098, -0.048, -0.018, +0.004) instead of
      falling like 1/kappa, which is the opposite of a perturbative
      correction and which I asserted before looking. Candidates
      for it -- the weight's exact zeros truncating the tail, the
      higher-order lattice series, the Gaussian approximation
      crossing over -- are named in s3 and NOT settled here. What
      the comparison does support is class membership; what it does
      not support is a clean perturbative approach.
  s3  WHAT REMAINS OPEN, STATED PLAINLY. Membership in the class is
      not a proof of nontriviality -- that is not proven for QCD
      either. What this establishes is that the continuity front's
      last item inherits the standard expectation rather than a
      special worry, and what a real test would cost.
"""

import importlib.util
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "mc0119")
os.makedirs(DIR, exist_ok=True)

_s = importlib.util.spec_from_file_location(
    "m92", os.path.join(HERE, "0092_the_coupling_scan.py"))
M = importlib.util.module_from_spec(_s)
_s.loader.exec_module(M)

TAUS = (0.0, 0.05, 0.15, 0.3, 0.6, 1.2)


def kappa_of(tau):
    """-d^2 ln W_tau/dtheta^2 at theta = 0, from the weight alone."""
    th = np.linspace(1e-7, 0.15, 20001)
    js = M.CJS
    lam = js * (js + 1)
    X = np.stack([np.sin((2 * j + 1) * th) / np.sin(th) for j in js])
    w = (M.CCOEF * np.exp(-tau * lam)) @ X
    c = np.polyfit(th, np.log(w), 4)
    return float(-2 * c[-3])


def measure(L, tau, sweeps=6000, burn=2000, every=20, seed=3300):
    key = f"L{L}_t{tau:.3f}"
    path = os.path.join(DIR, key + ".json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    lat = M.mklat(L)
    tab = M.lnw_table(tau)
    rs = M.seed_state(seed + int(1000 * tau))
    links = np.ascontiguousarray(
        np.tile([1.0, 0, 0, 0], (4, lat["V"], 1)))
    M.c_sweeps(links, lat, 5, 1.5, tab, rs)         # ordered start
    M.c_sweeps(links, lat, burn, 0.5 + 0.5 * tau, tab, rs)
    vals = []
    for _ in range((sweeps - burn) // every):
        M.c_sweeps(links, lat, every, 0.5 + 0.5 * tau, tab, rs)
        links /= np.linalg.norm(links, axis=-1, keepdims=True)
        th = M.all_plaq_thetas(links, lat)
        vals.append(float((1 - np.cos(th)).mean()))
    out = dict(L=L, tau=tau, val=float(np.mean(vals)),
               err=float(np.std(vals) / np.sqrt(len(vals))))
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(out, f)
    os.replace(tmp, path)
    return out


def s1_and_s2():
    print("== s1/s2: the non-circular test, across the family ==")
    print("  kappa(tau) comes from the WEIGHT (no Monte Carlo).")
    print("  SU(2) lattice perturbation theory: "
          "<1 - cos theta> = 3/(4 kappa) + O(kappa^-2)")
    print()
    print("    tau    kappa    3/(4 kappa)    measured        "
          "ratio     residual x kappa")
    rows = []
    for tau in TAUS:
        k = kappa_of(tau)
        r = measure(4, tau)
        pred = 3 / (4 * k)
        ratio = r["val"] / pred
        resid = (r["val"] - pred) / pred * k
        rows.append((tau, k, pred, r["val"], r["err"], ratio, resid))
        print(f"   {tau:.2f}   {k:6.2f}    {pred:.5f}     "
              f"{r['val']:.5f}+-{r['err']:.5f}   {ratio:.3f}    "
              f"{resid:+7.2f}")
    print()
    ratios = [x[5] for x in rows]
    print(f"  the ratio runs {min(ratios):.3f} to "
          f"{max(ratios):.3f} across the family: the measure "
          f"tracks the")
    print("  Wilson-class law to ~1% once smoothed and to 15% at "
          "the derived point.")
    assert 0.7 < min(ratios) and max(ratios) < 1.3
    rel = [(x[1], (x[3] - x[2]) / x[2]) for x in rows]
    print("  BUT THE TREND IS THE WRONG WAY. Relative residual vs "
          "kappa:")
    print("    " + "   ".join(f"k={k:.1f}: {r:+.3f}" for k, r in rel))
    print("  it GROWS with kappa instead of falling like 1/kappa. A "
          "perturbative correction")
    print("  would do the opposite, and I asserted the opposite "
          "before looking. So this")
    print("  supports CLASS MEMBERSHIP and does NOT support a clean "
          "perturbative approach;")
    print("  the origin of the trend is named in s3 and left "
          "open\n")
    return rows


def s3_open(rows):
    print("== s3: what remains open ==")
    print("  What this establishes: the continuity front's last "
          "item inherits the STANDARD")
    print("  expectation (asymptotic freedom -> nontrivial "
          "continuum limit) rather than a")
    print("  special worry. Triviality is a phi^4 and U(1) disease; "
          "this measure is in the")
    print("  class that does not have it, and the same asymptotic "
          "freedom supplies the")
    print("  hierarchy measured in 0128-0130.")
    print()
    print("  Nor does it explain s2's trend. Three candidates, none "
          "tested here: the")
    print("  weight's EXACT ZEROS truncate the plaquette "
          "distribution at theta = 2 pi/7,")
    print("  which bites hardest where the weight is most "
          "concentrated; the higher-order")
    print("  lattice perturbation series; and the Gaussian "
          "approximation to <1 - cos theta>")
    print("  crossing over between the ends of the family. "
          "Separating them is one cheap")
    print("  module and would sharpen the class claim considerably.")
    print()
    print("  What this does NOT establish: that the limit IS "
          "nontrivial. That is not proven")
    print("  for QCD either. A real test needs two physical scales "
          "measured at two")
    print("  couplings with their ratio held fixed -- and at "
          "kappa ~ 13 the physical scales")
    print("  are ~10^13 lattice spacings apart, so no such "
          "measurement is possible on this")
    print("  or any lattice. THE HONEST STATUS IS 'INHERITS THE "
          "STANDARD EXPECTATION,")
    print("  UNTESTABLE DIRECTLY' -- and that is a different, and "
          "much better, position than")
    print("  the open question 0130 recorded\n")


if __name__ == "__main__":
    rows = s1_and_s2()
    s3_open(rows)
    print("all assertions passed")
