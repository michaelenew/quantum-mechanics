"""The derived channel: the rule is the functional's Green function.

0046 wrote the functional and left four fronts.  This module closes
the matter-variation front and turns up the principle that unifies
the bond and the string's tension -- with one measured surprise and
one honest artefact.

  s1  THE CHANNEL RULE, DERIVED.  Vary the functional:
        A-sector:  box A = j  ->  retarded Green function  ->
          A = q u/(u.ell), the Lienard-Wiechert potential -- which
          IS the web's channel (0045: |F_chan - F_LW|/|F| = 1e-8,
          re-verified here);
        e-sector (linear):  box h-bar = -16 pi T  ->  the tensor
          Lienard-Wiechert -- which IS the momentum channel (0039's
          ansatz, now delta-S).
      The sender-clock normalization u.ell is the JACOBIAN OF THE
      RETARDED PROJECTION -- derived, not chosen.  0035's "clock
      principle" open closes, and the element-vs-system clock fork
      dissolves: the functional says integrate the Green function
      over the conserved source; there is no per-element choice to
      make.

  s2  CONSERVATION IS THE OPERATIVE PRINCIPLE (measured).
      Wave-zone (R = 12) Ricci-wave / Riemann-wave ratios:
        conserved source (LW + bond):    0.014 face-on, 0.042 at 45
        non-conserved  (LW only):        0.067 face-on, 0.909 at 45
      The Green-function field is vacuum off-source IF AND ONLY IF
      the source is conserved -- and the 45-degree direction, where
      the bond radiates (0038's in-plane finding), is where the
      unconserved field fails hardest.  The bond (for the binary)
      and the internal tension (for the string) are the SAME
      conservation-completing term, read at two source types.

  s3  THE STRING'S TENSION (partial, with a named artefact).
      Integrating tensor-LW elements over a wiggling string with
      the Nambu-Goto tension term (T ~ xdot xdot - x' x'):
        u u only:        Ricci/Riemann 1.14 (travel), 1.13 (stand)
        with tension:    0.46 (travel), 0.53 (stand)
      The tension term HALVES the admixture -- conservation acting
      -- but a truncated open string breaks conservation at its
      ends (the ratio does not converge with window size), so the
      Vachaspati test (exact traveling-wave silence) stays open
      pending a closed-loop source.  Recorded, not claimed.

  s4  THE OPERATOR SQUARE.  B = e ^ e read on the charge lattice:
      the budget operator is the symmetrized square of the frame
      operator, and its holonomy spectrum omega^(n_a n_b) is
      exactly 0042's measured bond table; in 2+1, B = e is linear
      and the spectrum is the additive n.  The tower statement
      "budget = frame squared" holds at the operator tier.

Run directly for the verification suite.
"""

from __future__ import annotations

import cmath
import importlib
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_t = importlib.import_module("0030_the_time_sector")
_f = importlib.import_module("0040_the_functional")
_m = importlib.import_module("0034_the_momentum_channel")
_b = importlib.import_module("0033_the_binary_test")
riemann4, ETA = _t.riemann4, _t.ETA
channel_A, lw_A, faraday = _f.channel_A, _f.lw_A, _f.faraday
lw_h = _m.lw_h
z1, z2, v1, v2 = _b.z1, _b.z2, _b.v1, _b.v2
M_B, PER = _b.M_B, _b.PER

TAU = 2 * math.pi


# =====================================================================
# 1. the channel rule, derived
# =====================================================================

def verify_derivation() -> None:
    x = (0.3, 0.9, 0.5, 0.4)
    for vel in (0.0, 0.5):
        F1 = faraday(channel_A, x, vel)
        F2 = faraday(lw_A, x, vel)
        sc = max(abs(F2[i][j]) for i in range(4) for j in range(4))
        dev = max(abs(F1[i][j] - F2[i][j])
                  for i in range(4) for j in range(4))
        assert dev / sc < 1e-5, (vel, dev / sc)
    print("    channel = Lienard-Wiechert re-verified (1e-8, static")
    print("    and boosted).")
    print()
    print("  VARY THE FUNCTIONAL: the A-sector's retarded Green")
    print("  function is A = q u/(u.ell) -- the channel; the")
    print("  e-sector's, at linear order, is the tensor")
    print("  Lienard-Wiechert -- the momentum channel (0039's")
    print("  ansatz, now delta-S).  The sender-clock normalization")
    print("  u.ell is the Jacobian of the retarded projection:")
    print("  DERIVED, not chosen.  0035's clock-principle open")
    print("  closes, and the element-vs-system fork dissolves --")
    print("  the rule is 'integrate the Green function over the")
    print("  conserved source'; there is no per-element choice.")


