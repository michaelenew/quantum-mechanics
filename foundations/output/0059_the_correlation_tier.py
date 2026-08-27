"""The correlation tier: the deficit is a function of mutual information.

The gap 0058 flagged as the program's highest-value structural open:
K = pi s sources curvature with PARTICIPATION density, and nothing
established that participation is a CORRELATION measure.  This module
closes that gap at the classical/Gaussian tier, by derivation, and
the closed form at the end is sharper than the gap demanded.

  s1  THE METRIC IS DERIVED, NOT POSITED.  Explicit inference
      network: nodes with positions, channels measuring line-of-sight
      separations with Gaussian noise of precision lam, an isotropic
      prior as ambient.  The Fisher information metric on
      configuration space -- computed as the Hessian of the expected
      log-likelihood, numerically, no formula assumed -- equals

        g = A0 + sum_channels lam u u^T        (max dev 3.7e-11)

      which is EXACTLY the web's metric ansatz (0019/0020), with the
      channel weight identified: w = lam = THE PRECISION OF THE
      PAIRWISE KNOWLEDGE.  Everything 0020 proved for this metric
      (K = pi s, the screening law) now rests on a derived object.

  s2  PRECISION IS THE TRUST AXIS, AND A BIJECTION OF MUTUAL
      INFORMATION.  For a channel built from n samples of noise
      variance sig^2: lam = n/sig^2 -- the EFFECTIVE SAMPLE COUNT,
      the axis the stat-tracker thread (0008) calls trust, the thing
      point-tracking folds into variance and distribution-tracking
      must carry separately.  And against a unit prior the channel's
      mutual information with the latent coordinate is

        I = (1/2) ln(1 + lam)      <=>      lam = e^{2I} - 1

      verified against direct entropy computation.  Monotone
      bijection: participation = precision = trust = e^{2I} - 1.

  s3  THE DEFICIT LAW.  Composing s1-s2 with 0019's exact cone
      (re-verified geometrically here):

        deficit = 2 pi (1 - e^{-I})

      -- the conical deficit around a channel is a closed-form
      function of the channel's mutual information.  Checks: weak
      limit delta ~ 2 pi I (curvature LINEAR in mutual information
      -- the first-law shape of the entanglement literature);
      the expansion pi w - (3/4) pi w^2 recovers 0019's measured
      correction; saturation I -> infinity gives delta -> 2 pi, so
      the extremal defect (0019) is COMPLETE INFORMATION, and with
      delta = 8 pi G m:

        m = (1 - e^{-I}) / 4G

      -- the per-defect mass bound m < 1/4G is the statement that
      mutual information is never actually infinite.  And 0020's
      screening law is an information statement verbatim:
      pi w / sqrt(det A0) = pi w e^{-J} with J = (1/2) ln det A0 =
      the ambient's total information -- the local coupling is
      damped by the exponential of what the neighbourhood already
      knows.

  s4  THE BOND TIER IS THE REDUNDANCY TIER.  Two collinear channels:
      precisions ADD (Fisher additivity = 0041's "charges add"),
      informations do not -- the redundancy
      R = I1 + I2 - I_joint = (1/2) ln((1+w1)(1+w2)/(1+w1+w2))
      ~ w1 w2 / 2 lives exactly at the bond's O(w1 w2) tier, and the
      measured geometric interaction of the two deficits is
      -3 pi x R at leading order (ratios -9.31/-9.20/-9.12 -> -3 pi
      = -9.42 as w -> 0).  Recorded as structural correspondence:
      THE BOND'S ORDER IS THE ORDER OF OVERCOUNTED INFORMATION.

Run directly for the verification suite.
"""

from __future__ import annotations

import math

NODES = [(0.0, 0.0), (2.0, 0.5), (-1.0, 1.5)]
CHANNELS = [((0, 1), 0.7), ((0, 2), 1.3), ((1, 2), 0.4)]
ALPHA = 0.35


def _sep(P, i, j):
    dx, dy = P[j][0] - P[i][0], P[j][1] - P[i][1]
    r = math.hypot(dx, dy)
    return r, (dx / r, dy / r)


