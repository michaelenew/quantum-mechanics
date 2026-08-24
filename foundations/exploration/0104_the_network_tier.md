# 0104 — The network tier: the lattice is a bank of S³ filters, and its smoother predicts the dressed vacuum

Second isomorphism stone. Everything proven so far is chain-shaped;
the physics object is a network — one S³ state per link, one
likelihood factor per plaquette, each link serving six factors.
Code: `output/0094_the_network_tier.py`.

## 1. The exact statement

The single-link conditional of the lattice measure is
p(U | rest) ∝ Haar(U) × Π₆ W_τ(angle(U·Sᵢ)) — a Bayes update with
Haar prior and six staple observations. The heat-bath kernel *is*
the S³ filter's update; the lattice measure *is* the bank's joint
posterior. This is the measure's own factorization — the content is
the identification, and the two quantitative sections cash it in.

## 2. The Gaussian sector predicts the dressed curve, zero knobs

In the small-angle sector the bank is 0095's Maxwell theory (u = DA,
D the lattice curl) — a Gaussian smoother on the link graph. Its
prediction: ⟨θ²⟩ = 3R/κ(τ), with κ the weight's local precision
(−(ln W_τ)″ at the origin — the *filter's* native object) and
R = rank(D)/P = 765/1536 the physical-mode fraction (kernel = 255
gauge + 4 Wilson modes, counted by SVD). Against 0092's measured
primary curve:

| τ | κ | predicted | measured | ratio |
|---|---|---|---|---|
| 0.00 | 13.33 | 0.1121 | 0.0968 | 1.16 |
| 0.05 | 10.44 | 0.1431 | 0.1322 | 1.08 |
| 0.15 | 6.93 | 0.2156 | 0.2124 | **1.015** |
| 0.30 | 4.43 | 0.3376 | 0.3494 | 0.97 |
| 0.60 | 2.43 | 0.6149 | 0.6843 | 0.90 |
| 1.20 | 1.15 | 1.2980 | 1.6074 | 0.81 |

The free filter-bank theory tracks the interacting vacuum across the
whole flow — within 1.5% at mid-flow, 16% at the stiff end
(anharmonicity), 20% only at the compact/Haar end. And it *had* to
be curvature, not moments: matching the bare weight's second moment
instead predicts 0.208 at τ = 0 — wrong by 2.1×. The filter's local
precision is the physically correct notion of the weight's strength.

## 3. Revision: the scale field is (almost all) kinematics

The same Gaussian bank, sampled exactly and scored with 0091's own
observables:

```
                Gaussian bank    measured (0092, τ=0)
  sP_exc          +0.0134          +0.0120
  c(1)            +0.0515          +0.0474
  c(2)            −0.0045          −0.0046
```

0101 read the scale field as surviving interaction structure; 0102
read its plateau as a property of the flow's transition region.
**Both readings revise**: the field's amplitude, its short range,
and even its negative d = 2 tail are reproduced — slightly
*over*-predicted — by the free Gaussian bank. The "wandering scale"
is link-sharing kinematics: any bank with this sharing pattern shows
it, interaction or none. What is genuinely non-Gaussian is the small
deficit (measured sits ~10% below the Gaussian baseline at τ = 0,
converging to it at mid-flow where the marginal is most Gaussian,
and collapsing at τ = 1.2 where the small-angle sector itself
dies). The house policy paying out again: the revised statement is
sharper *and* strengthens the isomorphism — the dressed vacuum,
marginal and field observables alike, IS the Gaussian filter-bank
smoother to ~10%, with the interaction living in the deviation
pattern along the flow.

## 4. The gauge quotient

The interacting measure's single-link marginal is exactly Haar
(⟨w²⟩ = 0.2500 on 0092's checkpoints): a link coordinate is pure
nuisance. Gauge orbit = the filter's unidentifiable directions;
identifiable content = class functions of loops = image(D). The
quotient the physics takes by symmetry is the quotient the filter
takes by identifiability — the same operation, named twice.

## Honest limits

- The Maxwell sector is the free tier of the network; the 10–20%
  residuals are the interacting content, identified but not yet
  derived (anharmonic corrections at small τ, compactness at large).
- s3's baseline is L = 4; the volume-stability of the measured
  numbers (0092) makes volume corrections unlikely to change the
  verdict, but they were not recomputed for the Gaussian bank.
- The lucid feed (0004) quoted s_P, φ as "physical trust-channel
  values"; the revision reclassifies them as *architectural*
  (kinematic) baselines — corrected there in the same push.

## Open

1. Derive the τ = 0 anharmonic correction (the 16%) from the
   quartic term of ln W — the first interacting network computation.
2. The deficit pattern (measured − Gaussian) as the honest
   interaction observable: recompute along the flow with errors.
3. The vertex tier (joint structure beyond product weights): the
   GPB1 ↔ vertex identification, still assertion-grade — candidate
   theorem: both equal the dropped total correlation.
