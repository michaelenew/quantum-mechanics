# 0001 — Mass as trapped momentum: the circulating null ray

The proposal: a particle is a massless excitation that closes on itself. "A
photon chasing its own tail." Net translation `< c`; relativistic kinematics
and the mass/momentum unification are supposed to fall out of the constancy of
`c` alone.

Verdict up front: **more of this drops out exactly than the user claimed, one
thing they claimed is backwards in a way that helps, and there is one sharp
defect that no amount of reframing removes.** There is also substantial prior
art, which they asked about, and it is closer to their picture than they
probably expect.

All numerical claims below are checked in `output/0001_circulating_null_ray.py`
(39/39, pure stdlib).

## What drops out exactly

### Spin, with no free parameter

Put the null ray on a loop of radius `r = ħ/(2mc)` — half the reduced Compton
wavelength. Then

```
L = m c r = m c · ħ/(2mc) = ħ/2      — the mass cancels identically
```

The circulation frequency is `ω = c/r = 2mc²/ħ`, which is **exactly the Dirac
zitterbewegung frequency**. So the model does not fit spin, it forces it: one
geometric input (a null loop at the Compton scale) and `ħ/2` comes out for
every massive fermion. This is the strongest structural point in the proposal
and it is worth leading with.

### Both de Broglie relations, exactly, at every speed

This is the result that most deserves attention, and it is stronger than what
was claimed. Postulate only an internal clock at the Compton frequency
`ω₀ = mc²/ħ` — which is what a closed null loop *is*. Lorentz-transform its
phase:

```
φ = ω₀τ = ω₀·γ(t − vx/c²) = (γω₀)·t − (γω₀v/c²)·x  ≡  ω t − k x

  ω = γω₀ = γmc²/ħ = E/ħ          p = ħk  ⟸  k = γω₀v/c² = γmv/ħ
```

**`E = ħω` and `p = ħk` are theorems**, not postulates, once there is an
internal clock at the Compton frequency. Verified to machine precision from
`v/c = 10⁻³` to `0.999`.

Two things this buys immediately:

- The de Broglie *phase* velocity `ω/k = c²/v > c` stops being disturbing. It
  is relativity of simultaneity applied to a clock that is synchronous in its
  own rest frame. Nothing moves superluminally; the loop's phase merely
  desynchronises along the boost direction. This is a much better account of
  the superluminal phase velocity than "it carries no information."
- The wave–particle duality is not a duality. The "wave" is the loop's own
  phase seen from a frame in which the loop is not at rest.

Historical placement: this is **de Broglie's own 1924 "harmony of phases"
argument**, and the circulating-null-ray model is essentially his internal
clock made geometric. The user reinvented it, which is a good sign.

### Time dilation, from one line of trigonometry

Boost along the spin axis (the clean case — transverse dimensions do not
contract, so the circle stays a circle and the null ray traces a helix of
unchanged radius). The pitch angle satisfies

```
sin θ = v/c        tangential speed = c cos θ = c/γ        ω = ω₀/γ
```

Exactly the user's description — "accelerating looks like the angle relative to
the path decreasing, stationary is orthogonal" — now with the precise relation
`sin θ = v/c`. Time dilation is the statement that a fixed total speed `c` gets
split between circulating and translating. That is the light-clock argument
with the mirrors replaced by a loop, and it is legitimate.

Caveat worth keeping: this is clean **only for boosts along the spin axis**.
Boost perpendicular to the spin and the circle contracts to an ellipse and you
are in Thomas-precession territory. Not fatal, but the model's simplicity is
axis-dependent, which bears on the "which axis" question below.

### A three-length identity that was not expected

`pitch ∝ v` while `λ_dB ∝ 1/v`, and their product is `v`-independent:

```
pitch × λ_dB = (2πc/ω₀)² = (h/mc)²        ⟹    √(pitch · λ_dB) = λ_Compton
```

The Compton wavelength is the **geometric mean** of the helix pitch and the de
Broglie wavelength, at every speed. They cross — both equal to `λ_C` — exactly
at `v = c/√2`, which is where `p = mc`.

This also flags a trap: **the de Broglie wavelength is not the helix pitch.**
They scale oppositely. `λ_dB` belongs to the phase wave, not the visible
winding. Anyone developing this picture will try to identify them; they must
not.

## The correction: spin is boost-invariant, not reduced

The claim was that accelerating *reduces* the trapped angular momentum, since
the procession rate falls. Half right — the rate does fall by `γ` — but the
inertia rises by `γ` at the same time:

```
L = (γm) · (c/γ) · r = m c r          — the gammas cancel identically
```

Verified invariant to `v = 0.999c`. This is a **repair, not a problem**: spin
magnitude is a Poincaré Casimir invariant, so a model in which boosting changed
it would be simply wrong. The model gets this right automatically, which is
another point in its favour. The intuition to keep is that boosting trades
circulation for translation at fixed total `c`, and angular momentum is exactly
the combination that is blind to the trade.

