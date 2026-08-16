"""The closed loop: the string sector joins the conserved-source law.

0047 predicted that the wiggling string's radiative Ricci admixture
(0.46-0.53 even with the tension term) was an open-end artefact --
a truncated string is not a conserved source -- and that a compact,
exactly conserved string would radiate clean vacuum waves.  This
module builds that source and confirms the prediction, then closes
the kappa residue of 0048 at its honest level.

  s1  THE EXACT LOOP.  A Kibble-Turok Nambu-Goto solution:
      x(sigma, t) = (1/2)[A(sigma - t) + B(sigma + t)] with
      A'(u) = (cos u, sin u, 0), B'(v) = (cos v, 0, sin v) -- unit
      left/right movers, closed, period 2 pi.  Conformal-gauge
      identities verified to machine precision (xdot.x' = 3e-17,
      xdot^2 + x'^2 - 1 = 2e-16): the source is EXACTLY conserved,
      with no ends to leak conservation.

  s2  THE MEASUREMENT.  The Green-function field of the exact loop
      (tensor elements xdot xdot - x' x', each at its own retarded
      time), Ricci-wave / Riemann-wave in the wave zone:
        exact loop:                  0.032 and 0.034  (two probes)
        truncated string (0047):     0.46 - 0.53
        conserved binary (0047):     0.014 - 0.042
      A 14x COLLAPSE: the string admixture was the open ends, and
      the string sector obeys the same law as the binary -- THE
      GREEN-FUNCTION FIELD IS VACUUM IFF THE SOURCE IS CONSERVED.
      The loop radiates healthily (Riemann wave 1e-2 at R = 8) as
      GR loops do; the Vachaspati traveling-wave silence is
      correctly an INFINITE-string statement -- a loop cannot carry
      a traveling-only mode, since both movers must close (B' const
      cannot be periodic with |B'| = 1).  What was once measured as
      an anomaly (0032's inverted selection rule) resolves into:
      wrong source model (no tension, open ends), not wrong field
      dynamics.

  s3  KAPPA IS A UNIT, N IS THE PHYSICS.  0048's residue #1 asked
      for kappa.  The 2+1 identification delta = 8 pi G m (0012)
      with the quantum ledger delta_q = 2 pi/N, m_q = 1/(4 G N)
      gives  8 pi G x 1/(4 G N) = 2 pi / N  IDENTICALLY: G cancels
      from the quantized theory.  G converts participation to
      deficit -- a unit choice, like c converting ticks to lengths
      (0022) -- and the only physical datum left in the coupling is
      THE LEVEL N.  The chain's "one free constant" is the rung of
      the tower, which 0029 already classified as content, not law.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_t = importlib.import_module("0030_the_time_sector")
riemann4, ETA = _t.riemann4, _t.ETA

TAU = 2 * math.pi
LAM = 0.01
NEL = 120


# =====================================================================
# the exact Nambu-Goto loop (Kibble-Turok family member)
# =====================================================================

def Af(u):
    return (math.sin(u), -math.cos(u), 0.0)


def Bf(v):
    return (math.sin(v), 0.0, -math.cos(v))


def Apf(u):
    return (math.cos(u), math.sin(u), 0.0)


def Bpf(v):
    return (math.cos(v), 0.0, math.sin(v))


def xpos(s, t):
    a, b = Af(s - t), Bf(s + t)
    return tuple(0.5 * (a[i] + b[i]) for i in range(3))


def xdot(s, t):
    ap, bp = Apf(s - t), Bpf(s + t)
    return tuple(0.5 * (-ap[i] + bp[i]) for i in range(3))


def xprm(s, t):
    ap, bp = Apf(s - t), Bpf(s + t)
    return tuple(0.5 * (ap[i] + bp[i]) for i in range(3))


def g_loop(x):
    """Green-function field of the exact loop: tensor Nambu-Goto
    elements, each at its own retarded time."""
    t = x[0]
    hbar = [[0.0] * 4 for _ in range(4)]
    ds = TAU / NEL
    for i in range(NEL):
        s = TAU * (i + 0.5) / NEL
        lo, hi = t - 12.0, t
        for _ in range(55):
            mid = 0.5 * (lo + hi)
            if (t - mid) - math.dist(x[1:], xpos(s, mid)) > 0:
                lo = mid
            else:
                hi = mid
        tr = 0.5 * (lo + hi)
        p = xpos(s, tr)
        ell0 = t - tr
        elv = (x[1] - p[0], x[2] - p[1], x[3] - p[2])
        vd = xdot(s, tr)
        vp = xprm(s, tr)
        denom = ell0 - sum(vd[k] * elv[k] for k in range(3))
        xd_l = (-1.0, vd[0], vd[1], vd[2])
        xp_l = (0.0, vp[0], vp[1], vp[2])
        for a in range(4):
            for b in range(4):
                hbar[a][b] += 4 * LAM * ds * (xd_l[a] * xd_l[b]
                                              - xp_l[a] * xp_l[b]) \
                    / denom
    trc = -hbar[0][0] + hbar[1][1] + hbar[2][2] + hbar[3][3]
    return [[ETA[i][j] + hbar[i][j] - 0.5 * ETA[i][j] * trc
             for j in range(4)] for i in range(4)]


# =====================================================================
# 1. the exact loop
# =====================================================================

def verify_exact_loop() -> None:
    worst_dot, worst_norm = 0.0, 0.0
    for i in range(24):
        s = TAU * i / 24
        for t in (0.37, 1.9):
            xd, xp = xdot(s, t), xprm(s, t)
            worst_dot = max(worst_dot,
                            abs(sum(xd[k] * xp[k] for k in range(3))))
            worst_norm = max(worst_norm,
                             abs(sum(xd[k] * xd[k] for k in range(3))
                                 + sum(xp[k] * xp[k]
                                       for k in range(3)) - 1.0))
    assert worst_dot < 1e-14 and worst_norm < 1e-14
    print(f"    Kibble-Turok loop: |xdot.x'| <= {worst_dot:.0e},")
    print(f"    |xdot^2 + x'^2 - 1| <= {worst_norm:.0e} -- exact")
    print(f"    conformal gauge, exactly conserved, no ends.")


# =====================================================================
# 2. the measurement
# =====================================================================

def loop_ratio(pt3, nph=8):
    Es, Rics = [], []
    for k in range(nph):
        t = TAU * k / nph
        Rlow, Ric = riemann4(g_loop, (t, pt3[0], pt3[1], pt3[2]),
                             h=2e-3)
        Es.append([[Rlow[0][1 + i][0][1 + j] for j in range(3)]
                   for i in range(3)])
        Rics.append(Ric)

    def amp(S, i, j):
        v = [s_[i][j] for s_ in S]
        return (max(v) - min(v)) / 2
    Eamp = max(amp(Es, i, j) for i in range(3) for j in range(3))
    ric = max(amp(Rics, i, j) for i in range(4) for j in range(4))
    return Eamp, ric / Eamp


def verify_measurement() -> None:
    for pt3 in ((0.0, 8.0, 0.0), (5.0, 5.0, 3.0)):
        Eamp, ratio = loop_ratio(pt3)
        assert ratio < 0.06, (pt3, ratio)
        assert Eamp > 1e-3, Eamp
        print(f"    probe {pt3}: Riemann wave {Eamp:.2e},  "
              f"Ricci/Riemann {ratio:.3f}")
    print("    (truncated open string, 0047: 0.46-0.53;")
    print("     conserved binary, 0047: 0.014-0.042)")
    print()
    print("  A 14x COLLAPSE: the string admixture was the open")
    print("  ends.  The string sector obeys the same law as the")
    print("  binary -- the Green-function field is vacuum iff the")
    print("  source is conserved.  The loop radiates healthily, as")
    print("  GR loops do; Vachaspati's traveling-wave silence is")
    print("  correctly an INFINITE-string statement (a loop cannot")
    print("  carry a traveling-only mode: both movers must close).")
    print("  0032's 'inverted selection rule' resolves: wrong source")
    print("  model, not wrong field dynamics.")


# =====================================================================
# 3. kappa is a unit, N is the physics
# =====================================================================

def verify_kappa() -> None:
    for N in (2, 3, 5, 8):
        for G in (1.0, 0.37, 6.674e-11):
            delta_q = 8 * math.pi * G * (1 / (4 * G * N))
            assert abs(delta_q - TAU / N) < 1e-12 * TAU / N
    print("    8 pi G x m_q = 8 pi G/(4 G N) = 2 pi/N identically,")
    print("    for every G and N.")
    print()
    print("  G CANCELS FROM THE QUANTIZED LEDGER: it is the")
    print("  participation -> deficit conversion unit (as c is the")
    print("  tick -> length unit, 0022).  The coupling's only")
    print("  physical datum is THE LEVEL N -- which 0029 classified")
    print("  as the world's content, not the law.  0048's residue")
    print("  #1 closes at its honest level: kappa was a unit.")


def run_verification_suite() -> None:
    sections = [
        ("The exact loop", verify_exact_loop),
        ("The measurement", verify_measurement),
        ("Kappa is a unit, N is the physics", verify_kappa),
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
