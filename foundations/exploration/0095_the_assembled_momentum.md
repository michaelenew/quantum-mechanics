# 0095 — The assembled momentum: tree Maxwell, one-loop isotropy

Sixteenth stone: the wall's last outstanding piece — A3, the momentum
half of the graviton propagator with sector resolution — attacked
perturbatively, which 0078's eigenvalue identity makes possible. The
perturbative half is now **done**, it contains an exact theorem that
reorganizes the arc's expectations, and the remaining half is
properly sized. Code: `output/0085_the_assembled_momentum.py`.

---

## 1. The expansion, and tree level

From Σs_k² = Σ|F_p|² (0078):

```
price = Σ|F_p|²/(2ε′) − tr(S⁴)/(4ε′²) + O(s⁶)
```

(O(s⁶) verified by exact halving: residual ratio 64-class). So **at
tree level the assembled measure is six independent massless lattice
Maxwell fields** — one per bivector component. The momentum half's
answer at leading order: the propagator is 1/k̂², massless, with *no
sector distinction* — the graviton content propagates massless
because everything does. The entire vertex physics is the quartic
tr S⁴.

## 2. The one-loop isotropy theorem (exact)

The quartic's tadpole — the complete one-loop self-energy of a local
quartic — is **exactly isotropic**:

- Under a unit isotropic background: Q_ab = 4.75·δ_ab, by
  machine-exact polarization.
- Under the **true** same-site lattice covariance (computed with
  forward-difference phases; it is *not* diagonal — off-diagonal
  entries ±0.108): Q(SD) = Q(ASD) = Q(balanced) to 1e−9, all equal
  to 4.75 × T_diag — **the off-diagonal covariance decouples from
  the tadpole exactly.**

Three consequences, at one loop in the assembled vacuum:

1. **No graviton mass** — masslessness is protected at this order,
   not tuned.
2. **No sector splitting** — the (1,0) lift is *not* a weak-coupling
   vacuum effect. The vacuum propagator treats every bivector
   direction identically.
3. The vertex's entire one-loop content is an **isotropic
   field-strength renormalization** — a pure coupling shift with the
   confining sign: 0093's β > 0, now seen diagrammatically.

## 3. Where the sector physics lives

The exact vacuum theorem coexists with 0089's solidly-measured
+1.17 ± 0.12 nat split because they probe different things:

- **Infinitesimal probes of a geometric background** (the Hessian):
  pack-noisy, consistent with zero (−3.2 ± 2.7 over 16 packs).
- **Finite-content probes**: the split is real, quadratic-ish in
  source amplitude above the regulator scale, with a measured sign
  crossover near amp ~ √ε′.

> **The lift is a finite-content background effect.** Unbalanced
> curvature is charged when real content sits on real geometry —
> not in the vacuum's fluctuation spectrum at weak coupling. This
> is a cleaner division than the arc had assumed: masslessness and
> sector-democracy for vacuum fluctuations; simplicity enforcement
> for content. (Consistent, in retrospect, with 0078's honest
> non-flip: the measure constrains *configurations*, not the
> vacuum's mode structure.)

The vacuum-spectrum fate of the sectors at **strong coupling** —
where 0093's flow runs every UV start — remains open, and is now
properly scoped: a nonperturbative Monte Carlo of the local-quartic
F-ensemble (or the group-level ledger with joint frame factors).
That computation is well-defined, heavy (hours of MC for marginal
propagator statistics in this environment), and is the honest
boundary of what this run of stones can deliver.

## 4. A3's ledger, closed out

| A3 piece | status |
|---|---|
| tensorial half (which modes, hierarchy) | 0075 (bare) + 0089 (context support) |
| momentum half, tree | **done — massless 1/k̂², here** |
| momentum half, one loop | **done — isotropy theorem, here** |
| sector fate at strong coupling | open; scoped as nonperturbative MC |
| boundary-state/intertwiner form | open (the spin-foam-grade completion) |

## Honest limits

- Perturbation theory around F = 0 in the Gaussian-regulated vertex
  (ε′ = 0.01); the expansion's validity ends at s ~ √ε′, exactly
  where the measured crossover sits — the two regimes are honestly
  disjoint.
- The one-loop theorem is for the *tadpole* of the local quartic —
  which is the complete one-loop self-energy for a local vertex, but
  two-loop (sunset) terms involve cross-site correlations that were
  not computed.
- The same-site covariance used Feynman gauge (⟨FF⟩ is
  gauge-invariant; the gauge choice affects nothing quoted).
- The Hessian split's "consistent with zero" is a statement at
  ±2.7 precision over 16 packs, not a proof of vanishing.

## Open

1. The strong-coupling F-ensemble MC (the scoped heavy remainder).
2. Two-loop: does the sunset break the isotropy? (The freeze/
   locality logic says cross-site structure is where it *could*.)
3. The boundary-state vertex (standing).
