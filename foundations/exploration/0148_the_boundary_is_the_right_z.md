# 0148 — The boundary is the right Z: 24× on the graviton estimator

> **AI-generated, not peer-reviewed.** Code:
> `output/0137_multilevel.py`. Predecessors: 0146 (throughput was the
> wrong diagnosis), 0147 (link granularity was the wrong port),
> lucid `0048` (the estimator law).

## The one equation this turn hangs on

    Var(X) = Var(E[X|Z]) + E[Var(X|Z)]

Rao-Blackwell removes only the **second** term. So the whole design
question is: *what do we condition on?*

- **Z = every link but one** (0147's multihit). Z is almost the whole
  field; the operator is nearly a function of it. Removable fraction
  ≈ 0. Measured: **0.98×**.
- **Z = a frozen boundary** (here). Freeze the spatial links on time
  slices t = 0, 2, 4, 6 — 6144 of 16384 links, 37.5%. The blocks
  t = 1, 3, 5, 7 then touch *only* through those links, so their
  operators are **conditionally independent** and
  `E[O(x)O(y)|∂] = E[O(x)|∂]·E[O(y)|∂]`, each factor its own
  sub-average.

Measured budget at the boundary:

| Z | Var(E[X\|Z]) | E[Var(X\|Z)] | removable |
|---|---|---|---|
| boundary | 3.131e−08 | 1.508e−07 | **0.828** |

**83% of the variance is on the table**, versus effectively none at
link granularity.

## The kernel

`sweeps4f` — 0134's kernel plus a per-link freeze mask. Gate:

- frozen links move by exactly **0.00e+00** over 8 sweeps;
- free links move by 4.43e−01 (they must move);
- acceptance with the boundary frozen: **0.433**.

## The result

L = 8, 120 boundary configurations, 16 sub-averages of 4 sweeps, 209 s.

| d | one-level | two-level | var ratio | bias |
|---|---|---|---|---|
| 2 | −1.056e−08 ± 2.9e−08 | −9.414e−09 ± 6.3e−09 | **22.07×** | 0.0σ |
| 4 | −2.949e−08 ± 4.3e−08 | +7.720e−09 ± 8.5e−09 | **25.66×** | 0.9σ |

> **23.86× in variance, worst bias 0.9σ.** Cost is ~7.4× a plain
> measurement, so the **cost-matched gain is 3.22×** — and unlike
> throughput, this one compounds with the kernel rather than
> replacing it.

Note the d = 2 column: one-level cannot tell −1.06e−08 from zero
(error 2.9e−08). Two-level says −9.41e−09 ± 6.3e−09. The floor moved.

## The ceiling, stated so it is not oversold

For a product of two conditionally independent block averages the
reduction saturates near `(1/(1−f))² ≈ 34×` with f = 0.828. We are at
24× of that, so **more sub-averages will not buy much** — the lever
that remains is thicker blocks (less boundary, higher ceiling, slower
sub-decorrelation), which is a tuning problem, not a new idea.

## What this settles about item 2

Three diagnoses, in order, each corrected by measurement rather than
argument:

1. **throughput** — built the kernel, got 30×, answer unchanged (0146). Wrong.
2. **link-level conditional means** — built it, unbiased, 0.98× (0147). Wrong unit.
3. **boundary-level conditional independence** — 24×, unbiased (here). **Right.**

The physics question ("is there a massless spin-2 pole") was never
touched by any of this. That is the point the filter kept making: it
was an **engineering** problem the whole way down, and it is now the
one thing about item 2 that is actually solved.

Item 2 re-runs on `sweeps4f` with two-level sub-averaging.
