# 0010 — The arithmetic bridge: measured evidence for P3/P4 from the formal-languages workstream

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

A parallel workstream (`michaelenew/formal-languages`, `arithmetic/`,
explorations 0056–0066) arrived at this repo's architecture from the
opposite direction — self-referential definitions over bitstrings
rather than particles — and *measured* several things this repo
posits. This note is the dictionary and the imports. Everything cited
as verified has a runnable module in that repo's
`arithmetic/output/`; nothing here is new derivation.

## The dictionary

| here (relational–epistemic QM) | there (revision dynamics on bitstrings) |
|---|---|
| pairwise knowledge state on an edge | a context: one constraint between two channels |
| mutual consistency of the web | stationarity under the revision map T |
| no global section (P3) | paradox: T has no fixed point |
| cocycle condition / H¹ (P4) | parity of negations around a reference cycle |
| frustration vs contextuality, same H¹ | verified: the liar-detection parity IS the context obstruction (0058) |
| composition rule selects the theory | probabilities vs amplitudes tier (0059 §5) |
| measurement = coincidence + re-projection | reading a context of a sampled world (0061) |

## Measured results that bear on the postulates

1. **P3's obstruction is graded, and the grade is a holonomy group**
   (0059, 0060, 0062). Forced entropy of a consistent belief state =
   log₂(smallest orbit of the revision holonomy); the floor
   distribution is Haar measure on the deck group. Joint systems
   synchronize on lcm of their clocks — never the sum ("one coin,
   many liars"). If P4's cocycle picture is right, this predicts the
   *cost* side of H¹: each nontrivial class taxes log₂(its order).

2. **The obstruction survives every classical repair and dies at
   amplitudes** (0059 §5, 0064). Product beliefs pay k bits;
   correlated beliefs pay exactly 1 (the phase of the forced
   oscillation); amplitudes pay 0 — the cat state is a *pure*
   stationary state whose measurement statistics equal the classical
   floor. Epistemic restrictions on classical points (Spekkens-style
   knowledge balance) reproduce the stabilizer fragment's structure
   and stop exactly at the parity (0064). Minimal negativity of the
   contextual triangle model: **1/2 exactly, located on the phase
   fiber** (0064) — the sign problem is the H¹ class priced in
   signed measure. Relevant to this repo's "composition rule selects
   the theory": the selection is *forced* at nontrivial H¹.

3. **The two-tier split (P2) has a measured analogue and a measured
   limit** (0061). The theory yields zero evidence about the mixture
   weight between consistency sectors (pure trust coordinate —
   probability/trust separation with fully known distributions);
   observation prices it through a closed-form channel; the
   context-bound reader pays Fisher efficiency η(½) = ½ against a
   global reader, and the gap is charged to contextuality itself
   (simultaneous context access = the oracle). Under drift the
   static 2× gap compresses to 2^{1/4} in tracking SD — oracle
   advantages enter at the fourth root.

4. **The sheet is relational** (0063). Absolute consistency-sector
   ("which of the two dual worlds") is *gauge*: no observable of the
   dynamics refers to it and its marginal is compulsory noise;
   relative sector between subsystems is invariant and exact. The
   frame's version of "2π rotation of the universe is invisible; of
   one interferometer arm, measurable." Directly supportive of P1
   (all content is relational) — with a sharper claim: the absolute
   coordinate is not merely unknown but gauge.

5. **Contextuality = holonomy = double-cover structure** (0062).
   One traversal of an odd constraint cycle is the deck flip
   (T^k = ¬); the obstruction dies on the double cover; the ± sectors
   upstairs are the spinor split. For P4: the "loop composition must
   be trivial-up-to-phase" clause is exactly what the amplitude tier
   supplies — the phase *is* the sheet index.

6. **Where commutativity breaks** (0066). Two constraint loops
   through a shared ≥3-valued node generalize the tax to
   log₂(smallest orbit of the generated group), and the commutator
   of loop-traversals becomes a deterministic observable — the
   permutation shadow of braiding. Binary-valued nodes cannot braid.
   If this repo's web ever needs non-abelian H¹ (anyonic sectors),
   the minimal mechanism is the second loop through a shared
   multi-valued edge.

7. **The logic face** (0065). Decided statements = deck-invariant
   ones; independent statements come in dual pairs swapped by the
   deck; gauge-fixing by a reference converts relative to absolute
   at exactly the 1-bit tax and the tower never closes (iterated
   incompleteness as dynamics). Gödel's fourth bucket ("true but
   unprovable") = truth on a sheet the language cannot name — the
   same relational-sheet structure as item 4, on the logic side.
   This is the strongest hint that this repo's P3 and incompleteness
   are one phenomenon: both are "no global section," differing in
   which cover the sections live on.

## Pointers

- Repo: `michaelenew/formal-languages`, branch
  `claude/clue-workstream-conclusion-a15blx`, `arithmetic/SUMMARY.md`
  (state of the art), explorations 0056–0066 with runnable
  verification modules in `arithmetic/output/`.
- Visual explainer of the core objects (functional graphs, the
  forced coin, the odometer, w and phase, the contextuality games):
  Claude artifact "The Clock and the Coin".
- The stat-tracker kernel imports (this repo's 0008/0009) are the
  same trust/probability split measured there as the orphaned
  mixture weight; 0061's η and fourth-root results quantify what the
  split can and cannot buy against contextuality.

## Cautions

- The arithmetic frame's "quantization" is one natural choice
  (permutation unitaries + invariant states); it demonstrates
  existence of zero-entropy consistent states, not uniqueness of QM.
- All group-theoretic results are for finite revision systems; the
  continuum/field-theoretic analogues are conjecture.
- Negativity 1/2 is for atom-diagonal quasidistributions of that one
  scenario; frame-dependence of negativity is known and unexplored
  there.
