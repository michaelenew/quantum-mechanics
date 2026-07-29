# Relational–Epistemic QM: a knowledge-first reading of measurement

**Thesis.** Take the viewpoint of a single particle *A*. Everything *A* can act
on is a probability distribution over the *relative* positions and momenta of
other particles — *A*'s **knowledge state**. Other particles are bumps in that
distribution, some sharp, some broad, none exactly a Dirac delta. Two
constraints govern these knowledge states:

1. **Locality of action** — *A* reacts only to what it knows; updates to its
   knowledge propagate no faster than *c* (standard relativistic causality /
   no-signalling).
2. **Consistency** — what *A* knows about *B* must be compatible with what *B*
   knows about *A*, and this composes recursively along chains
   *A → B → C*.

Under this reading the wavefunction is not a particle's position/momentum but a
particle's *belief about another particle's relative* position/momentum.
**Measurement is the exact coincidence of particles** (a split or a merge),
which is the event that makes a relative coordinate sharp and thereby collapses
the relative uncertainty two systems hold about each other.

## The central result (the fork)

The theory is forced to declare itself against **Bell's theorem**. Postulate 1
(local action) plus a *classical* reading of "knowledge" (beliefs about
pre-existing shared relative values) is exactly the local-realistic premise that
Bell rules out and that loophole-free experiments have falsified. So the idea
has exactly two consistent forms:

- **(A) Interpretation.** Read "consistency" quantum-mechanically (marginal
  representability + agreement-on-interaction) and treat knowledge as
  irreducibly perspectival. Then the theory is **empirically equivalent to
  standard QM** and sits beside Relational QM / QBism / quantum reference
  frames. It clarifies the measurement problem but predicts nothing new.

- **(B) Modification.** Insist that knowledge states are classical probability
  distributions over shared values updated by ordinary Bayes. Then the theory
  makes a **testable prediction: no Bell violation beyond the classical bound**
  — which is already contradicted by experiment.

The productive work is therefore to (i) state the idea precisely enough that
this fork is unavoidable, (ii) build out form (A) as far as it goes, and
(iii) hunt for any regime where form (A) still makes a *distinctive,
not-yet-tested* prediction (quantum-reference-frame effects are the leading
candidate). See `testability/`.

## Workstreams

| Folder | Question | State |
|---|---|---|
| `foundations/` | What are the precise objects and postulates? What is genuinely new vs. prior art? | Postulates P1–P5 stated; mapped to RQM, QBism, Spekkens, QRF, decoherence, marginal problem. |
| `mechanism/` | What *is* a measurement, mechanically? | Measurement = split/merge = sharpening of a relative coordinate. EPR commuting-observable refinement derived and checked (`output/`). |
| `testability/` | What would confirm or break it? | The Bell fork; a discriminator table separating interpretation-confirming from theory-breaking tests. |

Each folder has a `SUMMARY.md` with its current state, an `exploration/` with
numbered working notes, and (where relevant) an `output/` with checkable
artifacts.

## Honesty note

Most individual ingredients here already exist in the literature and are cited.
The contributions this repo aims at are (1) a single precise packaging of the
recursive-consistency postulate as **variance additivity / a data-processing
inequality on relative coordinates**, (2) the **EPR refinement** of the
split/merge mechanism (it is *relative* momentum that is uncertain; *total*
momentum is sharp by conservation), and (3) forcing the **Bell fork** into the
open as the theory's decisive test. Claims are qualified where evidence is
partial; speculative steps are labelled.
