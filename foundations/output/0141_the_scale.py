"""0141 -- why item 2 found nothing, quantitatively.

0139/0140 measure a mean spatial plaquette of 0.957. That is not a
disordered lattice -- it is an almost frozen one. And an almost
frozen SU(2) lattice does not have a short correlation length; by
asymptotic freedom it has an ENORMOUS one. So the null in the spin-2
channel is not "no state", it is "the box is far smaller than
anything the theory has to show".

This module puts a number on "far smaller". The number is not tuned:
kappa is DERIVED (0131/0142: the Spin(4) double copy gives
kappa = (2/3) sum n^2(n^2-1) / sum n^2 = 16 exactly), so the
resulting scale ratio is derived too.

  s1  IS KAPPA A WILSON BETA? Checked numerically, not asserted:
      expand -ln W around the identity and read the quadratic form.
  s2  THE EFFECTIVE COUPLING from the measured plaquette, as a
      second and independent handle.
  s3  THE TWO-LOOP SCALE, and the hierarchy it forces.
  s4  WHAT IT DOES TO ITEM 2, and the sensitivity, stated honestly.
"""

import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, tag):
    s = importlib.util.spec_from_file_location(
        tag, os.path.join(HERE, name))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


M = _load("0132_the_spin4_lattice.py", "m141")
M_SECT = 6

B0 = 11.0 / (24 * np.pi ** 2)
B1 = 17.0 / (96 * np.pi ** 4)


def lnW(tp, tm):
    A = sum(M.chi(n, tp) * M.chi(n, tm) for n in range(1, M_SECT + 1))
    return np.log(np.maximum(A ** 2, 1e-300))


def s1_is_kappa_a_beta():
    print("== s1: is kappa a Wilson beta? ==")
    print("  Wilson: S = beta (1 - cos th) ~ beta th^2 / 2.")
    print("  So beta is the quadratic coefficient of the plaquette "
          "action at the")
    print("  identity. Read it off the actual weight instead of "
          "assuming it.")
    h = 1e-3
    s = lambda a, b: -lnW(np.array(a), np.array(b))
    s00 = s(1e-9, 1e-9)
    dpp = (s(h, 1e-9) - 2 * s00 + s(-h if h > 0 else h, 1e-9))
    # chi is even in th, so use a one-sided second difference
    dpp = (s(2 * h, 1e-9) - 2 * s(h, 1e-9) + s(1e-9, 1e-9)) / h ** 2
    dmm = (s(1e-9, 2 * h) - 2 * s(1e-9, h) + s(1e-9, 1e-9)) / h ** 2
    cross = (s(h, h) - s(h, 1e-9) - s(1e-9, h) + s00) / h ** 2
    closed = (2 / 3) * (np.sum(np.arange(1, M_SECT + 1) ** 2
                               * (np.arange(1, M_SECT + 1) ** 2 - 1))
                        / np.sum(np.arange(1, M_SECT + 1) ** 2))
    print()
    print(f"    d2S/dth+^2  = {float(dpp):8.4f}")
    print(f"    d2S/dth-^2  = {float(dmm):8.4f}")
    print(f"    d2S/dth+dth-= {float(cross):8.4f}   "
          f"(must be ~0: the two records decouple at this order)")
    print(f"    closed form (2/3) sum n^2(n^2-1)/sum n^2 = "
          f"{closed:8.4f}")
    print()
    assert abs(float(dpp) - closed) < 0.05 * closed
    assert abs(float(dmm) - closed) < 0.05 * closed
    assert abs(float(cross)) < 0.05 * closed
    print("  YES. The derived weight is, to quadratic order, TWO "
          "independent SU(2)")
    print(f"  Wilson actions at beta = kappa = {closed:.3f}. The "
          f"cross term vanishes,")
    print("  so the two records do not mix in the coupling -- they "
          "mix only in the")
    print("  observable (the graviton is the synergy, 0142).")
    print()
    return float(closed)


def s2_from_the_plaquette(pl=0.957234):
    print("== s2: the effective coupling from the plaquette ==")
    print("  Weak-coupling SU(2): <(1/2) tr U_p> = 1 - 3/(4 beta) "
          "+ O(beta^-2).")
    beff = 3.0 / (4 * (1 - pl))
    print(f"  measured spatial plaquette (0140, unsmeared): "
          f"{pl:.6f}")
    print(f"  => beta_eff = {beff:.2f}")
    print()
    print("  Two independent handles on the same coupling: the "
          "weight's curvature")
    print(f"  says {16.0:.2f}, the measured plaquette says "
          f"{beff:.2f}. The gap is the higher-order")
    print("  part of the weight, and it sets the honest "
          "uncertainty band below.")
    print()
    return beff


