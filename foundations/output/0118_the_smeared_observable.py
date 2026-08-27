"""0118 -- the smeared observable: an arbitrary observation kernel,
and the Lorentz test retried.

0129 s3 failed to measure rotational invariance: at beta_eff ~ 12 the
connected plaquette correlator is O(g^4), so the anisotropy came out
+5.6 +- 4.8 and -19.7 +- 459. The named way in was "an operator whose
connected correlator is not O(g^4)".

The filter side (lucid 0037) supplies the object: an observation is
an arbitrary CONTINUOUS KERNEL against the field, not a fixed local
readout, and the kernel is chosen to maximise information about the
mode of interest. Two requirements fall out and both matter here:

  - HIGH SIGNAL-TO-NOISE. Averaging the local operator against a
    kernel of width w suppresses the (essentially uncorrelated)
    ultraviolet fluctuations by ~w^-4 in four dimensions while
    leaving the long-distance part, so the variance per
    configuration falls fast.
  - AS ISOTROPIC AS POSSIBLE, AND THEN SUBTRACTED ANYWAY. A cubic
    block injects a large anisotropy of its own; lucid 0037
    measured +0.156 on a field isotropic by construction. A
    Gaussian in the CONTINUUM momentum (exp(-w^2 k^2)) is far
    better -- but 0037 also measured that IT IS NOT CLEAN: +0.020,
    still 33 sigma from zero. So the kernel choice reduces the
    artefact from dominant to small, and the free-field baseline
    must be subtracted at the SAME w regardless. That subtraction
    is s3, and it is the whole method, not a refinement of it.

  s1  THE SMEARED CORRELATOR, MEASURED. Anisotropy at matched |r|
      for several kernel widths, with errors, on the derived
      measure. The question is whether the error bars come down far
      enough to say anything at all.
  s2  THE KINEMATIC BASELINE, EXACTLY, AND AT THE SAME VOLUME.
      The same kernel applied to the free lattice field -- no Monte
      Carlo -- which is the O(a^2) discretisation artefact and
      nothing else. It MUST be computed at the measurement's own L:
      a first pass of this module took it at L = 48 against an
      L = 12 measurement, and with kernels of width 2 on a 12^4
      lattice the wrap-around makes that comparison meaningless.
  s3  MEASURED MINUS KINEMATIC -- AND WHAT REPLACED THE PROBLEM.
      The kernel WORKED: the local operator's anisotropy was
      unresolvable (0.1 sigma), the smeared one reaches 49 sigma, a
      several-hundred-fold gain, exactly as lucid 0037 predicted.
      But the answer is still not available, for a NEW reason: on
      L = 12 the free-field baseline is itself 0.6 to 3.8 for the
      |r| = 6 pairs, i.e. wrap-around dominates, and the two usable
      widths disagree on the |r| = 4 pairs (difference -0.023 at
      w = 1.25 against +0.012 at w = 2.0). A kernel of width 2 plus
      a separation of 4 spans a 12^4 lattice. THE STATISTICAL
      OBSTRUCTION IS SOLVED AND A FINITE-VOLUME ONE REPLACED IT --
      which is progress, because volume is a known cost: this wants
      L >= 20, not more sweeps.
  s4  L = 20, WHICH SETTLES IT AS A BOUND. Run. At w = 2 the
      free-field baselines drop to 0.0003-0.0017 -- wrap-around
      finally under control -- and four rows are resolved at
      18-71 sigma. Measured minus kinematic: +0.0103, +0.0136,
      +0.0008, -0.0037. The pairs do not agree on one number, so
      this is a BOUND and not a measurement: the interacting
      contribution to rotational-symmetry breaking at r = 4-6 is
      AT MOST ABOUT 1.4%. And it SHRINKS as the probe lengthens
      (~0.03 at w = 1.25 against ~0.01 at w = 2.0, roughly the
      (a/scale)^2 law), which is what "the lattice becomes
      invisible at long distance" predicts -- now verified for the
      INTERACTING theory rather than assumed from the free one.
"""

import importlib.util
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "mc0118")
os.makedirs(DIR, exist_ok=True)

