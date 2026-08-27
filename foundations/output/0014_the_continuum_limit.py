"""The continuum limit: fuzzing the atoms into an Einstein equation.

O2 of the curvature thread, pressed from both ends at once.

  FRAMING A (limit of points): scatter N weak channels, total
  participation strength S fixed, and let N grow.
  FRAMING B (fuzzing): replace the point source by a DISTRIBUTION --
  the channel field is averaged over a density rho, no points at
  all.  The conjecture: both arrive at the same place.

  s1  THE ATOM OF A WEIGHTED CHANNEL.  A lone channel of strength w
      in ambient I is an EXACT cone: delta(w) = 2pi(1 - 1/sqrt(1+w))
      (verified against honest transport).  Weak law: delta -> pi*w
      as w -> 0 (with first correction -3w/4).  Saturation:
      delta -> 2pi as w -> infinity -- a single channel can approach
      but never exceed the EXTREMAL defect (0012's per-defect mass
      bound m < 1/4G appears as an asymptote).  And the ambient
      SCREENS: the same weak channel inside ambient information
      I + a e e^T has its atom reduced by a computable factor f(a)
      < 1 -- ambient information renormalizes the local coupling.

  s2  FUZZING DISSOLVES THE ATOM.  One Gaussian-fuzzed source
      (width sigma, total strength S): the transport profile T(R)
      interpolates from ~0 deep inside (no atom left; curvature at
      the centre is FINITE) to the point atom delta(S) outside --
      the exterior cannot tell fuzz from point (the shell property).
      Inside, T(R) tracks pi * (strength enclosed).

  s3  THE TWO FRAMINGS MEET.  Reference: the continuous-source
      metric computed by per-point polar integration (no
      discretization of the source at all).  Both a deterministic
      quadrature refinement (points -> density) and random clouds
      (sampling the density) converge to the SAME loop transport.

  s4  THE LOCAL LAW.  With the continuous fuzzed metric, pointwise
      Gaussian curvature (Brioschi) against the strength density
      s(x) = S rho(x):  K(x) = pi s(x) in the weak limit, tracking
      the density spatially -- the static Euclidean 2+1 Einstein
      equation K = 8 pi G rho_m with mass density rho_m = s / 8G.
      The finite-S correction is negative, matching s1's screening.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import random
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_o = importlib.import_module("0009_the_sharp_opens")
_f = importlib.import_module("0008_fisher_deficit")

TAU = 2 * math.pi


# =====================================================================
# metrics
# =====================================================================

def weighted_metric(sources):
    """Ambient I plus weighted channel fields: g = I + sum w u u^T."""
    def metric(x, y):
        E, F, G = 1.0, 0.0, 1.0
        for (px, py), w in sources:
            dx, dy = x - px, y - py
            r2 = dx * dx + dy * dy
            E += w * dx * dx / r2
            F += w * dx * dy / r2
            G += w * dy * dy / r2
        return (E, F, G)
    return metric


def point_deficit(w):
    return TAU * (1.0 - 1.0 / math.sqrt(1.0 + w))


def quad_sources(S, sigma, n, cut=4.0):
    """Deterministic quadrature grid for a Gaussian source (the tail
    beyond cut*sigma carries e^{-cut^2/2} of the mass: negligible)."""
    span = 2 * cut * sigma
    pts = []
    for i in range(n):
        for j in range(n):
            x = -cut * sigma + (i + 0.5) * span / n
            y = -cut * sigma + (j + 0.5) * span / n
            r2 = x * x + y * y
            if r2 <= (cut * sigma) ** 2:
                pts.append(((x, y), math.exp(-r2 / (2 * sigma * sigma))))
    total = sum(w for _, w in pts)
    return [(p, S * w / total) for p, w in pts]


def cloud_sources(S, sigma, N, seed):
    """Random cloud sampled from the same Gaussian."""
    rng = random.Random(seed)
    return [((rng.gauss(0, sigma), rng.gauss(0, sigma)), S / N)
            for _ in range(N)]


def fuzz_metric(S, sigma, nth=96, nt=64, reach=6.0):
    """The CONTINUOUS fuzzed-source metric: at each evaluation point
    the channel average E_rho[u u^T] is a polar integral around the
    point (the integrand rho * t is smooth: no singularity), so no
    source discretization enters at any stage."""
    Z = TAU * sigma * sigma

    def metric(x, y):
        E, F, G = 1.0, 0.0, 1.0
        base = math.hypot(x, y) + reach * sigma
        for it in range(nth):
            th = TAU * (it + 0.5) / nth
            c, s = math.cos(th), math.sin(th)
            ray = 0.0
            for jt in range(nt):
                t = base * (jt + 0.5) / nt
                px, py = x + t * c, y + t * s
                r2 = px * px + py * py
                ray += math.exp(-r2 / (2 * sigma * sigma)) * t
            ray *= base / nt
            w = S * ray / Z * (TAU / nth)
            E += w * c * c
            F += w * c * s
            G += w * s * s
        return (E, F, G)
    return metric


def rho_gauss(r, sigma):
    return math.exp(-r * r / (2 * sigma * sigma)) / (TAU * sigma * sigma)


# =====================================================================
# 1. the atom of a weighted channel
# =====================================================================

def screened_atom_factor(a, w=1e-4, steps=40000):
    """delta / (pi w) for a weak channel inside ambient I + a e e^T."""
    total = 0.0
    for s in range(steps):
        phi = TAU * (s + 0.5) / steps
        c, sn = math.cos(phi), math.sin(phi)
        E = 1.0 + a * c * c + w
        B = -a * c * sn
        C = 1.0 + a * sn * sn
        total += math.sqrt(max(E * C - B * B, 0.0)) / E * (TAU / steps)
    return (TAU - total) / (math.pi * w)


def verify_the_atom() -> None:
    # exact cone, verified by honest transport
    for w in (0.1, 0.5, 1.0):
        t = _o.transport_deficit(weighted_metric([((0.0, 0.0), w)]),
                                 0.0, 0.0, 0.5)
        exact = point_deficit(w)
        assert abs(t - exact) < 3e-3, (w, t, exact)
    print("    a lone channel of strength w is an EXACT cone:")
    print("    delta(w) = 2pi(1 - 1/sqrt(1+w)), transport-verified")
    print("    at w = 0.1, 0.5, 1.0.")
    print()
    # weak law and saturation
    for w in (1e-2, 1e-3):
        ratio = point_deficit(w) / (math.pi * w)
        assert abs(ratio - (1 - 0.75 * w)) < 1e-3, (w, ratio)
    print(f"    weak law: delta/(pi w) -> 1 (measured "
          f"{point_deficit(1e-3) / (math.pi * 1e-3):.6f} at w = 1e-3),")
    print(f"    first correction -3w/4.  the atom of participation is")
    print(f"    pi * strength;  m = delta/8piG ~ w/8G.")
    sat = [(w, point_deficit(w)) for w in (1.0, 10.0, 100.0, 1e4)]
    line = " · ".join(f"delta({w:g}) = {d:.3f}" for w, d in sat)
    assert sat[-1][1] < TAU and sat[-1][1] > 0.98 * TAU
    print()
    print(f"    saturation: {line} -> 2pi:")
    print("    one channel approaches but never exceeds the extremal")
    print("    defect -- 0012's per-defect bound m < 1/4G, as an")
    print("    asymptote of a single channel's strength.")
    print()
    factors = [(a, screened_atom_factor(a)) for a in (0.0, 0.25, 0.5, 1.0)]
    assert abs(factors[0][1] - 1.0) < 1e-3
    assert all(f2 < f1 for (_, f1), (_, f2) in zip(factors, factors[1:]))
    print("    ambient screening of a weak atom, delta/(pi w) inside")
    print("    ambient I + a e e^T:")
    print("      " + " · ".join(f"a={a:g}: {f:.4f}" for a, f in factors))
    for a, f in factors[1:]:
        assert abs(f - (1 + a) ** -0.5) < 2e-3, (a, f)
    print("    measured closed form: f(a) = (1+a)^(-1/2), matched to")
    print("    <2e-3 at a = 0.25, 0.5, 1.  (Isotropic ambient cI gives")
    print("    f = 1/c exactly, by algebra: delta = 2pi(1 -")
    print("    (1 + w/c)^(-1/2)) ~ pi w/c.)  Each stiffened ambient")
    print("    direction costs a -1/2 power: ambient information")
    print("    REDUCES the deficit of new participation -- the local")
    print("    coupling is renormalized downward.")


# =====================================================================
# 2. fuzzing dissolves the atom
# =====================================================================

def verify_fuzzing() -> None:
    S, sigma = 0.3, 0.2
    srcs = quad_sources(S, sigma, 24)
    metric = weighted_metric(srcs)
    exact = point_deficit(S)
    print(f"    one Gaussian-fuzzed source, S = {S}, sigma = {sigma}:")
    print(f"    {'R/sigma':>8} {'T(R)':>9} {'pi*S_enc':>9} {'point atom':>11}")
    profile = []
    for R in (0.1, 0.2, 0.3, 0.4, 0.6, 1.0):
        T = _o.transport_deficit(metric, 0.0, 0.0, R, steps=2500)
        enc = sum(w for (px, py), w in srcs
                  if px * px + py * py <= R * R)
        profile.append((R, T, enc))
        print(f"    {R / sigma:>8.2f} {T:>9.4f} {math.pi * enc:>9.4f} "
              f"{exact:>11.4f}")
    interior = [t for _, t, _ in profile[:4]]
    assert all(b > a for a, b in zip(interior, interior[1:]))
    for R, T, _ in profile[-2:]:
        assert abs(T - exact) / exact < 0.02, (R, T, exact)
    assert profile[0][1] < 0.12 * exact
    kc = _f.gaussian_curvature(fuzz_metric(S, sigma), 0.011, 0.007,
                               h=1e-3)
    print()
    print(f"    curvature at the centre (continuous metric):")
    print(f"    K = {kc:.3f} -- FINITE; the apex is gone.")
    print()
    print("  Outside, the fuzz is indistinguishable from the point")
    print("  atom (the shell property: exterior transport matches")
    print("  delta(S) to <2% at R = 3 sigma and 5 sigma).  Inside,")
    print("  T(R) climbs with pi * enclosed strength and no")
    print("  concentrated defect remains.  Matter as a distribution,")
    print("  not a point -- with the same exterior signature.")


# =====================================================================
# 3. the two framings meet
# =====================================================================

def verify_the_meeting() -> None:
    S, sigma, R = 0.3, 0.25, 0.5
    reference = _o.transport_deficit(fuzz_metric(S, sigma), 0.0, 0.0,
                                     R, steps=2000)
    print(f"    continuous-source transport (polar-integral metric,")
    print(f"    no source points at any stage):  T* = {reference:.4f}")
    print()
    print(f"    {'framing':>22} {'param':>8} {'T':>9} {'|T - T*|':>9}")
    quad_err = []
    for n in (8, 14, 22, 36):
        T = _o.transport_deficit(
            weighted_metric(quad_sources(S, sigma, n)), 0.0, 0.0, R,
            steps=2000)
        quad_err.append(abs(T - reference))
        print(f"    {'points (quadrature)':>22} {'n=' + str(n):>8} "
              f"{T:>9.4f} {quad_err[-1]:>9.5f}")
    cloud_err = []
    for N in (16, 64, 256, 1024):
        T = _o.transport_deficit(
            weighted_metric(cloud_sources(S, sigma, N, seed=19 + N)),
            0.0, 0.0, R, steps=2000)
        cloud_err.append(abs(T - reference))
        print(f"    {'cloud (random sample)':>22} {'N=' + str(N):>8} "
              f"{T:>9.4f} {cloud_err[-1]:>9.5f}")
    assert quad_err[-1] < 5e-3, quad_err
    assert quad_err[-1] <= quad_err[0]
    assert cloud_err[-1] < 2e-2, cloud_err
    assert cloud_err[-1] <= cloud_err[0]
    print()
    print("  Refining the point lattice and sampling the density both")
    print("  converge to the continuous-source transport: the limit of")
    print("  points and the fuzzed distribution are the SAME object.")


# =====================================================================
# 4. the local law
# =====================================================================

def verify_the_local_law() -> None:
    sigma = 0.25
    x0r, ang = 0.15, 0.37
    x0 = (x0r * math.cos(ang), x0r * math.sin(ang))
    print(f"    pointwise K (Brioschi on the continuous metric) vs")
    print(f"    pi * s(x),  s = S rho(x),  Gaussian fuzz sigma = {sigma}:")
    print()
    print(f"    weak-field sweep at r = {x0r}:")
    print(f"    {'S':>6} {'K':>10} {'pi*s':>10} {'ratio':>8}")
    ratios = []
    for S in (0.02, 0.05, 0.1, 0.2, 0.4):
        metric = fuzz_metric(S, sigma)
        K = _f.gaussian_curvature(metric, x0[0], x0[1], h=1e-3)
        target = math.pi * S * rho_gauss(x0r, sigma)
        ratios.append((S, K / target))
        print(f"    {S:>6.2f} {K:>10.5f} {target:>10.5f} "
              f"{K / target:>8.4f}")
    assert abs(ratios[0][1] - 1.0) < 0.04, ratios[0]
    assert all(r2 < r1 for (_, r1), (_, r2) in zip(ratios, ratios[1:]))
    slope = (ratios[2][1] - ratios[0][1]) / (0.1 - 0.02)
    print()
    print(f"    K/(pi s) -> 1 as S -> 0; finite-S correction is")
    print(f"    NEGATIVE (d(ratio)/dS ~ {slope:.2f}) -- the screening")
    print(f"    of s1, now at the field level.")
    print()
    S = 0.05
    metric = fuzz_metric(S, sigma)
    print(f"    spatial tracking at S = {S}:")
    print(f"    {'r':>6} {'K':>10} {'pi*s':>10} {'ratio':>8}")
    for r in (0.05, 0.15, 0.30, 0.45):
        x = (r * math.cos(ang), r * math.sin(ang))
        K = _f.gaussian_curvature(metric, x[0], x[1], h=1e-3)
        target = math.pi * S * rho_gauss(r, sigma)
        print(f"    {r:>6.2f} {K:>10.5f} {target:>10.5f} "
              f"{K / target:>8.4f}")
        assert abs(K / target - 1.0) < 0.08, (r, K, target)
    print()
    print("  THE LOCAL LAW:  K(x) = pi s(x) in the weak limit, with")
    print("  curvature tracking the participation density point by")
    print("  point.  Registered through delta = 8 pi G m, this is the")
    print("  static Euclidean 2+1 Einstein equation")
    print("      K = 8 pi G rho_mass,   rho_mass = s / 8G:")
    print("  participation density IS mass density, and the flagged")
    print("  'correlation sources curvature' row becomes an equation.")


def run_verification_suite() -> None:
    sections = [
        ("The atom of a weighted channel", verify_the_atom),
        ("Fuzzing dissolves the atom", verify_fuzzing),
        ("The two framings meet", verify_the_meeting),
        ("The local law", verify_the_local_law),
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
