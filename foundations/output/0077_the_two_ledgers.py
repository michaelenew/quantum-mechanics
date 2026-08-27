"""0077 -- the two ledgers: the polar theorem, and what the budget
actually protects.

0085 open 1, the protection calculation, run in the Z_N toy -- the
first pivot down the escalation ladder (full theory -> Z_N toy). The
result CORRECTS 0085's assumed mechanism, in two steps.

  s1  THE POLAR THEOREM (exact, open lattice). For the unconstrained
      ledger measure with frustration n_p and a Wilson loop enclosing
      area A:
          <W> = exp(i 2pi/N sum_enc n_p) * f(N)^A,  f = phi(N)/P(N)
      -- an exact factorization. The PHASE carries only the sources
      (additive, area-independent: the mass-extensive source ledger);
      the MODULUS carries only the record (area law, blind to the
      sources: the record account). 0085's two ledgers are the polar
      decomposition of one complex number, and the vacuum record
      cannot twist CATEGORICALLY -- no budget or constraint is needed
      to protect geometry from the zero-point record. (Trust reading:
      the modulus is the confidence channel, the phase the content
      channel -- the seed split, materialized.)
  s2  Exactness checks, dual t-sum formula vs brute flux enumeration
      (1e-12): vacuum phase = 0 for every loop on both geometries
      (W even, W-hat real); defect phases add mod 2pi; the modulus is
      independent of the frustration.
  s3  WHAT THE BUDGET ACTUALLY DOES (closed lattice): it does NOT
      delete uniform sources. N=3, P=9 (N | P): a uniform frustration
      passes the budget untouched -- loop phase = 2pi A/3 EXACTLY, a
      full quantized-Lambda leak. N=5, P=9 (coprime): the budget can
      only subtract ONE FLUX QUANTUM (fluxes are discrete -- there is
      no way to smear -n/P everywhere), so uniform curvature appears
      at essentially full strength, with small A-dependent
      corrections; the smeared trace-removal guess (1 - A/P) is
      REJECTED by measurement. The budget's one true job: the
      global residual -- the A = P loop reads exactly 0, i.e.
      Lambda * Volume is quantized in 2pi/N units (0069's spectrum,
      0080's distribution, now seen dynamically in loop phases).
  s4  The closed-lattice defect: near-full deficit with small budget
      corrections that grow with A/P (one compensating quantum in the
      complement), tabulated.

Revision recorded for 0085 s2: the vacuum record's safety is the
polar theorem (layer i, exact, constraint-free); the budget provides
only the global Lambda quantization (layer ii). The 'mutual
protection' framing survives with the roles reassigned.
"""

import cmath
import itertools
import math
from math import gcd


# ----------------------------------------------------------------------
# ledger kit
# ----------------------------------------------------------------------

