# 0041 — The bond ledger: why the web's law makes correlation invisible

0040's four opens, three answered computationally and one
registered. The central result is a coincidence that turns out not
to be one: **the equation of state that makes the bond conically
invisible holds if and only if the force law is inverse-square —
which is exactly the law the web's own vacuum principle selected.**
Code: `output/0036_the_bond_ledger.py`.

---

## 1. The local negative (a claim retired)

Is 0037's static O(M₁M₂) vacuum violation *locally* the bond's
field stress? **No.** The pointwise ratio G_ij/t_ij scatters from
−603 to +618 across four probe points, against the candidate
8π = 25.1. The bond is an **integrated, gauge-invariant** statement
(0040 §2, exact to the last digit); the superposition's local
residual is a pseudotensor-gauge object. So 0037's "violation" is
the two-body *gauge* problem, not a physical local defect — worth
recording before the tempting local reading hardened into a claim.

## 2. Tension is the force; μ = −T only for inverse square

Two measurements, one conclusion.

**Tension is the force, whatever the force is.** For a general law
F = k/d^(p+1), the virial deficit is S_ij = −(F·d)n̂ᵢn̂ⱼ at every
exponent tested (p = 0.5, 1, 2, 3; relative error 1e−8 to 1e−7).
The bond's tension equals the mutual force universally — that part
of 0040 was not special to gravity.

**But the equation of state is not universal:**

```
μ / T = −1/p        (exact, four exponents)
```

so μ + T = 0 — zero conical deficit — happens **only at p = 1**,
the inverse-square law. Verified through the 0033 charge reader:

| p | μ/T | deficit measured | predicted |
|---|---|---|---|
| 0.5 | −2.0000 | 0.12564 | 0.12566 |
| **1.0** | **−1.0000** | **0.00000** | **0.00000** |
| 1.5 | −0.6667 | 0.04188 | 0.04189 |
| 2.0 | −0.5000 | 0.06282 | 0.06283 |
| 3.0 | −0.3333 | 0.08376 | 0.08378 |

And p = 1 in 3D is precisely what the web's vacuum principle
selected in 0036 (w = 2M/ρ was the *unique* power law with flat
off-source curvature).

> **The web's field law is exactly the one for which correlation
> carries no participation charge.**

Read as a constraint rather than a coincidence: a theory whose two
tiers must stay distinguishable — participation curving the web and
read by loops, correlation binding without leaving monodromy — has
**one force law available to it**. Any other exponent would make
bonds masquerade as masses to the charge reader. This is a second,
independent route to the inverse-square law, and it comes from the
program's own two-tier postulate (P2) rather than from the field
equation.

## 3. The dimensional selection

The obvious next question — is this a 3D accident? — sharpens the
result instead of dissolving it. In d spatial dimensions the vacuum
(harmonic) profile gives U ∝ 1/s^p with **p = d − 2**; the
linearized transverse field of a line source is proportional to
**(μ + T) in any d** (trace reversal, dimension-free); and
μ/T = −1/p as measured. So:

| d | p = d−2 | μ/T | (μ+T)/T = (d−3)/(d−2) |
|---|---|---|---|
| 2 | 0 | (log potential — not scale-free) | — |
| **3** | **1** | **−1.0000** | **0.0000** |
| 4 | 2 | −0.5000 | +0.5000 |
| 5 | 3 | −0.3333 | +0.6667 |
| 6 | 4 | −0.2500 | +0.7500 |

**Three spatial dimensions is the unique dimension in which the
bond carries no transverse gravitational charge** — and it is also
the only dimension in which a bond (a line) is codimension 2, so
that the charge it fails to carry is a *conical deficit* at all.
The two-tier postulate, the inverse-square law, and d = 3 are one
condition, not three.

## 4. N bodies: charges add, bonds multiply

The three-body conservation deficit is exactly the pair sum of
bonds — relative error 2e−16, machine precision. So the ledger
reads:

- **participation: additive** — Σ_a m_a (the holonomy charge);
- **bonds: bilinear** — Σ_{a<b} m_a m_b.

The additive/multiplicative split *is* the participation/
correlation split — marginals versus joints, entropy versus mutual
information — in one line of arithmetic.

## 5. The bond's quantum (registered, not derived)

Participation is quantized additively (deficits 2πn/N, masses
n/(4GN) — 0027). The bond has no deficit, so it carries no such
charge — yet it is bilinear in participations, so with
m_a = n_a·(quantum) the bond weights go as n_a·n_b: **the
multiplication table, not the addition table**. Whatever quantizes
the bond is a product structure on the charge lattice — the shape
of entanglement rather than of charge. Consistent with 0029's
square-root ledger placing correlation on the amplitude tier, but
not derived. The open construction is the bond's operator, whose
classical limit must be tension = force.

## Honest limits

- §2's "only inverse-square" is over **power laws** (as in 0036);
  a non-power-law force with μ = −T pointwise is not excluded by
  this test, though μ = −T ⟺ U ∝ 1/d is immediate from
  μ = U/d, T = −U′.
- The deficit measurements use the linearized (μ, T) string metric
  — a model check of the equation of state, not a measurement of a
  physical bond's holonomy in a full two-body spacetime.
- §1's negative is about the *superposition ansatz*; a different
  (correct) two-body solution would have a different local
  residual. The statement is that no local identification of the
  bond survives gauge, not that the two-body field is unknowable.
- §3's d ≠ 3 rows use the **harmonic extension** of the vacuum
  principle (measured only at d = 3, in 0036); a genuine
  higher-dimensional test needs a d-dimensional curvature
  pipeline. The (μ+T) transverse-charge structure, by contrast, is
  dimension-free linearized algebra.
- §5 is an observation about scaling, not a quantization.

## Open

1. **The bond's operator**: the quantum tier's missing piece, with
   two constraints now in hand — classical limit tension = force,
   and a bilinear (product) charge structure.
2. **Beyond power laws**: whether μ + T = 0 forces U ∝ 1/d among
   *all* laws (immediate algebraically) and whether the web's
   vacuum principle admits non-power-law solutions at all
   (Birkhoff says no in GR; the web-native version is 0036's
   standing open).
3. **The two-body solution**: with the local reading retired, the
   remaining question is constructive — a two-body metric whose
   implied source is the pair plus the bond, exactly.
4. **The higher-dimensional measurement**: build a d-dimensional
   curvature pipeline and verify the harmonic profile is
   vacuum-selected for d ≠ 3, which would upgrade §3 from
   extension to theorem — and with it the claim that the web's
   own consistency picks three spatial dimensions.
