# 0002 — Why `L` doesn't fall, and what that buys for differential relativity

> **AI-generated, not peer-reviewed.** Prior art credited in [`ATTRIBUTION.md`](../../ATTRIBUTION.md) — results are re-derivations of
> established work unless explicitly marked otherwise.

Follows `0001`. Two things here: a proper answer to the objection that the
trapped angular momentum ought to decrease under a boost, and the structural
programme ("differential relativity") that the objection was in service of.

The short version: the objection's individual steps are mostly right, the
conclusion is blocked, and *the reason it is blocked turns out to be the
"mass is trapped momentum" claim itself.* That is a better outcome than the
objection failing for a boring reason.

All numbers checked in `output/0002_why_L_is_invariant.py` (45/45).

## The objection

> The procession angle per wavelength must be the same after a boost, implying
> longer wavelength, implying both slower procession and lower linear momentum,
> implying less angular momentum.

Taken apart:

| step | status |
|---|---|
| procession angle per wavelength is boost-invariant | **right**, and it is the key to the answer |
| ⟹ longer wavelength | **sign backwards** for the total wavelength; *unchanged* for the component that matters |
| ⟹ slower procession | **right** — verified, `Ω → Ω/γ` |
| ⟹ lower linear momentum | **backwards** — `\|p\| → γ\|p\|` |
| ⟹ less angular momentum | **blocked** |

### 1. The boost adds longitudinal momentum; it removes no transverse momentum

Rest frame: the null ray circulates in the `xy`-plane with 4-momentum
`(E/c, p_x, p_y, 0)` and `|p_⊥| = E/c`. Boost along `z` (the spin axis). A
`z`-boost mixes only `t` and `z`, so

```
p_⊥' = p_⊥                    (untouched, exactly)
p_∥' = γ β E/c                (created from nothing)
|p'| = γ|p|                   (so the TOTAL wavelength shortens by γ)
```

`p_⊥` is flat across every speed checked. The ray's total energy rises to
`γE₀` — as it must, since that is the particle's total energy. So the total
wavelength gets *shorter*, not longer.

### 2. The quantization condition pins exactly the invariant wavelength

This is the real answer, and it vindicates the instinct behind the objection.

"`n` wavelengths fit around the loop" is an integer and cannot change
continuously under a boost — correct, and a good invariant to reach for. But
read what it constrains: `n·λ_⊥ = 2πr`. It fixes the **transverse** wavelength.
And `r` is a transverse length, which a `z`-boost also leaves alone.

Both sides of the quantization condition are boost-invariant. There is nothing
to reconcile — the condition is not *strained* by the boost, it is *untouched*
by it. Verified: `λ_⊥ = 2πr/n` holds at every speed to machine precision.

The objection assumed the wavelength being counted is the ray's whole
wavelength. It isn't; only the component around the loop is, and that is
precisely the one the boost cannot reach.

### 3. Procession really does slow — the moment of inertia rises to match

This step was simply correct and it deserves saying plainly: `Ω = Ω₀/γ`.

It still doesn't reduce `L`, because `L = IΩ` is not a fixed-`I` relation here.
Transverse inertia is `γm`, so `I = γmr²`:

```
L = (γ m r²)(c / γr) = m c r        — the γ's cancel identically
```

The objection reasons as though `I` were fixed, which is right for a rigid
body. A null ray is not a rigid body: its speed is pinned at `c`, so a boost
changes how that speed is **shared** between circulating and translating, not
how much transverse momentum exists. **Angular frequency and angular momentum
decouple.** That is the conceptual crux.

### 4. `J^{xy}` is the component a `z`-boost cannot act on

The cheapest proof, and it removes any suspicion of a lucky cancellation:
`J'^{μν} = Λ^μ_α Λ^ν_β J^{αβ}`, and for a `z`-boost `Λ^x_α = δ^x_α`,
`Λ^y_β = δ^y_β`. So `J^{xy}` passes through unchanged with nothing mixed in.
Confirmed numerically — `J'^{xy}` exact, all other generated components
identically zero.

The general statement is stronger still. Spin magnitude is the Pauli–Lubanski
Casimir `W·W = −m²s(s+1)ħ²`, invariant under the whole Poincaré group by
construction. **A model whose spin magnitude changed under a boost would not be
a relativistic model.** The null ray isn't getting lucky; it's obeying a
theorem. Any version of this idea that *did* reduce `L` under boost would be
falsified on the spot.

