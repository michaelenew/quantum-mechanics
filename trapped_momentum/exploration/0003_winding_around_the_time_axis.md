# 0003 — The helix axis is timelike

Supersedes the framing (not the arithmetic) of `0002`'s Pythagoras section.

Two criticisms were raised: that the account leans on prior art at the expense
of the idea, and that the transverse/longitudinal decomposition sits at too
high a level because **time is orthogonal to every spatial direction**, so a
spatial orthogonality cannot be the fundamental one.

The second is correct and produces a better picture. The first is partly
correct and worth separating into its parts. Checks in
`output/0003_winding_around_the_time_axis.py` (31/31).

## The criticism of `0002` lands

`0002` split the ray's momentum into `p_⊥` (trapped) and `p_∥` (translating)
and called `E² = (mc²)² + (pc)²` Pythagoras on that split. The arithmetic is
right and the checks stand, but the framing has a defect that was not flagged:

**it required choosing a spin axis and boosting along it.** For a boost
perpendicular to the spin the loop contracts to an ellipse, the ray is
Doppler-modulated around the circuit, and no instantaneous "trapped vs
translating" split survives. The invariant `E² − (pc)² = (mc²)²` of course
still holds — it is `P·P` — but reading `p_⊥` as *the trapped part* is a
special-frame reading, not a covariant one.

So the spatial Pythagoras should be demoted: **keep it as intuition in an
adapted frame, not as the definition.** The covariant statement is below.

## The geometry: a null helix winding about the timelike worldline

Write the rest-frame worldline of the circulating ray:

```
x^μ(t) = ( ct,  r cos Ωt,  r sin Ωt,  0 ),        Ω = c/r
```

The centre of mass stays at the spatial origin for all `t`, so **its worldline
is the `ct`-axis** — and that is the axis the ray's helix winds around.

Verified: `ds² = 0` along the whole helix (null, to float noise), `|v| = c`
exactly, and the spacetime pitch angle is **exactly 45°** at every point,
which is the null condition seen as geometry — one unit of `ct` advanced per
unit of spatial arc.

**"Rotation around the time axis" is therefore not loose speech — it is
literally what the worldline does.** The helix axis is the timelike CoM
worldline, and it is frame-covariant. The spatial circulation plane is only its
3D shadow. That is why picking a spatial axis felt arbitrary in `0001`: *it is
arbitrary*. The invariant object is the winding about the worldline, and the
choice of spatial plane is a frame-dependent projection of it.

This is a straight upgrade to the earlier answer on the "which axis" question.
The prior note said guess (b) pointed at the rest-mass phase; that was right
but understated. The right statement is geometric and exact.

## Inertia, stated without any spatial axis

Boosting the particle **tilts the helix axis** by the rapidity: `tan(tilt) = β`,
verified. The winding is unchanged; what moves is the axis. Resistance to that
tilt is inertia — which is the argument as originally put, and it holds.

The frame-independent statement of trapping:

> A boost can always remove the spatial momentum (go to the rest frame). It can
> **never** remove the rest energy. `mc²` is the irreducible timelike component
> of `P^μ` — the minimum of `E` over all frames.

Checked by scanning 3999 boosts: `min_v E = mc²` exactly, at `v = 0`.

That is inertia with no reference to a spatial direction, which is what the
criticism asked for. `0002`'s "`p_⊥` cannot be spent" is the same fact seen in
one adapted frame — true, narrower, and not the definition.

## The hard obstruction, stated plainly

Here the prior art is not fashion and cannot be set aside, so it is worth being
exact about *why* it binds.

The Poincaré group has exactly two Casimirs:

```
P·P = m²c²                    (mass)
W·W = −m² s(s+1) ħ²           (spin, Pauli–Lubanski)
```

They are **independent**. So mass cannot simply *be* an angular momentum — if
it were, the two would be locked together, and the group structure says they
are not.

The empirical form is blunter and does not depend on any formalism: **massive
spin-0 particles exist.** The Higgs (125 GeV, `s = 0`) and the π⁰ (135 MeV,
`s = 0`) are massive with no spin at all. A model in which mass *is* trapped
angular momentum predicts they cannot exist.

The repair is a distinction worth stating explicitly:

> **The trapped thing is energy–momentum, not angular momentum.** How that
> trapped energy–momentum *circulates* is a separate question, and its answer
> is the spin.

