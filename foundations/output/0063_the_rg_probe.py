"""The RG probe: which phase the derived measure sits in.

Path A's first stone (0070).  The ledger weight has NO coupling knob
-- it is derived (0064) -- so its phase is a fact about the program,
not a parameter choice.  In the abelian sector that fact is exactly
computable, and it answers "where does the program bleed."

  s1  BLOCKING IS A DUAL POWER, AND THE ENSEMBLE IS RG-CLOSED.  In
      the 2D flux representation, merging 2x2 plaquette blocks makes
      the block flux the sum of the four fluxes, so the blocked
      weight is the 4-fold cyclic convolution: in the dual basis,
      What' = What^4, EXACTLY (verified in integer arithmetic at
      N = 12).  Functions of gcd(n, N) are closed under powers, so
      THE DIVISOR ENSEMBLE IS AN RG-INVARIANT FAMILY, the pure
      levels (BF at each divisor) are its fixed points, and the flow
      lives on the divisor simplex.

  s2  IN 2D THE JITTER WINS TOTALLY.  The ledger's level weights
      under successive blockings (N = 12): the free sector's share
      goes 0.300 -> 0.914 -> 1.000.  The ledger flows to the FREE
      theory in two steps -- which is the measured area law (0055)
      read as an RG statement.  D = 2 spacetime gravity is empty
      anyway; no loss, but total.

  s3  IN 3D THE LEDGER IS CONFINED.  Wegner duality rewrites the 3D
      Z_N gauge theory exactly as a spin model with bond weights
      equal to the DUAL ledger weights (0064's What = G(gcd)).  For
      prime N the ledger is two-valued and the couplings are exact:

        N = 2: Ising K = (1/2) ln 3 = 0.5493  vs  K_c ~ 0.2217
        N = 3: Potts J = ln(5/2)   = 0.9163  vs  J_c ~ 0.5506

      -- deep in the ORDERED phase, i.e. the gauge theory is
      CONFINED: Wilson magnitudes area-law at every scale, no
      long-range rigid geometry in the 3D vacuum measure.  (K_c
      values are cited literature numbers -- flagged.)

  s4  IN 4D, RIGIDITY BEGINS AT N = 3.  4D Z_N gauge is dual to
      itself; the two-valued family (r on F = 0, 1 else) is closed
      under duality with r~ = (r - 1 + N)/(r - 1), self-dual point
      r* = 1 + sqrt(N) (exact).  The ledger has r = N:

        N = 2:  r = 2  <  r* = 2.414   CONFINED
        N = 3:  r = 3  >  r* = 2.732   DECONFINED
        N = 5:  r = 5  >  r* = 3.236   DECONFINED
        (deconfined for every prime N >= 3: N - 1 > sqrt(N))

      Under the standard single-transition assumption, THE DERIVED
      MEASURE FIRST SUPPORTS LONG-RANGE RIGID GEOMETRY IN FOUR
      DIMENSIONS, AND ONLY FOR N >= 3.  Two firsts: the program's
      first internal evidence selecting D = 4 (the arena assumption
      F earns its first support), and the first derived constraint
      on the knob N (N >= 3; N = 2's degeneracy joins its exclusion
      from the Kulkarni-Nomizu and SD/ASD constructions).

  WHERE IT BLEEDS, honestly: the abelian interacting vacuum has no
  long-range geometry below four dimensions; in 4D the deconfined
  phase is TOPOLOGICAL order -- rigidity without gravitons (Z_N has
  no massless mode; the finiteness ceiling 0061 s4 stands).  The
  substrate is rigid; the modes need the continuous group (0063).
  The bleed-line moves to: the N >= 5 intermediate-phase caveat,
  and the nonabelian tier (0070's A1-A3).

Run directly for the verification suite.
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction as Fr
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


def ledger(N):
    return [gcd(F if F else N, N) for F in range(N)]


def conv(A, B, N):
    return [sum(A[i] * B[(f - i) % N] for i in range(N))
            for f in range(N)]


# =====================================================================
# 1. blocking is a dual power; the ensemble is RG-closed
# =====================================================================

def verify_closure() -> None:
    N = 12
    W = ledger(N)
    W2 = conv(W, W, N)
    W4 = conv(W2, W2, N)          # integer arithmetic throughout
    Fh = [sum(W[F] * cmath.exp(-2j * math.pi * n * F / N)
              for F in range(N)) for n in range(N)]
    F4 = [sum(W4[F] * cmath.exp(-2j * math.pi * n * F / N)
              for F in range(N)) for n in range(N)]
    worst = max(abs(F4[n] - Fh[n] ** 4) for n in range(N))
    print(f"    N = 12: dual(blocked) = dual^4: max dev {worst:.1e}")
    assert worst < 1e-6
    byg = {}
    for F in range(N):
        g = gcd(F if F else N, N)
        if g in byg:
            assert byg[g] == W4[F], (F, g)
        byg[g] = W4[F]
    print("    blocked weight is still a function of gcd(F, N):")
    print("    EXACT (integer arithmetic)")
    print()
    print("  THE DIVISOR ENSEMBLE IS AN RG-INVARIANT FAMILY: blocking")
    print("  raises the dual weight to the 4th power, gcd-functions")
    print("  are closed under powers, and the pure levels are the")
    print("  flow's fixed points.")


# =====================================================================
# 2. in 2D the jitter wins totally
# =====================================================================

def level_shares(W, N):
    prof = {}
    for F in range(N):
        prof[gcd(F if F else N, N)] = W[F]
    c = {}
    for d in divisors(N):
        c[d] = prof[d] - sum(c[e] for e in divisors(d) if e != d)
    tot = sum(c[d] * (N // d) for d in divisors(N))
    return {d: c[d] * (N // d) / tot for d in divisors(N)}


def verify_2d_flow() -> None:
    N = 12
    cur = [float(x) for x in ledger(N)]
    frees = []
    for it in range(3):
        sh = level_shares(cur, N)
        frees.append(sh[1])
        row = ", ".join(f"d={d}: {sh[d]:.3f}" for d in divisors(N))
        print(f"    blocking {it}: {row}")
        cur = conv(conv(cur, cur, N), conv(cur, cur, N), N)
        m = max(cur)
        cur = [x / m for x in cur]
    assert frees[0] < 0.35 and frees[-1] > 0.999, frees
    print()
    print("  THE 2D LEDGER FLOWS TO THE FREE SECTOR IN TWO BLOCKINGS")
    print("  -- 0055's measured area law, read as an RG flow.  D = 2")
    print("  gravity is empty anyway; no loss, but total.")


# =====================================================================
# 3. in 3D the ledger is confined
# =====================================================================

def verify_3d_confined() -> None:
    rows = [(2, 0.221654, "Ising", 0.5),
            (3, 0.550565, "3-state Potts", 1.0)]
    for N, Kc, name, half in rows:
        num, den = N - 1 + N, N - 1     # dual weights G(N), G(1)
        K = half * math.log(num / den)
        print(f"    N = {N}: dual bond ratio {num}/{den} -> "
              f"{name} coupling {K:.4f} vs cited K_c ~ {Kc}")
        assert K > Kc
    print()
    print("  DEEP IN THE ORDERED PHASE OF THE DUAL SPIN MODEL: the 3D")
    print("  ledger gauge theory is CONFINED -- Wilson magnitudes")
    print("  area-law at every scale, no long-range rigid geometry in")
    print("  the 3D vacuum.  (K_c values cited, flagged.)")


# =====================================================================
# 4. in 4D, rigidity begins at N = 3
# =====================================================================

def verify_4d_selfdual() -> None:
    # two-value family closed under duality: exact involution
    for N in (3, 5):
        r = Fr(4)
        rd = (r - 1 + N) / (r - 1)
        rdd = (rd - 1 + N) / (rd - 1)
        assert rdd == r, (N, rd, rdd)
    print("    duality map r -> (r-1+N)/(r-1): exact involution on")
    print("    the two-value family (checked over Q)")
    print("    self-dual point r* = 1 + sqrt(N); ledger has r = N:")
    for N in (2, 3, 5, 7, 11):
        r = N
        rstar = 1 + math.sqrt(N)
        side = "DECONFINED (rigid)" if r > rstar else \
               "CONFINED (jitter wins)"
        print(f"      N = {N:2d}: r = {r:2d} vs r* = {rstar:.4f}"
              f"   {side}")
        if N == 2:
            assert r < rstar
        else:
            assert r > rstar
    # N - 1 > sqrt(N) for all N >= 3: check a swath
    for N in range(3, 200):
        assert (N - 1) ** 2 > N
    print("    (N - 1)^2 > N for every N >= 3: the deconfined")
    print("    placement holds for ALL levels above 2")
    print()
    print("  UNDER THE SINGLE-TRANSITION ASSUMPTION, THE DERIVED")
    print("  MEASURE FIRST SUPPORTS LONG-RANGE RIGID GEOMETRY IN FOUR")
    print("  DIMENSIONS, AND ONLY FOR N >= 3.  First internal evidence")
    print("  selecting D = 4, and the first derived constraint on the")
    print("  knob: N >= 3.")


def run_verification_suite() -> None:
    sections = [
        ("Blocking is a dual power; the ensemble is RG-closed",
         verify_closure),
        ("In 2D the jitter wins totally", verify_2d_flow),
        ("In 3D the ledger is confined", verify_3d_confined),
        ("In 4D, rigidity begins at N = 3", verify_4d_selfdual),
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