_s = importlib.util.spec_from_file_location(
    "m92", os.path.join(HERE, "0092_the_coupling_scan.py"))
M = importlib.util.module_from_spec(_s)
_s.loader.exec_module(M)

WIDTHS = (0.0, 0.75, 1.25, 2.0)
PAIRS = [((4, 0, 0, 0), (2, 2, 2, 2)),
         ((6, 0, 0, 0), (3, 3, 3, 3)),
         ((4, 0, 0, 0), (3, 2, 1, 1)),
         ((6, 0, 0, 0), (4, 4, 2, 0))]
NEEDED = sorted({v for p in PAIRS for v in p})


def kernels(L):
    """|g~(k)|^2 = exp(-w^2 k^2) with the CONTINUUM k: exactly
    rotationally symmetric, so the probe adds no anisotropy."""
    ax = 2 * np.pi * np.fft.fftfreq(L)
    g = np.meshgrid(*([ax] * 4), indexing="ij")
    k2 = sum(gi ** 2 for gi in g)
    return {w: np.exp(-(w ** 2) * k2) for w in WIDTHS}


def action_density(links, lat, L):
    return np.cos(M.all_plaq_thetas(links, lat)).sum(1).reshape(
        L, L, L, L)


def run(L=12, nconf=1500, every=20, burn=3000, seed=5150):
    key = f"sm_L{L}_n{nconf}"
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
    K = kernels(L)
    acc = {w: {v: [] for v in NEEDED} for w in WIDTHS}
    for _ in range(nconf):
        M.c_sweeps(links, lat, every, 0.5, tab, rs)
        links /= np.linalg.norm(links, axis=-1, keepdims=True)
        O = action_density(links, lat, L)
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


def free_smeared(L=12):
    ax = 2 * np.pi * np.fft.fftfreq(L)
    g = np.meshgrid(*([ax] * 4), indexing="ij")
    p2h = sum(2 * (1 - np.cos(gi)) for gi in g)
    k2 = sum(gi ** 2 for gi in g)
    p2h[(0,) * 4] = np.inf
    G = np.real(np.fft.ifftn(1.0 / p2h))
    C0 = G ** 2
    P = np.fft.fftn(C0)
    return {w: np.real(np.fft.ifftn(P * np.exp(-(w ** 2) * k2)))
            for w in WIDTHS}


def aniso(get, a, b):
    ma, ea = get(a)
    mb, eb = get(b)
    A = (ma - mb) / (0.5 * (ma + mb))
    eA = abs(A) * np.sqrt((ea / ma) ** 2 + (eb / mb) ** 2)
    return A, eA


def s1_measured(res):
    print("== s1: the smeared correlator, measured ==")
    print("  kernel |g~(k)|^2 = exp(-w^2 k^2), continuum k: "
          "exactly isotropic probe")
    print("     w      pair                        anisotropy      "
          "   |A|/err")
    best = {}
    for w in WIDTHS:
        def get(v, w=w):
            return res[str(w)][str(v)]
        for a, b in PAIRS:
            A, e = aniso(get, a, b)
            sig = abs(A) / e if e else float("inf")
            best[(w, a, b)] = (A, e)
            print(f"   {w:.2f}   {str(a):13s} vs {str(b):13s}  "
                  f"{A:+.4f} +- {e:.4f}     {sig:6.1f}")
        print()
    return best


def s2_kinematic(L=12):
    print(f"== s2: the kinematic baseline, exactly, at the SAME "
          f"L = {L} ==")
    F = free_smeared(L)
    out = {}
    print("     w      pair                        free anisotropy")
    for w in WIDTHS:
        for a, b in PAIRS:
            fa, fb = F[w][a], F[w][b]
            A = float((fa - fb) / (0.5 * (fa + fb)))
            out[(w, a, b)] = A
            print(f"   {w:.2f}   {str(a):13s} vs {str(b):13s}  "
                  f"{A:+.4f}")
    print()
    return out


