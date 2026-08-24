"""0088 -- the homomorphism proper: what transports, and what the gap
is made of.

Step 2 of the crossing plan: state the lucid-filter family and the
ledger-chain family as the same kind of algebraic object, prove the
structure-preserving map where it holds, and MEASURE where it fails.
Both are transfer semigroups with a polar split and a predict/update
cycle; the map is 'swap the state-space group' -- R (filter) for the
holonomy group (physics). Three theorems verified, one gap located.

  s1  THEOREM 1 -- THE FREE TIERS ARE ISOMORPHIC. A Kalman predict
      step acts on Fourier modes as m(k) -> e^{ik mu} e^{-q k^2/2}:
      drift in the PHASE, noise in the MODULUS -- the two-ledger
      polar theorem (0086) on the group R, verified numerically to
      1e-10 on an arbitrary density. The ledger chain at heat-kernel
      weight acts on dual modes as m(n) -> omega^{n f} e^{-tau n^2}:
      same object on Z_N (flatness of -ln r_n / n^2 verified; source
      = pure phase re-verified). Both compose additively (q + q',
      tau + tau'): one semigroup, two groups.
  s2  THEOREM 2 -- ONE MK BLOCKING IS ONE KALMAN CYCLE. The bond move
      (pointwise power W^zeta) is Bayes conditioning on zeta - 1
      independent parallel replicas (precision x zeta -- exact
      Gaussian algebra, and pointwise product of weights is exactly
      how parallel bonds compose); decimation (b^2-fold convolution,
      r -> r^{b^2}) is predict. On the filter's own state space R the
      cycle with zeta = b^2 (the 4D MK exponents) is EXACTLY
      marginal: variance -> (b^2/zeta) v = v; beta_R = 0. The
      conjugate families correspond: Gaussians are exactly closed
      under the cycle; the heat-kernel family is closed to 1e-6 at
      tau = 0.1 (0092/0093). The RG is a self-measuring filter; tau
      is its posterior variance; the beta function is the variance
      recursion's residue.
  s3  THEOREM 3 -- THE GAP IS NONCOMMUTATIVE CURVATURE, NOT
      COMPACTNESS. The same cycle on three groups:
        R      (filter):            beta = 0        exactly
        U(1)   (compact, abelian):  |beta| < 1e-4   for tau <= 0.4
                                    (winding terms ~ e^{-pi^2/tau})
        SU(2)  (compact, nonabelian): beta = 0.127 tau^2
      Everything dynamical the wall contains -- running, the
      transmutation scale, confinement -- is the residue of the one
      structural ingredient the filter's state space lacks:
      noncommutative group curvature.
  s4  THE ISOMORPHISM GAP, CATALOGUED (the toy-to-prototype upgrade
      list; printed).

'Homomorphism' here means: an explicit structure-preserving
correspondence proved/verified on the free and cycle tiers, plus a
located, quantified failure list -- not a categorical functoriality
proof for the full interacting theories.
"""

import numpy as np

# ----------------------------------------------------------------------
# shared kit
# ----------------------------------------------------------------------

THS = np.linspace(1e-7, np.pi - 1e-7, 400001)      # SU(2) class angle
THU = np.linspace(-np.pi, np.pi, 400001, endpoint=False)  # U(1)


def chi_su2(j, th):
    return np.sin((2 * j + 1) * th) / np.sin(th)


def heat_su2(tau, jmax):
    W = np.zeros_like(THS)
    for j in np.arange(0, jmax + 0.1, 0.5):
        W += (2 * j + 1) * np.exp(-tau * j * (j + 1)) * chi_su2(j, THS)
    return np.maximum(W, 0)


def r_su2(W, j):
    p = W * np.sin(THS) ** 2
    return float(np.trapezoid(p * chi_su2(j, THS), THS)
                 / ((2 * j + 1) * np.trapezoid(p, THS)))


