# 0068 — The weight decomposition: coherence, tangle, and the Bloch budget

0067 left two opens: the local-coherence/tangle split (open 2) and
weight monogamy (open 1). Both close, and they close as **one
theorem** — a one-line identity on the Bloch sphere whose corollaries
run from 0066's channel to GHZ states. Code:
`output/0062_the_weight_decomposition.py` (0.08 s).

---

## 1. The Bloch budget

For a qubit carrier at node A in a pure two-qubit state, with Bloch
vector r and pointer direction n̂:

```
(r·n̂)²   +   (|r|² − (r·n̂)²)   +   C²   =   1
 bias           local coherence      tangle
```

verified to 10⁻¹⁵ on 200 random states. **The unit Bloch budget
partitions exactly into the decided part, the local coherence, and
the tangle.** One budget, three uses. (The identity is one line:
C² = 1 − |r|² for pure two-qubit states, and the rest is Pythagoras.)

## 2. The decomposition theorem

The channel weight — re-derived from fidelity numerically, matched
algebraically to 10⁻¹⁶ — is

> **w = κ²(1 − (r·n̂)²) = κ²(tangle + local coherence)**

Equivalently w = κ²·Var(pointer): **the weight is the carrier's
undecidedness about its pointer.** The decided part is inert — a
definite record sources nothing (|0⟩|χ⟩ has w = 0 exactly).

Covariance, verified at arbitrary generator directions: the **tangle
part is encoding-independent** (C² does not move as n̂ rotates) while
the **local part rotates with the encoding** and the bias is whatever
n̂ leaves decided. The entanglement contribution to geometry is
intrinsic to the pair; the coherence contribution depends on how the
coordinate is written in.

The poles are the previous two explorations: the relational family is
pure tangle (0067), |+⟩|0⟩ is pure coherence (0066). Both were
special cases of this identity all along.

## 3. Geometry is blind to privacy

Two states with the same weight but opposite splits — one all tangle
(C² = ½, zero coherence), one all local coherence (product state,
C = 0) — produce **identical Bures configuration metrics** (Hessians
equal at the finite-difference floor, 1.1×10⁻⁶).

> The deficit cannot distinguish private capacity from shared
> capacity. It charges undecidedness, wherever it lives. What
> differs is only *who can read the record* — a fact about the web's
> information structure that leaves no geometric trace.

## 4. The ladder, and mass monogamy

The identity holds verbatim for any pure *global* state, with the
tangle read as the node-vs-rest bipartite tangle 4·det ρ_A = 1 − |r|².
For three qubits, CKW (Coffman–Kundu–Wootters) then splits the tangle
into pairwise plus collective:

```
w/κ²  =  coherence²  +  C²_AB  +  C²_AC  +  τ₃
```

with τ₃ ≥ 0 the three-tangle. Verified on 200 random three-qubit
states (0 violations; the mixed-state Wootters concurrence computed
via characteristic-polynomial eigenvalues with zero-root deflation —
validated against the pure formula exactly, W-state's C_AB = 2/3, and
GHZ's C_AB = 0). The poles:

| | w/κ² | pairwise | three-tangle |
|---|---|---|---|
| GHZ | 1.0000 | 0.0000 | **1.0000** |
| W | 0.8889 | **0.8889** | 0.0000 |

Three consequences:

1. **The ladder**: weight = κ²(local coherence + Σ pairwise tangles
   + collective tangle) — private capacity, shared capacity, and
   collective capacity, each rung charged equally by geometry.
2. **Mass monogamy** (0067 open 1, delivered): a node's pairwise
   relational weights sum to at most its node-vs-rest tangle, which
   sums with coherence to at most κ² — **a per-node sourcing cap**,
   the web-level echo of the extremal-defect bound, now a theorem
   inherited from CKW rather than a measured asymptote.
3. **A P1 refinement**: GHZ's weight has *no pairwise carrier* — all
   its capacity is collective, invisible to every pair. So
   postulate P1's "all content is pairwise" must be read as
   **node-vs-rest** bipartitions, not literal pairs: collective
   entanglement sources geometry that no pair accounts for. This is
   a genuine sharpening of the program's first postulate, forced by
   a three-qubit example.

## Honest limits

- Pure global states throughout. Mixed global states degrade QFI
  below the variance (SLD formula); the conjecture w ≤ κ²(budget
  form) with equality iff pure is untested.
- Qubit carriers. Higher-dimensional pointers change 1 − (r·n̂)² to
  a genuine variance and C² to a higher-dimensional tangle;
  the clean budget identity is qubit-specific as written.
- The three-qubit ladder uses CKW, which is proven for qubits;
  beyond qubits monogamy can fail, so the mass-monogamy statement
  is currently a qubit-web statement.
- The deficit composition inherits 0019/0020's 2+1 static scope.

## Open

1. **The mixed tier**: w vs the budget under decoherence — does the
   weight decompose as (surviving coherence) + (surviving tangle)
   with a leakage term, and is decoherence literally the transfer of
   weight from capacity to bias (decided-ness)? That would make
   *collapse = geometric discharge*: a measurement converts sourcing
   capacity into inert record. Sharpest next question.
2. **Higher tangles**: four qubits and up — does the ladder continue
   (pairwise + three-tangles + four-tangles...), and does each rung
   stay equally charged?
3. **P1 formalization**: restate the postulate with node-vs-rest
   bipartitions and check nothing downstream shifts.
4. Standing: t and N; the τ A/B; the bond's h² from redundancy; the
   nonabelian Dirichlet square.
