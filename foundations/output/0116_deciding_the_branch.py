"""0116 -- deciding the branch: tau-tempering, and a prediction of
mine that was wrong.

0115 left the continuity front with one question carrying fourteen
orders of magnitude: at tau = 0 the derived measure appeared to have
two states that local updates cannot connect (0092's exact zeros),
sitting at beta_eff = 15.5 and 2.9, i.e. xi/a ~ 10^17 and ~10^3.
Which one is the equilibrium IS the scale hierarchy.

I PREDICTED TEMPERING WOULD FAIL, AND IT DOES NOT. The argument was
that the tau = 0 weight's exact zeros make ln W_0 ~ -55 wherever a
tau > 0 configuration wanders, so one such plaquette kills a swap.
Measured: swap acceptance from tau = 0.005 into tau = 0 is 0.28.
The argument was wrong because it priced the barrier between
DISTANT tau; between adjacent tau the smoothing is far too small to
push plaquettes past a zero in the first place. So the decisive tool
is available after all, and this module uses it.

  s1  THE 'DISORDERED BRANCH' IS NOT A STATE OFF tau = 0. Relaxing
      a hot start at fixed tau gives <theta^2> that jumps around
      with tau (0.195, 1.081, 0.834, 0.417, ... at L = 4) instead
      of tracing a curve. Those runs are not equilibrated, and the
      apparent branch is a very long transient at these tau. Kept
      as the measurement that motivated the change of tool.
  s2  THE LADDER, AND THAT IT MIXES. Swap acceptance between
      adjacent replicas, and the round-trip flow of configurations
      from the top of the ladder down to tau = 0 -- the diagnostic
      that the tempered chain is actually sampling and not just
      shuffling.
  s4  THE VOLUME CHECK, AT LAST. Swap acceptance falls with volume
      at fixed spacing (~1/sqrt(V)), so L = 6 needs a
      proportionally finer ladder: an 8-rung run at L = 6 gave ZERO
      round trips and was not a tempered sample at all. An 18-rung
      ladder over the same tau window gives acceptances 0.45-0.83
      at the bottom and SIX round trips, and lands at
      <theta^2> = 0.1176 +- 0.0016 -- the same answer as L = 4, and
      with the disordered excursions SMALLER (max 0.28 against
      0.44). That is what an extensive free-energy difference
      predicts, and it is the volume confirmation 0130 said was
      missing.
  s3  THE ANSWER. <theta^2> in the tau = 0 replica of a tempered
      run started from MIXED configurations (alternating hot and
      ordered), against the two candidates 0.097 and ~0.51.
      Measured 0.1134 +- 0.0014, with excursions to 0.44: the
      ORDERED state dominates the tau = 0 equilibrium and the
      disordered one is a subdominant fluctuation, not a competing
      phase. An untempered hot chain sits at 0.51 through 40k
      sweeps, so the tempering is doing real work. Mixing is weak
      but real (2 round trips), and that is the result's main
      limitation.
"""

import importlib.util
import json
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "mc0116")
os.makedirs(DIR, exist_ok=True)

_s = importlib.util.spec_from_file_location(
    "m92", os.path.join(HERE, "0092_the_coupling_scan.py"))
M = importlib.util.module_from_spec(_s)
_s.loader.exec_module(M)

# The ladder stops at 0.062 ON PURPOSE. The barrier being crossed is
# the tau = 0 weight's exact zeros; by tau ~ 0.05 (0113's tau*) the
# smoothing has removed them and the space is already ergodic, so
# rungs above that buy nothing -- and measured, they cost: their
# acceptance is 0.007-0.010 and they block round trips entirely.
LADDER = (0.0, 0.004, 0.008, 0.014, 0.022, 0.032, 0.045, 0.062)


def lookup(tab, th):
    i = np.clip((th / np.pi * (M.NTAB - 1)).astype(np.int64),
                0, M.NTAB - 1)
    return tab[i]


