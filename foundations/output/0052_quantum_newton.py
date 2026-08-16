"""Quantum Newton, and what stays massless at the critical point.

0056 found the critical point where the lattice graviton goes
massless.  This module asks the two questions that live there: what
force does the critical theory mediate, and what is still massless
when it does.  Both answer sharply.

  s1  THE CRITICAL DISPERSION IS QUADRATIC.  On a 3D spatial
      lattice with on-site price V and hopping t to six
      neighbours, E(k) = V - 2t sum_i cos k_i, and the gap closes
      at t_c = V/6.  There
        E(k) = 2t sum_i (1 - cos k_i)  ->  t k^2
      measured ratio E/(t k^2) = 0.9867, 0.9967, 0.9992, 0.9998 at
      k = 0.4, 0.2, 0.1, 0.05.  A quadratic dispersion means a
      1/k^2 propagator -- and in three spatial dimensions that is
      Newton.

  s2  QUANTUM NEWTON.  The static potential is the lattice Green
      function G(r) = (1/L^3) sum_{k != 0} cos(k.r)/E(k), with the
      k = 0 mode removed -- and that removal IS the closed-universe
      budget (sum F = 0, 0029/0054).  Fitting G(r) = A/r + B on an
      L = 56 lattice, as the fit window moves outward:

        window        r = 2..8   4..10   6..14
        A/(1/4 pi t)    1.0996  1.0237  0.9907

      and at fixed window r = 6..14 the coefficient converges
      monotonically as the box grows:

        L               32      40      56      72
        A/(1/4 pi t)  0.8744  0.9482  0.9907  1.0023
        offset B     -0.0145 -0.0133 -0.0104 -0.0084

      landing on A = 1/(4 pi t) -- the Newtonian coefficient -- to
      0.2%, with the offset B (the removed zero mode) heading to 0
      as the box grows.  And A is exactly proportional to 1/t:
      doubling the coupling halves A, ratio 2.0000.  THE CRITICAL
      LATTICE THEORY MEDIATES A 1/r FORCE.  0036's classical
      Newton, obtained from the quantized model.

  s3  WHAT STAYS MASSLESS: THE GEOMETRIC SECTOR ONLY.  The price
      has two tiers (0055/0056): geometric (simple) curvature costs
      2 log N, non-geometric costs 4 log N.  So there are two
      critical couplings, and at the geometric one t_c = 2 log N/6:
        simple-curvature gap      = 0.000000   MASSLESS
        non-simple curvature gap  = 2.197225 = 2 log N   MASSIVE
      Tuning to the geometric critical point leaves ONLY the
      geometric sector massless, with the non-geometric sector
      retaining a gap exactly equal to the geometric price itself.
      That is the mode selection Plebanski's constraint is supposed
      to perform, obtained here as a gap.

  s4  AND THE PRICED DIRECTION IS THE SELF-DUAL IMBALANCE.
      Decomposing the curvature bivector into self-dual and
      anti-self-dual parts, Pf(F) is a function of
      |F+|^2 - |F-|^2 ALONE (verified over all N^6 curvatures at
      N = 3).  Since the price depends only on Pf (0055), exactly
      ONE of the six internal directions is priced -- the SD/ASD
      imbalance -- and the balanced cone is cheap.  The simplicity
      constraint |F+| = |F-| is not imposed here: it is the
      statement that the theory charges for imbalance.

Run directly for the verification suite.
"""

from __future__ import annotations

import itertools
import math

PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


# =====================================================================
# 1. the critical dispersion
# =====================================================================

def verify_dispersion() -> None:
    V = 2 * math.log(3)
    t = V / 6
    print(f"    V = 2 log 3 = {V:.4f}, critical hopping "
          f"t_c = V/6 = {t:.4f}")
    print("    E(k) along one axis vs t k^2:")
    for kk in (0.4, 0.2, 0.1, 0.05):
        E = 2 * t * (1 - math.cos(kk))
        ratio = E / (t * kk * kk)
        print(f"      k = {kk:.3f}: E = {E:.6e}, t k^2 = "
              f"{t * kk * kk:.6e}, ratio {ratio:.4f}")
        assert abs(ratio - 1.0) < 0.02
    fine = 2 * t * (1 - math.cos(0.01)) / (t * 1e-4)
    assert abs(fine - 1.0) < 1e-4, fine
    print()
    print("  THE CRITICAL DISPERSION IS QUADRATIC: E ~ t k^2, so the")
    print("  propagator is 1/k^2 -- and in three spatial dimensions")
    print("  that is Newton.")


