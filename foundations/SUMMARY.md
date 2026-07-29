# foundations — SUMMARY

State of the formalization of the knowledge-first reading of measurement.

## Current state

Five postulates fix the theory's kinematics and update rule
(`exploration/0001`):

- **P1 Relational states** — all content is pairwise knowledge states
  `{ρ_{A→B}}` over *relative* coordinates; no absolute frame.
- **P2 Local action** — a system acts only on its own knowledge; updates are
  *c*-bounded (relativistic causality / no-signalling).
- **P3 Pairwise consistency** — `ρ_{A→B}` ↔ `ρ_{B→A}` by parity; the whole
  family must be globally representable = the **quantum marginal problem**.
- **P4 Recursive consistency** — relative coordinates add along chains, so
  uncertainties compose: **variance additivity** `Var(q_{AC})=Var(q_{AB})+Var(q_{BC})`
  / **data-processing inequality**. Chained knowledge is no sharper than any link.
- **P5 Measurement = coincidence** — a split/merge makes a relative coordinate
  sharp and fuses knowledge states (Bayesian in the classical reading, Lüders in
  the quantum reading). The sole source of uncertainty reduction.

Each object has two candidate readings (classical density vs. quantum
reduced/relative state); the choice is deferred to the Bell fork in
`testability/`.

## Positioning (`exploration/0002`)

Inherited from prior art: relational stance (RQM), epistemic/Bayesian state
(QBism, Spekkens), decoherence (Zurek), relative-frame states (QRF/Giacomini).
Contributed here: P4 as variance-additivity/DPI; the EPR refinement of the
split/merge mechanism; forcing the Bell fork; flagging QRF frame-dependence as
the one plausibly-distinctive prediction.

## Known gaps

- P1–P5 give kinematics + an update rule, **not** a unique dynamics or a
  derivation of the Born weights. Consistency constrains but does not select a
  state. This is the open frontier.
- The classical vs. quantum reading of `ρ_{A→B}` is unresolved until the fork.

## Next

Formalize P4's information version (DPI with the exact monotone) and check
whether P3's monogamy constraints alone reproduce any nontrivial QM bound
(e.g. Tsirelson) — if so, that would upgrade "interpretation" toward "derivation."
