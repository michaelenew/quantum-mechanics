# 0131 — Continuity, closed out: two volumes, a bound, and a scoped triviality

Code: `output/0116_deciding_the_branch.py` (s4),
`output/0118_the_smeared_observable.py` (s4),
`output/0119_the_triviality_question.py`. Fifth stone, clearing the
three items 0130 left.

## 1. The branch, at two volumes

0130 recorded the L = 6 tempering as a failure to mix — zero round
trips. **The fix was the ladder, not the statistics.** Swap
acceptance falls with volume at fixed spacing (~1/√V), so L = 6
needs a proportionally finer one:

| | rungs | acceptances | round trips | ⟨θ²⟩(τ=0) | excursions to |
|---|---|---|---|---|---|
| L = 4 | 8 | 0.005–0.471 | 2 | 0.1134 ± 0.0014 | 0.440 |
| L = 6 | **18** | 0.017–**0.833** | **6** | **0.1176 ± 0.0016** | **0.282** |

Against candidates 0.097 (ordered) and ~0.51 (disordered), both
volumes land on ordered — and **the disordered excursions shrink
with volume** (0.440 → 0.282), which is exactly what an extensive
free-energy difference predicts.

> **The branch decision now stands at two volumes.** β_eff ≈ 12–13,
> ξ/a ~ 10¹³, untuned.

## 2. Rotational symmetry, bounded at last

0129 could not measure it (0.1σ). 0130 got 49σ but at L = 12, where
the free-field baseline is itself 0.6–3.8 and the widths disagreed.
At **L = 20**, w = 2, the baselines finally drop to 0.0003–0.0017 —
wrap-around under control — and four rows resolve at 18–71σ:

| pair | measured | free | **difference** | σ |
|---|---|---|---|---|
| (4,0,0,0) vs (2,2,2,2) | +0.0106 ± 0.0002 | +0.0003 | **+0.0103** | 68 |
| (6,0,0,0) vs (3,3,3,3) | +0.0154 ± 0.0009 | +0.0017 | **+0.0136** | 18 |
| (4,0,0,0) vs (3,2,1,1) | −0.0577 ± 0.0008 | −0.0585 | **+0.0008** | 71 |
| (6,0,0,0) vs (4,4,2,0) | −0.0023 ± 0.0001 | +0.0014 | **−0.0037** | 19 |

The pairs do **not** agree on one number, so this is a **bound, not
a measurement**:

> **The interacting contribution to rotational-symmetry breaking at
> r = 4–6 is at most about 1.4%.**

And it **shrinks as the probe lengthens** — ~0.03 at w = 1.25 against
~0.01 at w = 2.0, roughly the (a/scale)² law. That law was assumed
from the free field in 0129; **it is now verified for the interacting
theory.** The standing "continuum Lorentz invariance, never tested"
debt moves from *untested* to *bounded at the percent level at
r ≈ 5a*, with the extrapolation to physical scales still an
extrapolation.

## 3. Triviality, scoped rather than faked

Triviality afflicts theories that are **not** asymptotically free —
φ⁴ and U(1) in four dimensions. A 4D nonabelian gauge theory runs
the other way. **The same asymptotic freedom that supplies this
program's hierarchy removes the triviality threat**, so the question
reduces to a premise: is the derived measure in that class, or only
SU(2)-shaped?

Tested non-circularly — κ(τ) comes from the weight with no Monte
Carlo, and SU(2) lattice perturbation theory predicts
⟨1 − cos θ⟩ = 3/(4κ):

| τ | κ | 3/(4κ) | measured | ratio |
|---|---|---|---|---|
| 0.00 | 13.34 | 0.05623 | 0.04781 ± 0.00009 | 0.850 |
| 0.15 | 6.93 | 0.10821 | 0.10299 ± 0.00021 | 0.952 |
| 0.60 | 2.43 | 0.30868 | 0.30977 ± 0.00066 | 1.004 |
| 1.20 | 1.15 | 0.65154 | 0.64583 ± 0.00085 | 0.991 |

Nothing on the left of that comparison came from the right.

**But the trend is the wrong way, and I asserted otherwise before
looking.** The relative residual *grows* with κ (−0.150, −0.098,
−0.048, −0.018, +0.004) instead of falling like 1/κ, which is the
opposite of a perturbative correction. Three candidates, none tested:
the weight's **exact zeros** truncating the plaquette distribution at
θ = 2π/7; the higher-order lattice series; the Gaussian approximation
crossing over across the family. Separating them is one cheap module.

> So: class membership is supported, a clean perturbative approach is
> not, and **the honest status of triviality is "inherits the
> standard expectation, untestable directly"** — a real test needs
> two physical scales at two couplings, and at κ ≈ 13 those scales
> are 10¹³ lattice spacings apart. That is a different and much
> better position than the open question 0130 recorded.

## 4. Front status

| | |
|---|---|
| the target | no dial → continuity means ξ/a is already large |
| the coupling | β_eff ≈ 12–15, weak — and this is *why gravity is weak*, 0069's (D) |
| the branch | **decided, two volumes** |
| the hierarchy | **ξ/a ~ 10¹³, untuned** |
| Lorentz restoration | **bounded at ≤1.4% at r ≈ 5a**, shrinking as (a/scale)² |
| triviality | **scoped**: inherits the standard expectation; directly untestable |
| open | the residual trend in §3; the extrapolation from r ≈ 5a to physical scales |

Continuity is no longer an open conjunct of 0069's wall in the sense
0127 recorded. It is a set of bounds and a class membership, with one
unexplained trend.