def mk_su2(tau, b=2, js=(0.5, 1, 1.5, 2)):
    W = heat_su2(tau, max(8, int(np.ceil(np.sqrt(80 / tau)))))
    Wb = (W / W.max()) ** (b * b)
    vals = [-np.log(r_su2(Wb, j)) * b * b / (j * (j + 1)) for j in js]
    return float(np.mean(vals)), max(abs(v / vals[0] - 1) for v in vals)


def heat_u1(tau, nmax=60):
    W = np.ones_like(THU)
    for n in range(1, nmax + 1):
        W += 2 * np.exp(-tau * n * n) * np.cos(n * THU)
    return np.maximum(W, 0)


def r_u1(W, n):
    return float(np.trapezoid(W * np.cos(n * THU), THU)
                 / np.trapezoid(W, THU))


def mk_u1(tau, b=2, ns=(1, 2, 3)):
    W = heat_u1(tau)
    Wb = (W / W.max()) ** (b * b)
    vals = [-np.log(r_u1(Wb, n)) * b * b / (n * n) for n in ns]
    return float(np.mean(vals)), max(abs(v / vals[0] - 1) for v in vals)


# ----------------------------------------------------------------------

def s1_free_iso():
    print("== s1: theorem 1 -- the free tiers are isomorphic ==")
    # Kalman predict on an arbitrary density: modes pick up
    # e^{ik mu} e^{-q k^2 / 2}
    x = np.linspace(-40, 40, 2 ** 15, endpoint=False)
    dx = x[1] - x[0]
    p = np.exp(-(x + 3) ** 2 / 2) + 0.6 * np.exp(-(x - 4) ** 2 / 4.5)
    p /= np.trapezoid(p, x)
    mu, q = 0.7, 0.9
    kern = np.exp(-(x - mu) ** 2 / (2 * q)) / np.sqrt(2 * np.pi * q)
    conv = np.fft.ifft(np.fft.fft(p) * np.fft.fft(kern)).real * dx
    conv = np.roll(conv, len(x) // 2)   # kernel centered at x=0 grid
    # mode integrals directly (no fft phase bookkeeping)
    devs = []
    for kk in (0.2, 0.5, 1.0, 1.7):
        m0 = np.trapezoid(p * np.exp(1j * kk * x), x)
        m1 = np.trapezoid(conv * np.exp(1j * kk * x), x)
        devs.append(abs(m1 / m0
                        - np.exp(1j * kk * mu - q * kk * kk / 2)))
    print(f"  Kalman predict on modes: max |dev| = {max(devs):.2e} "
          f"(drift in phase, noise in modulus)")
    assert max(devs) < 1e-6
    # physics side: heat-kernel chain on Z_N: -ln r_n / n^2 flat
    N, tau = 31, 0.1
    F = np.arange(N)
    W = np.ones(N)
    for n in range(1, 13):
        W += 2 * np.exp(-tau * n * n) * np.cos(2 * np.pi * n * F / N)
    rn = [float(np.sum(W * np.cos(2 * np.pi * n * F / N)) / np.sum(W))
          for n in (1, 2, 3)]
    taus = [-np.log(r) / n ** 2 for r, n in zip(rn, (1, 2, 3))]
    flat = max(abs(t / taus[0] - 1) for t in taus)
    print(f"  ledger chain (Z_31, heat weight): -ln r_n/n^2 flat to "
          f"{flat:.1e}; tau-hat = {taus[0]:.4f}")
    assert flat < 1e-6
    # source = pure phase (0086's polar theorem, one case)
    f0 = 4
    Ws = np.roll(W, f0)
    z = np.sum(Ws * np.exp(2j * np.pi * F / N)) / np.sum(Ws)
    z0 = np.sum(W * np.exp(2j * np.pi * F / N)) / np.sum(W)
    assert abs(abs(z) - abs(z0)) < 1e-12
    assert abs(np.angle(z) - np.angle(z0)
               - 2 * np.pi * f0 / N) % (2 * np.pi) < 1e-9
    print("  source shift = pure phase, modulus untouched (polar, "
          "re-verified)")
    print("  one semigroup, two groups: the free tiers are the same "
          "object\n")


def s2_cycle():
    print("== s2: theorem 2 -- one MK blocking is one Kalman cycle ==")
    v, zeta, bsq = 1.7, 4, 4
    v_series = bsq * v                    # predict: b^2 convolutions
    v_cycle = v_series / zeta             # update: zeta-replica precision
    print(f"  R: series (predict) v -> {v_series / v:.0f}v; "
          f"parallel (update) /{zeta}; cycle v -> {v_cycle / v:.2f}v")
    assert abs(v_cycle - v) < 1e-12
    print("  beta_R = 0 exactly: on the filter's state space the 4D "
          "MK cycle is marginal")
    _, leak = mk_su2(0.1)
    print(f"  conjugate families: Gaussians exactly closed (algebra); "
          f"heat kernel closed to {leak:.1e}")
    assert leak < 1e-4
    print("  the RG is a self-measuring filter: bond move = Bayes on "
          "parallel replicas,")
    print("  decimation = predict; tau is the posterior variance\n")


def s3_gap():
    print("== s3: theorem 3 -- the gap is noncommutative curvature ==")
    print("  the same cycle on three groups:")
    print("    R     : beta = 0 exactly")
    worst = 0.0
    for tau in (0.05, 0.1, 0.2, 0.4):
        to, _ = mk_u1(tau)
        worst = max(worst, abs(to - tau))
        print(f"    U(1)  : tau={tau:4.2f}  beta = {to - tau:+.6f}")
    assert worst < 1e-4
    to, _ = mk_su2(0.1)
    c = (to - 0.1) / 0.01
    print(f"    SU(2) : tau=0.10  beta = {to - 0.1:+.6f}   "
          f"(c = {c:.3f}, 0093's 0.127)")
    assert abs(c - 0.127) < 0.01
    print("  compact-but-abelian is still marginal (winding terms "
          "~ e^{-pi^2/tau} invisible):")
    print("  the running -- and with it transmutation and confinement "
          "-- is the residue of")
    print("  NONCOMMUTATIVE GROUP CURVATURE alone. That is what the "
          "wall's dynamics is made of,")
    print("  and it is precisely the ingredient the filter's state "
          "space lacks\n")


def s4_catalogue():
    print("== s4: the isomorphism gap, catalogued ==")
    print("  transports (proved/verified): the free tier (polar "
          "transfer semigroup), the")
    print("  predict/update cycle (MK = Kalman), conjugate-family "
          "closure, pinned roots =")
    print("  masslessness (0096), marginalization = hypothesis sets "
          "(0097)")
    print("  fails, with location and cure:")
    print("  1. GROUP CURVATURE -- running/transmutation/confinement "
          "(s3). Prototype upgrade:")
    print("     filtering on curved noncommutative state spaces "
          "(directional statistics on S^3)")
    print("  2. EXTERNAL INNOVATIONS -- the physics only self-"
          "conditions (parallel replicas);")
    print("     no outside data stream = no genuine time = the "
          "causal/measurement layer")
    print("  3. THE HYPOTHESIS BANK -- the physics vacuum is a point "
          "hypothesis (0097's cost");
    print("     and cure: marginalize the vacuum's scale)")
    print("  4. DISCRETE SECTORS -- the physics has superselection "
          "(center, reps); the filter's")
    print("     counterpart is discrete regimes, NOT yet in the "
          "shipped family: their 6.8%")
    print("     stratum. Pressing regime-hazard on the filter side "
          "IS building this tier\n")


if __name__ == "__main__":
    s1_free_iso()
    s2_cycle()
    s3_gap()
    s4_catalogue()
    print("all assertions passed")
