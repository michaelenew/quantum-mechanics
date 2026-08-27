# 0019 — The continuum limit: participation density is mass density

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

O2 — the widest-open obstruction on the curvature map — pressed from
both ends at once, per the two framings on the table: the **limit of
points** (scatter N weak channels and refine) and the **fuzzing**
reading (the point mass becomes a distribution; no points at all).
The conjecture was that both arrive at the same place. They do, and
the place is an equation:

```
K(x) = π s(x)          (weak limit)
```

curvature = π × participation-strength density, pointwise. Registered
through δ = 8πGm this is the static Euclidean 2+1 Einstein equation
K = 8πG ρ_mass with ρ_mass = s/8G. The flagged "correlation sources
curvature" row is now an equation with a measured constant. Code:
`output/0014_the_continuum_limit.py`.

---

## 1. The atom of a weighted channel

Ground work: give a single channel a strength w (metric
I + w·uuᵀ). Then:

- **Exact cone.** A lone weighted channel's deficit is closed-form,
  δ(w) = 2π(1 − (1+w)^(−1/2)), transport-verified at w = 0.1, 0.5, 1.
- **Weak law.** δ → πw as w → 0 (first correction −3w/4): the atom of
  participation is π × strength, so m = δ/8πG ≈ w/8G. This is the
  microscopic coupling the continuum law inherits.
- **Saturation.** δ(w) → 2π from below as w → ∞ (δ(10⁴) = 6.220):
  a single channel approaches but can never exceed the **extremal
  defect** — 0012's per-defect bound m < 1/4G reappears as the
  asymptote of one channel's strength. Mass caps are built into the
  metric's form.
- **Ambient screening — a discovered closed form.** The same weak
  channel inside ambient information I + a·eeᵀ has its atom reduced
  by f(a) — and the measurements at a = 0.25, 0.5, 1 match
  **f(a) = (1+a)^(−1/2)** to < 2·10⁻³. (Isotropic ambient cI gives
  f = 1/c exactly, by two lines of algebra.) Each stiffened ambient
  direction costs a −1/2 power: **ambient information screens new
  participation** — the local coupling runs downward with how much
  the neighborhood already knows.

## 2. Fuzzing dissolves the atom

One Gaussian-fuzzed source (σ = 0.2, total strength S = 0.3): the
channel field is averaged over the source distribution. The
transport profile T(R):

| R/σ | T(R) | π·S_enc | point atom |
|---|---|---|---|
| 0.5 | 0.0563 | 0.0649 | 0.7725 |
| 1.0 | 0.3533 | 0.4090 | 0.7725 |
| 2.0 | 0.6917 | 0.8132 | 0.7725 |
| 3.0 | 0.7824 | 0.9328 | 0.7725 |
| 5.0 | 0.7796 | 0.9425 | 0.7725 |

- **The shell property**: outside the fuzz (R = 3σ, 5σ) the
  transport matches the point atom δ(S) to < 2% — the exterior
  cannot tell a distributed source from a point one, the 2+1 version
  of Birkhoff/Newton's shell theorem, now for information webs.
- **Inside**, T(R) climbs with π × enclosed strength (times the
  finite-S screening), and the apex is simply gone: curvature at the
  centre is **finite** (K = 2.83 on the continuous metric, against
  the divergent 1/d of a point beacon). Matter as a distribution,
  with the point-mass exterior signature.

## 3. The two framings meet

The referee is a third object: the **continuous-source metric**,
computed at each evaluation point by polar integration of the
channel average around that point (the integrand ρ·t is smooth — no
singularity, no source points at any stage). Against its transport
T* = 0.6933 (S = 0.3, σ = 0.25, R = 0.5):

| framing | param | \|T − T*\| |
|---|---|---|
| points (quadrature) | n = 8 → 36 | 0.0036 → **0.0017** |
| cloud (random sample) | N = 16 → 1024 | 0.0267 → **0.0088** |

Both discretizations converge to the continuous-source transport
(the middle of each sequence is non-monotone — lattice/loop
alignment noise, honest and visible in the table — but the endpoints
bracket it and the errors collapse). **The limit of points and the
fuzzed distribution are the same object**, as conjectured; "N weak
defects" and "one smeared mass" are two coordinates on one limit.

## 4. The local law

With the continuous metric, pointwise Gaussian curvature (Brioschi)
against the strength density s(x) = S·ρ(x):

**Weak-field sweep** (at r = 0.15, σ = 0.25):

| S | K/(π·s) |
|---|---|
| 0.02 | 0.9802 |
| 0.05 | 0.9511 |
| 0.10 | 0.9054 |
| 0.20 | 0.8234 |
| 0.40 | 0.6896 |

K/(πs) → 1 as S → 0; the finite-S correction is **negative** with
d(ratio)/dS ≈ −0.93 — §1's screening surfacing at the field level
(the fuzz sits in its own ambient field).

**Spatial tracking** (S = 0.05): ratios 0.952, 0.951, 0.948, 0.941
at r = 0.05 … 0.45 — the law is local: curvature follows the
density point by point, with the uniform ~0.95 offset being the
finite-S screening, not a spatial failure.

So, in the weak limit:

```
K(x) = π s(x)   ⇔   K = 8πG ρ_mass,   ρ_mass(x) = s(x)/8G
```

**Participation density is mass density.** The microscopic atom
(δ = πw), the mass bound (Σm = 1/2G), the shell property, and now
the local field equation all come out of one metric with no tunable
constants — Chentsov forces the geometry, participation sources it,
and the "Einstein-like equation on the information manifold" is no
longer a slogan on the gap list.

## Honest limits

- These are measurements with controlled numerics, not a proof: the
  weak-limit constant π is verified to ~2% at S = 0.02 and by the
  exact single-atom law, but the limit theorem (with error bounds)
  is not written.
- The nonlinear regime is characterized only by its leading negative
  correction; whether the ratio is exactly a screening form like
  1/(1 + βS) with geometric β is open.
- The screening closed form f(a) = (1+a)^(−1/2) is measured at three
  points (and exact for the isotropic case); the anisotropic
  derivation is open.
- Everything remains **Euclidean and static**: O3 (signature) and O1
  (dynamics) are untouched — but O1 now has a field equation to be
  dynamics *of*.

## Open

1. **The two derivations**: K = πs by linearizing the metric (each
   weak atom is a πw delta-function; superposition does the rest —
   should be short), and f(a) = (1+a)^(−1/2) from the cone integral.
2. **The nonlinear law**: pin the finite-S form of K/(πs) — the
   candidate is a determinant/screening factor of the local ambient
   metric, which would make the full (not just weak-field) equation
   explicit.
3. **Dynamics on the equation** (O1, now sharper): the budget is
   topological, so the law is redistributive — what moves s(x,t),
   and does the screening make dense regions resist further
   curvature the way the exchange rate suggests?
4. **The Lorentzian step** (O3): unchanged, and now the only thing
   between this equation and a real 2+1 statement.
