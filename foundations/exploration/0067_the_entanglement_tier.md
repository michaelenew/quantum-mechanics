# 0067 — The entanglement tier: the weight is the tangle

0066's sharpest open: both ends quantum. A pair of nodes shares an
entangled two-qubit state and the relative coordinate is recorded
**relationally** — as a phase between the correlated branches,
|ψ⟩ = √p|00⟩ + √(1−p) e^{iκθ}|11⟩ — so that neither end alone can see
it. What sources the metric must then be a property of the *pair*,
and it is, in closed form. Code:
`output/0061_the_entanglement_tier.py` (0.2 s).

---

## 1. The relational record — P1 as a density matrix

ρ_A = diag(p, 1−p), **exactly θ-independent**: the coordinate is
invisible at each end, readable only jointly. That is postulate P1
("all content is pairwise") made literal in a two-qubit state.

The contrast case matters: a *product* state with local coherence
(|+⟩|0⟩, encoding on A) carries QFI = κ² with zero entanglement —
that is 0066's one-sided channel, a different mechanism. This module
isolates the purely relational one.

## 2. The weight is the tangle

The Bures metric on the two-node configuration space — numeric
fidelity Hessian, no formula assumed — is (QFI/4)·uuᵀ with
QFI = 4κ²p(1−p), at p = 0.1, 0.25, 0.5 (dev ~6×10⁻⁷). And Wootters'
concurrence of the family is C = 2√(p(1−p)), so, exactly:

> **w = κ² C²  — weight = coupling² × tangle.**

- **Separable ⇒ flat**: C = 0 ⇒ w = 0. An unentangled pair sources
  no geometry.
- **Maximal entanglement ⇒ the full one-carrier weight** (C = 1
  recovers 0066's κ²).
- The program's squares line up once more: probability = amplitude²,
  metric = channel², bond quantum = charge², ledger = Dirichlet
  square — and now **weight = concurrence squared**.

## 3. The discriminator: tangle, not entropy

Weak coupling (κ = 0.05), deficit per πκ² against the candidate
correlation measures:

| p | C² | E (ent. entropy) | 2E (QMI) | δ/(πκ²) |
|---|---|---|---|---|
| 0.01 | 0.0396 | 0.0560 | 0.1120 | **0.0396** |
| 0.15 | 0.5100 | 0.4227 | 0.8454 | **0.5095** |
| 0.50 | 1.0000 | 0.6931 | 1.3863 | **0.9981** |

The deficit tracks **C² to 3–4 digits** and neither entropy column
(41% off at p = 0.01). **The model chooses its correlation measure:
curvature couples to the tangle, not to entanglement entropy.** The
RT shape — curvature ∝ entropy — is *not* this program's pair-level
prediction. That is a sharp, falsifiable-in-model selection, and it
should be stated as such rather than blurred: if a future
construction demands the entropy coupling, this model is wrong about
it, and conversely.

(Scope note: RT's entropy is boundary-QFT entanglement inside a
duality, not pair entanglement in a network — the contrast says what
*this* model selects, not that RT is incorrect in its own setting.)

## 4. The persistent-pair law

The Bell-basis readout attains Fisher = κ²C² at the phase reference
(2×10⁻¹⁵), and the accumulated record's MI over n shared pairs
converges toward ½ln(1 + nκ²C²) — ratio 0.955 → 0.986 by n = 600,
monotone (slower than 0066's aligned case because the C < 1
channel's Fisher varies with θ). So the deficit law carries over:

```
δ = 2π(1 − e^{−I_record}),   per-pair capacity = κ²C²
```

**Entanglement is the capacity; the record is the account; the
deficit follows the account.** Chained across the three tiers:
trust = precision (0065) → survives as QFI with a dimension-capped
split (0066) → and at the fully relational tier the per-pair
precision *is* the tangle (0067).

## Honest limits

- **One family.** The Schmidt-aligned phase encoding is the cleanest
  relational record, and w = κ²C² is exact *for it*. The misaligned
  example shows local coherence contributes weight without
  entanglement, so the general statement is: relational records ride
  the tangle; local records ride local coherence; a generic record
  mixes both. A decomposition theorem (weight = local part +
  tangle part?) is not proven here.
- **Two qubits.** Concurrence does not generalize simply; higher
  dimensions need negativity or the I-tangle, untested.
- **Pure states.** Mixing degrades QFI; whether w ≤ κ²C² with
  equality iff pure is plausible and unproven.
- The deficit composition still inherits 0019/0020's 2+1 static
  scope; the persistent-pair convergence is numerically monotone but
  slower than the aligned case, and shown at one (p, κ).

## Open

1. **Weight monogamy.** CKW monogamy (C²_AB + C²_AC ≤ C²_A(BC) ≤ 1)
   plus w = κ²C² implies a *per-node cap on total sourced weight*
   across all of a node's pairwise channels: Σ_pairs w ≤ κ². Tangle
   monogamy would become **mass monogamy** — a per-node participation
   bound with the same flavor as the extremal-defect cap. Verify on
   three-qubit states; this is the most exciting new open.
2. **The decomposition**: split a general record's weight into local
   coherence + tangle parts; is QFI = QFI_local + κ²C² on some
   family?
3. **Mixed states**: w vs κ²C² under depolarization — conjecture
   w ≤ κ²C²(ρ) with Wootters' mixed-state concurrence.
4. Standing: t and N; the τ A/B; the bond's h² from redundancy; the
   nonabelian Dirichlet square.
