# 0023 — The compass and the flyby: O3′ decided

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

The boost-covariance test, run as the relativity principle itself:
*can any internal experiment on a co-moving system detect the common
velocity?* The answer is yes — cleanly, with the violation's exact
shape measured — so O3′ is decided, negatively, for the bare
retarded web, and the measurement specifies what a covariant
completion must add. Radiation and the two-body flyby are chased in
the same run. Code: `output/0018_the_compass_and_the_flyby.py`.

---

## 1. The covariance test: the web has an internal compass

The instrument: the screened moving atom, extrapolated to zero loop
radius (Richardson in R²), inside a constant ambient channel at
angle ψ to the motion. Numerical floor calibrated at 7×10⁻⁹ —
three orders below the smallest signal.

| v | ψ=0 | ψ=45° | ψ=90° | split |
|---|---|---|---|---|
| 0.0 | 0.818509 | 0.818509 | 0.818509 | −6×10⁻⁸ |
| 0.3 | 0.818637 | 0.818576 | 0.818516 | 1.21×10⁻⁴ |
| 0.6 | 0.819135 | 0.818892 | 0.818648 | 4.86×10⁻⁴ |

- At rest the screening is **direction-blind to 10⁻⁶** (the det law,
  as derived in 0020).
- In motion an orientation split appears: **pure cos 2ψ** (the 45°
  point sits at the midpoint to 10⁻⁵), scaling **exactly as v²**
  (split ratio 4.01 between v = 0.6 and 0.3).
- In situ, a co-moving pair shows the anomaly larger (the partner's
  field gradients contribute) plus a **fore-aft dipole**:
  ahead 0.821564 vs behind 0.818564 (+3.0×10⁻³) vs side 0.817178 —
  the aberration of the partner's direction breaks front-back
  symmetry.

**Verdict (O3′): the bare retarded web is causal but not
boost-invariant.** A co-moving observer can read their absolute
velocity — magnitude and direction — off a quadrupole compass at
order v², with a dipole refinement from any companion. The causal
cone (0021–0022) does not imply the relativity principle.

**Diagnosis**, by the exact electromagnetic analogy: a *retarded
scalar potential alone* fails covariance in precisely this way; the
cure in EM is the velocity-coupled vector sector (the magnetic
potential). The web carries only the "electric" channel field
u·uᵀ; covariance requires the gravitomagnetic (h₀ᵢ-type) sector,
and the measured multipoles — quadrupole ∝ v²·cos2ψ in constant
ambient, plus the gradient-fed dipole — are the specification of
the counterterm that sector must supply.

## 2. Radiation: no wave zone, and an airtight budget

- **Baseline**: under the instantaneous rule, off-source curvature
  is zero exactly (a displaced cone is a cone) — all far-field
  curvature is retardation-made.
- **No wave zone**: the oscillating source's far curvature decays
  with exponent **p = 3.07** — pure near-field. Radiation in 2D
  would decay as R^(−1/2); even the kinematic 1/R guess cancels.
  The retarded web is **radiation-free under periodic motion, like
  2+1 gravity itself**; with |u| = 1 there are no independent field
  degrees of freedom to radiate.
- **The budget**: the enclosed transport through the cycle averages
  to the *static* atom **exactly** (0.15142 vs 0.15142), breathing
  under 1% as the near-zone wave crosses the loop. So the
  moving-atom suppression (1 − v²) is a **redistribution into the
  near zone, not a loss** — and eternal uniform motion displays the
  bare (1 − v²) at every radius only because its compensating front
  departed in the infinite past. Conservation is airtight at every
  stage.

## 3. The flyby: gravitomagnetism, measured

A light probe (w₁ = 0.02, v = 0.6) passes a heavy static partner
(w₂ = 0.5) at impact parameter 0.5. The probe's atom ratio through
the encounter:

```
X:      -1.2       -0.6       0.0        0.6        1.2
ratio:  0.819592   0.819623   0.818648   0.818251   0.818534
```

against a static-static baseline that is flat to 1.3×10⁻⁶ over the
same track. **Relative motion induces an orientation-dependent
two-body coupling absent in the static theory** (0020's
no-pair-force), asymmetric between approach and recession — the
web's gravitomagnetism. Note the two-body structure is regular and
small (10⁻³-scale at v = 0.6): motion turns on a coupling, not a
Newtonian-style attraction.

## What closing O3′ leaves standing

The signature program now reads, in full: causal cone derived
(0022), signature-as-dynamics measured (0021), relativity principle
**false for the bare web** with the violation characterized to
multipole precision (this exploration). The remaining construction
is no longer a test but a build: the covariant completion.

One sharp observation constrains it. An *extrapolated* update rule
(channels point at the retarded-position + retarded-velocity ×
delay — still causal, built from retarded data only) would make
uniform motion exactly undetectable — restoring the relativity
principle *Galileo's way*, with no (1 − v²) at all. In EM, what
makes the answer Lorentz rather than Galileo is that the uniformly
moving charge's field points at the present position but with
**anisotropic strength** (1−v²)/(1−v²sin²θ)^(3/2). The web's
channels are constrained to |u| = 1 — unit strength — which is
exactly what blocks the Lorentzian option. **The covariant
completion must therefore promote channel strength to a dynamical,
velocity-dependent quantity** — i.e., the h₀ᵢ sector again, seen
from a second direction. Both diagnoses converge on the same
missing object.

## Honest limits

- The compass coefficients are measured at one ambient strength
  (a = 0.5) and one pair weight; scalings in a not swept.
- The radiation exponent is measured at one (A, Ω); the cycle-mean
  budget was checked at two frequencies (identical).
- The flyby curve is an observable, not a force law — the model
  still has no matter dynamics to deflect the probe.
- "Specification of the counterterm" means the anomaly's measured
  shape; the covariant completion itself is not constructed here.

## Open

1. **Build the completion**: velocity-dependent channel strength
   (the h₀ᵢ sector), tuned to cancel the compass multipoles; check
   whether the cancellation forces the Lorentzian strength profile
   uniquely (the EM precedent says yes at linear order).
2. **The Galileo/Lorentz dial**: bare retarded (ether), extrapolated
   (Galileo), strength-corrected (Lorentz?) — one model family, the
   symmetry decided by the update rule; locate what principle picks
   the middle option out.
3. **Closed forms**: the v²cos2ψ quadrupole coefficient and the fan
   f(θ) from the aberrated profile.
4. **Matter dynamics**: give the probe an equation of motion and
   see whether the flyby coupling deflects it (the web's analog of
   frame dragging).
