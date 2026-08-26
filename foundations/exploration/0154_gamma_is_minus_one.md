# 0154 — Item 6: γ = −1 in the diagonal sector, and why that is an obstruction rather than a verdict

> **AI-generated, not peer-reviewed.** Code: `output/0145_gamma_from_q4.py`.

Every classical test hangs off one PPN number:

    g_00 = −(1 − 2U),  g_ij = (1 + 2γU)δ_ij
    deflection ~ (1+γ)/2,   perihelion ~ (2+2γ−β)/3

**GR: γ = +1. A conformally flat metric: γ = −1 and ZERO light
bending** — null geodesics are conformally invariant. That is what
killed Nordström gravity in 1919, and 0125's matter coupling is
written conformally flat, so this is the sharpest test the program has
faced.

## The measurement

0142's identity holds for an *arbitrary per-link* weight, so nothing
new was needed — just let the weight depend on direction, which is a
diagonal metric:

    w_μ = √g g^{μμ}  ⟹  ln w = (J − 2I)a,   g_μμ = e^{2a_μ}

A static mass couples to the time-time stress alone, so the source
sits in direction 0; the response is δa = −[Γ″_a]⁻¹J_a and
**γ = −a_s/a_0** with a_s = (a₁+a₂+a₃)/3.

**Gate (s1):** force the coupling onto the trace mode and γ must come
back exactly −1. It does, to **2.22e−16**.

## The answer

L = 32, flat background, window rule from 0143 (keep r where the
temporal response is above 2% of its r = 1 value):

| r | a_0 | a_s | γ |
|---|---|---|---|
| 3 | −1.14381e−02 | −1.16665e−02 | −1.01997 |
| 5 | −4.99701e−03 | −5.00674e−03 | −1.00195 |
| 7 | −2.50191e−03 | −2.49527e−03 | −0.99735 |
| 9 | −1.21370e−03 | −1.20471e−03 | −0.99259 |

> **γ = −1.0058 over r = 1…9, spread 0.106, converging on −1.**

Classical tests as they stand: **deflection (1+γ)/2 = 0.000 × GR**.
Zero. Cassini measures γ − 1 = (2.1 ± 2.3)e−5.

## Why this is not yet a verdict

**The instrument is blind in a specific way, and it is blind to
exactly the sector that is supposed to carry the bending.** The link
weight `w_{x,μ}` can only carry a *diagonal* metric. The program's own
graviton is the spin-2 synergy sector — traceless-sym(B⁺⊗B⁻), 5 of 9
(0142/0146) — which has off-diagonal components.

The temptation is to call the diagonal restriction a gauge choice. It
is not:

> **(Γ″|_diag)⁻¹ ≠ (Γ″⁻¹)|_diag.** Restricting the variational space
> and then inverting is not the same as inverting and then
> restricting. The restriction biases the response, and it biases it
> in the direction of the conformal answer.

Having just spent item 2 learning that a null from a blind instrument
is not a result, calling this one fatal would repeat the mistake.

## The fix, derived

Extend the matter action to a full symmetric metric per site,

    S = Σ_x Σ_{μν} W_{μν}(x) (Δ_μφ)(x)·(Δ_νφ)(x),  W = exp(2A)

and expand ln det to second order in A. The generalisation of 0125's
identity is

> **Γ⁽²⁾[A] = tr(BA²) − tr(BABA)**,  B = D(DᵀD)⁺Dᵀ

which reduces to `½Σ‖B_lm‖²(λ_l−λ_m)²` when A is diagonal — checked
against 0142's form. A is then 10 components per site instead of 4,
and γ follows the same way.

## The honest statement of risk

If γ stays at −1 with the full symmetric W, **the program fails the
classical tests** and fails them the way scalar gravity failed in
1919. That is a real possibility and it should be run next, not
deferred. It is also the most falsifiable thing in the program — a
sharper test than the vacuum-energy target, and available now.

Item 6 is therefore **obstructed, with the obstruction named and the
fix derived** — not closed, and not failed.
