# 0153 — Item 4: the response measured, and the 1/r read

> **AI-generated, not peer-reviewed.** Code:
> `output/0143_read_the_one_over_r.py`. Depends on 0152, lucid 0049.
> Prior art credited in [`ATTRIBUTION.md`](../ATTRIBUTION.md).
>
> **Prior art.** Sakharov (1967); Einstein (1915) for the Newtonian limit being recovered.

Masslessness is not 1/r. lucid 0049 was emphatic: the same massless
field reads 1/r, 1/r², or *no decay at all* depending on the
projection. So this measures the profile.

## Does the quantum background distort, or only rescale?

Ratio p_quantum/p_flat at every available lattice momentum:

| k (units 2π/L) | ratio |
|---|---|
| 1 | 1.01429 ± 0.00012 |
| 2 | 1.01000 ± 0.00008 |

Spread across momenta **0.42%** of the mean. **Flat in k** — the
quantum background rescales the stiffness and leaves the dispersion
alone. No mass, no distortion.

## Three wrong instruments, then the right one

This took four attempts and the first three are the useful part.

**s2 — fit A/rⁿ + C.** n = 1.045 at L = 32. Newtonian-looking. But
lucid 0049's pre-registered 2-nat criterion **failed**: a Yukawa with
m = 0.100 beat pure 1/r by **3.13 nats**.

**s2b — is it the box?** A wrap artifact scales as 1/L. At a *fixed*
window r = 1…6: m = 0.210, 0.125, 0.105, 0.095, 0.095 for
L = 16…64. **It plateaus.** Not wrapping.

**s2c — is it short distance?** Move the window outward at L = 64:
m = 0.095, 0.035, 0.040, 0.105 for windows 1–6, 4–12, 8–20, 14–30.
Falls, then rises again — because the outer window is back in the
wrap region. Inconclusive, and honestly so.

**s2d — a same-volume reference.** The instrument was the problem. A
Yukawa fit on a periodic box absorbs short-distance structure at one
end and wrapping at the other into a *fake mass*. Instead build the
static response of an exactly massless lattice Laplacian `1/k̂²` on the
**same volume, same zero-mode removal, same projection**, and take the
ratio — every artifact cancels.

| r | induced | massless ref | ratio |
|---|---|---|---|
| 1 | +8.934580e−02 | +8.253725e−02 | 1.08249 |
| 4 | +1.800583e−02 | +1.677137e−02 | 1.07361 |
| 8 | +6.990607e−03 | +6.501945e−03 | 1.07516 |
| 12 | +3.438716e−03 | +3.211830e−03 | 1.07064 |
| 16 | +1.729058e−03 | +1.628849e−03 | 1.06152 |

Window rule, stated rather than eyeballed: keep r where the reference
is still above 2% of its r = 1 value — outside that both curves are
crossing zero (removing the k = 0 mode forces their 3D sum to vanish)
and a ratio is undefined. That gives r = 1…15.

> **Ratio 1.0722, spread 1.68%, across a factor 15 in r.** The induced
> static response *is* the massless lattice Coulomb profile times a
> constant. **The 1/r is there.**

The Yukawa masses in s2b and s2c were the instrument, not the physics
— as 0152's exact uniform-λ zero already required.

## The number

| | p | G = 1/(4πp) | ℓ_P |
|---|---|---|---|
| one field | 0.156813 | 0.5075 a² | 0.7124 a |
| **graviton, 2 polarisations** | 0.313627 | **0.2537 a²** | **0.5037 a** |

Item 5 retired the factor 20 and put ℓ_P at 0.507a. The quantum
background moves it to **0.5037a** — a −0.7% correction, inside the
band item 5 already quoted. Real, and small.

## Two corrections owed back to lucid 0049

1. **A Yukawa-vs-1/r fit on a periodic box is not a safe test of
   masslessness.** It rejected a provably massless channel at 3.1 nats
   against a 2-nat threshold. Use a same-volume massless reference.
2. **Any ratio test needs a stated window rule**, because removing the
   zero mode forces a zero crossing.

Both are ported back.
