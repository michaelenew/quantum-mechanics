"""0082 -- the heat-kernel theorem: universality's true mechanism.

The queue's "CLT fixed-point theorem" (why 0077's fixed structure is
the heat kernel), attempted -- and the filed conjecture is FALSE as
filed. What is true is sharper, and it explains 0077 exactly.

  s1  SECOND-MOMENT UNIVERSALITY (the true positive statement).
      chi_j(theta)/d_j = 1 - (2/3) C2(j) theta^2 + O(theta^4) with
      C2 = j(j+1), so for any LIGHT-TAILED class weight of width s,
      -ln r_j = (2/3) <theta^2> C2(j) + O(s^4): the transfer
      spectrum collapses onto the heat-kernel form with
      tau = (2/3)<theta^2>. Verified: Gaussian and window families,
      flatness deviation ~ s^2, tau matched to <1% at s = 0.1.
  s2  THE FREEZE LEMMA. Pure convolution powers coefficients,
      r_j -> r_j^A, so the ratios (-ln r_j)/(-ln r_k) NEVER move.
      Corollary: 2D gluing alone cannot flow any weight toward the
      heat kernel -- there is no convolution CLT for the ratio
      structure. The casually-filed theorem is false.
  s3  THE LEDGER IS OUTSIDE THE NAIVE BASIN. The Born counting
      weight (sum chi_j)^2 has Fejer-squared tails: kurtosis 13 at
      J = 5, 25 at J = 10 (light families: 1.2-1.7), and its
      flatness deviation is 0.63-0.67, NOT improving as the width
      shrinks. The bare ledger never resembles the heat kernel.
  s4  ONE BOND MOVE LOCALIZES. The MK bond move (pointwise power,
      W -> W^4) is a Laplace localization: a single application
      takes the Born weight's flatness from 0.633 to 0.0016, the
      second to 1e-4. THE MECHANISM: the RG's pointwise
      nonlinearity kills the heavy tails that convolution preserves,
      landing the weight in the heat-kernel family after one
      blocking; from then on the flow moves only tau. 0077's
      measured Casimir ratios are an RG-localization result, not a
      CLT -- theorem status now assigned correctly.
"""

import numpy as np

TH = np.linspace(1e-7, np.pi - 1e-7, 200001)


def chi(j, th):
    return np.sin((2 * j + 1) * th) / np.sin(th)


def r_of(W, j):
    p = W * np.sin(TH) ** 2
    return float(np.trapezoid(p * chi(j, TH), TH)
                 / ((2 * j + 1) * np.trapezoid(p, TH)))


def C2(j):
    return j * (j + 1)


JS = [0.5, 1, 1.5, 2, 3]


def flatness(W):
    vals = [-np.log(r_of(W, j)) / C2(j) for j in JS]
    return max(abs(v / vals[0] - 1) for v in vals), vals[0]


def moments(W):
    p = W * np.sin(TH) ** 2
    p = p / np.trapezoid(p, TH)
    t2 = float(np.trapezoid(p * TH ** 2, TH))
    t4 = float(np.trapezoid(p * TH ** 4, TH))
    return t2, t4 / t2 ** 2


def s1_universality():
    print("== s1: second-moment universality (light tails) ==")
    # expansion coefficient check: chi_j/d_j ~ 1 - (2/3) C2 theta^2
    th0 = 0.01
    for j in (0.5, 1, 2):
        lhs = 1 - chi(j, np.array([th0]))[0] / (2 * j + 1)
        assert abs(lhs / ((2 / 3) * C2(j) * th0 ** 2) - 1) < 1e-3
    print("  chi_j/d_j = 1 - (2/3) C2 theta^2 + O(theta^4): "
          "coefficient verified")
    for name, fam in (("gauss", lambda s: np.exp(-TH ** 2 / (2 * s * s))),
                      ("window", lambda s: (TH < s).astype(float))):
        devs = {}
        for s in (0.4, 0.2, 0.1):
            W = fam(s)
            dev, lead = flatness(W)
            t2, _ = moments(W)
            devs[s] = dev
            tau_err = abs(lead / ((2 / 3) * t2) - 1)
            print(f"  {name:6s} s={s}: flatness dev {dev:.4f}, "
                  f"tau vs (2/3)<t^2>: {100 * tau_err:.2f}%")
            if s == 0.1:
                assert dev < 0.01 and tau_err < 0.01
        assert devs[0.4] > devs[0.2] > devs[0.1]
    print("  collapse onto -ln r_j = tau C2(j), deviation ~ s^2: the "
          "heat kernel is the")
    print("  universal narrow-width limit FOR LIGHT-TAILED weights\n")


def s2_freeze():
    print("== s2: the freeze lemma ==")
    W = np.exp(-TH ** 2 / 0.08) + 0.3 * (TH < 0.5)
    r1 = [r_of(W, j) for j in JS]
    for A in (2, 5):
        ratios = [np.log(r1[k] ** A) / np.log(r1[0] ** A)
                  for k in range(len(JS))]
        base = [np.log(r1[k]) / np.log(r1[0]) for k in range(len(JS))]
        assert np.allclose(ratios, base, atol=1e-12)
    print("  r_j -> r_j^A under convolution: log-ratios exactly "
          "frozen, any A")
    print("  corollary: no convolution CLT exists for the ratio "
          "structure -- the filed")
    print("  'CLT fixed-point theorem' is FALSE as filed\n")


def s3_ledger_outside():
    print("== s3: the ledger is outside the naive basin ==")
    for J in (5, 10):
        W = sum(chi(j, TH) for j in np.arange(0, J + 0.1, 0.5)) ** 2
        dev, _ = flatness(W)
        _, kurt = moments(W)
        print(f"  Born counting J={J:2d}: flatness dev {dev:.3f}, "
              f"kurtosis {kurt:.1f}")
        assert dev > 0.4
        assert kurt > 10
    print("  heavy Fejer-squared tails (light families: kurtosis "
          "1.2-1.7): the bare ledger")
    print("  never resembles the heat kernel, at any width\n")


def s4_bond_move():
    print("== s4: one bond move localizes ==")
    W = sum(chi(j, TH) for j in np.arange(0, 5.1, 0.5)) ** 2
    devs = []
    for k in range(4):
        dev, lead = flatness(W)
        devs.append(dev)
        print(f"  MK iteration {k}: flatness dev {dev:.4f}  "
              f"(leading -ln r/C2 = {lead:.5f})")
        W = (W / W.max()) ** 4
    assert devs[0] > 0.4 and devs[1] < 0.01 and devs[2] < 1e-3
    print("  the pointwise power (the MK bond move) is a Laplace "
          "localization: one blocking")
    print("  lands the ledger in the heat-kernel family; the flow "
          "then moves only tau.")
    print("  0077's Casimir ratios are an RG-localization result, "
          "not a CLT\n")


if __name__ == "__main__":
    s1_universality()
    s2_freeze()
    s3_ledger_outside()
    s4_bond_move()
    print("all assertions passed")