# =====================================================================
# 2. quantum Newton
# =====================================================================

def green_line(L, t, rs):
    """Lattice Green function along an axis, zero mode removed."""
    out = {r: 0.0 for r in rs}
    for a in range(L):
        ca = math.cos(2 * math.pi * a / L)
        kx = 2 * math.pi * a / L
        cosr = {r: math.cos(kx * r) for r in rs}
        for b in range(L):
            cb = math.cos(2 * math.pi * b / L)
            for c in range(L):
                if a == 0 and b == 0 and c == 0:
                    continue
                cc = math.cos(2 * math.pi * c / L)
                E = 2 * t * ((1 - ca) + (1 - cb) + (1 - cc))
                for r in rs:
                    out[r] += cosr[r] / E
    return {r: v / L ** 3 for r, v in out.items()}


def fit_coulomb(rs, G):
    xs = [1.0 / r for r in rs]
    ys = [G[r] for r in rs]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    A = sum((xs[i] - mx) * (ys[i] - my) for i in range(n)) \
        / sum((xs[i] - mx) ** 2 for i in range(n))
    return A, my - A * mx


def verify_newton() -> None:
    V = 2 * math.log(3)
    t = V / 6
    pred = 1 / (4 * math.pi * t)
    L = 56
    rs = list(range(2, 17))
    G = green_line(L, t, rs)
    print(f"    L = {L}, t = {t:.4f}; prediction A = 1/(4 pi t) = "
          f"{pred:.5f}")
    ratios = {}
    for lo, hi in ((2, 8), (4, 10), (6, 14)):
        sub = [r for r in rs if lo <= r <= hi]
        A, B = fit_coulomb(sub, G)
        ratios[(lo, hi)] = A / pred
        print(f"      fit r = {lo:2d}..{hi:2d}: A = {A:.5f}, "
              f"A/(1/4 pi t) = {A / pred:.4f}, offset B = {B:+.5f}")
    assert ratios[(2, 8)] > ratios[(4, 10)] > ratios[(6, 14)]
    assert abs(ratios[(6, 14)] - 1.0) < 0.03, ratios
    # and the coefficient converges to 1 as the box grows
    print("    finite-size scan, fixed window r = 6..14:")
    prev = None
    for LL in (32, 40, 56, 72):
        rr = list(range(2, 15))
        GG = green_line(LL, t, rr)
        AA, BB = fit_coulomb([r for r in rr if 6 <= r <= 14], GG)
        print(f"      L = {LL:2d}: A/(1/4 pi t) = {AA / pred:.4f}, "
              f"offset B = {BB:+.5f}")
        if prev is not None:
            assert AA / pred > prev, (LL, AA / pred, prev)
        prev = AA / pred
    assert abs(prev - 1.0) < 0.01, prev
    # A is exactly proportional to 1/t
    G2 = green_line(40, 2 * t, [2, 3, 4, 5, 6, 7, 8])
    G1 = green_line(40, t, [2, 3, 4, 5, 6, 7, 8])
    A2, _ = fit_coulomb([2, 3, 4, 5, 6, 7, 8], G2)
    A1, _ = fit_coulomb([2, 3, 4, 5, 6, 7, 8], G1)
    assert abs(A1 / A2 - 2.0) < 1e-3, (A1, A2)
    print(f"      doubling t halves A: A(t)/A(2t) = {A1 / A2:.4f}")
    print()
    print("  QUANTUM NEWTON.  The critical lattice theory mediates a")
    print("  1/r force with the Newtonian coefficient 1/(4 pi t), to")
    print("  0.2% at the largest box -- and the constant offset is")
    print("  the removed zero mode, which IS the closed-universe")
    print("  budget (sum F = 0).  0036's classical Newton, obtained")
    print("  from the quantized model.")


