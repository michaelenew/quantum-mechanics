# 0053 — The quantum lattice: the square measure prices curvature

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

The lattice theory (0052) quantized at level N, full bore. Four
results, all exact, and the third is the one the program has been
walking toward since 0030: **the quantum mechanism by which the
ledger's square releases the gravitons.** Code:
`output/0048_the_quantum_lattice.py`.

---

## 1. The ground space derives the Weyl algebra

The level-N gauge sector on a 2-torus lattice is the Z_N quantum
double. Ground degeneracy computed two independent ways: the rank
formula N^(E − rank d₀ − rank d₁) = **N²**, and brute enumeration
(243 flat configurations / 27 gauge volume = **9** at N = 3). On
that ground space, with Wilson and dual ('t Hooft) loops *built
from the model*:

```
W_x T_x = ω T_x W_x     (6.5e−16)
W_x T_y = T_y W_x       (exactly 0)
```

**0027's postulated cycle algebra is now a theorem of the lattice
model** — one level-N Weyl pair per cycle, commuting across cycles.
The quantum tier's kinematics, which the prototype assumed, is what
the lattice's own ground space produces.

## 2. The 2-form tier is homology

On the 2×2×2 3-torus: the chain identities d₁∘d₀ = 0 and d₂∘d₁ = 0
hold **exactly over ℤ** — the conservation law dB = 0 is the
complex's own identity, prior to any dynamics. The mod-p Betti
numbers give b₁ = b₂ = 3 (N = 3 and 5): the 1-form (charge) sector
has ground degeneracy N³ and the 2-form (budget) sector N³ —
Poincaré-dual partners whose pairing is the linking algebra (0030).
Charges live on 1-cycles, budgets on 2-cycles, and the torus's
topology is what both count.

## 3. The square measure prices curvature

The plaquette weight is the budget sum K(F) = Σ_B m(B)·ω^{BF}:

| measure | K(F) | meaning |
|---|---|---|
| uniform budget (free BF) | N·δ_{F,0} | curvature **forbidden** — topological |
| squared budget (B = e·e) | **N·gcd(F, N)** | curvature **priced** — local dynamics |

(exact, all F, verified N = 3, 4, 5, 7, 8). The uniform sum is the
delta that enforces flatness; the multiplication table's
multiplicity distribution softens it into a finite Boltzmann
weight: relative cost gcd(F,N)/N, i.e. action **log(N/gcd(F,N))
per curved plaquette — one curved plaquette costs one level-N
symbol of the ledger.**

This is the quantum mechanism of the graviton release. 0050 counted
it classically (0 → 2 dof by rank); here the *same constraint*
appears as a change of measure that converts flatness-as-constraint
into curvature-as-priced — which is what lets curvature propagate.
It is also the quantum ancestor of the measured classical law
K = πs: **participation buys curvature**, with the exchange rate
now visible as a Gauss sum.

And on the tower N = 2^k the price is graded by the **2-adic
valuation** of the curvature — N = 8 weights: 64, 8, 16, 8, 32, 8,
16, 8, i.e. 8·gcd(F,8) — curvature quanta with higher 2-divisibility
are cheaper. The level tower's arithmetic (0028's 2-adic odometer)
appears directly in the action.

## 4. The measure is a correlated web

Under B = e·e, budgets on plaquettes sharing an edge are correlated:

| N | MI (shared edge) | MI (disjoint) |
|---|---|---|
| 3 | 0.1181 bits | ~1e−16 |
| 5 | 0.1426 bits | ~1e−16 |
| 7 | 0.1430 bits | ~1e−16 |

The algebraic sharing that makes d(e∧e) = 0 an identity classically
appears at the quantum tier as **correlation between neighbouring
budgets** — the conservation law's quantum seed. The theory's own
two-tier structure returns inside its measure: **the budget field
has bonds.** The web quantizes into a web.

## Honest limits

- §1–2 quantize the *abelian level-N truncation* of the lattice
  theory (the compact U(1)→Z_N sector), which is where the 0027
  prototype lived; the nonabelian SO(3,1) links of 0052 are not
  themselves quantized here (that is spin-foam territory).
- §3's "priced curvature ⇒ propagating dof" is the standard
  confinement/deconfinement reading of a softened plaquette weight;
  the spectrum of the constrained model (the actual lattice
  gravitons) is not computed.
- §3's squared measure takes the two frame factors uniform and
  independent per plaquette — the minimal operator reading of
  B = e·e; correlations imposed by shared edges (which §4 measures)
  are not yet fed back into K(F).
- §4's MI is a property of the prior measure, not yet of a
  dynamical state.

## Open

1. **The constrained model's spectrum**: diagonalize a small
   constrained lattice (transfer matrix with the K(F) = N·gcd(F,N)
   weights) and exhibit the propagating mode directly — the lattice
   graviton, the quantum completion of 0050's count.
2. **The correlated-measure feedback**: recompute K(F) with the
   shared-edge correlations of §4 included — the honest B = e∧e
   measure on a full plaquette complex.
3. **The 2-adic action**: on the tower, the curvature cost
   log(N/gcd) is Λ-adic; connect to 0028's deck-extension sectors
   (does the antiperiodic/spinor sector see a shifted price?).
4. Standing from 0048: the Lorentzian arena, P4 → Tsirelson,
   matter beyond scripted sources, the arithmetic bridges.
