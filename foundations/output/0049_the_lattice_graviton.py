"""The lattice graviton, and gravity computed from the quantum model.

The milestone: a gravitational effect DERIVED from the quantized
lattice and then COMPUTED in it.  The effect is the conical deficit
-- the web's oldest object (0014's atom, 0027's quantized spectrum)
-- obtained here as the expectation value of a Wilson loop in the
interacting quantum ground state, with a quantum correction that
has no classical counterpart.

  s0  THE DERIVATION.  Integrating the link variables out of the
      level-N partition function leaves an exact measure on
      plaquette fluxes.  The link -> flux Jacobian is the gauge
      volume, uniform, so nothing survives but the plaquette
      weights and the closure of the surface:

        P({F_p}) ~ prod_p W(F_p - n_p),   sum_p F_p = 0 (mod N)

      with n_p the inserted source (a quantized mass) and W the
      budget weight of 0053: W = delta_{F,0} for the free BF
      measure, W = gcd(F,N)/N for the ledger's squared measure
      B = e e.  The constraint sum F = 0 is the closed-universe
      budget (0029's Sigma delta = 4 pi): on a closed web a mass
      must be compensated.  A Wilson loop around a region R
      measures omega^(sum_{p in R} F_p) -- lattice Stokes, exact.

  s1  THE DEFICIT, COMPUTED.  Exact enumeration of all N^(P-1)
      flux configurations on a 3x3 torus with a neutral pair of
      sources (+1, -1 on opposite corners), squared measure:

        loop                    |<W>|      phase
        p0 (encloses +1)        0.4007    +2.09440
        p0 + p1                 0.1618    +2.09440
        2x2 block with source   0.0361    +2.09440
        p1 (encloses nothing)   0.4007    -0.00000
        2x2 block, empty        0.0361    +0.00000

      2 pi/3 = 2.09440.  THE PHASE IS EXACTLY THE CLASSICAL
      DEFICIT 2 pi n/N, for every loop that encloses the mass --
      independent of the loop's size and shape -- and exactly zero
      for every loop that does not.  The quantized conical defect,
      recovered as a quantum expectation value.  Verified for
      N = 2, 3, 4, 5: the phase tracks 2 pi/N to machine precision
      (and -> 0 as N -> infinity: the classical continuum).

  s2  THE QUANTUM CORRECTION, AND WHAT SEPARATES THE TWO
      THEORIES.  Under the free BF measure the same computation
      gives |<W>| = 1.0000 EXACTLY at every loop: the deficit is
      there, but the geometry is RIGID -- no fluctuation at all.
      Under the ledger's squared measure |<W>| < 1 and falls with
      the loop's AREA (0.4007, 0.1618, 0.0361 for 1, 2, 4
      plaquettes).  Same topological deficit; only the priced
      measure has zero-point curvature fluctuation.  That
      magnitude is a purely quantum observable with no classical
      counterpart -- the geometry's jitter.

  s3  THE LATTICE GRAVITON.  In the flux basis the plaquette price
      V(F) = -log W(F) = log(N/gcd(F,N)) is the on-site energy of a
      curvature quantum, and the electric term of the lattice
      theory shifts a link -- moving one quantum to a neighbouring
      plaquette.  Because sum F = 0, quanta exist only in +/-
      PAIRS (the budget again).  Diagonalizing the pair's
      centre-of-mass motion on a ring (N = 3, L = 12, t = 1):

        k      0.000   0.524   1.047   1.571   2.094   2.618   3.142
        E(k)  -1.666  -1.535  -1.149  -0.535  +0.265  +1.197  +2.197

      BANDWIDTH 3.86 (the 4t cos-envelope), max group velocity
      1.91: A PROPAGATING MODE.  Under the free BF measure
      V = +infinity, no state of nonzero curvature exists at any
      energy, and the band is empty.  The ledger's square is
      exactly what converts an infinitely-costly frozen constraint
      into a finite-price, dispersing excitation.

Run directly for the verification suite.
"""

from __future__ import annotations

import cmath
import itertools
import math

TAU = 2 * math.pi


# =====================================================================
# battery instrument: the induced flux measure
# =====================================================================

def weight_fn(measure, N):
    """W(F): the budget weight of 0053."""
    if measure == "square":
        def W(F):
            F %= N
            return math.gcd(F if F else N, N) / N
    else:
        def W(F):
            return 1.0 if F % N == 0 else 0.0
    return W


def flux_expectations(N, L, measure, src, regions):
    """Exact <omega^{sum_R F}> over all flux configs with sum F = 0."""
    P = L * L
    om = cmath.exp(2j * math.pi / N)
    W = weight_fn(measure, N)
    Z = 0.0
    acc = [0j] * len(regions)
    for c in itertools.product(range(N), repeat=P - 1):
        F = c + ((-sum(c)) % N,)
        w = 1.0
        for p in range(P):
            w *= W(F[p] - src.get(p, 0))
            if w == 0.0:
                break
        if w == 0.0:
            continue
        Z += w
        for ri, R in enumerate(regions):
            acc[ri] += w * om ** (sum(F[p] for p in R) % N)
    return [a / Z for a in acc], Z


REGIONS = [(0,), (0, 1), (0, 1, 3, 4), (1,), (1, 2, 4, 5)]
LABELS = ["p0 (encloses the mass)", "p0 + p1", "2x2 block with mass",
          "p1 (encloses nothing)", "2x2 block, empty"]
PAIR = {0: 1, 8: -1}


# =====================================================================
# 1. the deficit, computed
# =====================================================================