**Attribution correction (added after review).** The original proposal said
"mass is nothing but trapped momentum," and separately that the photon's linear
momentum *becomes effectively* angular momentum. It never claimed mass **is**
trapped angular momentum. That conflation was introduced in these notes, not by
the proposal, and the paragraph above originally implied otherwise. The
distinction is still worth having on the record — but as a clarification of the
notes, not a correction to the idea.

See `0004`: under the causal-type reading the objection dissolves entirely
rather than needing this repair, because mass and spin come from *different*
plane types.

## Counter-circulation resolves it — and it is the same repair as the factor 2

Two null rays on one loop, opposite senses, `E/2` each:

- angular momenta cancel exactly → **spin 0**
- energies add → **mass `E/c²`**

So massive spin-0 is naturally accommodated, by **the same structural fix
flagged in `0001` for the factor of 2** (that zitterbewegung is a beat between
two components, not one object going around). One repair addressing two
independent defects is a real signal and raises the priority of working it out.

A lead worth recording, flagged as speculation because the bookkeeping does not
yet close: in Dirac theory the zitterbewegung is interference between
positive- and negative-energy components, whose phases rotate *oppositely*,
`e^{∓imc²t/ħ}`. Two components each at the Compton frequency `mc²/ħ` beat at
`2mc²/ħ` — exactly the zitterbewegung frequency, and exactly the factor of 2.
That would make the 2 a beat frequency rather than a wrong radius, which is a
much more comfortable place for it to live. **Not shown**: whether the spin
then comes out `ħ/2` rather than cancelling to 0 as it does for spatially
counter-circulating rays. The counter-rotation must be in the phase (a
time-containing plane) while the spatial circulation stays co-rotating. That is
the thing to compute next.

## Kaluza–Klein: the prior art that supports the idea rather than constraining it

This should have been in the first pass and was not — a real miss, and the
closest prior art to the core claim, closer than zitterbewegung.

In Kaluza–Klein, a **massless** field with momentum quantised on a compact
dimension of radius `R` appears in four dimensions as a **massive** particle:

```
m = n ħ / (R c)              and hence      L = m c R = n ħ
```

That is "mass is trapped momentum" as a rigorous, standard derivation rather
than a picture. Three things it buys directly:

- **The "which axis" question dissolves** rather than being answered. There is
  no spatial axis to choose because the circulation is not in ordinary space.
- **The loop's invisibility is explained** rather than assumed — we do not see
  the winding because it is not a direction we can point along.
- It reproduces `L = nħ` exactly, matching `0002`'s integer-only result and
  inheriting the same factor-2 problem. Consistent, and it localises the defect
  to the *spin* side, not the mass side.

Note the tension worth keeping in view: KK says the circulation is in a
compact *spatial* extra dimension, while the argument here says the axis of the
winding is *timelike*. These are not the same claim. A compact timelike
direction is normally pathological (closed timelike curves), so if the timelike
reading is to be more than the observation that the helix winds about a
worldline, it needs an account of that. Open.

## On the prior-art criticism

Worth separating, because the two halves deserve different answers.

**Where it lands.** Kaluza–Klein should have been surfaced immediately and was
not; it is the strongest support the idea has and it went unmentioned while
weaker parallels were catalogued. And `0002`'s Pythagoras framing was left
unqualified when it is frame-adapted — that is a case of stopping at a
satisfying result instead of testing it in a general boost.

**Where it does not.** The Casimir independence and the existence of massive
spin-0 particles are not prior art in the sense of received opinion — one is a
group-theoretic theorem, the other is measured. They constrain the idea whether
or not anyone has written them down, and the useful response was the one taken
above: find the distinction that lets the idea survive them (energy–momentum
trapped, angular momentum separate) rather than route around them.

The general rule this suggests for the workstream: cite prior art when it
supplies a *mechanism* or a *bound*, not when it merely supplies a name.

## Next

1. **Compute the counter-rotating-phase model.** Two components,
   `e^{∓imc²t/ħ}`, co-rotating spatially. Does the spin come out `ħ/2` while
   the beat gives `2mc²/ħ`? This is now the single highest-value calculation in
   the workstream — it is the one candidate addressing the factor of 2, the
   spin-0 problem, and the double-cover question at once.
2. **Reconcile timelike-axis with Kaluza–Klein compactness**, or pick one.
3. Still open from `0001`/`0002`: what confines the ray; light bending as the
   cheapest test of the differential-relativity programme.
