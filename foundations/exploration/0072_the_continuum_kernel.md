# 0072 — The continuum kernel: the derived simplicity weight in closed form

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Path A's second stone (0070's A1). 0061 derived the Z_N price from a
frame Gauss sum; here the frames become continuous — a, b ∈ ℝ⁴ with a
Gaussian regulator at scale L — and the whole eight-dimensional
integral collapses to a rational closed form in the two simplicity
invariants:

> **K_L(F) = (2π)⁴ / (ε² + ε|F|² + Pf(F)²),  ε = 1/L⁴**

Code: `output/0064_the_continuum_kernel.py` (3 s).

---

## 1. How it collapses

Rotating the alternating matrix ⋆F to canonical form splits ℝ⁴×ℝ⁴
into two frame-planes; each contributes the atomic integral
∬ e^{iλxy − (x²+y²)/2L²} = 2π/√(ε+λ²) twice (verified by quadrature
to 7 digits, semi-analytic and brute). The canonical pair (λ₁, λ₂)
satisfies the exact characteristic identity x⁴ + |F|²x² + Pf² —
machine-checked on 50 random curvatures — so the product
(ε+λ₁²)(ε+λ₂²) is the rational form above. An 8-dimensional seeded
Monte-Carlo bridge on a generic (non-canonical) F confirms the full
integral: 1567.1 vs 1566.6 (0.03%).

## 2. The Z_N structure returns, with a dictionary

The price log(K_flat/K): flat costs 0; simple curvature at |F| = 1
costs **exactly 4 ln L**; the non-simple/simple ratio → **2**
(1.85 → 1.92 → 1.95 at L = 10, 100, 1000 — the parity theorem's
continuum echo). Against the Z_N hierarchy 0 / 2 log N / 4 log N:

> **N ~ L²** — the level is the *square* of the frame scale. The
> ledger squares one more thing.

## 3. What Barrett–Crane never had

With the Euclidean self-dual split, **Pf(F) = (|F⁺|² − |F⁻|²)/2
exactly**, so the kernel is a **Cauchy suppression of the self-dual
imbalance**. As ε → 0 it concentrates on the balanced cone
|F⁺| = |F⁻| — Plebański's constraint, i.e. Barrett–Crane's delta —
measured off/on-cone ratios 4.8e−2 → 4.0e−4 → 4.9e−6 at L = 3, 10,
30. But the derived kernel carries three things BC's bare delta never
specified:

1. **An on-cone measure**: K|_cone ∝ 1/(ε + |F|²) — log-uniform in
   curvature magnitude.
2. **An off-cone tail**: ∝ 1/Pf² — nothing forbidden, the ledger's
   signature suppression, now in the continuum.
3. **A canonical regulator**: ε = 1/L⁴, tied to the frame scale
   rather than chosen.

BC's known pathologies came from the bare delta (frozen intertwiners,
wrong propagator asymptotics); EPRL fixed them by *choosing* a
spread. Here the spread is *derived*, with a specific profile. Whether
that profile passes the graviton-propagator test is exactly 0070's
A2–A3 — this kernel is the per-plaquette weight the one-vertex
nonabelian model will use.

## The filter correspondence

The sibling program (`stat-tracker`) has progressed; a scan of its
current main (PR #18 era) finds three new mathematical workstreams,
and the resonances with this thread are worth recording precisely.

**What's new there**: (i) *filter-optimality-proof* — minimax
optimality with the loss seam removed: both layers now read under
code length (their Theorem A′), the class definition emerging as the
hard part; (ii) *filter-oracle-gap* — the GPB1 collapse (one shared
covariance across the grid) provably flattens the likelihood along a
ridge, repaired by per-node covariances (IMM), with the causal
ceiling measured at 96.3% of oracle; and the decisive negative that
the s_P = 0 boundary is **ill-posed for any point estimator because
Fisher information in a spread parameter vanishes at zero spread**;
(iii) *fractional-ode-filter* — the one categorical integer in the
filter family made continuous (order ν), learnable from both sides.

**The resonances**: the grid-of-filters with per-node lit weights is
structurally the divisor ensemble (a mixture of worlds, each carrying
its own uncertainty, weighted by information dynamics); both programs
price everything in nats; and the fractional-ν lesson — the
categorical made continuous, with the integer faces exact — is 0063's
"discreteness is an output, not an ingredient," discovered
independently on the filter side.

**Give-backs, concretely**:

1. **The boundary cure is the ledger's square.** Their measured
   pathology: Fisher in the spread s vanishes ∝ s² at s = 0, making
   the boundary ill-posed. Reparameterize by τ = s²: I(τ) =
   I(s)·(ds/dτ)² = s²·(1/2s)² = **1/4 — finite and nonzero at the
   boundary**. The amplitude²/probability move (0008's influence =
   √information, B = e∧e, weight = concurrence²) applied to their
   coordinate chart. One line, checkable on their data.
2. **Coherent IMM** (speculative, flagged as such): IMM mixes
   *probabilities* across grid nodes; the quantum ledger mixes
   *amplitudes* and squares. A filter bank carrying complex
   amplitudes with interference between nodes is the
   quantization-esque completion of their own procedure — whether it
   buys anything on classical data is an open experiment.

Also logged: the `formal-languages` repository carries an unmerged
branch (~14.6k lines, explorations 0057–0066: "no finite ħ," "the
paradox tax," "epistricted wall," "sign problem," "braided
holonomy") — apparently the arithmetic-bridge sibling. Not passed
through here; queued, and likely relevant to 0064's Eisenstein note
and 0048's standing arithmetic bridges.

## Honest limits

- Euclidean signature and a Gaussian regulator; other regulators
  (hard box, lattice frames) will shift the on-cone measure at O(1)
  — the *structure* (delta + tail + 4lnL tiers) should be
  regulator-independent, the profile is not proven so.
- The kernel is per-plaquette with independent frames; shared frames
  across plaquettes (0056 §3's correlation) are not folded in — same
  honest limit as 0055 §1, one tier up.
- The MC bridge is the only non-deterministic element (seeded,
  labeled); the deterministic core is the atomic integral plus exact
  algebra.
- The filter give-backs are recorded as suggestions; nothing was
  computed in the filter repo's own harness.

## Open

1. **A2**: the one-vertex nonabelian model with this kernel —
   character expansion, truncated spins, exact partial sums.
2. **A3**: the graviton-propagator test against 0063 — where BC bled;
   the derived spread profile stands or falls there.
3. The regulator-independence of the on-cone 1/|F|² measure.
4. The arithmetic-branch pass (formal-languages 0057–0066); the
   filter give-back experiments (their harness, their data).
