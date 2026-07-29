"""
Global-section test: "locally consistent, globally non-extendable" = quantum.

Pure standard library.

Demonstrates the central claim of the corrected (nonlocal) reading:

  A web of pairwise-consistent knowledge distributions is QUANTUM precisely when
  it admits NO single global joint distribution of definite values (no god's-eye
  view), even though every pairwise correlation is individually legitimate.

We use the CHSH scenario: two parties, each choosing one of two dichotomic
(+/-1) observables A,A' and B,B'.  Correlators E(XY) = <X.Y>.

Fine's theorem: a global joint distribution over (A,A',B,B') reproducing the
four correlators exists  <=>  all eight CHSH facet inequalities hold:

        | E(AB) s1 + E(AB') s2 + E(A'B) s3 + E(A'B') s4 | <= 2

for the four sign patterns with an odd number of minus signs (equivalently the
standard S = E(AB)+E(AB')+E(A'B)-E(A'B') and its symmetry group).

  - Bell-local (classical) correlators  -> all facets hold  -> global section EXISTS.
  - Tsirelson (quantum) correlators     -> a facet is violated -> NO global section,
    yet each correlator has |E| < 1 and is individually realizable.

This is the formal content of "mutual consistency but no absolute source of
truth": the pairwise views cohere, but there is no global joint they all come
from.  That non-extendability IS the quantumness.

Run:  python3 0002_global_section_test.py
"""

from itertools import product
import math


def deterministic_vertices():
    """The 16 definite global assignments (a,a',b,b') in {+1,-1}^4 and their
    correlator vectors (E_AB, E_AB', E_A'B, E_A'B').  Any global joint is a
    convex combination of these; their hull is the local (Bell) polytope."""
    verts = []
    for a, ap, b, bp in product((+1, -1), repeat=4):
        verts.append(((a, ap, b, bp), (a * b, a * bp, ap * b, ap * bp)))
    return verts


def chsh_facets(E):
    """Return the max |signed sum| over the 4 CHSH sign patterns (odd # of -).
    Global section exists iff this is <= 2 (Fine's theorem)."""
    E_AB, E_ABp, E_ApB, E_ApBp = E
    combos = [
        E_AB + E_ABp + E_ApB - E_ApBp,
        E_AB + E_ABp - E_ApB + E_ApBp,
        E_AB - E_ABp + E_ApB + E_ApBp,
        -E_AB + E_ABp + E_ApB + E_ApBp,
    ]
    return max(abs(c) for c in combos)


def report(name, E):
    s = chsh_facets(E)
    exists = s <= 2 + 1e-12
    each_ok = all(abs(e) <= 1 + 1e-12 for e in E)
    print(f"{name}")
    print(f"    correlators (E_AB, E_AB', E_A'B, E_A'B') = "
          f"({E[0]:+.4f}, {E[1]:+.4f}, {E[2]:+.4f}, {E[3]:+.4f})")
    print(f"    each |E| <= 1 (individually legitimate): {each_ok}")
    print(f"    max CHSH facet value = {s:.4f}   (threshold 2)")
    print(f"    GLOBAL SECTION (single joint of definite values) EXISTS: {exists}")
    print(f"    => {'classical / Bell-local' if exists else 'QUANTUM: locally consistent, globally NON-extendable'}")
    print()
    return exists


if __name__ == "__main__":
    verts = deterministic_vertices()
    print(f"Local polytope = convex hull of {len(verts)} deterministic assignments.")
    print("Sample vertices (assignment -> correlators):")
    for assign, corr in verts[:3]:
        print(f"    {assign} -> {corr}")
    print()

    inv = 1.0 / math.sqrt(2.0)  # Tsirelson correlator magnitude

    r1 = report("Classical target (S = 2, boundary of local set):",
                (0.5, 0.5, 0.5, -0.5))
    r2 = report("Tsirelson target (quantum optimum, S = 2*sqrt(2)):",
                (inv, inv, inv, -inv))
    r3 = report("PR-box target (super-quantum, S = 4):",
                (1.0, 1.0, 1.0, -1.0))

    ok = (r1 is True) and (r2 is False) and (r3 is False)
    print("EXPECTED: classical has a global section; quantum and super-quantum do not.")
    print("RESULT:", "OK" if ok else "MISMATCH")