def verify_deficit() -> None:
    ex, Z = flux_expectations(3, 3, "square", PAIR, REGIONS)
    exact = TAU / 3
    for lab, v in zip(LABELS, ex):
        print(f"    {lab:24s}: |W| {abs(v):.4f}   phase "
              f"{cmath.phase(v):+.5f}")
    for i in (0, 1, 2):
        assert abs(cmath.phase(ex[i]) - exact) < 1e-9, (i, ex[i])
    for i in (3, 4):
        assert abs(cmath.phase(ex[i])) < 1e-9, (i, ex[i])
    print(f"    2 pi n/N = {exact:+.5f}")
    print()
    print("  THE PHASE IS EXACTLY THE CLASSICAL DEFICIT, for every")
    print("  loop enclosing the mass -- whatever its size or shape --")
    print("  and exactly zero otherwise.  The conical defect of")
    print("  0014/0027, recovered as a quantum expectation value.")
    print()
    print("    level N:  phase of the enclosing loop vs 2 pi/N")
    for N in (2, 3, 4, 5):
        e2, _ = flux_expectations(N, 3, "square", PAIR,
                                  [(0,), (1,)])
        ph = cmath.phase(e2[0])
        assert abs(ph - TAU / N) < 1e-9, (N, ph)
        assert abs(cmath.phase(e2[1])) < 1e-9
        print(f"      N = {N}: {ph:+.5f}  vs  {TAU / N:+.5f}   "
              f"(|W| = {abs(e2[0]):.4f})")
    print("    -> 0 as N -> infinity: the classical continuum.")


# =====================================================================
# 2. the quantum correction
# =====================================================================

def verify_fluctuation() -> None:
    rigid, _ = flux_expectations(3, 3, "uniform", PAIR, REGIONS)
    soft, _ = flux_expectations(3, 3, "square", PAIR, REGIONS)
    print("    loop                      free BF        squared (ledger)")
    for lab, r, s in zip(LABELS, rigid, soft):
        print(f"    {lab:24s}  |W| {abs(r):.4f}     |W| {abs(s):.4f}")
        assert abs(abs(r) - 1.0) < 1e-9, (lab, r)
    for i in (0, 1, 2):
        assert abs(cmath.phase(rigid[i]) - TAU / 3) < 1e-9
    assert abs(soft[2]) < 0.5 * abs(soft[0])
    print()
    print("  SAME DEFICIT, DIFFERENT GEOMETRY.  Under free BF the")
    print("  magnitude is 1.0000 at every loop: the deficit exists")
    print("  but the geometry is RIGID.  Under the ledger's squared")
    print("  measure the magnitude falls with the loop's AREA -- a")
    print("  zero-point curvature fluctuation with no classical")
    print("  counterpart.  The square is what makes geometry jitter.")


# =====================================================================
# 3. the lattice graviton
# =====================================================================

def pair_dispersion(N=3, L=12, t=1.0):
    """Lowest energy of a +/- curvature pair at CoM momentum k.
    Both ends hop, so the relative hopping is -2t cos(k/2)."""
    V1 = math.log(N / math.gcd(1, N))
    n = L - 1

    def lowest(k):
        hop = -2 * t * math.cos(k / 2)
        diag = [2 * V1] * n
        shift = 20.0
        v = [1.0 / (i + 1) for i in range(n)]
        for _ in range(6000):
            w = [0.0] * n
            for i in range(n):
                w[i] += (shift - diag[i]) * v[i]
                if i > 0:
                    w[i] += -hop * v[i - 1]
                if i < n - 1:
                    w[i] += -hop * v[i + 1]
            nr = math.sqrt(sum(x * x for x in w))
            v = [x / nr for x in w]
        Hv = [0.0] * n
        for i in range(n):
            Hv[i] += diag[i] * v[i]
            if i > 0:
                Hv[i] += hop * v[i - 1]
            if i < n - 1:
                Hv[i] += hop * v[i + 1]
        return sum(v[i] * Hv[i] for i in range(n))
    ks = [math.pi * m / 6 for m in range(7)]
    return ks, [lowest(k) for k in ks], V1


def verify_graviton() -> None:
    ks, Es, V1 = pair_dispersion()
    print(f"    on-site price V = log(N/gcd(1,N)) = {V1:.4f} per")
    print(f"    curvature quantum; quanta exist only in +/- pairs")
    print(f"    (sum F = 0 -- the closed-universe budget).")
    print("    centre-of-mass dispersion:")
    for k, E in zip(ks, Es):
        print(f"      k = {k:.4f}:  E = {E:+.5f}")
    band = max(Es) - min(Es)
    vg = max(abs((Es[i + 1] - Es[i]) / (ks[i + 1] - ks[i]))
             for i in range(len(ks) - 1))
    assert band > 3.0, band
    assert vg > 1.0, vg
    for i in range(len(Es) - 1):
        assert Es[i + 1] > Es[i], (i, Es)
    print(f"    bandwidth {band:.4f}; max group velocity "
          f"{vg:.4f} -> PROPAGATES")
    print()
    print("  THE LATTICE GRAVITON.  The plaquette price is the")
    print("  on-site energy, the electric term is the hopping, and")
    print("  the curvature quantum disperses.  Under free BF the")
    print("  price is infinite: no state of nonzero curvature exists")
    print("  at any energy and the band is EMPTY.  The ledger's")
    print("  square is exactly what turns an infinitely costly frozen")
    print("  constraint into a finite-price, dispersing excitation --")
    print("  0050's classical count 0 -> 2, now as a spectrum.")


def run_verification_suite() -> None:
    sections = [
        ("The deficit, computed from the quantum model",
         verify_deficit),
        ("The quantum correction: rigid vs fluctuating geometry",
         verify_fluctuation),
        ("The lattice graviton", verify_graviton),
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
