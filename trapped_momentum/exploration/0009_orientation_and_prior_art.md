# 0009 — Orientation: where this actually stands

No new calculation. An honest assessment of the workstream's state, the prior
art, and what the next rung is.

## The prior-art question, answered

Grading matters here, so: **[V]** = verified by search this session,
**[K]** = asserted from my own knowledge, search quota exhausted before I could
check it. Treat [K] items as leads to confirm, not as established.

### The closest match is 55 years old and much further developed

**[V] Souriau (1970), *Structure of Dynamical Systems* — the coadjoint orbit
classification of elementary particles.** For the Poincaré group, coadjoint
orbits *are* the elementary particles, characterised by the invariants `m` and
`s`. Quantising a coadjoint orbit yields a unitary irreducible representation —
the Hilbert space of a relativistic particle. The classification covers both
elementary and composite particles.

That is the organising claim of this workstream, stated first and carried much
further. "The particle taxonomy is the orbit/conjugacy classification of the
symmetry group, with mass and spin as orbit invariants, and quantisation coming
from the orbit's geometry" is Souriau's programme. `0008` rediscovered a corner
of it.

**[V] Penrose–Rindler, *Spinors and Space-Time*.** Every Lorentz transformation
acts on the celestial sphere exactly as the corresponding Möbius transformation
acts on the Riemann sphere; `PGL₂(ℂ) ≅ SO⁺(1,3)`. Penrose called this "the
first step of a powerful correspondence between the spacetime geometry of
relativity and the holomorphic geometry of complex spaces." The null-flag
construction and the spinor treatment of null directions are the standard tools
for exactly the structures in `0005`–`0008`.

**[K]** The elliptic / hyperbolic / loxodromic / parabolic split is the standard
conjugacy classification of Möbius transformations, textbook material long
predating any of this. The search snippet confirmed the Möbius correspondence
but not this classification specifically — though I have no real doubt about it.

### Other pieces, all [K] and all standard

- **Wigner (1939)** — the little-group classification. Mass and spin as the two
  Poincaré Casimirs; massive little group `SO(3)`, massless `ISO(2)` giving
  helicity. `0006`'s "helicity is one number because `k^⊥` is degenerate" is
  this result reached geometrically.
- **Riemann–Silberstein vector** `F = E + iB`. Its square gives
  `(E² − B²) + 2i(E·B)` — both electromagnetic invariants packaged in one
  complex number. That is `0008`'s `det X` result, and it is standard
  electromagnetism.
- **Petrov classification** — classifies the Weyl tensor by the *degeneracy of
  principal null directions*, with the maximally degenerate type N being
  radiation. Structurally the same move as `0008`'s "masslessness is eigenvector
  degeneracy." Worth checking properly: if the parallel is as close as it looks,
  it is the most interesting unverified lead here.
- **Hestenes' zitterbewegung interpretation** and **Carter's Kerr–Newman
  electron** — both verified earlier in this workstream (`0001`).

### The verdict

**Essentially every piece of mathematical structure built here is standard and
well-mapped.** Not approximately — specifically. The trichotomy is Möbius
conjugacy, the complex determinant is Riemann–Silberstein, the helicity
degeneracy is Wigner, the taxonomy-as-orbits is Souriau, and the spinor
square root of a null vector is Penrose's flagpole.

What is not obviously in the literature is the *route* — arriving here from
"what if a photon chased its own tail." That is a pedagogical path, not a
result, and it should not be mistaken for one.

## Assessment of the stated position

The stated read was: a unifying framework that describes but does not predict;
nothing worth sharing; a pretty idea that survives basic scrutiny; possibly
already explored. That is close to right, with three amendments.

**1. It is weaker than "describes."** There is no dynamics — no action, no field
equations, no way to compute a cross-section or an amplitude. What exists is a
*kinematic taxonomy*: a statement of which structures exist and how they relate.
"Describes" oversells it; "classifies" is the honest word.

