"""0125 -- the port audit: which results live in the continuous
theory and which never left the Z_N toy.

Z_N was always a toy -- the exactly-solvable tier where this
program's theorems were first proven, before being lifted to SU(2).
That is the program's own framing (0074 lifts the Born square from
Z_N to SU(2) explicitly). So a fair question is which of the
program's standing claims are statements about the continuous theory
and which are statements about the toy.

This module audits three: requirement (A), requirement (C), and the
level N. Two survive intact. The third does not, and the part that
fails is one I asserted as recently as lucid 0041.

  s1  (A) IS CONTINUOUS. The interacting measure that the whole
      continuity front was measured on is 4D SU(2) -- unit
      quaternions, a continuous group. Verified mechanically: the
      modules carrying those results are scanned for any Z_N
      construction, and there is none.
  s2  (C) IS CONTINUOUS. The area law, Unruh and horizon
      thermodynamics come from a free scalar / graviton field and a
      continuum PDE. Same scan, same answer.
  s3  N IS HALF-PORTED, AND THE MISSING HALF IS THE LADDER.
        - band-as-budget (0118): SU(2)-native. Supporting N sectors
          costs ln N nats, measured with SU(2) characters.
        - N = exp(capacity) (lucid 0041 s1-s2): a phase circle at
          finite resolution. No finite ring anywhere.
        - THE ADMISSIBLE LADDER (0081's congruence, 0090's even
          wall, and lucid 0041 s3-s4): Z_N ONLY. Measured here:
          at the SU(2) tier EVERY level gives a nonnegative,
          reflection-positive weight with band 2M-1. There is no
          parity obstruction and no congruence obstruction. The
          sieve that produced 5, 13, 17, 25, 29, 37 is a property
          of the toy.
  s4  WHAT THAT COSTS. The ladder was the support of the level's
      prior. Without it, 0106's n* = 58 prices a measurement over a
      much larger candidate set, and the level-selection problem is
      LARGER than the board says, not smaller.
"""

import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

TH = np.linspace(1e-9, np.pi - 1e-9, 200001)
HAAR = (2 / np.pi) * np.sin(TH) ** 2


def chi(n):
    return np.sin(n * TH) / np.sin(TH)


def coef(f, n):
    return float(np.trapezoid(f * chi(n) * HAAR, TH))


# a Z_N construction leaves fingerprints: roots of unity, gcd
# ledgers, modular reduction of a level
ZN_MARKS = (r"\bgcd\s*\(", r"omega\s*\*\*", r"\bZ_N\b", r"% *N\b",
            r"np\.gcd", r"gauss_sum", r"\bmod N\b")


def scan(files, label):
    print(f"  {label}")
    print("     module                                 Z_N "
          "fingerprints")
    clean = True
    for f in files:
        p = os.path.join(HERE, f)
        if not os.path.exists(p):
            print(f"     {f:38s} (absent)")
            continue
        src = open(p).read()
        hits = [m for m in ZN_MARKS if re.search(m, src)]
        if hits:
            clean = False
        print(f"     {f:38s} "
              f"{'none' if not hits else ', '.join(hits)}")
    return clean


def s1_A_is_continuous():
    print("== s1: (A) is continuous ==")
    print("  the interacting measure of the continuity front is 4D "
          "SU(2) -- unit quaternions")
    ok = scan(["0091_the_lattice_mc.py", "0092_the_coupling_scan.py",
               "0115_the_continuum_probe.py",
               "0116_deciding_the_branch.py",
               "0123_lorentz_as_code_length.py",
               "0124_the_nongaussian_direction.py"],
              "modules carrying (A) and the continuity results:")
    src = open(os.path.join(HERE, "0092_the_coupling_scan.py")).read()
    assert "qmul" in src and "arccos" in src
    print("  and 0092 composes with quaternion multiplication and "
          "reads a CLASS ANGLE:")
    print("  the state space is S^3, not a finite ring.")
    assert ok
    print("  (A) PORTED.\n")


def s2_C_is_continuous():
    print("== s2: (C) is continuous ==")
    ok = scan(["0073_the_half_space.py",
               "0104_the_horizon_thermodynamics.py",
               "0113_the_induced_stiffness.py"],
              "modules carrying (C):")
    assert ok
    print("  free scalar / graviton covariances and a continuum "
          "PDE relaxation. No finite")
    print("  ring anywhere. (C) PORTED.\n")


