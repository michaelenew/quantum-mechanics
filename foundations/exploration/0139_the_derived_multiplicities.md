# 0139 — The derived multiplicities: item 1 is an obstruction, not a computation

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.
>
> **Prior art.** Rao (1945), Blackwell (1947) for the conditional-mean estimator; Parisi, Petronzio & Rapuano (1983) for multihit on the lattice.

Code: `output/0127_the_derived_multiplicities.py`. 0137's criticality
item 1 was "derive the SU(2) amplitude's multiplicities and re-run
the coupling." **It cannot be closed that way**, and why not is the
result.

## 1. The derivation yields a family, not a vector

0074 §3's construction, recomputed (vectorised, 4×10⁶ frame pairs):
two frame vectors from the χ₄ radial law, relative angle from the
semicircle law, bivector magnitude s = r_a r_b sin θ/√2, binned at
scale s₀.

| s₀ | κ | ξ/a |
|---|---|---|
| 0.50 | 13.78 | 2.1e+15 |
| 0.75 | 10.62 | 4.4e+11 |
| 1.00 | 8.09 | 5.1e+08 |
| 1.50 | 4.83 | 1.1e+05 |
| 2.00 | 3.19 | 1.6e+03 |

> Across **0074's own free parameter**, κ runs 3.19 → 13.78 and ξ/a
> runs 1.6e3 → 2.1e15 — a spread of **10¹²**.

And the *shape* depends on s₀ too: coarse binning peaks at j = 0,
fine binning moves the peak up. 0074 reported "peaked, not monotone"
at its own scales; that is one member of a family.

**So flat counting was not a lazy choice over a known answer. It was
a choice over an undetermined one.**

## 2. A second unpriced step, found while doing this

0074 §3 derives multiplicities for the **Spin(4)** frame amplitude,
A(U⁺,U⁻) = Σ_j n_j χ_j(U⁺)χ_j(U⁻). The lattice simulates a **single
SU(2)**, A(U) = Σ_j n_j χ_j(U). These are different objects — on the
diagonal the first becomes Σ_j n_j χ_j(U)², whose character content
is each sector fused with itself.

| | κ | ξ/a |
|---|---|---|
| flat, single SU(2) *(simulated)* | 13.337 | 6.4e+14 |
| flat, Spin(4) diagonal *(derived object)* | 31.971 | 2.7e+36 |

**Ratio in ξ/a: 4×10²¹.** The reduction between them is recorded
nowhere in the program, and it is worth more than the first gap.

## 3. Verdict

> **The coupling is not derived.** κ = 13.34 is the value of one
> particular choice — flat multiplicities on a single SU(2) — and the
> program has treated it as the theory's own number since 0091.

What this does **not** touch: the structural results. There is still
no dial to tune; asymptotic freedom still supplies the separation
without tuning; Lorentz restoration was measured on whatever weight
was in fact used, and that measurement stands.

What it removes: **the number** — ξ/a ~ 10¹³ — and with it the "why
gravity is weak" chain, whose entire content was that number.

**Item 1 is an obstruction.** It needs a derivation that fixes s₀
*and* the group reduction. That is a real open problem, now stated
precisely, and it is not fixable by more computation.

It does not block items 2 and 3: a double slit demonstrates
*structure* (interference out of the derived measure via
Osterwalder–Schrader), and structure is insensitive to the
multiplicities — any nonnegative counting gives a positive transfer
operator and hence a Hilbert space.