One place the underlying intuition does have purchase, worth keeping:
*orbital* angular momentum is genuinely frame-dependent, since `J^{μν}` mixes
rotations with boost generators under a general Lorentz transformation, and it
depends on the choice of origin. It is specifically the spin part — angular
momentum about the centre of mass, along the boost axis — that is rigid.
Boosts *perpendicular* to the spin are also a different story: the magnitude is
still fixed by the Casimir, but the direction undergoes Wigner rotation
(Thomas precession), and the local wavelength genuinely varies around the loop
— blueshifted on the approaching arc, redshifted on the receding one. That
perpendicular case is not computed here and is the honest place to look if one
wants the "longer wavelength" intuition to bite somewhere legitimate.

## The payoff: `E² = (mc²)² + (pc)²` is Pythagoras on the null ray

Chasing the objection produced something better than a rebuttal. Decompose the
ray's momentum into trapped (transverse) and translating (longitudinal) parts.
`|p|` is not fixed; `p_⊥` is:

```
m c  =  p_⊥            mass IS the trapped transverse momentum
p    =  p_∥            momentum IS the untrapped part
E²   =  (p_⊥ c)² + (p_∥ c)²   =   (m c²)² + (p c)²
```

Verified to machine precision through `v = 0.999c`. **The relativistic
dispersion relation is the hypotenuse.** Mass and momentum are not analogous
quantities in a shared framework — they are one quantity resolved along two
axes, and `E² = m²c⁴ + p²c²` is the statement that the resolution is
orthogonal.

This is the sharpest available form of the original "mass is trapped momentum"
claim, and it is an identity rather than an analogy.

It also closes the original question in one line. `L = r·p_⊥ = r·mc`. **If `L`
fell under a boost, the rest mass would fall under a boost.** "Angular momentum
is invariant" and "rest mass is invariant" are not two facts; they are one fact
about one quantity. The objection, pushed through, is an argument that rest
mass is frame-dependent — which is the one thing the framework cannot give up.

## A corollary that makes the factor-2 problem worse, not better

Run the quantization route on its own: `n·λ_⊥ = 2πr` with `p_⊥ = h/λ_⊥` gives

```
L = r · p_⊥ = r · nh/(2πr) = n ħ
```

`L = nħ` — the radius cancels, and the answer is an **integer** multiple of `ħ`
for any loop size. The wavelength-counting picture cannot produce `ħ/2` at all;
it lands on the spin-1 branch of `0001`'s table by construction.

So the "procession per wavelength" framing sharpens the factor-2 defect rather
than relieving it. That is useful: it says the problem is not a bad choice of
radius but something structural about treating the particle as **one** ray
winding an integer number of times. It strengthens the two-counter-circulating-
components reading flagged in `0001` — a half-integer wants a double cover, and
a single-valued winding number can't supply one.

## Differential relativity

The stated programme: spacetime is the global frame handling these relations,
curvature is implicit in the relationships between individual particles, and
mass appears twice — as resistance to motion (inertia) and as implied curvature
(gravity) — so the two have one explanation.

### What the null-ray picture actually delivers

**Inertia gets a mechanism, and a good one.** From the Pythagoras result: you
cannot convert `p_⊥` into `p_∥`. A boost only *adds* longitudinal momentum, in
quadrature. If the trapped component could be traded away, acceleration would
be free. So **inertia is the rigidity of the trapped component** — resistance
to motion is the refusal of `p_⊥` to be spent. That is a mechanical account of
inertia rather than a label on a coefficient in `F = ma`, and it is the
strongest thing this workstream has to offer the programme.

**Gravitational mass is the same object.** Confined energy-momentum enters
`T_μν` and sources curvature as `E/c²`. Same `p_⊥`.

So "two effects, one explanation" is delivered — but be precise about the level
at which it is delivered. It identifies the **quantity**; it does not derive
the **field equations**. GR already ties inertial and gravitational mass
together through `T_μν`; what the null-ray picture adds is a *reason the
quantity is the same one*, namely that it is literally the same momentum
resolved transversally rather than longitudinally. Real contribution to
intuition, not new dynamics. Claiming more would be overclaiming.

### Prior art, since the programme has a long history

- **Mach's principle** — inertia from relations to all other matter. The direct
  ancestor. Motivated Einstein; GR does **not** actually implement it (Minkowski
  and Schwarzschild have inertia with no matter around).
- **Barbour & Bertotti (1982), shape dynamics** — dynamics built from relative
  configurations only, no absolute space. The closest existing formalisation of
  "the global frame is just the relations," and the nearest neighbour to this
  repo's P1.
- **Sakharov, induced gravity (1967)** — the Einstein–Hilbert action is not
  fundamental but induced by quantum fluctuations of matter fields. Nearly a
  restatement of "curvature is implicit in the relationships between particles."