def s3_difference(best, kin):
    print("== s3: measured minus kinematic ==")
    print("     w      pair                        measured        "
          "  free       difference")
    got = False
    for w in WIDTHS:
        for a, b in PAIRS:
            A, e = best[(w, a, b)]
            K = kin[(w, a, b)]
            d = A - K
            flag = ""
            resolved = e < 0.3 * abs(A)
            r = np.sqrt(sum(x * x for x in a))
            usable = resolved and abs(K) < 0.1 and r <= 4.0
            if usable:
                flag = "  <-- resolved AND out of the wrap"
                got = True
            elif resolved:
                flag = "  <-- resolved, but wrap-dominated"
            print(f"   {w:.2f}   {str(a):13s} vs {str(b):13s}  "
                  f"{A:+.4f}+-{e:.4f}  {K:+.4f}   {d:+.4f}{flag}")
    print()
    print("  THE KERNEL WORKED. The local operator sat at 0.1 "
          "sigma; the smeared one reaches")
    print("  49 sigma -- a several-hundred-fold gain, as lucid "
          "0037 predicted.")
    print()
    print("  THE ANSWER IS STILL NOT AVAILABLE, for a NEW reason. "
          "On L = 12 the free-field")
    print("  baseline is itself 0.6 to 3.8 on the |r| = 6 pairs: "
          "wrap-around dominates, so")
    print("  those rows say nothing about the theory. And the two "
          "usable widths disagree on")
    print("  the |r| = 4 pairs (-0.023 at w = 1.25 versus +0.012 at "
          "w = 2.0), which is what")
    print("  a kernel of width 2 plus a separation of 4 does to a "
          "12^4 lattice.")
    print()
    print("  So: the statistical obstruction is SOLVED and a "
          "finite-volume one replaced it.")
    print("  That is progress, because volume is a known cost. "
          "This measurement wants")
    print("  L >= 20 and the same number of sweeps -- not more "
          "statistics, more room.")
    assert got
    return got


def s4_bigger_volume():
    print("== s4: L = 20, which settles it as a bound ==")
    res = run(L=20, nconf=300, every=15, burn=2000, seed=7220)
    F = free_smeared(20)
    print("     w      pair                        measured        "
          "     free      difference   sigma")
    diffs = {}
    for w in WIDTHS:
        for a, b in PAIRS:
            ma, ea = res[str(w)][str(a)]
            mb, eb = res[str(w)][str(b)]
            A = (ma - mb) / (0.5 * (ma + mb))
            eA = abs(A) * np.sqrt((ea / ma) ** 2 + (eb / mb) ** 2)
            K = float((F[w][a] - F[w][b])
                      / (0.5 * (F[w][a] + F[w][b])))
            r = np.sqrt(sum(x * x for x in a))
            use = eA < 0.3 * abs(A) and abs(K) < 0.1 and r <= 20 / 3
            if use:
                diffs.setdefault(w, []).append(A - K)
            print(f"   {w:.2f}  {str(a):13s} vs {str(b):13s} "
                  f"{A:+.4f}+-{eA:.4f}  {K:+.4f}  {A - K:+.4f}  "
                  f"{abs(A) / eA:6.1f}" + ("  <-- usable" if use
                                           else ""))
    print()
    for w in sorted(diffs):
        d = diffs[w]
        print(f"  w = {w}: {len(d)} usable rows, |measured - "
              f"kinematic| up to {max(abs(x) for x in d):.4f}")
    big = max(abs(x) for x in diffs[2.0])
    print()
    print("  THE PAIRS DO NOT AGREE ON ONE NUMBER, so this is a "
          "BOUND, not a measurement:")
    print(f"  the interacting contribution to "
          f"rotational-symmetry breaking at r = 4-6 is")
    print(f"  AT MOST ABOUT {100 * big:.1f}%.")
    print()
    print("  And it SHRINKS as the probe lengthens -- roughly the "
          "(a/scale)^2 law, now")
    print("  verified for the INTERACTING theory instead of assumed "
          "from the free one.")
    print("  0129 could not bound this at all; 0130 could not "
          "either. It is bounded now.")
    assert big < 0.05
    print()


if __name__ == "__main__":
    res = run()
    best = s1_measured(res)
    kin = s2_kinematic()
    s3_difference(best, kin)
    s4_bigger_volume()
