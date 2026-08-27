"""0148 -- flat space was never a solution.

Before testing the constrained sector I re-derived 0146's setup and
found an omission that has to be fixed first, because it changes the
sign structure on its own.

A Hessian is only parametrisation-independent AT A STATIONARY POINT.
0146 expanded the induced action around W = I and never checked
whether that is one. It is not. With W = exp(2A),

    Gamma = (1/2) ln det'(D^T W D),   Gamma^(1)[A] = tr(B A),

and for uniform A = eps I this is exactly rank(B) * eps = 4(V-1) eps
-- large and nonzero. That is the INDUCED COSMOLOGICAL CONSTANT. Flat
space is not a solution of the induced action alone, so its Hessian
there is not the graviton kinetic operator; it is the second
derivative at a non-stationary point, and it is parametrisation
dependent. (Indeed: in the LINEAR variable W the same Gamma is
concave, since ln det is concave and ln Z is convex. The whole sign
flips with the choice of variable, which is the tell.)

The fix is the standard one in induced gravity, and it is forced, not
tuned: add the bare cosmological term and fix its coefficient by
demanding that flat space BE stationary. With
sqrt(g) = det(W)^(1/2) = exp(tr A),

    S_ct = c sum_x exp(tr A(x)),   c fixed by Gamma^(1) + S_ct^(1) = 0

and the second-order part of S_ct, c (tr A)^2 / 2 per site, is a
NEGATIVE contribution in the trace direction -- exactly the conformal
mode.

  s1  THE INDUCED LAMBDA, measured, and the coefficient it forces.
  s2  THE SPECTRUM WITH THE COUNTERTERM. GR needs nine positive and
      exactly one negative.
  s3  GAMMA.
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


O = _load("0146_offdiagonal_metric.py", "o148")
S = _load("0147_the_missing_sign.py", "s148")
EB, PAIRS = O.EB, O.PAIRS
L = 12
V = L ** 4


def s1_lambda():
    print("== s1: the induced cosmological constant ==")
    lat = O.F.M.mklat(4)
    v4 = lat["V"]
    one = [np.tile([1.0, 0, 0, 0], (v4, 1)) for _ in range(4)]
    D = O.F.build_D(one, one, lat)
    B = O.F.projector(D)
    rk = float(np.trace(B))
    print(f"  L = 4:  rank(B) = tr(B) = {rk:.4f}, "
          f"4(V-1) = {4 * (v4 - 1)}")
    assert abs(rk - 4 * (v4 - 1)) < 1e-6
    print("  Gamma^(1)[A] = tr(B A), so for uniform A = eps I the "
          "first derivative is")
    print(f"  {rk:.0f} eps -- NOT ZERO. Flat space is not a "
          f"stationary point of the induced")
    print("  action, so 0146's Hessian was taken at the wrong "
          "place.")
    print()
    vh = O.vhat(L)
    b, _ = O.beta_mat(vh)
    Lc = 4.0 * b[0, 0]
    print(f"  Linear coefficient per site, from beta: "
          f"L = 4*beta_00 = {Lc:.8f}")
    print(f"  Closed form (V-1)/V                     = "
          f"{(V - 1) / V:.8f}")
    assert abs(Lc - (V - 1) / V) < 1e-8
    print()
    print("  So the counterterm coefficient is c = -L, forced by "
          "stationarity. Nothing")
    print("  is tuned: it is the unique value that makes flat "
          "space a solution.")
    print()
    return Lc


def counterterm(Lc):
    """H_ct[a,c] = -(L V / 2) tr(E_a) tr(E_c)."""
    t = np.array([np.trace(EB[a]) for a in range(10)])
    return -(Lc * V / 2.0) * np.outer(t, t)


def s2_spectrum(Lc):
    print("== s2: the spectrum, with the counterterm ==")
    print("  Einstein-Hilbert needs NINE POSITIVE and EXACTLY ONE "
          "NEGATIVE.")
    print()
    vh = O.vhat(L)
    Hct = counterterm(Lc)
    print("     k                 without ct        with ct       "
          "  verdict")
    ok = True
    for k in ((0, 1, 0, 0), (0, 2, 0, 0), (0, 1, 1, 0),
              (0, 2, 1, 1), (0, 3, 0, 0)):
        HA, _ = O.hessian(vh, k, L, False)
        w0 = np.linalg.eigvalsh(HA)
        w1 = np.linalg.eigvalsh(HA + Hct)
        n0 = int((w0 < -1e-6 * abs(w0).max()).sum())
        n1 = int((w1 < -1e-6 * abs(w1).max()).sum())
        good = (n1 == 1)
        ok &= good
        print(f"    {str(k):14s}   {n0} negative       "
              f"{n1} negative      "
              f"{'EH structure' if good else 'NOT EH'}")
    print()
    if ok:
        print("  EXACTLY ONE NEGATIVE MODE AT EVERY MOMENTUM. The "
              "counterterm supplies")
        print("  the conformal mode's sign, and it supplies "
              "exactly one -- which is the")
        print("  Einstein-Hilbert signature, not an arbitrary "
              "indefiniteness.")
    else:
        print("  NOT the Einstein-Hilbert signature. Recorded as "
              "measured.")
    print()
    return ok


def s3_gamma(Lc):
    print("== s3: gamma ==")
    vh = O.vhat(L)
    Hct = counterterm(Lc)
    Sm = S.S_AH
    j = S.source_h()
    print("     k                 gamma (no ct)     gamma (with ct)")
    gs = []
    for k in ((0, 1, 0, 0), (0, 2, 0, 0), (0, 1, 1, 0),
              (0, 2, 1, 1), (0, 3, 0, 0)):
        HA, _ = O.hessian(vh, k, L, False)

        def g_of(H):
            Hh = Sm.T @ H @ Sm
            x = np.linalg.solve(Hh, -j)
            h = np.einsum("z,zmn->mn", x, EB)
            hs = (h[1, 1] + h[2, 2] + h[3, 3]) / 3.0
            return -hs / h[0, 0]

        a, b = g_of(HA), g_of(HA + Hct)
        gs.append(b)
        print(f"    {str(k):14s}   {a:+.5f}          {b:+.5f}")
    gs = np.array(gs)
    print()
    print(f"  with counterterm: gamma = {gs.mean():+.5f} "
          f"+- {gs.std():.5f} across momenta")
    print(f"  GR: +1.   Nordstrom: -1.")
    print()
    if abs(gs.mean() - 1) < 0.1 and gs.std() < 0.1:
        print("  GAMMA = +1. The quantum tier passes the classical "
              "tests once flat space")
        print("  is actually a solution. 0146's -1 came from "
              "expanding around a point")
        print("  that is not stationary, with an induced "
              "cosmological constant of order")
        print("  the cutoff left in.")
        print()
        print("  Light deflection: "
              f"(1+gamma)/2 = {(1 + gs.mean()) / 2:.4f} x GR.")
    else:
        print(f"  gamma = {gs.mean():+.4f}: the counterterm changes "
              f"the spectrum but does")
        print("  not deliver Einstein. Recorded as measured.")
    print()
    return float(gs.mean())


if __name__ == "__main__":
    Lc = s1_lambda()
    s2_spectrum(Lc)
    s3_gamma(Lc)
    print("all assertions passed")
