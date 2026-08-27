# 0008 — The kernel from stat-tracker: separate the distribution from the trust

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

The user's sibling project (`michaelenew/stat-tracker`, in
`adaptive-random-walk-filter/`) built a tuning-free adaptive filter from
purely information-theoretic reasoning. Three of its findings port directly
to this project's theory, in one case exactly. This note extracts them.

## Kernel 1 — Distribution vs. trust vs. influence: three levels, not one

The stat-tracker's central move: **separate three things that everyday
Bayesian statistics conflates**.

- **Distribution.** What I currently believe about the underlying process
  (mean, variance) — the posterior.
- **Trust.** How much confidence I have in my *model* (the parameters
  `Q, σ², φ_P, φ_M, s_P, s_M` that govern how the distribution should evolve).
  This is meta-uncertainty: not uncertainty in the state, but uncertainty in
  the structure generating the state's dynamics.
- **Influence.** How much a new data point should be allowed to move the
  estimator. Turns out to be **the square root of the trust** (see kernel 2).

The three-way split is engineered, not academic. `fit()` learns the trust
level from history; `filter()/update()` uses that trust to allocate
influence. The two operations use disjoint machinery, and conflating them
produces the known Kalman pathologies (drift, jump lag, sensitivity to
outliers).

**Translation to this project.** A knowledge state `ρ_{A→B}` carries all
three of these implicitly and, in standard QM, they are collapsed into a
single density-matrix object. Making the split explicit gives us:

| stat-tracker | consistency-first QM |
|---|---|
| distribution over state | the "mean" content of `ρ_{A→B}` |
| trust in the model (fitted noise/persistence) | meta-uncertainty in the *dynamics* / effective Hamiltonian / commutation structure |
| influence a data point earns | how strongly a coincidence event should reshape the connected component of the web |

Standard QM assumes the trust structure (the Hamiltonian, the observables,
the commutators) is *given* and fixed. But in a truly information-first
theory, the trust structure is itself a learned pairwise property of the
web. This is not a wild claim: quantum reference frames already make the
"commutation structure" of an observable frame-dependent (Giacomini et al.
2019); effective field theories are exactly this learned trust structure at
different scales; and quantum error correction routinely models "uncertainty
about the noise channel" as a meta-uncertainty over an unknown super-operator.

The engineering payoff of the split: decoherence becomes surgical to
describe — the environment *erodes trust* in an edge's ρ without necessarily
changing its mean. Recovery / echo protocols become "trust rebuilding"
rather than mysterious state undoings.

## Kernel 2 — Influence = √(information): the classical shadow of the Born rule

Stat-tracker's `theory/02` proves and verifies to machine precision, for the
scalar random-walk-plus-noise filter at steady state:

    influence weight  a_k     ∝  (1 - K)^k
    incremental information  Δ_k  ∝  (1 - K)^{2k}
    =>                 a_k  ∝  √(Δ_k)

**Information is an energy; influence is an amplitude.** Confirmed here in
`output/0002_amplitude_shadow.py` across `q ∈ {0.005, 0.05, 0.5, 5.0}` — the
ratio `a_k / √Δ_k` is a constant to full float precision (verified in the
run).

This is precisely the amplitude-vs-probability relationship the Born rule
imposes in QM (`P = |ψ|²`) — showing up here in a purely classical Bayesian
tracking problem, with no quantum content anywhere. It is not a theorem
"in disguise," it is the same theorem: on any manifold where information
composes quadratically (Fisher metric), the natural composable object is a
square-root — the amplitude.

**Consequence for the theory (real content).** The Born rule is not a
QM-only axiom. It is the *forced* rule for how any coherent-inference
machinery must convert additive log-evidence into linear composable
sensitivity. This lines up with existing arguments in the reconstruction
literature (Wootters 1981 identified the Fubini–Study metric on QM states
with the Fisher–Rao metric on classical probability distributions via the
√-substitution) but is here demonstrated *from the outside*, in a
random-walk filter completely unaware of QM. That is stronger evidence than
a QM-internal derivation would be.

## Kernel 3 — "Trustworthy" is contextual (evidence against the alternatives, not for the hypothesis)

Stat-tracker's `theory/04` refuses to accept nats as absolute. Its
proposed definition:

    Λ_h^robust(m) = min_{h' ∈ ℋ \ {h}} KL( P_h^(m) || P_h'^(m) )

The "trustworthy" evidence for hypothesis `h` is the evidence that survives
minimisation over the alternative set `ℋ`. Trust in `h` depends on which
alternatives are in play.

**This is contextuality, in classical Bayesian dress.** In QM: a measurement
outcome is defined only relative to a measurement basis (Kochen–Specker).
There is no context-free "the outcome." In stat-tracker: there is no
context-free "the evidence"; you must name the alternative set for a nat
count to mean anything.

**Consequence for the theory.** Our sheaf-theoretic reading of
contextuality (`0004`) says "locally consistent, no global section." The
stat-tracker's operational definition says the same thing in the language of
evidence: local per-context evidence is well defined; a globally
context-independent "amount of evidence for h" is not. These are the same
statement, but the stat-tracker version is a *usable engineering
definition* that runs today.

## What to actually do with these kernels

Ordered by how immediately they change the repo:

1. **Adopt the three-level split (distribution / trust / influence) as
   primitive.** Rewrite the definition of the knowledge state `ρ_{A→B}` in
   `foundations/0001` to carry an explicit "trust" scalar alongside the
   density, and note that "influence" (how strongly it composes) is
   √trust. Small change, big clarity.
2. **Take the Born rule off the axiom list.** The reconstruction route
   (`0007`) currently lists Born-like axioms implicitly via Fisher/Bures
   metric uniqueness. With Kernel 2, we can point at "amplitude structure
   = √(information) is forced by any Fisher-metric optimal inference" as
   the reason — one fewer axiom to postulate, one more thing to derive.
3. **Reframe decoherence as trust erosion, not distribution destruction.**
   `mechanism/0002` already reads decoherence as *dilution* of correlation
   across environmental partners. The trust-language makes this exact: the
   distribution's mean may be unchanged; its trust drops toward the
   uniform-prior floor as environmental partners accumulate.
4. **Use "trustworthy = evidence-against-alternatives" as an operational
   handle on P3.** Our "no global section" is abstract; stat-tracker's
   `Λ^robust` is a concrete quantity that computes contextuality-witness
   values for named hypothesis sets. This is the most tractable place to
   look for an engineering-usable contextuality test.

## Status

- The three-level split: **borrowed wholesale from stat-tracker**; the port
  to consistency-first QM is a framing claim, well-motivated, worth doing.
- Influence = √(information) as classical shadow of the Born rule:
  **verified computationally in `output/0002` to full float precision** on
  the stat-tracker Kalman model; the *general* claim that the Fisher-metric
  Born-rule structure is derivable rather than postulated is standard
  (Wootters 1981), so we do not claim novelty — but the stat-tracker
  witness gives it a form the reconstruction route can lean on.
- Contextual "trustworthy" as classical shadow of quantum contextuality:
  **structural analogy**, sharpened here into an operational proposal;
  proving equivalence to sheaf-contextuality is open.
- Related to but not identical to purification (`0007`): purification says
  mixed states come from pure states + partial trace; the trust split says
  the *dynamics* itself carries meta-uncertainty. Complementary, not
  redundant.
