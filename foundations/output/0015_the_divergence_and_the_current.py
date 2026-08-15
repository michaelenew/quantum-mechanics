"""The divergence and the current: O2 made rigorous, O1 read off the
proof.

  s1  THE PROOF OF K = pi s (linear tier, each step machine-checked).
      (a) EXACT FLATNESS: the weighted cone I + w u u^T is flat off
          the apex at ANY w (polar coefficients constant) -- Brioschi
          K < 1e-8 pointwise at w = 0.7.
      (b) THE DIVERGENCE IDENTITY: linearized curvature is a total
          divergence, K_lin = div V with
            V = (d2 h12 - (1/2) d1 h22,  -(1/2) d2 h11).
          For the point channel, the flux integral is computed by
          finite differences of h alone:  INT V.n ds = pi w for
          every radius -- radius-independence calibrates the
          delta-function: K_lin = pi w delta^2.  Superposition
          (linearity in h) then gives K = pi s for a density.  The
          boundary integral is also done in closed form in the doc:
          V.n = w cos^2(theta)/R, whose circle integral is pi w.
      (c) THE CONSTANT, PINNED: Richardson extrapolation of the
          field-level ratio K/(pi s) at S and S/2 removes the O(S)
          screening term; the extrapolated constant is 1 to <0.5%.
      (d) THE SCREENING LAW, DERIVED AND GENERALIZED: the doc
          derives delta = pi w / sqrt(1+a) exactly (two standard
          circle integrals).  Numerically the general law
            delta = pi w / sqrt(det A0)
          is confirmed for biaxial and rotated (correlated) ambients.
          The local coupling is 1/sqrt(information volume).
      (e) THE TRACE IDENTITY: tr h(x) = S at EVERY point (each
          channel contributes exactly its strength to the trace,
          regardless of distance) -- so the isotropic part of the
          web's field is a global constant, constant SPD is flat,
          and ALL curvature lives in the traceless (anisotropy)
          sector, matching the exchange-rate results.

  s2  THE FIELD-LEVEL NONLINEARITY IS NOT BARE SCREENING (honest
      negative): applying the pointwise atom law delta = pi w /
      sqrt(det A) with the measured local ambient underestimates the
      finite-S correction of 0019 -- gradient terms carry the rest.
      Reported, quantified, open.

  s3  THE CURRENT (O1 + O5 read off the proof).  Because K_lin =
      div V[h] STRUCTURALLY, any time-dependence of the web gives
      dK/dt = div(dV/dt): a curvature continuity equation with
      current J = -dV/dt exists by construction -- the linearized
      Bianchi/conservation pair is free.  Checked concretely:
      (a) a moving point defect changes a loop's transport ONLY on
          crossing (constant to <2e-3 on both sides, jump = the
          atom);
      (b) a moving fuzzed source obeys d/dt INT K = pi d/dt S_enc:
          transport tracks pi * enclosed strength along the whole
          path -- the continuity law  dK/dt + div(pi s v) = 0;
      (c) NO PAIR FORCE: the atom of source 1 is independent of the
          distance to source 2 (constant to <1e-3 over d = 0.5..4)
          -- like 2+1 gravity, no Newtonian attraction; matter moves
          freely, geometry bookkeeps, interaction survives only as
          holonomy/braiding.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_o = importlib.import_module("0009_the_sharp_opens")
_f = importlib.import_module("0008_fisher_deficit")
_cl = importlib.import_module("0014_the_continuum_limit")

TAU = 2 * math.pi


# =====================================================================
# 1. the proof of K = pi s
# =====================================================================

def point_h(w):
    """The channel field h = w u u^T of a unit source at the origin,
    as three component functions."""
    def h11(x, y):
        r2 = x * x + y * y
        return w * x * x / r2

    def h12(x, y):
        r2 = x * x + y * y
        return w * x * y / r2

    def h22(x, y):
        r2 = x * x + y * y
        return w * y * y / r2
    return h11, h12, h22


def flux_integral(h11, h12, h22, R, steps=4000, fd=1e-6):
    """INT V.n ds around the circle of radius R, V built from finite
    differences of h:  V = (d2 h12 - d1 h22 / 2, -d2 h11 / 2)."""
    total = 0.0
    for s in range(steps):
        t = TAU * (s + 0.5) / steps
        x, y = R * math.cos(t), R * math.sin(t)
        d2h12 = (h12(x, y + fd) - h12(x, y - fd)) / (2 * fd)
        d1h22 = (h22(x + fd, y) - h22(x - fd, y)) / (2 * fd)
        d2h11 = (h11(x, y + fd) - h11(x, y - fd)) / (2 * fd)
        v1 = d2h12 - 0.5 * d1h22
        v2 = -0.5 * d2h11
        nx, ny = math.cos(t), math.sin(t)
        total += (v1 * nx + v2 * ny) * R * (TAU / steps)
    return total


def screened_atom_general(amb, w=1e-4, steps=40000):
    """delta/(pi w) for a weak radial channel inside constant ambient
    A0 = I + amb, amb = ((a11, a12), (a12, a22))."""
    (a11, a12), (_, a22) = amb
    total = 0.0
    for s in range(steps):
        phi = TAU * (s + 0.5) / steps
        c, sn = math.cos(phi), math.sin(phi)
        # polar components of A0 = I + amb
        E0 = 1 + a11 * c * c + 2 * a12 * c * sn + a22 * sn * sn
        B0 = (a22 - a11) * c * sn + a12 * (c * c - sn * sn)
        C0 = 1 + a11 * sn * sn - 2 * a12 * c * sn + a22 * c * c
        E = E0 + w
        total += math.sqrt(max(E * C0 - B0 * B0, 0.0)) / E \
            * (TAU / steps)
    return (TAU - total) / (math.pi * w)


def verify_the_proof() -> None:
    # (a) exact flatness off the apex
    w = 0.7
    metric = _cl.weighted_metric([((0.0, 0.0), w)])
    worst = max(abs(_f.gaussian_curvature(metric, x, y, h=1e-4))
                for x, y in ((0.4, 0.1), (-0.2, 0.5), (1.1, -0.7)))
    assert worst < 1e-6, worst
    print(f"    (a) the weighted cone is flat off the apex: |K| < "
          f"{worst:.1e}")
    print(f"        at w = 0.7 (polar coefficients are constant --")
    print(f"        exact, not approximate, flatness at any w).")
    print()
    # (b) the divergence identity and the flux calibration
    h11, h12, h22 = point_h(0.2)
    print(f"    (b) K_lin = div V;  flux INT V.n ds by finite")
    print(f"        differences of h alone (target pi w = "
          f"{math.pi * 0.2:.6f}):")
    for R in (0.3, 1.0, 3.0):
        fl = flux_integral(h11, h12, h22, R)
        assert abs(fl - math.pi * 0.2) < 1e-4, (R, fl)
        print(f"          R = {R:<4}  flux = {fl:.6f}")
    print(f"        radius-independent = the delta is calibrated:")
    print(f"        K_lin = pi w delta^2, so superposition gives")
    print(f"        K = pi s(x) for any density.  (Closed form:")
    print(f"        V.n = w cos^2/R, and INT cos^2 = pi.)")
    print()
    # (c) Richardson: kill the O(S) term, read the constant
    sigma, r0, ang = 0.25, 0.15, 0.37
    x0 = (r0 * math.cos(ang), r0 * math.sin(ang))
    ratios = {}
    for S in (0.01, 0.02):
        K = _f.gaussian_curvature(_cl.fuzz_metric(S, sigma),
                                  x0[0], x0[1], h=1e-3)
        ratios[S] = K / (math.pi * S * _cl.rho_gauss(r0, sigma))
    extrap = 2 * ratios[0.01] - ratios[0.02]
    assert abs(extrap - 1.0) < 5e-3, (ratios, extrap)
    print(f"    (c) the constant, pinned: K/(pi s) = "
          f"{ratios[0.02]:.4f} (S = 0.02),")
    print(f"        {ratios[0.01]:.4f} (S = 0.01); Richardson "
          f"extrapolation -> {extrap:.4f}.")
    print(f"        The weak-limit constant is pi to <0.5%.")
    print()
    # (d) the screening law, generalized
    cases = [
        ("uniaxial a=0.5", ((0.5, 0.0), (0.0, 0.0)), 1.5),
        ("biaxial a=0.5 b=0.3", ((0.5, 0.0), (0.0, 0.3)), 1.5 * 1.3),
        ("rotated/correlated", ((0.35, 0.21), (0.21, 0.45)),
         1.35 * 1.45 - 0.21 * 0.21),
    ]
    print(f"    (d) the screening law  delta = pi w / sqrt(det A0):")
    for name, amb, det in cases:
        f = screened_atom_general(amb)
        pred = det ** -0.5
        assert abs(f - pred) < 2e-3, (name, f, pred)
        print(f"          {name:<22} measured {f:.4f}   "
              f"1/sqrt(det) {pred:.4f}")
    print(f"        (uniaxial case derived exactly in the doc; the")
    print(f"        general det law measured to <2e-3.)  The local")
    print(f"        coupling is 1/sqrt(information volume).")
    print()
    # (e) the trace identity
    srcs = _cl.quad_sources(0.3, 0.2, 24)
    metric = _cl.weighted_metric(srcs)
    S_tot = sum(wt for _, wt in srcs)
    worst = 0.0
    for x, y in ((0.1, 0.05), (0.5, -0.3), (2.0, 1.0)):
        E, F, G = metric(x, y)
        worst = max(worst, abs((E + G - 2) - S_tot))
    assert worst < 1e-12, worst
    print(f"    (e) the trace identity: tr h(x) = S_total at every")
    print(f"        point (max dev {worst:.1e}) -- each channel puts")
    print(f"        its whole strength into the trace at any")
    print(f"        distance.  The isotropic part is a global")
    print(f"        constant (and constant SPD is flat), so ALL")
    print(f"        curvature lives in the traceless anisotropy")
    print(f"        sector -- the field-level form of 'the deficit")
    print(f"        is anisotropy-priced'.")


# =====================================================================
# 2. the field nonlinearity is not bare screening
# =====================================================================

def verify_not_bare_screening() -> None:
    sigma, r0, ang = 0.25, 0.15, 0.37
    x0 = (r0 * math.cos(ang), r0 * math.sin(ang))
    print(f"    measured K/(pi s) vs the bare pointwise prediction")
    print(f"    1/sqrt(det A(x)) with the ambient read off the field:")
    print(f"    {'S':>6} {'measured':>10} {'bare screening':>15}")
    rows = []
    for S in (0.1, 0.2, 0.4):
        metric = _cl.fuzz_metric(S, sigma)
        E, F, G = metric(x0[0], x0[1])
        det = E * G - F * F
        K = _f.gaussian_curvature(metric, x0[0], x0[1], h=1e-3)
        meas = K / (math.pi * S * _cl.rho_gauss(r0, sigma))
        rows.append((meas, det ** -0.5))
        print(f"    {S:>6.2f} {meas:>10.4f} {det ** -0.5:>15.4f}")
    assert all(m < p for m, p in rows)
    print()
    print("  The bare atom law under-corrects at every S: the finite-")
    print("  strength deviation is carried partly by GRADIENTS of the")
    print("  ambient, not by its pointwise value alone.  The exact")
    print("  nonlinear law remains open -- but bounded between the")
    print("  measured curve and the bare-screening one.")


# =====================================================================
# 3. the current
# =====================================================================

def verify_the_current() -> None:
    # (a) point defect crossing a loop
    w, R = 0.08, 1.0
    atom = _cl.point_deficit(w)
    print(f"    (a) moving point defect (w = {w}), loop R = {R}:")
    print(f"        {'source x':>9} {'T(loop)':>9}")
    outside, inside = [], []
    for cx in (-1.6, -1.25, -0.6, -0.25, 0.3, 1.3, 1.7):
        metric = _cl.weighted_metric([((cx, 0.13), w)])
        T = _o.transport_deficit(metric, 0.0, 0.0, R, steps=3000)
        (inside if abs(cx) < 0.95 else outside).append(T)
        print(f"        {cx:>9.2f} {T:>9.5f}")
    assert all(t < 2e-3 for t in outside), outside
    assert all(abs(t - atom) < 2e-3 for t in inside), (inside, atom)
    print(f"        constant 0 outside, constant {atom:.5f} (= the")
    print(f"        atom) inside: INT K over the region changes ONLY")
    print(f"        when a participant crosses the boundary.")
    print()
    # (b) continuity for a moving fuzzed source
    S, sigma, R = 0.05, 0.2, 0.6
    srcs0 = _cl.quad_sources(S, sigma, 24)
    print(f"    (b) moving fuzzed source (S = {S}, sigma = {sigma}),")
    print(f"        loop R = {R}: transport vs pi * enclosed strength:")
    print(f"        {'centre':>7} {'T':>9} {'pi*S_enc':>9}")
    for c in (0.0, 0.3, 0.5, 0.7, 0.9, 1.2):
        srcs = [((px + c, py), wt) for (px, py), wt in srcs0]
        metric = _cl.weighted_metric(srcs)
        T = _o.transport_deficit(metric, 0.0, 0.0, R, steps=2500)
        enc = sum(wt for (px, py), wt in srcs
                  if px * px + py * py <= R * R)
        assert abs(T - math.pi * enc) < 0.012, (c, T, enc)
        print(f"        {c:>7.2f} {T:>9.5f} {math.pi * enc:>9.5f}")
    print(f"        d/dt INT K = pi d/dt S_enc along the whole path:")
    print(f"        the continuity law dK/dt + div(pi s v) = 0, with")
    print(f"        the current READ OFF THE PROOF: K_lin = div V[h]")
    print(f"        makes dK/dt = div(dV/dt) an identity -- the")
    print(f"        linearized Bianchi/conservation pair is free.")
    print()
    # (c) no pair force
    w1, w2 = 0.02, 0.5
    vals = []
    for d in (0.5, 1.0, 2.0, 4.0):
        metric = _cl.weighted_metric([((0.0, 0.0), w1), ((d, 0.0), w2)])
        T = _o.transport_deficit(metric, 0.0, 0.0, 0.04, steps=3000)
        vals.append(T)
    spread = (max(vals) - min(vals)) / vals[0]
    pred = math.pi * w1 / math.sqrt(1 + w2)
    print(f"    (c) atom of source 1 vs distance to source 2")
    print(f"        (w1 = {w1}, w2 = {w2}):")
    print(f"        d = 0.5..4:  T = " +
          ", ".join(f"{t:.6f}" for t in vals))
    print(f"        relative spread {spread:.1e}; screened prediction")
    print(f"        pi w1/sqrt(1+w2) = {pred:.6f}.")
    assert spread < 2e-3, spread
    assert abs(vals[-1] - pred) / pred < 0.02, (vals[-1], pred)
    print()
    print("  NO PAIR FORCE: a partner's distance does not change your")
    print("  atom (its det-screening is distance-blind), so nothing")
    print("  pulls -- exactly the 2+1 situation.  Dynamics is matter's")
    print("  own movie; geometry responds by redistribution with a")
    print("  conserved current, and the surviving interaction is")
    print("  holonomy (masses add, centres braid).")


def run_verification_suite() -> None:
    sections = [
        ("The proof of K = pi s", verify_the_proof),
        ("The field nonlinearity is not bare screening",
         verify_not_bare_screening),
        ("The current", verify_the_current),
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