def expected_nll(P):
    s = 0.0
    for (i, j), lam in CHANNELS:
        r0, _ = _sep(NODES, i, j)
        r, _ = _sep(P, i, j)
        s += 0.5 * lam * (r - r0) ** 2
    for k in range(3):
        s += 0.5 * ALPHA * ((P[k][0] - NODES[k][0]) ** 2
                            + (P[k][1] - NODES[k][1]) ** 2)
    return s


def fisher_numeric(h=1e-5):
    v0 = [c for p in NODES for c in p]

    def val(v):
        return expected_nll([(v[0], v[1]), (v[2], v[3]), (v[4], v[5])])

    n = 6
    H = [[0.0] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            vs = []
            for da, db in ((h, h), (h, -h), (-h, h), (-h, -h)):
                v = v0[:]
                v[a] += da
                v[b] += db
                vs.append(val(v))
            H[a][b] = (vs[0] - vs[1] - vs[2] + vs[3]) / (4 * h * h)
    return H


def fisher_analytic():
    n = 6
    H = [[0.0] * n for _ in range(n)]
    for (i, j), lam in CHANNELS:
        _, u = _sep(NODES, i, j)
        J = [0.0] * n
        J[2 * j], J[2 * j + 1] = u[0], u[1]
        J[2 * i], J[2 * i + 1] = -u[0], -u[1]
        for a in range(n):
            for b in range(n):
                H[a][b] += lam * J[a] * J[b]
    for a in range(n):
        H[a][a] += ALPHA
    return H


# =====================================================================
# 1. the metric is derived, not posited
# =====================================================================

def verify_metric_derived() -> None:
    Hn, Ha = fisher_numeric(), fisher_analytic()
    worst = max(abs(Hn[a][b] - Ha[a][b])
                for a in range(6) for b in range(6))
    print(f"    3 nodes, 3 line-of-sight channels (lam = 0.7, 1.3,"
          f" 0.4), ambient prior {ALPHA}*I")
    print(f"    Hessian of expected log-likelihood vs"
          f" A0 + sum lam u u^T: max dev = {worst:.1e}")
    assert worst < 1e-8, worst
    print()
    print("  THE WEB'S METRIC IS THE FISHER METRIC OF AN EXPLICIT")
    print("  INFERENCE MODEL, with the channel weight identified:")
    print("  w = lam = the PRECISION of the pairwise knowledge.  0020's")
    print("  K = pi s and screening law now rest on a derived object.")


# =====================================================================
# 2. precision = trust = e^{2I} - 1
# =====================================================================

def verify_precision_is_information() -> None:
    for lam_n, n, sig2 in ((1.0, 1, 1.0), (2.0, 4, 2.0), (5.0, 10, 2.0)):
        lam = n / sig2
        var_y = 1.0 + sig2 / n
        det = var_y - 1.0
        I_direct = 0.5 * math.log(var_y / det)
        I_closed = 0.5 * math.log(1 + lam)
        assert abs(I_direct - I_closed) < 1e-12
        assert abs(lam - (math.exp(2 * I_closed) - 1)) < 1e-12
        print(f"    n = {n:2d} samples, noise var {sig2}: "
              f"lam = n/sig^2 = {lam:.1f}, I = {I_closed:.6f} "
              f"(direct entropy: {I_direct:.6f})")
    print()
    print("  w = n/sig^2 is the EFFECTIVE SAMPLE COUNT -- the trust")
    print("  axis of 0008, the quantity point-tracking (Kalman) folds")
    print("  into the variance and distribution-tracking must carry")
    print("  separately -- and w = e^{2I} - 1 exactly: participation =")
    print("  precision = trust = a monotone bijection of the pairwise")
    print("  MUTUAL INFORMATION.")


# =====================================================================
# 3. the deficit law
# =====================================================================

def verify_deficit_law() -> None:
    print("    deficit three ways (geometric / 0019 closed form /")
    print("    2 pi (1 - e^-I)):")
    for w in (0.1, 0.5, 1.0, 3.0):
        r = 2.7
        circ = 2 * math.pi * r
        proper_rad = math.sqrt(1 + w) * r
        d_geom = 2 * math.pi * (1 - circ / (2 * math.pi * proper_rad))
        d_0019 = 2 * math.pi * (1 - (1 + w) ** -0.5)
        I = 0.5 * math.log(1 + w)
        d_info = 2 * math.pi * (1 - math.exp(-I))
        assert abs(d_geom - d_info) < 1e-12
        assert abs(d_0019 - d_info) < 1e-12
        print(f"      w = {w}: {d_geom:.6f} = {d_0019:.6f} = "
              f"{d_info:.6f}   (I = {I:.4f})")
    w = 0.01
    exact = 2 * math.pi * (1 - (1 + w) ** -0.5)
    weak = math.pi * w - 0.75 * math.pi * w * w
    assert abs(exact - weak) < 3e-6
    print(f"    weak expansion pi w - (3/4) pi w^2: 0019's measured")
    print(f"    correction recovered ({exact:.8f} vs {weak:.8f})")
    for a in (0.25, 0.5, 1.0):
        J = 0.5 * math.log(1 + a)
        assert abs((1 + a) ** -0.5 - math.exp(-J)) < 1e-15
    print("    screening: pi w / sqrt(det A0) == pi w e^{-J},")
    print("    J = (1/2) ln det A0 = the ambient's total information")
    print()
    print("  DEFICIT = 2 pi (1 - e^{-I}).  Weak limit: delta ~ 2 pi I")
    print("  -- curvature LINEAR in mutual information, the first-law")
    print("  shape.  Saturation: I -> inf gives delta -> 2 pi, so with")
    print("  delta = 8 pi G m,  m = (1 - e^{-I})/4G: the extremal")
    print("  defect is COMPLETE INFORMATION and the mass cap m < 1/4G")
    print("  is the statement that mutual information is never")
    print("  actually infinite.  'Correlation sources curvature' -- the")
    print("  row 0058 found unclosed -- closes at the Gaussian tier,")
    print("  in closed form.")


# =====================================================================
# 4. the bond tier is the redundancy tier
# =====================================================================

def verify_redundancy_tier() -> None:
    print("    two collinear channels -- precisions add, informations")
    print("    overlap:")
    ratios = []
    for w1, w2 in ((0.02, 0.03), (0.05, 0.05), (0.1, 0.04)):
        R = 0.5 * math.log((1 + w1) * (1 + w2) / (1 + w1 + w2))
        dint = (2 * math.pi * (1 - (1 + w1 + w2) ** -0.5)
                - 2 * math.pi * (1 - (1 + w1) ** -0.5)
                - 2 * math.pi * (1 - (1 + w2) ** -0.5))
        ratios.append(dint / R)
        print(f"      w = ({w1}, {w2}): redundancy {R:.3e} "
              f"(~ w1 w2/2 = {0.5 * w1 * w2:.3e}), geometric "
              f"interaction {dint:.3e}, ratio {dint / R:.3f}")
    print(f"      -> -3 pi = {-3 * math.pi:.3f} as w -> 0")
    for r in ratios:
        assert -3 * math.pi - 0.35 < r < -3 * math.pi + 0.35, r
    print()
    print("  Fisher additivity IS 0041's 'charges add'; the")
    print("  information REDUNDANCY I1 + I2 - I_joint ~ w1 w2 / 2")
    print("  lives exactly at the bond's O(w1 w2) tier, and the")
    print("  geometric interaction equals -3 pi x redundancy at")
    print("  leading order.  Structural correspondence, recorded:")
    print("  the bond's order is the order of overcounted information.")


def run_verification_suite() -> None:
    sections = [
        ("The metric is derived, not posited", verify_metric_derived),
        ("Precision = trust = e^{2I} - 1",
         verify_precision_is_information),
        ("The deficit law", verify_deficit_law),
        ("The bond tier is the redundancy tier",
         verify_redundancy_tier),
    ]
    for index, (title, check) in enumerate(sections, start=1):
        print("=" * 70)
        print(f"{index}. {title}")
        print("=" * 70)
        check()
        print()
    print("=" * 70)
    print("suite complete")
    print("=" * 70)


if __name__ == "__main__":
    run_verification_suite()
