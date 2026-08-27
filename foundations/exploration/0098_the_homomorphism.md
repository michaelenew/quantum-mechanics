# 0098 — The homomorphism proper: what transports, and what the gap is made of

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Step 2 of the crossing plan, delivered. Both families stated as one
kind of algebraic object, the structure-preserving map proved where
it holds, and — the part that turns the toy into a prototype — the
failure *located and quantified*, not just listed. Three theorems,
one catalogue. Code: `output/0088_the_homomorphism.py`.

The claim of the word "homomorphism," stated honestly up front: an
explicit structure-preserving correspondence proved/verified on the
free and cycle tiers, plus a located, measured failure list. Not a
categorical functoriality proof for the full interacting theories.

---

## Theorem 1 — the free tiers are isomorphic

Both families' one-step maps are the **same polar transfer**, on
different groups:

```
filter predict (group ℝ):    mode k  →  e^{ikμ} · e^{−qk²/2} · mode k
ledger chain  (group Z_N):   mode n  →  ω^{nf} · e^{−τn²}   · mode n
```

Drift/source in the phase, noise/record in the modulus — the
two-ledger polar theorem (0086) is a *statement about Kalman
filtering* when the group is ℝ. Verified: the Kalman factorization on
an arbitrary bimodal density to 5e−16; the ledger side's flatness of
−ln r_n/n² to 9e−16; source = pure phase re-verified; both semigroups
compose additively (q + q′ ↔ τ + τ′). **One object, two groups; the
map is "swap the group."**

## Theorem 2 — one MK blocking is one Kalman cycle

The Migdal–Kadanoff recursion decomposes as the filter's own cycle:

- **bond move** (pointwise power W^ζ) = **Bayes update** on ζ−1
  independent parallel replicas — pointwise product of weights is
  exactly how parallel bonds compose, and conditioning a Gaussian on
  ζ−1 agreeing replicas multiplies precision by ζ (exact algebra);
- **decimation** (b²-fold series composition, r → r^{b²}) =
  **predict**.

So the RG is a *self-measuring filter*: each blocking, the theory
observes itself through its parallel bonds and forecasts itself along
its series bonds. τ is the posterior variance; the conjugate families
correspond (Gaussians exactly closed under the cycle; the heat-kernel
family closed to 1.4e−6); and the beta function is the variance
recursion's residue. On the filter's own state space ℝ, with the 4D
exponents ζ = b², the residue **vanishes identically**:
predict ×b², update ÷b², net 1. β_ℝ = 0, exactly.

## Theorem 3 — the gap is noncommutative curvature, not compactness

The same cycle run on three groups:

| group | character | β |
|---|---|---|
| ℝ (the filter's state space) | e^{ikx} | **0, exactly** (algebra) |
| U(1) (compact, abelian) | e^{inθ} | **< 1e−6 for τ ≤ 0.4** (winding terms ~ e^{−π²/τ}, invisible) |
| SU(2) (compact, nonabelian) | χ_j | **0.127·τ²** (0093, re-verified) |

Compactness alone changes nothing measurable. The entire dynamical
content of the wall — the running of the coupling, the emergent
scale, the confining runaway — is the residue of **one structural
ingredient: noncommutative group curvature**, and it is precisely the
ingredient the filter's flat state space lacks. Asymptotic freedom is,
in this exact sense, *the failure of the filter analogy, quantified*:
β = cτ² is the homomorphism's defect, and we have its coefficient.

## The isomorphism gap — the toy-to-prototype upgrade list

**What transports (proved/verified):** the free tier (polar transfer
semigroups, Theorem 1); the predict/update cycle (Theorem 2); the
conjugate-family/closure logic (0092 ↔ Kalman-Gaussian); pinned roots
= masslessness (0096); marginalization = hypothesis sets (0097).

**What fails, where, and what building it would mean:**

1. **Group curvature** (Theorem 3) — running, transmutation,
   confinement. Prototype upgrade: filtering on curved,
   noncommutative state spaces — directional statistics on S³. A
   walking filter whose level lives on a sphere would *have* a beta
   function; its regret would run.
2. **External innovations** — the physics only self-conditions
   (parallel replicas); there is no outside data stream. That absence
   *is* the missing time/measurement/causal layer (the wall's one
   permanent stratum, per the filter's own 3.7%). The physics'
   measurement problem, in filter words: *who supplies the
   innovation?*
3. **The hypothesis bank** — the physics vacuum is a point hypothesis;
   0097 measured the cost (sector structure erased) and the cure
   (marginalize the vacuum's scale — their (φ_P, s_P) grid).
4. **Discrete sectors** — the physics has superselection (the center,
   the rep labels); the filter's counterpart is discrete *regimes*,
   which are exactly what their shipped family lacks (their 6.8%
   stratum is "AR(1) vs regime"). **Pressing regime-hazard on the
   filter side is not adjacent to this gap — it is this gap**: it
   builds the filter's sector tier, the doppelgänger of
   superselection. The owner's pressure-point instinct lands on the
   catalogue's fourth row exactly.

## What this buys

The blueprint reading is now live: for any physics question, ask
which tier it lives on. Free tier / cycle tier → the filter answers
are *theorems here too* (transport them). Curvature tier → the
filter cannot see it; only the physics (or a curved-state-space
prototype) can. Data/causal tier → neither side has it; it is the
wall's foundation. Bank/sector tiers → the filter is the cheaper
laboratory, and its next two shipped designs (scale marginalization,
regime-hazard) are literally the two missing structures.

## Honest limits

- Theorem 2's replica reading of the bond move is exact for the
  hierarchical (MK) lattice, where parallel-bond pointwise
  multiplication is the composition rule; on the hypercubic lattice
  MK is an approximation and inherits that status.
- Theorem 3 localizes the gap at the level of "which group produces
  the effect"; the mechanism inside SU(2) (Weyl measure vs C₂'s
  linear term) is identified but not dissected term by term.
- U(1)'s β bound is numerical (grid 4e5, τ ≤ 0.4); the winding-term
  scaling is stated from theory, not measured (it is below the
  floor).
- Gaps 2 and 4 are located, not built.

## Open

1. The prototype's first brick: a minimal filter on a compact
   noncommutative state space (S³ random walk with heat-kernel
   steps) — verify its regret *runs* with the measured c-shape; the
   filter-side experiment that would confirm the gap-1 diagnosis
   from their side of the wall.
2. Regime-hazard (gap 4) — per the owner, the next pressure point;
   now with its physics meaning attached (building superselection).
3. The innovation question (gap 2) as a formal statement: what
   external stream, if any, does the physics admit? (This is the
   measurement thread's cleanest formulation to date.)
4. Fold the blueprint into the standing queue: the strong-coupling
   MC's target (the vacuum's radial mixture, 0097) is a bank-tier
   question — the filter's marginalization design applies as-is.
