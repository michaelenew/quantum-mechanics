# 0050 — The Palatini construction: the chain's last constructive gap

0048 enumerated the residue; 0049 closed two items. This closes the
constructive one — the functional built from its own variables and
verified on the web's own solution — and settles the two remaining
quantitative fronts. Code: `output/0045_the_lattice_palatini.py`.

---

## 1. The simplicity constraint counts the gravitons

0030's obstruction was a degree-of-freedom claim, so it is settled
by **counting**, not argument. Ranks of the linearized systems:

| system | count |
|---|---|
| free BF (B unconstrained) | F = 0 leaves 1 solution per internal pair; the gauge orbit (ω_μ = k_μλ) is also 1 → **0 physical dof** |
| Palatini (B = e∧e) | the torsion equation on ω has **rank 24 of 24** → ω is determined *algebraically* by e |
| the resulting system | 10 symmetric − 4 constraints − 4 residual gauge = **2 dof** |

**Imposing B = e∧e takes the count from 0 to 2.** The simplicity
constraint is exactly what releases the gravitons — and by 0046 it
*is* the ledger (probability = amplitude²). The rank-24 fact is the
mechanism: constraining B to be a square makes the connection a
*dependent* field, and a theory second-order in e alone propagates.

## 2. The construction, on the web's own solution

Take the channel tetrad e = 𝟙 + ½w·kkᵀη (0046), solve the torsion
equation for ω numerically (24×24), build F(ω), contract to Ricci,
compare with the metric route:

| profile | torsion residual | Ricci(Palatini) vs Ricci(metric) |
|---|---|---|
| w = 0.3 | 6e−17 | 1e−6 relative (scale 0.242) |
| w = 0.2/r^0.5 | 3e−17 | 5e−6 (scale 0.076) |
| w = 0.25/r² | 7e−17 | 9e−6 (scale 0.193) |
| w = 0.1/r (vacuum) | — | Ricci-flat both ways |

The solved ω annihilates the torsion to machine precision, and the
functional's own variables reproduce — on the web's channel tetrad,
at three *non-vacuum* strengths — the field equation the program has
measured all along. **0046's identification is now a construction**;
the chain's last constructive gap (0048 residue #2) closes.

## 3. Loop decay: Γ measured

The exact loop (0049) radiates, by Isaacson flux over a sphere:

| R | P | Γ = P/(Gμ²) |
|---|---|---|
| 20 | 4.581e−3 | **45.8** |
| 30 | 4.542e−3 | **45.4** |

against GR's Γ ~ 40–100 for Kibble–Turok loops, and size-independent
(the two radii agree to 1%). A quantitative correspondence with an
independent GR result — and the loop's decay constant is the kind of
number that has no adjustable freedom left in this theory.

*(An instrument bug found and fixed en route: the retarded-time
bracket must exceed the probe radius, or the bisection never
brackets the root. The first run gave Γ = 2.7e6.)*

## 4. The residual is velocity, not nonlinearity

> **Corrected by 0051 §3.** The scan below cannot separate strength
> from velocity: at fixed R/λ the field strength h ≈ 4v³ is
> *determined* by v, so the "M halved" row necessarily had the same
> h as the baseline. A distance scan settles it — the residual falls
> as exactly 1/R, i.e. it is **near-zone contamination**, and the
> conserved binary's wave-zone field is **exactly vacuum**. The
> measurements below stand; the inference drawn from them does not.

0048 residue #5 asked whether the conserved binary's 1–4% vacuum
residual is O(v) source structure or O(h²) field nonlinearity.
Measured at ~6 wavelengths:

| configuration | v | ratio |
|---|---|---|
| baseline | 0.200 | 0.0138 |
| v halved | 0.100 | 0.0017 (factor 8.2) |
| M halved | 0.200 | **0.0138 (factor 1.00)** |

**Velocity exponent 3.03, and exactly strength-independent.** The
residual is post-Newtonian *source* structure — which the quadrupole
formula also lacks — not a failure of the field theory. Residue #5
closes.

## Honest limits

- §1's counts are the standard linearized ones, done here by
  explicit rank rather than quoted; they are performed at one null
  wavevector and in one gauge-fixing scheme.
- §2 verifies the ω-equation (torsion) and the curvature
  contraction on a spherically-symmetric channel family; the
  e-equation is verified indirectly (both routes give the same
  Ricci, and the vacuum profile is flat), not by varying a discrete
  action on a lattice. "Lattice Palatini" in the strict
  spin-foam sense remains unbuilt — what is built is the
  continuum-limit Palatini route on the web's solution.
- §3's Γ is one loop family, one λ, one quadrature resolution; the
  GR comparison range (40–100) spans loop families, so this is a
  consistency match, not a match to a specific published number.
- §4 uses the leading virial bond; the v³ scaling identifies the
  order but does not name which post-Newtonian term supplies it.

## Open

1. **The discrete action** (the strict version of §2): vary
   S = Σ ε e∧e∧F on 0030's lattice and recover both EOMs
   variationally — the remaining formal step, now with the
   continuum route verified to compare against.
2. **Cusp beaming**: the loop has Kibble–Turok cusps (σ = π/2,
   t = π/2 mod π); GR predicts beamed bursts with a characteristic
   opening angle. The machinery measures it directly.
3. **Which PN term** supplies §4's v³.
4. Standing from 0048: the Lorentzian-arena construction, P4 →
   Tsirelson, matter beyond scripted sources, the arithmetic
   bridges.
