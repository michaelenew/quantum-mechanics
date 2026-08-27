# 0149 — Item 2 closed: the null is the box, not the channel

> **AI-generated, not peer-reviewed.** Code: `output/0138_item2_closed.py`,
> `output/0139_the_control_channel.py`,
> `output/0140_fixed_time_operators.py`. Scale analysis: 0150.
> Prior art credited in [`ATTRIBUTION.md`](../ATTRIBUTION.md).
>
> **Prior art.** Albanese et al. (1987) for APE smearing; Wilson (1974).

## What was run

**0138 — the two-level production run.** Boundaries at t = 0, 4; blocks
A = {1,2,3}, B = {5,6,7}. The block decomposition is *asserted*, not
assumed: every link is owned by A, B or the boundary, A ∩ B = ∅, and
frozen links move by exactly `0.00e+00`. 3000 boundary configurations,
24 sub-averages each, 1.75 s per configuration.

| d | C(d) | σ |
|---|---|---|
| 2 | +1.0973e−10 ± 1.2e−09 | 0.1 |
| 3 | −3.7432e−10 ± 7.2e−10 | 0.5 |
| 4 | −4.7740e−10 ± 9.1e−10 | 0.5 |

Errors down ~25× from 0135. **Still consistent with zero everywhere.**

**0139 — the control.** The same pipeline on the 0++ channel, 15000
configurations, one-level:

| d | 0++ | 2++ |
|---|---|---|
| 0 | +1.4829e−06 ± 7.0e−09 (211σ) | +1.5907e−06 ± 3.3e−09 (484σ) |
| 1 | +1.3309e−07 ± 5.2e−09 (**25.7σ**) | −9.8073e−10 ± 2.4e−09 (0.4σ) |
| 2 | +4.2047e−09 ± 5.5e−09 (0.8σ) | −2.7360e−10 ± 2.1e−09 (0.1σ) |

**The pipeline is not blind.** Whatever the tensor's silence is, it is
not the measurement failing.

**0140 — the operator was not a fixed-time operator.** `all_plaq`
returns plaquettes ordered (0,1),(0,2),(0,3),(1,2),(1,3),(2,3) — the
first three are *temporal*. Averaging all six straddles two time
slices, so it was never an operator of the transfer matrix, and its
correlator is contaminated by contact terms at d = 0 and 1. Indices
3,4,5 are the spatial ones. Rebuilt fixed-time, plus real APE link
smearing (in the quaternion representation the group projection is
exactly normalisation — gated: deviation from |q| = 1 is ≤ 3e−16 and
the plaquette rises monotonically 0.9572 → 0.9997, so smearing cools
as it must).

Result across 0, 2, 4, 8 smearings: the 0++ stays resolved
(m_eff ≈ 3.2–3.7); the 2++ never exceeds **1.3σ** at d ≥ 1. Bound:
any state in this channel has **m·a > 5.10 or overlap < 0.61%** of the
operator's norm.

And smearing *reduces* the 2++ signal (1.7e−09 at 4 smearings,
2.1e−10 at 8). Smearing removes ultraviolet fluctuation — so
ultraviolet fluctuation is all this operator has here.

## Why the null, and why it was never an estimator problem

0150 does the arithmetic; the short version: the mean spatial
plaquette is **0.957**, an almost *frozen* lattice, so β ≈ 16–17.5,
so by asymptotic freedom **ξ/a ≈ 10¹⁸**. The 8⁴ box is ~10⁻¹⁷ of one
correlation length.

> Nothing bound can appear on that box — **in either channel.** The
> 0++'s m_eff ≈ 3.2 is not a glueball mass either; it is the
> ultraviolet slope of a local operator on a very fine lattice. Both
> columns are UV.

**Two verdict lines in 0139 and 0140 were written before this was
understood and said "the tensor channel is empty" and "everything in
this theory is sub-lattice-spacing".** Both are wrong — the
correlation length is enormous, not tiny — and both modules have been
corrected in place rather than left to contradict 0150.

## The ledger on item 2

| diagnosis | built | delivered | verdict |
|---|---|---|---|
| throughput (0145) | C kernel | 30× sweeps | wrong — answer unmoved |
| link conditional means (0147) | multihit | 0.98× | wrong unit |
| boundary independence (0148) | `sweeps4f` | **24×**, unbiased | right — and insufficient |
| the box (0150) | — | — | **the actual limit** |

The estimator work was correct and is banked: `sweeps4f`, the
multihit machinery, the fixed-time operator, and APE smearing are all
gated and reusable. They bought a factor **24** against a deficit of
**10¹⁸**.

> No estimator closes that gap. Item 2 as posed — "measure the
> graviton propagator on the lattice" — is not hard, it is
> **ill-posed at the derived coupling**, and the right response is
> not more compute. It is 0150.

## What closes and what opens

**Closes:** item 2. The spin-2 propagator cannot be measured directly
on a Planck-spacing lattice, and now we know the number that says so
rather than guessing at estimators.

**Opens:** the reason it can't is itself a derived quantity, and it is
large — which is what 0150 is about, and it is the first thing in this
program with the shape of a prediction.
