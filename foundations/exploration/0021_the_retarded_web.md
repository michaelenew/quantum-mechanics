# 0021 — The retarded web: where the light cone enters the geometry

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

O3, engaged directly — and no pivot was needed. The move is the one
0020's proof pointed at: replace the quasi-static channel field
(directions point at sources' *current* positions) with the
c-bounded rule — directions point at the **retarded** position,
t_obs − t_ret = |x − y(t_ret)|/c. One change, three results, one of
them an exact law. Code: `output/0016_the_retarded_web.py`.

---

## 1. The moving atom: δ = πw(1 − v²), exact

For uniform motion the retarded time is homogeneous of degree 1 in
position, so the channel field is exactly scale-free and the atom's
linearized weight is computed by 0020's flux integral
(R-independent to 10⁻¹³). Measured at five speeds:

| v | δ/(πw) | 1 − v² |
|---|---|---|
| 0.2 | 0.960000 | 0.96 |
| 0.4 | 0.840000 | 0.84 |
| 0.6 | 0.640000 | 0.64 |
| 0.8 | 0.360000 | 0.36 |

**δ = πw(1 − v²)** to six digits — a discovered exact law (honest
transport confirms at weak w). In the Euclidean web, motion
*suppresses* a source's gravity by (1 − v²).

The signature reading, stated carefully as a reading: under the
analytic continuation v → iv the law becomes **πw(1 + v²)** — a
Lorentzian moving mass gravitates *more*, as relativistic intuition
demands (kinetic energy gravitates). The coefficient of v² is
exactly where Euclidean and Lorentzian kinematics differ, and in
this model that sign is set by the **retarded update rule** — the
state-space metric was never touched. The minus sign lives in the
dynamics, not in the space of knowledge states.

## 2. The fan — and a correction to 0014

The moving source wears a **curvature fan**: because the field is
scale-free, K = f(θ)/r² exactly (measured: K·r² identical at
r = 0.4 and 0.8 to four decimals) — negative ahead (−0.055) and to
the sides (−0.083), strongly positive astern (+0.222) — with
**vanishing angular average**: transport is R-independent to 10⁻⁵
(0.47487 at R = 0.05 and R = 2.0). A moving mass drags an
angularly balanced, scale-invariant curvature wake; its *net*
deficit is the reduced πw(1 − v²).

The fan also exposed a real subtlety. 0014's closed-form deficit
2π − ∮√(EC−B²)/E assumes the apex **develops** into the flat plane,
which requires B = E′/2 — true for the static radial cone, false
for the aberrated one. At w = 0.3, v = 0.6 the formula gives 0.528
against transport's 0.475. Corollary worth recording: **0014's own
0.04% formula-vs-transport gaps were real model error, not
numerics** — beacon apexes are slightly non-developable too.
Transport and the flux integral are ground truth throughout the
thread; the closed form is exact only on the developable subclass.

## 3. The light cone, measured

A source rests at the origin forever, then moves quickly
(peak 0.83c) to a point 0.25 away — still inside a fixed loop of
radius 0.8 — and rests. The loop's transport over time:

| t | T − static |
|---|---|
| −0.2 | −0.0002 |
| 0.5 | −0.0002 |
| 0.9 | **+0.0413** |
| 1.4 | +0.0045 |
| 2.5 | −0.0003 |

- At t = 0.5 the move is **finished** (it ended at t = 0.45) — and
  the loop has not heard: T is unchanged to 10⁻³. No superluminal
  update of the geometry, even though the "event" is over.
- The news shell crosses the loop radius around t ≈ 0.8–1.2 (the
  blip), and T then returns exactly: conservation through the
  transient, as 0020's continuity law requires.
- Scanning curvature along a ray: **K = 0 beyond r = ct to 10⁻⁶** —
  a sharp domain of dependence — and the front's edge tracks
  r = ct at two times (1.186 at t = 1.2; 1.779 at t = 1.8), fitted
  **front speed 0.988c**.

## What this says about O3

The obstruction read "Fisher geometry is Riemannian; spacetime is
Lorentzian; no derivation turns the two-tier split into a causal
cone." The computed answer splits the problem in a way the
obstruction's phrasing didn't anticipate:

1. **The causal cone is not in the state space and doesn't need to
   be.** The web's spatial metric stays Riemannian — it is a space
   of knowledge states, and Chentsov forces it. The cone appears in
   the *response*: with c-bounded channel updates, curvature has a
   sharp domain of dependence expanding at c. Signature-as-dynamics,
   not signature-as-state — which is precisely P2's two-tier split
   (actionable is c-bounded), now computed in curvature rather than
   posited.
2. **The Euclidean/Lorentzian dial is measurable.** The exact law
   δ = πw(1 − v²) puts the signature into a single coefficient; its
   continuation (1 + v²) is the Lorentzian statement. What the
   Euclidean web computes and what a Lorentzian one would compute
   differ by the sign of v² — the same relation Euclidean quantum
   field theory bears to real quantum field theory.
3. **What O3 still owes**: the retarded rule was *imposed*, not
   derived — c enters by hand exactly as the two-tier split states
   it. Deriving the bound (why actionable updates are c-bounded —
   plausibly from the interaction algebra's event structure, where
   influence propagates one crossing at a time) is the remaining
   content of O3, and it is now a question about the update rule
   alone.

## Honest limits

- The retarded web is a specific c-bounded model, not derived from
  the postulates; the results are laws *of that model* (exact and
  measured), offered as the existence proof that a causal cone can
  live in the geometry's dynamics over a Riemannian state space.
- The v → iv reading is an analytic continuation of a measured law,
  not a constructed Lorentzian theory.
- δ = πw(1 − v²) is exact at the linear (flux) tier; finite-w moving
  atoms mix with the fan and were only spot-checked by transport.
- The fan's f(θ) profile is measured, not derived; a closed form
  (the 2D Liénard–Wiechert analog) should exist.

## Open

1. **Derive the fan**: f(θ) in closed form from the aberrated
   profile; check f integrates to zero analytically and whether the
   fore-aft asymmetry is the 2D analog of the velocity field of a
   moving charge.
2. **Radiation**: the kicked source's blip carried curvature
   outward and conservation restored the budget — does an
   *accelerating* source radiate net curvature to infinity
   (measure ∮ at large R vs time), or is the web like 2+1 GR,
   radiation-free in the far field?
3. **Derive c**: ground the retarded rule in the event structure
   (influence propagates one interaction per step — the movie's
   own causality), turning O3's remaining content into a theorem
   of the interaction algebra.
4. **Two moving sources**: the retarded two-body problem — does
   the no-pair-force result of 0020 survive retardation, or does
   motion induce velocity-dependent (magnetic-like) interaction?
