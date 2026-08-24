"""0086 -- the pinned root: the filter's bias theorem is the physics'
masslessness theorem.

First stone of the homomorphism to the lucid-filter family (the user's
directive: Z_N has done its job; the minimal dynamics-corresponding
object is the filter's bias computation). Their theorem (lucid-filter
ode-filter 0041): an additive bias can only live in a characteristic
root pinned at z = 1 EXACTLY; a free ML fit lands the root at 1 +- eps
with eps = O(1/n), and because a root is an exponent, an additive climb
is rendered as geometric growth or decay -- catastrophic at horizon.
The cure is structural: factor (z-1)^d out by construction and fit
only the quotient. Right pin free (+0.0003 nats), wrong pin loud
(-0.148), never subtle.

This module verifies BOTH SIDES of the correspondence in miniature.

  s1  FILTER SIDE (their phenomenon, reproduced minimally): fit a free
      AR(2) to walk-plus-drift data; the largest root lands at 1 +- eps,
      never exactly 1, and the h = 60 forecast bias is ~5x worse than the pinned fit (difference the series =
      impose the unit root, then forecast).
  s2  PHYSICS SIDE (the mirror, exact): for ANY positive class weight,
      the trivial channel has r_0 = 1 exactly -- conservation is an
      automatic pin, the physics' d = 1. Every nontrivial channel of a
      generic weight has r_j < 1 strictly: mass is generic; a free
      measure cannot hold a nontrivial unit root, exactly as a free
      fit cannot. A nearly-symmetric weight gives r = 1 - eps: the
      channel survives only to horizon ~ 1/eps -- the same
      root-is-an-exponent catastrophe. And a CENTER-supported weight
      holds |r_j| = 1 for every j exactly: topological ('t Hooft)
      channels are pinned roots, persistent at any distance.

The dictionary row this establishes: pinned unit root <-> gauge/
budget-protected massless mode; free-fit eps-displacement <-> mass
generation by imperfectly-held symmetry (0056's massive graviton off
criticality vs 0063's massless-by-construction is the arc's own
free-vs-pinned dichotomy); 'right pin free, wrong pin loud' <-> true
constraints cost nothing, false ones move couplings by orders.
"""

import math

import numpy as np


# ----------------------------------------------------------------------
# s1 -- filter side: free fit cannot hold the root
# ----------------------------------------------------------------------

def s1_filter_side():
    print("== s1: filter side -- the free fit cannot hold the root ==")
    n, h, drift = 300, 60, 0.08
    eps_list, bias_free, bias_pin = [], [], []
    for seed in range(16):
        r = np.random.default_rng(seed)
        walk = np.cumsum(r.normal(0, 0.15, n))
        y = drift * np.arange(n) + walk + r.normal(0, 0.2, n)
        tr = y
        # expected continuation given the walk's endpoint (drift line)
        expect_end = drift * (n - 1 + h) + walk[-1]
        # free AR(2), conditional least squares
        X = np.stack([tr[1:-1], tr[:-2]], axis=1)
        Y = tr[2:]
        a = np.linalg.lstsq(X, Y, rcond=None)[0]
        roots = np.roots([1, -a[0], -a[1]])
        eps = abs(np.max(np.abs(roots)) - 1)
        eps_list.append(eps)
        # free forecast, recursive
        buf = [tr[-2], tr[-1]]
        ffree = []
        for _ in range(h):
            nxt = a[0] * buf[-1] + a[1] * buf[-2]
            buf.append(nxt)
            ffree.append(nxt)
        # pinned: impose the unit root -- model differences, forecast
        d = np.diff(tr)
        fpin = tr[-1] + np.mean(d) * np.arange(1, h + 1)
        bias_free.append(ffree[-1] - expect_end)
        bias_pin.append(fpin[-1] - expect_end)
    eps_med = float(np.median(eps_list))
    bf = float(np.mean(np.abs(bias_free)))
    bp = float(np.mean(np.abs(bias_pin)))
    print(f"  free AR(2) largest root: |root| - 1 = {eps_med:.4f} "
          f"median (never exactly 0; O(1/n))")
    print(f"  |h=60 bias|: free {bf:.2f}  vs  pinned {bp:.2f}   "
          f"(ratio {bf / bp:.1f}x)")
    assert 1e-4 < eps_med < 0.05
    assert bf > 3 * bp
    print("  the symmetry (shift equivariance) must be held by "
          "construction; estimated, it")
    print("  breaks at O(1/n) and the break is an exponent -- their "
          "0041, reproduced\n")


# ----------------------------------------------------------------------
# s2 -- physics side: the exact mirror
# ----------------------------------------------------------------------

TH = np.linspace(1e-7, np.pi - 1e-7, 200001)


def chi(j, th):
    return np.sin((2 * j + 1) * th) / np.sin(th)


def r_of(W, j):
    p = W * np.sin(TH) ** 2
    return float(np.trapezoid(p * chi(j, TH), TH)
                 / ((2 * j + 1) * np.trapezoid(p, TH)))


def s2_physics_side():
    print("== s2: physics side -- conservation pins, genericity "
          "masses, center persists ==")
    rng = np.random.default_rng(7)
    worst0, best_nontriv = 0.0, 0.0
    for _ in range(10):
        # random positive class weight
        c = rng.uniform(0.2, 1, 4)
        W = c[0] * np.exp(-0.5 * (TH - c[1]) ** 2 / c[2] ** 2) + c[3]
        worst0 = max(worst0, abs(r_of(W, 0) - 1))
        for j in (0.5, 1, 1.5, 2):
            best_nontriv = max(best_nontriv, r_of(W, j))
    print(f"  any weight: r_0 = 1 exactly (max dev {worst0:.1e}) -- "
          f"conservation is the automatic pin")
    print(f"  generic weights: largest nontrivial r = "
          f"{best_nontriv:.4f} < 1 -- mass is generic;")
    print("  a free measure cannot hold a nontrivial unit root, "
          "exactly as a free fit cannot")
    assert worst0 < 1e-9
    assert best_nontriv < 1 - 1e-4
    # nearly-symmetric weight: r = 1 - eps, horizon ~ 1/eps
    tau = 0.01
    W = np.exp(-TH ** 2 / (2 * (math.sqrt(3 * tau)) ** 2))
    r_half = r_of(W, 0.5)
    eps = 1 - r_half
    horizon = 1 / eps
    print(f"  nearly-symmetric weight: r_1/2 = 1 - {eps:.4f}; the "
          f"channel survives ~{horizon:.0f} steps --")
    print("  the root-is-an-exponent catastrophe, physics dress "
          "(0056's massive graviton)")
    # center-supported weight: support on the single center element -1
    # (a narrow bump at theta = pi): r_j -> (-1)^{2j}, so |r_j| = 1 for
    # every j -- a nontrivial exact pin. (Weight spread over BOTH
    # center elements averages the signs and kills half-integer
    # channels instead -- support on one center element is the pin.)
    s = 0.004
    Wc = np.exp(-(np.pi - TH) ** 2 / (2 * s * s))
    devs = []
    for j in (0.5, 1, 1.5, 2):
        devs.append(abs(abs(r_of(Wc, j)) - 1))
    print(f"  center-supported weight: max ||r_j| - 1| = "
          f"{max(devs):.4f} for j <= 2 -- topological")
    print("  ('t Hooft) channels are pinned roots: exact persistence "
          "at any distance\n")
    assert max(devs) < 0.02


if __name__ == "__main__":
    s1_filter_side()
    s2_physics_side()
    print("all assertions passed")
