"""The gauge audit: the web's wave is TT after all.

The severity question -- does 0032's "wrong polarization" force
falsified predictions? -- demanded a gauge audit before any new
construction: is the vector metric wave gauge-INVARIANTLY there?
The audit reverses 0032's verdict.

  s1  THE INSTRUMENT (ricci_tensor3).  The full 3D Ricci TENSOR
      pipeline, validated: the unit 3-sphere satisfies the Einstein
      condition R_ij = 2 g_ij to 1e-5; a TT plane wave has a LINEAR
      Ricci tensor equal to -1/2 lap(h) to 0.1% (so TT is invisible
      to the linear Ricci SCALAR of 0032/s1 but visible to the
      linear tensor); a vector plane wave has IDENTICALLY ZERO
      Ricci tensor.  In 3D, Weyl vanishes identically, so Ricci
      determines Riemann: zero Ricci tensor = flat = pure
      coordinates.  The tensor is the gauge-invariant meter.

  s2  THE AUDIT.  The web wave's RICCI-TENSOR polarization,
      decomposed against the propagation direction: TT fraction
      0.98 at R = 3 and R = 6 (channel amplitude halving exactly,
      1/R); the vector channel -- dominant in the raw METRIC -- is
      1-2% of the invariant wave.  0032's "pure vector wave" was
      the gauge dressing of a TT wave: the slaved-channel form
      I + w u u^T writes TT curvature in vector metric components,
      because the direction field's z-structure (along the string)
      crossed with its radial retardation carries curvature a
      plane-wave decomposition cannot see.

  s3  THE LINEAR TT WAVE.  The dominant invariant component is
      R_xz -- TT, polarized in the (jitter, string-axis) plane --
      and it is LINEAR in the wiggle amplitude (exponent ~1.06),
      at the FUNDAMENTAL (harmonic purity > 1e3), decaying as
      exactly 1/R (amp ratio 1.170 vs 7/6 = 1.167), OUTGOING at c
      (radial phase advance 1.998 vs Om dR = 2.000; instantaneous
      control 337x weaker with no outgoing phase).  The diagonal
      components are quadratic at 2 Om -- the quadrupole tier that
      0031's scalar-only instrument saw.

  s4  THE SEVERITY VERDICT.  No falsified predictions are forced.
      Had the vector wave been physical it would have been fatal
      (LIGO's multi-detector polarization tests favor tensor over
      vector; binary-pulsar decay forbids a dominant dipole
      channel; waveforms sit at twice the orbital frequency) --
      wrong channel, wrong frequency, wrong multipole is not a
      coefficient patch.  But the vector wave carries (essentially)
      no invariant curvature: no gauge-invariant observable at
      linear order transmits it.  What IS invariantly there has
      the Einstein signature: TT-dominant, linear at the source
      frequency + quadratic at its double, 1/R, speed c.  Remaining
      genuine risks, named: the second-order scalar admixture
      (longitudinal 0.19 / trace 0.10 of the invariant wave); the
      luminal traveling wiggle radiating where Nambu-Goto strings
      exactly do not (a matter-sector difference, not field
      dynamics); and the unbuilt time sector (lapse/shift), which
      full detector response requires.  0032's strength-sector
      diagnosis is CORRECTED: the direction field alone carries
      TT radiation; the strength tensor remains demanded by the
      velocity-statics anomalies (0023/0024/0025), not by waves.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_t = importlib.import_module("0027_the_correspondence_test")
mode_metric = _t.mode_metric
polarization_channels = _t.polarization_channels
travel_pos = _t.travel_pos
string_wave_metric = _t.string_wave_metric
A_W, OM_W, K_W, W_W = _t.A_W, _t.OM_W, _t.K_W, _t.W_W
_c = importlib.import_module("0026_testing_the_candidate")
harmonic = _c.harmonic
sphere_metric = _c.sphere_metric

TAU = 2 * math.pi
PERIOD = TAU / OM_W


# =====================================================================
# battery instrument: the 3D Ricci tensor
# =====================================================================

def inv3(m):
    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]
    A = (e * i - f * h)
    B = -(d * i - f * g)
    C = (d * h - e * g)
    D = -(b * i - c * h)
    E = (a * i - c * g)
    F = -(a * h - b * g)
    G = (b * f - c * e)
    H = -(a * f - c * d)
    I = (a * e - b * d)
    det = a * A + b * B + c * C
    return [[A / det, D / det, G / det],
            [B / det, E / det, H / det],
            [C / det, F / det, I / det]]


def ricci_tensor(gfun, x, h=1e-3):
    """Full Ricci tensor R_ij of a 3D metric, central differences."""
    ex = [(h, 0, 0), (0, h, 0), (0, 0, h)]

    def shift(p, k, s):
        return (p[0] + s * ex[k][0], p[1] + s * ex[k][1],
                p[2] + s * ex[k][2])

    def christ(p):
        gp = [gfun(shift(p, k, 1)) for k in range(3)]
        gm = [gfun(shift(p, k, -1)) for k in range(3)]
        dg = [[[(gp[k][i][j] - gm[k][i][j]) / (2 * h)
                for j in range(3)] for i in range(3)] for k in range(3)]
        gi = inv3(gfun(p))
        G = [[[0.0] * 3 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    s = 0.0
                    for l in range(3):
                        s += gi[i][l] * (dg[j][l][k] + dg[k][l][j]
                                         - dg[l][j][k])
                    G[i][j][k] = 0.5 * s
        return G

    G0 = christ(x)
    Gp = [christ(shift(x, k, 1)) for k in range(3)]
    Gm = [christ(shift(x, k, -1)) for k in range(3)]
    dG = [[[[(Gp[k][i][j][l] - Gm[k][i][j][l]) / (2 * h)
             for l in range(3)] for j in range(3)]
           for i in range(3)] for k in range(3)]
    R = [[0.0] * 3 for _ in range(3)]
    for j in range(3):
        for l in range(3):
            s = 0.0
            for i in range(3):
                s += dG[i][i][j][l] - dG[j][i][i][l]
                for p in range(3):
                    s += G0[i][i][p] * G0[p][j][l] \
                        - G0[i][j][p] * G0[p][i][l]
            R[j][l] = s
    return R


def wiggle_metric_A(A, t_obs):
    """The 0031/0032 traveling wiggle at amplitude A."""
    def pos(zp, t):
        return travel_pos(zp, t, A)
    return string_wave_metric(pos, t_obs)


def h1_of(series):
    m = sum(series) / len(series)
    return harmonic([v - m for v in series], 1), \
        harmonic([v - m for v in series], 2)


# =====================================================================
# 1. the instrument
# =====================================================================

def verify_instrument() -> None:
    pt = (0.3, 0.1, 0.2)
    R = ricci_tensor(sphere_metric, pt)
    g = sphere_metric(pt)
    err = max(abs(R[i][j] - 2 * g[i][j])
              for i in range(3) for j in range(3))
    assert err < 1e-4, err
    print(f"    unit 3-sphere: Einstein condition R_ij = 2 g_ij to "
          f"{err:.0e}.")
    pt = (0.3, 0.2, 0.4)
    eps, k = 1e-3, 2.0
    Rtt = ricci_tensor(mode_metric(eps, "TT", k), pt)
    pred = 0.5 * k * k * eps * math.cos(k * pt[2])
    assert abs(Rtt[0][0] - pred) / abs(pred) < 0.01, (Rtt[0][0], pred)
    assert abs(Rtt[1][1] + pred) / abs(pred) < 0.01
    print(f"    TT plane wave: LINEAR Ricci tensor, R_xx = -1/2 lap h")
    print(f"    = {Rtt[0][0]:.3e} vs analytic {pred:.3e} -- TT is")
    print(f"    invisible to the linear scalar (0032/s1) but visible")
    print(f"    to the linear tensor.")
    Rv = ricci_tensor(mode_metric(eps, "vector", k), pt)
    nv = max(abs(Rv[i][j]) for i in range(3) for j in range(3))
    assert nv < 1e-11, nv
    print(f"    vector plane wave: Ricci tensor identically zero")
    print(f"    ({nv:.0e}).  In 3D Weyl vanishes identically, so")
    print(f"    Ricci determines Riemann: zero tensor = flat = pure")
    print(f"    coordinates.  The tensor is the gauge-invariant meter.")


# =====================================================================
# 2. the audit
# =====================================================================

def ricci_polarization(R, nph=12):
    n = (0.0, 1.0, 0.0)
    pt = (0.0, R, 0.3)
    Rs = [ricci_tensor(wiggle_metric_A(A_W, (k / nph) * PERIOD), pt,
                       h=2e-3) for k in range(nph)]
    mean = [[sum(Rm[i][j] for Rm in Rs) / nph for j in range(3)]
            for i in range(3)]
    acc = [0.0] * 4
    for Rm in Rs:
        d = [[Rm[i][j] - mean[i][j] for j in range(3)]
             for i in range(3)]
        c = polarization_channels(d, n)
        for i in range(4):
            acc[i] += c[i] ** 2 / nph
    return [math.sqrt(a) for a in acc]


def verify_audit() -> None:
    chans = {}
    for R in (3.0, 6.0):
        L, V, Ttr, TTn = ricci_polarization(R)
        chans[R] = (L, V, Ttr, TTn)
        tot = math.sqrt(L * L + V * V + Ttr * Ttr + TTn * TTn)
        assert TTn / tot > 0.9, (R, TTn / tot)
        assert V / tot < 0.05, (R, V / tot)
        print(f"    R = {R}: long {L:.2e}  vector {V:.2e}  "
              f"trace {Ttr:.2e}  TT {TTn:.2e}")
        print(f"           TT fraction {TTn / tot:.3f}, "
              f"vector fraction {V / tot:.3f}")
    ratio = chans[3.0][3] / chans[6.0][3]
    assert abs(ratio - 2.0) < 0.05, ratio
    print(f"    TT channel halves R = 3 -> 6 (ratio {ratio:.3f}): 1/R.")
    print()
    print("  THE METRIC-LEVEL VERDICT OF 0032 REVERSES gauge-")
    print("  invariantly: the 'pure vector wave' carries almost no")
    print("  curvature -- it is the gauge dressing of a TT wave.  The")
    print("  slaved form I + w u u^T writes TT curvature in vector")
    print("  metric components: the direction field's z-structure")
    print("  (along the string) crossed with radial retardation is")
    print("  curvature a plane-wave decomposition cannot see.")


# =====================================================================
# 3. the linear TT wave
# =====================================================================

def rxz_series(A, R, nph=12):
    pt = (0.0, R, 0.3)
    return [ricci_tensor(wiggle_metric_A(A, (k / nph) * PERIOD), pt,
                         h=2e-3)[0][2] for k in range(nph)]


def instant_metric_A(A, t_obs):
    """Instantaneous (non-retarded) control: channels point at the
    string's current position."""
    def f(x, zp):
        return math.dist(x, travel_pos(zp, t_obs, A))

    def g(x):
        zc = x[2]
        best, bz = None, None
        for i in range(41):
            zp = zc - 2.0 + 4.0 * i / 40
            d = f(x, zp)
            if best is None or d < best:
                best, bz = d, zp
        a, b = bz - 0.15, bz + 0.15
        gr = (math.sqrt(5) - 1) / 2
        c = b - gr * (b - a)
        d2 = a + gr * (b - a)
        fc, fd = f(x, c), f(x, d2)
        for _ in range(45):
            if fc < fd:
                b, d2, fd = d2, c, fc
                c = b - gr * (b - a)
                fc = f(x, c)
            else:
                a, c, fc = c, d2, fd
                d2 = a + gr * (b - a)
                fd = f(x, d2)
        s = travel_pos(0.5 * (a + b), t_obs, A)
        dist = math.dist(x, s)
        u = ((s[0] - x[0]) / dist, (s[1] - x[1]) / dist,
             (s[2] - x[2]) / dist)
        return [[(1 if i == j else 0) + W_W * u[i] * u[j]
                 for j in range(3)] for i in range(3)]
    return g


