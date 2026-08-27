# 0125 — The induced stiffness: the gravity channel's precision, measured

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Code: `output/0113_the_induced_stiffness.py`.

lucid 0032 closed the matter coupling as a formula — the stress
tensor is the local record's Fisher information, and
**G = 1/(4πp)** with *p* the record precision of the channel that
carries gravity. That turned "direct G" into a single measurement
with a target. This module makes it.

## 1. The object, and why its normalisation is not free

Gravity here is *induced*: the trust field λ has no bare action, so
its entire dynamics is what the matter's own record generates. The
filter fixes λ's normalisation — a node transmits e^{−2I} of an
incident influence (lucid 0010), which on the lattice is the link
weight **w = e^{2λ}**, exactly the D = 4 conformally-flat matter
coupling √g g^{μν} = e^{2λ}δ. Integrating out one massless lattice
scalar gives Γ[λ] = ½ ln det′(DᵀWD); *p* is the coefficient of
½|∇λ|² in its quadratic part.

Nothing here is tuned. The same λ that couples to matter is the one
whose stiffness is measured, so *p* is a number, not a convention.

## 2. The induced scale action is massless and positive — a theorem

With **B = D M₀⁻¹ Dᵀ** the orthogonal projector onto gradient link
fields,

> Γ″[λ] = Σ_{l,l′} B_{ll′}² (λ_l − λ_{l′})²   identically.

Two consequences fall out with no input:

- **Positive semidefinite.** The scale channel is stable.
- **Kernel = exactly the constants.** There is *no induced mass
  term*. A uniform λ multiplies every link weight by e^{2λ} and
  shifts ln det′ by exactly 2λ(V−1) — linear, so the k = 0 quadratic
  response vanishes identically (verified to <1e−6 at L = 6, 8).

So the massless mode lucid 0019 needs is not a tuned coincidence on
this side either; it is forced by the structure of a determinant.
This also disposes of an apparent conflict: 0124 measured the
plaquette *scale field* screened within ~0.32 a, but that is a
composite observable — the trust channel itself is exactly massless.

And the stiffness has a reading: **B_{ll′}² is how much two links
share a mode.** Precision comes from record overlap.

Verified against dense log-determinants at L = 6 and 8, agreeing to
≤7e−6 at every momentum.

## 3. The number

| L | 12 | 16 | 20 | 24 | 28 | 32 |
|---|---|---|---|---|---|---|
| p(L) | 0.153106 | 0.153893 | 0.154264 | 0.154467 | 0.154590 | 0.154670 |

1/L² extrapolation: **p = 0.154932** per field (the same
extrapolation one size down gives 0.154931 — six stable digits).

|  | value |
|---|---|
| measured, graviton (2 polarisations) | **0.30986** |
| target from lucid 0032 (G = 5.165 a²) | **0.01541** |
| plaquette weight's local precision | 13.337 |

> **The prediction is wrong by 20×, and wrong in the unexpected
> direction: the gravity channel is too STIFF, not too soft.**

The predicted softness ratio against the plaquette weight was 866×.
Measured, it is **43×**. The channel *is* much softer than a single
plaquette — the qualitative expectation held — but by a factor 20
less than the induced-gravity value of G requires.

## 4. The residue is field-count independent

The obvious escape is the number of gravitating polarisations. It is
not available. Both routes to G scale as 1/N:

- entanglement route (0115 s1b): G = 1/(4Nα)
- matter-coupling route (lucid 0032): G = 1/(4πNp)

so their ratio does not:

> **G_entanglement / G_induced = π p / α = 20.11**, for any N.

| N | G_ent | G_ind | ratio |
|---|---|---|---|
| 1 | 10.331 a² | 0.5136 a² | 20.11 |
| 2 | 5.165 a² | 0.2568 a² | 20.11 |
| 6 | 1.722 a² | 0.0856 a² | 20.11 |

2π² = 19.739 sits 1.9% away. **Priced, not claimed**: α itself is
converged only to about a percent, and one near-miss at n = 1 is not
evidence — the same standard 0124 applied to McKay.

## 5. What this actually closes and opens

**Closed.** Direct G is now a measured number rather than a named
measurement. The masslessness premise the whole derived-gravity
chain rests on is proved on this side, exactly, rather than assumed.

**Opened, and sharper than what it replaces.** The two routes to
Newton's constant disagree by a pure number ≈ 20. That is not a
units problem (both are in lattice spacings), not a field-count
problem (proved above), and not a convergence problem (six digits).
It is a genuine disagreement between *entanglement across a cut* and
*stiffness against a smooth deformation* — two regulators of the
same loop. Reconciling them is one calculation, and it is now the
entire content of what "direct G" means.

Worth naming honestly: reading G from the scale channel is where
Einstein–Hilbert's conformal mode has its *negative* kinetic term,
while the induced form measured here is provably positive. The
filter's gravity is a scalar theory in λ and is stable; GR's
conformal sector is not. These are not the same object, and the
factor 20 may well live in exactly that gap.