## The sharp defect: a factor of 2 you cannot remove

| loop radius | spin `L/ħ` | energy `ħω/mc²` |
|---|---|---|
| `ħ/(2mc)` (half Compton) | **0.5** ✓ | 2.0 ✗ |
| `ħ/(mc)` (Compton) | 1.0 ✗ | **1.0** ✓ |

**You may have the right spin or the right energy, not both.** Fix the radius
to get `ħ/2` and the circulating quantum carries `2mc²`; fix it to get `mc²` and
the model predicts spin 1.

This should not be papered over — it is the first thing a serious critic will
find. Two honest observations, neither a resolution:

- The factor 2 is exactly where the **spinor double cover** lives: a spin-½
  state needs 720° to return to itself, and the zitterbewegung frequency is
  twice the Compton frequency for the same reason. Suggestive. Nothing here
  derives it.
- Standard Dirac theory has the same factor and does not regard it as a
  defect, because zitterbewegung is interference between positive- and
  negative-energy components — a *two*-component beat, not a single circulating
  object. That is arguably the real content of the 2, and it is a hint that
  the correct version of this model has two counter-circulating pieces rather
  than one.

Closing this is the single highest-value open problem in the idea.

## Prior art — the user asked, and there is a lot

Ordered by closeness to the proposal.

1. **Zitterbewegung (Schrödinger 1930).** Not an analogy — the Dirac velocity
   operator `cα` has eigenvalues `±c` **only**. In standard Dirac theory a free
   electron always moves at `c` instantaneously; the sub-luminal observed
   velocity is the time-average of a `c`-speed jitter at frequency `2mc²/ħ`
   with amplitude `ħ/(2mc)`. The user's core premise is textbook relativistic
   QM, not a departure from it. This is the most important single fact to know.
2. **Hestenes' zitterbewegung interpretation** (Found. Phys. **20**, 1213
   (1990); see also arXiv:1910.11085). Explicitly models the electron as a
   point charge in *lightlike circular motion* at the Compton frequency, radius
   one half the Compton radius, in a plane orthogonal to the spin — and derives
   Dirac structure in geometric algebra, with spin as the orbital angular
   momentum of that motion. This is the user's idea, developed, by a serious
   person, for thirty years.
3. **de Broglie's internal clock (1924).** The `ω₀ = mc²/ħ` clock, from which
   Part 3 above follows. Has even been probed experimentally: Catillon et al.,
   *Found. Phys.* **38**, 659 (2008), report a channeling-transmission
   resonance in ~80 MeV electrons through thin silicon at the Compton
   frequency. Contested, not replicated to consensus — cite as an attempt, not
   as evidence.
4. **Kerr–Newman electron models (Carter 1968; Burinskii).** Take the
   Kerr–Newman solution with the electron's mass, charge, and angular momentum.
   Carter's result: the gyromagnetic ratio comes out **exactly `g = 2`**, the
   Dirac value, with no fitting. The ring singularity sits at `a = J/mc =
   ħ/(2mc)` — the same half-Compton radius as the zitterbewegung loop. A
   "ring of light at the Compton scale" reproducing `g = 2` is a strong
   independent hit on the same geometry, from general relativity rather than
   from quantum theory.
5. **Wheeler's geons (1955).** Literally self-gravitating bundles of
   electromagnetic radiation held together by their own gravity — "light
   chasing its tail" in the gravitational case. Wheeler's own conclusion is the
   relevant one: they exist only at absurd masses and are unstable. This is the
   honest answer to "can radiation self-trap?" in GR.
6. **Confinement mass in QCD.** See below; the empirical core.

Not prior art but adjacent and worth knowing: preon models, Bohmian internal
clocks, and the "photon in a box" pedagogy that shows confined radiation has
inertial mass `E/c²`.

## "Mass is trapped momentum" is already true, for most of the mass there is

The strongest empirical support is not speculative at all:

```
proton                       938.272 MeV/c²
sum of current quark masses    8.990 MeV/c²   (uud)
from the Higgs mechanism        0.958 %
from confined energy-momentum  99.042 %
```

**~99% of the mass of ordinary matter is already trapped momentum** — kinetic
and binding energy of near-massless quarks and strictly massless gluons,
confined. The reframing is not a new hypothesis for hadrons; it is the Standard
Model's own accounting. What the proposal adds is the suggestion that the
*remaining* ~1% (the Higgs-generated current-quark and lepton masses) works the
same way. That is the actual novel claim and it should be stated that narrowly.

The equivalence-principle point holds too, and cleanly: confined
energy-momentum sources gravity as `E/c²` in GR, so inertial and gravitational
mass agree for trapped momentum **as a theorem rather than an assumption**.
That is the user's third consequence and it survives.

