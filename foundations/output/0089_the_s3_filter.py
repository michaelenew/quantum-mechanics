"""0089 -- the S^3 filter: the fusion tax, and the beta law derived.

Gap 1's prototype brick (0098's catalogue): a tracking filter whose
state lives on SU(2) = S^3, run in the conjugate heat-kernel family.
Built to show that curvature makes the filter's precision law fail --
and the failure turned out to be cleaner than the plan: a CONSTANT.

  s1  THE FUSION TAX. Bayes fusion of two identity-centered heat
      kernels on SU(2): in precision units the flat law p = p_a + p_b
      fails by a WIDTH-INDEPENDENT constant:
          p_post = p_a + p_b - delta,     delta = 0.167 +- few %
      across tau = 0.02 .. 0.4 (equal widths; unequal-width checks
      included). On U(1) the tax is < 1e-3 for tau <= 0.4; on R it is
      zero by algebra. Curved fusion costs a fixed quantum of
      precision per fusion -- and delta is numerically consistent
      with 1/6, the DeWitt a1 = R/6 heat-coefficient flavor (S^3
      scalar curvature; identification flagged, not proven).
  s2  THE BETA LAW, DERIVED. An MK bond move W^zeta is zeta - 1
      fusions; propagating the constant tax through bond move +
      decimation gives
          beta(tau) = (1 - 1/b^2) * delta * tau^2
      predicting c(b=2) = 0.75 delta = 0.125 and c(b=3) =
      0.889 delta = 0.148 against 0093's measured 0.127 and 0.151
      (within ~2%). The MK 'scheme dependence' is a law, and the
      scheme-independent object is delta -- the elementary fusion
      tax. The beta function is literally: how much information the
      geometry's self-measurement loses to curvature per fusion.
  s3  THE RUNNING FILTER. The full cycle (predict tau + tau_q, update
      against a width-tau_r likelihood) iterated to its stationary
      width: on SU(2) the fixed point exceeds the flat-space Kalman
      fixed point, and the excess grows with the noise scale -- the
      walking filter on S^3 has a running stationary width; on R it
      cannot. (The data-side face of asymptotic freedom's IR growth.)
  s4  FAMILY BREAKDOWN. The conjugate description's leak grows from
      3e-4 (tau = 0.4) through percent level beyond tau ~ 1: the
      curved filter's strong-coupling scale, where the one-parameter
      family stops describing its own posterior. (True lock-loss also
      needs the association/centering problem -- out of scope,
      flagged.)
"""

import numpy as np

THS = np.linspace(1e-7, np.pi - 1e-7, 400001)
THU = np.linspace(-np.pi, np.pi, 400001, endpoint=False)


def chi(j, th):
    return np.sin((2 * j + 1) * th) / np.sin(th)


def heat_su2(tau, jmax=None):
    jmax = jmax or max(8, int(np.ceil(np.sqrt(80 / tau))))
    W = np.zeros_like(THS)
    for j in np.arange(0, jmax + 0.1, 0.5):
        W += (2 * j + 1) * np.exp(-tau * j * (j + 1)) * chi(j, THS)
    return np.maximum(W, 0)


def fit_su2(W, js=(0.5, 1, 1.5, 2)):
    p = W * np.sin(THS) ** 2
    Z = np.trapezoid(p, THS)
    taus = []
    for j in js:
        r = np.trapezoid(p * chi(j, THS), THS) / ((2 * j + 1) * Z)
        taus.append(-np.log(max(r, 1e-300)) / (j * (j + 1)))
    return float(np.mean(taus)), max(abs(v / taus[0] - 1) for v in taus)


def heat_u1(tau, nmax=80):
    W = np.ones_like(THU)
    for n in range(1, nmax + 1):
        W += 2 * np.exp(-tau * n * n) * np.cos(n * THU)
    return np.maximum(W, 0)


def fit_u1(W, ns=(1, 2, 3)):
    Z = np.trapezoid(W, THU)
    taus = []
    for n in ns:
        r = np.trapezoid(W * np.cos(n * THU), THU) / Z
        taus.append(-np.log(max(r, 1e-300)) / (n * n))
    return float(np.mean(taus)), max(abs(v / taus[0] - 1) for v in taus)