def verify_linear_tt() -> None:
    # linear in A, fundamental-pure
    amps = {}
    for A in (0.05, 0.1):
        s = rxz_series(A, 4.0)
        (a1, _), (a2, _) = h1_of(s)
        amps[A] = a1
        assert a1 > 1e3 * a2, (a1, a2)
    q = math.log(amps[0.1] / amps[0.05]) / math.log(2)
    assert 0.9 < q < 1.2, q
    print(f"    R_xz -- TT, polarized in the (jitter, string-axis)")
    print(f"    plane -- is LINEAR in the wiggle amplitude (exponent")
    print(f"    {q:.2f}) and fundamental-pure (H1/H2 > 1e3).")
    # 1/R and outgoing at c
    s6 = rxz_series(A_W, 6.0)
    s7 = rxz_series(A_W, 7.0)
    (a6, p6), _ = h1_of(s6)
    (a7, p7), _ = h1_of(s7)
    assert abs(a6 / a7 - 7.0 / 6.0) < 0.02, a6 / a7
    adv = (p7 - p6) % TAU
    assert abs(adv - OM_W) < 0.05, (adv, OM_W)
    print(f"    decay: amp(6)/amp(7) = {a6 / a7:.3f} vs 7/6 = "
          f"{7 / 6:.3f} -- exactly 1/R.")
    print(f"    outgoing: radial phase advance {adv:.3f} vs "
          f"Om dR = {OM_W:.3f}.")
    # instantaneous control
    si = [ricci_tensor(instant_metric_A(A_W, (k / 12) * PERIOD),
                       (0.0, 6.0, 0.3), h=2e-3)[0][2]
          for k in range(12)]
    (ai, _), _ = h1_of(si)
    assert a6 / ai > 100, a6 / ai
    print(f"    instantaneous control: {a6 / ai:.0f}x weaker -- the")
    print(f"    wave is retardation-made.")
    print()
    print("  A GENUINE LINEAR TT CURVATURE WAVE at the source's own")
    print("  frequency, plus the quadratic 2 Om quadrupole tier on")
    print("  the diagonal -- the structure linearized Einstein")
    print("  gravity assigns to a radiating source.")


