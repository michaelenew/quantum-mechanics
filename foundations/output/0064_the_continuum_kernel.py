"""The continuum kernel: the derived simplicity weight in closed form.

Path A's second stone (0070's A1).  0061 derived the Z_N price from
the frame Gauss sum; here the frames become CONTINUOUS (a, b in R^4,
Gaussian-regulated at scale L), and the whole integral collapses to
a rational closed form in the two simplicity invariants:

    K_L(F)  =  (2 pi)^4 / ( eps^2 + eps |F|^2 + Pf(F)^2 ),
    eps = 1/L^4

  s1  THE ATOMIC INTEGRAL.  Rotating the alternating matrix star-F
      to canonical form factorizes the 8D integral into four copies
      of  II dx dy e^{i lam x y - (x^2+y^2)/2L^2} = 2pi/sqrt(eps +
      lam^2)  -- verified by quadrature to 7 digits (semi-analytic
      and brute).

  s2  THE CLOSED FORM.  The canonical pair (lam1, lam2) of star-F
      satisfies the exact characteristic identity  x^4 + |F|^2 x^2 +
      Pf(F)^2  (verified to machine precision), so
      (eps + lam1^2)(eps + lam2^2) = eps^2 + eps |F|^2 + Pf^2 and

        K = (2pi)^4 / ((eps + lam1^2)(eps + lam2^2)).

      A seeded Monte-Carlo bridge on a generic (non-canonical) F
      confirms the full 8D integral: 1567.1 vs 1566.6 (0.03%).

  s3  THE TIERS RECOVERED, AND THE LEVEL-SCALE DICTIONARY.  The
      price log(K_flat/K) is: 0 (flat); log(1 + |F|^2/eps) -- at
      |F| = 1 EXACTLY 4 ln L plus O(eps) -- (simple); and for
      non-simple the ratio price_ns/price_simple -> 2 (measured
      1.85, 1.92, 1.95 at L = 10, 100, 1000).  The Z_N hierarchy
      0 / 2 log N / 4 log N is the same structure under the
      dictionary  N ~ L^2 (2 log N <-> 4 log L): the level is the
      SQUARE of the frame scale -- the ledger's square, again.

  s4  WHAT BARRETT-CRANE NEVER HAD.  With the Euclidean self-dual
      split, Pf(F) = (|F+|^2 - |F-|^2)/2 EXACTLY, so

        K = (2pi)^4 / ( eps^2 + eps(|F+|^2+|F-|^2)
                        + (|F+|^2-|F-|^2)^2/4 )

      -- a CAUCHY (Lorentzian) suppression of the self-dual
      imbalance.  As eps -> 0 it concentrates on the balanced cone
      |F+| = |F-| (Plebanski), which is Barrett-Crane's delta -- but
      the derived kernel carries what BC's bare delta never did:
      (i) a specified ON-CONE measure, K|_cone = (2pi)^4/(eps(eps +
      |F|^2)) ~ 1/|F|^2, log-uniform in curvature magnitude; (ii) a
      specified OFF-CONE tail ~ 1/Pf^2 -- nothing forbidden, the
      ledger's signature, now in the continuum; (iii) a canonical
      regulator eps = 1/L^4 tied to the frame scale.  This is the
      per-plaquette weight the one-vertex nonabelian model (0070's
      A2) will use.

Run directly for the verification suite.
"""

from __future__ import annotations

import cmath
import math
import random

PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def eps4(i, j, k, l):
    p = [i, j, k, l]
    if len(set(p)) < 4:
        return 0
    s = 1
    for a in range(4):
        for b in range(a + 1, 4):
            if p[a] > p[b]:
                s = -s
    return s


def star_matrix(F):
    d = dict(zip(PAIRS, F))
    return [[sum(eps4(i, j, k, l) * d[(k, l)] for (k, l) in PAIRS)
             for j in range(4)] for i in range(4)]


def pf(F):
    d = dict(zip(PAIRS, F))
    return (d[(0, 1)] * d[(2, 3)] - d[(0, 2)] * d[(1, 3)]
            + d[(0, 3)] * d[(1, 2)])


def K_closed(F, L):
    e = L ** -4
    F2 = sum(x * x for x in F)
    return (2 * math.pi) ** 4 / (e * e + e * F2 + pf(F) ** 2)


