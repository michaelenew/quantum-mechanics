"""0071 -- the open budget: what Sum F = 0 becomes off the closed surface.

The closed-universe budget Sum F = 0 (mod N) was derived on closed
lattices (0053) and reappeared as the deleted k = 0 mode (0057) and the
measure's sole divergence W-hat(0) ~ P(N)/phi(N) (0064). 0069 SS2 step 1
asked what the budget becomes on an open arena. Answered here by exact
enumeration, no sampling:

  s1  A disk has NO budget: every flux configuration is attained with
      identical multiplicity N^(V-1) (pure gauge volume). The constraint
      was the closure of the surface, not the dynamics.
  s2  Freezing the boundary restores it as a boundary condition:
      Sum F = hol(boundary), exactly, for every boundary assignment.
      The open-universe budget is Stokes' theorem mod N.
  s3  The torus control: Sum F = 0 recovered, multiplicity
      N^(V-1) x N^2 (gauge x two Wilson-line moduli).
  s4  The toy Lambda: on the free disk the total curvature Sum F is an
      observable with exact distribution
        P(h) = (1/N) Sum_n (W-hat(n)/W-hat(0))^Plaq * omega^{nh},
      quantized in units 2pi/N and approaching the UNIFORM distribution
      at rate r_max^Plaq where r_max = max_{n!=0} W-hat(n)/W-hat(0).
      For prime N, r_max = phi(N)/P(N) = f(N) -- the confinement/jitter
      base. For composite N the slowest mode is the coarsest subgroup:
      the fine structure of the budget dies first, the mod-(smallest
      prime) residue last.

Everything is exact integer/rational arithmetic except the final decay
ratios (floats compared at 1e-12).
"""

import itertools
import math
from collections import Counter
from fractions import Fraction
from math import gcd

import random


# ----------------------------------------------------------------------
# lattice helpers
# ----------------------------------------------------------------------

def disk_2x2():
    """2x2 plaquettes on a 3x3 vertex grid: 12 edges.

    Edge indexing: h(i,j): (i,j)->(i+1,j) for i in 0..1, j in 0..2 are
    edges 0..5; v(i,j): (i,j)->(i,j+1) for i in 0..2, j in 0..1 are
    edges 6..11.
    """
    EH = {(i, j): i + 2 * j for j in range(3) for i in range(2)}
    EV = {(i, j): 6 + i + 3 * j for j in range(2) for i in range(3)}

    def fluxes(a, N):
        out = []
        for j in range(2):
            for i in range(2):
                F = (a[EH[(i, j)]] + a[EV[(i + 1, j)]]
                     - a[EH[(i, j + 1)]] - a[EV[(i, j)]]) % N
                out.append(F)
        return tuple(out)

    boundary = [EH[(0, 0)], EH[(1, 0)], EH[(0, 2)], EH[(1, 2)],
                EV[(0, 0)], EV[(0, 1)], EV[(2, 0)], EV[(2, 1)]]
    interior = [e for e in range(12) if e not in boundary]

    def boundary_holonomy(a, N):
        # counterclockwise around the outer square from (0,0)
        return (a[EH[(0, 0)]] + a[EH[(1, 0)]]
                + a[EV[(2, 0)]] + a[EV[(2, 1)]]
                - a[EH[(1, 2)]] - a[EH[(0, 2)]]
                - a[EV[(0, 1)]] - a[EV[(0, 0)]]) % N

    return fluxes, boundary, interior, boundary_holonomy


def torus_2x2_fluxes(a, N):
    """2x2 torus: 4 vertices (i,j), 8 edges. a[0..3]=h(i,j) at index
    i+2j, a[4..7]=v(i,j) at index 4+i+2j."""
    out = []
    for j in range(2):
        for i in range(2):
            F = (a[i + 2 * j] + a[4 + ((i + 1) % 2) + 2 * j]
                 - a[i + 2 * ((j + 1) % 2)] - a[4 + i + 2 * j]) % N
            out.append(F)
    return tuple(out)


