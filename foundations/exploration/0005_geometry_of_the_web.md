# 0005 — Geometry of the web (Fisher / Bures)

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Pressing on: "in the same way gravity falls out of relativity's premise,
something similar may happen here." Concrete answer: the moment we say
"knowledge is a distribution," the web *inherits* a Riemannian geometry
without any further axiomatic choice. This note extracts it.

## The metric is not chosen — it is forced

Given a family of probability distributions `p(x|θ)` parametrized by `θ`, the
**Fisher information metric**

    g_{ij}(θ) = ∫ p(x|θ) ∂_i ln p · ∂_j ln p dx

is (up to scaling) the **unique** Riemannian metric invariant under
sufficient statistics (Chentsov's theorem, 1972). In quantum mechanics, the
analogous invariant metric on the space of density operators — invariant
under CPTP maps that don't discard information — is a *family* (Petz's
theorem), and the **Bures metric** (arising from the symmetric logarithmic
derivative) is the natural choice. Both are, in effect, "the" metric on their
domain, with no wiggle room worth arguing about.

**Two concrete cases (both worked, both used later):**

- **Gaussian knowledge, one dimension `(μ, σ)`.** Fisher metric:
        ds² = dμ²/σ² + 2 dσ²/σ²
  This is (up to normalization) the **hyperbolic upper half-plane** —
  **constant negative curvature.** Geodesics are semicircles orthogonal to
  the σ = 0 boundary. Falling out for free from "knowledge is Gaussian."
- **Pure qubit knowledge.** Bures / Fubini–Study metric on `CP¹ = S²`,
  **constant positive curvature.** Fidelity `F = cos²(α/2)` where `α` is
  the great-circle angle. Verified in `output/0001_qubit_geometry.py`,
  including the Gauss–Bonnet excess formula on a spherical triangle.

## What geometry buys us (the GR-analog, exactly)

| GR (curvature-of-spacetime) | Consistency-first (curvature-of-knowledge) |
|---|---|
| spacetime manifold | manifold of knowledge states |
| Riemannian/Lorentzian metric | Fisher / Bures metric (fixed by invariance) |
| geodesic = free-fall trajectory | geodesic = optimal information path |
| curvature = gravity | curvature = geometric shadow of uncertainty relations |
| mass sources curvature (Einstein) | correlation / entanglement sources curvature (open) |
| light cones = causal structure | two-tier partition of actionable-vs-correlational |
| general covariance | invariance under sufficient statistics / CPTP maps |

The last row is not analogy — it's the same *kind* of principle: physical
content should not depend on how we coordinate/represent it. In GR that's
diffeomorphism invariance; in information geometry it's sufficient-statistics
invariance. Both single out the metric uniquely.

The "mass sources curvature" row is the honest open question — holographic
entanglement (Ryu–Takayanagi) and ER=EPR are the community's groping. I flag
it without claiming.

## Composition as parallel transport; cocycle as curvature

The picture from `0004` (recursive consistency as a cocycle) becomes literal
differential geometry:

- Each edge of the web carries a linear map (composition of knowledge states).
- Composing along a path = **parallel transport**.
- Going around a loop = **holonomy** of the connection.
- Failure of the holonomy to be identity = **curvature**.
- The obstruction to a globally consistent state = the connection's curvature,
  integrated over the graph = a differential-geometric statement of `H¹`.

This lines up cleanly with quantum geometric phases (Berry, Aharonov–Anandan)
and with lattice-gauge theory's plaquette-holonomy = field-strength picture.
Standard differential geometry; the framing brings your posit into contact
with it.

## Uncertainty relations are curvature bounds

On the qubit's positively-curved `S²`, triangles have angular excess
(Gauss–Bonnet): `A + B + C = π + Δ` where `Δ` is the enclosed area.
Numerically verified in `output/0001` (Δ = π/2 for the octant, matched to
machine precision).

That excess is a geometric statement of a QM fact: you cannot pack three
mutually-orthogonal knowledge states into a region smaller than the sphere
allows. For a general N-level system on `CP^(N-1)`, the Fubini–Study
curvature governs the Anandan–Aharonov quantum-speed-limit
`dt ≥ ℏ π / (2 ΔE)` — a curvature bound on how fast a state can evolve to an
orthogonal one. The uncertainty principle, in geometric dress, is the
manifold's shape.

## Engineering tractability

For an engineer, this is not just aesthetic. The quantities that fall out are
the ones already used in quantum-info practice:

- Fidelity ↔ geodesic distance (fixed budget per operation).
- Coherence time ↔ how fast curvature drains a pure state's purity toward the
  interior of the Bloch ball.
- Optimal state estimation ↔ Cramér–Rao bound on the Fisher metric.
- Quantum control ↔ geodesic-following on the state manifold.

The consistency-first framing is compatible with, and centered on, exactly
these tools. If nothing else, that suggests the picture is *ergonomic* for
building intuition.

## Status

- Metric-forced-by-invariance (Chentsov / Petz): **established, cited.**
- Hyperbolic Gaussian manifold, spherical qubit manifold, Gauss–Bonnet: known
  and verified in `output/0001`.
- Cocycle-as-curvature: **framing claim, matches gauge theory / Berry phase**;
  this workstream's job is to make the equivalence with Abramsky–Brandenburger
  sheaves precise. Open.
- Correlation sources curvature (the analog of Einstein's equations for
  information geometry): **speculative**, real active-research territory
  (holography). Named, not claimed.