**2. "Doesn't crumble" is worth something, but less than it feels like.** The
framework has absorbed several rounds of correction — the photon break, the
retracted `u + S` hack, two of my own coding bugs, the `0004` single-invariant
limitation. Absorbing corrections gracefully feels like progress and is
partly a warning sign: a framework flexible enough to accommodate everything
predicts nothing. The discipline that fixes this is stating an expected answer
*before* computing it. That has not been done once yet in this workstream.

**3. There is a rung between "pretty idea" and "predicts values."** Namely:
**derive a known result the framework did not have built in.** That is
reachable now, and it is the correct next milestone.

## On the measuring stick

"Can this framing set up correct relativistic calculations" is the right
instinct but too easy a bar. Any correct reformulation passes it — that is what
"correct" means. The bar that separates a contribution from a notation change:

> **Does it get a known answer more cheaply than the standard route?**

If the same work reappears in different symbols, there is no contribution, only
a translation. Most "everything falls out of one framing" claims fail exactly
here — the work is not removed, it is relocated into the setup.

### The concrete first test: Thomas precession

Proposed as the next calculation because it is a genuine test rather than a
demonstration:

- **The framework's own generic class predicts it.** The product of two boosts
  about different axes is **loxodromic** — it has a rotation part that neither
  factor had. In this framing that is not a surprise to be explained; it is
  what the classification says must happen.
- **The rotation part is the Wigner rotation**, whose accumulation is Thomas
  precession — the factor that famously fixes the spin–orbit coupling in the
  hydrogen fine structure.
- **It is famously fiddly** in the standard vector formalism and famously short
  in `SL(2,ℂ)`. So it is a real test of "is this framing cheaper," not just
  "is it consistent."
- **It is falsifiable.** The factor comes out right or it does not, and it can
  be checked against the textbook value.

Crucially: the expected answer should be written down *before* computing it,
to break the retrofitting pattern noted above.

Second and third tests, in order of difficulty: relativistic velocity addition
(trivial, a warm-up), and `g = 2` for the electron (hard, and where Carter's
Kerr–Newman result suggests the framework might have something).

## On what predictive power would look like

The stated form — predicting specific values — is right but it is not the only
form, and it is the hardest one.

- **Values** (a mass, a coupling): hardest. `0006` already argued the value of
  α is out of reach for a kinematic framework, since α runs.
- **Relations between values** (`g = 2`, a mass ratio): more achievable, still
  a genuine result.
- **Forbidding things**: underrated and often the strongest available. A
  framework that says "only these structures can exist" is predictive if the
  list is right, finite, and matches. Ours says the taxonomy has exactly four
  classes — but it has not yet been checked whether that forbids anything
  observed, or explains anything absent. **Worth noting: Wigner's classification
  permits "continuous spin" representations that are not observed. If this
  framing said why, that would be a real result.** [K] — the existence of those
  reps is standard; whether anything here bears on their absence is untested.

## On the two named prizes

**Quantum gravity** is very far. The honest distance: no dynamics at all. The
nearest thing produced is `0005`'s result that a traceless source cannot couple
to a scalar mediator, which forecloses one option rather than supplying a
theory. Treat as a direction, not a target.

**Saving students a pile of equations** is the realistic and honourable outcome,
and it is worth more than the phrasing suggests — reformulations that genuinely
reduce the work are rare. But it is *conditional on the Thomas-precession-style
test passing*. A unification that does not make anything cheaper is a
restatement.

## Recommended next steps

1. **Thomas precession**, with the expected answer written first. Tests
   cheapness, not just consistency.
2. **Check the Petrov parallel properly** — the most interesting unverified
   lead, and if it is as close as it appears, the framework's mass/degeneracy
   result is a known theorem in another domain.
3. **Read Souriau** before building further. That is where this programme
   already lives, and duplicating it would be waste.
4. Standing open items unchanged: what fixes `ζ`, charge quantisation as a
   winding number, whether the dynamics select the antiperiodic sector.
