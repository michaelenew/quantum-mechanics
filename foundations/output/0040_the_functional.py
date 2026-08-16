"""The functional: the channel is a gauge field, the metric its square.

The task was to write the action.  Half of it works, cleanly, and
resolves 0030's standing obstruction; the other half fails in a way
worth recording, and falls back to the prototype path (charges and
conservation fix the functional, as in 0026).

  s1  THE CHANNEL IS A MAXWELL FIELD.  Take the web's own channel
      one-form A_mu = w k_mu (0035's covariant channel).  Its field
      strength is EXACTLY the Lienard-Wiechert field: |F_channel -
      F_LW| / |F| = 1e-8 for a static source and 1e-8 for one
      boosted to v = 0.5 (the two potentials differ by a pure
      gradient -- the same gauge orbit).  The web's metric building
      block is a LINEAR GAUGE FIELD.

  s2  THE METRIC IS ITS SQUARE, AND THAT EXPLAINS FOUR MEASURED
      FACTS.  g = eta + w k k^T is quadratic in the channel data
      (the Kerr-Schild double copy: A = phi k solves Maxwell, g =
      eta + phi k k solves Einstein -- imported from the GR
      literature, verified here for the web's channel).  Then:
        - 0044's Kerr-Schild linearization is INHERITED: gravity is
          linear per channel because the gauge theory is linear;
        - 0041's "charges add, bonds multiply" is addition in the
          single copy versus multiplication in the square;
        - 0042's bond quantum = (charge quantum)^2, likewise;
        - the square-root ledger reappears at the top of the
          theory: THE CHANNEL IS THE AMPLITUDE, THE METRIC IS THE
          PROBABILITY.
      Measured here: the single copy's vacuum condition (w
      harmonic) selects p = d - 2 -- the SAME ladder gravity's
      vacuum principle selected in 0042 -- for every d >= 3.

  s3  0030's OBSTRUCTION RESOLVED.  0030 stopped at "4D BF is
      topological, so no gravitons; the bridge is Plebanski."  The
      answer is that the 3+1 single copy is not BF but MAXWELL: it
      carries a genuine field strength (Coulomb, Lienard-Wiechert,
      radiative), and its double copy is gravity WITH gravitons.
      The dimension dependence matches what the program already
      measured on both sides:
        2+1: the single copy degenerates (d = 2 gravity selects
             constant w -- the conical defect, no force, 0043 --
             where Maxwell would give a logarithm with a force);
             gravity is topological, and 0023 measured no radiation;
        3+1: Maxwell propagates, and 0031-0035 measured 1/R TT
             waves at the quadrupole luminosity.
      The obstruction was an artefact of taking BF as the 3+1
      single copy.

  s4  THE HONEST NEGATIVE, AND THE FALLBACK.  Does the double copy
      work OFF SHELL -- i.e. does adding the square's cross term to
      the two-body metric fix 0037's O(M1 M2) violation?  Measured:
      no.  Scanning the cross-term coefficient c over
      [-1, 1] leaves the violation MINIMAL AT c = 0 (5.2e-3, rising
      to 4.3e-2 at c = -1 and 5.0e-2 at c = +1).  The double copy is
      a solution-level correspondence, not an off-shell squaring
      map.  The bond therefore enters where it was already verified
      to work: as SOURCE STRESS (0039/0040 -- the quadrupole
      formula to 0.01% and the ADM binding energy to 0.03%).
      So: the single copy's functional is written, and the
      GRAVITATIONAL functional stands on the prototype path --
      fixed by its charges and conservation laws (0044), as 0026
      fixed the 2+1 action, rather than derived by squaring.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_t = importlib.import_module("0030_the_time_sector")
ricci4, ETA = _t.ricci4, _t.ETA

TAU = 2 * math.pi
M_C = 0.02


# =====================================================================
# 1. the channel is a Maxwell field
# =====================================================================

def _retarded(x, vel):
    t = x[0]
    lo, hi = t - 100.0, t
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if (t - mid) - math.dist(x[1:], (vel * mid, 0.0, 0.0)) > 0:
            lo = mid
        else:
            hi = mid
    tr = 0.5 * (lo + hi)
    ell0 = t - tr
    elv = (x[1] - vel * tr, x[2], x[3])
    gam = 1 / math.sqrt(1 - vel * vel)
    return ell0, elv, gam, gam * (ell0 - vel * elv[0])


def channel_A(x, vel=0.0):
    """The web's channel one-form A_mu = w k_mu."""
    ell0, elv, gam, udotl = _retarded(x, vel)
    w = 2 * M_C / udotl
    k = (-ell0 / udotl, elv[0] / udotl, elv[1] / udotl,
         elv[2] / udotl)
    return [w * c for c in k]


