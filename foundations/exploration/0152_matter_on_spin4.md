# 0152 — Item 3: the source (T = Fisher) as lattice code

> **AI-generated, not peer-reviewed.** Code: `output/0142_matter_on_spin4.py`.
> Scope set by lucid `0049`.
> Prior art credited in [`ATTRIBUTION.md`](../ATTRIBUTION.md).
>
> **Prior art.** Sakharov (1967) for gravity induced by a matter determinant; Plebanski (1977) for the simplicity constraint.

## The scope correction that started it

lucid 0049 caught something before any code was written. The
masslessness of the trust channel in 0113/0125 follows from a
**uniform λ shifting ln det by exactly a constant** — a property of
**matter's** determinant. A uniform λ on the *gauge* weight only
rescales β, and the free energy is not linear in β. So item 3 is not
"insert an operator we already have". It is **put matter on the
lattice**.

## The field

For Spin(4) = SU(2)⁺ × SU(2)⁻ the natural matter is the bifundamental
(2,2) — which is a real 4-vector of SO(4), i.e. **a quaternion per
site**, in the arithmetic this program already runs on:

    (D_μ φ)(x) = U⁺_μ(x) φ(x+μ) U⁻_μ(x)† − φ(x) = R_μ(x)φ(x+μ) − φ(x)

Gated, not assumed:

| check | result |
|---|---|
| `Rφ` vs `U⁺φU⁻†` | 4.44e−16 |
| `RRᵀ = I` | 4.44e−16 |
| det R | 1.000000 … 1.000000 |

The link acts on matter as an **exact SO(4) rotation**, which is what
a (2,2) of Spin(4) must do.

## The source

Weight the links `w_l = e^{2λ_l}` and integrate the matter out:
`Γ[λ] = ½ ln det′(DᵀWD)`. Then 0125's identity, generalised to a
multi-component field (`B²_{lm}` → the Frobenius norm of the 4×4
block):

    Γ″[λ] = Σ_{l,m} ‖B_lm‖²_F (λ_l − λ_m)²,   B = D(DᵀD)⁺Dᵀ

`B` is the orthogonal projector onto range(D) — computed by SVD, which
is stable where forming `(DᵀD)⁻¹` is not.

**"T = Fisher" is then not an analogy.** The Fisher information of the
one-parameter family `W_p^{1+λ}` is `Var(ln W_p)` exactly, so the
source operator is defined rather than modelled.

## The theorem, in a quantum background

The identity is PSD with kernel exactly the constants **for any D** —
including a gauge-covariant one. So masslessness should survive
quantisation exactly. Checked rather than argued:

| background | Q(uniform λ) |
|---|---|
| flat | +4.5e−13 |
| **quantum (a real configuration)** | **−2.3e−13** |

> **The trust channel is massless in the quantum theory**, not only in
> the free background. That is what item 4's 1/r rests on.

## The number

| | |
|---|---|
| p_quantum / p_flat | **1.01423 ± 0.00006** (spread over configs 0.00031) |
| p_flat (0113) | 0.154932 per field |
| p_quantum | 0.157136 ± 0.000010 |

The quantum background **stiffens** the channel by +1.4%, so G moves
−1.4% and ℓ_P by −0.7%.

## A bug worth recording

The first run reported `1.01349 ± 0.00000` — an error bar of exactly
zero over 24 configurations. `as_links` returns **views** into the
live buffer, so all 24 stored configurations were the same one. Fixed
with copies, and an assertion now fails if the spread across
configurations is ever below 1e−12. Same class as 0132's
frozen-configuration bug: an assertion that passes on broken data is
worse than no assertion.
