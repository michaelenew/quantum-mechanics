"""0149 -- gamma = 1/2 is the vDVZ value, so measure the mass.

0148 added the cosmological counterterm, forced by demanding that
flat space be stationary, and the signature became Einstein-Hilbert:
exactly one negative mode at every momentum. But gamma came out
+0.5086 +- 0.0052, not +1, and light deflection 0.754 x GR.

Those are not arbitrary numbers. van Dam-Veltman-Zakharov: a MASSIVE
graviton gives gamma = 1/2 and deflection 3/4 of GR, discontinuously,
however small the mass. We measured 0.5086 and 0.754.

And the program said so already. 0056: "the lattice graviton is
massive off criticality, so the long-range Newtonian limit is a
critical point."

So: measure the mass. A massless kernel must vanish as k -> 0. Fit

    H(k) = H_0 + khat^2 H_2

per matrix element. H_0 is the non-derivative part -- a graviton mass
term, which a lattice is free to induce because it breaks
diffeomorphism invariance. Cancelling it is the second standard
fine-tuning of induced gravity, and 0056's criticality is the same
condition.

  s1  IS THERE A MASS? H_0 measured, and whether it is direction
      independent.
  s2  GAMMA FROM THE KINETIC PART ALONE.
  s3  WHAT IT COSTS: this is a tuning, not a derivation, and the
      ledger says so.
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


O = _load("0146_offdiagonal_metric.py", "o149")
S = _load("0147_the_missing_sign.py", "s149")
C = _load("0148_the_counterterm.py", "c149")
EB = O.EB
L = 12
V = L ** 4


def khat2(L, k):
    return float(sum(4 * np.sin(np.pi * ki / L) ** 2 for ki in k))


def fit_along(vh, Hct, direction, ns=(1, 2, 3, 4, 5), order=2):
    """H(k) = H_0 + khat^2 H_2 + khat^4 H_4, fitted element-wise."""
    X, Y = [], []
    for n in ns:
        k = tuple(n * d for d in direction)
        H, _ = O.hessian(vh, k, L, False)
        X.append(khat2(L, k))
        Y.append(H + Hct)
    X = np.array(X)
    Y = np.array(Y)
    A = np.vstack([X ** i for i in range(order + 1)]).T
    coef, *_ = np.linalg.lstsq(A, Y.reshape(len(X), -1), rcond=None)
    H0 = coef[0].reshape(10, 10)
    H2 = coef[1].reshape(10, 10)
    pred = (A @ coef).reshape(Y.shape)
    resid = np.abs(pred - Y).max() / np.abs(Y).max()
    return H0, H2, resid


def s1_mass():
    print("== s1: is there a graviton mass? ==")
    print("  A massless kernel vanishes as k -> 0. Fit "
          "H(k) = H_0 + khat^2 H_2 along")
    print("  three axes and look at H_0.")
    print()
    vh = O.vhat(L)
    Lc = 4.0 * O.beta_mat(vh)[0][0, 0]
    Hct = C.counterterm(Lc)
    out = []
    print("     direction      ||H_0|| / ||H_2||     fit residual")
    for d in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)):
        H0, H2, r = fit_along(vh, Hct, d)
        out.append((H0, H2))
        print(f"    {str(d):14s}   "
              f"{np.linalg.norm(H0) / np.linalg.norm(H2):8.4f}"
              f"             {r:.2e}")
    n01 = np.linalg.norm(out[0][0] - out[1][0]) / np.linalg.norm(
        out[0][0])
    print()
    print(f"  H_0 from two different axes agrees to "
          f"{n01:.2e} relative")
    print()
    print("  H_0 IS NOT ZERO. The induced kernel has a "
          "non-derivative piece -- a")
    print("  graviton mass term. A lattice is free to induce one: "
          "it breaks")
    print("  diffeomorphism invariance, which is exactly what "
          "would have forbidden it.")
    print()
    return out[0][0], out[0][1], Hct, vh, Lc


def gamma_of(H):
    Sm = S.S_AH
    j = S.source_h()
    Hh = Sm.T @ H @ Sm
    x = np.linalg.solve(Hh, -j)
    h = np.einsum("z,zmn->mn", x, EB)
    hs = (h[1, 1] + h[2, 2] + h[3, 3]) / 3.0
    return -hs / h[0, 0]


def s2_gamma(H0, vh, Hct):
    print("== s2: gamma from the kinetic part alone ==")
    print("  Cancel the non-derivative part -- the second standard "
          "fine-tuning of")
    print("  induced gravity, and 0056's 'Newton lives at a "
          "critical point'.")
    print()
    print("     k                gamma (with mass)   gamma "
          "(mass cancelled)")
    gs = []
    for k in ((0, 1, 0, 0), (0, 2, 0, 0), (0, 3, 0, 0),
              (0, 1, 1, 0), (0, 2, 1, 1)):
        H, _ = O.hessian(vh, k, L, False)
        a = gamma_of(H + Hct)
        b = gamma_of(H + Hct - H0)
        gs.append(b)
        print(f"    {str(k):14s}  {a:+.5f}            {b:+.5f}")
    gs = np.array(gs)
    print()
    print(f"  gamma = {gs.mean():+.5f} +- {gs.std():.5f} "
          f"across momenta")
    print(f"  GR: +1.   vDVZ (massive): +0.5.   Nordstrom: -1.")
    print()
    if abs(gs.mean() - 1) < 0.1:
        print("  GAMMA = +1. The quantum tier reproduces Einstein "
              "once the two standard")
        print("  fine-tunings of induced gravity are made: zero "
              "cosmological constant")
        print("  and zero graviton mass.")
        print(f"  Light deflection: (1+gamma)/2 = "
              f"{(1 + gs.mean()) / 2:.4f} x GR.")
    else:
        print(f"  gamma = {gs.mean():+.4f}. Cancelling the mass "
              f"moves it but does not")
        print("  deliver Einstein. Recorded as measured.")
    print()
    return float(gs.mean())


def s2b_the_slope(vh, Hct):
    print("== s2b: gamma from the fitted SLOPE, not a "
          "subtraction ==")
    print("  s2 failed for a numerical reason worth stating: "
          "||H_0|| is about 80x")
    print("  ||H_2|| at the momenta this box provides, so H - H_0 "
          "is a catastrophic")
    print("  cancellation and gamma came out +0.25 +- 1.56 -- a "
          "spread larger than the")
    print("  answer. That is not a measurement.")
    print()
    print("  H_2 is fitted directly, so no cancellation happens. "
          "And since the source")
    print("  is k-independent, the response is -(1/khat^2) H_2^-1 "
          "j and the 1/khat^2")
    print("  cancels in the ratio: gamma depends on H_2 alone.")
    print()
    print("  GATE: the same procedure on a pure Einstein-Hilbert "
          "kernel must give +1.")
    eh = S.eh_hessian(1.0)
    print(f"    gamma(H_2) for Einstein-Hilbert = "
          f"{gamma_of(eh):+.6f}")
    assert abs(gamma_of(eh) - 1) < 1e-9
    print()
    print("     direction        gamma(H_2)")
    gs = []
    for d in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
              (0, 1, 1, 0)):
        H0, H2, r = fit_along(vh, Hct, d)
        g = gamma_of(H2)
        gs.append(g)
        print(f"    {str(d):15s}  {g:+.5f}")
    gs = np.array(gs)
    print()
    print(f"  gamma = {gs.mean():+.5f} +- {gs.std():.5f} "
          f"across directions")
    print(f"  GR: +1.   vDVZ (massive): +0.5.   Nordstrom: -1.")
    print()
    if abs(gs.mean() - 1) < 0.12 and gs.std() < 0.12:
        print("  GAMMA = +1. The quantum tier reproduces Einstein "
              "in the kinetic sector,")
        print("  once the cosmological constant is cancelled "
              "(forced) and the graviton")
        print("  mass is separated off (0056's criticality).")
    elif abs(gs.mean() - 0.5) < 0.12 and gs.std() < 0.12:
        print("  GAMMA = +1/2 STILL -- the vDVZ value. The mass "
              "is not the whole story:")
        print("  even the kinetic operator alone is not "
              "Fierz-Pauli.")
    else:
        print(f"  gamma = {gs.mean():+.4f} +- {gs.std():.4f}. "
              f"Recorded as measured.")
    print()
    return float(gs.mean()), float(gs.std())


def s3_the_ledger(g):
    print("== s3: what this costs ==")
    print("  Two conditions were imposed, not derived:")
    print("    1. zero cosmological constant -- forced by "
          "requiring flat space to be a")
    print("       stationary point, which is not optional if you "
          "want a graviton at all;")
    print("    2. zero graviton mass -- the lattice breaks "
          "diffeomorphism invariance and")
    print("       so induces one, and it has to be subtracted.")
    print()
    print("  Both are the standard fine-tunings of induced "
          "gravity, and 0056 already")
    print("  identified the second as criticality. But they are "
          "TUNINGS. The derived-")
    print("  knob count does not go up here; if anything this "
          "says the quantum tier's")
    print("  gravity costs two conditions the classical tier "
          "gets for free, because")
    print("  its construction -- double copy plus the simplicity "
          "constraint -- builds")
    print("  diffeomorphism invariance in from the start.")
    print()
    print("  THE SEQUENCE, which is the real answer to 'what is "
          "the difference':")
    print("    no counterterms          gamma = -1     "
          "Nordstrom, zero bending")
    print("    + zero Lambda            gamma = +0.51  "
          "vDVZ, massive graviton, 3/4 GR")
    tag = "EINSTEIN" if abs(g - 1) < 0.12 else "still not Einstein"
    print(f"    + kinetic part only      gamma = {g:+.2f}     "
          f"{tag}")
    print()


if __name__ == "__main__":
    H0, H2, Hct, vh, Lc = s1_mass()
    s2_gamma(H0, vh, Hct)
    g, sd = s2b_the_slope(vh, Hct)
    s3_the_ledger(g)
    print("all assertions passed")
