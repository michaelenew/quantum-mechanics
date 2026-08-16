"""The binary test: superposed channels miss the quadrupole formula.

0037 opened the strongest correspondence test in reach: orbit two
vacuum-profile sources and compare the radiation against GR's
quadrupole formula, coefficient included.  Run here.  The result is
a sharp, quantified NO for the naive two-body rule -- and a precise
diagnosis.

Setup: equal masses M on a circular orbit (radius a0, Newtonian
Omega, v = 0.2), each sourcing a covariant retarded null channel
with the vacuum profile w = 2M/(u.ell); the two-body metric is the
superposition (the web's natural ansatz, already known to violate
vacuum at O(M1 M2) in statics, 0037).  The GR side is the retarded
quadrupole formula computed NUMERICALLY from the same worldlines
(h = (2/R) TT[I-ddot(t-R)], E = -1/2 h-ddot -- no hand factors).

  s1  THE GR PREDICTOR sanity: face-on E amplitude = 2x edge-on
      (the (1+cos^2 i)/2 vs sin^2 pattern), circular polarization
      on axis -- the standard binary pattern, reproduced by the
      numerical predictor.

  s2  THE MEASUREMENT.  The web's E-wave vs GR's, same worldlines:
        face-on (orbit axis):  ratio 0.014  -- 70x too weak;
        edge-on (in plane):    ratio ~0.47  -- half strength.
      The radiation PATTERN INVERTS: GR is loudest face-on; the
      web is nearly silent there.  (On axis the two particles'
      direction-jitters cancel pairwise -- the dipole cancellation
      works -- but the surviving channel quadrupole is far below
      GR's.)

  s3  THE VACUUM STRUCTURE: the on-axis wave, tiny as it is, is
      VACUUM (4D Ricci wave ~ 1e-8); the orbital plane carries a
      large non-vacuum oscillating stress (Ricci wave comparable to
      the Riemann wave) -- the O(M1 M2) interaction zone, now seen
      radiating.

  s4  THE DIAGNOSIS.  Linearized GR's moving-source solution is the
      tensor Lienard-Wiechert potential h ~ 4 m u_mu u_nu/(u.ell):
      the source's MOMENTUM FLUX (u u^T) enters the tensor
      structure.  The channel form w k k^T carries mass and
      direction but not this m v_i v_j sector at the needed order
      -- and the quadrupole wave IS an order-v^2 effect.  This is
      the third independent appearance of the anisotropic-strength
      object (0024's m m^T kinematics; 0032's strength-sector
      demand, corrected to statics by 0034; now the radiative
      two-body tier).  The single-source sector is fully Einstein
      (statics exact, TT waves, classical tests); the TWO-BODY RULE
      is the program's frontier, with its failure now measured:
      0.014 face-on, 0.47 edge-on, O(M1 M2) static violation.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_t = importlib.import_module("0030_the_time_sector")
ks_metric = _t.ks_metric
riemann4 = _t.riemann4
ETA = _t.ETA

TAU = 2 * math.pi

M_B, A0 = 0.02, 0.125
OM_B = math.sqrt(2 * M_B / (2 * A0) ** 3)
PER = TAU / OM_B


def z1(t):
    return (A0 * math.cos(OM_B * t), A0 * math.sin(OM_B * t), 0.0)


def z2(t):
    return (-A0 * math.cos(OM_B * t), -A0 * math.sin(OM_B * t), 0.0)


def v1(t):
    return (-A0 * OM_B * math.sin(OM_B * t),
            A0 * OM_B * math.cos(OM_B * t), 0.0)


def v2(t):
    return (A0 * OM_B * math.sin(OM_B * t),
            -A0 * OM_B * math.cos(OM_B * t), 0.0)


def chan(zf, vf, x):
    t = x[0]
    lo, hi = t - 60.0, t
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
    g_ = 1.0 / math.sqrt(1.0 - sum(c * c for c in vv))
    udotl = g_ * (ell0 - sum(vv[i] * elv[i] for i in range(3)))
    k = (-ell0 / udotl, elv[0] / udotl, elv[1] / udotl,
         elv[2] / udotl)
    return k, 2 * M_B / udotl


def g_binary(x):
    m = [[ETA[i][j] for j in range(4)] for i in range(4)]
    for zf, vf in ((z1, v1), (z2, v2)):
        k, w = chan(zf, vf, x)
        for i in range(4):
            for j in range(4):
                m[i][j] += w * k[i] * k[j]
    return m


def E_of(x, h=2e-3):
    Rlow, Ric = riemann4(g_binary, x, h)
    return [[Rlow[0][1 + i][0][1 + j] for j in range(3)]
            for i in range(3)], Ric


# GR quadrupole predictor -- fully numerical, no hand factors
def I_ij(t):
    out = [[0.0] * 3 for _ in range(3)]
    for zf in (z1, z2):
        z = zf(t)
        for i in range(3):
            for j in range(3):
                out[i][j] += M_B * z[i] * z[j]
    return out


def gr_E(nvec, R, t, dt=1e-3):
    def hTT(tt):
        Ipp = [[(I_ij(tt - R + dt)[i][j] - 2 * I_ij(tt - R)[i][j]
                 + I_ij(tt - R - dt)[i][j]) / dt ** 2
                for j in range(3)] for i in range(3)]
        P = [[(1 if i == j else 0) - nvec[i] * nvec[j]
              for j in range(3)] for i in range(3)]
        T = [[sum(P[i][a] * Ipp[a][b] * P[b][j]
                  for a in range(3) for b in range(3))
              for j in range(3)] for i in range(3)]
        tr = T[0][0] + T[1][1] + T[2][2]
        return [[(2.0 / R) * (T[i][j] - 0.5 * tr * P[i][j])
                 for j in range(3)] for i in range(3)]
    hp, h0, hm = hTT(t + dt), hTT(t), hTT(t - dt)
    return [[-0.5 * (hp[i][j] - 2 * h0[i][j] + hm[i][j]) / dt ** 2
             for j in range(3)] for i in range(3)]


def series_amp(series, i, j):
    vals = [s[i][j] for s in series]
    return (max(vals) - min(vals)) / 2


def measure(pt3, nvec, nph=12):
    Es, Rics, grs = [], [], []
    for k in range(nph):
        t = (k / nph) * PER
        E, Ric = E_of((t, pt3[0], pt3[1], pt3[2]))
        Es.append(E)
        Rics.append(Ric)
        grs.append(gr_E(nvec, 3.0, t))
    ric = max(series_amp(Rics, i, j)
              for i in range(4) for j in range(4))
    return Es, grs, ric


# =====================================================================
# 1. the GR predictor
# =====================================================================

def verify_gr_predictor() -> None:
    face = [gr_E((0, 0, 1), 3.0, (k / 12) * PER) for k in range(12)]
    edge = [gr_E((0, 1, 0), 3.0, (k / 12) * PER) for k in range(12)]
    f_xx = series_amp(face, 0, 0)
    f_xy = series_amp(face, 0, 1)
    e_xx = series_amp(edge, 0, 0)
    assert abs(f_xx / e_xx - 2.0) < 0.01, f_xx / e_xx
    assert abs(f_xy / f_xx - 0.95) < 0.1, f_xy / f_xx
    print(f"    face-on/edge-on amplitude = {f_xx / e_xx:.3f} (= 2,")
    print(f"    the (1+cos^2)/2 vs sin^2 pattern); on-axis cross")
    print(f"    component comparable to diagonal (circular")
    print(f"    polarization) -- the standard binary pattern from the")
    print(f"    numerical predictor, no hand factors.")


# =====================================================================
# 2. the measurement
# =====================================================================

def verify_measurement() -> None:
    print(f"    binary: M = {M_B}, a0 = {A0}, Omega = {OM_B:.3f}, "
          f"v = {OM_B * A0:.2f}")
    Ef, grf, ricf = measure((0.0, 0.0, 3.0), (0, 0, 1))
    Ee, gre, rice = measure((0.0, 3.0, 0.0), (0, 1, 0))
    rf = series_amp(Ef, 0, 0) / series_amp(grf, 0, 0)
    re = series_amp(Ee, 0, 0) / series_amp(gre, 0, 0)
    print(f"    face-on:  web/GR E_xx ratio = {rf:.3f}")
    print(f"    edge-on:  web/GR E_xx ratio = {re:.3f}")
    assert rf < 0.05, rf
    assert 0.2 < re < 0.8, re
    print()
    print("  THE QUADRUPOLE FORMULA IS MISSED: 70x too weak face-on,")
    print("  half-strength edge-on -- and the pattern INVERTS (GR is")
    print("  loudest face-on; the web nearly silent there).  The")
    print("  dipole cancellation works on axis; the surviving channel")
    print("  quadrupole is far below GR's.")
    # vacuum structure
    Eampf = max(series_amp(Ef, i, j)
                for i in range(3) for j in range(3))
    Eampe = max(series_amp(Ee, i, j)
                for i in range(3) for j in range(3))
    assert ricf < 0.01 * Eampf, (ricf, Eampf)
    assert rice > 0.5 * Eampe, (rice, Eampe)
    print(f"    on-axis Ricci wave {ricf:.1e} (vacuum wave);")
    print(f"    in-plane Ricci wave {rice:.1e} vs Riemann {Eampe:.1e}")
    print(f"    -- the O(M1 M2) interaction zone, seen radiating.")


# =====================================================================
# 3. the diagnosis
# =====================================================================

def verify_diagnosis() -> None:
    print("  Linearized GR's moving-source solution is the tensor")
    print("  Lienard-Wiechert potential h ~ 4 m u_mu u_nu/(u.ell):")
    print("  the source's MOMENTUM FLUX enters the tensor structure.")
    print("  The channel form w k k^T carries mass and direction but")
    print("  not the m v_i v_j sector at the needed order -- and the")
    print("  quadrupole wave is an order-v^2 effect.  Third")
    print("  appearance of the anisotropic-strength object (0024")
    print("  kinematics; 0034 statics; now the radiative two-body")
    print("  tier).  The single-source sector is fully Einstein; THE")
    print("  TWO-BODY RULE is the program's frontier, its failure")
    print("  measured: 0.014 face-on, ~0.47 edge-on, O(M1 M2) static")
    print("  violation.")


def run_verification_suite() -> None:
    sections = [
        ("The GR predictor", verify_gr_predictor),
        ("The measurement", verify_measurement),
        ("The diagnosis", verify_diagnosis),
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
