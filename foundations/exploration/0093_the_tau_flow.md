# 0093 — The τ flow: the ledger's coupling runs like one loop

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Fourteenth stone, and one of the wall's three original outstanding
pieces lands: **the running of τ** — filed heavy, delivered cheap,
because 0092 collapsed the problem. After one MK blocking the weight
sits in the heat-kernel family, so the entire 4D flow is a scalar map
τ → τ′. Extracting it took an afternoon's numerics where the plan had
budgeted a campaign (and had marked the row *filter-first* for that
reason). Code: `output/0083_the_tau_flow.py`.

---

## 1. The flow is one-dimensional — verified, then used

One 4D MK step (bond move W → W^{b²} pointwise, decimation
r → r^{b²}) applied to a heat-kernel weight returns a heat-kernel
weight with flatness leak ≤ 1.2e−4 for τ ≤ 0.4 (1e−6 at τ = 0.1).
0092's freeze made this expected; here it is measured and then relied
on: the recursion closes on the family, and the only thing that
flows is τ.

## 2. The beta function has the one-loop shape

```
β(τ) = τ_out − τ_in = c·τ²(1 + O(τ)),    c(b=2) = 0.127 ± 3%
```

stable across τ ∈ [0.05, 0.2], **positive** — τ flows *up* toward
the infrared:

- **τ = 0 is the UV fixed point: asymptotic freedom** in the
  ledger's one continuum coupling. The geometry sector's coupling
  vanishes logarithmically at short distance.
- At strong coupling the flow goes super-quadratic (β = +0.09 at
  τ = 0.8, +0.37 at 1.5): the confining runaway.

Scheme test (b = 3): same sign, same quadratic order,
c = 0.151 per blocking — the coefficient is scheme-dependent by
~30% (per e-fold: 0.183 vs 0.137), which is MK's known accuracy
class. The *shape* is the claim; the number is a scheme artifact.
(Context, memory-flagged: continuum one-loop SU(2) has b₀ = 22/3
≈ 0.046/e-fold in the analogous normalization; MK overshooting 3–4×
is its usual behavior on spin systems.)

## 3. Dimensional transmutation — a scale from a scale-free start

Integrating dτ/dn = cτ² predicts a pole at n* = 1/(cτ₀); direct
iteration of the actual map from τ₀ = 0.05 reaches strong coupling
at **n = 152 blockings against the predicted 157** (3%). So the
ledger generates an invariant scale

```
ln(L*/a) = ln b / (c·τ₀)
```

exponentially separated from the lattice scale for small τ₀. **This
is the program's first emergent dimensionful quantity** — and it is
the standard hierarchy-generation mechanism arriving unforced: an
O(1) bare coupling produces a scale ratio e^{1/(cτ₀)} that can be
astronomically large. If anything ever pins τ₀ (the bar's
knob-derivation demand, 0069 (D)), this formula converts it into a
predicted hierarchy — the sharpest falsifiable-shaped statement the
RG arc has produced.

## 4. Reconciliation and bookkeeping

- **0076's "4D near-stationary" is resolved**: what their grid
  method saw was the smallness of cτ² at their operating τ
  (β(0.1) ≈ 1.3e−3, invisible at their resolution) — slow one-loop
  flow, not exact marginality. No contradiction; a better
  instrument.
- **0077's gapless graviton channel is untouched**: μ(1,1) ∝ ε was
  a statement about the fixed *structure* (ratios), which the flow
  preserves exactly; the running moves the overall τ scale under
  the tower.
- **F2's escalation, updated**: the adoption plan marked the running
  of τ filter-first ("the instrument is exact where MK is not").
  The full theory got there first after all — via 0092's theorem —
  but the filter row keeps its value with a sharpened target: the
  prequential regret-growth coefficient should be the doppelgänger
  of c, and the two can now be compared as numbers, not shapes.

## Honest limits

- MK is uncontrolled in 4D; the scheme-dependence measured here
  (~30% in c) is the honest error bar's floor, not its ceiling.
- The flow is for the SU(2) ledger sector's τ; the map from τ to
  the physical normalization of the graviton tower (and to any
  gravitational observable) is not fixed by this stone.
- Euclidean; heat-kernel family truncated at jmax(τ) with measured
  leak; b = 2, 3 only.
- b₀ = 22/3 quoted from memory, flagged.

## Open

1. Pin τ₀ — the knob-derivation. Candidates the program already
   owns: the vertex normalization (0078's ε′ and amplitude scales),
   or the level N via the constraint stack (smallest admissible
   N = 5). Either would turn §3 into a numerical hierarchy
   prediction.
2. The two-coupling flow: τ plus the vertex coupling strength
   (0088's susceptibility) — does the vertex charge run, and does it
   stay subordinate to τ?
3. F2's cross-check: the filter-side regret coefficient vs c.
4. Standing heavy stone: the assembled complex (A3) — now the only
   member left of the wall's original outstanding three.
