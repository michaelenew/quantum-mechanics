# 0022 — The cone from the web: closing O3

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0021 established that a causal cone lives in the geometry's response
*if* channel updates are c-bounded — leaving the bound itself as an
assumption. This exploration removes the assumption. The c-bound is
derived from the postulates the program already holds: P1 (all
content is pairwise) plus the movie's premise (all change happens at
interactions). Together they say a node's knowledge can update only
through its channels — and everything 0021 imposed then *emerges*,
including the retarded rule itself. Code:
`output/0017_the_cone_from_the_web.py`.

---

## The derivation, in four computed steps

**1. Locality gives an exact cone; connectivity gives its shape.**
If change happens only at interactions, influence relays at most one
hop per event round — so news emitted at an event occupies *exactly*
the graph-metric ball of radius = elapsed rounds. Verified
set-equal against BFS on N4 and N8 lattices at two horizons: the
dependency cone is exact, with zero tail — not a Lieb–Robinson-style
bound with exponential leakage, but strict, because the update rule
is strictly local. But the lattice cone is polygonal: anisotropy
√2 = 1.414 on both N4 and N8 (measured 1.408, 1.414). On a random
geometric web the front is round: anisotropy 1.127 and 1.073 at two
snapshots. **The isotropy of the light cone is not an axiom — it is
the statistical isotropy of the web's connectivity**, absent on
crystals, emergent on disordered webs.

**2. The retarded rule emerges.** Nodes gossip the freshest record
of a moving source (0021's kicked worldline) through their channels.
The resulting record field converges to the retarded field
y(t − ρ/c), with c the *measured* front speed of the web itself:
mean |recorded − retarded| falls from 6.3% to 4.3% of the move size
as the web densifies. So 0021's update rule was never an extra
physical assumption: **the retarded field is what "a node knows only
what its channels have told it" looks like in the continuum.** All
of 0021's results — the light cone in curvature, δ = πw(1 − v²), the
fan — now stand on the postulates alone.

**3. One web, one cone — why c is universal.** Two different
payloads (position news, strength news) gossiped on the same web
arrive at every one of 2500 nodes at *identical* ticks, equal to
graph distance. Every signal rides the same interaction graph, so
all influence shares a single cone — which is the physical content
of "c is universal." The *value* of c is the conversion a/τ between
the web's length unit and its event unit: a unit choice — precisely
the status the physical c has (a defined constant, not a measured
ratio).

**4. The two tiers are the trace and traceless sectors.** The
signature question's last piece is why the "instantaneous" tier of
P2 doesn't violate the cone. Computed, with three sources gossiped
independently: **tr h(x) = S_total at every node at every tick**
(deviation 2×10⁻¹⁶) — even mid-transient, while news is still in
flight. The trace sector never updates because it never needs to: it
is position-blind, carries no signal, and cannot be used to
communicate. The **traceless (anisotropy) sector carries all the
news** — frozen at a far probe until its arrival tick, then
changing — and by 0020 it carries *all the curvature*. So P2's
split is realized as an exact sector decomposition of the web's own
field:

```
correlational tier  =  trace sector      (exact always, signal-free)
actionable tier     =  traceless sector  (c-bounded, carries curvature)
```

## What "closed" means here, precisely

O3 asked where the minus sign comes from. The answer assembled over
0021–0022:

- **Causal structure is derived.** Strict locality (from P1 + the
  movie) ⇒ exact cone; statistical isotropy ⇒ round cone; one graph
  ⇒ one universal c; relayed knowledge ⇒ retarded fields ⇒ the
  measured light cone in curvature, with the state-space metric
  Riemannian throughout. Signature lives in the dynamics, and the
  dynamics' cone is now a consequence, not an input.
- **The Euclidean/Lorentzian dial is a measured coefficient**
  (0021): δ = πw(1 − v²), continuing to (1 + v²) under v → iv.
- **The non-signalling of the instantaneous tier is a theorem of
  the field's structure** (the trace identity), not a separate
  postulate.

What is *not* claimed: full Lorentz invariance — that boosts are a
symmetry of the dynamics, not merely that a cone exists. A cone
gives causal order; Lorentz symmetry is more. The evidence in hand
is suggestive — the exactly clean (1 − v²) law is what a
boost-covariant theory would print — but it is one law, not an
invariance proof. That, and only that, remains of O3; call it O3′.

## Honest limits

- The gossip model instantiates "change only at interactions" in
  the simplest way (freshest-record relay). Other local rules give
  the same cone (that part is general) but could give different
  effective fields at finite density; the retarded-field convergence
  is shown for this rule.
- Front-speed measurement on the random web has finite-size scatter
  (front anisotropy ~1.1 at the tested densities); the
  isotropy-from-disorder claim is a trend with density, exact only
  in the limit.
- The trace/traceless identification of P2's tiers is exact for
  channel fields of the form Σw·uuᵀ; richer channel structures
  (varying strengths in flight) would put strength-news into the
  trace sector, which would then be c-bounded too — the clean
  "trace = correlational" split is a property of
  strength-conserving webs.

## Open

1. **O3′ — boost symmetry**: test Lorentz covariance directly — e.g.
   compute the fan f(θ) and the two-body retarded interaction in
   two frames related by the candidate boost and check covariance;
   the (1 − v²) law suggests it may hold exactly.
2. **Radiation** (from 0021, still queued): does an accelerating
   source radiate net curvature to infinity, or is the web
   radiation-free like 2+1 GR?
3. **The retarded two-body problem**: velocity-dependent
   (magnetic-like) corrections to the no-pair-force result.
4. **First-passage universality**: the measured front advance
   (~0.83 r per tick across densities) suggests a universal
   first-passage constant of the random web — the microscopic
   origin of c's numerical stability.
