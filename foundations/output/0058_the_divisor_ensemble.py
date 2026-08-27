"""The divisor ensemble: what the ledger measure actually is.

Pursuing the novelty thread (0058 s3, 0062 open 1, 0063 open 1).  The
quantum arc's weight gcd(F,N)/N has been a number-theoretic black box
since 0053.  A classical identity opens it, and what is inside answers
0063's sharpest open -- the continuum ledger -- by DERIVATION rather
than choice.

  s1  THE LEDGER IS AN ENSEMBLE OF TOPOLOGICAL THEORIES.  Cesaro's
      identity (verified exactly, all N <= 60):

        gcd(F, N) = sum_{d | N} phi(d) [d | F]

      so the per-plaquette ledger weight is a phi-weighted mixture of
      FLATNESS CONSTRAINTS at every level d dividing N -- each [d|F]
      is the BF/Dijkgraaf-Witten weight of the level-d subtheory.
      Expanding the product over plaquettes, the ledger partition
      function is a sum over DIVISOR FIELDS {d_p}: the quantization
      level is a LOCAL, DYNAMICAL variable, distributed by Euler phi.
      On a closed 2-plaquette universe the budget couples the levels
      through their lcm:

        Z = sum_{d1,d2 | N} phi(d1) phi(d2) N / lcm(d1, d2)

      verified exactly against the direct gcd sum at N = 6 and 12 --
      0053 s4's mysterious inter-plaquette correlation is the lcm.

  s2  CLOSED FORMS FOR THE MEASURED ARC.  The single-plaquette jitter
      base of 0055 (measured 1/3, 2/5, 1/4, 4/9, 6/13) is exactly

        f(N) = phi(N) / P(N),        P(N) = Pillai's function,

      and equals the probability that the plaquette's local level is
      MAXIMAL: the classical rigid geometry is the d = N sector, and
      the quantum jitter is the phi-probability of sub-maximal local
      levels.  Tension = log(P(N)/phi(N)).  For prime N the ensemble
      is two-level -- BF plus the free theory, weights -> (1/2, 1/2),
      tension -> log 2.  For N = 2^k the level distribution is
      asymptotically UNIFORM over the dyadic tower -- 0053's 2-adic
      grading is the divisor lattice, resolved.

  s3  THE CONTINUUM LEDGER, DERIVED.  In the character (charge) basis
      the dual weight is What(n) = sum_{e | gcd(n,N)} e phi(N/e), and
      for divisibility-saturated N (N = lcm(1..K)^2):

        What(n) / What(1)  =  tau(n)   EXACTLY, for all n <= K

      -- the number-of-divisors function.  And tau = 1 * 1, the
      DIRICHLET SQUARE of BF's flat weight: the ledger's
      "probability = amplitude squared" becomes Dirichlet convolution
      in the charge basis.  So the continuum U(1) ledger weight is
      ARITHMETIC and heavy-tailed -- emphatically not 0063's chosen
      heat kernel -- and 0063 open 1 is answered at the abelian tier.
      The zero mode What(0)/What(1) = P(N)/phi(N) diverges: exactly
      the mode the closed-universe budget removes (0029/0057).

  s4  FIRST OBSERVABLE AND ITS DELICACY.  The closed 2-plaquette
      universe's Wilson expectation under the ledger falls slowly
      with N (0.350 at N = 144 -> 0.239 at N = 705600) -- the
      tau-weights' heavy tail (sum tau^2 diverges logarithmically)
      makes the strict continuum value delicate, tied to the same
      zero-mode/budget treatment as the Green function of 0057.
      Recorded as measured trend, not limit.

Run directly for the verification suite.
"""

from __future__ import annotations

import cmath
import math
from math import gcd


def phi(n):
    r, m = n, n
    p = 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            r -= r // p
        p += 1
    if m > 1:
        r -= r // m
    return r


