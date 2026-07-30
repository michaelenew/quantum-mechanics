# 0007 — A route to reconstructing QM from the consistency-first postulates

Goal (per the user): a set of neat assumptions that either derives standard QM
up to what's measured, or agrees with it computationally in a form that is
more tractable for understanding and engineering.

This note pulls together the pieces we've assembled into a candidate route,
attributes each ingredient honestly (much is prior art in the "reconstruction"
literature), and states what remains to be shown.

## The candidate axiom list

Numbered so we can point at gaps. Each is a candidate; the exact minimal set
is itself a research question.

1. **Relational states (P1).** All content is pairwise knowledge states
   `{ρ_{A→B}}` over relative coordinates. No absolute frame.
2. **Two-tier locality (P2, reframed in `0003`, `0006`).** Actionable
   knowledge propagates ≤ `c`; correlational knowledge is spacelike
   constraint structure, not a propagation.
3. **Pairwise consistency, no global section (P3, reframed in `0003`).**
   Local agreement without a god's-eye joint distribution — the sheaf-
   theoretic content of contextuality.
4. **Recursive consistency = cocycle (P4, `0004`).** Composition along paths
   agrees; loop-holonomy is the curvature of the connection.
5. **Fisher / Bures uniqueness (`0005`).** Knowledge distributions form a
   Riemannian manifold with a metric fixed (up to scale) by invariance under
   sufficient statistics / CPTP maps (Chentsov 1972; Petz 1996).
6. **MRE / Petz update rule (`0003`, P5).** Measurement = projection onto
   the constraint surface minimizing relative entropy — reduces to Bayes
   classically, to Lüders/Petz quantum-mechanically.
7. **Purification.** Every mixed knowledge state on a node is the partial
   view of a pure state on a larger web. Extremely natural in the
   consistency-first framing: my ignorance of `B` is a slice of the pure
   state of `B ∪ (rest of web)`.
8. **Continuous reversibility.** Between any two pure states there is a
   continuous, reversible transformation (a smooth reparametrization of
   knowledge; a unitary rotation on the manifold).

## Where each axiom probably suffices for something

- (5) alone fixes the *geometry* of a node's knowledge manifold to be
  `CP^(N-1)` with the Fubini–Study metric for finite-dimensional systems and
  the hyperbolic geometry of Gaussians for continuous ones. This is real
  content: it explains why the quantum state space is a complex projective
  space, not something else.
- (7) + (8) is essentially Hardy's five reasonable axioms (2001) or the
  Chiribella–D'Ariano–Perinotti purification-based reconstruction (2011).
  Both **derive standard finite-dimensional QM** (Hilbert-space structure,
  Born rule, unitary evolution, Lüders update). This is not conjecture; it
  is theorem in the reconstruction literature.
- (3) + (4) together give the contextuality skeleton — the *shape* of the
  correlation polytope. As `testability/output/0002` showed, this rules out
  the classical (Bell-local) polytope but not by itself the super-quantum
  (PR-box) region.
- (6) inside a super-quantum scenario is the concrete candidate for the
  additional bite that tightens the correlation set from the no-signalling
  polytope to the quantum one. **Untried; the concrete open theorem.**

## The story if this works

If (1)–(8) can be shown mutually consistent and jointly to imply standard QM,
the consistency-first theory is a *reconstruction of QM* — not a modification.
That would be a genuine outcome for the user's stated goal:

- Understanding: every piece of QM has a natural informational reason to be
  there.
- Engineering: the objects (Bloch spheres, Fisher metrics, MRE projections)
  are *already* the tools quantum engineers use — this framing centers them,
  and its computations run in exactly the same libraries.
- Novelty: not in predictions, but in what the theory *tells you to do*. That
  can matter — general relativity didn't add new observations for years, but
  reorganizing gravity as geometry made problems tractable that Newtonian
  perturbation had struggled with for decades.

## Prior art, honestly

- Hardy, *Quantum theory from five reasonable axioms* (2001).
- Chiribella–D'Ariano–Perinotti, *Informational derivation of quantum theory*
  PRA 84, 012311 (2011). Key axiom: purification.
- Masanes & Müller, *A derivation of quantum theory from physical requirements*
  NJP 13, 063001 (2011).
- Barnum, Barrett, Leifer, Wilce, and others in the GPT program.

We are not the first to try to reconstruct QM from information-theoretic
axioms — that literature is deep and largely successful in finite dimensions.
What the consistency-first packaging may add:

- A **single physical picture** — the web of pairwise knowledge with a
  two-tier locality structure — that motivates *all* the axioms at once,
  rather than adopting them from convenience.
- **Explicit relational / no-god's-eye reading** (Rovelli-style RQM) as the
  ground floor, so the reconstruction lives natively in the picture where
  measurement problems don't arise.
- **The two-tier resolution** of the c-vs-instantaneous puzzle from within,
  removing a piece of confusion that the existing reconstructions typically
  leave to interpretation.

## Concrete milestones (order of decreasing tractability)

1. **Sanity-check the Fisher / Bures uniqueness on a couple of small
   systems** and see that "engineering with the metric" recovers standard
   quantum-info results. Done for the qubit in `output/0001`. Extend to a
   two-qubit example (CP³ with Fubini–Study) as the next step.
2. **Formalize P4 as a cocycle-with-curvature statement on the web** and
   check that its integrated form reproduces the standard uncertainty
   relations as curvature bounds on the state manifold. Half-done in `0005`;
   the honest write-up is missing.
3. **Attempt an MRE update inside a PR-box scenario** and check for
   over-constraint against the quantum update. This is the concrete step
   that would either derive the Tsirelson bound or falsify axiom (6).
4. **Prove or disprove that (1)–(8) collectively imply the CDP / Hardy
   axiom set.** If yes: we have a reconstruction, and can claim it. If not:
   name the axiom (1)–(8) is missing, and iterate.

## Status

- The list of axioms: **candidate**, not proven minimal or complete.
- Existing reconstructions do derive QM from information-theoretic axioms —
  **theorem, cited**, not our result.
- The claim that (1)–(8) *specifically* imply QM: **open**. Milestone (4).
- Engineering value of the metric picture: **immediate**, since it lines up
  with existing quantum-info tooling; the framing hopefully makes those tools
  feel less arbitrary.