def s1_fusion_tax():
    print("== s1: the fusion tax ==")
    deltas = []
    for tau in (0.02, 0.05, 0.1, 0.2, 0.4):
        tu, _ = fit_su2(heat_su2(tau) ** 2)
        delta = 2 / tau - 1 / tu
        deltas.append(delta)
        print(f"  equal widths tau={tau:4.2f}: p_a + p_b - p_post = "
              f"{delta:.4f}")
    # unequal widths
    for ta, tb in ((0.05, 0.2), (0.1, 0.4)):
        tu, _ = fit_su2(heat_su2(ta) * heat_su2(tb))
        delta = 1 / ta + 1 / tb - 1 / tu
        deltas.append(delta)
        print(f"  unequal ({ta},{tb}):        tax = {delta:.4f}")
    d = np.array(deltas)
    d0 = float(d.mean())
    print(f"  SU(2): a WIDTH-INDEPENDENT tax, delta = {d0:.4f} "
          f"(spread {100 * d.std() / d0:.1f}%)")
    assert d.std() / d0 < 0.06
    assert abs(d0 - 1 / 6) < 0.01
    print(f"  numerically consistent with 1/6 = {1 / 6:.4f} "
          f"(DeWitt a1 = R/6 flavor -- flagged, not proven)")
    for tau in (0.1, 0.4):
        tu, _ = fit_u1(heat_u1(tau) ** 2)
        du = 2 / tau - 1 / tu
        print(f"  U(1) tau={tau}: tax = {du:.2e}")
        assert abs(du) < 1e-3
    print("  R: zero by algebra. The tax is curvature's, alone\n")
    return d0


def s2_beta_law(delta):
    print("== s2: the beta law, derived ==")
    meas = {2: 0.127, 3: 0.151}
    for b in (2, 3):
        pred = (1 - 1 / b ** 2) * delta
        print(f"  b={b}: (1 - 1/b^2) delta = {pred:.4f}   vs 0093 "
              f"measured {meas[b]:.3f}   "
              f"({100 * abs(pred / meas[b] - 1):.1f}%)")
        assert abs(pred / meas[b] - 1) < 0.03
    print("  beta(tau) = (1 - 1/b^2) delta tau^2: the MK scheme "
          "dependence is a law, delta is")
    print("  the scheme-independent core: the beta function measures "
          "the information the")
    print("  geometry's self-measurement loses to curvature, per "
          "fusion\n")


def s3_running_filter():
    print("== s3: the running filter ==")
    tau_r = 0.1
    print(f"  cycle: predict (+tau_q), update against width-{tau_r} "
          f"likelihood; stationary width:")
    for tau_q in (0.005, 0.02, 0.05, 0.1):
        # flat fixed point
        tf = (-tau_q + np.sqrt(tau_q ** 2 + 4 * tau_q * tau_r)) / 2
        # curved: iterate
        t = tf
        for _ in range(60):
            pred = t + tau_q
            post, _ = fit_su2(heat_su2(pred) * heat_su2(tau_r))
            t = post
        exc = (t - tf) / tf
        print(f"  tau_q={tau_q:5.3f}: flat {tf:.4f}  SU(2) {t:.4f}  "
              f"excess {100 * exc:+.1f}%")
        assert t > tf
    print("  the S^3 walking filter's stationary width runs with the "
          "noise scale; on R it")
    print("  cannot -- the data-side face of the coupling's IR "
          "growth\n")


def s4_breakdown():
    print("== s4: family breakdown ==")
    prev = 0.0
    for tau in (0.4, 0.8, 1.5, 2.5):
        _, leak = fit_su2(heat_su2(tau) ** 2)
        print(f"  tau={tau:4.2f}: conjugate-family leak = {leak:.4f}")
        assert leak >= prev - 1e-6
        prev = leak
    print("  the one-parameter description degrades past tau ~ 1: "
          "the curved filter's")
    print("  strong-coupling scale. (Full lock-loss needs the "
          "association problem -- flagged,")
    print("  out of scope)\n")


if __name__ == "__main__":
    d0 = s1_fusion_tax()
    s2_beta_law(d0)
    s3_running_filter()
    s4_breakdown()
    print("all assertions passed")