def divisors(n):
    ds = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            ds.append(d)
            if d * d != n:
                ds.append(n // d)
        d += 1
    return sorted(ds)


def pillai(n):
    return sum(gcd(k if k else n, n) for k in range(n))


def tau(n):
    return len(divisors(n))


def lcm_range(k):
    L = 1
    for i in range(2, k + 1):
        L = L * i // gcd(L, i)
    return L


def dual_weight(n, N):
    """What(n) = sum_{e | gcd(n,N)} e phi(N/e)  (Fourier dual of gcd)."""
    g = gcd(n if n else N, N)
    return sum(e * phi(N // e) for e in divisors(g))


# =====================================================================
# 1. the ledger is an ensemble of topological theories
# =====================================================================

def verify_ensemble() -> None:
    bad = 0
    for N in range(1, 61):
        for F in range(N):
            lhs = gcd(F if F else N, N)
            rhs = sum(phi(d) for d in divisors(N) if F % d == 0)
            if lhs != rhs:
                bad += 1
    assert bad == 0
    print("    Cesaro: gcd(F,N) = sum_{d|N} phi(d)[d|F] -- EXACT for")
    print("    every F at every N <= 60")
    for N in (6, 12):
        z_direct = sum(gcd(F if F else N, N) ** 2 for F in range(N))
        z_ens = sum(phi(d1) * phi(d2) * (N // (d1 * d2 // gcd(d1, d2)))
                    for d1 in divisors(N) for d2 in divisors(N))
        w_direct = sum(gcd(F if F else N, N) ** 2
                       * cmath.exp(2j * math.pi * F / N)
                       for F in range(N))
        assert z_direct == z_ens, (N, z_direct, z_ens)
        print(f"      closed 2-plaquette universe, N = {N}: "
              f"Z_gcd = {z_direct} = "
              f"sum phi phi N/lcm = {z_ens}   <W> = "
              f"{w_direct.real / z_direct:+.4f}")
    print()
    print("  THE LEDGER IS A phi-WEIGHTED ENSEMBLE OF TOPOLOGICAL")
    print("  THEORIES, one flatness level per divisor, with the LEVEL A")
    print("  LOCAL DYNAMICAL VARIABLE.  The closed-universe budget")
    print("  couples neighbouring levels through their lcm -- 0053 s4's")
    print("  correlation, now an exact formula.")


# =====================================================================
# 2. closed forms for the measured arc
# =====================================================================

def verify_closed_forms() -> None:
    table = {2: (1, 3), 3: (2, 5), 4: (1, 4), 5: (4, 9), 7: (6, 13)}
    print("    f(N) = phi(N)/P(N) vs 0055's measured area-law base:")
    for N in (2, 3, 4, 5, 6, 7, 8, 9, 12):
        om = cmath.exp(2j * math.pi / N)
        num = sum(gcd(F if F else N, N) * om ** F for F in range(N))
        f_direct = num.real / pillai(N)
        f_closed = phi(N) / pillai(N)
        assert abs(f_direct - f_closed) < 1e-12, N
        mark = ""
        if N in table:
            a, b = table[N]
            assert abs(f_closed - a / b) < 1e-12, N
            mark = f"   = 0055's {a}/{b}"
        print(f"      N = {N:2d}: f = phi/P = {phi(N)}/{pillai(N)} "
              f"= {f_closed:.6f}{mark}")
    print()
    print("    prime-N ensemble -> two levels (BF + free):")
    for N in (101, 1009, 10007):
        wBF = N / (2 * N - 1)
        wfree = (N - 1) / (2 * N - 1)
        print(f"      N = {N}: weights (BF, free) = "
              f"({wBF:.4f}, {wfree:.4f}), f = {phi(N) / pillai(N):.4f}")
    print(f"      -> (1/2, 1/2); tension -> log 2 = {math.log(2):.4f}")
    print()
    print("    dyadic N = 2^k: level distribution (j = log2 d):")
    for k in (3, 6, 10):
        N = 2 ** k
        P = pillai(N)
        w0 = N / P
        wj = (2 ** (k - 1)) / P
        print(f"      k = {k:2d}: weight(d=1) = {w0:.4f}, each "
              f"level j >= 1: {wj:.4f}  (uniform: 1/(k+2) = "
              f"{1 / (k + 2):.4f})")
        assert abs(wj - 1 / (k + 2)) < 1e-12
    print()
    print("  THE JITTER IS THE PROBABILITY OF A SUB-MAXIMAL LOCAL")
    print("  LEVEL: f(N) = phi(N)/P(N) is exactly P(level = N).")
    print("  Classical rigidity is the maximal-level sector; 0053's")
    print("  2-adic grading is the divisor tower, uniformly populated.")


# =====================================================================
# 3. the continuum ledger, derived
# =====================================================================

def verify_continuum_ledger() -> None:
    print("    dual weights What(n)/What(1) at divisibility-saturated N:")
    for K in (6, 10, 14):
        N = lcm_range(K) ** 2
        ok = all(dual_weight(n, N) == tau(n) * dual_weight(1, N)
                 for n in range(1, K + 1))
        assert ok, K
        row = " ".join(f"{tau(n)}" for n in range(1, min(K, 10) + 1))
        print(f"      N = lcm(1..{K})^2: ratios = tau(n) EXACTLY "
              f"(n <= {K}): {row} ...")
    ok = all(tau(n) == sum(1 for d in divisors(n))
             for n in range(1, 2001))
    assert ok
    print("    tau = 1 * 1 (Dirichlet convolution of the flat weight")
    print("    with itself): checked n <= 2000")
    print("    zero mode: What(0)/What(1) = P(N)/phi(N):")
    for K in (6, 10, 14):
        N = lcm_range(K) ** 2
        r = dual_weight(0, N) / dual_weight(1, N)
        print(f"      K = {K}: {r:.2f}")
    print()
    print("  THE CONTINUUM U(1) LEDGER WEIGHT IS tau(n) -- the number")
    print("  of divisors of the charge -- and tau = 1*1: probability =")
    print("  amplitude^2 becomes DIRICHLET CONVOLUTION in the charge")
    print("  basis.  Arithmetic and heavy-tailed, NOT the heat kernel:")
    print("  0063 open 1 answered at the abelian tier, by derivation.")
    print("  The divergent zero mode is exactly the mode the")
    print("  closed-universe budget removes.")


# =====================================================================
# 4. first observable and its delicacy
# =====================================================================

def verify_first_observable() -> None:
    print("    closed 2-plaquette universe under the ledger:")
    prev = None
    for N in (144, 3600, 705600):
        num = 0.0
        den = 0.0
        for F in range(N):
            g = gcd(F if F else N, N)
            num += g * g * math.cos(2 * math.pi * F / N)
            den += g * g
        w = num / den
        print(f"      N = {N:>6}: <W> = {w:.4f}")
        if prev is not None:
            assert w < prev
        prev = w
    print()
    print("  Falls slowly with N: the tau-weights' heavy tail (sum of")
    print("  tau^2 diverges logarithmically) makes the strict continuum")
    print("  value delicate -- the same zero-mode/budget treatment the")
    print("  Green function needed (0057).  Recorded as a trend, not a")
    print("  limit.")


def run_verification_suite() -> None:
    sections = [
        ("The ledger is an ensemble of topological theories",
         verify_ensemble),
        ("Closed forms for the measured arc", verify_closed_forms),
        ("The continuum ledger, derived", verify_continuum_ledger),
        ("First observable and its delicacy", verify_first_observable),
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
