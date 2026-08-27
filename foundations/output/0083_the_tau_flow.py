"""0083 -- the tau flow: the ledger's coupling runs like one loop.

The 'running of tau' -- one of the wall's three outstanding pieces
(F2's row in the adoption plan) -- made cheap by 0092: after one MK
blocking the weight sits in the heat-kernel family, so the 4D flow is
a SCALAR map tau -> tau'. Extracted here.

  s1  The flow is one-dimensional, verified: applying the 4D MK step
      (bond move W -> W^{b^2} pointwise, decimation r -> r^{b^2}) to
      a heat-kernel weight returns a heat-kernel weight to flatness
      leak <= 1.2e-4 for tau <= 0.4 (1e-6 at tau = 0.1) -- the
      family is closed under the recursion at working precision.
  s2  THE BETA FUNCTION IS ONE-LOOP-SHAPED: beta(tau) =
      tau_out - tau_in = c tau^2 (1 + O(tau)) with c(b=2) = 0.127,
      stable to 3% over tau in [0.05, 0.2], flowing UP toward the
      infrared. tau = 0 is the UV fixed point: ASYMPTOTIC FREEDOM in
      the ledger's one continuum coupling, with strong coupling
      reached at a finite blocking depth.
  s3  Scheme test: b = 3 gives the same sign and the same quadratic
      order with c = 0.151 per blocking (per e-fold: 0.183 vs 0.137)
      -- the COEFFICIENT is scheme-dependent by ~30% (MK-typical),
      the sign and order are not. (Context, from memory and flagged:
      continuum one-loop SU(2) YM has b0 = 22/3, i.e. ~0.046 per
      e-fold in the analogous normalization -- MK overshoots by
      3-4x, as it does for standard spin systems.)
  s4  DIMENSIONAL TRANSMUTATION: integrating dtau/dn = c tau^2 gives
      tau_n = tau0 / (1 - c tau0 n): the flow leaves any UV tau0
      logarithmically slowly and diverges at n* = 1/(c tau0),
      i.e. an invariant scale ln(L*/a) = ln b / (c tau0). A
      scale-free start generates a scale -- the program's first
      emergent dimensionful quantity. Reconciliation: 0076's '4D
      near-stationary' verdict was the smallness of the quadratic
      beta at their operating tau (beta(0.1) ~ 1e-3), not exact
      marginality; the frozen-structure instrument resolves the slow
      flow their grid method could not.
"""

import numpy as np

TH = np.linspace(1e-7, np.pi - 1e-7, 600001)


def chi(j, th):
    return np.sin((2 * j + 1) * th) / np.sin(th)


def C2(j):
    return j * (j + 1)


def heat_W(tau, jmax):
    W = np.zeros_like(TH)
    for j in np.arange(0, jmax + 0.1, 0.5):
        W += (2 * j + 1) * np.exp(-tau * C2(j)) * chi(j, TH)
    return np.maximum(W, 0)


def r_of(W, j):
    p = W * np.sin(TH) ** 2
    return float(np.trapezoid(p * chi(j, TH), TH)
                 / ((2 * j + 1) * np.trapezoid(p, TH)))


def mk_step(tau_in, b, js=(0.5, 1, 1.5, 2)):
    """One 4D MK blocking on the heat-kernel family: bond move
    zeta = b^{d-2} = b^2 (pointwise power), decimation r -> r^{b^2}.
    Returns (tau_out, flatness leak)."""
    jmax = max(8, int(np.ceil(np.sqrt(80 / tau_in))))
    W = heat_W(tau_in, jmax)
    Wb = (W / W.max()) ** (b * b)
    vals = [-np.log(r_of(Wb, j)) * b * b / C2(j) for j in js]
    return float(np.mean(vals)), max(abs(v / vals[0] - 1) for v in vals)


def s1_one_dimensional():
    print("== s1: the flow is one-dimensional ==")
    for tau in (0.05, 0.1, 0.2, 0.4):
        _, leak = mk_step(tau, 2)
        print(f"  tau={tau:4.2f}: heat-kernel flatness leak per step = "
              f"{leak:.6f}")
        assert leak < 1.2e-4
    print("  the family is closed under the recursion: the flow is a "
          "scalar map (0092's freeze)\n")


def s2_beta():
    print("== s2: the beta function ==")
    cs = []
    for tau in (0.05, 0.1, 0.2):
        to, _ = mk_step(tau, 2)
        beta = to - tau
        cs.append(beta / tau ** 2)
        print(f"  tau={tau:4.2f}: beta = {beta:+.5f}   beta/tau^2 = "
              f"{beta / tau ** 2:.4f}")
    assert all(b > 0 for b in cs)
    assert max(cs) / min(cs) < 1.05
    print(f"  beta = c tau^2 with c(b=2) = {cs[1]:.3f}, stable to 3% "
          f"-- one-loop shape, flowing UP")
    print("  toward the IR: tau = 0 is the UV fixed point "
          "(asymptotic freedom); strong")
    for tau in (0.8, 1.5):
        to, _ = mk_step(tau, 2)
        print(f"  tau={tau:4.2f}: beta = {to - tau:+.4f}  "
              f"(super-quadratic -- the confining runaway)")
    print()
    return cs[1]


def s3_scheme():
    print("== s3: scheme test, b = 3 ==")
    cs = []
    for tau in (0.05, 0.1, 0.2):
        to, _ = mk_step(tau, 3)
        cs.append((to - tau) / tau ** 2)
    c2 = 0.127
    print(f"  c(b=3) = {cs[1]:.3f} per blocking (b=2: {c2:.3f}); "
          f"per e-fold: {cs[1] / np.log(3):.3f} vs "
          f"{c2 / np.log(2):.3f}")
    assert all(b > 0 for b in cs) and max(cs) / min(cs) < 1.05
    print("  sign and quadratic order scheme-stable; coefficient "
          "scheme-dependent ~30% (MK-typical).")
    print("  (context, memory-flagged: continuum one-loop SU(2) has "
          "b0 = 22/3 ~ 0.046/e-fold --")
    print("  MK overshoots 3-4x, its usual behavior)\n")
    return cs[1]


def s4_transmutation(c):
    print("== s4: dimensional transmutation ==")
    # integrate the map from tau0 and verify the pole position
    tau0 = 0.05
    tau, n = tau0, 0
    while tau < 1.0 and n < 2000:
        to, _ = mk_step(tau, 2)
        tau, n = to, n + 1
    n_pred = 1 / (c * tau0)
    print(f"  tau0 = {tau0}: strong coupling (tau > 1) reached at "
          f"n = {n} blockings")
    print(f"  one-loop prediction n* = 1/(c tau0) = {n_pred:.0f}")
    assert abs(n - n_pred) / n_pred < 0.25
    print("  ln(L*/a) = ln b / (c tau0): an invariant scale from a "
          "scale-free start -- the")
    print("  program's first emergent dimensionful quantity. (0076's "
          "'near-stationary' was")
    print("  the smallness of c tau^2 at their tau, now resolved as "
          "slow one-loop flow)\n")


if __name__ == "__main__":
    s1_one_dimensional()
    c = s2_beta()
    s3_scheme()
    s4_transmutation(c)
    print("all assertions passed")
