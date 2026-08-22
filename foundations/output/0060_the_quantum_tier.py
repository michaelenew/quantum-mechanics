"""The quantum tier: the deficit law survives, and where it splits.

0065 closed "correlation sources curvature" at the Gaussian tier:
w = precision = e^{2I} - 1 and deficit = 2 pi (1 - e^{-I}).  This
module lifts the channel's CARRIER to a quantum system -- a qubit
recording the relative coordinate as a rotation -- and asks which
pieces survive.  Fisher becomes Bures, precision becomes quantum
Fisher information, and the single classical "information" splits
into a tower.  The law survives in two regimes and splits, sharply
and instructively, in the third.

  s1  THE METRIC DERIVATION SURVIVES QUANTIZATION.  For a network
      whose channels write kappa x (line-of-sight separation) into
      qubit rotations, the BURES metric on configuration space --
      computed numerically from fidelity, no formula assumed -- is

        g_B = (QFI/4) u u^T   per channel,   additive over channels

      (max dev 8e-7; additivity exact for product carriers).  And
      fidelity IS |amplitude|^2: the quantum metric tier is built on
      the ledger's own rule.  The weight identification survives:
      w_Q = QFI, the quantum precision.

  s2  THE WEIGHT IS ATTAINABLE.  The sigma_x measurement has
      classical Fisher = QFI = kappa^2 at EVERY theta (machine
      precision): w_Q is operationally the precision of the best
      readout, not an abstract bound.  At weak coupling the induced
      record's mutual information matches the classical law
      (1/2) ln(1 + QFI) to 0.3%: the Gaussian tier is the weak limit
      of the quantum tier.

  s3  THE BIJECTION SPLITS INTO A TOWER.  Classically w and I
      determine each other.  Quantum-mechanically, at strong
      coupling:

        I_meas  <=  chi (Holevo)  <=  ln d      while QFI -> infinity

      Measured (kappa = 0.1 ... 30): the classical-law value
      (1/2)ln(1+QFI) grows without bound (3.40 at kappa = 30) while
      chi saturates at ln 2 = 0.693 and the sigma_x record at 0.307.
      A single qubit's EXTRACTABLE CORRELATION is capped by its
      dimension; its DISTINGUISHABILITY (QFI) is not.  The two
      things the classical tier merged -- trust and correlation --
      come apart exactly where quantum mechanics begins.

  s4  THE DEFICIT LAW: TWO SURVIVALS AND ONE SPLIT.
      (i) Weak coupling: delta = 2 pi (1 - e^{-I}) holds with all
          measures coinciding (0.3% at kappa = 0.3).
      (ii) Persistent channels (n uses, wrap-free): the record's MI
          converges to (1/2) ln(1 + n QFI) -- ratio 0.9973 -> 1.0000
          by n = 600 -- so the law holds with I = the accumulated
          record's mutual information.  The web's channels are
          persistent; THIS is the physical regime, and there the
          quantum tier changes nothing.
      (iii) A single strong carrier: geometry follows QFI
          (delta -> 2 pi) while the information law is capped at

            delta_info <= 2 pi (1 - e^{-ln d}) = 2 pi (1 - 1/d)

          -- for a qubit, EXACTLY pi: one maximally-informative
          qubit can close at most HALF the circle by correlation
          accounting, while its distinguishability can close nearly
          all of it.  Mass reading: m = (1 - e^{-I})/4G becomes a
          DISTINGUISHABILITY bound at the quantum tier -- a defect
          approaching the extremal mass 1/4G requires unboundedly
          many carriers (or unbounded dimension), not just
          unboundedly strong correlation.

  Also recorded: postulate 0005's "Petz uniqueness fixes the quantum
  metric" needs a caveat -- Petz classifies a FAMILY of monotone
  metrics on mixed states; uniqueness holds on pure states (all
  coincide with Fubini-Study) and by the Cramer-Rao selection of
  Bures.  The channel families here are pure-state, so downstream
  results are safe.

Run directly for the verification suite.
"""

from __future__ import annotations

import math
from math import lgamma

LN2 = math.log(2)


# =====================================================================
# 1. the metric derivation survives quantization
# =====================================================================

def _qubit(a):
    return (math.cos(a), math.sin(a))


def _fid1(a, b):
    s, t = _qubit(a), _qubit(b)
    return (s[0] * t[0] + s[1] * t[1]) ** 2


