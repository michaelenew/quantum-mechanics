# 0160 — Item 6 closed: the difference is diffeomorphism invariance, measured

> **AI-generated, not peer-reviewed.** Code:
> `output/0150_diffeo_invariance.py`. Closes the thread 0145 → 0146 →
> 0154 → 0156 → 0158 → 0159.

Rather than rebuild the constrained sector, this tests the **property
that separates the two routes** — and it turns out to settle the
question.

## s1 — Einstein-Hilbert is forced, not assumed

Build the general **local**, two-derivative quadratic form in h — four
scalars, `k²h·h`, `k²(tr h)²`, `|k·h|²`, `(khk)(tr h)` — and demand it
annihilate every gauge mode `h → h + kξ + ξk`.

| trial (random k) | null dim | coefficients |
|---|---|---|
| 0 | **1** | (1, −1, −2, 2) |
| 1 | **1** | (1, −1, −2, 2) |
| 2 | **1** | (1, −1, −2, 2) |

Momentum-independent to **3.77e−15**. Those are exactly the linearised
Einstein-Hilbert coefficients.

> **GR is not assumed anywhere here — it is forced** by locality, two
> derivatives, and diffeomorphism invariance. That is why invariance
> is the right thing to test: anything with it *is* Einstein; anything
> without it is free to be anything at all.

*(A first pass included a fifth scalar `(khk)²/k²`. It is
two-derivative by power counting but **non-local** — it is R²_lin/k² —
and it made the family two-dimensional. Locality is a physical
requirement, and excluding it collapses the family to one.)*

## s2 — The induced kernel does not have it

Same test on the lattice, with lattice momenta and the matching
lattice gauge mode:

| k | k̂² | EH violation | induced violation | ratio |
|---|---|---|---|---|
| (0,1,0,0) | 0.268 | 1.789e−16 | 3.020e−01 | 1.7e15 |
| (0,2,0,0) | 1.000 | 1.813e−16 | 2.966e−01 | 1.6e15 |
| (0,1,1,0) | 0.536 | 2.143e−16 | 3.329e−01 | 1.6e15 |
| (0,2,1,1) | 1.536 | 1.477e−16 | 3.506e−01 | 2.4e15 |
| (0,3,0,0) | 2.000 | 1.813e−16 | 2.903e−01 | 1.6e15 |
| (0,3,2,1) | 3.268 | 1.908e−16 | 3.472e−01 | 1.8e15 |

**And the decisive column is k̂².** An O(a²) lattice artifact would
scale as k̂², i.e. exponent +1. Measured: k̂² varies by a factor
**12.2**, the violation by a factor **1.21** —

> **violation ~ (k̂²)^{+0.029}. Flat in k.** The breaking is *not* an
> irrelevant artifact that dies in the continuum. It is real and
> unsuppressed.

So nothing forbids a cosmological constant or a graviton mass in the
induced route, and both duly appeared at the cutoff scale (0159). That
is the complete diagnosis of γ = −1 → +0.509: **it is what a
non-invariant kernel does.**

## s3 — Where the constrained sector gets it

The derived weight is `A(U⁺,U⁻) = Σ_j n_j χ_j(U⁺)χ_j(U⁻)` — a sum over
the **diagonal** j⁺ = j⁻. Those are the **balanced representations**,
and restricting to them *is* the simplicity constraint B = e∧e
(equivalently |B⁺| = |B⁻|, which lucid 0045 verified machine-exact).

An *unconstrained* weight would **factorise** into two independent
SU(2) gauge theories — no gravity. So: does the derived weight
factorise? Singular values of the 2-D weight table, normalised:

    1.00000  0.73764  0.12579  0.09777  0.06018  0.05235  ~1e-16 ...

**Numerical rank 6, not 1.** The second singular value is 0.7376 of
the first. The weight does not factorise, and that non-factorisability
is exactly what 0142 measured as **synergy** — residual spread 1.0000
given either stream alone, 0.0000 given both.

> **The synergy is the simplicity constraint, seen from the
> information side.**

0050 counted the consequence: free BF has **0** physical degrees of
freedom, imposing simplicity gives **2**. The classical tier measured
the payoff: bending **0.008046** against GR's 0.008000.

## The close-out

**Item 6's question — does the quantum tier pass the classical tests —
now has a complete answer.**

- **The induced-matter sector fails, and the reason is measured, not
  guessed.** It is not diffeomorphism invariant, by 15 orders of
  magnitude, and the breaking does not vanish in the continuum. So it
  generates a cutoff-scale Λ and a graviton mass; cancelling the first
  is forced and yields γ = +0.509, the vDVZ value; the residual mass
  is the gap to +1, which 0056 had already identified as
  off-criticality.
- **The constrained sector is where GR lives.** By s1's uniqueness,
  *any* local two-derivative diffeomorphism-invariant kernel is
  Einstein-Hilbert, hence γ = +1. This is not a separate computation
  to be run — it is forced, provided the sector is invariant.
- **The program's own weight sits on the constrained side**, and does
  so by construction rather than by tuning: balanced representations,
  rank 6 not 1, 0142's synergy.

**What remains, stated so it is not mistaken for done:** the lattice
constrained-BF kernel has not itself been put through the s2 test. The
uniqueness theorem gives γ = +1 *given* invariance, and a lattice
realisation must be checked rather than assumed — a lattice breaks
diffeomorphisms somewhere, and the question is whether it breaks them
at EH's 1e−16 level or the induced route's 0.30. That single
measurement, not a new derivation, is what would turn "forced" into
"verified".

Items 4 and 5's numbers are unaffected either way: they measure the
induced scale stiffness, which is a real quantity. What 0156 got wrong
was calling it Newton's constant, and what 0159 got wrong before that
was measuring it at a non-stationary point.
