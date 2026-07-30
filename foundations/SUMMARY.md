# foundations — SUMMARY

State of the formalization. **Reframed** around consistency as the fundamental
law; nonlocality embraced (see `exploration/0003`, which supersedes P2 of
`0001`).

## Current postulates

- **P1 Relational states** — all content is pairwise knowledge states
  `{ρ_{A→B}}` over relative coordinates; no absolute frame.
- **P2 Two-tier knowledge** *(reframed)*.
  - **Actionable** knowledge (usable to do something differently — forces,
    signals) is *c*-bounded.
  - **Correlational** knowledge (the mutual consistency of the web) updates
    **instantaneously and nonlocally** — not as a propagation, but as global
    re-satisfaction of a constraint. Non-signalling because the outcome is
    random and averages away in every distant marginal.
- **P3 Pairwise consistency, no global section** *(reframed)*. Every pairwise
  overlap agrees, but the family need **not** admit a single global joint
  distribution of definite values. Demanding such a joint = local
  hidden-variable model (Fine's theorem) → falsified. Local consistency
  *without* a global section is the sheaf-theoretic content of
  contextuality/nonlocality — the mathematical name for "no god's-eye view."
- **P4 Recursive consistency** — chains compose; variance additivity /
  data-processing inequality on relative coordinates. Interpreted now as a
  candidate quantum-selecting principle (see `testability/`).
- **P5 Measurement = coincidence + minimum-relative-entropy projection.** A
  split/merge sharpens one edge; the whole connected component re-settles by
  projecting onto the consistency manifold with minimum relative entropy — the
  unique rule matching the posit's own desiderata (reduces to Bayes, injects no
  extra uncertainty, order-independent). Classical version solid; quantum
  equivalence to the Lüders/Born update is open and concretely tractable.

## The corrected central story

- Consistency is fundamental and global; nonlocality is its shape.
- The two-tier structure (actionable vs. correlational) resolves the
  c-vs-instantaneous tension without violating no-signalling.
- The consistency law read *without* a global section automatically forces
  non-classical (Bell-violating) correlations — a derivation from the posit's
  own words. Demonstrated numerically in `testability/output/0002`.
- Whether it forces *quantum* (S ≤ 2√2) rather than merely *non-classical* is
  the frontier; concrete open leads listed there.

## Positioning (`exploration/0002`)

Inherited: relational stance (RQM), epistemic/Bayesian state (QBism, Spekkens),
decoherence (Zurek — now re-read as *dilution*, not destruction), relative-frame
states (QRF/Giacomini), sheaf-contextuality (Abramsky–Brandenburger),
information-causality (Pawłowski) as a candidate cousin of P4.

Contributed: the two-tier resolution of the c-vs-instantaneous puzzle;
MRE-projection as the specific update rule; the framing that P4/MRE *might*
select the quantum set (open, do not overclaim); consistency-first packaging
that turns "no god's-eye view" from a slogan into the sheaf-theoretic
non-extendability condition.

## Recursive consistency as a cocycle (`exploration/0004`)

Pressing on P4 directly. Model the web as a graph, edges = pairwise knowledge
states. Recursive consistency = composition along any two paths agrees =
**cocycle condition** (Čech cohomology). Nontrivial `H¹` of the constraint
sheaf = "no god's-eye view" made mathematically precise.

- **Tree-shaped webs** have vacuous cocycle → always classical.
- **Loop-containing webs** admit nontrivial holonomy → frustration (classical)
  or contextuality (quantum), depending on the composition rule.
- The **composition rule on edges selects the theory** (convolution → classical
  probability; symplectic/unitary → QM; other rules → other GPTs).
- Frustration and contextuality are proposed to be the *same* `H¹` structure
  with different composition rules. Target, not yet proven.
- Verified in `testability/output/0003`: compatible-observable triangle has
  polytope = classical (1/3 of cube), so pure-graph-topology contextuality
  requires **choice of context** (incompatible observables) — an important
  localization of where quantumness enters.

## Geometry of the web (`exploration/0005`, `output/0001`)

The moment we say "knowledge is a distribution," the web inherits a
Riemannian geometry with **no axiomatic freedom**: Chentsov (classical) /
Petz (quantum) uniqueness fixes the metric up to scale. Immediate
consequences:

- Gaussian knowledge `(μ, σ)` → hyperbolic upper half-plane
  (constant negative curvature).
- Pure qubit knowledge → `CP¹ = S²` with the Fubini–Study metric
  (constant positive curvature). Fidelity `= cos²(α/2)`. Verified in
  `output/0001_qubit_geometry.py`, including Gauss–Bonnet excess to
  machine precision.
- Composition of knowledge along the web = parallel transport.
  Loop-holonomy = curvature = the differential-geometric statement of the
  cocycle obstruction (`0004`).
- Uncertainty relations = curvature bounds on the state manifold
  (Anandan–Aharonov speed limit is the canonical example).

The GR analog is literal, not metaphor: general covariance ↔ sufficient-
statistics invariance; light-cone causal structure ↔ two-tier
actionable-vs-correlational split; mass sources curvature ↔ (open)
correlation/entanglement sources information-manifold curvature (holography /
Ryu–Takayanagi territory, cited-not-claimed).

## Two-tier structure & the FTL barrier (`exploration/0006`)

Taking the user's precise reading of SR seriously: relativity forbids
*continuous* crossing of `c`, not FTL per se. That leaves a clean slot for
discrete, non-continuous, non-signalling correlational updates. Geometrically:

- **Actionable knowledge = dynamics on the manifold** (timelike/null,
  continuous, ≤ c).
- **Correlational knowledge = spacelike constraint structure on the manifold**
  (not a propagation, no speed applies).

The "instantaneous distant update" is the spacelike-slice re-shaping to keep
the constraint satisfied. Nothing crosses `c` because nothing crosses at all.
Tachyons are not needed and come with their own baggage; the cleaner slot is
constraint-structure vs. dynamics. Removes the paradox-flavor of "collapse is
instantaneous but SR is respected" — the two describe different geometric
objects.

## Reconstruction route (`exploration/0007`)

Candidate axiom list combining P1–P5 with Fisher/Bures uniqueness,
purification, and continuous reversibility. Existing reconstructions
(Hardy 2001; Chiribella–D'Ariano–Perinotti 2011; Masanes–Müller 2011) already
derive standard finite-dim QM from information-theoretic axioms; what the
consistency-first packaging may add is a **single unifying physical picture**
motivating all of them at once, plus the two-tier resolution of the
c-vs-instantaneous puzzle. Concrete milestones ordered by tractability; the
crux step is showing that (1)–(8) collectively imply the CDP/Hardy axiom set.

## Known gaps

- Whether P4 (or MRE inside a PR-box) tightens the bound to Tsirelson — the
  quantum-selection question. Open and tractable (`exploration/0007` step 3).
- Quantum-MRE equivalence to Lüders / Petz recovery — open.
- Frustration ≅ contextuality as cohomological structures — proposed, not shown.
- "Correlation sources curvature" as an Einstein-like equation on the
  information manifold — speculative; standing candidate.
- No dynamics yet; only kinematics and the update rule.
