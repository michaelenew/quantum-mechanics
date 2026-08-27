"""0096 -- the bridge floor: the level is a measurable constant,
with a computed sample complexity.

The hierarchy chain's one unproven link (0094): nothing in the
constraint stack SELECTS the level N from the admissible ladder --
the menu has no knob. The lucid filter's epistemology for exactly
this situation (their p-floor; AIC/BIC refused) is: do not derive
what the data prices. Ported: the level is a learnable local
constant, and the bridge question becomes 'how many vacuum
observations pin it?' -- a computable floor, not a metaphysical
selection.

  s1  The admissible ladder, recomputed from the congruence
      (x^2 = -1 solvable mod N, 0081): 5, 13, 17, 25, 29, 37 ...
      -- matches 0081's direct scan.
  s2  Level identifiability: each admissible level N carries the
      stack weight W_N = |sum_{j <= (N-1)/2} chi_j|^2; the vacuum
      plaquette law p_N is its Born density. The KL matrix between
      admissible levels' laws is finite and O(0.1-1) nats/sample:
      adjacent levels are distinguished in tens of samples.
  s3  The floor: two-part code (universal integer price for the
      level + prequential data code). n* = samples after which the
      true level beats every admissible rival including the
      cheapest. Computed exactly from the KL matrix, then verified
      by simulation at n* (truth wins the code-length comparison).
  s4  The epistemic closure statement, printed: N is not derived;
      it is pinned by ~n* vacuum samples, the same status as any
      measured coupling. The bridge's open link is thereby reposed
      from 'why this N' to 'measure the capacity' -- with 0100/0105
      supplying the measuring channel (the boundary carries ln N
      nats).
"""

import numpy as np

TH = np.linspace(1e-7, np.pi - 1e-7, 200001)
CONF = 20.0                    # nats of posterior odds demanded


def admissible(nmax):
    out = []
    for n in range(3, nmax + 1, 2):   # odd: the even wall (0090)
        if any(pow(x, 2, n) == n - 1 for x in range(1, n)):
            out.append(n)
    return out


def p_level(N):
    J = (N - 1) / 2
    A = sum(np.sin((2 * j + 1) * TH) / np.sin(TH)
            for j in np.arange(0, J + 0.1, 0.5))
    p = A ** 2 * np.sin(TH) ** 2
    return p / np.trapezoid(p, TH)


def s1_ladder():
    print("== s1: the admissible ladder (odd, x^2 = -1 mod N) ==")
    lad = admissible(40)
    print(f"  N <= 40: {lad}")
    assert lad == [5, 13, 17, 25, 29, 37]
    print("  matches 0081's constraint-stack scan\n")
    return lad


def s2_kl(lad):
    print("== s2: the level KL matrix (nats per vacuum sample) ==")
    ps = {N: p_level(N) for N in lad}
    K = np.zeros((len(lad), len(lad)))
    for i, N in enumerate(lad):
        for j, M in enumerate(lad):
            if i != j:
                K[i, j] = np.trapezoid(
                    ps[N] * np.log(np.maximum(ps[N], 1e-300)
                                   / np.maximum(ps[M], 1e-300)), TH)
    print("       " + "".join(f"{M:>8d}" for M in lad))
    for i, N in enumerate(lad):
        print(f"  {N:3d}  " + "".join(f"{K[i, j]:8.3f}"
                                      for j in range(len(lad))))
    assert (K[~np.eye(len(lad), dtype=bool)] > 0).all()
    return ps, K


def s3_floor(lad, ps, K):
    print("\n== s3: the floor ==")
    price = {N: 2 * np.log(N) for N in lad}   # universal int code
    nstar = 0
    for i, N in enumerate(lad):
        worst = max(
            (CONF + max(price[N] - price[M], 0)) / K[i, j]
            for j, M in enumerate(lad) if j != i)
        nstar = max(nstar, worst)
        print(f"  true N = {N:3d}: pins against every rival in "
              f"<= {worst:6.1f} samples")
    nstar = int(np.ceil(nstar))
    print(f"  n* = {nstar} vacuum samples pin the level at "
          f"{CONF:.0f} nats, any truth")
    # simulation check at the hardest pair
    rng = np.random.default_rng(4)
    cdf = {N: np.cumsum(ps[N]) / np.sum(ps[N]) for N in lad}
    lp = {N: np.log(np.maximum(ps[N], 1e-300)) for N in lad}
    wins = 0
    TRIALS = 300
    for _ in range(TRIALS):
        idx = np.searchsorted(cdf[5], rng.random(nstar))
        scores = {M: lp[M][np.clip(idx, 0, len(TH) - 1)].sum()
                  - price[M] for M in lad}
        wins += max(scores, key=scores.get) == 5
    print(f"  simulation (true N = 5, n = n*): truth wins the "
          f"two-part code in {wins}/{TRIALS} trials")
    assert wins >= 0.99 * TRIALS
    return nstar


def s4_statement(nstar):
    print("\n== s4: the epistemic closure ==")
    print("  The bridge's unproven link is reposed, not forced: "
          "nothing a priori selects N")
    print("  from the admissible ladder (0094's no-knob menu), and "
          "nothing needs to --")
    print(f"  ~{nstar} vacuum plaquette observations pin it "
          f"prequentially, and the boundary")
    print("  channel carries it directly (ln N nats per closed "
          "surface, 0100/0105). The")
    print("  level has the epistemic status of a measured coupling "
          "constant: the filter's")
    print("  p-floor answer to 'why this N' is 'that is a "
          "measurement, and here is its cost'.")


if __name__ == "__main__":
    lad = s1_ladder()
    ps, K = s2_kl(lad)
    nstar = s3_floor(lad, ps, K)
    s4_statement(nstar)
    print("\nall assertions passed")