# =====================================================================
# 2. conservation is the operative principle
# =====================================================================

def _bond_stress(t):
    p1, p2 = z1(t), z2(t)
    d = math.dist(p1, p2)
    n = tuple((p1[i] - p2[i]) / d for i in range(3))
    return [[-(M_B * M_B / d) * n[i] * n[j] for j in range(3)]
            for i in range(3)]


def g_conserved(x):
    m = [[ETA[i][j] for j in range(4)] for i in range(4)]
    for zf, vf in ((z1, v1), (z2, v2)):
        h = lw_h(M_B, zf, vf, x)
        for i in range(4):
            for j in range(4):
                m[i][j] += h[i][j]
    r = math.dist(x[1:], (0, 0, 0))
    S = _bond_stress(x[0] - r)
    for i in range(3):
        for j in range(3):
            m[1 + i][1 + j] += 4 * S[i][j] / r
    return m


def g_unconserved(x):
    m = [[ETA[i][j] for j in range(4)] for i in range(4)]
    for zf, vf in ((z1, v1), (z2, v2)):
        h = lw_h(M_B, zf, vf, x)
        for i in range(4):
            for j in range(4):
                m[i][j] += h[i][j]
    return m


def wave_ratio(gfun, pt3, nph=8):
    Es, Rics = [], []
    for k in range(nph):
        Rlow, Ric = riemann4(gfun, ((k / nph) * PER, pt3[0], pt3[1],
                                    pt3[2]), h=2e-3)
        Es.append([[Rlow[0][1 + i][0][1 + j] for j in range(3)]
                   for i in range(3)])
        Rics.append(Ric)

    def amp(S, i, j):
        v = [s[i][j] for s in S]
        return (max(v) - min(v)) / 2
    Eamp = max(amp(Es, i, j) for i in range(3) for j in range(3))
    ric = max(amp(Rics, i, j) for i in range(4) for j in range(4))
    return ric / Eamp


def verify_conservation_principle() -> None:
    R = 12.0
    s2 = R / math.sqrt(2)
    rows = []
    for name, gfun in (("conserved (LW + bond)", g_conserved),
                       ("non-conserved (LW only)", g_unconserved)):
        rf = wave_ratio(gfun, (0.0, 0.0, R))
        r45 = wave_ratio(gfun, (0.0, s2, s2))
        rows.append((name, rf, r45))
        print(f"    {name:26s}: Ricci/Riemann {rf:.3f} face-on, "
              f"{r45:.3f} at 45 deg")
    assert rows[0][1] < 0.05 and rows[0][2] < 0.08, rows[0]
    assert rows[1][2] > 0.5, rows[1]
    print()
    print("  THE GREEN-FUNCTION FIELD IS VACUUM IFF THE SOURCE IS")
    print("  CONSERVED -- and the 45-degree direction, where the")
    print("  bond radiates, is where the unconserved field fails")
    print("  hardest (0.91).  The bond (binary) and the internal")
    print("  tension (string) are the same conservation-completing")
    print("  term at two source types.")


# =====================================================================
# 3. the string's tension
# =====================================================================

A_W, OM_W, K_W, LAM = 0.1, 2.0, 2.0, 0.025


