# 0065 — The correlation tier: the deficit is a function of mutual information

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

The gap 0058 flagged as the program's highest-value structural open:
K = πs sources curvature with *participation* density, and nothing
established that participation is a *correlation* measure — so
"correlation sources curvature" was a claimed row with a different row
delivered. This closes it at the classical/Gaussian tier, by
derivation, and the closed form that falls out is sharper than the gap
demanded. It is also the landing site of the trust axis — the
stat-tracker thread's central insight — inside the physics. Code:
`output/0059_the_correlation_tier.py` (0.02 s).

---

## 1. The metric is derived, not posited

Explicit inference network: nodes with positions, channels that
measure line-of-sight separations with Gaussian noise of precision λ,
an isotropic prior as ambient. The Fisher metric on configuration
space — computed as the numerical Hessian of the expected
log-likelihood, no formula assumed — equals

```
g = A₀ + Σ_channels λ · u uᵀ         (max deviation 3.7e−11)
```

which is **exactly the web's metric ansatz** (0019/0020), with the
channel weight identified:

> **w = λ = the precision of the pairwise knowledge.**

The ansatz that 0019 posited and 0020 proved theorems about is the
Fisher metric of an explicit estimation model. Everything downstream —
K = πs, the screening law — now rests on a derived object.

## 2. Precision is the trust axis, and a bijection of mutual information

For a channel built from n samples of noise variance σ²:

```
λ = n/σ²
```

— the **effective sample count**. This is the axis the stat-tracker
thread (0008) calls *trust*: the quantity a point-tracker (Kalman)
folds into its variance and gets away with, because its variance is
free to mean "my uncertainty." A distribution-tracker cannot — the
spread *is* the state — so the sample-count axis must be carried
separately. Here it is carried by the metric itself: **w is the count,
and w is what curves.**

And against a unit prior, the channel's mutual information with the
latent coordinate is

```
I = ½ ln(1 + λ)      ⟺      λ = e^{2I} − 1
```

verified against direct entropy computation. Participation = precision
= trust = a monotone bijection of the pairwise mutual information.

## 3. The deficit law

Composing §1–2 with 0019's exact cone (re-verified geometrically
here — proper radius √(1+w)·r against circumference 2πr):

> **δ = 2π (1 − e^{−I})**

The conical deficit around a channel is a closed-form function of the
channel's mutual information. Every check lands:

- **Weak limit**: δ ≈ 2πI — curvature *linear* in mutual
  information, which is the first-law shape of the entanglement
  literature (Jacobson, Van Raamsdonk — cited for shape, not
  claimed as equivalence; theirs is quantum entanglement in a
  different setting).
- **The expansion** πw − ¾πw² recovers 0019's measured −3w/4
  correction.
- **Saturation**: I → ∞ gives δ → 2π. With δ = 8πGm:

```
m = (1 − e^{−I}) / 4G
```

  **The extremal defect is complete information, and the per-defect
  mass bound m < 1/4G is the statement that mutual information is
  never actually infinite.** 0012's mass cap, 0019's saturating
  atom, and the channel's information content are one formula.
- **The screening law is an information statement verbatim**:
  πw/√det A₀ = πw·e^{−J} with J = ½ ln det A₀ — the ambient's total
  information. The local coupling is damped by the exponential of
  what the neighbourhood already knows. (0059 established this is
  bookkeeping, not varying G — that stands; what is new is what the
  bookkeeping *says*.)

The complement form is worth saying aloud: 2π − δ = 2π·e^{−I} — the
angle that survives is the exponential of the unknown. A channel
about which nothing is known (I = 0) leaves the full circle; a
channel about which everything is known closes it to a point.

## 4. The bond tier is the redundancy tier

Two collinear channels: precisions **add** (Fisher additivity — this
*is* 0041's "charges add," derived). Informations do not add — the
redundancy

```
R = I₁ + I₂ − I_joint = ½ ln((1+w₁)(1+w₂)/(1+w₁+w₂)) ≈ w₁w₂/2
```

lives exactly at the bond's O(w₁w₂) tier, and the measured geometric
interaction of the two deficits is **−3π × R** at leading order
(ratios −9.31 / −9.20 / −9.12 → −3π = −9.42 as w → 0).

Recorded as a structural correspondence, not a theorem: **the bond's
order is the order of overcounted information.** The two-body
nonlinearity the program has chased since 0037 sits at exactly the
order where independent information sources start to overlap.

## Honest limits

- **Gaussian and classical throughout.** The quantum tier — Bures
  metric, entanglement in place of MI, whether δ = 2π(1 − e^{−I})
  survives with quantum I — is untouched and is now the sharpest
  open on this front. The literature's objects (entanglement entropy
  in QFT) are not these objects; §3 claims a *shape* match in the
  weak limit, nothing stronger.
- The measurement model (line-of-sight separations) is chosen to
  match the web's radial channel structure; any relative-coordinate
  measurement yields u-directional Fisher terms, but the specific
  identification is model-dependent at the margins.
- §3's composition inherits 0019/0020's own scope: 2+1, static,
  exact for the lone channel; the anisotropic-ambient case uses the
  weak screening law.
- §4 is a leading-order ratio with slow convergence (−9.12 at
  w ~ 0.1); the −3π is clean but the identification with the 3+1
  bond (0040–0042) is by tier, not by construction.

## Open

1. **The quantum tier**: replace the Gaussian channel with a qubit
   pair, Fisher with Bures, MI with entanglement — does
   δ = 2π(1 − e^{−I}) survive, and with which information measure?
   This is now the precise form of the repo's oldest flagged row.
2. **The redundancy → bond construction**: build the 3+1 bond's h²
   candidate *from* the information redundancy (0060's open 1 with a
   new handle: the strut tension from overcounting).
3. **δ = 2π(1 − e^{−I}) in the quantum lattice**: the Z_N deficit was
   exactly 2πn/N (0054); is there an information reading of n/N —
   the divisor ensemble's level as quantized information?
4. Standing: t and N derivations; the τ-theory A/B (0064); the
   nonabelian Dirichlet square.
