# 0097 — The marginalized vacuum: the ridge tilts, and the coordinate is the scale

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Step 1 of the crossing plan (owner's ordering: build the filter's
marginalization in the physics on analogy alone; then prove the
homomorphism proper; then use the filter as blueprint). Built, run,
and the success criterion — set in advance — is met, with an
attribution twist that lands the analogy even closer to the filter's
own machinery than designed. Code:
`output/0087_the_marginalized_vacuum.py`.

---

## 1. The design

The filter's breach of its biggest wall stratum: the GPB1 collapse
(one shared covariance for the hypothesis bank) makes the likelihood
*exactly flat* along a ridge — it cannot split a constant noise level
from a wandering one; per-hypothesis memory (IMM) tilts the ridge;
and the spread parameter must be **marginalized, never
point-estimated** ("a hypothesis set is not a point").

The physics has a provable ridge of its own: **0095's isotropy
theorem** — expand around the point vacuum (F = 0, Gaussian summary)
and sector structure (self-dual vs balanced content) is *exactly*
flat. So the experiment writes itself: replace the point vacuum with
**hypothesis-set vacua matched to the same second moments** — the
collapsed summaries identical by construction — and measure whether
the sector distinction reappears.

Three background ensembles on the six-plaquette vertex, one 36×36
covariance:

| | structure | kurtosis |
|---|---|---|
| H1 | geometric mixture (random tetrad packs) | 5.95 |
| H0 | the Gaussian collapse of H1 (Cholesky of its covariance) | 2.99 |
| H2 | scale mixture of H0 (radial two-point mixing; no geometry) | 6.02 |

## 2. The ridge tilts

Sector split of a t = 0.5 source probe (paired SD vs balanced,
common backgrounds, 2000 draws each):

```
isolated (no background):      +1.706
H0  collapsed Gaussian:        +0.004 ± 0.003     — flat
H1  geometric mixture:         +0.473 ± 0.006     — 75σ
H2  scale mixture:             +0.501 ± 0.012     — 42σ
```

Same second moments throughout. The collapsed vacuum **erases sector
structure entirely** — the bath, taken at its mean strength, screens
even the isolated splitting to 0.2%. The marginalized vacua keep it
alive at half its bare value. The flat direction of the collapsed
treatment is an artifact of the collapse; the physics the collapse
deletes is exactly the physics we were missing.

## 3. The attribution: it's the scale

The control decides what carries the information: H2 ≈ H1
(difference −0.028 ± 0.013). At this observable the sector
discrimination rides the **radial mixture** — epochs of weak bath,
where the probe is read almost unscreened — not the tetrad
orientation structure (which, if anything, screens slightly more).
The marginalized coordinate that matters is **the scale of the
vacuum's fluctuations**, not their shape.

Which snaps the analogy onto the filter's exact hardware: the
sector-carrying channel is *their wandering-scale channel* — s_P > 0.
The collapsed vacuum is their **self-confirming s_P = 0** (the
fixed-scale theory that concludes it needs no scale channel because
it evaluated itself with the collapsed likelihood). And their next
design item — *marginalize the (φ_P, s_P) grid, because a hypothesis
set is not a point* — is, word for word, what the physical vacuum
needs: not a background, and not even a background ensemble at fixed
strength, but a **marginalized distribution over vacuum scales**.

## 4. What this closes and opens

- It closes a loop with 0092: the ledger's high kurtosis — the
  structure RG localization must kill to reach heat-kernel
  universality — is the same structure that carries sector
  information at the vertex. **Universality and sector-blindness are
  one phenomenon; discrimination lives in the non-Gaussian
  remainder.** The strong-coupling question ("which sector wins in
  the vacuum?") is now precisely the question of what the vacuum's
  scale-mixture looks like — and the τ flow (0093) says the scale
  *runs*, so a multi-scale vacuum is not exotic; it is what an RG
  trajectory already is.
- It reframes 0095's honest verdict: "no sector splitting at one
  loop" was true of the collapsed vacuum and *diagnostic of the
  collapse*, not of the theory.
- Per the plan, success here does not prove the correspondence — it
  motivates step 2: **the homomorphism proper**, whose proof should
  show exactly which structures transport (and which don't — the
  isomorphism gap), turning analogy into prototype.

## Honest limits

- One observable (a one-slot SD/balanced shift at t = 0.5,
  ε′ = 0.01), one bath strength, one radial-mixture shape. The
  geometry-vs-scale attribution is at this observable; orientation
  structure could matter for multi-slot or loop observables (0088's
  lensing says it does for *aligned* probes).
- The ensembles are hand-built hypothesis sets, not derived from the
  measure; the derived version — the vacuum's actual scale
  distribution under the interacting measure — is the strong-coupling
  computation, now with a sharper target (its radial profile is the
  physical s_P).
- Analogy-first by design (the owner's step 1); the homomorphism
  proof (step 2) is where this either becomes structure or breaks
  informatively.

## Open

1. **Step 2 — the homomorphism proper**: state both families as
   transfer semigroups with confidence channels and prove/refute the
   structure-preserving map; catalogue what fails (the isomorphism
   gap) as the toy-to-prototype upgrade list.
2. The derived scale distribution of the interacting vacuum (the
   strong-coupling MC's new, sharper question: measure the vacuum's
   radial mixture, i.e. the physical s_P).
3. The filter blueprint's pressure point after step 2, per the
   owner: regime-hazard (their 6.8% stratum) — the closure-family
   question, tractable on their side first.