One caveat with teeth. Trapped radiation has pressure `p = ρc²/3`, and active
gravitational mass in GR goes as `(ρ + 3p/c²)`. For a *box* of light the
container's tension cancels the pressure contribution and the total comes out
`E/c²` — but only because there is a container. **The model owes an account of
what does the trapping.** A bare circulating null ray with nothing confining it
is not a solution of anything. This is the second major open problem, and it is
where the QCD analogy is most instructive: in hadrons the confining agent is
the gluon field's own nonlinearity.

## The three loose ends, addressed

**Is there a Maxwell solution?** No, and for a structural reason worth stating:
**Maxwell is linear, so it has no self-interaction and therefore no
self-trapping.** No amount of cleverness produces a localized non-dispersing
vacuum soliton. But two things soften this:

- **Rañada's knotted electromagnetic fields** (1989) are *exact* source-free
  Maxwell solutions built on the Hopf fibration, in which every pair of
  electric field lines (and every pair of magnetic ones) is linked, carrying a
  topologically conserved helicity. This is "light chasing its own tail"
  realised topologically in genuine vacuum Maxwell theory. They disperse — the
  theory is still linear — but they exist, and they show the *topology* the
  user wants is not forbidden. A genuine surprise hit.
- The required nonlinearity is supplied by the theories that actually apply at
  this scale: QED's effective photon–photon coupling (Euler–Heisenberg), and
  gravity (Wheeler's geons). So "not in Maxwell, plausibly in the effective
  nonlinear completion" is the correct summary, with the caveat that neither
  known nonlinearity is anywhere near strong enough at the electron scale.

**The "infinitely contracted" note.** Phrase this carefully — there is no valid
rest frame for a lightlike trajectory, so "the photon is close to every point
of its orbit" is not a legitimate frame statement. The *legitimate* version is
stronger and cleaner: **a closed null curve has zero proper length.** `∮ds = 0`
along the loop. The entire particle is one null-separated structure — every
point of the loop is at zero interval from every other. If one wants a
mechanism by which a "particle" is not a point but is nevertheless not spread
out in any causally meaningful way, that is it.

This connects directly to `foundations/0006`. That note assigns correlational
structure to *spacelike* separation. Here is a *null* structure with the same
flavour: zero interval, no propagation, no speed applicable. Whether the
framework's two-tier split should be a three-way split (timelike dynamics /
null internal structure / spacelike correlation) is a real question this raises
for the main line of work.

**Which axis?** Both guesses have real content.

- Guess (a), "superposition over axes, aggregate behaviour is the
  amortization": this is essentially right and it already has a name — spin
  coherent states, and the plain fact that a spin-½ system has no definite axis
  until measured. The rotation plane is not a hidden variable to be averaged
  over; it is the observable, and its indefiniteness is the standard one.
- Guess (b), "rotation around the time axis", was offered as an odd hunch with
  no theory behind it. It has more support than expected. Every massive
  particle at rest carries the phase factor `e^{−imc²t/ħ}` — a rotation at
  exactly the Compton frequency, present regardless of spin orientation, and
  it is the *one* rotation every massive particle has. In geometric-algebra
  treatments of Dirac (Hestenes again) the zitterbewegung rotor's generating
  bivector contains the time direction, so "rotation in a plane containing
  time" is close to literal. The hunch is pointing at the rest-mass phase, and
  the rest-mass phase is exactly what Part 3 above turns into `E = ħω`.

The two guesses are not in competition: (b) is the universal circulation that
gives mass and the de Broglie relations, (a) is the spatial orientation of the
spin plane on top of it.

## Where this stands, and what to do next

Honest positioning. Nothing here is new physics; almost every piece is
recoverable from Dirac theory, de Broglie 1924, or Hestenes. What the framing
does have is real **pedagogical and structural** value: it derives spin, both de
Broglie relations, time dilation, and the mass/momentum unification from a
single geometric premise, and it makes the equivalence principle look
inevitable rather than coincidental. That is a lot of reach for one postulate,
and reach is what this repo is looking for.

Ranked next steps:

1. **Close the factor of 2, or characterise it as irreducible.** The
   two-counter-circulating-components reading (from the positive/negative-energy
   beat origin of zitterbewegung) is the most promising route. This is the
   crux; without it the model predicts the wrong spin or the wrong mass.
2. **Say what does the trapping.** Otherwise the pressure/active-gravitational-
   mass bookkeeping does not close and the model is not a model.
3. **Read Hestenes properly** (arXiv:1910.11085 and Found. Phys. 20, 1213)
   before developing further. If the idea has legs, that is where the legs
   already are, and duplicating thirty years of it would be waste.
4. **Follow the null-loop lead back into `foundations/`.** The zero-proper-
   length observation is the one place this workstream may have something to
   give the main line rather than take from it: it suggests the timelike /
   spacelike two-tier split wants a null middle term.
5. Charge and generation number are entirely unaddressed. Any loop model owes
   an account of why there are three generations at the same spin. No lead.
