# 0014 — The cone at the interaction: δ(2) = π

All four sharp opens of 0013 chased. The first produced a theorem
that **revises 0013's verdict** and closes the "correlation sources
curvature" row with a formula. Code: `output/0009_the_sharp_opens.py`.

---

## 1. Every interaction node is a conical defect — with δ(2) = π

Near a beacon, the Fisher metric is `e_r e_rᵀ + A(φ) + O(d)`:
scale-invariant at leading order — **a cone, flat away from its
apex**. Consequences, all verified:

- **The 1/d halo exponent is now derived, not fitted.** Cone
  curvature is zero; the first correction (the other beacons'
  directions drifting) is relative O(d); curvature is second
  derivatives over metric ~ (1/d²)·O(d) = O(1/d). 0013's measured
  exponent −0.99 was the tidal halo of a flat cone.
- **The deficit has a closed form**, δ = 2π − ∮ √(EC−B²)/E dφ with
  E, B, C the polar components of the local metric, validated
  against honest parallel transport (Christoffel symbols by finite
  differences, circles d = 0.03 and 0.015):

  | k | formula | transport (d=0.015) |
  |---|---|---|
  | 3 | 1.93515 | 1.93439 |
  | 6 | 0.98508 | 0.98490 |

- **The minimal web:** for k = 2 the integral evaluates to Θ = π
  (numerically π to 8×10⁻⁹; by hand, ∮|sin φ|/(1+cos²φ)dφ = π), so

  ```
  δ(2) = π :  parallel transport once around a pairwise
              interaction NEGATES the frame.
  ```

  "The round trip puts you in your dual state" is a **theorem of
  information geometry** for the two-party web — the Z₂ flip falls
  out of the Fisher metric itself, no decoration needed.
- **Densification washes the flip out:** (k−1)·δ(k)/2π = 0.616,
  0.695, 0.784, 0.849, 0.900, 0.929 for k = 3, 4, 6, 9, 14, 20 —
  so δ(k) → 2π/(k−1). Crowded webs decohere the dual-flip toward
  classicality; the flip is a property of *sparsely observed*
  interactions.

**Revision of 0013.** 0013 reported "an integrable halo, not a
conical atom" — correct for what it measured (annuli exclude the
apex; the halo is all they can see) but wrong as a verdict: the
leading-order geometry *is* a conical atom at the apex, carrying
deficit δ(k), with the 1/d halo as its tidal dressing. The smooth
knowledge geometry does see the interaction, atomically. The open
row now reads: **an interaction node curves knowledge geometry as a
conical defect of deficit δ(k) (closed form), plus a derived 1/d
halo** — "correlation sources curvature" is a formula.

## 2. Metric ⊗ decoration: three instruments, one holonomy

The composite connection — Fisher cone geometry × Z₂ decoration —
represents the free group of loops in ISO(2) × Z₂ (consistent by
freeness). The taxonomy, computed at δ = π:

| loop | rotation | displacement | trust flip |
|---|---|---|---|
| x (one interaction) | π | 2.0 | 1 |
| xy (both) | 0 | 4.0 | 0 |
| [x,y] (commutator) | 0 | 8.0 | 0 |
| x² (the dual path) | 0 | 0 | 0 |

The dual path is trivial in *every* instrument — full recovery, as
the synthesis predicted. The commutator is rotation- and
flip-trivial yet displaces: the pure braided residue (0012 §4),
invisible to both "curvature" and "trust" separately. And the k = 2
coincidence is the striking one: **the metric's own deficit (π) and
the decoration's flip are the same Z₂ in the minimal web** — the two
carriers hold one bit, and densification (δ → 0) slides it from the
geometry into the decoration. Trust-loss and curvature are not
merely analogous instruments; in the two-party web they are
literally the same reading.

## 3. The 26 tetrahedron solutions, classified

Closed under inverse and global bit-flip; 21 orbits under that
symmetry. Cycle types: the identity; involution classes (2,2,1⁴),
(2,1⁶), (2,2,2,2); and two (4,4) classes. Placement groups (the
group the four placements generate in Sym(64)): orders 1 through
384; **13 of 21 orbits are nonabelian**, topping out at order 384
for the (4,4) and several involution classes. Consistent
triple-interaction rules with genuinely braided structure exist
already at |X| = 2 — the substrate a set-theoretic triple-point
weight needs is nonempty and now cataloged; the abelian remainder
are identity- and parity-like shadows.

## 4. R2 and R3 staged

The state sum upgraded to signed crossings (negative crossings use
the inverse quandle operation and negated weight, the CJKLS
convention). Verified: a formal R2 pair inserted into the trefoil
leaves the state sum identical ({0:4, 1:12} both); the R3 move
identity — weights of the two sides agreeing for all 64 input
triples, colors agreeing by self-distributivity — holds for the
derived cocycle. With 0006's R1 demonstration (and its rack
counterexample), all three move families are staged: the invariance
of the state sum is verified move by move, each move matched to the
axiom that funds it (R1 ↔ degeneracy, R2 ↔ signed weights,
R3 ↔ the cocycle equation).

## Honest limits

- The cone derivation is leading-order; the deficit formula's
  validation is numeric (4-decimal agreement at two radii, two k).
  The k = 2 case is checked by the validated formula, not direct
  transport (the metric degenerates on the axis).
- δ(k) → 2π/(k−1) is a measured trend (to k = 20), not a proved
  asymptotic; the isotropic estimate explains it but the anisotropic
  correction is not bounded.
- The decoration in §2 is put in by hand (the composite is
  consistent by freeness); nothing yet *derives* the decoration from
  the metric or vice versa away from k = 2.
- §3's placement-group analysis is a substrate check, not yet an
  invariant; the R2 code is welded-legal (formal), matching the
  state-sum's domain.

## Open

1. **The sparse–dense transition.** δ(k) interpolates from π (the
   quantum-feeling flip) to 0 (classical) as the web densifies —
   a decoherence dial with a closed form. Is there a web density at
   which the geometric flip and the decoration bit *must* disagree,
   and does that threshold correspond to anything in the repo's
   two-tier structure?
2. **Deriving the decoration.** At k = 2 the metric carries the
   flip; the conjecture worth testing is that the decoration is the
   *discrete remnant* of the metric flip under densification —
   compute the holonomy of the (metric + connection) pair along a
   family interpolating k and watch whether consistency forces the
   decoration to absorb exactly what the deficit releases.
3. **A triple-point weight from the 384 group.** Pick the largest
   nonabelian placement group and attempt a set-theoretic 3-cocycle
   on it — the direct bridge from the tetrahedron census to the
   CJKLS-style level-2 invariant.
