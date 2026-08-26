# 0143 — One record or two: settled, and the factor was wrong

Code: `output/0131_one_record_or_two.py`. **Criticality item 1 is
closed.**

## 1. Three constructions, not two

0142 posed this as a binary and priced it at 12/5. That was the wrong
object. There are three:

| | construction | κ at M = 6 |
|---|---|---|
| **(a)** one record, single SU(2): A(U) = Σ n_j χ_j(U) | κ = (2/3)Σn_j n(n²−1)/Σn_j n | 13.333 |
| **(b)** double copy on Spin(4): A(U⁺,U⁻) = Σ n_j χ_j(U⁺)χ_j(U⁻) | κ = (2/3)Σn_j n²(n²−1)/Σn_j n² | **16.000** |
| **(c)** diagonal restriction: A(U) = Σ n_j χ_j(U)² | 2.4 × (a) | 32.000 |

Closed forms verified against direct differentiation of each weight
to <0.5%. **(b) = 6/5 × (a) exactly at every M** — the double copy
costs a factor **1.2**, not the 2.4 that 0142 quoted for the
*diagonal restriction*, which is a different object.

## 2. The program already contained the answer, in three places

Never combined before:

- **0045 §3** — *"the 3+1 single copy is not BF but Maxwell, and its
  **double copy** is gravity with gravitons."* Gravity is the double
  copy, so the gravitational amplitude carries **two** copies of the
  gauge spin content.
- **0066** — *"a∧b spans a **simple** bivector, and simple =
  **balanced** (|B⁺| = |B⁻|, machine-exact), so the frame-counting
  amplitude is **diagonal**."* The two copies carry the **same j** —
  which is why the amplitude is Σ_j n_j χ_j(U⁺)χ_j(U⁻) and not a free
  double sum.
- **0055** — *"Plebanski's simplicity constraint is not imposed, it
  is **priced**, and the price ratio is exactly 2."* The geometric
  sector is where the two copies are locked.

All three select **(b): two copies, locked diagonal.**

## 3. The decisive test — do the two windows agree?

| construction | κ | ξ/a | vs required |
|---|---|---|---|
| (a) one record | 13.333 | 6.4e+14 | 2.2e−05 |
| **(b) double copy** | **16.000** | **7.7e+17** | **2.6e−02** |
| (c) diagonal | 32.000 | 2.9e+36 | 9.9e+16 |

In κ — which is what the theory fixes — the required coupling is
**17.37**:

| | κ | from required |
|---|---|---|
| (a) | 13.333 | **−23.2%** |
| **(b)** | **16.000** | **−7.9%** |
| (c) | 32.000 | **+84.3%** |

> **At N = 5 — the level 0096's vacuum-sample route independently
> returns — the double copy lands within 8% of the coupling that
> gravity's observed weakness requires.**

The two windows on the level now agree **at the same level**, not one
apart as 0142 reported. The other constructions are out by 23% and
84% in κ, which is four and seventeen orders of magnitude in ξ.

## 4. The answer, and the residual

> **It is two — two *locked* copies.**
> A(U⁺,U⁻) = Σ_j n_j χ_j(U⁺)χ_j(U⁻),
> κ = (2/3)Σ n_j n²(n²−1)/Σ n_j n² = **16 at M = 6**.

**The residual, named.** An 8% shortfall in κ is a factor ~37 in ξ,
and the inversion carries ℓ_P = 2.27a (conditional on the
induced-gravity route and its standing factor 20) plus the
identification of gravity's weak scale with ξ. Either could absorb
8%. **So this is not a prediction of α_G.** It is two independent
determinations of N agreeing to within their own stated
uncertainties — the first time that has happened in this program.

## 5. Item 1, closed

- the multiplicity profile is **flat** (capacity-achieving, lucid 0045);
- the coupling is **κ = (2/3)Σn²(n²−1)/Σn²** over M = N+1 sectors;
- the record count is **two, locked**.

**No free parameter remains between the level and the hierarchy.**
