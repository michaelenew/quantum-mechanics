# 0042 — The bond operator, the dimension theorem, and a trap

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0041's three fronts: measure the dimensional selection instead of
extending it, find the bond's quantum operator, construct the
two-body source. All three move here — and the third turns into a
caution that explains a design choice already made. Code:
`output/0037_the_bond_operator.py`.

---

## 1. The dimension theorem, now measured

New battery instrument: a **general-dimension curvature pipeline**
(`ricci_nd`, any n). Applied to the point channel g = η + w·kkᵀ with
w = w₀/ρ^p in d spatial dimensions, the off-source Ricci vanishes at
**p = d − 2 and only there**:

| d | vacuum scan (max\|R_μν\| off-source) |
|---|---|
| 3 | p=1: **3e−7** · p=2: 5e−2 |
| 4 | p=1: 3e−2 · p=2: **7e−7** · p=3: 7e−2 |
| 5 | p=2: 3e−2 · p=3: **1e−6** · p=4: 8e−2 |

**The web's vacuum principle selects the harmonic profile in every
dimension.** Combined with 0041's measured μ/T = −1/p, the bond's
transverse charge is (μ+T)/T = (d−3)/(d−2) — zero only at d = 3.

> **Three spatial dimensions is the unique dimension in which
> correlation carries no participation charge.**

0041's extension is now a measurement. The chain is: web field law
→ harmonic profile in any d → μ/T = −1/(d−2) → the two tiers stay
distinguishable only at d = 3.

## 2. The bond's operator: the mutual braiding phase

0041 predicted "a product structure on the charge lattice." The
web's quantum tier already contains exactly one such object — the
**mutual braiding phase of two defects**, ω^(n_a n_b), built from
the level-N Weyl algebra as transport of a's charge around b's
holonomy (0027's abelian anyons). Verified at N = 5:

- **Its spectrum is the multiplication table mod N**, where the
  charge's is the addition table:

```
      n_b:  0  1  2  3  4
   n_a=0:   0  0  0  0  0
   n_a=1:   0  1  2  3  4
   n_a=2:   0  2  4  1  3
   n_a=3:   0  3  1  4  2
   n_a=4:   0  4  3  2  1
```

- **It separates states the charge cannot**: every total-charge
  sector contains three distinct bond values (Q = 0 → {0,1,4},
  Q = 1 → {0,3,4}, …). *Correlation is not a function of the
  marginals* — the quantum statement of 0041's "charges add, bonds
  multiply."

And the ledger closes: with m = n·(1/4GN), bond energies go as
n_a·n_b, so **the bond's quantum is the square of the charge
quantum** — one tier apart in the same ½-ledger that carries
trust = √information and amplitude = √probability. The classical
limit is fixed (tension = force, 0040); the quantum object was
already in the theory.

## 3. Where the bond's energy lives (a trap, measured)

The constructive front produced a caution instead of a
construction. Modelling the bond as an **independent matter
source** with its own (μ, T) gives a far-field mass of exactly
**2.000× the binding energy** (measured at R = 20 and 40) — an
overcount.

The bond is **field, not matter**. Its *stress* is a legitimate
source — it supplies the quadrupole formula's missing half
(0039/0040) — while its *energy* is already carried by the field's
nonlinearity. Adding it again as matter double-counts.

Satisfying closure: the channel built in 0034/0035 adds 4S_ij/r to
the **spatial block only**. The construction that reproduced
Einstein's luminosity to 0.01% is exactly the one that avoids this
trap — a choice made on structural grounds then, with the reason
measured now.

## Honest limits

- §1 measures the *vacuum selection* in d = 3, 4, 5 over power-law
  profiles; the (μ+T) transverse-charge formula remains
  dimension-free linearized algebra, and μ/T = −1/p was measured
  in 3D only (its derivation μ = U/s, T = −U′ is dimension-free).
- §2 identifies a *candidate* operator with the two required
  properties (product spectrum, marginal-independence); it is not
  derived from a bond action, and the classical limit
  (tension = force) is matched by ledger scaling, not by an
  operator-to-metric computation.
- §3's factor 2 is a linearized-Tolman bookkeeping statement; the
  general-relativistic energy of a field configuration is not a
  tensor, which is precisely why the stress sector (gauge-
  invariant, radiative) is the one the program measures.

## Open

1. **The bond's action**: an operator with the right spectrum is
   not yet dynamics. The target: a term whose variation gives
   tension = force classically and ω^(n_a n_b) quantum-
   mechanically — the two ends now both pinned.
2. **d ≠ 3 radiation**: with `ricci_nd` in hand, does the
   quadrupole/bond split survive in higher dimensions, or is the
   half-and-half structure also 3D-specific?
3. **The two-body metric**: still unconstructed as an exact
   source-plus-bond solution; §3 says what *not* to do, and the
   remaining route is a genuine second-order solve.
4. **Braiding and binding**: the mutual phase ω^(n_a n_b) is the
   quantum bond; is the classical binding energy its
   semiclassical limit (a phase per unit time = energy)? That
   would connect tension = force to the braiding phase directly,
   and it is a concrete calculation.
