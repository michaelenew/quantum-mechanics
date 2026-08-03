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

### Correction to the original proposal, and why it matters (`exploration/0002`)

Acceleration does **not** reduce the trapped angular momentum. Pressed on this
directly, and the reason it cannot is the reframing's own central claim:

- A boost along the spin axis leaves `p_⊥` **exactly** untouched and creates
  `p_∥` from nothing. Total `|p| → γ|p|`, so the ray's total wavelength gets
  *shorter*, not longer.
- "`n` wavelengths around the loop" constrains `λ_⊥ = 2πr/n`, and both `λ_⊥`
  and `r` are transverse, hence boost-invariant. The quantization condition is
  not strained by the boost, it is **untouched** by it.
- Procession genuinely does slow (`Ω → Ω₀/γ`) — but transverse inertia rises,
  `I = γmr²`, and `L = IΩ = mcr` exactly. **Angular frequency and angular
  momentum decouple**; a null ray is not a rigid body.
- Cheapest proof: `J^{xy}` is the tensor component a `z`-boost cannot act on
  (`Λ^x_α = δ^x_α`). Generally, spin magnitude is the Pauli–Lubanski Casimir —
  a model whose spin changed under boost would not be relativistic at all.

**`L = r·p_⊥ = r·mc`, so if `L` fell under a boost, rest mass would fall under
a boost.** "Angular momentum is invariant" and "rest mass is invariant" are one
fact, not two.

### The Pythagoras identity — and its demotion (`0002`, then `0003`)

```
m c = p_⊥      p = p_∥      E² = (p_⊥c)² + (p_∥c)² = (mc²)² + (pc)²
```

Verified to machine precision through `v = 0.999c`. But this is a **frame-
adapted** reading, not a covariant one: it requires choosing a spin axis and
boosting *along* it. Boost perpendicular and the loop contracts to an ellipse,
the ray is Doppler-modulated around the circuit, and no instantaneous
trapped/translating split survives. Keep as intuition, not as the definition.

### The covariant version: the helix axis is timelike (`exploration/0003`)

The rest-frame worldline `x^μ(t) = (ct, r cos Ωt, r sin Ωt, 0)` is a **null
helix winding about the particle's own timelike CoM worldline**. Verified:
`ds² = 0` throughout, `|v| = c`, spacetime pitch angle exactly **45°** (the
null condition as geometry).

**"Rotation around the time axis" is literal, not loose.** The helix axis is
frame-covariant; the spatial circulation plane is only its 3D shadow — which is
why choosing a spatial axis felt arbitrary. It is arbitrary.

Boosting **tilts that axis** (`tan(tilt) = β`, verified); the winding is
unchanged. Inertia is resistance to the tilt. Frame-independently:

> A boost can always remove the spatial momentum. It can **never** remove the
> rest energy. `mc²` is the irreducible timelike component of `P^μ` — the
> minimum of `E` over all frames (checked over 3999 boosts).

That states inertia with no reference to any spatial direction.

### The obstruction, and the distinction that survives it

Mass and spin are the **two independent Poincaré Casimirs** (`P·P`, `W·W`), so
mass cannot simply *be* an angular momentum. Empirically blunter: **massive
spin-0 particles exist** (Higgs, π⁰). A model where mass *is* trapped angular
momentum forbids them.

> **The trapped thing is energy–momentum, not angular momentum.** How it
> circulates is a separate question, and that answer is the spin.

"Mass is trapped momentum" survives; "mass is trapped *angular* momentum" does
not. The two were being run together.

**Counter-circulation resolves it:** two opposed rays at `E/2` each cancel in
spin and add in energy → massive, spin 0. This is the **same structural fix**
already flagged for the factor of 2, which raises its priority considerably.

### A corollary that worsens the factor-2 problem

Running the quantization route alone: `L = r·p_⊥ = r·nh/(2πr) = nħ`. The radius
cancels and the answer is an **integer** multiple of `ħ` for any loop. The
wavelength-counting picture cannot reach `ħ/2` at all. So the defect is not a
bad choice of radius but something structural about one ray winding an integer
number of times — strengthening the two-counter-circulating-components reading.

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

- **Kaluza–Klein** — the closest prior art to the core claim, and the one that
  *supports* rather than constrains it. A massless field with momentum
  quantised on a compact dimension of radius `R` appears in 4D as massive:
  `m = nħ/(Rc)`, hence `L = mcR = nħ`. "Mass is trapped momentum" as a standard
  derivation rather than a picture. It dissolves the "which axis" question
  (no spatial axis to choose), explains the loop's invisibility rather than
  assuming it, and reproduces the same integer-only `L = nħ` — localising the
  factor-2 defect to the spin side, not the mass side. Open tension: KK's
  compact direction is spatial, while `0003`'s winding axis is timelike, and a
  compact timelike direction is normally pathological.
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