def ledger(F, N):
    """The divisor-ensemble weight: W(F) = gcd(F, N), with W(0) = N."""
    return gcd(F, N) if F else N


def what(n, N):
    """Exact dual ledger weight, from gcd = sum_{d|N} phi(d) [d|F]:

        W-hat(n) = sum_F W(F) omega^{nF}
                 = sum_{d|N, (N/d) | n} phi(d) * (N/d)      (an integer)
    """
    tot = 0
    for d in range(1, N + 1):
        if N % d:
            continue
        if n % (N // d) == 0:
            phi = sum(1 for k in range(1, d + 1) if gcd(k, d) == 1)
            tot += phi * (N // d)
    return tot


# ----------------------------------------------------------------------
# s1 -- the disk has no budget
# ----------------------------------------------------------------------

def s1_disk_free(N=3):
    print(f"== s1: free-boundary disk (2x2 plaquettes, N={N}) ==")
    fluxes, _, _, _ = disk_2x2()
    cnt = Counter()
    for a in itertools.product(range(N), repeat=12):
        cnt[fluxes(a, N)] += 1
    mults = set(cnt.values())
    print(f"  attained flux combos : {len(cnt)}  (all of N^4 = {N**4})")
    print(f"  multiplicity         : {mults}  (gauge volume N^(V-1) = "
          f"{N**8})")
    assert len(cnt) == N ** 4, "some flux configuration unattained"
    assert mults == {N ** 8}, "multiplicity not uniform -- constraint?"
    sums = {sum(f) % N for f in cnt}
    print(f"  attained Sum F mod N : {sorted(sums)}  -- every value, "
          f"no budget\n")
    assert sums == set(range(N))


# ----------------------------------------------------------------------
# s2 -- freezing the boundary restores the budget as Stokes mod N
# ----------------------------------------------------------------------

def s2_disk_frozen(N=3, trials=6, seed=5):
    print(f"== s2: frozen-boundary disk (N={N}, {trials} random "
          f"boundaries) ==")
    fluxes, boundary, interior, bhol = disk_2x2()
    rng = random.Random(seed)
    for t in range(trials):
        a = [0] * 12
        for e in boundary:
            a[e] = rng.randrange(N)
        hol = bhol(a, N)
        seen = Counter()
        for iv in itertools.product(range(N), repeat=len(interior)):
            for e, v in zip(interior, iv):
                a[e] = v
            seen[fluxes(a, N)] += 1
        sums = {sum(f) % N for f in seen}
        mult = set(seen.values())
        print(f"  boundary {t}: hol = {hol}; attained Sum F = {sums}; "
              f"combos = {len(seen)}, mult = {mult}")
        assert sums == {hol}, "budget != boundary holonomy"
        assert len(seen) == N ** 3 and mult == {N}, \
            "interior gauge volume wrong"
    print("  Sum F = hol(boundary) exactly, every trial -- the open "
          "budget is Stokes mod N\n")


# ----------------------------------------------------------------------
# s3 -- torus control: the closed budget recovered
# ----------------------------------------------------------------------

def s3_torus(N=3):
    print(f"== s3: 2x2 torus control (N={N}) ==")
    cnt = Counter()
    for a in itertools.product(range(N), repeat=8):
        cnt[torus_2x2_fluxes(a, N)] += 1
    sums = {sum(f) % N for f in cnt}
    print(f"  attained Sum F mod N : {sorted(sums)}  (closed budget)")
    print(f"  combos = {len(cnt)} (= N^3), mult = {set(cnt.values())} "
          f"(= N^(V-1) x N^2 Wilson moduli = {N**5})\n")
    assert sums == {0}
    assert len(cnt) == N ** 3 and set(cnt.values()) == {N ** 5}


# ----------------------------------------------------------------------
# s4 -- the toy Lambda: distribution of the total curvature
# ----------------------------------------------------------------------

def _ph_exact(N):
    """The exact n-spectrum W-hat(n)/W-hat(0) as Fractions; the free-disk
    distribution is P(h) = (1/N) sum_n (spectrum_n)^Plaq omega^{nh}."""
    W0 = what(0, N)
    return [Fraction(what(n, N), W0) for n in range(N)]


def s4_toy_lambda():
    print("== s4: the toy Lambda -- total curvature on the free disk ==")

    # (a) validate the dual formula against direct weighted enumeration
    N = 3
    fluxes, _, _, _ = disk_2x2()
    num = [0] * N
    den = 0
    for combo in itertools.product(range(N), repeat=4):
        w = 1
        for F in combo:
            w *= ledger(F, N)
        num[sum(combo) % N] += w
        den += w
    ratios = _ph_exact(N)
    for h in range(N):
        dual = sum(float(ratios[n]) ** 4 * math.cos(2 * math.pi * n * h / N)
                   for n in range(N)) / N
        enum = num[h] / den
        assert abs(dual - enum) < 1e-12, (h, dual, enum)
    print(f"  dual formula == weighted enumeration at N=3, P=4 "
          f"(max diff < 1e-12)")

    # (b) quantization + approach to uniformity, prime N
    r1 = ratios[1]
    fN = Fraction(2, 5)  # phi(3)/P(3)
    assert r1 == fN, "rate is not f(N) = phi/P at prime N"
    print(f"  N=3 : values of Lambda-residual = 2 pi h / 3, h in Z_3")
    print(f"        r_max = W-hat(1)/W-hat(0) = {r1} = phi(3)/P(3) "
          f"= f(3)")
    prev = None
    for P in (4, 16, 64):
        dev = sum(float(ratios[n]) ** P * math.cos(0.0)
                  for n in range(1, N)) / N   # P(0) - 1/N
        print(f"        P={P:3d}: P(h=0) - 1/N = {dev:.3e}   "
              f"f^P = {float(fN)**P:.3e}")
        if prev is not None:
            ratio = dev / prev[0]
            expect = float(fN) ** (P - prev[1])
            assert abs(ratio / expect - 1.0) < 1e-9
        prev = (dev, P)

    # (c) composite N: the coarsest subgroup dies last
    N = 15
    ratios = _ph_exact(N)
    W0 = what(0, N)
    tbl = sorted({(gcd(n, N), what(n, N)) for n in range(1, N)})
    print(f"  N=15: P(15) = {W0}; dual weights by gcd(n,15): " +
          ", ".join(f"gcd {g}: {w} (r={Fraction(w, W0)})"
                    for g, w in tbl))
    rmax = max(Fraction(what(n, N), W0) for n in range(1, N))
    nstar = [n for n in range(1, N)
             if Fraction(what(n, N), W0) == rmax]
    print(f"        r_max = {rmax} at n = {nstar} -- gcd 3 modes")
    assert rmax == Fraction(20, 45) and all(gcd(n, 15) == 3
                                            for n in nstar)
    # the surviving deviation at large P depends on h only mod 5:
    # sum over n in {3,6,9,12} of omega^{nh} = 5*[5|h] - 1
    P = 256
    devs = [sum(float(Fraction(what(n, N), W0)) ** P
                * math.cos(2 * math.pi * n * h / N)
                for n in range(1, N)) / N for h in range(N)]
    lead = [(5 * (1 if h % 5 == 0 else 0) - 1) * float(rmax) ** P / N
            for h in range(N)]
    err = max(abs(d - l) for d, l in zip(devs, lead))
    assert err < abs(max(lead)) * 1e-6
    print(f"        P={P}: deviation from uniform = "
          f"(5[5|h]-1)/15 * r_max^P to 1e-6 relative --")
    print(f"        the residual Lambda equilibrates mod 15 fast, "
          f"mod 5 last: fine budget structure dies first\n")


if __name__ == "__main__":
    s1_disk_free(N=3)
    s2_disk_frozen(N=3)
    s3_torus(N=3)
    s4_toy_lambda()
    print("all assertions passed")
