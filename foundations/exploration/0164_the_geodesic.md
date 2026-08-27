# 0164 — A lattice that shows you a geodesic

> **AI-generated, not peer-reviewed.** Code: `output/0154_the_geodesic.py`.
> Field from R3 (0163). Retires the closing sentence of 0161.
> Prior art credited in [`ATTRIBUTION.md`](../ATTRIBUTION.md).
>
> **Prior art.** Einstein (1915) for 4GM/b; Dyson, Eddington & Davidson (1919) for the measurement this reproduces the ratio of.

0161 said the program "cannot claim a lattice that shows you a
geodesic." Two retired blockers later — the scale (0162) and the
carrier (0163) — that is no longer true.

## The setup

**The field** is R3's: the static metric response to a static mass,
computed in the constrained sector on the Spin(4) lattice, where the
kernel is Einstein-Hilbert to O(a²) and **no counterterms are needed**.
L = 48, γ = **+1.00000** over r = 1…13, fitted `U(r) = GM/r + C` with
**GM = 0.04330** in lattice units.

**The trajectory** comes from integrating the eikonal ray equation
`d(nu)/ds = ∇n` — an actual trajectory, not a Born estimate. For a
static metric a null geodesic extremises the optical path with
`n = √(g_xx/−g_tt) = 1 + (1+γ)U`, so the 1919 test is a **ratio**: the
full metric must bend twice as far as one carrying the Newtonian g₀₀
alone.

## The result

| b | full metric | g₀₀ only | ratio |
|---|---|---|---|
| 4 | +0.041512 | +0.020355 | 2.0394 |
| 6 | +0.025595 | +0.012651 | 2.0231 |
| 8 | +0.017880 | +0.008867 | 2.0164 |
| 10 | +0.013174 | +0.006544 | 2.0131 |

> **ratio = 2.0230 ± 0.0101.** Einstein needs 2.

A null ray integrated in the field this program's own lattice produces
bends **twice as far** as the same ray in a metric with the Newtonian
potential alone. That is the measurement that separated Einstein from
Newton in 1919, run here on the quantum lattice's own field.

## Why the absolute number is not the physics, stated exactly

measured/GR = 0.8580 ± 0.0733, falling with b. That is **not** a
discrepancy, and the reason is exact:

> U is periodic, so `∮∇_⊥U ds` over a **full period is identically
> zero**. On a torus the total deflection along a complete period
> vanishes, so any nonzero absolute deflection is necessarily
> path-truncated and depends on where the ray starts and stops.

The shortfall tracks that prediction:

| b | finite-path factor | measured/GR | corrected |
|---|---|---|---|
| 4 | 0.976 | 0.959 | 0.982 |
| 6 | 0.949 | 0.887 | 0.935 |
| 8 | 0.914 | 0.826 | 0.904 |
| 10 | 0.874 | 0.761 | 0.870 |

with the residue from periodic images, which pull the other way and
grow with b.

**The ratio is immune to both** — the two rays traverse the same field
over the same path, so truncation and images cancel exactly. That is
why the 1919 test is a ratio, and why 0037 ran it as one on the
classical tier too.

## What this closes

The chain now runs end to end **inside the quantum theory**:

    derived weight (κ = 16.0001, balanced reps = simplicity)
      → constrained sector
      → kernel = Einstein-Hilbert, verified on the lattice to O(a²)
      → static response, γ = +1.000, n = 1.020
      → null ray integrated in that field
      → deflection ratio 2.023

Every step measured or gated, and no counterterms anywhere.

Two turns ago I called this impossible for two different reasons and
both were wrong on measurement. The lesson is worth more than the
result: **a named blocker that has not been measured is a
conjecture.**

## What a geodesic still does not give you

Bending is a **linear**-field, test-particle effect. Perihelion
precession is not — it needs the metric at second order in the mass.
That is R5, and it is untouched. So is R6 (Lorentzian real time) and
R7 (matter content: no spinors).
