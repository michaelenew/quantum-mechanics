# 0156 — Item 6, the fix run: γ = −1 survives, and the reason is algebraic

> **AI-generated, not peer-reviewed.** Code:
> `output/0146_offdiagonal_metric.py`. Supersedes 0154's "obstructed"
> and the item-6 line in 0151.

0154 measured γ = −1 with an instrument that could only carry a
*diagonal* metric, and refused to call it fatal because the program's
graviton is the off-diagonal spin-2 synergy. The restriction is now
removed.

## The extension, gated

Let the matter see a full symmetric metric per site, `W = exp(2A)`,
A symmetric 4×4 — **10 components, not 4**. Expanding ln det to second
order gives the generalisation of 0125's identity:

    Γ⁽²⁾[A] = tr(BA²) − tr(BABA),   B = D(DᵀD)⁺Dᵀ

which collapses to `½Σ‖B_lm‖²(λ_l−λ_m)²` when A is diagonal. For a
plane wave in the flat background this evaluates to
`Q(Â) = 2V·tr[βÂ²] − 2Σ_p |v̂(p)†Âv̂(p+k)|²`.

| gate | result |
|---|---|
| momentum formula vs **dense brute-force projector**, random symmetric A | **5.5e−16, 2.0e−16, 2.8e−16** |
| restrict A to diagonal — must reproduce 0154 | γ = −1.11 ✓ |

The dense check shares no algebra with the momentum formula.

## The answer

| computation | γ |
|---|---|
| diagonal only (0154) | −1.11 |
| **full symmetric, external-body source** | **−1.37 (L=12), −1.23 (L=16)** |
| **full symmetric, same-matter source** | **−1.07 (L=16)** |

Two source conventions were run because 0154 and this module's first
draft disagreed about which is right — the source either couples to
the weight it sees (`W₀₀`) or to the metric the way GR says
(`T^{μν}h_{μν}`, giving j = (−1,1,1,1)/2). **They agree**, so nothing
hinges on that choice. r = 1 is a short-distance outlier inflating the
spreads; the clean mid-range points sit at −1.0 to −1.2.

> **The off-diagonal sector does not rescue it. γ ≈ −1.**

## Why — and this is stronger than the measurement

B is a projector, so `tr(BA²) = tr(BABA) + tr(BA(1−B)A)` and

> **Γ⁽²⁾[A] = tr(BA(1−B)A) = ‖(1−B)AB‖²_F ≥ 0**

**identically, for every symmetric A, including the conformal mode.**
Verified numerically (min over random A: +2.63e+02) but it is an
algebraic identity, not a measurement.

Linearised Einstein-Hilbert **requires** the conformal mode to carry
the opposite sign to the transverse-traceless modes. That is the
conformal-factor problem of Euclidean quantum gravity, and it is not a
nuisance — it is the *signature* of a spin-2 kinetic term. **An action
that is positive semidefinite in every direction cannot be
Einstein-Hilbert, whatever source is applied to it.**

So γ = +1 was never available. And because a sum of PSD forms is PSD,
**no amount of matter content or field count changes this** — the
result does not depend on the (2,2), on Spin(4), or on κ.

## The verdict

**Item 6 fails.** The program's induced-gravity route predicts **zero
light bending** — the 1919 result that killed scalar gravity — against
Cassini's γ − 1 = (2.1 ± 2.3)e−5.

**What this does not touch:** the derived measure, the Born-rule
chain, OS reconstruction, the finite-dimensional Hilbert space, Λ
quantisation, κ = 16 as the exact curvature, or 0155's hierarchy. None
of those depend on the induced determinant.

**What it does touch:** the route from the matter determinant to
gravity — which is exactly the route that produced G = 1/(4πp) and
ℓ_P = 0.507a. Items 4 and 5's numbers remain correct as measurements
of the induced *scale* stiffness. What is now in question is calling
that stiffness Newton's constant.

## The escapes, named rather than left vague

Three, and all are narrow:

1. **The metric identification.** If the physical metric is not
   `W = √g g^{μν}`, the map changes — but that identification is the
   program's own (0125), and it is what makes the D = 4 conformally
   flat coupling work.
2. **Gravity not induced.** If there is a *bare* Einstein-Hilbert term
   the argument does not apply — but 0125 is explicit that "the trust
   field λ has no bare action, so its entire dynamics is what the
   matter's own record generates."
3. **Higher orders.** They do not change a linearised PPN parameter.

If none of those opens, this is where the program bleeds.