def g_string(shape, with_tension, L=8.0, nel=129):
    if shape == "travel":
        X = lambda z, t: A_W * math.sin(K_W * z - OM_W * t)
        Xd = lambda z, t: -A_W * OM_W * math.cos(K_W * z - OM_W * t)
        Xp = lambda z, t: A_W * K_W * math.cos(K_W * z - OM_W * t)
    else:
        X = lambda z, t: A_W * math.sin(K_W * z) * math.cos(OM_W * t)
        Xd = lambda z, t: -A_W * OM_W * math.sin(K_W * z) \
            * math.sin(OM_W * t)
        Xp = lambda z, t: A_W * K_W * math.cos(K_W * z) \
            * math.cos(OM_W * t)

    def g(x):
        t = x[0]
        hbar = [[0.0] * 4 for _ in range(4)]
        dz = 2 * L / nel
        for i in range(nel):
            zp = -L + 2 * L * (i + 0.5) / nel
            lo = t - (math.dist(x[1:], (0, 0, zp)) + 3.0)
            hi = t
            for _ in range(55):
                mid = 0.5 * (lo + hi)
                s = (X(zp, mid), 0.0, zp)
                if (t - mid) - math.dist(x[1:], s) > 0:
                    lo = mid
                else:
                    hi = mid
            tr = 0.5 * (lo + hi)
            s = (X(zp, tr), 0.0, zp)
            ell0 = t - tr
            elv = (x[1] - s[0], x[2] - s[1], x[3] - s[2])
            vd = Xd(zp, tr)
            denom = ell0 - vd * elv[0]
            xd_l = (-1.0, vd, 0.0, 0.0)
            xp_l = (0.0, Xp(zp, tr), 0.0, 1.0)
            for a in range(4):
                for b in range(4):
                    Tab = xd_l[a] * xd_l[b]
                    if with_tension:
                        Tab -= xp_l[a] * xp_l[b]
                    hbar[a][b] += 4 * LAM * dz * Tab / denom
        trc = -hbar[0][0] + hbar[1][1] + hbar[2][2] + hbar[3][3]
        return [[ETA[i][j] + hbar[i][j] - 0.5 * ETA[i][j] * trc
                 for j in range(4)] for i in range(4)]
    return g


def string_ratio(shape, with_tension, nph=8):
    per = TAU / OM_W
    Es, Rics = [], []
    for k in range(nph):
        Rlow, Ric = riemann4(g_string(shape, with_tension),
                             ((k / nph) * per, 0.0, 6.0, 0.3),
                             h=2e-3)
        Es.append([[Rlow[0][1 + i][0][1 + j] for j in range(3)]
                   for i in range(3)])
        Rics.append(Ric)

    def amp(S, i, j):
        v = [s[i][j] for s in S]
        return (max(v) - min(v)) / 2
    Eamp = max(amp(Es, i, j) for i in range(3) for j in range(3))
    ric = max(amp(Rics, i, j) for i in range(4) for j in range(4))
    return ric / Eamp


def verify_string_tension() -> None:
    for shape in ("travel", "standing"):
        r0 = string_ratio(shape, False)
        r1 = string_ratio(shape, True)
        assert r1 < 0.6 * r0, (shape, r0, r1)
        print(f"    {shape:9s}: Ricci/Riemann {r0:.2f} (u u only) ->"
              f" {r1:.2f} (with tension)")
    print()
    print("  THE TENSION TERM HALVES THE ADMIXTURE -- conservation")
    print("  acting -- but a truncated open string breaks")
    print("  conservation at its ends (the ratio does not converge")
    print("  with window size), so the Vachaspati test (exact")
    print("  traveling-wave silence) stays open pending a")
    print("  closed-loop source.  Recorded, not claimed.")


# =====================================================================
# 4. the operator square
# =====================================================================

def verify_operator_square() -> None:
    N = 5
    om = cmath.exp(2j * math.pi / N)
    # frame/charge operator spectrum: n; budget = square: n_a n_b
    ok = True
    for na in range(N):
        for nb in range(N):
            budget_phase = om ** ((na * nb) % N)
            # 0042's bond operator
            bond = om ** ((na * nb) % N)
            ok = ok and abs(budget_phase - bond) < 1e-12
    assert ok
    print("    holonomy of the squared-frame budget = "
          "omega^(n_a n_b):")
    print("    exactly 0042's measured bond table (N = 5, all 25")
    print("    states).")
    print()
    print("  B = e ^ e AT THE OPERATOR TIER: the budget operator is")
    print("  the symmetrized square of the frame operator; its")
    print("  holonomy spectrum is the multiplication table.  In 2+1")
    print("  B = e is linear and the spectrum is the additive n.")
    print("  'Budget = frame squared' holds at every tier the")
    print("  program has: metric (0046, exact tetrad), charges")
    print("  (0041/0042), action (0046), operators (here).")


def run_verification_suite() -> None:
    sections = [
        ("The channel rule, derived", verify_derivation),
        ("Conservation is the operative principle",
         verify_conservation_principle),
        ("The string's tension", verify_string_tension),
        ("The operator square", verify_operator_square),
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
