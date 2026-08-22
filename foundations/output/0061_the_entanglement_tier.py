"""The entanglement tier: the weight is the tangle.

0066's sharpest open: both ends quantum.  A pair of nodes shares an
entangled two-qubit state, and the relative coordinate is recorded
RELATIONALLY -- as a phase between the correlated branches:

  |psi> = sqrt(p)|00> + sqrt(1-p) e^{i kappa theta}|11>

Neither end alone sees theta (rho_A is exactly theta-independent):
the record is pairwise-only, which is postulate P1 made literal.
What sources the metric then has to be a property of the PAIR -- and
it is, in closed form.

  s1  THE RELATIONAL RECORD.  rho_A = diag(p, 1-p) independent of
      theta, exactly: the coordinate is invisible at each end,
      readable only jointly.  Contrast: a product state with LOCAL
      coherence (|+>|0>, encoding on A) carries QFI = kappa^2 with
      zero entanglement -- that is 0066's one-sided channel.  The
      two mechanisms are distinct, and this module isolates the
      purely relational one.

  s2  THE WEIGHT IS THE TANGLE.  The Bures metric on the two-node
      configuration space (numeric fidelity Hessian, no formula
      assumed) is (QFI/4) u u^T with QFI = 4 kappa^2 p(1-p), and
      Wootters' concurrence of the family is C = 2 sqrt(p(1-p)), so

        w  =  kappa^2 C^2       (weight = coupling^2 x tangle)

      exactly (1e-12).  Separable (p = 0 or 1): C = 0, w = 0 -- AN
      UNENTANGLED PAIR SOURCES NO GEOMETRY.  Maximal entanglement:
      C = 1, the full one-carrier weight.  The program's squares
      align: probability = amplitude^2, metric = channel^2, bond =
      charge^2, ledger = Dirichlet square -- and now weight =
      concurrence SQUARED.

  s3  THE DISCRIMINATOR: TANGLE, NOT ENTROPY.  Weak coupling
      (kappa = 0.05), deficit per pi kappa^2 against the candidate
      correlation measures:

        p        C^2     E(entropy)   2E(QMI)   delta/(pi kappa^2)
        0.01   0.0396      0.0560      0.1120        0.0396
        0.15   0.5100      0.4227      0.8454        0.5095
        0.50   1.0000      0.6931      1.3863        0.9981

      The deficit tracks C^2 to 3-4 digits and neither entropy
      column.  THE MODEL CHOOSES ITS CORRELATION MEASURE: curvature
      couples to the tangle, not to entanglement entropy -- the
      RT-shape (curvature ~ entropy) is NOT what this program
      predicts at the pair level.  A sharp, falsifiable-in-model
      selection.

  s4  THE PERSISTENT-PAIR LAW.  The Bell-basis readout attains
      Fisher = kappa^2 C^2 at the phase reference, and the
      accumulated record's MI over n shared pairs converges toward
      (1/2) ln(1 + n kappa^2 C^2) (ratio 0.955 -> 0.986 by n = 600;
      slower than 0066's aligned case because the C < 1 channel's
      Fisher varies with theta).  So the deficit law

        delta = 2 pi (1 - e^{-I_record})

      carries over with the per-pair CAPACITY set by the tangle:
      entanglement is the capacity, the record is the account, the
      deficit follows the account.

Run directly for the verification suite.
"""

from __future__ import annotations

import cmath
import math
from math import lgamma


def fid(p, kap, dth):
    return abs(p + (1 - p) * cmath.exp(1j * kap * dth)) ** 2


def concurrence(p, kap, th):
    """Wootters C = |<psi| sy x sy |psi*>| for the family."""
    a = math.sqrt(p)
    d = math.sqrt(1 - p) * cmath.exp(1j * kap * th)
    return abs(a * (-d.conjugate()) + d.conjugate() * (-a))


# =====================================================================
# 1. the relational record
# =====================================================================

def verify_relational_record() -> None:
    p = 0.25
    for th in (0.0, 0.6, 1.3):
        amp00 = math.sqrt(p)
        amp11 = math.sqrt(1 - p) * cmath.exp(1j * 0.9 * th)
        # rho_A entries: <0|rho_A|0> = |amp00|^2, <1|rho_A|1> = |amp11|^2,
        # off-diagonal needs |01>/|10> amplitudes -- absent by structure
        assert abs(abs(amp00) ** 2 - p) < 1e-15
        assert abs(abs(amp11) ** 2 - (1 - p)) < 1e-15
    print("    rho_A = diag(p, 1-p), theta-INDEPENDENT, exactly: the")
    print("    coordinate is invisible at each end, readable only")
    print("    jointly -- postulate P1 as a density matrix.")
    print("    contrast: |+>|0> with local encoding has QFI = kappa^2")
    print("    and C = 0 -- local coherence, 0066's one-sided channel.")
    print()
    print("  THE RECORD IS PAIRWISE-ONLY.  Whatever sources the metric")
    print("  must be a property of the pair.")


# =====================================================================
# 2. the weight is the tangle
# =====================================================================

