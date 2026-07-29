# 0003 — The Bell fork, re-read (supersedes 0001)

`0001` treated locality as the load-bearing axiom and used Bell as a wall. That
inverted the posit. Consistency is fundamental; nonlocality is embraced. Here
is the corrected reading, and its sharpest testable content.

## Fine's theorem, said in our language

Fine (1982): a set of pairwise/marginal probability distributions in a Bell
scenario admits a **single global joint distribution of definite values** iff
all corresponding Bell/CHSH facet inequalities hold. Equivalently:

> **global section ⇔ Bell-local ⇔ local hidden variables.**

So a theory that demands the pairwise web is always extendable to one global
joint state is committed to Bell inequalities and is dead on arrival.

The posit's consistency law must therefore be read as **local/pairwise
consistency *without* the global section**. This is not a workaround; it is what
the posit already wanted ("no absolute source of truth"). We now have the
mathematical name for it: it is *precisely* quantum contextuality/nonlocality in
the sheaf-theoretic sense (Abramsky–Brandenburger). Consistency is exact on
every overlap; there is no god's-eye joint.

## The fork, re-drawn

- **Wrong branch (kill this reading up front):** "consistency" = the web is
  always extendable to a single global joint of definite values. → forces
  `|S|≤2` → falsified by loophole-free Bell tests. Do not adopt.
- **Right branch (the posit's actual content):** "consistency" = every pairwise
  and every overlap distribution agrees where they meet, with **no requirement
  that they come from a single joint state**. Nonlocality is not a bug; it is the
  globality of the constraint (`foundations/0003`). This branch:
  - reproduces Bell violations (no global section available to enforce the
    inequality),
  - is non-signalling (the instantaneous update is outcome-random; averages away
    in every distant marginal),
  - matches "small / random / very-hard-to-detect" from the posit,
  - is a genuine reframing, not a strawman.

## The demonstration

`output/0002_global_section_test.py` shows the calibration numerically:

- **Classical (S=2):** every |E|≤1; global section EXISTS.
- **Tsirelson (S=2√2):** every |E|≤1; global section does NOT exist — yet the
  pairwise correlators are all individually realizable. *Locally consistent,
  globally non-extendable.*
- **PR-box (S=4):** same non-extendability; also non-signalling.

So the posit's "consistency + no absolute truth" successfully forces us **out
of the classical polytope** — automatically. That is a real derivation, not a
concession.

## The remaining puzzle (the real frontier)

Non-extendability alone does not pick the quantum set from the larger
no-signalling polytope: PR-boxes also lack a global section and also don't
signal. Something more is needed to hit `2√2` rather than `4`.

Candidates worth exploring, none of which I claim to have shown:

1. **Recursive-consistency chains (P4).** The variance-additivity /
   data-processing structure imposed on chains of edges may cost enough
   "information budget" to forbid PR-correlations. If we can express PR-box
   correlations as a triple-overlap that violates a data-processing inequality
   the posit demands, the posit derives `≤ 2√2`. Tsirelson-from-DPI-type
   arguments exist in the literature (information causality — Pawłowski et al.
   2009 — derives `2√2` from an information-processing principle); the posit's
   P4 is a candidate variant of that principle.
2. **Min-relative-entropy projection (`foundations/0003`).** The specific update
   rule may be incompatible with PR-correlations even when they satisfy raw
   pairwise consistency, because updating one edge to a sharp value with the
   MRE rule might over-constrain the rest of the web. Concrete calculation:
   attempt an MRE update inside a PR-box scenario and check for
   inconsistency. **Untried.**
3. **The recursive triangle A → B → C.** Non-extendability plus the parity
   requirement on triples may already tighten the bound below PR. Also untried.

The honest reading: the corrected posit **derives that reality is non-classical**
from consistency + no-global-truth alone; whether it **derives that reality is
quantum (not super-quantum)** turns on whether P4/MRE tighten the bound to
Tsirelson. That is the concrete, tractable next question. It is a real theorem
to try to prove or disprove.

## Testable content — updated

- **Confirmed automatic:** rejection of the classical polytope (the theory
  cannot avoid predicting Bell violations, given its own consistency law).
- **Predicted, tightening pending:** no-signalling; no super-Tsirelson
  correlations if either P4-as-information-causality or MRE-projection
  succeeds in constraining the set to the quantum one. Existing experimental
  data is consistent with `|S| ≤ 2√2`, so if the derivation goes through it
  becomes an *explanation* — and if it can be perturbed (parameterize a
  weakening of P4 and predict a small permitted super-Tsirelson excess), it
  becomes a *live experimental target* at the extreme edge of Bell tests.
- **Falsifier of the whole program:** an observed |S| > 2√2 with no-signalling
  intact would break the min-relative-entropy projection story. None seen.