def verify_bures_metric() -> None:
    kappa = 0.8
    P0 = [(0.0, 0.0), (2.0, 0.5), (-1.0, 1.5)]
    chans = [((0, 1), 0.8), ((0, 2), 1.1)]

    def angles(P):
        out = []
        for (i, j), kap in chans:
            r = math.hypot(P[j][0] - P[i][0], P[j][1] - P[i][1])
            out.append(kap * r / 2)
        return out

    def d2(P):
        F = 1.0
        for a, a0 in zip(angles(P), angles(P0)):
            F *= _fid1(a, a0)
        return 2 * (1 - math.sqrt(max(F, 0.0)))

    h = 1e-5
    v0 = [c for p in P0 for c in p]
    n = 6
    H = [[0.0] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            acc = 0.0
            for da, db, sg in ((h, h, 1), (h, -h, -1),
                               (-h, h, -1), (-h, -h, 1)):
                v = v0[:]
                v[a] += da
                v[b] += db
                acc += sg * d2([(v[0], v[1]), (v[2], v[3]),
                                (v[4], v[5])])
            H[a][b] = acc / (4 * h * h)
    pred = [[0.0] * n for _ in range(n)]
    for (i, j), kap in chans:
        r = math.hypot(P0[j][0] - P0[i][0], P0[j][1] - P0[i][1])
        u = ((P0[j][0] - P0[i][0]) / r, (P0[j][1] - P0[i][1]) / r)
        J = [0.0] * n
        J[2 * j], J[2 * j + 1] = u[0], u[1]
        J[2 * i], J[2 * i + 1] = -u[0], -u[1]
        for a in range(n):
            for b in range(n):
                # Hessian of d_B^2 = 2 g_B = (QFI/2) J J^T
                pred[a][b] += (kap ** 2 / 2) * J[a] * J[b]
    worst = max(abs(H[a][b] - pred[a][b])
                for a in range(n) for b in range(n))
    print(f"    two qubit channels (kappa = 0.8, 1.1), product carrier:")
    print(f"    Bures Hessian vs sum (QFI/4) u u^T blocks: "
          f"max dev = {worst:.1e}")
    assert worst < 1e-5, worst
    print()
    print("  THE METRIC DERIVATION SURVIVES: Bures = (QFI/4) u u^T per")
    print("  channel, additive over independent carriers -- and Bures")
    print("  is built from fidelity = |amplitude|^2, the ledger's own")
    print("  rule.  w_Q = QFI: precision survives quantization.")


# =====================================================================
# 2. the weight is attainable
# =====================================================================

def _mi_single(kap, s0=1.0, ngrid=20001, span=8.0):
    tot = [0.0, 0.0]
    cond = 0.0
    Z = 0.0
    for i in range(ngrid):
        th = -span * s0 + 2 * span * s0 * (i + 0.5) / ngrid
        w = math.exp(-th * th / (2 * s0 * s0))
        p = (1 + math.sin(kap * th)) / 2
        Z += w
        tot[0] += w * p
        tot[1] += w * (1 - p)
        for q in (p, 1 - p):
            if q > 1e-300:
                cond -= w * q * math.log(q)
    tot = [x / Z for x in tot]
    cond /= Z
    return (-sum(q * math.log(q) for q in tot if q > 0)) - cond


def verify_weight_attainable() -> None:
    kap = 0.8
    devs = []
    for th in (-1.2, -0.3, 0.0, 0.5, 1.4):
        p = (1 + math.sin(kap * th)) / 2
        dp = kap * math.cos(kap * th) / 2
        devs.append(abs(dp * dp / (p * (1 - p)) - kap ** 2))
    print(f"    sigma_x readout: classical Fisher = QFI = kappa^2 at")
    print(f"    every theta (max dev {max(devs):.1e})")
    assert max(devs) < 1e-12
    for kap in (0.1, 0.3):
        I1 = _mi_single(kap)
        Icl = 0.5 * math.log(1 + kap * kap)
        print(f"    weak coupling kappa = {kap}: I_record = {I1:.5f}, "
              f"classical law = {Icl:.5f}, ratio {I1 / Icl:.4f}")
        assert abs(I1 / Icl - 1) < 0.005
    print()
    print("  w_Q IS THE PRECISION OF THE BEST READOUT, and at weak")
    print("  coupling the record's MI matches the classical law: the")
    print("  Gaussian tier is the weak limit of the quantum tier.")


# =====================================================================
# 3. the bijection splits into a tower
# =====================================================================

def _holevo(kap, s0=1.0):
    c = math.exp(-kap * kap * s0 * s0 / 2)
    lam = [(1 + c) / 2, (1 - c) / 2]
    return -sum(x * math.log(x) for x in lam if x > 1e-300)


def verify_tower() -> None:
    print("    kappa    I_record   chi(Holevo)   classical law   ln 2")
    vals = {}
    for kap in (0.1, 1.0, 3.0, 10.0, 30.0):
        I1 = _mi_single(kap)
        chi = _holevo(kap)
        Icl = 0.5 * math.log(1 + kap * kap)
        vals[kap] = (I1, chi, Icl)
        print(f"    {kap:5.1f}   {I1:8.4f}   {chi:8.4f}      "
              f"{Icl:8.4f}      {LN2:.4f}")
        assert I1 <= chi + 1e-9 and chi <= LN2 + 1e-9
    assert abs(vals[30.0][1] - LN2) < 1e-6
    assert vals[30.0][2] > 3.0
    assert abs(vals[30.0][0] - vals[10.0][0]) < 1e-3
    print()
    print("  THE TOWER: I_record <= chi <= ln 2, all saturating, while")
    print("  the classical-law value (1/2)ln(1+QFI) grows without")
    print("  bound.  A single qubit's extractable correlation is")
    print("  capped by its dimension; its distinguishability is not.")
    print("  Trust and correlation -- merged at the classical tier --")
    print("  come apart exactly where quantum mechanics begins.")


# =====================================================================
# 4. the deficit law: two survivals and one split
# =====================================================================

def _mi_record(kap, n, s0=1.0, ngrid=1201, span=8.0):
    ths = [-span * s0 + 2 * span * s0 * (i + 0.5) / ngrid
           for i in range(ngrid)]
    ws = [math.exp(-t * t / (2 * s0 * s0)) for t in ths]
    Z = sum(ws)
    logC = [lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)
            for k in range(n + 1)]
    marg = [0.0] * (n + 1)
    cond = 0.0
    for w, t in zip(ws, ths):
        p = min(max((1 + math.sin(kap * t)) / 2, 1e-12), 1 - 1e-12)
        l1, l0 = math.log(p), math.log(1 - p)
        for k in range(n + 1):
            lp = logC[k] + k * l1 + (n - k) * l0
            P = math.exp(lp)
            marg[k] += w * P
            cond -= w * P * lp
    marg = [m / Z for m in marg]
    cond /= Z
    Hm = -sum(m * math.log(m) for m in marg if m > 1e-300)
    return Hm - cond