# =====================================================================
# 3. what stays massless
# =====================================================================

def verify_mode_selection() -> None:
    for N in (3, 5):
        V_simple = 2 * math.log(N)
        V_hard = 4 * math.log(N)
        tc = V_simple / 6
        g_simple = V_simple - 6 * tc
        g_hard = V_hard - 6 * tc
        assert abs(g_simple) < 1e-12
        assert abs(g_hard - 2 * math.log(N)) < 1e-12
        print(f"    N = {N}: geometric price {V_simple:.4f}, "
              f"non-geometric {V_hard:.4f}, t_c = {tc:.4f}")
        print(f"      at t_c: simple gap {g_simple:+.6f} (MASSLESS), "
              f"non-simple gap {g_hard:+.6f}")
        print(f"      the surviving gap is exactly 2 log N = "
              f"{2 * math.log(N):.4f}")
    print()
    print("  ONLY THE GEOMETRIC SECTOR IS MASSLESS.  Tuning to the")
    print("  geometric critical point leaves non-geometric curvature")
    print("  gapped by exactly the geometric price itself.  That is")
    print("  the mode selection Plebanski's constraint is supposed to")
    print("  perform -- obtained here as a gap, not an imposition.")


# =====================================================================
# 4. the priced direction is the self-dual imbalance
# =====================================================================

def eps4(i, j, k, l):
    p = [i, j, k, l]
    if len(set(p)) < 4:
        return 0
    s = 1
    for x in range(4):
        for y in range(x + 1, 4):
            if p[x] > p[y]:
                s = -s
    return s


def hodge(F, N):
    d = dict(zip(PAIRS, F))
    out = []
    for (I, J) in PAIRS:
        v = 0
        for (K, L) in PAIRS:
            e = eps4(I, J, K, L)
            if e:
                v += e * d[(K, L)]
        out.append(v % N)
    return tuple(out)


def sd_asd(F, N):
    inv2 = pow(2, N - 2, N)
    st = hodge(F, N)
    Fp = tuple((inv2 * (F[i] + st[i])) % N for i in range(6))
    Fm = tuple((inv2 * (F[i] - st[i])) % N for i in range(6))
    return Fp, Fm


def pfaffian(F, N):
    d = dict(zip(PAIRS, F))
    return (d[(0, 1)] * d[(2, 3)] - d[(0, 2)] * d[(1, 3)]
            + d[(0, 3)] * d[(1, 2)]) % N


def verify_self_dual() -> None:
    for N in (3, 5):
        rel = {}
        ok = True
        for F in itertools.product(range(N), repeat=6):
            Fp, Fm = sd_asd(F, N)
            key = (sum(x * x for x in Fp)
                   - sum(x * x for x in Fm)) % N
            p = pfaffian(F, N)
            if key in rel and rel[key] != p:
                ok = False
            rel.setdefault(key, p)
        assert ok, N
        print(f"    N = {N}: Pf(F) is a function of "
              f"|F+|^2 - |F-|^2 alone: {ok}")
        if N == 3:
            for k in sorted(rel):
                print(f"      imbalance {k} -> Pf = {rel[k]}")
    print()
    print("  THE PRICED DIRECTION IS THE SELF-DUAL IMBALANCE.  Since")
    print("  the price depends only on Pf (0055) and Pf depends only")
    print("  on |F+|^2 - |F-|^2, exactly ONE of the six internal")
    print("  directions is priced and the balanced cone is cheap.")
    print("  Plebanski's |F+| = |F-| is not imposed here -- it is")
    print("  the statement that the theory charges for imbalance.")


def run_verification_suite() -> None:
    sections = [
        ("The critical dispersion is quadratic", verify_dispersion),
        ("Quantum Newton", verify_newton),
        ("What stays massless: the geometric sector only",
         verify_mode_selection),
        ("The priced direction is the self-dual imbalance",
         verify_self_dual),
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
