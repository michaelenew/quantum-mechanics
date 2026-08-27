# 0141 — The one dimensionless prediction, computed and priced

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.
>
> **Prior art.** Wilson (1974); Gross & Wilczek (1973) and Politzer (1973) for asymptotic freedom; Caswell (1974) and Jones (1974) for the two-loop coefficient; Hasenfratz & Hasenfratz (1980) for the lattice Lambda parameter.

Code: `output/0129_the_one_dimensionless_prediction.py`, after lucid
0044.

A one-parameter theory cannot predict a **dimensionful** quantity —
G, ξ/a and the Λ quantum are the same undetermined scale seen through
three windows. It *can* predict a **dimensionless** one, because the
scale cancels. The program has exactly one candidate.

## 1. The prediction

lucid 0042's port: **Λ·R² ∈ (2π/q)·ℤ**, q the charge the record winds
under, R the spatial curvature radius. In the continuum q is the
gauge group's **centre** — Z₂ for SU(2) — so q = 2 and the quantum is
**π**.

## 2. In observables — and H₀ drops out

Λ = 3H₀²Ω_Λ/c² and R = c/(H₀√|Ω_k|), so

> **Λ·R² = 3Ω_Λ/|Ω_k|**

exactly. Verified numerically at H₀ = 67.4 and 73.0 km/s/Mpc — both
give Λ·R² = 2934.4. **The Hubble tension is irrelevant to this
prediction**; H₀ is not in it.

## 3. Confronted

Measured 3Ω_Λ/|Ω_k| = 2934.4, so n = 934.1.

| n | implied \|Ω_k\| | status |
|---|---|---|
| 1 | 0.653840 | **EXCLUDED** (344σ) |
| 2 | 0.326920 | **EXCLUDED** (172σ) |
| 5 | 0.130768 | **EXCLUDED** (69σ) |
| 50 | 0.013077 | **EXCLUDED** (6.5σ) |
| 200 | 0.003269 | allowed (1.4σ) |
| 934 | 0.000700 | consistent (0.0σ) |

**Low-winding universes are dead** — n ≤ 5 at hundreds of sigma.
That is a real, if weak, kill.

**And one qualitative claim is sharp: Ω_k cannot be exactly zero.** A
flat universe has R infinite, so Λ·R² is infinite and there is no
integer. The mechanism *requires* spatial curvature — lucid 0042's
"the loop must close", in observational clothes.

## 4. Priced

At n ≈ 934 adjacent predictions differ by **Δ|Ω_k| = 7.5×10⁻⁷**
against a current error of **1.9×10⁻³**.

> **Ratio: 2538×.** Ω_k must be known ~2500 times better before this
> is a test rather than a compatibility statement — beyond Planck,
> beyond what is planned, and limited by cosmic variance rather than
> instruments.

## 5. The honest summary

The program's entire predictive content, as of this stone:

- **one** dimensionless prediction, Λ·R² ∈ πℤ;
- it **kills** low-winding universes (n ≤ 5) at hundreds of sigma;
- it **requires** Ω_k ≠ 0, falsifiable in principle;
- its fine structure needs Ω_k to 2500× current precision.

That is not enough to live or die on. It is, however, a number, a
kill, and a requirement — which is more than the program had before
this turn, and it is stated where anyone can check it.
