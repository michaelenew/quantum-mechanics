# 0071 — The RG probe: where the program bleeds

Path A's first stone (0070's A0), executed. The ledger weight has no
coupling knob — it is *derived* (0064) — so which phase it sits in is
a fact about the program, not a parameter choice. In the abelian
sector that fact is exactly computable, and it answers the question
directly. Code: `output/0063_the_rg_probe.py` (0.04 s).

---

## 1. Blocking is a dual power; the ensemble is RG-closed

In the 2D flux representation, merging 2×2 plaquette blocks sums the
four fluxes, so the blocked weight is the 4-fold cyclic convolution —
in the dual basis, **Ŵ′ = Ŵ⁴ exactly** (integer arithmetic, N = 12).
Functions of gcd(n, N) are closed under powers, so:

> **The divisor ensemble is an RG-invariant family.** Blocking is a
> flow on the divisor simplex, and the pure levels (BF at each
> divisor) are its fixed points.

The measure the program derived is not just a point — it lives in a
family the RG preserves. That is a structural gift: the flow can be
followed exactly.

## 2. In 2D the jitter wins totally

The ledger's level shares under successive blockings (N = 12): the
free sector goes **0.300 → 0.914 → 1.000**. Two blockings and the
constraint content is gone — which is 0055's measured area law,
re-read as an RG flow to the free fixed point. D = 2 spacetime
gravity is empty anyway; no loss, but total.

## 3. In 3D the ledger is confined

Wegner duality rewrites the 3D Z_N gauge theory *exactly* as a spin
model whose bond weights are the dual ledger weights (0064's
Ŵ = G(gcd)). For prime N the ledger is two-valued and the couplings
are exact:

| N | dual model | ledger coupling | cited K_c | phase |
|---|---|---|---|---|
| 2 | 3D Ising | ½ln 3 = 0.549 | ≈ 0.2217 | ordered ⇒ **confined** |
| 3 | 3-state Potts | ln(5/2) = 0.916 | ≈ 0.5506 | ordered ⇒ **confined** |

Deep in the ordered phase both times: Wilson magnitudes obey an area
law at every scale. **The 3D vacuum measure sustains no long-range
rigid geometry.** (Consonant, at least, with 2+1 gravity being
topological — there are no local geometric dof to be rigid — but the
honest statement is that the vacuum ensemble's large-loop geometry
washes out; the finite-lattice results of 0054–0055 are near-source,
small-scale statements and stand.)

## 4. In 4D, rigidity begins at N = 3

4D Z_N gauge is self-dual, and the two-valued family (weight r on
F = 0, 1 otherwise) is closed under duality with the exact involution
r ↦ (r−1+N)/(r−1) and self-dual point **r\* = 1 + √N**. The ledger
sits at r = N:

| N | r | r* | phase |
|---|---|---|---|
| 2 | 2 | 2.414 | **confined** |
| 3 | 3 | 2.732 | **deconfined** |
| 5 | 5 | 3.236 | **deconfined** |
| any N ≥ 3 | N | 1+√N | **deconfined** ((N−1)² > N) |

Under the standard single-transition assumption:

> **The derived measure first supports long-range rigid geometry in
> four dimensions, and only for N ≥ 3.**

Two firsts. The program's first *internal* evidence selecting D = 4 —
the arena assumption (0069's F) earns its first support, from the
measure itself rather than from a choice. And the first derived
constraint on the knob: **N ≥ 3**, with N = 2's failure joining its
long-standing degeneracies (excluded from Kulkarni–Nomizu, from the
SD/ASD split, anomalous in the divisor ensemble).

## Where it bleeds — the honest ledger

- **D ≤ 3: bled.** The abelian interacting vacuum has no long-range
  geometry below four dimensions. The jitter wins at all scales.
- **D = 4, N ≥ 3: survives its first test** — but deconfined Z_N is
  *topological order*: rigidity without gravitons. Z_N has no
  massless mode; 0061 §4's finiteness ceiling stands. The substrate
  is rigid; the propagating modes still require the continuous group
  (0063). The marriage of the two is exactly 0070's A1–A3.
- **The bleed-line moves to**: the N ≥ 5 intermediate-phase caveat
  (4D Z_N clock gauge has a three-phase structure for large N with
  standard actions; the two-valued ledger action may differ — not
  resolved here), and the nonabelian tier.

## Honest limits

- 3D K_c values are cited literature numbers, not computed in-repo —
  the couplings are exact, the comparison is not self-contained.
- 4D placement assumes a single transition at the self-dual point
  (standard for N = 2, 3; the N ≥ 5 caveat above).
- Abelian and Euclidean throughout; Wilson-loop magnitude is the
  rigidity criterion — source sectors and protected phases may
  behave differently in the confined phases.
- The 2D/3D/4D lattices are hypercubic; universality is assumed
  where cited K_c's are used.

## Open

1. **The N ≥ 5 phase structure of the two-valued ledger action** in
   4D — does the intermediate phase open, and where does the ledger
   land? (Determines whether the N ≥ 3 window is bounded above.)
2. **The 4D deconfined phase's topological entanglement entropy** —
   path C's alternative route, now tied to the established phase.
3. **A1 of 0070**: the continuum frame kernel — the delta-plus-tail
   structure of the continuous simplicity weight.
4. Standing: Λ1 (budget with boundary); C1 (graviton half-space
   entanglement); the nonabelian blocking question raised by §1.
