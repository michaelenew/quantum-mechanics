# 0092 — The heat-kernel theorem: universality's true mechanism

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Thirteenth stone: the queue's "CLT fixed-point theorem" — prove that
0077's fixed structure (μ_R = τ·C₂(R), Casimir ratios exact) is the
heat kernel because of a central-limit effect. Attempted honestly,
**the filed conjecture is false** — and what is true instead is
sharper and explains 0077 to the digit. Code:
`output/0082_the_heat_kernel_theorem.py`.

---

## 1. What is true: second-moment universality, for light tails

From χ_j(θ)/d_j = 1 − (2/3)C₂(j)θ² + O(θ⁴), any **light-tailed**
class weight of width s has transfer spectrum

```
−ln r_j = (2/3)⟨θ²⟩ · C₂(j) + O(s⁴)
```

— the heat-kernel form, with τ = (2/3)⟨θ²⟩ and no other memory of
the weight. Verified on two unrelated families (Gaussian, hard
window): flatness deviation falls as s², τ matched to 0.1–0.3% at
s = 0.1. The heat kernel is the universal narrow-width limit — *for
weights in the second-moment basin.*

## 2. What is false: there is no convolution CLT here

Pure convolution (2D gluing) powers coefficients, r_j → r_j^A, so
the log-ratios (−ln r_j)/(−ln r_k) are **exactly frozen** at every
A. Convolution can damp everything; it can never *reshape* the
spectrum toward Casimir ratios. The "CLT fixed-point" intuition dies
on this one-line lemma.

And the ledger needs reshaping: the Born counting weight (Σχ_j)² has
Fejér-squared tails with kurtosis **13 at J = 5, 25 at J = 10**
(light families: 1.2–1.7), and its flatness deviation is 0.63–0.67,
*not improving* as the width shrinks. **The bare ledger never
resembles the heat kernel, at any width.** Had 0077 been a
convolution effect, its Casimir ratios would have been impossible.

## 3. The true mechanism: the bond move is a Laplace localization

The MK bond move — the pointwise power W → W^ζ (0076's recursion) —
does what convolution cannot:

| MK iteration | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| flatness deviation | 0.633 | **0.0016** | 0.0001 | 0.0000 |

**One blocking step kills the heavy tails and lands the ledger in
the heat-kernel family**; every subsequent step only moves τ. The
pointwise nonlinearity is a Laplace localization — it concentrates
the weight where ln W is quadratic, which is exactly the
second-moment basin of §1. So the corrected theorem:

> The heat-kernel family is the universal limit of narrow
> light-tailed class weights (second-moment collapse, §1); the
> ledger is *not* light-tailed, and it is the **RG's pointwise
> nonlinearity** — not gluing, not any CLT — that carries it into
> the basin, in a single step. 0077's measured Casimir ratios are an
> RG-localization result, with the basin's entry mechanism now
> identified and its speed measured (one iteration).

## 4. Bookkeeping

- 0077's language ("the fixed structure is the heat kernel")
  survives unchanged; its *attribution* is corrected from
  CLT-flavored to RG-localization, and the queue item "CLT
  fixed-point theorem" is closed as **false-as-filed,
  replaced-by-better**.
- The freeze lemma retroactively sharpens 0086/0087: the free
  tiers' exactness (polar theorem, reading theorem) and their
  *rigidity* (no flow of structure) are the same fact — convolution
  preserves everything, which is why free tiers can neither distort
  sources nor renormalize themselves. Structure moves only where
  nonlinearity lives (the bond move under RG; the vertex under
  interaction, 0088). One mechanism, two appearances.

## Honest limits

- SU(2) class weights on a 1D transfer structure; "light-tailed"
  operationalized as bounded kurtosis, not sharply characterized
  (the basin boundary between kurtosis 1.7 and 13 was not mapped).
- The bond move here is the pointwise power alone; 0076's full grid
  recursion adds decimated reconstruction, which (per the freeze
  lemma) cannot change ratio structure — so the attribution is
  complete, but the τ-trajectory under the full recursion was not
  re-derived here (0076/0077 measured it).
- τ = (2/3)⟨θ²⟩ uses this repo's χ normalization; the 2/3 is
  convention.

## Open

1. Map the basin boundary: the critical tail weight where
   localization-in-one-step fails (expect a kurtosis threshold; the
   window family at large s is the natural probe).
2. The τ beta function proper: with the structure frozen to heat
   kernel after one blocking, the flow is one-dimensional — extract
   dτ/d(block) from 0076's machinery as a scalar map (this is the
   full theory's own version of F2, and it is now a *cheap*
   computation rather than a heavy one).
3. Standing heavy stone: the assembled complex (A3).
