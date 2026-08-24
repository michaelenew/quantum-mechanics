# 0103 — The time tier: Euclidean = smoother, Lorentzian = filter

First of three stones completing the isomorphism where it can be
completed (the missing tiers, in tractability order: time, network,
prequential — this is time). The structural seam: the filter is
causal; the physics' measure is Euclidean with no arrow. Closed, at
every tier where the isomorphism is proven.
Code: `output/0093_the_time_tier.py`.

> **The Euclidean measure is the smoother; the filter is its causal
> half; the dynamics is the same object in both readings. The
> Lorentzian lift removes end-conditioning and nothing else.**

- **ℝ tier, exact**: the Euclidean propagator on a Dirichlet chain
  (inverse tridiagonal Laplacian) *is* the smoother covariance
  s(T−t)/T, entrywise (1e−13); its diagonal is the forward/backward
  precision sum (1/t + 1/(T−t))⁻¹. The causal half alone has
  variance t — the massless linear growth, i.e. the pinned root
  (0096) is literally the smoother's end-pin.
- **U(1) tier**: the end-conditioned Euclidean chain marginal,
  computed by brute grid contraction, equals forward-message ×
  backward-message (wrapped heat kernels) at 5.5e−15.
- **SU(2) tier**: same identity by characters (semigroup at 4.5e−16),
  **and the smoother inherits 0099's curvature tax exactly**: the
  bridge fusion satisfies p_bridge = p_fwd + p_bwd − 2/3, the defect
  width-independent and converging to −2/3 = −4δ (δ = 1/6) as widths
  → 0. Mechanism: each single message's van Vleck factor θ/sinθ
  cancels half the Haar curvature (a +1/3 precision bonus); the
  product completes the cancellation and pays both bonuses back.

**Causal attainability, now exact at the free tier** (the F3
template): the fraction of smoother precision available causally is
1 − t/T on ℝ — linear decay toward the far end — with the SU(2)
curve sitting just above it (0.894/0.783/0.545/0.286/0.146 at
t/T = ⅛…⅞), shifted by the tax. The entropy cost of causality is
½ ln(p_smoother/p_filter) per site: computable, bounded, zero at the
near end. F3's question "which posterior structures survive the
causal restriction" now has an exact free-tier answer to calibrate
the bank-level experiment against.

## Honest limits

- Chain topology only; the network version of the identity is
  0104's subject (the lattice's Gaussian sector *is* a smoother, so
  the extension is made there quantitatively).
- "Lorentzian lift = choose an order" is exact for the *measure's*
  reading (verified again at the prequential tier, 0105); the
  dynamical signature question (⋆² = −1, 0081's congruence) is a
  separate, already-proven kinematic layer — this stone does not
  touch representation content.

## Open

1. The bank-level attainability experiment (F3 proper, filter-side)
   now has an exact yardstick; run when the queue reaches it.
2. The tax in the smoother suggests every fusion in a curved-state
   filter pays 2δ per message pair — check against the S³ filter's
   multi-step smoother (0099's association problem).
