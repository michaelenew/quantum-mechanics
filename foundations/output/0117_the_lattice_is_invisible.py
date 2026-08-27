"""0117 -- is the lattice invisible? Rotational invariance at the
derived point, and the standing Lorentz debt closed as a bound.

0128 argued that with no dial to tune, "continuous" has to mean the
lattice is ALREADY invisible at the derived coupling. 0115 gave the
indirect evidence (xi exceeds every reachable box; two-loop puts
xi/a ~ 10^17 on the ordered branch). This module measures the direct
consequence, which is also the program's standing "continuum Lorentz
invariance, never tested" debt:

    at what separation does the theory stop being able to tell a
    lattice axis from a diagonal?

  s1  THE MEASUREMENT, WHICH FAILED. The connected correlator of
      the local action density, compared at separations with the
      SAME |r| and different orientations. At 240 configurations on
      L = 12 the signal is BURIED: the anisotropy comes out
      +5.6 +- 4.8 at |r| = 2 and -19.7 +- 459 at |r| = 3. Reported
      as a failed measurement, with the reason, because the reason
      is itself informative: at beta_eff ~ 15 the connected
      plaquette correlator is O(g^4) ~ 1e-3 of the disconnected
      piece, so the statistics needed scale like g^-8. The theory
      is too weakly coupled to see its own interacting correlator
      at reachable cost. A smeared operator or a Wilson-loop
      static potential is the way in; neither is attempted here.
  s2  WHAT IS EXACTLY COMPUTABLE: THE KINEMATIC ANISOTROPY. The
      same observable for the FREE lattice field (the exact Fourier
      transform of 1/phat^2) carries the pure O(a^2) discretisation
      artefact and nothing else, and needs no Monte Carlo. Its
      falloff with r is computed here over a range of matched-|r|
      orientation pairs, and it is the shape the interacting theory
      must approach at weak coupling.
  s3  WHAT CAN AND CANNOT BE CLAIMED. The free-field anisotropy
      falls as (a/r)^2, so IF the interacting correction is small
      -- which weak coupling makes plausible and s1 could not test
      -- rotational (hence Lorentz) violation at separation r is
      O((a/r)^2). That is a conditional statement, not a bound the
      program has earned, and it is recorded as such.
"""

import importlib.util
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "mc0117")
os.makedirs(DIR, exist_ok=True)

_s = importlib.util.spec_from_file_location(
    "m92", os.path.join(HERE, "0092_the_coupling_scan.py"))
M = importlib.util.module_from_spec(_s)
_s.loader.exec_module(M)

# matched-|r| orientation pairs: (axis vector, diagonal vector)
PAIRS = [((2, 0, 0, 0), (1, 1, 1, 1)),
         ((3, 0, 0, 0), (2, 2, 1, 0)),
         ((4, 0, 0, 0), (2, 2, 2, 2)),
         ((3, 0, 0, 0), (1, 2, 2, 0))]


def action_density(links, lat, L):
    """O(x) = sum over the 6 plaquettes at x of cos(theta)."""
    th = M.all_plaq_thetas(links, lat)          # (V, 6)
    return np.cos(th).sum(1).reshape(L, L, L, L)


def conn_corr(f):
    F = np.fft.fftn(f - f.mean())
    return np.real(np.fft.ifftn(np.abs(F) ** 2)) / f.size