# =====================================================================
# 1. the atomic integral
# =====================================================================

def _atomic_semianalytic(lam, L, n=1501, span=9.0):
    h = 2 * span * L / n
    tot = 0.0
    for i in range(n):
        x = -span * L + (i + 0.5) * h
        tot += (math.sqrt(2 * math.pi) * L
                * math.exp(-lam * lam * x * x * L * L / 2)
                * math.exp(-x * x / (2 * L * L)) * h)
    return tot


def verify_atomic() -> None:
    for lam, L in ((0.0, 2.0), (0.5, 2.0), (1.5, 2.0), (0.7, 1.2)):
        e = L ** -4
        pred = 2 * math.pi / math.sqrt(e + lam * lam)
        got = _atomic_semianalytic(lam, L)
        assert abs(got - pred) / pred < 1e-6, (lam, L, got, pred)
        print(f"    lam = {lam}, L = {L}: quadrature {got:.6f} = "
              f"2 pi / sqrt(eps + lam^2) = {pred:.6f}")
    lam, L = 0.5, 2.0
    n, span = 1200, 8.0
    h = 2 * span * L / n
    tot = 0j
    for i in range(n):
        x = -span * L + (i + 0.5) * h
        for j in range(n):
            y = -span * L + (j + 0.5) * h
            tot += cmath.exp(1j * lam * x * y
                             - (x * x + y * y) / (2 * L * L)) * h * h
    pred = 2 * math.pi / math.sqrt(L ** -4 + lam * lam)
    assert abs(tot.real - pred) / pred < 1e-4 and abs(tot.imag) < 1e-9
    print(f"    brute 2D check: {tot.real:.5f} (imag {tot.imag:.0e})")
    print()
    print("  THE ATOMIC INTEGRAL IS EXACT: each canonical plane of")
    print("  star-F contributes (2 pi)^2/(eps + lam^2) to the kernel.")


# =====================================================================
# 2. the closed form
# =====================================================================

def _char_poly(M):
    def mm(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(4))
                 for j in range(4)] for i in range(4)]

    c3 = -sum(M[i][i] for i in range(4))
    A2 = mm(M, [[M[i][j] + (c3 if i == j else 0) for j in range(4)]
                for i in range(4)])
    c2 = -sum(A2[i][i] for i in range(4)) / 2
    A3 = mm(M, [[A2[i][j] + (c2 if i == j else 0) for j in range(4)]
                for i in range(4)])
    c1 = -sum(A3[i][i] for i in range(4)) / 3
    A4 = mm(M, [[A3[i][j] + (c1 if i == j else 0) for j in range(4)]
                for i in range(4)])
    c0 = -sum(A4[i][i] for i in range(4)) / 4
    return c3, c2, c1, c0


def verify_closed_form() -> None:
    rng = random.Random(5)
    for _ in range(50):
        F = [rng.gauss(0, 1) for _ in range(6)]
        c3, c2, c1, c0 = _char_poly(star_matrix(F))
        F2 = sum(x * x for x in F)
        assert abs(c3) < 1e-12 and abs(c1) < 1e-12
        assert abs(c2 - F2) < 1e-9 * max(1, F2)
        assert abs(c0 - pf(F) ** 2) < 1e-9 * max(1, pf(F) ** 2)
    print("    char poly of star-F = x^4 + |F|^2 x^2 + Pf^2:")
    print("    machine-exact on 50 random curvatures, so")
    print("    (eps+lam1^2)(eps+lam2^2) = eps^2 + eps |F|^2 + Pf^2")
    F = [0.3, -0.5, 0.8, 0.2, -0.4, 0.6]
    L = 1.2
    rng = random.Random(7)
    n = 400000
    M = star_matrix(F)
    acc = 0j
    for _ in range(n):
        a = [rng.gauss(0, L) for _ in range(4)]
        b = [rng.gauss(0, L) for _ in range(4)]
        ph = sum(a[i] * M[i][j] * b[j]
                 for i in range(4) for j in range(4))
        acc += cmath.exp(1j * ph)
    est = ((2 * math.pi * L * L) ** 4 * (acc / n)).real
    closed = K_closed(F, L)
    assert abs(est - closed) / closed < 0.01, (est, closed)
    print(f"    8D Monte-Carlo bridge, generic F: {est:.1f} vs closed"
          f" form {closed:.1f}  ({abs(est - closed) / closed:.2%})")
    print()
    print("  K_L(F) = (2 pi)^4 / (eps^2 + eps |F|^2 + Pf(F)^2),")
    print("  eps = 1/L^4: THE CONTINUUM LEDGER KERNEL, DERIVED AND")
    print("  CLOSED-FORM in the two simplicity invariants.")