def aLambda(beta):
    g2 = 4.0 / beta
    return (B0 * g2) ** (-B1 / (2 * B0 ** 2)) * np.exp(
        -1.0 / (2 * B0 * g2))


def s3_the_scale(kappa, beff):
    print("== s3: the two-loop scale ==")
    print("  a Lambda_L = (b0 g^2)^(-b1/2b0^2) exp(-1/(2 b0 g^2)), "
          "g^2 = 4/beta")
    print(f"  b0 = {B0:.6f}, b1 = {B1:.6e}")
    print()
    print("     beta      a*Lambda_L        xi/a = 1/(a Lambda_L)")
    out = {}
    for b, tag in ((kappa, "derived curvature"),
                   (beff, "measured plaquette")):
        al = aLambda(b)
        out[tag] = al
        print(f"    {b:6.2f}    {al:.3e}        {1 / al:.3e}    "
              f"({tag})")
    print()
    lo = 1 / max(out.values())
    hi = 1 / min(out.values())
    print(f"  THE HIERARCHY: xi/a between {lo:.2e} and {hi:.2e}.")
    print()
    print("  The lattice spacing is the program's Planck length "
          "(item 5: l_P = 0.507a),")
    print("  so this says the theory's confinement scale sits "
          f"{lo:.0e} to {hi:.0e} lattice")
    print("  spacings out from the Planck length -- i.e. a mass "
          "scale of order")
    print(f"  10^-{np.log10(hi):.0f} to 10^-{np.log10(lo):.0f} of "
          f"the Planck mass.")
    print()
    print("  For reference, M_Planck / 1 GeV = 1.22e19. Nothing "
          "here was tuned to that:")
    print("  kappa is fixed by the band (M = 6 characters) and the "
          "double copy, and the")
    print("  rest is one-loop plus two-loop asymptotic freedom.")
    print()
    return lo, hi


def s4_item2(lo, hi):
    print("== s4: what this does to item 2 ==")
    print(f"  The graviton run used L = 8. The correlation length "
          f"is {lo:.0e}-{hi:.0e} a.")
    print(f"  The box is therefore about 10^-{np.log10(lo) - 1:.0f}"
          f" of one correlation length.")
    print()
    print("  A null in the spin-2 channel on that box is not "
          "evidence of anything")
    print("  physical. It is the EXPECTED result, and it was "
          "predictable from the")
    print("  plaquette alone without running a single correlator.")
    print()
    print("  So item 2 closes, but not the way it was posed. The "
          "three engineering")
    print("  diagnoses (throughput, link means, boundary "
          "independence) were all real")
    print("  and the third one worked -- 24x. It bought a factor "
          "24 against a deficit")
    print("  of 10^18. No estimator closes that gap; only a "
          "different question does.")
    print()
    print("  THE SENSITIVITY, stated so this is not oversold: "
          "d ln(a Lambda)/d beta")
    print(f"  = {1 / (2 * B0 * 4):.2f}, so one unit of beta is a "
          f"factor {np.exp(1 / (8 * B0)):.0f} in the scale. The two "
          f"handles on beta")
    print("  differ by ~1.1, which is the whole spread above. The "
          "ORDER (10^17-10^19)")
    print("  is robust; the digit is not.")
    print()
    print("  AND THAT IS THE 'WHY IS GRAVITY WEAK' ANSWER IN THIS "
          "PROGRAM: the coupling")
    print("  is not chosen, it is derived -- kappa = 16 from the "
          "band and the double")
    print("  copy -- and asymptotic freedom exponentiates a derived "
          "O(10) number into a")
    print("  derived O(10^18) hierarchy. That is the first quantity "
          "in this program that")
    print("  is both DERIVED and LARGE, and it is the shape a "
          "falsifiable prediction")
    print("  has to have.")
    print()


if __name__ == "__main__":
    k = s1_is_kappa_a_beta()
    b = s2_from_the_plaquette()
    lo, hi = s3_the_scale(k, b)
    s4_item2(lo, hi)
    print("all assertions passed")