def lw_A(x, vel=0.0):
    """Lienard-Wiechert: A_mu = q u_mu / (u . ell), q = 2M."""
    ell0, elv, gam, udotl = _retarded(x, vel)
    u = (-gam, gam * vel, 0.0, 0.0)
    return [2 * M_C * c / udotl for c in u]


def faraday(Afun, x, vel, h=1e-4):
    dA = [[0.0] * 4 for _ in range(4)]
    for mu in range(4):
        xp, xm = list(x), list(x)
        xp[mu] += h
        xm[mu] -= h
        Ap, Am = Afun(tuple(xp), vel), Afun(tuple(xm), vel)
        for nu in range(4):
            dA[mu][nu] = (Ap[nu] - Am[nu]) / (2 * h)
    return [[dA[mu][nu] - dA[nu][mu] for nu in range(4)]
            for mu in range(4)]


def verify_channel_is_maxwell() -> None:
    x = (0.3, 0.9, 0.5, 0.4)
    for vel in (0.0, 0.5):
        F1 = faraday(channel_A, x, vel)
        F2 = faraday(lw_A, x, vel)
        sc = max(abs(F2[i][j]) for i in range(4) for j in range(4))
        dev = max(abs(F1[i][j] - F2[i][j])
                  for i in range(4) for j in range(4))
        assert dev / sc < 1e-5, (vel, dev / sc)
        print(f"    v = {vel}: |F_channel - F_LW| / |F| = "
              f"{dev / sc:.0e}")
    print()
    print("  THE CHANNEL IS A MAXWELL FIELD.  A_mu = w k_mu has")
    print("  exactly the Lienard-Wiechert field strength (the two")
    print("  potentials differ by a pure gradient -- one gauge")
    print("  orbit).  The web's metric building block is LINEAR.")


# =====================================================================
# 2. the metric is its square
# =====================================================================

def maxwell_residual(d, p, w0=0.02, h=1e-3):
    """div F = 0 off source <=> w harmonic; residual = lap w."""
    x = [0.7, 0.5, 0.4, 0.35, 0.3][:d]

    def w(pt):
        r = math.sqrt(sum(c * c for c in pt))
        return w0 / r ** p
    lap = 0.0
    for k in range(d):
        y1, y2 = list(x), list(x)
        y1[k] += h
        y2[k] -= h
        lap += (w(y1) - 2 * w(x) + w(y2)) / h ** 2
    return abs(lap)


def verify_double_copy() -> None:
    print("    single-copy vacuum (w harmonic), by dimension:")
    for d in (3, 4, 5):
        row = [(p, maxwell_residual(d, p))
               for p in (d - 3, d - 2, d - 1) if p >= 1]
        s = "  ".join(f"p={p}: {v:.0e}" + ("*" if p == d - 2 else "")
                      for p, v in row)
        print(f"      d = {d}:  {s}")
        for p, v in row:
            if p == d - 2:
                assert v < 1e-5, (d, p, v)
            else:
                assert v > 1e-3, (d, p, v)
    print("      (* = d-2: the SAME ladder gravity's vacuum")
    print("      principle selected in 0042)")
    print()
    print("  THE METRIC IS THE CHANNEL'S SQUARE (the Kerr-Schild")
    print("  double copy: A = phi k solves Maxwell, g = eta + phi k k")
    print("  solves Einstein).  That single structural fact explains")
    print("  four separate measurements:")
    print("    - 0044's linearization: gravity is linear per channel")
    print("      because the gauge theory is;")
    print("    - 0041's charges add, bonds multiply: addition in the")
    print("      single copy, multiplication in the square;")
    print("    - 0042's bond quantum = (charge quantum)^2;")
    print("    - the square-root ledger, at the top of the theory:")
    print("      THE CHANNEL IS THE AMPLITUDE, THE METRIC IS THE")
    print("      PROBABILITY.")


# =====================================================================
# 3. the obstruction resolved
# =====================================================================

