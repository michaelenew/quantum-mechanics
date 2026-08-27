# 0028 — Completing the prototype: the level, the dressing, the measurement rule

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

The three items standing between 0027's shape and a finished 2+1
prototype, resolved in one pass. Two close outright; the third
reduces to a single explicit bit. Code:
`output/0023_completing_the_prototype.py`.

---

## 1. The level: even, cored at 2, and a tower that never closes

What fixes N? Three results, the first two operator-exact:

- **Evenness is a theorem.** The measured two-party flip δ(2) = π
  (0014) must be in the deficit spectrum {2πn/N}, and π is
  representable iff N is even (checked N = 2–9). The geometry's
  flip forces an even level.
- **The tower is a chain of deck extensions.** At level 2N, the
  pair (U², V) satisfies the level-N Weyl relation, and the
  half-period translation **C = V^N is central with C² = 1 — the
  deck swap**. The 4 → 2 sectors, restricted explicitly: the
  C = +1 sector carries (Z, X) with *periodic* shift; the C = −1
  sector carries the *antiperiodic* (twisted) shift — **the
  cat/spinor pair of the double-cover thread, operator-exactly.**
  Level 2N is a central Z₂ extension of level N; the tower
  2 → 4 → 8 → … is the chain of double covers.
- **The full object is the inverse limit.** The arithmetic thread
  proved the reference tower never closes (0063), and its unique
  maximal causal paradox is the odometer (0060). The web's level
  structure is that same object: even at every stage, N = 2 at the
  decoration core (the qubit, the flip), and the completed system
  the inverse limit of the 2^k tower — **the 2-adic odometer as
  the level structure of the quantized web.** The two repos meet a
  third time, now at the deepest tier.

(Honest residue: this pins the *structure* of the level — evenness,
the 2-core, the 2-adic tower — not a single finite value; a finite
world truncates the tower at some rung, and what selects the rung
is the remaining freedom.)

## 2. The dressing, closed: K = πs/det g

0019's open nonlinearity is not open anymore. The exact local law:

```
K(x) = π s(x) / det g(x)
```

Tested over the full strength sweep, the spatial profile, and an
anisotropic two-lump configuration (ratios K·det g/(πs)):

| S | r=0.05 | r=0.15 | r=0.30 | r=0.45 |
|---|---|---|---|---|
| 0.05 | 1.0000 | 0.9992 | 0.9958 | 0.9887 |
| 0.10 | 0.9998 | 0.9982 | 0.9917 | 0.9784 |
| 0.20 | 0.9996 | 0.9963 | 0.9842 | 0.9604 |
| 0.40 | 0.9992 | 0.9930 | 0.9720 | 0.9319 |

Two-lump anisotropic: 1.0000, 0.9974, 0.9820 at the tested points.
The law holds to <1% wherever sources are appreciable; the far-tail
residual is the source-free **tidal halo** (known since 0014),
which carries no strength.

Everything reconciles at once:

- **The atom law is its proper-area integral**: δ = ∫K√det d²x =
  π∫s/√det = πS/√det A₀ — exactly 0020's derived screening
  f = 1/√det A₀. The apparent det^(−1/2) (atoms) vs det^(−1)
  (field) tension was proper-vs-coordinate bookkeeping.
- **0020's "gradient" hypothesis dies**: the under-correction of
  bare screening was just the wrong power of det; no gradient
  terms are needed at this order.
- The reading: **participation buys curvature at the local rate
  π/det g — discounted by the square of the information volume
  already at the point.** The full nonlinear field equation of the
  prototype is one line.

## 3. The measurement rule, reduced to one bit

P5 says measurement = minimum-relative-entropy projection. On the
holonomy Hilbert space this is now a computation, run on the web's
own observable: two punctures at N = 2, W = Z⊗Z (total deficit
parity), outcome "even" — a rank-2, *degenerate* projector P — with
a generic prior σ carrying cross-sector coherence.

- The MRE update has the closed form ρ* = exp(P log σ P)|_P /Z
  (Gibbs variational principle; verified as the true minimum
  against 200 random feasible perturbations).
- Lüders gives PσP/tr(PσP).
- **They agree exactly** for rank-1 outcomes and whenever
  [σ, P] = 0 (distance 6×10⁻¹⁷ measured) — in particular on all
  classical (diagonal) priors, where both are Bayes.
- **They diverge for degenerate outcomes on coherent priors**:
  trace distance **0.158** in the test case, with
  S(MRE‖σ) = 1.948 < S(Lüders‖σ) = 2.029.

And the web cannot dodge the regime: total-deficit Wilson loops on
multi-puncture sectors — its most natural observables — are exactly
degenerate. So the measurement problem, in the prototype, is
**one explicit bit**:

- *MRE on states* (P5 as literally written): a falsifiable
  departure from textbook QM, with the measured signature above —
  sequential measurements after a degenerate outcome distinguish
  exp(P log σ P) from PσP.
- *MRE on instruments/channels*: recovers Lüders, i.e. textbook QM,
  and P5 becomes a derivation of the update rule rather than a
  rival to it.

The relational stance of the repo (measurement is an interaction,
not a conditioning) leans toward the instrument reading — but that
is now a physical choice with a computable experimental signature,
not a philosophical one. This is the sharpest form the repo's
founding question has ever had.

## The prototype, complete

With this batch the 2+1 prototype has: postulates → forced metric →
field equation with its exact nonlinearity (K = πs/det g + halo) →
conservation as the action's second EOM → derived causal cone →
forced Poincaré symmetry with confirmed structure constants → BF
action with monodromy charges → quantized: intersection-deformed
holonomy algebra, quantized participation, anyonic matter, an even
level cored on the qubit with a 2-adic tower — and a measurement
rule pinned to one explicit, testable bit. That is the guide for
3+1.

## Honest limits

- The level result pins structure, not a numerical rung; the halo
  remains outside the local law (as it must — it carries no
  strength); the two-lump law was tested at core points (tails are
  halo-dominated).
- The MRE/Lüders fork is computed for projective outcomes on
  finite-dimensional sectors; POVMs and the instrument-level MRE
  computation (showing it reproduces Lüders) are stated from the
  literature, not recomputed here.
- The tower's inverse-limit reading imports the arithmetic thread's
  never-closing theorem across the bridge; the identification is
  structural (same tower, same deck sectors), not yet a single
  formalized statement spanning both repos.

## Open

1. **The rung**: what truncates the 2-adic tower for a finite
   world — plausibly the budget (Σδ = 4π caps atoms at 2N), making
   N a property of the universe's content rather than its laws.
2. **The halo's own law**: the source-free tidal field as a
   function of the anisotropy tensor — the last undescribed
   classical structure.
3. **The measurement bit, decided**: find a web-native principle
   (relational/interaction reading of P5, or the arithmetic
   thread's trust calculus) that selects states vs instruments —
   or design the sequential-measurement discriminator as a concrete
   protocol.
4. **Then 3+1**, with the completed prototype as the guide.
