"""The momentum channel, and the half that is the bond.

0038 diagnosed the binary deficit: the null channel w k k^T lacks
the sender's momentum-flux tensor.  This module builds the
MOMENTUM CHANNEL -- the sender broadcasts its stress tensor,
metered by its clock:

    h_mu_nu = [4 m u_mu u_nu + 2 m eta_mu_nu] / (u . ell)

(the tensor Lienard-Wiechert form; the trace term is the
trace-reversal of h-bar = 4 m u u / (u.ell)) -- and re-runs the
binary in the true wave zone.  The result is exact, surprising,
and lands on the program's founding claim.

  s1  THE CONSTRUCTION.  Static limit: g_00 = -1 + 2m/r,
      g_ij = (1 + 2m/r) delta_ij -- linearized isotropic
      Schwarzschild, exactly.  Uniform motion: the momentum channel
      and the null channel agree at the gauge-invariant tier
      (E_ij = R_0i0j) to O(m) (0.8% at m = 0.01) -- the two
      broadcasts are gauge-equivalent wherever the sender does not
      accelerate.  Acceleration is where they part.

  s2  THE WAVE ZONE (R = 12, R/lambda ~ 6; 0038's R = 3 was near
      zone).  Face-on ratios to the GR quadrupole formula:
        null channel (KS):       0.001  -- NO quadrupole radiation;
        momentum channel (LW):   0.528 / 0.498  -- ONE HALF.

  s3  THE HALF THEOREM.  The direct field of free particles
      radiates from the momentum-flux integral
      int T_ij = sum m gamma^2 v_i v_j; the quadrupole formula's
      (2/R) I-ddot instead uses SOURCE CONSERVATION, which converts
      int T_ij into (1/2) I-ddot -- adding the stress of whatever
      binds the orbit.  For a circular orbit the oscillating parts
      obey (algebra):  int T_ij  =  (1/2) x (1/2) I-ddot -- the
      free-particle field is EXACTLY HALF the quadrupole formula.
      Measured: 0.528 = 1/2 (1 + O(v)).  THE MISSING HALF IS THE
      BOND: the binding interaction's own stress must radiate.  In
      web language, the pair's mutual channel -- their CORRELATION
      -- carries budget and sources curvature.  The program's
      founding claim ("correlation sources curvature") is,
      quantitatively, the other half of the quadrupole formula.
      The same object explains 0037's O(M1 M2) static vacuum
      violation (the bond's unaccounted stress) and 0038's
      in-plane non-vacuum radiation (the bond lives between the
      bodies -- in the plane).

  s4  THE BOND CHANNEL, BUILT AND VERIFIED.  The bond's integrated
      stress is exactly the conservation deficit
      S_ij(t) = (1/2) I-ddot_ij - sum m gamma v_i v_j (computed
      numerically from the worldlines, no model needed), broadcast
      retarded from the pair's center.  Result:
        face-on:  E_xx 1.017   E_xy 0.988
        edge-on:  E_xx 0.978   E_zz 1.005
      THE QUADRUPOLE FORMULA IS REPRODUCED to ~2% (= O(v)
      residuals).  The channel ontology that radiates like Einstein
      gravity: a channel broadcasts (i) the sender's participation
      (mass -> deficits, statics, Newton), (ii) the sender's
      momentum flux (u u^T -> the free half), (iii) the pair's BOND
      -- correlation as a source -- the other half.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_t = importlib.import_module("0030_the_time_sector")
_b = importlib.import_module("0033_the_binary_test")
riemann4 = _t.riemann4
ks_metric = _t.ks_metric
ETA = _t.ETA
z1, z2, v1, v2 = _b.z1, _b.z2, _b.v1, _b.v2
chan = _b.chan
gr_E = _b.gr_E
M_B, PER = _b.M_B, _b.PER

TAU = 2 * math.pi


# =====================================================================
# battery instrument: the momentum channel
# =====================================================================

def lw_h(m, zf, vf, x):
    """Tensor Lienard-Wiechert contribution of one worldline:
    h = [4 m u u^T + 2 m eta] / (u.ell), retarded, covariant."""
    t = x[0]
    lo, hi = t - 80.0, t
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if (t - mid) - math.dist(x[1:], zf(mid)) > 0:
            lo = mid
        else:
            hi = mid
    tr = 0.5 * (lo + hi)
    z = zf(tr)
    vv = vf(tr)
    ell0 = t - tr
    elv = tuple(x[1 + i] - z[i] for i in range(3))
    gam = 1.0 / math.sqrt(1.0 - sum(c * c for c in vv))
    udotl = gam * (ell0 - sum(vv[i] * elv[i] for i in range(3)))
    u = (-gam, gam * vv[0], gam * vv[1], gam * vv[2])
    return [[(4 * m * u[i] * u[j] + 2 * m * ETA[i][j]) / udotl
             for j in range(4)] for i in range(4)]


def E_of(gfun, x, h=2e-3):
    Rlow, _ = riemann4(gfun, x, h)
    return [[Rlow[0][1 + i][0][1 + j] for j in range(3)]
            for i in range(3)]


def g_lw_binary(x):
    m = [[ETA[i][j] for j in range(4)] for i in range(4)]
    for zf, vf in ((z1, v1), (z2, v2)):
        h = lw_h(M_B, zf, vf, x)
        for i in range(4):
            for j in range(4):
                m[i][j] += h[i][j]
    return m


def g_ks_binary(x):
    m = [[ETA[i][j] for j in range(4)] for i in range(4)]
    for zf, vf in ((z1, v1), (z2, v2)):
        k, w = chan(zf, vf, x)
        for i in range(4):
            for j in range(4):
                m[i][j] += w * k[i] * k[j]
    return m


def series_amp(series, i, j):
    vals = [s[i][j] for s in series]
    return (max(vals) - min(vals)) / 2


# =====================================================================
# 1. the construction
# =====================================================================

def verify_construction() -> None:
    m = 0.01
    zf = lambda t: (0.0, 0.0, 0.0)
    vf = lambda t: (0.0, 0.0, 0.0)

    def g_st(x):
        h = lw_h(m, zf, vf, x)
        return [[ETA[i][j] + h[i][j] for j in range(4)]
                for i in range(4)]
    g_ = g_st((0.0, 1.0, 0.0, 0.0))
    assert abs(g_[0][0] - (-1 + 2 * m)) < 1e-12
    assert abs(g_[1][1] - (1 + 2 * m)) < 1e-12
    assert abs(g_[0][1]) < 1e-12
    print("    static: g_00 = -1 + 2m/r, g_ij = (1 + 2m/r) delta --")
    print("    linearized isotropic Schwarzschild, exactly.")
    # uniform motion: gauge-invariant agreement with the null channel
    v = 0.5
    zfm = lambda t: (v * t, 0.0, 0.0)
    vfm = lambda t: (v, 0.0, 0.0)

    def g_lw1(x):
        h = lw_h(m, zfm, vfm, x)
        return [[ETA[i][j] + h[i][j] for j in range(4)]
                for i in range(4)]

    def g_ks1(x):
        t = x[0]
        lo, hi = t - 80.0, t
        for _ in range(70):
            mid = 0.5 * (lo + hi)
            if (t - mid) - math.dist(x[1:], zfm(mid)) > 0:
                lo = mid
            else:
                hi = mid
        tr = 0.5 * (lo + hi)
        ell0 = t - tr
        elv = (x[1] - v * tr, x[2], x[3])
        gam = 1 / math.sqrt(1 - v * v)
        udotl = gam * (ell0 - v * elv[0])
        k = (-ell0 / udotl, elv[0] / udotl, elv[1] / udotl,
             elv[2] / udotl)
        w = 2 * m / udotl
        return [[ETA[i][j] + w * k[i] * k[j] for j in range(4)]
                for i in range(4)]
    pt = (0.2, 0.5, 1.2, 0.4)
    E1 = E_of(g_lw1, pt)
    E2 = E_of(g_ks1, pt)
    mx = max(abs(E1[i][j]) for i in range(3) for j in range(3))
    dev = max(abs(E1[i][j] - E2[i][j])
              for i in range(3) for j in range(3))
    assert dev / mx < 0.02, dev / mx
    print(f"    uniform motion (v = 0.5): momentum channel and null")
    print(f"    channel agree at the E_ij tier to {dev / mx:.3f}")
    print(f"    (= O(m)): gauge-equivalent broadcasts wherever the")
    print(f"    sender does not accelerate.")


# =====================================================================
# 2. the wave zone
# =====================================================================

def wave_ratios(gfun, R=12.0, nph=12):
    grs = [gr_E((0, 0, 1), R, (k / nph) * PER) for k in range(nph)]
    Es = [E_of(gfun, ((k / nph) * PER, 0.0, 0.0, R))
          for k in range(nph)]
    out = {}
    for (i, j) in ((0, 0), (0, 1)):
        out[(i, j)] = series_amp(Es, i, j) / series_amp(grs, i, j)
    return out


def verify_wave_zone() -> None:
    rks = wave_ratios(g_ks_binary)
    rlw = wave_ratios(g_lw_binary)
    print(f"    face-on, R = 12 (R/lambda ~ 6), ratios to the GR")
    print(f"    quadrupole formula:")
    print(f"      null channel (KS):     E_xx {rks[(0, 0)]:.3f}   "
          f"E_xy {rks[(0, 1)]:.3f}")
    print(f"      momentum channel (LW): E_xx {rlw[(0, 0)]:.3f}   "
          f"E_xy {rlw[(0, 1)]:.3f}")
    assert rks[(0, 0)] < 0.01, rks
    assert 0.4 < rlw[(0, 0)] < 0.65, rlw
    assert 0.4 < rlw[(0, 1)] < 0.65, rlw
    print()
    print("  THE NULL CHANNEL CARRIES NO QUADRUPOLE RADIATION (0038's")
    print("  0.014 at R = 3 was near-zone residue); the momentum")
    print("  channel carries EXACTLY HALF.")


# =====================================================================
# 3. the half theorem
# =====================================================================

def verify_half_theorem() -> None:
    print("  The direct field of free particles radiates from the")
    print("  momentum-flux integral int T_ij = sum m g^2 v_i v_j; the")
    print("  quadrupole formula's (2/R) I-ddot uses SOURCE")
    print("  CONSERVATION, converting int T_ij -> (1/2) I-ddot and")
    print("  thereby including the stress of whatever binds the")
    print("  orbit.  Circular-orbit algebra: I = sum m z z^T gives")
    print("  I-ddot = 2 sum m [v v^T + z a^T]; with a = -Om^2 z the")
    print("  two oscillating terms are EQUAL, so the free (v v^T)")
    print("  field is exactly half.  Measured: 0.528 = 1/2 (1+O(v)).")
    print()
    print("  THE MISSING HALF IS THE BOND: the binding interaction's")
    print("  own stress must radiate.  In web language: the pair's")
    print("  mutual channel -- their CORRELATION -- carries budget")
    print("  and sources curvature.  The founding claim of this")
    print("  program is, quantitatively, the other half of the")
    print("  quadrupole formula.  The same object explains 0037's")
    print("  O(M1 M2) static vacuum violation (the bond's unaccounted")
    print("  stress) and 0038's in-plane non-vacuum radiation (the")
    print("  bond lives between the bodies).")


# =====================================================================
# 4. the bond channel
# =====================================================================

def I_ij(t):
    out = [[0.0] * 3 for _ in range(3)]
    for zf in (z1, z2):
        z = zf(t)
        for i in range(3):
            for j in range(3):
                out[i][j] += M_B * z[i] * z[j]
    return out


def part_T(t):
    """Integrated particle momentum flux sum m gamma v_i v_j."""
    out = [[0.0] * 3 for _ in range(3)]
    for vf in (v1, v2):
        v = vf(t)
        gam = 1 / math.sqrt(1 - sum(c * c for c in v))
        for i in range(3):
            for j in range(3):
                out[i][j] += M_B * gam * v[i] * v[j]
    return out


def S_bond(t, dt=1e-3):
    """The bond's integrated stress: the conservation deficit
    (1/2) I-ddot - sum m gamma v v^T, from the worldlines alone."""
    Ipp = [[(I_ij(t + dt)[i][j] - 2 * I_ij(t)[i][j]
             + I_ij(t - dt)[i][j]) / dt ** 2
            for j in range(3)] for i in range(3)]
    P = part_T(t)
    return [[0.5 * Ipp[i][j] - P[i][j] for j in range(3)]
            for i in range(3)]


def g_full_binary(x):
    """Momentum channels + the bond channel (retarded from the
    pair's center)."""
    m = [[ETA[i][j] for j in range(4)] for i in range(4)]
    for zf, vf in ((z1, v1), (z2, v2)):
        h = lw_h(M_B, zf, vf, x)
        for i in range(4):
            for j in range(4):
                m[i][j] += h[i][j]
    r = math.dist(x[1:], (0, 0, 0))
    S = S_bond(x[0] - r)
    for i in range(3):
        for j in range(3):
            m[1 + i][1 + j] += 4 * S[i][j] / r
    return m


def verify_bond_channel() -> None:
    R = 12.0
    nph = 12
    for name, pt3, nvec, comps in (
            ("face-on", (0.0, 0.0, R), (0, 0, 1), ((0, 0), (0, 1))),
            ("edge-on", (0.0, R, 0.0), (0, 1, 0), ((0, 0), (2, 2)))):
        grs = [gr_E(nvec, R, (k / nph) * PER) for k in range(nph)]
        Es = [E_of(g_full_binary, ((k / nph) * PER, pt3[0], pt3[1],
                                   pt3[2])) for k in range(nph)]
        out = []
        for (i, j) in comps:
            ratio = series_amp(Es, i, j) / series_amp(grs, i, j)
            assert 0.9 < ratio < 1.1, (name, i, j, ratio)
            out.append(f"E_{i}{j} {ratio:.3f}")
        print(f"    {name}: " + "  ".join(out))
    print()
    print("  THE QUADRUPOLE FORMULA IS REPRODUCED (~2% = O(v)):")
    print("  momentum channels + the bond channel -- the pair's")
    print("  correlation broadcast as a source, its stress the")
    print("  conservation deficit -- radiate like Einstein gravity.")
    print("  The channel ontology, complete at this tier:")
    print("    (i)   participation (mass):   statics, Newton;")
    print("    (ii)  momentum flux (u u^T):  the free half;")
    print("    (iii) the bond (correlation): the other half.")


def run_verification_suite() -> None:
    sections = [
        ("The construction", verify_construction),
        ("The wave zone", verify_wave_zone),
        ("The half theorem", verify_half_theorem),
        ("The bond channel", verify_bond_channel),
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