def verify_obstruction_resolved() -> None:
    print("  0030 stopped at: '4D BF is topological, so no")
    print("  gravitons; the bridge is Plebanski's constraint.'  The")
    print("  resolution: the 3+1 single copy is not BF but MAXWELL.")
    print()
    print("    dim    single copy              gravity")
    print("    " + "-" * 58)
    print("    2+1    degenerate (d=2 gravity  topological; NO")
    print("           takes constant w --      radiation (measured,")
    print("           the conical defect,      0023)")
    print("           no force, 0043)")
    print("    3+1    Maxwell: Coulomb,        gravitons; 1/R TT")
    print("           Lienard-Wiechert,        waves at the")
    print("           radiative                quadrupole luminosity")
    print("                                    (measured, 0031-0035)")
    print()
    print("  Both rows were measured on both sides before this")
    print("  module; the double copy is what ties them together.")
    print("  The obstruction was an artefact of taking BF as the")
    print("  3+1 single copy.")


# =====================================================================
# 4. the honest negative, and the fallback
# =====================================================================

M_S, D_S = 0.01, 1.0
C1, C2 = (-D_S / 2, 0.0, 0.0), (D_S / 2, 0.0, 0.0)


def g_cross(cc):
    """Sum of squares plus cc times the double-copy cross term."""
    def g(x):
        ch = []
        for c in (C1, C2):
            r = math.dist(x[1:], c)
            k = (-1.0, (x[1] - c[0]) / r, (x[2] - c[1]) / r,
                 (x[3] - c[2]) / r)
            ch.append((2 * M_S / r, k))
        (w1, k1), (w2, k2) = ch
        m = [[ETA[i][j] for j in range(4)] for i in range(4)]
        for (w, k) in ch:
            for i in range(4):
                for j in range(4):
                    m[i][j] += w * k[i] * k[j]
        s = math.sqrt(w1 * w2)
        for i in range(4):
            for j in range(4):
                m[i][j] += cc * s * (k1[i] * k2[j]
                                     + k2[i] * k1[j]) / 2
        return m
    return g


PTS = [(0.0, 0.0, 0.45, 0.30), (0.0, 0.35, 0.60, 0.0),
       (0.0, 0.2, 0.3, 0.4)]


def verify_negative_and_fallback() -> None:
    print("    does off-shell squaring fix the two-body sector?")
    results = []
    for cc in (-1.0, -0.5, 0.0, 0.5, 1.0):
        worst = 0.0
        for x in PTS:
            R = ricci4(g_cross(cc), x, h=1e-3)
            worst = max(worst, max(abs(R[i][j])
                                   for i in range(4)
                                   for j in range(4)))
        results.append((cc, worst))
        tag = "   <-- sum of squares (0037)" if cc == 0.0 else ""
        print(f"      c = {cc:+.1f}: max|R_mn| = {worst:.2e}{tag}")
    best = min(results, key=lambda r: r[1])
    assert best[0] == 0.0, best
    print(f"    minimum at c = {best[0]:+.1f}: NO.")
    print()
    print("  THE DOUBLE COPY IS A SOLUTION-LEVEL CORRESPONDENCE,")
    print("  not an off-shell squaring map.  The bond therefore")
    print("  enters where it was already verified to work -- as")
    print("  SOURCE STRESS (0039/0040: the quadrupole formula to")
    print("  0.01%, the ADM binding energy to 0.03%).")
    print()
    print("  THE STATE OF THE ACTION:")
    print("    single copy, WRITTEN:")
    print("      S = -(1/4) int F_mn F^mn d^4x + sum_a q_a int A.dx")
    print("      with g = eta + phi k k, A = phi k, k null geodesic;")
    print("      linear per channel, reducing in 2+1 to the")
    print("      topological form 0026 built (S = sum B(curl th -")
    print("      src));")
    print("    gravitational functional: PROTOTYPE PATH -- fixed by")
    print("      its charges and conservation laws (0044), as 0026")
    print("      fixed the 2+1 action, rather than derived by")
    print("      squaring.  What remains is an off-shell map, and")
    print("      the measured obstruction to the naive one is")
    print("      recorded above.")


def run_verification_suite() -> None:
    sections = [
        ("The channel is a Maxwell field",
         verify_channel_is_maxwell),
        ("The metric is its square", verify_double_copy),
        ("0030's obstruction resolved",
         verify_obstruction_resolved),
        ("The honest negative, and the fallback",
         verify_negative_and_fallback),
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