def verify_deficit_regimes() -> None:
    print("    (ii) persistent channel, wrap-free (kappa = 0.3):")
    last = None
    for n in (1, 10, 60, 200, 600):
        In = _mi_record(0.3, n)
        Ig = 0.5 * math.log(1 + n * 0.09)
        last = In / Ig
        print(f"       n = {n:3d}: I_n = {In:.4f}  "
              f"(1/2)ln(1+n QFI) = {Ig:.4f}  ratio {In / Ig:.4f}")
    assert last > 0.999, last
    print("       -> the deficit law delta = 2 pi (1 - e^{-I}) holds")
    print("          with I = the accumulated record's MI")
    print()
    print("    (iii) single strong carrier:")
    for kap in (3.0, 10.0):
        w = kap * kap
        d_geom = 2 * math.pi * (1 - (1 + w) ** -0.5)
        d_chi = 2 * math.pi * (1 - math.exp(-_holevo(kap)))
        print(f"       kappa = {kap:4.1f}: delta_QFI = {d_geom:.4f},  "
              f"info law cap 2 pi(1 - e^-chi) = {d_chi:.4f}")
        assert d_chi <= math.pi + 1e-3
    assert 2 * math.pi * (1 - (1 + 100) ** -0.5) > 5.6
    print(f"       cap = 2 pi (1 - 1/d) = pi = {math.pi:.4f} for d = 2")
    print()
    print("  GEOMETRY FOLLOWS DISTINGUISHABILITY; the information law")
    print("  caps at 2 pi (1 - 1/d).  One maximally-informative qubit")
    print("  can close at most HALF the circle by correlation")
    print("  accounting.  Mass reading: m -> 1/4G requires unboundedly")
    print("  many carriers or unbounded dimension -- at the quantum")
    print("  tier the mass cap is a DISTINGUISHABILITY bound, not a")
    print("  correlation bound.")


def run_verification_suite() -> None:
    sections = [
        ("The metric derivation survives quantization",
         verify_bures_metric),
        ("The weight is attainable", verify_weight_attainable),
        ("The bijection splits into a tower", verify_tower),
        ("The deficit law: two survivals and one split",
         verify_deficit_regimes),
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
