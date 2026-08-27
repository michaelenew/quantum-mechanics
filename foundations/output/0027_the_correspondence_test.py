"""The correspondence test: which wave theory does the web carry?

0031 established EXISTENCE: the 3+1 web radiates (1/R, outgoing at
c, frequency-doubled).  This module runs the CORRESPONDENCE test
against linearized Einstein gravity, in three independent probes,
and returns a sharp verdict: the wave sector is real but it is NOT
Einstein's -- and the mismatch is localized to one named object.

  s1  THE DISCRIMINATORS.  Plane-wave test metrics pushed through
      the validated Ricci pipeline fix what each polarization looks
      like to our instrument: a TT wave carries ZERO spatial Ricci
      at linear order (amplitude-scaling exponent 2.00 -- purely
      quadratic), scalar and trace modes respond LINEARLY (1.00),
      and a vector plane wave is IDENTICALLY zero.  So Einstein's
      radiation is invisible to the linear Ricci scalar, and any
      linear-order Ricci wave is already non-Einstein.

  s2  THE POLARIZATION.  The web's far-field metric wave,
      decomposed Frobenius-orthogonally against the propagation
      direction, is PURE VECTOR: amplitude = w A / R exactly
      (0.6% at R = 3 and 6), oscillating at the fundamental
      (harmonic purity > 1e9), while longitudinal, transverse-
      trace, and TT channels all sit at ~1% and fall as 1/R^2
      (second order).  Coherence check: the Ricci wave is
      QUADRATIC in the wiggle amplitude (exponent ~1.9) at 2 Om --
      exactly as it must be, since the linear wave is vector and a
      vector wave carries no linear Ricci (s1).  Einstein gravity
      FORBIDS a propagating vector polarization.

  s3  TRAVELING VS STANDING.  In GR a traveling wave on a straight
      string is an EXACT NON-RADIATING solution (Vachaspati 1986;
      Garfinkle 1990 -- literature import), while standing waves
      radiate.  The web inverts this: both radiate at 1/R and the
      traveling wave is ~3x STRONGER.

  s4  THE VERDICT.  Correspondence FAILS at linear order, in a
      precisely characterized way: the only thing that propagates
      is the direction field u -- the sole unfrozen piece of
      g = I + w u u^T once |u| = 1 slaves the channel and w is
      frozen.  The TT graviton would have to live in a PROPAGATING
      STRENGTH TENSOR, and nothing propagates there.  This is the
      same missing object three independent 2+1 diagnoses already
      demanded (0023's compass, 0024's baseline necessity, 0025's
      Michelson-Morley), whose kinematic form the Lorentz
      completion already built (the m m^T channel + boosted
      baseline).  The web-native job of Plebanski's simplicity
      constraint is now sharp: promote the strength sector to a
      dynamical field whose radiative modes are TT.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_c = importlib.import_module("0026_testing_the_candidate")
ricci_scalar = _c.ricci_scalar
harmonic = _c.harmonic

TAU = 2 * math.pi

# the wiggle family (same parameters as 0031)
A_W, OM_W, K_W, W_W = 0.1, 2.0, 2.0, 0.3
PERIOD = TAU / OM_W


# =====================================================================
# battery instrument 1: plane-wave discriminator modes
# =====================================================================

def mode_metric(eps, kind, k=2.0):
    """Plane-wave test metric g = I + eps * (mode) * cos(k z)."""
    def g(x):
        c = eps * math.cos(k * x[2])
        m = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
        if kind == "TT":
            m[0][0] += c
            m[1][1] -= c
        elif kind == "scalar":
            m[0][0] += c
        elif kind == "vector":
            m[0][2] += c
            m[2][0] += c
        elif kind == "trace":
            for i in range(3):
                m[i][i] += c
        return m
    return g


# =====================================================================
# battery instrument 2: the polarization decomposer
# =====================================================================

def polarization_channels(dg, n):
    """Frobenius-orthogonal split of a symmetric perturbation dg
    against propagation direction n: returns (longitudinal, vector,
    transverse-trace, TT) Frobenius amplitudes, with
    |dg|^2 = L^2 + V^2 + Ttr^2 + TT^2."""
    L = sum(n[i] * dg[i][j] * n[j] for i in range(3) for j in range(3))
    dgn = [sum(dg[i][j] * n[j] for j in range(3)) for i in range(3)]
    V = [dgn[i] - n[i] * L for i in range(3)]
    Vn = math.sqrt(2 * sum(v * v for v in V))
    P = [[(1 if i == j else 0) - n[i] * n[j] for j in range(3)]
         for i in range(3)]
    T = [[sum(P[i][a] * dg[a][b] * P[b][j]
              for a in range(3) for b in range(3))
          for j in range(3)] for i in range(3)]
    trT = T[0][0] + T[1][1] + T[2][2]
    Ttr = abs(trT) / math.sqrt(2)
    TT = [[T[i][j] - 0.5 * trT * P[i][j] for j in range(3)]
          for i in range(3)]
    TTn = math.sqrt(sum(TT[i][j] ** 2
                        for i in range(3) for j in range(3)))
    return abs(L), Vn, Ttr, TTn


# =====================================================================
# battery instrument 3: general string-shape retarded metric
# =====================================================================

def travel_pos(zp, t, A=A_W):
    return (A * math.sin(K_W * zp - OM_W * t), 0.0, zp)


def standing_pos(zp, t, A=A_W):
    return (A * math.sin(K_W * zp) * math.cos(OM_W * t), 0.0, zp)


def string_wave_metric(spos, t_obs, w=W_W):
    """Retarded nearest-point channel metric for an arbitrary string
    shape spos(zp, t) -> point (same rule as 0031, generalized)."""
    def ret_dist(x, zp):
        lo, hi = t_obs - (math.dist(x, (0, 0, zp)) + 3.0), t_obs
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            s = spos(zp, mid)
            if (t_obs - mid) - math.dist(x, s) > 0:
                lo = mid
            else:
                hi = mid
        s = spos(zp, 0.5 * (lo + hi))
        return math.dist(x, s), s

    def g(x):
        zc = x[2]
        best, bz = None, None
        for i in range(41):
            zp = zc - 2.0 + 4.0 * i / 40
            d, _ = ret_dist(x, zp)
            if best is None or d < best:
                best, bz = d, zp
        a, b = bz - 0.15, bz + 0.15
        gr = (math.sqrt(5) - 1) / 2
        c = b - gr * (b - a)
        d2 = a + gr * (b - a)
        fc = ret_dist(x, c)[0]
        fd = ret_dist(x, d2)[0]
        for _ in range(45):
            if fc < fd:
                b, d2, fd = d2, c, fc
                c = b - gr * (b - a)
                fc = ret_dist(x, c)[0]
            else:
                a, c, fc = c, d2, fd
                d2 = a + gr * (b - a)
                fd = ret_dist(x, d2)[0]
        dist, s = ret_dist(x, 0.5 * (a + b))
        u = ((s[0] - x[0]) / dist, (s[1] - x[1]) / dist,
             (s[2] - x[2]) / dist)
        return [[(1 if i == j else 0) + w * u[i] * u[j]
                 for j in range(3)] for i in range(3)]
    return g


# =====================================================================
# 1. the discriminators
# =====================================================================

def mode_scaling(kind):
    """Amplitude-scaling exponent of the Ricci response of a plane-
    wave mode; None means identically zero."""
    pt = (0.3, 0.2, 0.4)
    r1 = abs(ricci_scalar(mode_metric(1e-2, kind), pt))
    r2 = abs(ricci_scalar(mode_metric(1e-3, kind), pt))
    if r1 < 1e-12 and r2 < 1e-12:
        return None
    return math.log(max(r1, 1e-30) / max(r2, 1e-30)) / math.log(10)


def verify_discriminators() -> None:
    print("    plane-wave modes through the validated pipeline;")
    print("    Ricci amplitude scaling in eps (1e-2 vs 1e-3):")
    results = {}
    for kind in ("TT", "scalar", "trace", "vector"):
        s = mode_scaling(kind)
        results[kind] = s
        label = "identically zero" if s is None else f"exponent {s:.2f}"
        print(f"      {kind:7s} {label}")
    assert abs(results["TT"] - 2.0) < 0.05, results["TT"]
    assert abs(results["scalar"] - 1.0) < 0.05, results["scalar"]
    assert abs(results["trace"] - 1.0) < 0.05, results["trace"]
    assert results["vector"] is None
    print()
    print("  THE DISCRIMINATORS: a TT wave has ZERO spatial Ricci at")
    print("  linear order (quadratic only); scalar/trace waves show")
    print("  up linearly; a vector plane wave not at all.  Einstein")
    print("  radiation is invisible to the linear Ricci scalar --")
    print("  so any linear-order Ricci wave is already non-Einstein,")
    print("  and the polarization question must be asked of the")
    print("  METRIC wave itself (s2).")


# =====================================================================
# 2. the polarization of the web's wave
# =====================================================================

def web_polarization(R, nph=12):
    """RMS Frobenius amplitude per polarization channel of the web's
    far-field metric wave at (0, R, 0.3), n = (0, 1, 0)."""
    n = (0.0, 1.0, 0.0)
    pt = (0.0, R, 0.3)
    gs = [string_wave_metric(travel_pos, (k / nph) * PERIOD)(pt)
          for k in range(nph)]
    mean = [[sum(g[i][j] for g in gs) / nph for j in range(3)]
            for i in range(3)]
    acc = [0.0] * 4
    for g in gs:
        dg = [[g[i][j] - mean[i][j] for j in range(3)]
              for i in range(3)]
        c = polarization_channels(dg, n)
        for i in range(4):
            acc[i] += c[i] ** 2 / nph
    return [math.sqrt(a) for a in acc]


def verify_polarization() -> None:
    chans = {}
    for R in (3.0, 6.0):
        L, V, Ttr, TTn = web_polarization(R)
        chans[R] = (L, V, Ttr, TTn)
        pred = W_W * A_W / R
        print(f"    R = {R}: long {L:.2e}  VECTOR {V:.2e}  "
              f"trace {Ttr:.2e}  TT {TTn:.2e}")
        print(f"           predicted vector amplitude "
              f"w A / R = {pred:.2e}")
        assert abs(V - pred) / pred < 0.02, (V, pred)
        for other in (L, Ttr, TTn):
            assert other < 0.02 * V, (other, V)
    # second-order channels fall as 1/R^2, the vector as 1/R
    assert abs(chans[3.0][1] / chans[6.0][1] - 2.0) < 0.05
    for i in (0, 2, 3):
        ratio = chans[3.0][i] / chans[6.0][i]
        assert ratio > 3.0, (i, ratio)
    print()
    # the vector channel oscillates at the FUNDAMENTAL
    nph = 12
    series = [string_wave_metric(travel_pos,
                                 (k / nph) * PERIOD)((0.0, 6.0, 0.3))[0][1]
              for k in range(nph)]
    m = sum(series) / nph
    h1, _ = harmonic([v - m for v in series], 1)
    h2, _ = harmonic([v - m for v in series], 2)
    assert h1 > 1e6 * h2, (h1, h2)
    print(f"    the vector channel (g_xy) oscillates at the")
    print(f"    fundamental: |H1|/|H2| = {h1 / max(h2, 1e-300):.0e}.")
    # coherence: the Ricci wave is QUADRATIC in the wiggle amplitude
    pt = (0.0, 4.0, 0.3)
    amps = []
    for A in (0.05, 0.1):
        pos = lambda zp, t, A=A: travel_pos(zp, t, A)
        vals = [ricci_scalar(string_wave_metric(pos, (k / 8) * PERIOD),
                             pt, h=2e-3) for k in range(8)]
        amps.append((max(vals) - min(vals)) / 2)
    q = math.log(amps[1] / amps[0]) / math.log(2)
    assert 1.7 < q < 2.1, q
    print(f"    the Ricci wave is quadratic in the wiggle amplitude")
    print(f"    (exponent {q:.2f}) at 2 Om -- as it must be: the")
    print(f"    linear wave is vector, and s1 showed a vector wave")
    print(f"    carries no linear Ricci.")
    print()
    print("  THE WEB'S WAVE IS PURE VECTOR: amplitude w A / R exactly")
    print("  (< 1%), at the fundamental; TT, longitudinal and trace")
    print("  are all second order (1/R^2, ~1% at R = 3).  Einstein")
    print("  gravity FORBIDS a propagating vector polarization; its")
    print("  TT channel is exactly the one the web only produces at")
    print("  second order.")


# =====================================================================
# 3. traveling vs standing
# =====================================================================

def wave_amplitudes(spos, radii=(2.0, 4.0, 8.0), nph=8):
    out = []
    for R in radii:
        pt = (0.0, R, 0.3)
        vals = [ricci_scalar(string_wave_metric(spos,
                                                (k / nph) * PERIOD),
                             pt, h=2e-3) for k in range(nph)]
        out.append((max(vals) - min(vals)) / 2)
    return out


def verify_traveling_vs_standing() -> None:
    print("    GR (literature import): a traveling wave on a string")
    print("    is an EXACT non-radiating solution (Vachaspati 1986;")
    print("    Garfinkle 1990); standing waves radiate.  The web:")
    amps = {}
    for name, pos in (("traveling", travel_pos),
                      ("standing", standing_pos)):
        row = wave_amplitudes(pos)
        amps[name] = row
        p = math.log(row[2] / row[0]) / math.log(4.0)
        print(f"      {name:9s} Ricci amps " +
              ", ".join(f"{a:.2e}" for a in row) +
              f"  (exponent {p:.2f})")
        assert -1.25 < p < -0.8, p
    ratio = amps["traveling"][1] / amps["standing"][1]
    assert 2.0 < ratio < 6.0, ratio
    print(f"    traveling/standing amplitude at R = 4: {ratio:.1f}x")
    print()
    print("  BOTH radiate at 1/R, and the traveling wave -- exactly")
    print("  silent in GR -- is the STRONGER emitter.  The web does")
    print("  not reproduce GR's selection rule for string radiation.")


# =====================================================================
# 4. the verdict
# =====================================================================

def verify_verdict() -> None:
    print("  CORRESPONDENCE FAILS AT LINEAR ORDER -- and the failure")
    print("  is localized.  What propagates is the direction field u:")
    print("  the only unfrozen piece of g = I + w u u^T once |u| = 1")
    print("  slaves the channel and w is frozen.  That gives a vector")
    print("  wave (measured: w A / R, fundamental); Einstein's TT")
    print("  modes would have to live in a PROPAGATING STRENGTH")
    print("  TENSOR, and nothing propagates there -- TT appears only")
    print("  as the vector wave's second-order composite.")
    print()
    print("  The gap converges with three independent 2+1 diagnoses")
    print("  of the SAME object: the compass anomaly (0023), the")
    print("  necessity of the boosted baseline (0024), and the in-")
    print("  model Michelson-Morley (0025) all demanded strength-")
    print("  tensor structure beyond unit channels -- and the Lorentz")
    print("  completion (0024) already built its kinematic form: the")
    print("  m m^T channel with a boosted baseline.  The web-native")
    print("  content of Plebanski's simplicity constraint is now a")
    print("  sharp program: make the strength sector dynamical and")
    print("  check that its radiative modes are the two TT gravitons.")


def run_verification_suite() -> None:
    sections = [
        ("The discriminators (what GR waves look like to the "
         "instrument)", verify_discriminators),
        ("The polarization of the web's wave", verify_polarization),
        ("Traveling vs standing", verify_traveling_vs_standing),
        ("The verdict", verify_verdict),
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
