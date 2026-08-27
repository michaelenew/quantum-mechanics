# 0136 — The port audit: (A) and (C) survive, the ladder does not

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Code: `output/0125_the_port_audit.py`. An audit, prompted by a
direct challenge: *Z_N was always a toy — confirm (A), (C) and N are
ported to the full continuous theory.*

Two survive intact. The third does not, and the part that fails is
one I asserted as recently as yesterday.

## 1. (A) is continuous — ported

The interacting measure the entire continuity front was measured on
is **4D SU(2)**: unit quaternions, a continuous group. Scanned
mechanically for Z_N fingerprints (roots of unity, gcd ledgers,
modular reduction of a level):

| module | Z_N fingerprints |
|---|---|
| 0091 the lattice MC | none |
| 0092 the coupling scan | none |
| 0115 the continuum probe | none |
| 0116 deciding the branch | none |
| 0123 Lorentz as code length | none |
| 0124 the non-Gaussian direction | none |

0092 composes with quaternion multiplication and reads a **class
angle**. The state space is S³, not a finite ring. **(A) ported.**

## 2. (C) is continuous — ported

Same scan over the area law, horizon thermodynamics and induced
stiffness: **none**. Free scalar / graviton covariances and a
continuum PDE relaxation. **(C) ported.**

## 3. N is half-ported, and the missing half is the ladder

**What ports.** The band-as-budget argument (0118) is SU(2)-native:
sector j is read through |χ_j|²sin²θ, and supporting N sectors costs
ln N nats. lucid 0041's first half — additivity plus finite
resolution forces a cyclic resolvable set, N = exp(capacity) — is
about a phase circle, with no finite ring in it.

**What does not.** The SU(2)-tier test, run on every level:

| M | W ≥ 0 | all char coeffs ≥ 0 (RP) | band | Z_N verdict |
|---|---|---|---|---|
| 1 | ✓ | ✓ | 1 | EXCLUDED |
| 2 | ✓ | ✓ | 3 | EXCLUDED |
| 3 | ✓ | ✓ | 5 | admissible |
| 4 | ✓ | ✓ | 7 | EXCLUDED |
| 5 | ✓ | ✓ | 9 | admissible |
| 6 | ✓ | ✓ | 11 | EXCLUDED |
| 7 | ✓ | ✓ | 13 | admissible |
| 8 | ✓ | ✓ | 15 | EXCLUDED |

> **Every level passes at the SU(2) tier** — nonnegative, reflection
> positive, band 2M−1, no exceptions — while the Z_N tier excludes
> half of them.

Neither obstruction has a continuum shadow:

- **The congruence** (0081) asks whether √−1 exists *in the base
  ring*. Over ℂ it does, trivially — and 0081 says so itself, calling
  the congruence "the continuum fact in arithmetic dress." A fact
  wearing arithmetic dress constrains the arithmetic, not the
  continuum.
- **The even wall** (0090) is about quadratic **Gauss sums** over
  Z_N. SU(2) counting amplitudes have no parity structure to
  violate, as the table shows.

**And this corrects me.** lucid 0041's second half imported the Z_N
ledger and the congruence, and I described the result as "the ladder
recovered from the source ledger with no geometry." That was true
and beside the point: I had removed the geometry and kept the toy.

## 4. What it costs

The ladder was **the support of the level's prior**. 0106 priced
level selection at n\* = 58 vacuum samples to pin N "whichever level
is true" — over the *admissible ladder*. Widen the candidate set
from a sparse ladder to every level and that price goes **up**: more
candidates, and neighbouring levels are the hardest pairs to
separate (0106's own worst case was 25 vs 29 at 0.35–0.41
nats/sample).

The board corrections are not cosmetic:

- **(A) and (C) stand**, on the continuous theory.
- **N's definition ports**: a sector budget, and a channel capacity.
- **N's candidate set does not.** "The admissible ladder" must be
  labelled a Z_N-tier result everywhere it appears, and 0106's floor
  read as conditional on it.
- **Requirement (D) is harder than the board implied**, not easier:
  the thing to derive is a level with no arithmetic sieve narrowing
  it.

## 5. The honest summary

The challenge was right. Two of three port; the third ports as a
*definition* and not as a *constraint*. The program's exactly-solvable
tier did what toys do — it made theorems provable — and one of those
theorems turned out to be about the toy.