def measure_corr(L, nconf=240, every=20, burn=3000, seed=4242):
    key = f"corr_L{L}_n{nconf}"
    path = os.path.join(DIR, key + ".json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    lat = M.mklat(L)
    tab = M.lnw_table(0.0)
    rs = M.seed_state(seed)
    links = np.ascontiguousarray(
        np.tile([1.0, 0, 0, 0], (4, lat["V"], 1)))
    M.c_sweeps(links, lat, 5, 1.5, tab, rs)     # ordered protocol
    M.c_sweeps(links, lat, burn, 0.5, tab, rs)
    samples = {}
    for _ in range(nconf):
        M.c_sweeps(links, lat, every, 0.5, tab, rs)
        links /= np.linalg.norm(links, axis=-1, keepdims=True)
        C = conn_corr(action_density(links, lat, L))
        for v in {v for p in PAIRS for v in p}:
            samples.setdefault(v, []).append(float(C[v]))
    out = {str(k): (float(np.mean(v)),
                    float(np.std(v) / np.sqrt(len(v))))
           for k, v in samples.items()}
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(out, f)
    os.replace(tmp, path)
    return out


def free_corr(L):
    """Connected correlator of the same operator for the FREE
    lattice field: C_free(r) ~ [G(r)]^2 with G the lattice
    propagator, since the action density is quadratic."""
    ax = 2 * np.pi * np.fft.fftfreq(L)
    g = np.meshgrid(*([ax] * 4), indexing="ij")
    p2 = sum(2 * (1 - np.cos(gi)) for gi in g)
    p2[(0,) * 4] = np.inf
    G = np.real(np.fft.ifftn(1.0 / p2))
    return G ** 2


def s1_failed_measurement():
    print("== s1: the measurement, which failed ==")
    L = 12
    meas = measure_corr(L)
    print("  connected action-density correlator, matched |r|, "
          "240 configurations at L = 12:")
    print("     |r|    axis             diagonal          "
          "measured anisotropy")
    noisy = True
    for a, b in PAIRS:
        ma, ea = meas[str(a)]
        mb, eb = meas[str(b)]
        r = np.sqrt(sum(x * x for x in a))
        A = (ma - mb) / (0.5 * (ma + mb))
        eA = abs(A) * np.sqrt((ea / ma) ** 2 + (eb / mb) ** 2)
        if eA < 0.5 * abs(A):
            noisy = False
        print(f"    {r:.2f}   {str(a):16s} {str(b):16s}  "
              f"{A:+.4f} +- {eA:.4f}")
    print("  EVERY ROW IS CONSISTENT WITH ANYTHING. This is a "
          "failed measurement, and the")
    print("  reason is worth as much as the result would have "
          "been: at beta_eff ~ 15 the")
    print("  connected plaquette correlator is O(g^4), so the "
          "statistics needed scale as")
    print("  g^-8. THE THEORY IS TOO WEAKLY COUPLED TO SEE ITS OWN "
          "INTERACTING CORRELATOR")
    print("  at reachable cost -- which is the same fact that makes "
          "its lattice invisible.")
    print("  The ways in are a smeared operator or a Wilson-loop "
          "static potential; neither")
    print("  is attempted here.\n")
    assert noisy      # every row noise-dominated: the failure


def s2_kinematic():
    print("== s2: what IS exactly computable -- the kinematic "
          "anisotropy ==")
    print("  free lattice field, no Monte Carlo. Two volumes, so "
          "finite-volume")
    print("  contamination is visible rather than assumed:")
    pairs = [((2, 0, 0, 0), (1, 1, 1, 1)),
             ((4, 0, 0, 0), (2, 2, 2, 2)),
             ((6, 0, 0, 0), (3, 3, 3, 3)),
             ((8, 0, 0, 0), (4, 4, 4, 4)),
             ((10, 0, 0, 0), (5, 5, 5, 5))]
    out = {}
    for L in (32, 48):
        C = free_corr(L)
        print(f"    L = {L}:   |r|    anisotropy      x (r/a)^2")
        rows = []
        for a, b in pairs:
            if max(max(a), max(b)) > L // 3:
                continue
            r = np.sqrt(sum(x * x for x in a))
            fa, fb = C[a], C[b]
            A = float((fa - fb) / (0.5 * (fa + fb)))
            rows.append((r, A))
            print(f"             {r:5.1f}    {A:+.5f}       "
                  f"{A * r * r:+.3f}")
        out[L] = rows
        del C
    big = out[48]
    scaled = [A * r * r for r, A in big]
    print(f"  at L = 48 the (r/a)^2-rescaled column is flat to "
          f"{100 * (max(scaled) / min(scaled) - 1):.0f}% across "
          f"r = 2..10")
    print("  (L = 32 drifts upward past r ~ 8: that is the "
          "finite-volume contamination,")
    print("   shown rather than assumed -- an earlier pass of this "
          "module read it as signal)")
    assert max(scaled) / min(scaled) < 2.0
    print("  SO THE LATTICE'S KINEMATIC ANISOTROPY IS O((a/r)^2), "
          "exactly as expected for")
    print(f"  an O(a^2)-improved-free discretisation, with "
          f"coefficient ~{np.mean(scaled):.1f}\n")
    return float(np.mean(scaled))


def s3_what_can_be_claimed(coef):
    print("== s3: what can and cannot be claimed ==")
    print("  IF the interacting correction is small -- which weak "
          "coupling makes plausible")
    print("  and s1 could NOT test -- then anisotropy ~ "
          f"{coef:.1f} (a/r)^2:")
    print("      r/a           implied anisotropy")
    for rr in (2, 10, 1e3, 1e6, 1.9e17):
        print(f"    {rr:12.0f}        {coef / rr ** 2:.2e}")
    print()
    print("  So at the ordered branch's xi/a ~ 1.9e17 the implied "
          "rotational -- hence,")
    print("  through Osterwalder-Schrader, LORENTZ -- violation is "
          "of order 1e-34.")
    print()
    print("  THIS IS NOT A BOUND THE PROGRAM HAS EARNED. It is the "
          "FREE-FIELD artefact")
    print("  extrapolated under an assumption s1 was too noisy to "
          "check. The standing")
    print("  'continuum Lorentz invariance, never tested' debt "
          "STAYS OPEN. What this module")
    print("  establishes is the shape of the answer, the "
          "coefficient of the kinematic part,")
    print("  and the honest cost of getting the rest: an operator "
          "whose connected")
    print("  correlator is not O(g^4).\n")


if __name__ == "__main__":
    s1_failed_measurement()
    coef = s2_kinematic()
    s3_what_can_be_claimed(coef)
