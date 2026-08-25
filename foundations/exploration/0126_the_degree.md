# 0126 — The degree: why alternatives are summed, from the budget

Code: `output/0114_the_degree.py`.

lucid 0034 closed the composition rule (amplitudes multiply in ℂ)
and named the one clause it assumed rather than measured: **why the
amplitudes of alternatives are added.** This closes it, and it needs
no new postulate — it is the band budget again.

## 1. The bridge: the interference hierarchy measures the degree

Sorkin's I_k is the k-th finite difference of the measure over k
disjoint bundles of histories. A measure that is a form of **degree
d** in the amplitude has I_{d+1} = 0 and I_d ≠ 0. So the hierarchy
*measures the degree* — and "alternatives are summed" is exactly
"the degree is 2":

> μ(S) = (Σ_{i∈S} a_i)²  **is** the sum rule, and nothing else is.

## 2. This program's own ledger has I₃ = 0 pointwise

W = A², A = Σ_{j≤5/2} χ_j. Decompose A = a₁+a₂+a₃ **as functions**
(each character's coefficient divided among three alternatives —
alternatives are bundles of histories, not partitions of the
character set). For four random decompositions:

sup|I₃| ≈ 1.6–2.4e−13, i.e. **4e−16 relative to sup W.** Identically
zero in θ, for every decomposition — an algebraic identity of a
quadratic form, not a fitted smallness.

## 3. The hierarchy, measured

| d | sup&#124;I₃&#124; | sup&#124;μ(123)&#124; | ratio |
|---|---|---|---|
| 1 | 5.3e−15 | 2.1e+01 | 0.000 |
| 2 | 1.7e−13 | 4.4e+02 | 0.000 |
| 3 | 1.5e+03 | 9.3e+03 | 0.167 |
| 5 | 1.9e+06 | 4.1e+06 | 0.472 |
| 10 | 1.4e+13 | 1.7e+13 | 0.831 |

A wrong degree is not a small correction — at d = 10 the third-order
term is 83% of the measure itself. (d = 3 is exactly 6a₁a₂a₃,
verified to 5e−12.)

## 4. The budget narrows the degree to four values, and three die

The record's band is measured here: the weight's character
coefficients are **6, 10, 13, 14, 14, 12, 9, 6, 4, 2, 1** and then
exactly 0 — **B = 11.** A degree-d weight needs an amplitude of band
M with d(M−1)+1 = B, so **d must divide B−1 = 10**: d ∈ {1, 2, 5, 10}.

| d | M | amplitude sign-changes | weight ≥ 0 | I₂ | I₃ | verdict |
|---|---|---|---|---|---|---|
| 1 | 11 | yes | **no** | 0.000 | 0.000 | **no interference at all** — excluded by lucid 0033's measured 0.302 nats/trial |
| 2 | 6 | yes | yes | 0.189 | 0.000 | **survives** |
| 5 | 3 | yes | **no** | 0.070 | 0.592 | odd power of a sign-changing amplitude — **not a measure** |
| 10 | 2 | yes | yes | 0.035 | 0.826 | **third-order interference** — absent in the record |

Each row dies for a *different* measured reason, and the survivor is
unique.

> **Degree 2 is forced. The band budget fixed the band; the band
> fixes the degree; the degree is the sum rule.**

## 5. What this closes

The source ledger's chain is now complete end to end, with no step
postulated:

| step | why | where |
|---|---|---|
| the ledger's content is *interference* | two records, each firing one detector | lucid 0033 |
| amplitudes **multiply** in ℂ | two additive ledgers ⇒ Frobenius; ℝ costs 0.302 nats, ℍ leaks 0.019 | lucid 0034 |
| the weight is a **square** | budget ⇒ band ⇒ degree, by elimination | 0119 + here |
| alternatives are **summed** | degree 2 ⇔ I₃ = 0 | here + lucid 0035 |

Nothing in that chain is a postulate about Hilbert space. What
remains of the program's gravity side is not a postulate either —
it is the factor 20 of 0125.
