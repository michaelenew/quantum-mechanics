# 0130 — The smeared observable: the kernel worked, and the obstruction moved

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Code: `output/0118_the_smeared_observable.py`. Fourth stone of the
continuity front, and the first one built by taking a prescription
from the filter side (lucid 0037) rather than porting a result back.

## 1. Weak coupling is load-bearing, and it belongs to (D)

Worth recording before the measurement, because it reframes what
0129 found. The chain is: **weak coupling → large ξ/a → the only
scales in the theory are ~10¹³ lattice spacings apart → gravity's
coupling at ordinary scales is (a/ξ)² ~ 10⁻²⁶.**

> That *is* "why gravity is weak" — which is 0069's requirement
> **(D)**, the one that has never moved and that 0127 recorded as
> having been quietly reclassified from law to data.

It is not a derivation of N yet. But it is the first time the
hierarchy has been a *computed consequence* of the derived measure
rather than an input, and a theory predicting **strong** gravity at
small scales would already be dead.

## 2. The kernel worked

0129 could not measure the anisotropy of the local operator at all
(+5.6 ± 4.8, −19.7 ± 459). lucid 0037's prescription: smear with a
radially symmetric kernel exp(−w²k²) in the **continuum** momentum,
width w ~ r/3.

| w | pair | anisotropy | \|A\|/err |
|---|---|---|---|
| 0.00 | (4,0,0,0) vs (2,2,2,2) | +1.0448 ± 8.5447 | 0.1 |
| 0.75 | " | +1.3568 ± 2.4532 | 0.6 |
| 1.25 | " | **−0.0150 ± 0.0006** | **24.6** |
| 2.00 | " | **+0.0541 ± 0.0011** | **49.1** |

> **0.1σ → 49σ.** A several-hundred-fold gain, exactly as 0037's
> 62× measurement predicted.

## 3. And a methodological error the fix exposed

The first pass computed the free-field baseline at L = 48 against an
L = 12 measurement. **That comparison is invalid** — with kernels of
width 2 on a 12⁴ lattice, wrap-around is severe. Recomputed at the
measurement's own volume, the free baseline is not small at all:

| w | pair | free anisotropy (L = 12) |
|---|---|---|
| 0.75 | (6,0,0,0) vs (3,3,3,3) | **+3.8486** |
| 1.25 | (6,0,0,0) vs (4,4,2,0) | +0.6327 |
| 2.00 | (4,0,0,0) vs (2,2,2,2) | +0.0418 |

The |r| = 6 rows are wrap-dominated and say nothing about the
theory. The baseline must always be computed at the measurement's
own L.

## 4. What replaced the problem

Of the sixteen rows, four are both resolved and out of the wrap
(|r| = 4, w = 1.25 and 2.0). They give measured − kinematic of
**−0.023 and +0.012** for one pair, **−0.060 and −0.018** for the
other — i.e. **the two usable widths disagree**, which is what a
kernel of width 2 plus a separation of 4 does to a 12⁴ lattice.

> **The statistical obstruction is solved, and a finite-volume one
> replaced it.** That is progress, because volume is a known cost:
> this measurement wants **L ≥ 20 and the same number of sweeps** —
> not more statistics, more room.

## 5. The L = 6 tempering, which did not mix

The volume check on 0129's branch decision: at L = 6 the τ = 0
replica sits at ⟨θ²⟩ = 0.09695 ± 0.00004 — the ordered value. But
the acceptances collapse above the third rung (0.098, 0.111, 0.020,
0.003, 0.005, 0.005, 0.005) and there are **zero round trips**.

> So L = 6 does **not** independently confirm the branch decision;
> it merely fails to mix. Swap acceptance falls with volume at fixed
> Δτ (as ~1/√V), so L = 6 needs a proportionally finer ladder. The
> branch result stands on L = 4 alone until that is run.

## 6. Front status

| | |
|---|---|
| the coupling | β_eff ≈ 12–15, weak — and now understood as *why gravity is weak* |
| the branch | ordered, **L = 4 only**; L = 6 ladder too coarse to confirm |
| the hierarchy | ξ/a ~ 10¹³, untuned |
| Lorentz restoration | statistics solved (49σ); **needs L ≥ 20** |
| triviality | untouched |