- **Jacobson (1995)**, *Thermodynamics of Spacetime: The Einstein Equation of
  State*, PRL **75**, 1260 — **the most important one to read.** Derives the
  full Einstein field equations by demanding the Clausius relation `δQ = T dS`
  hold on every local Rindler horizon, with `S ∝` horizon area and `T` the
  Unruh temperature. Einstein's equations come out as an *equation of state*
  rather than a fundamental law. This is an existence proof that the programme
  is achievable.
- **Van Raamsdonk (2010), Ryu–Takayanagi, ER=EPR** — geometry from entanglement.
  Already flagged as the open frontier in `foundations/0005`; the differential-
  relativity idea is that same conjecture approached from the particle side
  rather than the field side. Worth noting the convergence explicitly.
- **Verlinde (2011) entropic gravity**, **Padmanabhan's emergent gravity** —
  same family; Verlinde is the more contested.

### The obstruction to check first

Any construction of gravity from inter-particle relations must reproduce a
**massless spin-2** interaction, and this is where such programmes usually die.

- Weinberg's soft-graviton theorem derives the universality of gravitational
  coupling — the equivalence principle — from Lorentz invariance and S-matrix
  consistency in the soft limit, for a massless spin-2 mediator.
- Deser's bootstrap: a self-coupled massless spin-2 field iterates to full
  nonlinear GR. The tensor structure is not optional decoration.
- The cheapest empirical discriminator is **light bending**. Scalar gravity
  (Nordström) predicts **zero** deflection of light. GR predicts 1.75″ at the
  solar limb, and that is what is measured. A vector mediator makes like
  charges repel, so it is out immediately.

**Concrete first test for differential relativity: does the relational
construction bend light, and by the GR coefficient?** A naive "particles pull
on each other according to their trapped momentum" scheme is scalar and gives
zero. This is cheap to check and it is the fastest way to find out whether the
idea has a chance. Do this before building anything else on it.

### A speculative lead that may point the right way

Flagged as speculation, not result — but it is concrete enough to test.

A null-ray particle is not characterised by a scalar. Its state carries a
**circulation plane** (equivalently, a spin axis) alongside its momentum. So
the relational data between two such particles is not mass-to-mass but
**plane-to-plane**: the relative orientation of two 2-planes, which is
naturally a rank-2 symmetric object, not a scalar.

That is at least the right **index structure** for a spin-2 mediator, and it is
exactly what a scalar "mass attracts mass" relation cannot supply. If the
differential-relativity programme has a route past the spin-2 obstruction, this
seems the most likely place for it to live. Testing it means computing the
plane-to-plane relation for two null-ray particles and asking whether the
resulting interaction has the trace structure of a graviton exchange rather
than a scalar exchange.

### One empirical constraint to respect

If inertia is to *derive* from relations to other matter, then since the
galaxy's matter distribution is anisotropic, inertial mass could acquire a
tensor character and vary with direction. This was tested directly:
**Hughes–Drever** clock-comparison experiments (1959–60, and much tighter
since) bound the fractional anisotropy of inertial mass to `< 10⁻²⁰`
originally, and modern versions reach `~10⁻²⁸`.

Important nuance, in fairness to the programme: **Dicke (1961) showed the null
result does not refute Mach's principle** — it only requires the anisotropy to
be *universal across all particle species*, in which case it is locally
unobservable. So this is a design constraint, not a falsification: any
differential-relativity scheme must make its inertial anisotropy species-
independent. Worth knowing before building, because a scheme in which inertia
depends on a particle's own internal structure would likely violate it.

## Cross-link to the gravity workstream

Recorded because the two prompts were flagged as semi-related and they do in
fact meet. The gravitational which-branch experiment (other branch,
`gravitation/exploration/0001`) forces the conclusion that **the gravitational
field must be an edge in the web rather than a function of the state** — a
classical field sourced by `⟨T_μν⟩` is precisely the absolute frame-independent
object P1 denies.

That is the same commitment differential relativity starts from: curvature
carried by the relationships between particles, not by a global object over and
above them. The two lines of argument arrive at it independently — one from a
superposition-and-causality paradox, one from a reframing of what a particle
is. Worth noting as mutual support, with the caveat that agreeing on an
ontological commitment is a long way from either one producing dynamics.

## Next

1. **Light bending.** Cheapest possible falsifier of the relational
   construction. Do it first.
2. **Read Jacobson (1995).** It is the existence proof that Einstein's
   equations can be derived rather than postulated, and it will discipline what
   "curvature is implicit in the relations" has to mean.
3. **Test the plane-to-plane rank-2 lead** — the one place a route past the
   spin-2 obstruction might live.
4. Still blocking from `0001`: the factor of 2 (now sharpened), and what
   confines the ray.
