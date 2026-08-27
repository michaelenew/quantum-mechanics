# trapped_momentum — SUMMARY

> **AI-generated, not peer-reviewed.** Prior art credited in [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results are re-derivations of
> established work unless explicitly marked otherwise.

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

### Causal type of the winding plane, and quantization (`exploration/0004`)

**The central result of the workstream.** A 2-plane in Minkowski space has an
induced metric whose determinant sign is Lorentz-invariant and takes exactly
three values — there is no fourth case:

| `det g` | type | motion | class |
|---|---|---|---|
| `> 0` | spacelike | rotation | elliptic |
| `< 0` | timelike | boost | hyperbolic |
| `= 0` | null | null rotation | parabolic |

"The time axis, the space axis, or their `x = t` line" **is** this
classification, forced by the metric signature rather than chosen.

**Quantization is compactness.** Pushing a test vector around each motion: only
the spacelike plane gives a closed orbit (`|orbit(2π) − start| = 7×10⁻¹⁵`); the
boost runs off along a hyperbola (`10¹⁷` by `s = 40`), the null rotation along
a parabola. Running the Fourier argument in both: on a circle,
`(1/2π)∫e^{i(m−n)θ}dθ = δ_{mn}` to 1e-17 → **discrete**; on the line, overlap
decays as `sinc` and *any* real mode number is admissible → **continuous**. The
orthogonality integral produces a lattice only when the domain is compact.

**Prediction ledger, scored against measurement:**

| plane | orbit | spectrum | observable | experiment |
|---|---|---|---|---|
| spacelike | closed | discrete | spin | quantized, `ħ/2` steps ✓ |
| null | open* | discrete* | helicity | quantized, `±1` photon ✓ |
| timelike | open | continuous | **mass** | **not** quantized ✓ |
| timelike | open | continuous | rapidity | continuous ✓ |

\* the parabolic motion is itself open; massless states escape a continuum only
because the null-rotation generators annihilate them, leaving a compact circle
about the momentum. Same rule applied to what survives.

The third row is the result: if mass came from a closed winding it would arrive
in a ladder. `m_μ/m_e = 206.768`, `m_τ/m_μ = 16.817` — no pattern. **The split
between "mass is continuous" and "spin is quantized" falls out of the causal
type of the plane**, from the proposal's own structure.

**On the KK tension from `0003`** — `0004` concluded that the absent mass ladder
favours an open (timelike) winding over KK's compact one. **`0005` shows that
was too quick.** Sweeping a one-parameter family of planes
`span{(a,0,0,1),(0,1,0,0)}` (`det g = 1−a²`), the generator's eigenvalues are
`±i√(1−a²)`, so a spacelike winding is closed with frequency `ω = √(1−a²)` and

> **level spacing ∝ √(1−a²) → 0 as the plane approaches null.**

So a **near-null** winding is genuinely quantized yet has spacing too fine to
resolve — apparent continuity from real quantization, which is exactly the
proposed mechanism. Mass continuity becomes a property of how the plane sits
relative to the time axis (an effect of the implied geometry) rather than
something intrinsic. KK is back in play provided the winding is near-null.

Honest status: with `n` and `a` both free per particle, `m = n√(1−a²)·scale`
fits anything, so this explains *how* apparent continuity arises but predicts
no value. It becomes predictive only if something independent fixes `a`.

### The photon break, and the reorganisation (`exploration/0006`)

The naive formulation **fails for the photon**: `sin θ = v/c` at `v = c` gives
`p_⊥ = 0`, hence `L = 0`, against a measured helicity of `±1`. Real internal
contradiction. The fix was already in the trichotomy, unused.

**A null plane carries no timelike direction at all** — for `w = ak + bx`,
`w·w = −b² ≤ 0`, never positive. Scanning every direction: spacelike plane has
0 timelike, timelike plane has 1798/3600, **null plane has 0**. So it can spin
spatially with no time-axis content, which is exactly what was wanted.

**And the null plane *is* a photon field.** Writing `F = k ∧ x` gives
`|E| = |B| = 1`, `E·B = 0`, `E × B` along `k`, and **both Lorentz invariants
vanish** — the signature of radiation, holding in every frame because no frame
removes either component. Nothing fitted. (Contrast: `x∧y` is pure magnetic,
`t∧x` pure electric; each has a frame killing the other. Only the null case
does not — which is why it moves at `c` for everyone.)

**Helicity's two states fall out for free.** A null vector is orthogonal to
*itself*, so `k^⊥` is 3-dimensional but degenerate (rank 2). Quotienting the
null direction leaves a 2D spacelike polarization plane carrying only `SO(2)`
→ one number, two signs. Massive: `u^⊥` is 3D nondegenerate → full `SO(3)` →
spin as a 3-vector with `2s+1` states. **The photon's missing longitudinal
state is the direction that got quotiented away** — from `k·k = 0`, not a rule.

**The `u + S` reorganisation proposed here is RETRACTED** (see `0007`). It was
Frenkel–Pirani asserted rather than derived — three structures fitted to what
is already measured, in place of one object. What survives from `0006` is the
null-plane-is-a-photon-field result and helicity from the degeneracy of `k^⊥`.

### One object: split quaternions (`exploration/0007`)

The proper fix. Split quaternions, `i² = −1`, `j² = k² = +1`. For **any** pure
`v = bi + cj + dk`:

```
v² = −(b² − c² − d²)·1  ≡  −Q(v)·1
```

The square of a pure element is a **scalar**, so one number controls everything
it can do — and the trichotomy of `0004` is just the sign of `Q` on **one
object**, not three structures:

| | `exp(θv)` | orbit |
|---|---|---|
| `Q > 0` | `cos(θ√Q) + v sin(θ√Q)/√Q` | closed, period `2π/√Q` |
| `Q < 0` | `cosh + v sinh` | open, exponential |
| `Q = 0` | **`1 + θv` exactly** (series terminates) | open, **linear only** |

**The point.** `i² = −1` makes the `i`-part genuinely *rotational*; `j,k` square
to `+1` and are *boost* content. So `Q` is rotation² minus boost². A
**nilpotent** (`i+j`) has rotational component `b = 1 ≠ 0` — **genuine spin** —
with `Q = 0` — **no mass, no rest frame**. Rotation exactly balanced against
boost, so it never enters the invariant.

> "No projected evidence of rotation in time but spinning in space" is exactly
> `b ≠ 0` with `b² − c² − d² = 0`. **The nilpotents are the light cone of the
> algebra** — lightlike character and nilpotency are one fact.

Also unifies earlier results: the `2×2` nilpotent has `N² = 0` while `0004`'s
`4×4` vector-rep version had `N³ = 0`, because the vector rep is the **symmetric
square** (verified). And `0005`'s level-spacing collapse is recovered as
**mass ~ `√Q` = distance from the nilpotent cone**, so apparent continuity near
the cone and exact masslessness on it are one phenomenon.

**Scope.** Split quaternions are 2+1 dimensional. The 3+1 version is `sl(2,ℂ)`,
where `X² = −det(X)·1` still holds but `det X` is complex, giving a **fourth**
class: **loxodromic** — rotation *and* boost about one axis.

### The loxodromic case: one object, mass and spin (`exploration/0008`)

Answered. Write `X = (ζ/2)(n̂·σ)` with `ζ = η − iθ` the **complex rapidity**
(boost `η` and rotation `θ` about the *same* axis). Then `det X = −ζ²/4`, and
the four classes are four regions of one complex parameter.

**`det X` carries both bivector invariants** — the gap `0005` flagged:

```
Re(det X) = (θ² − η²)/4  ~  F·F   ~  B² − E²
Im(det X) = ηθ/2         ~  F·F̃   ~  E·B      ← nonzero only for loxodromic
```

This exposes a limitation in `0004`: it classified by **one** invariant, so a
loxodromic element with `θ = η` (`Re det = 0`, `Im det ≠ 0`) would have been
misfiled as null/massless. It is neither.

**A massive spinning particle is not a plane.** A bivector is simple (a single
plane) iff `F·F̃ = 0`, so loxodromic ⟺ **non-simple** — and a non-simple
bivector has a *canonical* decomposition into two orthogonal simple pieces. That
is a theorem about the one object, not a case-split. Verified explicitly:
`span{t,z}` closed with a **boost** of rapidity `η`, `span{x,y}` closed with a
**rotation** by `θ`, the two orthogonal complements. **So `0006`'s imposed
`S^{μν}u_ν = 0` is automatic** — the hack is retired, not merely retracted.

**Mass is having an axis.** `det X ≠ 0` → distinct eigenvalues → two
independent eigendirections → an invariant timelike plane → a rest frame →
massive. `det X = 0` → the eigendirections **collide** (`|v₁×v₂| = 0`) → no rest
frame → massless. Masslessness is the matrix being **defective**; "has a rest
frame" and "is diagonalizable" are the same statement. Sharper than `0007`'s
distance-from-the-cone, and agrees with it (`|det X|` *is* that distance).

**The flow factors: compact × non-compact.** `exp(sX)` has eigenvalues
`exp(±s(a+ib))`; the phase returns to zero at *every* multiple of the period
while the modulus grows and never returns. Applying `0004`'s rule to each
factor:

```
compact factor     → DISCRETE   → spin
non-compact factor → CONTINUOUS → momentum
```

One object gives a quantized spin and a continuous momentum. They need no
gluing — they are the two factors of one flow.

**The whole taxonomy from one family:** `θ→0` pure boost (massive, **spin 0**);
`η→0` pure rotation; axis→null nilpotent (**massless**, helicity); both nonzero
**loxodromic** (massive **with** spin, generic). Massive spin-0 — the case that
forced the retracted hack — is just `θ = 0`. The particle taxonomy is the
conjugacy classification of one-parameter subgroups of `SL(2,ℂ)`, **with no
case-splitting anywhere.**

Masslessness is worth one more line: `det X = 0` is **not** `ζ = 0` (that is
`X = 0`). It needs a **complex null axis** `n̂·n̂ = 0`. Masslessness is a
different *kind* of axis, not a limit — which is why no tuning of `η, θ` reaches
it, and why `0006` felt forced into a separate case.

### Spin-0 objection: withdrawn

`0003` raised massive spin-0 particles (Higgs, π⁰) against "mass is trapped
angular momentum" — but that claim was never made; the proposal said *trapped
momentum*, and the conflation was introduced in these notes. Under the causal-
type reading the objection dissolves anyway: mass is timelike winding, spin is
spacelike winding, and a massive spin-0 particle simply has the first without
the second. `0003` is annotated accordingly.

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

**Done (`exploration/0005`).** A winding plane is a bivector
`F^{μν} = u^μv^ν − u^νv^μ`, and its unique symmetric rank-2 bilinear
`T^{μν} = F^{μα}F^ν_α − ¼η^{μν}F²` is **symmetric and traceless for every plane
type** — the graviton's index structure, by the algebra of 2-forms with nothing
electromagnetic assumed.

The discriminator is decisive. Scalar exchange contracts as `(tr T)(tr T′)`;
spin-2 as `T^{μν}T′_{μν} − ½(tr T)(tr T′)`. Every source here is traceless, so

> **the scalar amplitude vanishes identically.** Scalar gravity is not
> disfavoured in this model — it is unavailable. The lowest available universal
> long-range channel is spin-2.

Same fact as the classic test: Nordström scalar gravity predicts *zero* light
deflection precisely because radiation's stress tensor is traceless; measured
is 1.75″. **The light-bending falsifier of `0002` is passed in the only sense
available** — the model cannot produce the Nordström answer. Getting the
coefficient right needs dynamics it does not have; this is not a derivation
of 1.75″.

Read the table carefully: some *spin-2* entries also vanish, which is
orientation-dependence (what having a tensor means), not gravity switching off.
The static limit `T⁰⁰T′⁰⁰` is nonzero in every row, so universal attraction
survives while sub-leading structure is orientation-sensitive — the expected
shape of spin–spin coupling.

**Mass is the trace.** Free null ray → traceless → massless. For any stationary
bound system the tensor virial theorem gives `∫T^{ij} = 0`, hence
`∫T^μ_μ = ∫T⁰⁰ = Mc²`. So "mass is trapped momentum" = **mass is the trace that
trapping generates**, which finally says what the confining agent is *for*.

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

## On α (`exploration/0006`)

Asked directly. **The decisive fact is experimental: α runs.** `α⁻¹ = 137.036`
at `q² = 0` but `≈ 127.95` at `M_Z`. Any "derivation of 137" targets the
zero-momentum limit of a scale-dependent coupling — a dynamical quantity this
framework has no machinery for. Cautionary case: Eddington argued 136, then
revised to 137 when measurement improved; the revision is what the episode is
remembered for.

**In reach: charge quantization**, by the mechanism already owned from `0004` —
compactness → closed orbit → discrete winding number. If charge is a winding
number on a compact direction, integer charge is automatic, by the same
argument that gave quantized spin. Same shape as Dirac's monopole argument and
KK charge quantization, so the framework would be rediscovering a known
mechanism — a success condition under the standing method.

**Not in reach: the value.** In KK the coupling ties to the radius,
`α ~ (l_P/R)²` → `R ≈ 11.7 l_P` (order of magnitude; coefficient is
convention-dependent). Geometry *relocates* "why 137" into "why `R ≈ 12 l_P`".
Honest progress of a kind, not an answer.

Recommendation: **pursue charge quantization, not the value of α.**

## Status: what this is, and what it is not (`0009`, `0010`)

**Prior art — the honest verdict.** Essentially every piece of mathematical
structure here is standard and specifically mapped. The trichotomy is Möbius
conjugacy; the complex determinant is the Riemann–Silberstein vector; helicity
from `k^⊥` degeneracy is Wigner (1939); the spinor square root of a null vector
is Penrose's flagpole; and the organising claim — *particle taxonomy = orbit
classification of the symmetry group, mass and spin as orbit invariants,
quantisation from the orbit's geometry* — is **Souriau's coadjoint-orbit
programme (1970)**, stated first and carried much further. What is not in the
literature is the *route* here, which is a pedagogical path, not a result.
(Souriau and Penrose–Rindler verified by search; Riemann–Silberstein, Petrov,
and Wigner asserted from knowledge, search quota exhausted — confirm before
relying on them.)

**Where it stands.** Weaker than "describes": there is no dynamics, no action,
no field equations. It is a **kinematic taxonomy**. And absorbing many rounds of
correction gracefully is partly a warning sign — a framework flexible enough to
accommodate everything predicts nothing.

**The first real test (`0010`), and its result.** Thomas precession, with
predictions recorded *before* computing. Three confirmed: the Wigner angle
formula, `Δ = 2π(γ−1)` per orbit, and the slow limit `πβ²`. Plus a clean
cross-check — rapidity space has curvature `−1`, so the holonomy is the
enclosed hyperbolic area `2π(cosh η − 1) = 2π(γ−1)`. **Thomas precession is the
curvature of velocity space.**

**The fourth prediction was falsified**, and that is the finding: a product of
two boosts is **hyperbolic**, not loxodromic (`tr A = 2[c₁c₂ + s₁s₂cos θ]`,
manifestly real). The Wigner rotation lives in the **polar** decomposition, not
the **conjugacy class** — and `0008` classified by the latter.

> **The workstream has two separable assets, and only one passed.**
> The **representation** (`SL(2,ℂ)`, Pauli algebra, spinors, bivectors) earns
> its keep — the rotation is one visible term where the standard route is a page
> of tensor algebra. The **classification** (`0008`'s four classes) was the wrong
> instrument here and remains untested.
>
> This matters because the "saves students a pile of equations" hope rests
> entirely on the first, which is decades-old Penrose–Rindler material — while
> everything novel-sounding in `0004`–`0008` sits in the second.

**Standing practice adopted:** no result claimed for the framework without a
prediction recorded before the computation. Prediction 4 is exactly the kind
that retrofitting would have hidden.

## The starting point found, and the factor-2 CLOSED (`0011`, `output/0010`)

Reframing adopted: the workstream **found its starting point**. From Einstein's
"what if a photon were the clock" we arrived by our own route at **Souriau's
coadjoint-orbit structure for particles** — the route validated the
destination. Plan: absorb Souriau rather than rederive (his *orbit*
classification is the right instrument where our *conjugacy* taxonomy failed
`0010`'s test — orbits are phase spaces, so dynamics can live on them), then
build back to SR and GR with the tail-chasing photon as the constructive guide.

**The factor-2 question is closed** (`output/0010`, 29/29, 4/4 pre-registered
predictions confirmed). The spin sphere has symplectic area `4πs`; a quantum
phase over it needs two patches; single-valuedness of the transition function
forces `e^{4πis} = 1`, i.e. **`2s ∈ ℤ`**. Verified three ways: patch mismatch
`= 4πs`, Chern number `= 2s` (integer), and `R(2π) = (−1)^{2s}` uniformly on
each SU(2) multiplet. `0005` showed half-integers *permitted*; this shows
everything else **forbidden** — `s = 0, ½, 1, …` is exhaustive, and the factor
2 is `area(S²)/period(S¹) = 4π/2π`. The "do dynamics select the antiperiodic
sector?" question dissolves: it was never dynamical. `0004`'s rule in final
form: **quantization is the integrality of curvature over a compact surface.**

**Souriau sourcing (updated).** The text is unreachable from this environment
— `books.google.com`/`www.google.com` return a gateway **403 to CONNECT under
organization egress policy**, arXiv and Springer are blocked, and
`googleapis.com` passes but the Books API has 0/day quota. WebSearch works, and
verified most of the claims: the coadjoint-orbit treatment with invariants
`(m,s)` **[V]**; massless orbits non-generic and **smaller-dimensional** than
massive **[V]** (the specific 8 and 6 are *not* confirmed); **BMT equations**
from linearizing a presymplectic refinement of Souriau's structure **[V]**;
spinning particles in **curved backgrounds** **[V]**; and a **9-dimensional
evolution space** for his massless spinning model **[V, new]** (evolution space
≠ orbit, so it neither confirms nor contradicts the "6"). Still **[K]**:
massless non-localizability — do not build on it. The integrality result is
independent of the text (`output/0010`, 29/29).

**The road back** (Souriau content flagged per the sourcing note above): Stage 1, SR — done in reverse by `0001`–`0003`; the
tail-chasing move *constructs massive orbits from the massless one*. Stage 2,
external gravity — pre-registered test: does the loop-averaged tidal force on
the circulating photon reproduce the Mathisson–Papapetrou spin-curvature term?
Stage 3, GR — the honest wall; needs interaction, where symplectic
no-interaction theorems lurk (their hypotheses assume worldline canonical
variables; whether the tail-chasing reading escapes them must be *shown*).
Problems to eye in Souriau: unpopulated orbits (continuous spin — if the
null-ray construction *cannot* build them, that is an explanatory win),
massless non-localizability vs our concrete null plane, and interaction.

## Method note

Standing rule adopted for this workstream: **name the assumption, cite the
measurement.** A theorem is a map of where the load-bearing assumptions sit,
not a wall. It earned its keep immediately — the Poincaré-Casimir argument
*looked* like an obstruction and was not one (the framework routes around it by
using different plane types, and Wigner's classification assumes particles are
irreps of exactly the Poincaré group, which a modified symmetry structure need
not grant). What actually did the work was measurement: the Higgs and π⁰ spins,
and the absence of a lepton mass ladder, which is what settled KK-vs-timelike
in `0004`.

**Correction to an earlier caution** (`0011`): "absorbing corrections
gracefully is partly a warning sign" mis-aimed. Every absorption in this
workstream *removed* a difference in kind (photon-as-third-structure → one
algebra element; mass+spin as two objects → one non-simple bivector); none
added structure. That is the Maxwell pattern — unification of apparent kinds —
and it is to be aspired to. The caution that survives: flexibility is a warning
sign only when absorption *adds* structure (epicycles). Track the direction of
absorption, not the count. Pre-registration stays regardless.

## Known gaps

- **The factor of 2 — largely resolved** (`0005`), by the model's own premise.
  A null vector is a **spinor squared** (`k^μσ_μ` is rank 1, so `K = ξξ†`), and
  the square root is two-valued: rotating 360° about a null direction leaves
  the vector fixed and sends the spinor to **minus itself**. So the object on
  the loop is a spinor, antiperiodic boundary conditions are admissible, and
  the lowest mode is `½` → **`L = ħ/2`**. Nothing added. Supersedes `0003`'s
  beat and `0004`'s group-winding fork.
  **Residual:** this shows half-integers are *permitted*; that the dynamics
  *select* the antiperiodic sector is not shown. Much smaller problem than the
  original.
- **What fixes `a`** (the winding plane's tilt) — the whole predictive content
  of the mass sector now sits here. If `a` is set by the particle's relation to
  the rest of the web, generations might be different `a` at the same `n`.
- **Charge quantization as a winding number** — the one α-adjacent target with
  a real chance. Needs a compact direction the framework can *motivate* rather
  than assume.
- **Does the classification forbid anything?** (`0010`) The taxonomy makes
  existence claims, so test it on existence questions. Sharpest target: Wigner's
  classification permits continuous-spin representations that are not observed.
  If the loxodromic/nilpotent structure says why, that is a real result; if it
  says nothing, the taxonomy is decorative.
- **Composition closure** — follows from `0010`'s failure. Products of boosts
  stay hyperbolic. What physically meaningful process *generates* loxodromic
  elements? Deprioritised by `0011`: Souriau's *orbit* classification is the
  right instrument where conjugacy failed, so answer this inside the orbit
  picture after reading him.
- **Read Souriau** — now the gating item (`0011`); every [K] claim there needs
  verification against the text. Blocked on network access this session.
- **Stage 2 — DONE, CLEAN** (`0012`, `output/0011`, 20/20, 5/5 predictions).
  The loop-averaged force on the confined photon ring equals
  `−½R^i_{0jk}S^{jk}` with the coefficient **−1/2 exact** (machine precision by
  both quadrupole subtraction and Richardson), in a generic random stationary
  metric. The hoop tension (`τ = E/2πr`, the null-string condition) is
  load-bearing: photon alone mis-weighs by its pressure term; with tension the
  system weighs exactly `E` and combined `T^{jk} ≡ 0` pointwise, so the spin
  force is purely the energy-flux (gravitomagnetic) coupling. Universality
  confirmed: a 100× heavier, 100× slower flywheel with equal `S` feels the
  identical dipole force — gravity reads only `(E,S)` at this order, so the
  guide is *consistent and necessarily silent* here. Two pre-registered
  sub-claims were falsified en route by the same object — the ring's **mass
  quadrupole** `Q = Er²/2` — which is thereby promoted to the distinguishing
  observable: at fixed `(E,S)` the light ring has the *minimum* quadrupole
  `S²/2E` and sits at `r = S/E`, which is exactly Kerr's `a = J/M`.
- **Stage 2b — DONE; the registered hope FAILED at factor 1/2, productively**
  (`0013`, `output/0012`, 21/21). `M₂_ring = −Ma²/2` vs Kerr's `−Ma²`, both
  verified two ways from scratch (the Appell form reproduces
  `M_l = M·Re[(ia)^l]` through `l = 4`). SSC doesn't bite: the static
  symmetric source has an unambiguous centroid, so the 1/2 is physics. The
  gap is carried by the **confinement stresses**: with
  `ρ_eff = T⁰⁰ + T^kk`, the virial protects `M₀ = E` but the stress second
  moment `Y = ∫T^kk ρ²` is architecture-dependent, `M₂ = −½(Ea² + Y)`, and
  **Kerr ⟺ the confinement's own stress second moment vanishes**. Computed
  ladder: hoop 1/2, membrane 3/4, spokes 5/6 of Kerr (`1 − 1/2n`, noted not
  explained); pre-stressed structures can reach 1. Extracted constraint: if
  minimal coupling = Kerr multipoles [K, unverified], the electron sits AT
  Kerr, so **whatever confines the zitter motion must carry zero stress
  second moment** — GR returning information about the model's oldest gap.
  Exact Kerr (all moments) needs the **Israel disk**, re-derived here from
  the Appell branch cut: `σ = −Ma/2π(a²−ρ²)^{3/2}`, negative interior sheet
  plus positive rim, moments summing to `M` and `−Ma²` distributionally.
- **Stage 3 first piece — DONE** (`0014`, `output/0013`, 11/11). The
  registered "exterior must be Kerr" justification was **withdrawn before
  computing** (no Birkhoff for rotation; neutron stars have `q ≈ 2–10` [K]),
  and replaced by the correct mechanism: material tension is the *only*
  negative-second-moment agent, so with gravity supplying fraction `f` of the
  confinement, `Y(f) = f·Ea²` and `M₂` marches **linearly from half-Kerr to
  exactly Kerr at `f = 1`**. Confirmed at leading order; the `f → 1` endpoint
  has uncontrolled second-order corrections (`GE/a ≈ 0.59` there).
  Two findings en route: **the null ring's gravitational self-interaction is
  finite in the thin limit with no cutoff** — parallel null neighbours do not
  interact (TEP), while the static massive ring diverges as `ln(1/δ)`;
  *nullness regularizes*, a structural virtue of the trapped-light premise.
  And the hand-derived self-force `f_in = (32/3)Gσ²/a` (verified by an
  independent component-wise route to 8 digits) puts the **linearized geon at
  `a* = (16/3π)GE ≈ 1.70 GE`** — the extremal-Kerr scale times an order-unity
  factor. One registered sub-prediction falsified: the sector slope ratio is
  `1 : +2 : −3` (measured), not `1 : −2 : 1` (guessed from the energy
  contraction); the force's momentum-flux term redistributes the sectors, and
  the log-cancellation itself stands.
  **The electron is not a geon**: gravity supplies `~10⁻⁴⁴` of its
  confinement (`a/GE = (m_P/m_e)²/2 ≈ 3×10⁴⁴`, super-extremal, no horizon).
  The `0013` zero-stress-moment constraint must be met by non-gravitational
  structure. Running theme now explicit: every GR probe converts "what
  confines the ray" from a philosophical gap into a quantitative constraint —
  load-bearing (weight), zero stress second moment (Kerr `M₂`),
  non-gravitational (electron scale), finite self-energy (null limit).
- **The confinement bound — THEOREM** (`0015`, `output/0014`, 17/17, 5/5
  predictions). Reducing the stress second moment to the **transmitted radial
  force** `u(ρ) = 2πρS^{ρρ}` collapses everything to one quadrature,
  `Y_tot = −2∫₀^a uρ²dρ` (verified against all three architectures to 1e-8 —
  the `0013` ladder was three choices of one function). Then: all stresses in
  tension ⟹ `u ≤ 0`, `u' ≤ 0`, `|u(a)| ≤ E/a` ⟹

  > `0 ≤ Y_tot ≤ 2Ea²/3`, i.e. **M₂ fraction ∈ [1/2, 5/6]. No all-tension
  > material confinement reaches Kerr — it is outside the reachable set.**

  Bound **tight at both ends** via `u = −(E/a)(ρ/a)^n`, closed form
  `(1 + 2/(n+3))/2`: `n = 0` → 5/6 (spokes), `n → ∞` → 1/2 (hoop). Reaching
  Kerr needs peak `|u| = 1.5 E/a` — 50% more internal tension than the load
  transmitted — closable only by **hoop compression**: a pre-stressed
  tensegrity, not a web. DEC then bounds its energy below by `~πE` at radius
  `a`, so **the confinement is comparable to or heavier than the ring**
  (lower bound only; the self-consistency where confinement energy shifts
  `a = S/E` is unsolved). This dissolves the apparent `0013`/`0014` tension:
  the ladder's 5/6 is a hard ceiling for *matter*, and self-gravity reaches 1
  precisely because it removes matter stress rather than rearranging it.

  > **Kerr's quadrupole is a signature of non-material confinement.**

  ~~Chain for the electron...~~ **RETRACTED — see below.**
- **Link 1 verified, and it breaks the electron chain** (`0016`,
  `output/0015`, 9/9, 5/5 predictions). Minimal coupling *does* generate
  Kerr's complete multipole series (Arkani-Hamed–Huang–O'Connell
  arXiv:1906.10100; Guevara–Ochirov–Vines PRD **100**, 104024;
  Chung–Huang–Kim–Lee) — **but in the infinite-spin limit.** A spin-`s` state
  carries multipoles only to rank `2s`, and the spin-induced quadrupole
  operator `S_iS_j + S_jS_i − (2/3)δ_ijS²` **vanishes identically as a
  matrix** for `s = ½` (verified; nonzero for `s ≥ 1`).

  > **The electron has no quadrupole moment at all.**

  So `0015`'s inference ("the electron sits at Kerr's quadrupole, hence its
  confinement is neither tension nor gravity") is **void and withdrawn** —
  annotated at the source. The `0015` **theorem is untouched**; it never
  needed the electron. Surviving: `g = 2` at dipole order (rank 1 ≤ 2s), the
  Carter match from `0001`. **Correction to `0001`/`0013`: the Kerr–electron
  coincidence is weaker evidence than those notes treated it as** — Kerr and
  the electron agree exactly where the electron *has* moments and vacuously
  beyond, because spin-½ truncates the series.
- **Confinement as geometry — the positive mechanism** (`0016`). Covariantly,
  a photon on a **closed null geodesic is unforced**: what reads as a
  confining force in flat coordinates is the connection. (Boundary: *not* a
  boost effect — `∂_μT^{μν} = 0` is covariant, so the content is curvature,
  not velocity.) Such a confinement carries **no matter stress**, so
  `Y_conf = 0` ⟹ `M₂ = −Ea²` = **exactly Kerr, with no free parameter**,
  where every material architecture needs one. This is the positive
  realisation of `0015`'s negative result.
- ~~**Self-consistency picks extremality** (`0016`)~~ — **FALSIFIED by the
  invariant redo** (`0017`, `output/0016`, 22/22, 5/5 predictions). The
  degeneracy was worse than a caveat: at extremality the horizon and prograde
  photon orbit share both BL `r = M` *and* circumferential radius `2M`, with
  only proper distance (logarithmically divergent) separating them. Stated
  invariantly, the coordinate-independent size of a photon orbit is its
  **impact parameter** `b = L/E`; since each photon carries `L/E = b` and
  `a = J/M = b`, the condition is `a = b` — but
  `b_ph − a = r^{3/2}/√M > 0` for every `r > 0`, so **no fixed point exists.**
  (Orbit equations `u³ − 3Mu ± 2a√M = 0`, `b = a ± r^{3/2}/√M`, verified
  against `3√3M`, `2M`, `−7M` plus an independent closed form.) It fails a
  second way too: a ring on the extremal orbit generates `a = 2M`
  (super-extremal), where **no circular photon orbit exists at all**. And
  binding energy (`M < ΣE` ⟹ `a = kb > b`) makes the gap *wider*, so the
  result doesn't hinge on test-particle mass bookkeeping.
  **With it goes `0016`'s claim to have answered `0014`'s strong-field
  endpoint — that is open again.** What survives untouched: the
  geodesic-confinement mechanism itself (`Y_conf = 0` ⟹ `M₂ = −Ea²`); only the
  claim that a *self-generated* Kerr geometry supplies such an orbit to its
  own source is dead.
  **Remaining gap, honest:** the analysis treats each photon as a test
  particle in the *total* field, double-counting its own contribution. A ring
  element should move in the field of the *others*, and `0014` showed that
  self-field is finite for null rings — so the correction is well-defined,
  bounded, and O(1) here. **Self-confinement is unresolved, not refuted.**
- **Bridge to `foundations/`** (`0016`): the repo posits mutual **consistency**,
  not force, as fundamental — and a consistency constraint carries no
  stress-energy, evading the `0015` bound for the same reason geometry does.
  "What confines the ray?" may be a category error like "what force keeps a
  free particle moving straight?". Testable content: constraint-confinement
  predicts `Y_conf = 0` identically, hence `M₂` with **no free parameter**.
- **Unpopulated orbits**: if the tail-chasing construction *cannot* build
  continuous-spin orbits, the constructive principle selects exactly the
  observed particle types — a genuine explanatory win. Pre-register first.
- **Values need representations.** `0008` settles the kinematic *structure* —
  which objects exist and how they relate — but claims no number: not the spin
  magnitude, not `±1` helicity, not a mass. Getting values needs the rep and
  the dynamics, neither of which exists yet. This is where `0005`'s spinor
  square root should reconnect, since `sl(2,ℂ)` is where both live.
- **What fixes `ζ`?** The mass sector's whole predictive content is now the
  value of **one complex number per particle**. Generations would be different
  `ζ` — and since `ζ` is complex there are *two* real numbers per particle to
  explain, not one.
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
