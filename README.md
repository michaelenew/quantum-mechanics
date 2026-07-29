# Relational–Epistemic QM: a knowledge-first, consistency-first reading

**Thesis.** Take the viewpoint of a single particle *A*. Everything *A* can act
on is a probability distribution over the *relative* positions and momenta of
other particles — *A*'s **knowledge state**. Other particles are bumps in that
distribution; none are exact Dirac deltas. **Mutual consistency** of the whole
web of pairwise knowledge distributions is the fundamental law. It is nonlocal
by nature: sharpening one edge instantaneously re-settles the whole connected
component. Under this reading, **measurement is the exact coincidence of
particles** (a split or a merge) — the event that makes a relative coordinate
sharp and triggers the global re-projection.

## The two-tier structure that reconciles instantaneous updates with relativity

Knowledge splits into two kinds:

- **Actionable knowledge** — what a system can use to *do* something
  differently (forces, signals). *c*-bounded, standard relativity.
- **Correlational knowledge** — the mutual consistency of the web. Updates
  **instantaneously, nonlocally**, because it is the satisfaction of a global
  constraint, not a propagation. Non-signalling because outcomes are random
  and average to zero in every distant marginal.

That firewall is the resolution of the c-vs-instantaneous puzzle from *inside*
the posit.

## The central derivation

The consistency law, read faithfully, requires that the web be **locally
consistent on every overlap** but need **not** admit a **single global joint
distribution of definite values**. By Fine's theorem, that is exactly the
sheaf-theoretic signature of quantum contextuality/nonlocality — and it
automatically forces departure from the classical Bell polytope. So the
posit's own "no absolute source of truth" *derives* the fact that reality
must be non-classical.

Demonstrated numerically in `testability/output/0002_global_section_test.py`:
Tsirelson (S=2√2) correlators are pairwise legitimate but have no global
section; classical (S=2) correlators have one.

## The frontier

Non-extendability alone rules classical out but does not pick *quantum* over
*super-quantum* (PR-boxes are also non-extendable). Two live candidates inside
the posit that might tighten the bound from 4 to 2√2:

1. **P4 (recursive consistency) as an information-causality-type principle.**
   Pawłowski et al. (2009) derive `2√2` from an information-processing axiom;
   whether P4 entails it is a concrete open theorem.
2. **Min-relative-entropy projection (the P5 update rule) inside a PR-box
   scenario** — check whether it over-constrains and forbids super-Tsirelson
   correlations.

Neither shown; both concrete and tractable. See `testability/`.

## Workstreams

| Folder | Question | State |
|---|---|---|
| `foundations/` | Postulates and formal objects. | P1–P5 reframed around consistency-first (`exploration/0003`). |
| `mechanism/` | What *is* a measurement, mechanically? | Coincidence / split-merge + EPR refinement + a dilution law from monogamy (`exploration/0002`). |
| `testability/` | What confirms or breaks it? | The Bell fork reframed (`exploration/0003`); non-classicality now a derivation; quantum-selection open. Numerical demonstration in `output/0002`. |

Each folder has a `SUMMARY.md` (current state), `exploration/` (numbered notes,
later = more recent), and where applicable `output/` (checkable artifacts).

## Honesty note

- **Contributed here (with real confidence):** the two-tier resolution of the
  c-vs-instantaneous puzzle; consistency-first packaging that turns "no
  god's-eye view" into the sheaf-theoretic non-extendability condition and
  *derives* non-classicality from the posit; the dilution reading of
  decoherence; the EPR refinement of the split/merge mechanism.
- **Proposed, not shown:** that P4 or MRE-projection tightens the bound to
  Tsirelson (would upgrade the theory from re-framing to partial derivation).
  Do not cite as fact.
- **Inherited (explicitly named):** the relational stance (RQM), epistemic
  reading (QBism, Spekkens), QRF formalism, decoherence, Fine's theorem,
  Abramsky–Brandenburger sheaves, information causality. Each labelled in
  `foundations/exploration/0002`.
