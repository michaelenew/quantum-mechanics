# 0120 — Closing the three: the square is a restriction, the level agreement is coincidence, induced gravity keeps its test

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

The three standing questions, closed. Code:
`output/0110_the_three_closures.py`.

## 1. The SU(2) Fejér–Riesz statement is **false** — with a criterion

0119 proved on U(1) that nonnegative + band-limited ⟹ squared, and
conjectured the SU(2) analogue. **It is refuted.** Generic
nonnegative class functions with character support ≤ 2J are *not*
|A|² for any A supported ≤ J: 200-restart Levenberg–Marquardt solves
plateau at residuals of 0.04–5.7 where genuine solutions land at
4e−16.

And the obstruction is identifiable. An amplitude's polynomial is
**anti-palindromic** (its coefficients antisymmetric about the
middle), so its root set is closed under r ↦ 1/r; Fejér–Riesz
forces exactly one root from each *conjugate-reciprocal* pair. For a
**real** pair {r, 1/r} those two demands conflict. Hence:

> **Criterion.** W factors as |A|² with A band-limited to half
> iff F(z) — the polynomial form of W·sin²θ — has **no real
> off-circle roots**.

Verified: the criterion agrees with the solver on **6/6** trials
(0 real off-circle roots ⟺ factors; 4 ⟺ does not).

**Consequence for the program.** On the tier where its physics
actually lives, **the Born square is not free**. Band-limiting is a
budget (0118); *squaring is extra structure*, and the physical
weight sits in a proper subclass — characterised here for the first
time. This corrects 0119's conjecture and, notably, *agrees* with
everything the program found from three other directions: record
noise cannot make nodes (lucid 0027), amplitudes never pay on
classical streams (lucid 0005), and monogamy lives in the source
ledger (lucid 0024). The two-ledger split is not an artifact of
where we looked.

## 2. The level agreement is a coincidence of scale

The **arithmetic** constraint (0081) gives an admissible ladder; the
**budget** (0118) gives a cost per level; 0106 gives a pinning cost.
If the two costs tracked each other across the ladder, that would be
a hidden identity. They do not:

| N | pinning cost | budget cost | ratio |
|---|---|---|---|
| 5 | 7.0 | 364.7 | 52.0 |
| 13 | 26.0 | 303.5 | 11.7 |
| 17 | 34.2 | 322.7 | 9.4 |
| 25 | 46.7 | 369.4 | 7.9 |
| 29 | 54.7 | 393.3 | 7.2 |

The ratio drifts by **7.2×** across the ladder. So the numerical
agreement at N = 5 (~47 vs 58 in 0118's normalisation) is
**coincidence at one point, not a law**. The level remains a
measured constant on an arithmetically constrained ladder — exactly
what 0106 priced. *Question closed as "no law here", which is an
answer.*

## 3. Induced gravity: a hypothesis with a named test

**Status.** S_horizon = S_entanglement fixes G = 5.17 a² (ℓ_P =
2.27 a) from the measured area law (0115); the independent
information/geometry crossover at √3 = 1.73 a agrees to 31% (0117).
Evidence, not proof.

**The test that would settle it.** Measure G *directly*: insert a
known information source into the lattice trust field and read the
coefficient of its 1/r response in lattice units. That number is
independent of both the area law and the induced-gravity
assumption. Better-than-31% agreement confirms; disagreement
refutes. It needs the vertex-corrected measure (0112/0116) trusted
at the percent level, which is why it is named rather than run —
the one honest "not yet" left on the board.
