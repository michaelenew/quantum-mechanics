# 0004 — Recursive consistency as a cocycle: press

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Pressing on P4. The user's statement is more than variance-additivity: it is a
compatibility law between paths in a graph. This note extracts the
mathematical content.

## The core structure

Model the world as a **web**: nodes are particles/events, edges are pairwise
knowledge states `ρ_{i→j}` over the relative coordinate `q_{ij}`. Composition
along a path chains these states.

**Recursive consistency, precisely:** for any two paths `π, π'` between the
same endpoints, the composed states along `π` and `π'` agree where they
overlap. Equivalently, composition **around any loop is trivial** (identity, or
identity-up-to-phase). This is a **cocycle condition** — the defining condition
of a Čech 1-cocycle on the graph.

- **Tree-shaped webs** (no loops): the cocycle condition is vacuous. Global
  sections always exist. Everything is classical.
- **Webs with loops**: the cocycle condition has content. Its failure around
  some loop = **holonomy** = frustration (classical) or contextuality
  (quantum).

The obstruction to a globally consistent state is the graph's **first
cohomology** `H¹(𝒢, ℱ)` of the constraint sheaf `ℱ`. This is exactly
Abramsky–Brandenburger's language for contextuality, arrived at here from the
user's posit directly.

## Frustration and contextuality: same shape, different composition

- **Classical frustration** (spin glasses): pairwise couplings around a
  triangle can be individually satisfiable but jointly incompatible. Around
  the odd loop `σ_{AB} · σ_{BC} · σ_{CA} = −1`. Verified numerically for the
  Z/2 case in `testability/output/0003` (frustration-free polytope = 1/3 of
  the cube, holonomy correlates with the obstruction).
- **Quantum contextuality**: pairwise-compatible measurement contexts consistent
  locally but globally non-extendable (Kochen–Specker, Fine, Bell).

**Framing claim** (target, not shown): these are the *same* mathematical
object — non-vanishing `H¹` of the constraint sheaf — with different
composition rules on edges. Classical composition (convolution of densities /
product on booleans) → frustration. Quantum composition (unitary /
symplectic on Wigner functions) → contextuality.

## What choice of composition rule buys

The consistency law fixes the *structure* (cocycle on a graph). The
*composition rule* on edges selects the specific theory:

| composition rule | resulting theory |
|---|---|
| convolution of probability densities | classical stochastic mechanics |
| symplectic composition of Wigner functions (or unitary conjugation) | quantum mechanics |
| non-signalling but non-classical polytope operations | general-probabilistic theories, PR-boxes |

This connects the posit to the GPT (general probabilistic theories) program
naturally: the composition rule is the theory. **Concrete open question:**
which composition rules are consistent with (a) unitarity of composition
around loops, and (b) min-relative-entropy projection as the update rule
(`0003`)? If exactly quantum is picked out, we have derived it from P4 + P5.

## What the cocycle framing predicts, cleanly

1. **Tree histories are classical.** Systems whose interaction history has no
   loops cannot show contextuality. In standard QM this is implicit
   (entanglement traces to a common past = loop); the cocycle framing makes
   it explicit and states it as an empirical prediction.
2. **Compatible observables on a triangle are classical.** Even on a loopy
   graph, if all pairwise observables commute (are compatible), the polytope
   of pairwise correlators equals the classical (Bell-Cirel'son-type)
   polytope. Verified in `testability/output/0003`.
3. **Contextuality requires choice.** The genuinely quantum obstruction only
   appears when each site has multiple, mutually incompatible observables to
   choose among (Kochen–Specker measurement contexts; CHSH inputs). So the
   "context" in "contextuality" is a **choice**, not just an interaction
   graph. This is a real localization of the source of quantumness.

## Quantitative content: variance-additivity is a Gaussian shadow

`Var(q_{AC}) = Var(q_{AB}) + Var(q_{BC})` is the cocycle for Gaussian classical
composition on a chain. The quantum version, when the intermediate carries
entanglement, allows sub-additivity for connected pairs (EPR steering / Reid).
The sharp form of P4 is composition-rule-dependent — this is *why* fixing the
composition rule fixes the theory.

## Status

- Cocycle framing: **confident** as a repackaging; it lines up exactly with
  Abramsky–Brandenburger's sheaf presentation of contextuality.
- Frustration ≅ contextuality as the same `H¹` structure: **plausible target,
  not yet a proof**. The parallel is standard in special cases; general
  equivalence I state as a goal.
- Composition-rule-selects-theory: **framing borrowed from GPTs**; the
  recursive-consistency lens naturally reproduces that program's premise.
  Not new by itself; the naturalness is the contribution.
- Tree-history → classical, compatible-observable → classical: **derived and
  numerically checked** in `0003`.
- Deriving quantum uniquely from P4 + P5: **the frontier**. Concrete route
  proposed; nothing shown.