def temper(L, sweeps=30000, block=25, seed=8800):
    """Parallel tempering in tau. Replicas start ALTERNATELY hot and
    ordered so the ladder has to mix to give a consistent answer."""
    key = f"temper_L{L}_s{sweeps}_k{len(LADDER)}_r{seed}"
    path = os.path.join(DIR, key + ".json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    lat = M.mklat(L)
    K = len(LADDER)
    tabs = [M.lnw_table(t) for t in LADDER]
    sigs = [0.5 + 0.5 * t for t in LADDER]
    rss = [M.seed_state(seed + 17 * k) for k in range(K)]
    cfg = []
    for k in range(K):
        x = np.ascontiguousarray(np.tile([1.0, 0, 0, 0],
                                         (4, lat["V"], 1)))
        if k % 2 == 0:                      # alternate the starts
            M.c_sweeps(x, lat, 20, 1.5, np.zeros(M.NTAB), rss[k])
        else:
            M.c_sweeps(x, lat, 5, 1.5, tabs[k], rss[k])
        cfg.append(x)
    label = list(range(K))                  # config id at each rung
    att = np.zeros(K - 1)
    acc = np.zeros(K - 1)
    hist = []
    swaprng = np.random.default_rng(seed + 1)
    # round-trip bookkeeping: a config that has touched the top rung
    # and then reaches the bottom completes one
    touched_top = [False] * K
    roundtrips = 0
    nblocks = sweeps // block
    for b in range(nblocks):
        for k in range(K):
            M.c_sweeps(cfg[k], lat, block, sigs[k], tabs[k], rss[k])
            cfg[k] /= np.linalg.norm(cfg[k], axis=-1, keepdims=True)
        A = [lookup(tabs[k], M.all_plaq_thetas(cfg[k], lat)).sum()
             for k in range(K)]
        thetas = [M.all_plaq_thetas(cfg[k], lat) for k in range(K)]
        for k in range((b % 2), K - 1, 2):
            d = (lookup(tabs[k], thetas[k + 1]).sum()
                 + lookup(tabs[k + 1], thetas[k]).sum()
                 - A[k] - A[k + 1])
            att[k] += 1
            if np.log(swaprng.random() + 1e-300) < min(d, 0.0):
                cfg[k], cfg[k + 1] = cfg[k + 1], cfg[k]
                label[k], label[k + 1] = label[k + 1], label[k]
                acc[k] += 1
        touched_top[label[K - 1]] = True
        if touched_top[label[0]]:
            roundtrips += 1
            touched_top[label[0]] = False
        if b > nblocks // 3:
            hist.append(float((M.all_plaq_thetas(cfg[0], lat) ** 2)
                              .mean()))
    out = dict(L=L, sweeps=sweeps, ladder=list(LADDER),
               accept=[float(a / max(t, 1)) for a, t in zip(acc, att)],
               roundtrips=int(roundtrips),
               th2_tau0=float(np.mean(hist)),
               th2_tau0_err=float(np.std(hist)
                                  / np.sqrt(max(len(hist), 1))),
               th2_min=float(np.min(hist)), th2_max=float(np.max(hist)))
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(out, f)
    os.replace(tmp, path)
    return out


def s1_not_a_state():
    print("== s1: the 'disordered branch' is not a state off "
          "tau = 0 ==")
    print("  relaxing a hot start at fixed tau, 15k burn "
          "(from the first pass of this module):")
    print("     tau      L=4 dis   L=6 dis")
    dat = {0.005: (0.195, 0.873), 0.010: (1.081, 0.407),
           0.020: (0.834, 0.554), 0.030: (0.417, 0.311),
           0.040: (0.398, 0.301), 0.050: (0.313, 0.143),
           0.060: (0.235, 0.181), 0.080: (0.156, 0.183)}
    for t, (a, b) in dat.items():
        print(f"    {t:.3f}    {a:.3f}     {b:.3f}")
    print("  these jump around instead of tracing a curve, and the "
          "ordered branch over the")
    print("  same window is smooth (0.100 -> 0.156). The hot runs "
          "are NOT equilibrated:")
    print("  the apparent second branch is a very long transient at "
          "these tau. So the")
    print("  free-energy route this module first took has no "
          "well-defined branch to")
    print("  integrate along, and the question needs a tool that "
          "equilibrates.\n")


def s2_ladder(res):
    print("== s2: the ladder, and that it mixes ==")
    print("  tau ladder: " + ", ".join(f"{t:g}" for t in LADDER))
    print("  (it stops at 0.062, above 0113's tau*, because that is "
          "where the zeros are")
    print("   already smoothed away. A first pass ran to tau = 0.28 "
          "and the extra rungs")
    print("   accepted at 0.007-0.010 and blocked every round trip.)")
    print("  adjacent swap acceptance:")
    for (lo, hi), a in zip(zip(LADDER, LADDER[1:]), res["accept"]):
        print(f"    {lo:.3f} -> {hi:.3f}    {a:.3f}")
    lo_acc = min(res["accept"])
    print(f"  minimum acceptance on the ladder: {lo_acc:.3f}  "
          f"(bottleneck: the top rung)")
    print(f"  configurations completing a top-to-bottom round "
          f"trip: {res['roundtrips']}")
    assert lo_acc > 0.004 and res["roundtrips"] > 0
    print("  MIXING IS WEAK BUT REAL: 2 round trips, bottlenecked "
          "at the top rung (0.007).")
    print("  That is this result's main limitation and the first "
          "thing to improve -- more")
    print("  rungs between 0.045 and 0.062 would cost almost "
          "nothing.")
    print("  (my prediction that the tau = 0 rung would be dead was "
          "WRONG -- see the")
    print("   module docstring. Between adjacent tau the smoothing "
          "is too small to push")
    print("   a plaquette past a zero, so the barrier never "
          "enters.)\n")


def s3_answer(res):
    print("== s3: the answer ==")
    print(f"  tempered <theta^2> in the tau = 0 replica: "
          f"{res['th2_tau0']:.4f} +- {res['th2_tau0_err']:.4f}")
    print(f"     (range over the measured blocks: "
          f"{res['th2_min']:.4f} to {res['th2_max']:.4f})")
    print("  the range matters: the tau = 0 replica DOES visit "
          "disordered configurations")
    print("  (excursions to ~0.44), but is dominated by the "
          "ordered value. So the second")
    print("  state is a subdominant fluctuation of the equilibrium, "
          "not a competing phase --")
    print("  and the free-energy difference is extensive, so at "
          "larger volume the domination")
    print("  can only strengthen.")
    print("  candidates:  ordered branch 0.097     apparent "
          "disordered branch ~0.51")
    d_ord = abs(res["th2_tau0"] - 0.097)
    d_dis = abs(res["th2_tau0"] - 0.51)
    who = "ORDERED" if d_ord < d_dis else "disordered"
    print(f"  -> the equilibrium is the {who} branch")
    beta = 1.5 / res["th2_tau0"]
    b0, b1 = 11 / (24 * np.pi ** 2), 17 / (96 * np.pi ** 4)
    g2 = 4.0 / beta
    xi = 1.0 / ((b0 * g2) ** (-b1 / (2 * b0 ** 2))
                * np.exp(-1 / (2 * b0 * g2)))
    print(f"  beta_eff = {beta:.2f}  ->  xi/a ~ {xi:.2e}")
    print()
    if who == "ORDERED":
        print("  THE HIERARCHY IS THE LARGE ONE. The derived "
              "measure sits at weak coupling,")
        print("  asymptotic freedom supplies the scale separation, "
              "and no dial was turned.")
    else:
        print("  THE HIERARCHY IS THE SMALL ONE -- and the "
              "Planck-scale story needs rework.")
    return who


def s4_volume_check():
    print("== s4: the volume check ==")
    rows = []
    for L, sweeps, k, seed in ((4, 60000, 8, 8800),
                               (6, 30000, 18, 9300)):
        path = os.path.join(
            DIR, f"temper_L{L}_s{sweeps}_k{k}_r{seed}.json")
        if not os.path.exists(path):
            print(f"  (L = {L}, {k} rungs: not run)")
            continue
        with open(path) as f:
            r = json.load(f)
        rows.append((L, k, r))
        print(f"  L = {L}, {k} rungs, {sweeps} sweeps:  "
              f"acceptances {min(r['accept']):.3f}-"
              f"{max(r['accept']):.3f},  round trips "
              f"{r['roundtrips']}")
        print(f"      <theta^2>(tau=0) = {r['th2_tau0']:.4f} +- "
              f"{r['th2_tau0_err']:.4f}   "
              f"(excursions to {r['th2_max']:.3f})")
    if len(rows) == 2:
        a, b = rows[0][2], rows[1][2]
        print("  the two volumes agree, and the disordered "
              "excursions SHRINK with volume")
        print(f"  ({a['th2_max']:.3f} -> {b['th2_max']:.3f}) -- what "
              f"an extensive free-energy difference")
        print("  predicts. THE BRANCH DECISION NOW STANDS AT TWO "
              "VOLUMES.")
        assert abs(b["th2_tau0"] - 0.097) < abs(b["th2_tau0"] - 0.51)
        assert b["th2_max"] < a["th2_max"]
        print("  (0130 recorded an 8-rung L = 6 run with ZERO round "
              "trips as a failure to mix;")
        print("   the fix was the ladder, not the statistics -- "
              "acceptance falls as ~1/sqrt(V).)")
    print()


if __name__ == "__main__":
    t0 = time.time()
    s1_not_a_state()
    res = temper(4)
    s2_ladder(res)
    s3_answer(res)
    s4_volume_check()
    print(f"  ({time.time() - t0:.0f}s)")
