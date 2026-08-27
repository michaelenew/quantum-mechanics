# 0018 — The wall theorem: the state sum, the anomaly polynomial, and group-independence

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0017's three opens, executed. The batch upgrades all three: the
branch-point-free state sum exists and is verified as a working
invariant; the reversal anomaly is an exact degree-1 polynomial,
canonical per orbit, with the mirror-twin structure descending to it;
and the branch wall is promoted from a p = 2, 3 observation to a
**theorem over every group** — with an unexpected corollary about
where the arrow of time lives. Code:
`output/0013_movies_anomaly_and_the_wall.py`.

---

## 1. The movie state sum exists — and the arrow is fiberwise

Branch-point-free abstract movies (n strands, events = triples of
strand slots, no births or deaths — the class 0017 identified as the
wall-free arena) carry a state sum: Z(movie) = the distribution of
total weight over all initial colorings. Verified:

- **Tetrahedron move at any embedding**: the 4-event cluster mapped
  through an arbitrary strand injection into an 8-strand movie,
  after a 3-event prefix — final state *and* total weight agree per
  initial state (all 256). The identity verified on the standard
  placement complex really is local: it holds wherever the complex
  embeds.
- **Distant commutation** of disjoint events: exact, per state.
- **Nontrivial**: Z(4-event cluster) = (32, 32) ≠ (64, 0) =
  Z(empty) — the state sum separates movies.

Then the aggregate question 0017 left implicit. The chiral weight's
fiberwise functional is ill-defined on reversed movies (32 of 64
states order-dependent). But the **state sum of the reversed movie is
ordering-independent anyway**: Z = (32, 32) under both orderings,
because the fiberwise flips split exactly 16 states 1→0 against 16
states 0→1. **The local anomaly cancels in the aggregate.** So the
arrow of time is a *fiberwise* invariant — visible to an observer who
tracks which coloring the world is in, invisible to the plain state
sum that integrates over all of them. The census's arrow is real but
lives one level below the partition function — the same shape as a
local anomaly that cancels globally.

## 2. The anomaly is a linear polynomial, and the mirror descends to it

The failure pattern F(s) = left(s) ⊕ right(s) of a chiral weight on
the reversed movie, fitted exactly over GF(2):

```
orbit 1:  F(s) = 1 + s₁ + s₃ + s₅        (minimal degree 1)
orbit 2:  F(s) = 1 + s₀ + s₃ + s₄        (minimal degree 1)
```

Three sharpenings:

- **Canonical.** Sweeping the *entire* forward-weight kernel: every
  nonconstant forward weight on a chiral orbit produces the *same*
  anomaly functional — one distinct F per orbit, always nonzero. The
  anomaly is a class attached to the orbit, not to the weight choice.
- **Structured.** Degree 1: the obstruction to running the film
  backward is an affine character of the state group — the parity of
  three specific strands plus a constant. Notably each orbit's F
  reads exactly the strand set of one placement: {1,3,5} is the
  third event's slots, {0,3,4} the second's. The anomaly is
  localized on an event.
- **Mirrored.** F₂(s) = F₁(s ∘ π) with π = (1,0,2,3,5,4) — swap
  strands 0↔1 and 4↔5. The mirror-twin relation between the two
  chiral orbits (0017) descends to their anomaly polynomials as a
  strand relabeling.

This answers 0017's open 2 at the census level: the anomaly is not
noise but a computable class — balanced (32/64, which is *why* §1's
aggregate cancellation happens), linear, canonical, and
parity-conjugate between the twins.

## 3. The wall theorem: group-independence

0017 measured the branch wall at p = 2, 3 and asked whether
nonabelian targets rescue it. The answer is a theorem, and the route
is the observation that makes everything tractable: **with
branch-point degeneracy the weight has only two free values**,
a = θ(0,1,0) and b = θ(1,0,1) (the other six triples are degenerate
and forced to e). The bidirectional tetrahedron identities then
become **word equations in a, b, valid over any group whatsoever**.
Per orbit, three tiers:

1. **Universal cancellation.** Deleting forced symbols, stripping
   common prefixes/suffixes (left/right multiplication by inverses),
   and reading off one-letter identities — moves valid in every
   group. Result: **all 19 walled orbits force a = b = e by
   cancellation alone.** (The chiral orbits' systems contain `e = a`
   and `e = b` outright.) The wall is **group-independent — a
   theorem over every group**, not a small-modulus artifact.
2. **The solvability tier** (now a cross-check): the abelianized
   difference lattice L has |Z²/L| = 1 for the same 19 orbits, so
   any solution would generate a perfect subgroup — walling all
   solvable targets independently of tier 1.
3. **Brute force**: Z₂, Z₃, Z₅, S₃, D₄, Q₈, S₄, and A₅ (smallest
   non-solvable). Zero nontrivial solutions on all 19 walled orbits
   in all eight groups; the Z_p counts match 0012's kernel
   dimensions exactly (p^dim − 1).

And the two orbits where the wall is down are laid bare: the
identity orbit's entire equation system is **ab = ba**, and the
abelian survivor's is **a = b**. So across the whole census and
every group: **zero genuinely noncommuting weight pairs exist**.
Even where weights survive, they are essentially abelian.

The interpretation now has no wiggle room: with branch points
allowed, braiding in the weight target is dead — not at small
moduli, not at any modulus, not in any group. The escape from the
wall is not a bigger group. It is exactly the two routes 0017 named,
minus one: **branch-point-free surfaces** (where §1's state sum
already operates), or **values beyond groups** (twisted/cocycle
coefficients, where the two-value collapse doesn't apply because the
degenerate triples need not map to a single identity).

## Honest limits

- §1's movies are abstract event sequences on strands; the claim
  "branch-point-free 2-knot invariant" still needs real movie
  presentations of real surfaces (the spun-trefoil test remains
  open — it needs the birth/death/saddle bookkeeping this state sum
  deliberately excludes).
- §2's anomaly polynomial is computed on the 4-event placement
  complex; its behavior under embedding into larger movies (does the
  class pull back along the injection?) is untested.
- §3's theorem is complete for group-valued weights under
  branch-point degeneracy with |X| = 2. Larger color sets X give
  more nondegenerate triples (more free values), and the collapse
  argument weakens; the wall's fate at |X| = 3 is open.
- A₅ brute force covers the smallest non-solvable group as a sanity
  tier; it is logically subsumed by tier 1's universal result.

## Open

1. **The spun-trefoil test**, still the head of the queue: real
   movie presentations with births/deaths/saddles, over the two
   abelian survivors (which passed every local condition) and over
   the 19-orbit bidirectional census on branch-point-free
   presentations.
2. **The anomaly under embedding**: does F pull back along strand
   injections (making it a class of the movie, not the complex)?
   If so, the fiberwise arrow globalizes: any movie containing a
   chiral cluster inherits an orientation functional.
3. **|X| = 3**: the wall theorem's collapse argument thins as the
   color set grows. A census at |X| = 3 is expensive but the
   degenerate-triple count (3² · 2 − 3 overlap) still leaves few
   free values — the wall may persist structurally.
4. **Twisted coefficients**: the one target class the theorem
   doesn't touch. The CJKLS literature's twisted cohomology is the
   natural next formalism for the census.