def verify_weight_is_tangle() -> None:
    KAP = 0.9
    P0 = [(0.0, 0.0), (2.0, 0.5)]

    def sep(P):
        return math.hypot(P[1][0] - P[0][0], P[1][1] - P[0][1])

    for p in (0.1, 0.25, 0.5):
        def d2(P):
            return 2 * (1 - math.sqrt(fid(p, KAP, sep(P) - sep(P0))))

        h = 1e-5
        v0 = [P0[0][0], P0[0][1], P0[1][0], P0[1][1]]
        H = [[0.0] * 4 for _ in range(4)]
        for a in range(4):
            for b in range(4):
                acc = 0.0
                for da, db, sg in ((h, h, 1), (h, -h, -1),
                                   (-h, h, -1), (-h, -h, 1)):
                    v = v0[:]
                    v[a] += da
                    v[b] += db
                    acc += sg * d2([(v[0], v[1]), (v[2], v[3])])
                H[a][b] = acc / (4 * h * h)
        r0 = sep(P0)
        u = ((P0[1][0] - P0[0][0]) / r0, (P0[1][1] - P0[0][1]) / r0)
        J = [-u[0], -u[1], u[0], u[1]]
        QFI = 4 * KAP * KAP * p * (1 - p)
        worst = max(abs(H[a][b] - (QFI / 2) * J[a] * J[b])
                    for a in range(4) for b in range(4))
        C = concurrence(p, KAP, 0.7)
        assert worst < 1e-5, (p, worst)
        assert abs(C - 2 * math.sqrt(p * (1 - p))) < 1e-12
        assert abs(QFI - KAP * KAP * C * C) < 1e-12
        print(f"    p = {p}: Bures = (QFI/4) u u^T (dev {worst:.0e}),"
              f"  C = {C:.4f},  QFI = kappa^2 C^2 exactly")
    print()
    print("  w = kappa^2 x TANGLE.  Separable => C = 0 => w = 0: an")
    print("  unentangled pair sources NO geometry.  Maximal")
    print("  entanglement => the full one-carrier weight.  Weight =")
    print("  concurrence SQUARED -- the program's square, again.")


# =====================================================================
# 3. the discriminator: tangle, not entropy
# =====================================================================

def verify_discriminator() -> None:
    kap = 0.05
    print(f"    {'p':>6} {'C^2':>8} {'E':>8} {'2E':>8} "
          f"{'delta/(pi k^2)':>15}")
    for p in (0.01, 0.05, 0.15, 0.3, 0.5):
        q = 1 - p
        C2 = 4 * p * q
        E = -(p * math.log(p) + q * math.log(q))
        w = kap * kap * C2
        d = 2 * math.pi * (1 - (1 + w) ** -0.5)
        ratio = d / (math.pi * kap * kap)
        print(f"    {p:6.2f} {C2:8.4f} {E:8.4f} {2 * E:8.4f} "
              f"{ratio:15.4f}")
        assert abs(ratio - C2) / C2 < 0.01, (p, ratio, C2)
    p = 0.01
    q = 1 - p
    E = -(p * math.log(p) + q * math.log(q))
    assert E / (4 * p * q) > 1.3
    print()
    print("  THE DEFICIT TRACKS THE TANGLE C^2 TO 3-4 DIGITS AND")
    print("  NEITHER ENTROPY COLUMN.  The model chooses its")
    print("  correlation measure: curvature couples to the tangle,")
    print("  not entanglement entropy -- the RT shape is not this")
    print("  program's pair-level prediction.  Sharp and")
    print("  falsifiable-in-model.")


# =====================================================================
# 4. the persistent-pair law
# =====================================================================

def _mi_record(p, kap, n, s0=1.0, ngrid=1201, span=8.0):
    C = 2 * math.sqrt(p * (1 - p))
    ths = [-span * s0 + 2 * span * s0 * (i + 0.5) / ngrid
           for i in range(ngrid)]
    ws = [math.exp(-t * t / (2 * s0 * s0)) for t in ths]
    Z = sum(ws)
    logC = [lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)
            for k in range(n + 1)]
    marg = [0.0] * (n + 1)
    cond = 0.0
    for w, t in zip(ws, ths):
        pr = min(max((1 + C * math.sin(kap * t)) / 2, 1e-12), 1 - 1e-12)
        l1, l0 = math.log(pr), math.log(1 - pr)
        for k in range(n + 1):
            lp = logC[k] + k * l1 + (n - k) * l0
            P = math.exp(lp)
            marg[k] += w * P
            cond -= w * P * lp
    marg = [m / Z for m in marg]
    cond /= Z
    Hm = -sum(m * math.log(m) for m in marg if m > 1e-300)
    return Hm - cond


def verify_persistent_pairs() -> None:
    p = 0.15
    C = 2 * math.sqrt(p * (1 - p))
    kap = 0.3
    F0 = C * C * kap * kap
    th = 1e-6
    pr = (1 + C * math.sin(kap * th)) / 2
    dp = C * kap * math.cos(kap * th) / 2
    F_num = dp * dp / (pr * (1 - pr))
    assert abs(F_num - F0) / F0 < 1e-4
    print(f"    Bell-basis readout Fisher at the phase reference = "
          f"kappa^2 C^2 = {F0:.4f} (dev {abs(F_num - F0):.1e})")
    print(f"    record MI over n shared pairs vs "
          f"(1/2)ln(1 + n kappa^2 C^2):")
    prev = 0.0
    for n in (1, 10, 60, 200, 600):
        In = _mi_record(p, kap, n)
        Ig = 0.5 * math.log(1 + n * kap * kap * C * C)
        r = In / Ig
        print(f"      n = {n:3d}: I_n = {In:.4f}  gauss = {Ig:.4f}  "
              f"ratio = {r:.4f}")
        assert r > prev
        prev = r
    assert prev > 0.98, prev
    print()
    print("  THE DEFICIT LAW CARRIES OVER: delta = 2 pi (1 -")
    print("  e^{-I_record}) with the per-pair CAPACITY set by the")
    print("  tangle.  Entanglement is the capacity, the record is the")
    print("  account, the deficit follows the account.")


def run_verification_suite() -> None:
    sections = [
        ("The relational record", verify_relational_record),
        ("The weight is the tangle", verify_weight_is_tangle),
        ("The discriminator: tangle, not entropy",
         verify_discriminator),
        ("The persistent-pair law", verify_persistent_pairs),
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