## Differential relativity (`exploration/0002`)

The programme: spacetime as the global frame handling the relations, curvature
implicit in inter-particle relationships, and mass appearing twice — as inertia
and as sourced curvature — so the two have one explanation.

**Delivered.** Inertia gets a real mechanism: `p_⊥` cannot be converted into
`p_∥` (a boost only *adds* longitudinal momentum, in quadrature), so
**inertia is the rigidity of the trapped component**. If `p_⊥` could be spent,
acceleration would be free. And the same `p_⊥` enters `T_μν`. So "two effects,
one explanation" holds — **at the level of identifying the quantity, not of
deriving the field equations.** GR already ties the two via `T_μν`; what this
adds is a reason the quantity is the *same* one. Intuition, not new dynamics.

**Prior art.** Mach's principle (which GR does *not* implement — Minkowski has
inertia with no matter); Barbour–Bertotti shape dynamics (nearest neighbour to
P1); Sakharov induced gravity (1967); **Jacobson (1995)**, PRL **75**, 1260,
deriving the full Einstein equations from `δQ = T dS` on local Rindler horizons
— the existence proof that the programme is achievable, and the one to read
first; Van Raamsdonk / Ryu–Takayanagi (the same conjecture from the field side,
already the open frontier in `foundations/0005`); Verlinde and Padmanabhan.

**The obstruction.** Any relational construction must reproduce a massless
**spin-2** interaction — Weinberg's soft-graviton theorem forces universal
coupling, Deser's bootstrap iterates self-coupled spin-2 to full GR. Scalar
gravity (Nordström) predicts **zero** light deflection; vector makes like
charges repel. **First test: does the construction bend light, and by the GR
coefficient?** Cheap, and the fastest way to learn whether the idea survives.

**Speculative lead.** A null-ray particle carries a *circulation plane*, so the
relational data between two of them is plane-to-plane — naturally rank-2
symmetric, not scalar. That is the right index structure for a spin-2 mediator
and exactly what mass-to-mass cannot supply. Most likely place a route past the
obstruction lives. Not computed.

**Constraint to respect.** If inertia derives from relations to anisotropically
distributed matter, inertial mass could become direction-dependent.
Hughes–Drever bounds the fractional anisotropy to `<10⁻²⁰` (modern versions
`~10⁻²⁸`). In fairness: **Dicke (1961) showed this does not refute Mach** —
it requires the anisotropy be universal across species, hence locally
unobservable. A design constraint, not a falsification.

## Cross-link to `gravitation/`

The which-branch thought experiment forces the gravitational field to be **an
edge in the web rather than a function of the state**. That is the same
commitment differential relativity starts from, reached independently from a
superposition-and-causality paradox. Mutual support — with the caveat that
agreeing on an ontological commitment is far from producing dynamics.

## What this may give back to the main line

The zero-proper-length null loop is the one place this workstream may
contribute rather than borrow. `foundations/0006` assigns correlational
structure to *spacelike* separation and dynamics to *timelike*. A null
structure has the same flavour — zero interval, no propagation, no applicable
speed — which raises whether the two-tier split wants a **null middle term**:
timelike dynamics / null internal structure / spacelike correlation.

## Known gaps

- **The factor of 2** — unresolved, and fatal to the naive one-ray version.
  Sharpened by `0002`: the wavelength-quantization route gives `L = nħ` for any
  radius, so it cannot reach `ħ/2` by construction. **Top priority
  calculation** (`0003`): two components with oppositely-rotating phases
  `e^{∓imc²t/ħ}`, co-rotating spatially, beat at `2mc²/ħ` — exactly the
  zitterbewegung frequency. Does the spin then come out `ħ/2` rather than
  cancelling? This single calculation bears on the factor of 2, the spin-0
  problem, and the double cover at once. Not shown.
- **Timelike winding axis vs KK's compact spatial dimension** — not reconciled;
  they are different claims and one may have to go.
- **Light bending by the relational construction** — the cheapest falsifier of
  differential relativity, and untried. Do this first.
- **The plane-to-plane rank-2 lead** — speculative, uncomputed.
- **What confines the ray** — unaddressed; without it the pressure and
  active-gravitational-mass bookkeeping does not close.
- **Charge, and why three generations at the same spin** — entirely
  unaddressed. No lead.
- Nothing in this workstream is new physics. Its value is structural: one
  geometric premise reaching spin, both de Broglie relations, time dilation,
  and the equivalence principle. Do not overclaim beyond that.
