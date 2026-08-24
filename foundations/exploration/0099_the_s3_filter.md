# 0099 — The S³ filter: the fusion tax, and the beta function derived

The gap-1 prototype brick (0098's catalogue), built as ordered — and
it produced the run's sharpest quantitative result. The plan was to
show a filter on a curved state space has a running width. What fell
out is a **derivation of the beta function from a single measured
constant**, with the MK scheme dependence explained as a law. Code:
`output/0089_the_s3_filter.py`.

---

## 1. The fusion tax

Bayes fusion of two identity-centered heat kernels on SU(2) ≅ S³,
written in precision units (p = 1/τ):

```
p_post = p_a + p_b − δ,        δ = 0.1686  (spread 0.9%)
```

The flat law "precisions add" fails by a **width-independent
constant** — verified across τ = 0.02–0.4, equal and unequal widths
alike, drifting toward **1/6 = 0.1667** as τ → 0. Every fusion on the
curved space costs one fixed quantum of precision. On U(1) the tax is
≤ 1.6e−4 (winding-level); on ℝ it is zero by algebra. **The tax is
curvature's alone** — and its small-τ value is numerically consistent
with the DeWitt heat-coefficient a₁ = R/6 (S³'s scalar curvature
normalization; flagged as a candidate identification, not proven).

## 2. The beta law, derived

An MK bond move W^ζ is ζ − 1 fusions. Propagating the constant tax
through bond move + decimation:

```
β(τ) = (1 − 1/b²) · δ · τ²
```

| b | (1 − 1/b²)·δ | 0093 measured | agreement |
|---|---|---|---|
| 2 | 0.1264 | 0.127 | **0.4%** |
| 3 | 0.1499 | 0.151 | **0.8%** |

What 0093 honestly reported as "MK-typical ±30% scheme dependence" is
not sloppiness — it is the exact factor (1 − 1/b²), and the
scheme-independent core is δ. The physical sentence: **the beta
function measures the information the geometry's self-measurement
loses to curvature, per fusion.** Asymptotic freedom's coefficient is
the fusion tax. If δ = 1/6 exactly (the a₁ candidate), the beta
function of this scheme is β = (1 − 1/b²)τ²/6 — a closed form from
one geometric constant.

## 3. The running filter, as promised

The full cycle (predict + τ_q, update against a width-τ_r likelihood)
iterated to its stationary width: the S³ filter's fixed point exceeds
the flat Kalman fixed point by an excess that **grows with the noise
scale** (+0.9% → +1.2% across the sweep). A walking filter on S³ has
a running stationary width; on ℝ it cannot. This is the data-side
face of the coupling's IR growth — the experiment 0098 predicted the
filter side could run, run.

## 4. Family breakdown — the curved filter's strong coupling

The conjugate (heat-kernel) description's leak under fusion grows
monotonically: 3e−4 at τ = 0.4, 2.4e−2 at 1.5, 9.3e−2 at 2.5. Past
τ ~ 1 the one-parameter family stops describing its own posterior —
the filter-side strong-coupling scale, where 0092's localization
logic runs in reverse. (Genuine lock-loss also involves the
association/centering problem, out of scope and flagged.)

## What this changes upstream

- **0093 upgraded**: the τ flow's coefficient is no longer a
  scheme-stained number but (1 − 1/b²)·δ with δ measured to 1% and a
  candidate exact value (1/6). The b → ∞ limit δ·τ² is the scheme's
  clean beta function.
- **0094's hierarchy menu tightens**: the exponent ln(L*/a) =
  ln b/(c·τ₁) with c = (1 − 1/b²)δ — the c-uncertainty that dominated
  the error budget collapses to the δ-identification question.
- **The homomorphism (0098) is now quantitative in its defect**: the
  gap isn't just located at curvature; its magnitude is one constant,
  and the filter side can measure it (any directional-statistics
  fusion experiment on S³ measures δ).

## Honest limits

- The tax's constancy is measured over τ ∈ [0.02, 0.4] and drifts
  ~3% across that range (higher-order terms); the 1/6 identification
  is numerical (0.1% at τ = 0.02), not derived from the heat-kernel
  expansion here.
- The cycle in s3 uses identity-centered (symmetric) updates — the
  width recursion of an unbiased filter, not a full tracking run
  with innovations.
- The beta-law derivation treats the tax as exactly constant through
  the bond move's sequential fusions; the 1–2% residuals vs 0093
  include that approximation.
- U(1)'s tax bound is numerical at the stated grid.

## Open

1. **Prove δ = 1/6**: the small-τ product of SU(2) heat kernels via
   the (j+½)² spectrum — the C₂ = (j+½)² − ¼ shift looks like it
   yields the constant in three lines. (If so, β = (1 − 1/b²)τ²/6
   is a theorem of this scheme.)
2. The filter-side measurement of δ (wall-correspondence: a fusion
   experiment in directional statistics — their harness, our
   constant).
3. Gap 2 next per the owner's ordering: the innovation question —
   what external stream, if any, does the physics admit.
4. The association problem on S³ (true lock-loss) — the compact
   filter's deepest untouched layer.