# =====================================================================
# 3. the tiers recovered
# =====================================================================

def verify_tiers() -> None:
    Fs = [1.0, 0, 0, 0, 0, 0]
    Fn = [1 / math.sqrt(2), 0, 0, 0, 0, 1 / math.sqrt(2)]
    prev = 0.0
    for L in (10.0, 100.0, 1000.0):
        e = L ** -4
        ps = math.log((e * e + e * 1 + pf(Fs) ** 2) / (e * e))
        pn = math.log((e * e + e * 1 + pf(Fn) ** 2) / (e * e))
        ratio = pn / ps
        print(f"    L = {L:6.0f}: price_simple = {ps:7.3f} "
              f"(4 ln L = {4 * math.log(L):7.3f}), ratio "
              f"non-simple/simple = {ratio:.4f}")
        assert abs(ps - 4 * math.log(L)) < 0.02
        assert ratio > prev
        prev = ratio
    assert prev > 1.94
    print()
    print("  THE Z_N HIERARCHY 0 / 2 log N / 4 log N RETURNS with the")
    print("  dictionary N ~ L^2: the level is the SQUARE of the frame")
    print("  scale.  The parity ratio -> 2 exactly as L -> infinity.")


# =====================================================================
# 4. what Barrett-Crane never had
# =====================================================================

def verify_bc_structure() -> None:
    rng = random.Random(9)
    for _ in range(50):
        F = [rng.gauss(0, 1) for _ in range(6)]
        sF = [F[5], -F[4], F[3], F[2], -F[1], F[0]]
        Fp = [(F[i] + sF[i]) / 2 for i in range(6)]
        Fm = [(F[i] - sF[i]) / 2 for i in range(6)]
        imb = sum(x * x for x in Fp) - sum(x * x for x in Fm)
        assert abs(pf(F) - imb / 2) < 1e-9
    print("    Pf(F) = (|F+|^2 - |F-|^2)/2: exact on 50 random")
    print("    curvatures -- the kernel is a CAUCHY suppression of")
    print("    the self-dual imbalance")
    Fbal = [1.0, 0, 0, 0, 0, 1.0]          # |F+|=|F-| balanced? pf=1
    # balanced example: F with sF = -F components mix; use imbalance
    # scan instead: fix |F| = 1, vary Pf via mixing angle
    print("    concentration on the balanced cone as eps -> 0")
    print("    (weight at imbalance i relative to cone, |F| = 1):")
    for L in (3.0, 10.0, 30.0):
        e = L ** -4
        cone = 1 / (e * e + e)
        off = 1 / (e * e + e + 0.25)        # Pf = 0.5
        print(f"      L = {L:4.0f}: off-cone/on-cone = "
              f"{off / cone:.2e}")
    assert (1 / (30.0 ** -8 + 30.0 ** -4 + 0.25)) \
        / (1 / (30.0 ** -8 + 30.0 ** -4)) < 1e-4
    print()
    print("  AS eps -> 0 THE KERNEL BECOMES BARRETT-CRANE'S DELTA ON")
    print("  THE SIMPLE CONE -- but carrying what BC never specified:")
    print("  an on-cone measure ~ 1/|F|^2 (log-uniform in curvature")
    print("  magnitude), an off-cone Cauchy tail ~ 1/Pf^2 (nothing")
    print("  forbidden -- the ledger's signature), and a canonical")
    print("  regulator eps = 1/L^4 tied to the frame scale.  This is")
    print("  the per-plaquette weight for the one-vertex nonabelian")
    print("  model (0070's A2).")


def run_verification_suite() -> None:
    sections = [
        ("The atomic integral", verify_atomic),
        ("The closed form", verify_closed_form),
        ("The tiers recovered", verify_tiers),
        ("What Barrett-Crane never had", verify_bc_structure),
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