# =====================================================================
# 4. the severity verdict
# =====================================================================

def verify_verdict() -> None:
    print("  DOES THE WRONG OSCILLATION FORCE FALSIFIED PREDICTIONS?")
    print("  No.  Itemized:")
    print("    - IF the vector metric wave were physical, it would be")
    print("      fatal: multi-detector polarization tests favor")
    print("      tensor over vector; binary-pulsar decay forbids a")
    print("      dominant dipole channel; observed waveforms sit at")
    print("      twice the orbital frequency.  Wrong channel + wrong")
    print("      frequency + wrong multipole cannot be patched by a")
    print("      coefficient.")
    print("    - But it is NOT physical: its invariant curvature")
    print("      content is 1-2%.  No gauge-invariant observable at")
    print("      linear order transmits it (exact on spatial")
    print("      geometry; full detector response needs the unbuilt")
    print("      time sector).")
    print("    - What IS invariant has the Einstein signature:")
    print("      TT-dominant (0.98), linear at the source frequency,")
    print("      quadratic at its double, 1/R, speed c.")
    print("  Remaining genuine risks: the second-order scalar")
    print("  admixture (long 0.19 / trace 0.10); the luminal")
    print("  traveling wiggle radiating where Nambu-Goto strings")
    print("  exactly do not (matter sector, not field dynamics; no")
    print("  observational data constrains it); the time sector.")
    print("  0032's strength diagnosis CORRECTED: the direction")
    print("  field alone carries TT radiation; the strength tensor")
    print("  remains demanded by velocity STATICS (0023/0024/0025),")
    print("  not by waves.")


def run_verification_suite() -> None:
    sections = [
        ("The instrument (ricci_tensor3)", verify_instrument),
        ("The audit: invariant polarization", verify_audit),
        ("The linear TT wave", verify_linear_tt),
        ("The severity verdict", verify_verdict),
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
