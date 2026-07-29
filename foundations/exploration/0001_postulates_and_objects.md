# 0001 — Postulates and formal objects

Goal: pin down what the informal words ("knowledge distribution", "sharpness",
"consistency", "collapse") refer to, precisely enough that later claims are
provable or falsifiable.

## Formal objects

**Knowledge state.** For an ordered pair of systems, let `ρ_{A→B}` denote the
state *A* effectively acts on when it acts on *B*. Two candidate readings, held
in parallel until the fork (see `testability/`) forces a choice:

- *Quantum reading.* `ρ_{A→B}` is the reduced density operator on the
  **relative** degrees of freedom of *B* as described in a reference frame whose
  origin is *A* — i.e. a quantum-reference-frame conditional state
  (Giacomini–Castro-Ruiz–Brukner 2019; Bartlett–Rudolph–Spekkens 2007). Its
  Wigner function `W_{A→B}(q, p)` on relative phase space may be negative.
- *Classical reading.* `W_{A→B}` is an honest probability density over the
  relative values `(q,p) = (q_B - q_A, p_B - p_A)`, non-negative everywhere.

**Sharpness.** A scalar functional of `ρ_{A→B}` that is large when *A* localizes
*B*. Working definitions, roughly interchangeable for Gaussian states:
inverse phase-space variance `1/√(Var q · Var p)`, or purity `Tr ρ²`, or
negative entropy. "Dirac delta" = the singular limit (unattainable:
complementarity forbids simultaneous sharpness in `q` and `p`).

**Relative, not absolute.** The state carried is over *relative* coordinates. A
global position has no meaning for a lone perspective — matching the relational
stance and eliminating the god's-eye frame the measurement problem quietly
assumes.

## Postulates

- **P1 (Relational states).** All physical content is a set of pairwise
  knowledge states `{ρ_{A→B}}` over relative coordinates. There is no
  frame-independent absolute state.

- **P2 (Two-tier knowledge).** *Superseded framing — see
  `exploration/0003` and `mechanism/exploration/0002`.* Knowledge is of two
  kinds. **Actionable** knowledge (what a system can use to do something
  differently — forces, signals) is *c*-bounded. **Correlational** knowledge
  (the mutual consistency of the web) updates **instantaneously and nonlocally**
  when any edge is sharpened — this is not a propagation but the re-satisfaction
  of a global constraint. The two are separated by a firewall: the instantaneous
  update is non-signalling because it is random (outcome-dependent), so it
  averages away in every distant marginal. (The original "everything is
  *c*-bounded" reading was wrong to the posit; kept here only to mark the
  correction.)

- **P3 (Pairwise consistency, no global section).** `ρ_{A→B}` and `ρ_{B→A}`
  describe one relative coordinate related by parity; they must be the same
  physical relative state, and this holds on every overlap of the web. Crucially
  the family `{ρ_{A→B}}` is required to be **locally/pairwise consistent but need
  NOT be extendable to a single global joint distribution of definite values**.
  Demanding such a global joint (a "god's-eye picture") is exactly a local
  hidden-variable model (Fine's theorem) → Bell-local → falsified. Local
  consistency *without* a global section is the sheaf-theoretic signature of
  contextuality/nonlocality, and it is what makes the web quantum. See
  `testability/exploration/0003`.

- **P4 (Recursive consistency).** Knowledge composes along chains. When *A*
  knows *C* only through *B*, the relative coordinates add, `q_{AC}=q_{AB}+q_{BC}`,
  so uncertainties compose: for independent links
  `Var(q_{AC}) = Var(q_{AB}) + Var(q_{BC})` — a **variance-additivity / triangle
  inequality**. Chained knowledge is strictly **no sharper** than either link;
  the information analogue is the **data-processing inequality**
  `I(A:C) ≤ min(I(A:B), I(B:C))`. (Checked numerically in
  `mechanism/output/0001`.)

- **P5 (Measurement = coincidence).** An interaction that brings two systems to
  the same place is a split/merge event. It makes the relative coordinate sharp
  and updates the participating knowledge states by an optimal fusion rule
  (Gaussian/Bayesian in the classical reading; the QM state-update / Lüders rule
  in the quantum reading). This is the *only* place uncertainty is removed;
  between coincidences it can only grow (P4).

## What each postulate buys, and what it costs

- P1+P2 give the relational, no-absolute-truth picture and the *c*-bound "for
  free" — but P2 is precisely the locality half of Bell's premise.
- P3 turns "consistency" from a slogan into the quantum marginal problem, a hard
  but well-defined object with known monogamy constraints.
- P4 is the crisp, possibly-novel packaging of the user's recursive statement.
- P5 locates collapse in a physical event (coincidence) rather than in an
  observer's mind — the appealing move — but the *rule* used to fuse decides the
  fork.

## Open / underdetermined

Consistency (P3) constrains but does not *select* a state: the set of globally
representable marginal families is convex and large. P1–P5 as stated give a
kinematics and an update rule, **not** a unique dynamics or a derivation of the
Born weights. A dynamical principle (or the assertion of empirical equivalence
to QM) is still needed. Flagged, not hidden.
