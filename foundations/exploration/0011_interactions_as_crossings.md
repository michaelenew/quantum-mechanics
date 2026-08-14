# 0011 — Interactions as crossings: knots as consistency webs

The proposal: interactions are fundamentally topological — every
interaction adds a crossing to a knot-like structure — and perceived
curvature is the holonomy of closed loops around those crossings (a
sign you must see going around once, resolved on the dual/double
loop). This note tests the checkable parts exactly and registers the
proposal against the physics that already realizes pieces of it.
Code: `output/0004_knots_as_consistency_webs.py`.

---

## 1. A knot diagram is literally one of our webs

Take a knot diagram and read: **arcs = channels, crossings =
three-party interaction constraints** (`2·over = under_in +
under_out mod p`). Then global sections of the web are Fox
p-colorings — equivalently, flat dihedral connections on the knot
complement. Computed from Gauss codes by exact elimination:

| knot | p=2 | p=3 | p=5 | p=7 | first nontrivial |
|---|---|---|---|---|---|
| unknot | 2 | 3 | 5 | 7 | — |
| trefoil | 2 | **9** | 5 | 7 | 3 |
| figure-eight | 2 | 3 | **25** | 7 | 5 |
| cinquefoil | 2 | 3 | **25** | 7 | 5 |
| granny | 2 | **27** | 5 | 7 | 3 |

The web "opens extra sections" exactly at the knot's holonomy
moduli. So the interaction-as-crossing reading is not a metaphor to
develop — it is an isomorphism of formalisms: knot theory *is* the
consistency-web theory of a particular family of webs (one loop of
channels, one constraint per interaction), and P3's global-section
question is the coloring question.

## 2. The invariant lives on the double cover — and abelian shadows vanish

The modulus where extra sections appear divides the knot determinant
|Δ(−1)| = |H₁(branched **double** cover)| — the knot's tax is
counted on its second loop, exactly matching the arithmetic frame's
paradox tax (forced entropy paid on the deck of the double cover).
Verified against the torus-knot Alexander polynomial by exact
polynomial division: det T(2,3) = 3, T(2,5) = 5, T(2,7) = 7 — and
**det T(3,5) = 1**: a nontrivial knot whose entire abelian holonomy
shadow vanishes.

Consequence for the proposal, and for the "braided is the
interesting one" instinct: **knot detection needs nonabelian
holonomy.** Every abelian invariant can be blind to a nontrivial
knot; Kronheimer–Mrowka's theorem (every nontrivial knot admits
irreducible SU(2) representations of its group — literature, not
re-proved) says the nonabelian level *never* misses. "Every
nontrivial knot forces perceived curvature on the path-to-self" is
true exactly at the nonabelian tier, and can fail at every abelian
tier.

## 3. Curvature: the right form of the clause

Two computations pin the geometry:

- **Discrete Bianchi** (octahedron, random Z₂ connections): every
  edge borders exactly two faces, so the product of all face
  holonomies is +1, always. Bulk curvature cancels pairwise — the
  same two-ends cancellation as the knot counter's full loop and
  the chord diagram's double cover. Total curvature is topology,
  never a bulk sum.
- **Flat but holonomied** (3×3 torus, exact GF(2) ranks): the
  connections flat on *every* face still fall into 4 gauge classes
  = |H¹(T²;Z₂)| — holonomy around non-contractible loops with zero
  local curvature everywhere.

So the accurate version of the curvature clause: **holonomy is the
primitive; curvature is its local density; and the density can be
zero everywhere you travel while the loop still turns you** — the
Aharonov–Bohm / conical-defect configuration. The strongest physics
registration: in 2+1 dimensions this is not an analogy but the whole
theory — matter is conical defects, spacetime is flat away from
them, gravity is pure loop holonomy (Deser–Jackiw–'t Hooft), and
the theory is a Chern–Simons theory (Witten) — the same Chern–Simons
whose Wilson-loop expectations are knot invariants. Interactions as
crossings, curvature as crossing holonomy, and knot invariants as
the amplitudes are, in 2+1D, one formalism. The honest boundary: in
3+1D curvature also propagates freely (gravitational waves), so
"curvature = defect holonomy" cannot be the whole story there.

## 4. What this buys the web program

- P3/P4 gain a large worked example family: knots are webs whose H¹
  is completely understood, with a graded invariant (colorings /
  Alexander / determinant) measuring the obstruction — candidate
  test cases for the composition-rule question (classical
  convolution on knot webs = colorings; what does the
  unitary/symplectic rule give on the same webs? The known answer —
  quantum invariants, Jones-type — suggests the composition-rule
  dial interpolates Alexander-tier to Jones-tier invariants).
- The interaction-history of a web is a braid word; 0066 (arithmetic
  repo) shows order-of-interaction becomes observable exactly when
  loop monodromies stop commuting, and the tax generalizes to
  log₂(smallest orbit of the generated group). The web's "memory of
  its own history" is the braided tier.

## Honest limits

- Colorings computed for five small diagrams; determinant identities
  for torus knots via the standard Alexander formula (exact
  arithmetic). |Δ(−1)| = |H₁ of the double branched cover| and
  colorings-as-dihedral-representations are classical results,
  cited not re-proved.
- 2+1 gravity and Kronheimer–Mrowka are literature registrations.
- The proposal's strongest form — that *physical* interactions in
  3+1D are crossings in an actual knotted structure — is not
  addressed; what is shown is that the web formalism this repo is
  already committed to *contains* knot theory as a sub-case, so the
  question becomes internal and testable rather than analogical.

## Open

1. **The composition-rule dial on knot webs.** Same web, three
   rules: convolution (→ colorings), unitary (→ which quantum
   invariant?), general GPT — does Tsirelson-type interpolation
   appear between Alexander-tier and Jones-tier detection power?
2. **det-1 webs as "quantum-only" knots.** T(3,5) is invisible to
   every abelian section count; build its web and ask whether the
   repo's MRE/consistency machinery sees it — a concrete
   discriminator between abelian and nonabelian consistency laws.
3. **Curvature from crossing density.** In 2+1 the dictionary is
   exact (deficit = mass). Whether the web's information metric
   (foundations/0005) reproduces deficit-angle geometry around
   high-degree interaction nodes is a computation, not a philosophy
   question.
