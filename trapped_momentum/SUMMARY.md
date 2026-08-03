# trapped_momentum — SUMMARY

Reframing a particle as a massless excitation closed on itself — "a photon
chasing its own tail" — so that mass is trapped momentum and relativistic
kinematics follow from the constancy of `c`.

## Current state

The premise is **not** a departure from established theory: the Dirac velocity
operator `cα` has eigenvalues `±c` only, so a free electron already moves at `c`
instantaneously in standard relativistic QM, with the observed sub-luminal
velocity being the average of a `c`-speed jitter (zitterbewegung) at frequency
`2mc²/ħ` and amplitude `ħ/(2mc)`. The workstream is therefore an attempt to
take that structure as fundamental rather than emergent.

All results below verified in `output/0001_circulating_null_ray.py`
(39/39 checks, pure stdlib).

### What drops out exactly

- **Spin, with no free parameter.** A null ray on a loop of radius
  `r = ħ/(2mc)` gives `L = mcr = ħ/2` — the mass cancels identically — and
  circulation frequency `ω = c/r = 2mc²/ħ`, exactly the Dirac zitterbewegung
  frequency.
- **Both de Broglie relations.** An internal clock at `ω₀ = mc²/ħ`,
  Lorentz-transformed, *is* a plane wave: `φ = ω₀γ(t − vx/c²)` gives
  `ω = γmc²/ħ = E/ħ` and `k = γmv/ħ = p/ħ`. `E = ħω` and `p = ħk` are
  **theorems**, not postulates. Exact to machine precision from `v/c = 10⁻³`
  to `0.999`. The superluminal de Broglie phase velocity `c²/v` becomes just
  relativity of simultaneity applied to a clock synchronous in its rest frame.
- **Time dilation**, from `sin θ = v/c` on the helix: total speed `c` splits
  between circulating and translating, tangential component `c cos θ = c/γ`,
  tick rate `ω₀/γ`. Clean only for boosts **along the spin axis**; perpendicular
  boosts contract the circle and land in Thomas-precession territory.
- **A three-length identity:** `√(pitch · λ_dB) = λ_Compton` at every speed,
  since `pitch ∝ v` and `λ_dB ∝ 1/v`. They cross at `v = c/√2`, where `p = mc`.
  Corollary trap: **the de Broglie wavelength is not the helix pitch.**

### Correction to the original proposal

Acceleration does **not** reduce the trapped angular momentum. The circulation
rate falls by `γ` but the inertia rises by `γ`, so `L = (γm)(c/γ)r = mcr` is
**boost-invariant** — verified to `v = 0.999c`. This is a repair, not a
problem: spin magnitude is a Poincaré Casimir, so a model in which boosting
changed it would be wrong. The model gets it right automatically.

### The sharp defect

| loop radius | spin `L/ħ` | energy `ħω/mc²` |
|---|---|---|
| `ħ/(2mc)` | **0.5** ✓ | 2.0 ✗ |
| `ħ/(mc)` | 1.0 ✗ | **1.0** ✓ |

**Right spin or right energy, never both.** The factor 2 coincides with the
spinor double cover, and with the fact that zitterbewegung in Dirac theory is a
*beat* between positive- and negative-energy components — suggesting the
correct model has two counter-circulating pieces, not one. Neither observation
is a resolution. Closing this is the highest-value open problem.

## Empirical core: the reframing is already true for most mass

```
proton                       938.272 MeV/c²
sum of current quark masses    8.990 MeV/c²
from the Higgs mechanism        0.958 %
from confined energy-momentum  99.042 %
```

~99% of ordinary matter's mass is already trapped momentum — the Standard
Model's own accounting, not a hypothesis. The genuinely novel claim is only
that the remaining ~1% (Higgs-generated current-quark and lepton masses) works
the same way, and should be stated that narrowly.

The equivalence-principle payoff survives: confined energy-momentum sources
gravity as `E/c²` in GR, so inertial and gravitational mass agree for trapped
momentum **as a theorem**. Caveat with teeth: trapped radiation has
`p = ρc²/3` and active gravitational mass goes as `(ρ + 3p/c²)`; the box's
tension is what cancels it. **The model owes an account of what does the
trapping.**

## Prior art (the user asked; there is a lot)

- **Zitterbewegung** — Schrödinger 1930. The premise is textbook Dirac theory.
- **Hestenes' zitterbewegung interpretation** — Found. Phys. **20**, 1213
  (1990); arXiv:1910.11085. Electron as a point charge in *lightlike circular
  motion* at the Compton frequency, radius half the Compton radius, spin as
  that motion's orbital angular momentum. This is the proposal, already
  developed, over thirty years. **Read before developing further.**
- **de Broglie's internal clock** — 1924 "harmony of phases"; the derivation
  above is his. Probed experimentally by Catillon et al., *Found. Phys.* **38**,
  659 (2008) (electron channeling resonance at the Compton frequency) —
  contested, not replicated to consensus; cite as an attempt, not evidence.
- **Kerr–Newman electron** — Carter (1968): the Kerr–Newman solution with
  electron parameters gives gyromagnetic ratio **exactly `g = 2`**, with the
  ring singularity at `a = ħ/(2mc)`, the same half-Compton radius. A "ring of
  light at the Compton scale" reproducing `g = 2` from GR rather than QM.
- **Wheeler geons** (1955) — self-gravitating radiation bundles; exist only at
  absurd masses and unstable. The honest answer to "can radiation self-trap?"

## The three loose ends

- **Maxwell solution?** No — Maxwell is linear, hence no self-interaction and
  no self-trapping, structurally. But **Rañada's knotted fields** (1989) are
  exact source-free Maxwell solutions on the Hopf fibration with all field
  lines linked and conserved helicity: the desired topology is realisable in
  vacuum Maxwell even though it disperses. The needed nonlinearity would have
  to come from QED (Euler–Heisenberg) or gravity, neither remotely strong
  enough at the electron scale.
- **"Infinitely contracted space."** There is no rest frame for a lightlike
  path, so phrase it as the legitimate and stronger statement: **a closed null
  curve has zero proper length** (`∮ds = 0`). Every point of the loop is at
  zero interval from every other.
- **Which axis?** Both guesses have content and are not in competition.
  "Superposition over axes" is spin coherent states / the ordinary
  indefiniteness of a spin-½ axis. "Rotation around the time axis" points at
  the rest-mass phase `e^{−imc²t/ħ}` — a rotation at the Compton frequency
  present for every massive particle regardless of spin orientation, and
  exactly what Part 3 turns into `E = ħω`.

## What this may give back to the main line

The zero-proper-length null loop is the one place this workstream may
contribute rather than borrow. `foundations/0006` assigns correlational
structure to *spacelike* separation and dynamics to *timelike*. A null
structure has the same flavour — zero interval, no propagation, no applicable
speed — which raises whether the two-tier split wants a **null middle term**:
timelike dynamics / null internal structure / spacelike correlation.

## Known gaps

- **The factor of 2** — unresolved, and fatal to the naive one-ray version.
- **What confines the ray** — unaddressed; without it the pressure and
  active-gravitational-mass bookkeeping does not close.
- **Charge, and why three generations at the same spin** — entirely
  unaddressed. No lead.
- Nothing in this workstream is new physics. Its value is structural: one
  geometric premise reaching spin, both de Broglie relations, time dilation,
  and the equivalence principle. Do not overclaim beyond that.
