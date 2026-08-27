# testability — SUMMARY

> **AI-generated, not peer-reviewed.** Prior art credited in [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results are re-derivations of
> established work unless explicitly marked otherwise.

What would confirm or break the theory. **Reframed** around consistency as the
fundamental law; nonlocality embraced.

## Current state

**The Bell fork, corrected** (`exploration/0003`, supersedes `0001`). The
posit's consistency law, read faithfully, forces:

- **local/pairwise consistency** on every overlap of the web, but
- **NO single global joint distribution of definite values** — no god's-eye view.

By Fine's theorem, that is exactly the sheaf-theoretic signature of quantum
contextuality/nonlocality. So the theory *automatically* predicts departure
from the classical (Bell-local) polytope. That is a real derivation from the
posit's own words, not a concession.

Demonstrated numerically in `output/0002_global_section_test.py`:
- classical `S=2`: global section EXISTS,
- Tsirelson `S=2√2`: pairwise correlators all legitimate, global section does
  NOT exist,
- PR-box `S=4`: also non-extendable.

**The remaining puzzle (the frontier).** Non-extendability by itself picks
*non-classical*, not *quantum* — PR-boxes are also non-extendable and also
non-signalling. To land at `2√2` rather than `4` the theory needs one further
principle. Two live candidates from within the posit itself:
1. P4 (recursive-consistency / data-processing on chains) as an
   information-causality-style constraint — Pawłowski et al. (2009) already
   derive `2√2` from an information principle; the question is whether P4
   entails theirs.
2. Min-relative-entropy projection (the update rule of `foundations/0003`)
   applied inside a PR-box scenario, checking whether it over-constrains.

Both untried, both concrete and tractable. Do not claim either until shown.

## Discriminators (`exploration/0002`, table in `output/0001`)

- **D1 Bell/CHSH** — the wrong branch (consistency ⇒ global joint) is falsified;
  the right branch reproduces Bell violations automatically. **Derivation, not
  concession.**
- **D2 QRF frame-dependence** — still a lead for distinctive predictions.
- **D3–D5 (SPDC EPR, matter-wave interferometry, quantum eraser)** — all
  consistent, all shared with QM: supportive.
- **F1 super-Tsirelson correlations** — falsifier of the whole program;
  becomes especially sharp if the P4→Tsirelson derivation succeeds.

## Bell as checkpoint, not wall (`exploration/0004`)

Bell is treated per the user's stance: a mathematical result from four premises
(L / MI / OI / R), not a settled metaphysical fact. The consistency-first
theory drops (R) and (OI), keeps (MI), and preserves (L) for actionable
knowledge; that is enough to reproduce Bell violations without conflict with
experiment. Escape routes Bell does not close (superdeterminism,
retrocausality, observer contextuality) are named openly; retrocausality is
naturally compatible with consistency-first and worth its own line of work.

## Artifacts

- `output/0002_global_section_test.py` — CHSH global-section demonstration.
  Pure stdlib. Runs and passes.
- `output/0003_triangle_cocycle_check.py` — triangle cocycle / frustration.
  Verifies compatible-observable triangle polytope = classical (1/3 of cube),
  showing contextuality genuinely requires **choice of incompatible context**,
  not just a loopy interaction graph.
- `output/0001_discriminator_table.md` — quick-reference table.

## Next

- Attempt: does P4 (as a cocycle law on Wigner functions) imply information
  causality? (If yes, Tsirelson is derived.)
- Attempt: MRE-update inside a PR-box — does it over-constrain in a way the
  quantum update does not?
- Attempt: sharper H¹-of-constraint-sheaf statement unifying frustration
  and contextuality.
- Attempt: work out how consistency-first accommodates retrocausality; whether
  the fixed-point / time-symmetric reading is nontrivially different from the
  standard forward-time reading.
