# 0004 — Bell as informative checkpoint, not settled wall

Written in the user's stance: experiment is the only authority; theorems
constrain but do not settle; and passing experiment is survival, not truth.
Bell is treated here as a strong, useful constraint on the *shape* of any
theory — not a foreclosure of thinking.

## What Bell strictly forbids

Bell's theorem is a mathematical result given four premises:

- **(L) Local causality**: outcomes depend on hidden variables in their past
  light cone only.
- **(MI) Measurement independence**: measurement setting choices are
  probabilistically independent of the hidden variables.
- **(OI) Outcome independence**: given hidden variables, Alice's outcome does
  not depend on Bob's outcome.
- **(R) Realism / counterfactual definiteness**: outcomes of unperformed
  measurements are well-defined.

`(L) ∧ (MI) ∧ (OI) ∧ (R) ⇒ |S| ≤ 2`. Loophole-free experiments show
`|S| > 2` with high statistical significance. So at least one of the four
fails. Bell tells us *which set of premises* is incompatible with experiment;
it does not tell us which one to give up.

## Where the consistency-first theory sits

Under the reframing:
- **(R) is dropped.** No global joint distribution of definite counterfactual
  values (`foundations/0003`).
- **(OI) is dropped.** Outcomes are correlated through global consistency, not
  through common past values.
- **(L) is preserved for actionable knowledge (c-bounded)**; relaxed for
  correlational knowledge, which updates instantaneously as global-constraint
  re-satisfaction. The randomness firewall keeps this non-signalling.
- **(MI) is preserved** (no superdeterminism required).

This is enough to reproduce Bell violations without conflict with experiment,
and it is arguably more parsimonious than interpretations that keep (R) in
some form (Bohmian pilot waves, many-worlds).

## Escape routes that Bell does not close

Bell is not a wall against all imaginable alternatives. Live minority positions
that formally evade the theorem:

- **Superdeterminism** (Palmer; Hance & Hossenfelder). (MI) is false;
  measurement settings are correlated with hidden variables. Preserves (L)
  and (R). Rigorous mathematical escape; philosophically contentious.
- **Retrocausality** (Price, Wharton, Sutherland). Time-symmetric hidden
  variables; future measurement choices influence past hidden variables.
  Preserves (L) and (R) in local frames.
- **Contextuality of the observer**. The setting choice is entangled with the
  observer's state; "free choice" is a limiting assumption.

The consistency-first framing is **naturally compatible with retrocausality**:
if the fundamental law is fixed-point global consistency, temporal direction
is not privileged — consistency doesn't care which way time flows. Worth
exploring separately (own note; not done here).

## What the theory does *not* claim

Being honest about survival-vs-truth cuts both ways:

- Not claiming to violate no-signalling. Experiment forbids it; theory
  respects it (via the randomness firewall of `foundations/0003`).
- Not claiming to violate Tsirelson (`|S| > 2√2`). Experiment is consistent
  with `2√2`; the theory currently permits up to `4` (PR-boxes) at the level
  of the consistency law alone. The frontier work is to tighten this via
  P4/MRE (`testability/0003`, `foundations/0004`), *not* to predict a value
  above `2√2`.
- Not claiming Bell is "wrong." Claiming that Bell's theorem rules out one
  specific class of theories, and the consistency-first theory is not in
  that class.

## What would move Bell from checkpoint to fully settled

Given the user's cautions, being explicit:
1. Every premise axiomatized in a shared, minimal, metaphysics-free language.
2. Every escape route ruled out experimentally (superdeterminism,
   retrocausality, observer contextuality). Currently *cannot* be — most are
   unfalsifiable in principle.
3. A canonical theorem statement without hidden philosophical commitments
   (some critics argue Bell's derivations quietly assume a specific
   measure-theoretic frame that isn't neutral).

None of these hold. Bell is thus an exceptionally strong constraint on the
*form* of viable theories, not a proof of their content.

## Practical conclusion

Bell is used here as: "any theory must give up at least one of L/MI/OI/R, in
a way compatible with observed CHSH violations and no-signalling." The
consistency-first theory pays that price by giving up (R) and (OI) — the
minimal, least-metaphysically-invasive cut compatible with everything else the
posit says. If downstream we find pressure to also relax (L) or (MI) in some
regime, we do so with open eyes and label it clearly.

## Testable consequences of taking Bell as a checkpoint

- If somebody demonstrated a super-Tsirelson correlation (`|S| > 2√2`) with
  no-signalling intact, standard QM would need modification. The
  consistency-first theory currently permits it at the level of P1–P3 alone;
  P4/MRE-projection is the candidate mechanism forbidding it. So a
  super-Tsirelson experiment is a *simultaneous* test of both standard QM
  and the strength of P4.
- Conversely, if a P4-based derivation of exactly `2√2` (à la information
  causality) succeeds, then observing `2√2` becomes an *explanation* rather
  than a raw fact — a genuine advance.
