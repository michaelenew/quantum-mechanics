# 0144 — The Spin(4) lattice: the rebuild

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Code: `output/0132_the_spin4_lattice.py`, to lucid 0046's spec.
**Burndown item 1 is done.**

## 1. Why it had to be rebuilt, not patched

lucid 0046 measured that the graviton sector — traceless-sym(B⁺⊗B⁻) —
is **pure synergy**: knowing either stream alone leaves its direction
completely undetermined (residual spread 1.0000), knowing both fixes
it exactly (0.0000).

> A single-SU(2) lattice has no spin-2 sector. The rebuild is the
> difference between having a graviton and not — **no amount of
> post-processing the old runs recovers it.**

## 2. The build

| | |
|---|---|
| link | (U⁺, U⁻), a pair of unit quaternions |
| plaquette | two class angles |
| weight | W = \|Σ_{n=1..6} χ_n(θ⁺)χ_n(θ⁻)\|² |
| update | checkerboard Metropolis over both factors, staples built per factor, step auto-tuned |

## 3. The first check, named in advance and passed

lucid 0046 §4 specified the test before the run: measure κ from the
simulated plaquette distribution against 0094's ⟨θ²⟩ = 3R/κ.

| | κ |
|---|---|
| **measured κ⁺** | **16.99** |
| **measured κ⁻** | **17.03** |
| Spin(4) target | 16.00 |
| old single-SU(2) | 13.33 |

**6.2% from the Spin(4) value; 27.4% from the old one.** The two
factors agree with each other (16.99 vs 17.03), as the locking
requires. The residual 6% is the standing gap between 0094's Gaussian
bank and measurement, the same one 0120 characterised.

**A false pass caught on the way:** the first run had acceptance
**0.000** — the proposals were sized for a κ≈13 action and the
configuration never left the ordered start, giving a meaningless
κ = 110. The original assertion (`new closer than old`) *passed* on
that broken run, 590% vs 728%. The module now auto-tunes the step and
asserts acceptance in 0.15–0.75 and κ within 15% of target.

## 4. The sector that did not exist before

Projecting the simulated plaquette bivector pair B⁺ ⊗ B⁻:

| sector | dim | share | spin |
|---|---|---|---|
| trace | 1 | 0.280 | 0 |
| antisymmetric | 3 | 0.266 | 1 |
| **traceless symmetric** | **5** | **0.453** | **2 — the graviton** |

**The spin-2 sector is populated on simulated configurations**, at
essentially the free-field share lucid 0046 predicted (0.455). This
is a quantity the old lattice could not have produced.

## 5. Where the burndown stands

| | |
|---|---|
| ✅ 1 | **Rebuild on Spin(4)** — done, checked |
| ▶ 2 | **Identify the graviton mode** — correlate the spin-2 projection at separation. That correlator *is* the graviton propagator |
| 3 | implement the source (T = Fisher) as lattice code |
| 4 | measure the response, read the 1/r |
| 5 | the factor 20 — run in parallel |
| 6 | classical tests from Q4 |

The next object is one measurement away: the spin-2 correlator at
separation, on configurations that now exist.
