# 0003 — Consistency-first ontology (the corrected core)

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Supersedes the locality-first framing of `0001` P2. This note takes the posit on
its own terms: **mutual consistency is the fundamental law, and it is nonlocal.**

## The reframe

Reality is not a set of particles carrying independent states. It is a **web**:
nodes = particles, edges = pairwise knowledge distributions over relative
coordinates, on the graph of everything that has ever interacted (directly or
indirectly). The one law is:

> The web must be mutually consistent, everywhere, at all times.

A configuration of the web that satisfies this is a **fixed point** of the
consistency constraint. "Physical state" = a consistent web. Dynamics and
collapse are then not separate postulates; they are what re-satisfying the
constraint *looks like* when an edge changes.

## Nonlocality is the globality of the constraint (not a signal)

When a measurement sharpens one edge, the whole connected component must
re-settle into a consistent configuration. This is instantaneous — and there is
no paradox, because **nothing propagated**. There is no "speed" to a constraint;
there is only whether the configuration satisfies it. The distant particle's
knowledge state changes at once because it was never independent — it was a
coordinate of the same fixed-point object.

This is the key move that dissolves the c-vs-instantaneous tension:

- **Correlational knowledge** = the web's consistency. Instantaneous, nonlocal,
  because it is global-constraint satisfaction.
- **Actionable knowledge** = what a system can use to behave differently.
  *c*-bounded, because using the correlation to *do* something requires a
  classical record to be carried at ≤ *c*.

The firewall between them is randomness. The instantaneous update to a distant
edge depends on the measurement *outcome*, which is random; average over the
outcome and every distant marginal is unchanged (law of total probability /
no-signalling). So the nonlocal update is real but **provably undetectable
locally** — exactly the posit's "small / random / very-hard-to-detect."

## The update rule: minimum-relative-entropy projection

The posit says knowledge combines "Bayesian-optimally, injecting no additional
uncertainty, into the most coherent picture." That is not vague — it names a
specific operation:

> **Collapse = project the current web onto the manifold of configurations
> consistent with the newly sharpened edge, minimizing relative entropy.**

`W_new = argmin_{W ∈ 𝓒'} D(W ‖ W_old)`, where `𝓒'` is the consistency manifold
intersected with the new sharp-edge constraint. Minimum-relative-entropy update
(Shore–Johnson) is the unique rule that (i) reduces to Bayes when the constraint
is "event E occurred," (ii) changes nothing not forced to change ("no additional
uncertainty injected"), and (iii) is order-independent. All three are the
posit's own desiderata. Because `𝓒'` is a **global** manifold, the projection
moves the whole web at once — the instantaneity falls out of the same principle.

*Open, do-not-claim-yet:* whether the **quantum** version (minimize quantum
relative entropy `D(σ‖ρ)=Tr σ(ln σ−ln ρ)` over the consistency manifold)
reproduces the Lüders/Born update. There are suggestive connections (minimal
disturbance, Petz recovery) but I have not shown equivalence. This is a concrete
target: if it reproduces Lüders, the posit *derives* collapse; if it deviates,
that deviation is a prediction.

## The load-bearing subtlety: consistent, but no global section

"Most coherent global picture" is a trap. If the web is always extendable to a
*single global joint distribution of definite values*, then by Fine's theorem it
is a local hidden-variable model → Bell inequalities hold → falsified. So the
consistency demanded must be the weaker, stranger kind:

> **Every local patch (every overlap, every triangle) is consistent, yet there
> is no global joint state that all patches are marginals of.**

No god's-eye view — which the posit wanted anyway. This "locally consistent,
globally non-extendable" structure is exactly quantum contextuality in the
sheaf language (Abramsky–Brandenburger). So the recursive triangle constraint
(P4) must be read as *local-patch* consistency, and the theory must actively
**forbid** the global section. Getting this calibration exactly right is the
whole game (see `testability/exploration/0003` and `output/0002`).

## Status

- Reframe (consistency-first, nonlocal, instantaneous-but-non-signalling):
  faithful to the posit and internally coherent. **Confident as a framing.**
- Min-relative-entropy as the update: strong fit to the stated desiderata;
  classical version solid, quantum equivalence **open**.
- "Local consistency without global section = quantumness": this is the sharp,
  possibly-generative claim. Demonstrated concretely for CHSH in
  `testability/output/0002`. Whether it *singles out* the quantum set (vs.
  super-quantum) is the frontier — **open**.