def what(k, N):
    tot = 0
    for d in range(1, N + 1):
        if N % d == 0 and k % (N // d) == 0:
            phi = sum(1 for x in range(1, d + 1) if gcd(x, d) == 1)
            tot += phi * (N // d)
    return tot


def f_of(N):
    return what(1, N) / what(0, N)


def open_W(N, P, enc, ns):
    """<W> on the unconstrained (open/disk) lattice: exact product."""
    z = 1 + 0j
    for p in range(P):
        c = 1 if p in enc else 0
        z *= cmath.exp(2j * math.pi * ns[p] * c / N) \
            * (what(c, N) / what(0, N))
    return z


def torus_W(N, P, enc, ns):
    """<W> on the closed lattice (budget sum F = 0): dual t-sum."""
    num = 0j
    den = 0j
    for t in range(N):
        zn = 1 + 0j
        zd = 1 + 0j
        for p in range(P):
            c = 1 if p in enc else 0
            zn *= cmath.exp(2j * math.pi * ns[p] * (c + t) / N) \
                * what((c + t) % N, N)
            zd *= cmath.exp(2j * math.pi * ns[p] * t / N) * what(t, N)
        num += zn
        den += zd
    return num / den


def torus_W_brute(N, P, enc, ns):
    num = 0j
    den = 0.0
    for F in itertools.product(range(N), repeat=P - 1):
        Fs = list(F) + [(-sum(F)) % N]
        w = 1
        for p in range(P):
            x = (Fs[p] - ns[p]) % N
            w *= gcd(x if x else N, N)
        num += w * cmath.exp(2j * math.pi
                             * sum(Fs[p] for p in enc) / N)
        den += w
    return num / den


def open_W_brute(N, P, enc, ns):
    num = 0j
    den = 0.0
    for Fs in itertools.product(range(N), repeat=P):
        w = 1
        for p in range(P):
            x = (Fs[p] - ns[p]) % N
            w *= gcd(x if x else N, N)
        num += w * cmath.exp(2j * math.pi
                             * sum(Fs[p] for p in enc) / N)
        den += w
    return num / den


def ang_diff(a, b):
    return abs((a - b + math.pi) % (2 * math.pi) - math.pi)


# ----------------------------------------------------------------------

def s1_polar_theorem():
    print("== s1: the polar theorem (open lattice, exact) ==")
    N, P = 5, 6
    fN = f_of(N)
    for enc, ns in ([{0, 1}, [2, 0, 1, 0, 0, 3]],
                    [{0, 2, 3}, [1, 1, 1, 1, 1, 1]],
                    [{4}, [0] * 6]):
        z = open_W(N, P, enc, ns)
        zb = open_W_brute(N, P, enc, ns)
        assert abs(z - zb) < 1e-12
        pred_phase = 2 * math.pi * sum(ns[p] for p in enc) / N
        pred_mod = fN ** len(enc)
        assert ang_diff(cmath.phase(z), pred_phase) < 1e-12
        assert abs(abs(z) - pred_mod) < 1e-12
        print(f"  enc={sorted(enc)}, ns={ns}: arg = 2pi/N * sum_enc n "
              f"and |W| = f^A, both exact")
    print("  <W> = e^{i delta_source} * f^Area: phase = source ledger "
          "ONLY, modulus = record ONLY.")
    print("  the vacuum record cannot twist, categorically -- no "
          "constraint needed\n")


def s2_exactness():
    print("== s2: exactness checks (dual vs brute, vacuum, "
          "additivity) ==")
    N, P = 3, 4
    for enc, ns in ([{0}, [0] * 4], [{0, 1}, [1, 0, 0, 0]],
                    [{0}, [1, 1, 1, 1]], [{1, 2}, [2, 1, 0, 2]]):
        assert abs(torus_W(N, P, enc, ns)
                   - torus_W_brute(N, P, enc, ns)) < 1e-12
    print("  dual t-sum == brute flux enumeration (N=3, P=4), all "
          "cases, 1e-12")
    for A in (1, 2, 3, 4):
        for W in (open_W(5, 9, set(range(A)), [0] * 9),
                  torus_W(5, 9, set(range(A)), [0] * 9)):
            assert abs(cmath.phase(W)) < 1e-12
    print("  vacuum phase = 0 for every loop, open and closed alike "
          "(W even, W-hat real)")
    z1 = open_W(5, 9, {0, 1, 2}, [1, 0, 0] + [0] * 6)
    z2 = open_W(5, 9, {0, 1, 2}, [0, 3, 0] + [0] * 6)
    z12 = open_W(5, 9, {0, 1, 2}, [1, 3, 0] + [0] * 6)
    assert ang_diff(cmath.phase(z12),
                    cmath.phase(z1) + cmath.phase(z2)) < 1e-12
    assert abs(abs(z1) - abs(z12)) < 1e-12
    print("  defect phases add mod 2pi; the modulus never sees the "
          "sources\n")


def s3_budget_job():
    print("== s3: what the budget actually does ==")
    # N | P: exact quantized-Lambda leak
    N, P = 3, 9
    for A in (1, 2, 3):
        z = torus_W(N, P, set(range(A)), [1] * P)
        assert ang_diff(cmath.phase(z), 2 * math.pi * A / 3) < 1e-12
    print("  N=3, P=9 (N | P): uniform frustration passes the budget "
          "-- loop phase = 2piA/3 EXACTLY.")
    print("  uniform Lambda is NOT deleted; it is allowed whenever "
          "P n = 0 (mod N)")
    # coprime: one-quantum compensation only
    N, P = 5, 9
    print("  N=5, P=9 (coprime): uniform n=1 --")
    for A in (1, 2, 3):
        z = torus_W(N, P, set(range(A)), [1] * P)
        naive = 2 * math.pi * A / 5
        smear = (2 * math.pi / 5) * A * (1 - 1 / 9)  # smeared-comp guess
        dev_naive = ang_diff(cmath.phase(z), naive)
        dev_smear = ang_diff(cmath.phase(z), smear)
        print(f"    A={A}: arg = {cmath.phase(z):+.4f}  (naive Lambda "
              f"{naive:.4f}, dev {dev_naive:.4f}; smeared guess dev "
              f"{dev_smear:.4f})")
        assert dev_naive < 0.08
        # the record stays in the modulus even with sources; on the
        # closed lattice the f^A law bends as A -> P/2 (vacuum
        # complementarity |W(A)| = |W(P-A)|), so hold it only for
        # small A/P
        if A <= 2:
            assert abs(abs(z) / f_of(N) ** A - 1) < 0.02
    print("    full-strength curvature minus one-quantum corrections: "
          "fluxes are discrete, the")
    print("    budget cannot smear -n/P; the (1 - A/P) trace-removal "
          "guess is rejected")
    # the one true deletion: the global loop
    for N, P, n in ((5, 9, 1), (3, 9, 1), (5, 9, 3)):
        z = torus_W(N, P, set(range(P)), [n] * P)
        assert abs(cmath.phase(z)) < 1e-12
    print("  the A = P loop reads phase 0 exactly, any uniform n: "
          "Lambda*Volume is quantized")
    print("  in 2pi/N units -- 0069's spectrum and 0080's residual, "
          "now dynamical\n")


def s4_torus_defect():
    print("== s4: the closed-lattice defect ==")
    N, P = 5, 9
    full = 2 * math.pi / 5
    print("  single defect n=1, enclosed; deficit vs the open-lattice "
          "exact 2pi/5:")
    fracs = []
    for A in (1, 2, 3, 4):
        z = torus_W(N, P, set(range(A)), [1] + [0] * 8)
        frac = cmath.phase(z) / full
        fracs.append(frac)
        print(f"    A={A}: arg = {cmath.phase(z):.4f} = {frac:.3f} x "
              f"(2pi/5)")
    assert all(f2 < f1 for f1, f2 in zip(fracs, fracs[1:]))
    assert fracs[2] > 0.9 and fracs[3] > 0.5
    print("  near-full deficit; the budget's compensating quantum "
          "sits in the complement and")
    print("  erodes the phase as A/P grows -- a finite-universe "
          "correction, not trace removal\n")


if __name__ == "__main__":
    s1_polar_theorem()
    s2_exactness()
    s3_budget_job()
    s4_torus_defect()
    print("all assertions passed")