def s3_N_half_ported():
    print("== s3: N is half-ported, and the missing half is the "
          "ladder ==")
    print("  THE SU(2)-TIER TEST. Build the counting amplitude "
          "A = sum_{n=1..M} chi_n and its")
    print("  weight W = A^2 at every level, and ask whether an even "
          "or non-congruent level")
    print("  fails anything the continuous theory cares about:")
    print("     M    W >= 0    all char coeffs >= 0 (RP)    band"
          "    Z_N verdict")
    zn_ok = {1: 0, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0, 7: 1, 8: 0}
    for M in range(1, 9):
        A = sum(chi(n) for n in range(1, M + 1))
        W = A ** 2
        cs = [coef(W, n) for n in range(1, 3 * M)]
        band = max(i + 1 for i, c in enumerate(cs) if abs(c) > 1e-6)
        nn = bool(np.all(W >= -1e-9))
        rp = bool(min(cs) > -1e-6)
        assert nn and rp and band == 2 * M - 1
        print(f"     {M}    {str(nn):5s}     {str(rp):5s}"
              f"                    {band:3d}"
              f"     {'admissible' if zn_ok[M] else 'EXCLUDED'}")
    print()
    print("  EVERY LEVEL PASSES AT THE SU(2) TIER. Nonnegative, "
          "reflection positive, band")
    print("  2M-1, no exceptions -- while the Z_N tier excludes "
          "half of them.")
    print()
    print("  The two Z_N obstructions do not have continuum "
          "shadows:")
    print("   - the congruence (0081) asks whether sqrt(-1) exists "
          "IN THE BASE RING. Over C")
    print("     it does, trivially, and 0081 says so itself: the "
          "congruence is 'the continuum")
    print("     fact in arithmetic dress'. A fact wearing arithmetic "
          "dress constrains the")
    print("     arithmetic, not the continuum.")
    print("   - the even wall (0090) is about quadratic GAUSS SUMS "
          "over Z_N. SU(2) counting")
    print("     amplitudes have no parity structure to violate, as "
          "the table shows.")
    print()
    print("  WHAT DOES PORT: the band-as-budget argument (0118) is "
          "SU(2)-native -- sector j")
    print("  is read through |chi_j|^2 sin^2(theta) and supporting "
          "N sectors costs ln N nats.")
    print("  And lucid 0041's first half -- additivity + finite "
          "resolution forces a cyclic")
    print("  resolvable set, N = exp(capacity) -- is about a phase "
          "circle, with no finite")
    print("  ring in it. Its SECOND half (s3, s4) imported the Z_N "
          "ledger and the congruence,")
    print("  and I described the result as 'the ladder recovered "
          "with no geometry'. That was")
    print("  true and beside the point: I had removed the geometry "
          "and kept the toy.\n")


def s4_what_it_costs():
    print("== s4: what that costs ==")
    print("  The ladder was the SUPPORT OF THE LEVEL'S PRIOR. "
          "0106 priced level selection as")
    print("  n* = 58 vacuum samples to pin N 'whichever level is "
          "true' -- over the admissible")
    print("  ladder. Widen the candidate set from a sparse ladder "
          "to every level and that")
    print("  price goes UP: more candidates, and neighbouring "
          "levels are the hardest pairs")
    print("  to separate (0106's own worst case was 25 vs 29 at "
          "0.35-0.41 nats/sample).")
    print()
    print("  So the honest board correction is not cosmetic:")
    print("   - (A) and (C) stand, on the continuous theory.")
    print("   - N's DEFINITION ports: it is a sector budget, and a "
          "channel capacity.")
    print("   - N's CANDIDATE SET does not. 'The admissible ladder' "
          "should be labelled a")
    print("     Z_N-tier result everywhere it appears, including in "
          "the published summary")
    print("     of the level, and 0106's floor should be read as "
          "conditional on it.")
    print("   - requirement (D) is therefore HARDER than the board "
          "implied, not easier:")
    print("     the thing to derive is a level with no arithmetic "
          "sieve narrowing it.\n")


if __name__ == "__main__":
    s1_A_is_continuous()
    s2_C_is_continuous()
    s3_N_half_ported()
    s4_what_it_costs()
    print("all assertions passed")
