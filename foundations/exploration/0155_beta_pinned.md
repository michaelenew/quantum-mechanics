# 0155 — Item 7: β pinned non-perturbatively, and the band moves

> **AI-generated, not peer-reviewed.** Code: `output/0144_matching_beta.py`.
> Prior art credited in [`ATTRIBUTION.md`](../ATTRIBUTION.md).

0141 left the hierarchy with a two-decade band because β had two
handles that disagreed by 1.5, and one unit of β is a factor 15 in
aΛ. The weak handle was `⟨½trU_p⟩ = 1 − 3/(4β)` — the leading term of
a perturbative series, used at the 4% level.

**Replace it with a matching.** Run the actual Wilson double copy
through the same kernel on the same lattice and find the β_W that
reproduces the derived weight's own plaquette. Non-perturbative, and
entirely self-contained — no series, no external input.

## The scan

Derived weight: `⟨cos θ⟩ = 0.956952 ± 0.000007`,
`Var = 1.1283e−03 ± 5.1e−07`.

| β_W | ⟨cos θ⟩ | Var(cos θ) |
|---|---|---|
| 17.00 | 0.955340 | 1.3133e−03 |
| 17.50 | 0.956617 | 1.2398e−03 |
| 18.00 | 0.957843 | 1.1706e−03 |

**Matched on the plaquette: β_W = 17.637.**

## The second observable — matching on one moment defines a scheme, not a coupling

So predict a second one. Wilson at β_W = 17.637 predicts
Var = 1.2208e−03; the derived weight has 1.1283e−03. **Deviation
−7.58%, −182σ.** The β that fits the variance instead is
**β_V = 18.351**.

> **The moments disagree. The derived weight is not Wilson, and no
> single β_W represents it.** The gap — **0.714 in β** — is the
> irreducible scheme ambiguity, now *measured* rather than guessed.

## The band

| β | aΛ_L | ξ/a | |
|---|---|---|---|
| 16.000 | 1.2934e−18 | 7.73e+17 | curvature (0141) |
| 17.540 | 2.1296e−20 | 4.70e+19 | perturbative — **retired** |
| **17.637** | 1.6454e−20 | **6.08e+19** | matched, plaquette |
| **18.351** | 2.4490e−21 | **4.08e+20** | matched, variance |

0141's band was a factor **60**. The matched band is
**6.1e19 … 4.1e20**, a factor **6.7**.

Two consequences, and the second is not comfortable.

**(i) β = 16 is excluded.** The derived weight's actual plaquette
corresponds to Wilson at 17.64. **κ = 16.000 remains exact as the
curvature at the identity** — 0141's measurement of that stands — but
it is *not* the coupling to feed the two-loop formula. The full weight
has higher character content and behaves stiffer.

**(ii) The band moves away from the reference point.** M_Planck/1 GeV
= 1.22e19 now sits **below** the matched band by a factor 5 to 33.

> 0141 noted that the observed hierarchy fell inside the band and was
> careful to call the order robust and the digit not. The better
> measurement shows that **the agreement was a consequence of the
> band's width, not of the physics.** Narrowing it removed it.

That is the correct outcome of doing the measurement properly, and it
is worth more than the coincidence it replaced. The derived-knob
candidate survives — a derived O(10) coupling still exponentiates into
a derived O(10²⁰) hierarchy with nothing tuned — but it no longer
lands on the observed number, and any future claim has to explain the
factor 5–33, not celebrate it.
