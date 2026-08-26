# 0147 — Multihit ported, and it bought nothing: the granularity was wrong

> **AI-generated, not peer-reviewed.** Code:
> `output/0136_multihit.py`. Sibling stone:
> `lucid-filter research/wall-correspondence/0048`.

## Where this came from

Item 2 (the graviton propagator) sits at the statistical floor. 0145
diagnosed **throughput**; 0146 recorded that the diagnosis was wrong —
the C kernel delivered ~30× and the answer did not move.

The filter was asked to find the engineering problem instead, and
found one: **estimation.** lucid 0048 showed that in a correlation
between two products of `k` noisy factors, the signal is identical at
every `k` while the error grows 7.8× from k = 1 to k = 8 — every extra
factor contributes fluctuation and none of it carries signal.
Rao-Blackwell (replace a sampled factor by its conditional mean;
exact, not approximate) bought **120×** in variance at k = 8, j = 7,
and — overturning my own expectation — **did not evaporate for stiff
factors**: ~8× even at v/m² = 0.005, because the gain comes from the
operator's **length**, not per-link noisiness.

The lattice name for that move is **multihit**. This ports it.

## The port

For a table-valued weight the conditional mean of a link has no closed
form — the six plaquettes touching a link do not collapse into one
effective staple the way a Wilson action's do — so it is estimated the
original way: extra local Metropolis hits on that link alone,
averaged. The checkerboard condition holds exactly here: the two
same-direction links in a plaquette sit at opposite parity, so a
whole (direction, parity) class can be integrated simultaneously.

L = 8, 400 configurations, 12 hits per link, 854 s.

| r | plain | multihit | var ratio |
|---|---|---|---|
| 1 | +0.000104 ± 0.000342 | −0.000126 ± 0.000355 | 0.93× |
| 2 | −0.000063 ± 0.000353 | −0.000430 ± 0.000348 | 1.03× |
| 3 | −0.000342 ± 0.000355 | −0.000543 ± 0.000351 | 1.02× |
| 4 | −0.000666 ± 0.000493 | +0.000066 ± 0.000506 | 0.95× |

**0.98× on average.** Bias check (the site operator's six plaquettes
share links, so the substitution is exact per plaquette and
approximate for their product): worst disagreement **1.0σ** — the
estimator is fine, it just does nothing.

## Why — and it is not a failure of the filter's law

Rao-Blackwell rests on

    Var(X) = Var(E[X|Z]) + E[Var(X|Z)]

and removes **only the second term.** Conditioning a link on
everything else puts almost the entire field into `Z`. The site
operator is then very nearly a function of `Z` alone, so
`Var(E[X|Z]) ≈ Var(X)` and there is nothing left to take.

> The variance lives in the part being **conditioned on**, not the
> part being integrated out. lucid 0048's law is correct; a **link is
> the wrong unit.**

That is a sharper statement than "the fix didn't work," and it names
its own successor: make `Z` small. Freeze the spatial links on a set
of time slices and the sub-lattices between them interact *only*
through those links, so operators in different blocks become
conditionally independent and their sub-averages multiply. `Z` is then
a boundary rather than a neighbourhood. That is 0137.

## What is banked

- The multihit estimator itself, gated and **unbiased** (≤1.0σ) — it
  is correct machinery, reusable at any granularity.
- A measured variance budget saying where the item-2 error actually
  lives, which is what 0145's guess got wrong twice over.
- A discipline note: this is the second wrong diagnosis of item 2 in
  a row. Both were fixed by **measuring the decomposition** rather
  than reasoning about the mechanism.
