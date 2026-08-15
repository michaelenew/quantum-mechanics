# 0020 — The divergence and the current

O2's rigor and O1's dynamics, pressed together — and the user's
instinct was right that the proof would pay for the dynamics: the
central identity of the derivation (*curvature is a total
divergence*) is simultaneously the missing conservation law. Code:
`output/0015_the_divergence_and_the_current.py`.

---

## 1. The proof of K = πs

Linear tier, every step machine-checked; short enough to write out.

**Step 1 — exact flatness.** A weighted channel's metric
I + w·uuᵀ is, in polar coordinates around its source,
(1+w)dr² + r²dθ² — constant coefficients, hence *exactly* flat off
the apex at any w, with deficit δ(w) = 2π(1 − (1+w)^(−1/2)).
(Checked: |K| < 10⁻⁶ pointwise at w = 0.7.)

**Step 2 — the divergence identity.** Linearizing Gaussian curvature
in g = I + h:

```
K_lin = ∂₁∂₂h₁₂ − ½∂₁²h₂₂ − ½∂₂²h₁₁  =  div V,
V     = ( ∂₂h₁₂ − ½∂₁h₂₂ ,  −½∂₂h₁₁ )
```

For the point channel h = w·uuᵀ the flux through a circle of radius
R evaluates in closed form: V·n = w·cos²θ / R, so

```
∮ V·n ds = w ∮ cos²θ dθ = πw     — for every R.
```

(Checked by finite differences of h alone: flux = πw at R = 0.3, 1,
3 to 10⁻⁴.) Radius-independence + pointwise flatness off the origin
means the linear curvature of one weak channel is exactly a point
measure: **K_lin = πw·δ²**. Since h is linear in the sources,
superposition gives, for a density,

```
K(x) = π s(x)     (weak limit)
```

**Step 3 — the constant, pinned.** The finite-S measurement carries
an O(S) screening term; Richardson extrapolation at S = 0.02, 0.01
removes it: K/(πs) → **1.0002**. The constant is π to 0.02%.

**Step 4 — the screening law, derived.** For a weak channel inside
constant ambient A₀ = I + a·e₁e₁ᵀ, expand the cone integral to first
order in w. det(A₀ + w e_r e_rᵀ) = (1+a) + w(1 + a sin²θ), and with
the two standard circle integrals
∮dθ/(1+a cos²θ) = 2π/√(1+a) and
∮dθ/(1+a cos²θ)² = 2π(1+a/2)/(1+a)^{3/2}, the algebra collapses to

```
δ = πw / √(1+a) .
```

Numerically the general form holds for *any* constant ambient —
biaxial and rotated/correlated cases match to < 2·10⁻³:

```
δ = πw / √(det A₀) :      the local coupling is
                          1 / √(information volume).
```

**Step 5 — the trace identity.** tr h(x) = S_total at *every* point
(machine precision): a channel contributes its full strength to the
trace at any distance. So the isotropic part of the web's field is a
global constant — and constant SPD metrics are flat — meaning **all
curvature lives in the traceless (anisotropy) sector**. This is the
field-level form of the exchange-rate results ("the deficit is
anisotropy-priced"), and it says something sharper: the web stores
its *total* strength locally everywhere (a distinctly holographic
identity), while only the directional part varies and curves.

## 2. Honest negative: the nonlinearity is not bare screening

Does the pointwise atom law δ = πw/√det A explain 0019's finite-S
correction, using the ambient read off the field itself?

| S | measured K/(πs) | bare screening 1/√det A(x) |
|---|---|---|
| 0.1 | 0.9054 | 0.9524 |
| 0.2 | 0.8234 | 0.9091 |
| 0.4 | 0.6896 | 0.8334 |

No — it under-corrects at every S. The finite-strength deviation is
carried partly by **gradients** of the ambient, not by its pointwise
value. The exact nonlinear law stays open, now bounded between the
measured curve and the bare-screening curve.

## 3. The current: O1 and O5 read off the proof

The creative step the user asked for turns out to be a *reading* of
Step 2. Because K_lin = div V[h] is structural — true for any h —
any time-dependence whatsoever gives

```
∂ₜK = div(∂ₜV[h])      ⇒      ∂ₜK + div J = 0,   J = −∂ₜV
```

**The conservation law is not an extra axiom; it is the proof's
central identity run in time.** O5's "participation current" exists
by construction at linear order. Concretely:

- **The jump law.** A moving point defect (w = 0.08) changes a fixed
  loop's transport *only on crossing*: T is constant 0.00000 outside,
  constant 0.23719 (= the atom, exactly) inside, at every sampled
  position. ∫K over a region changes only when a participant crosses
  its boundary.
- **Continuity.** A moving fuzzed source tracks
  d/dt ∫K = π·d/dt(S_enclosed) along its whole path (six stations,
  within 3%): the redistribution law is the continuity equation
  **∂ₜK + div(π s v) = 0** — the linearized Bianchi/conservation
  pair, free of charge.
- **No pair force.** The atom of source 1 is independent of the
  distance to source 2 — constant to a relative spread of 1.6·10⁻⁶
  over d = 0.5…4, and equal to the screened value πw₁/√(1+w₂)
  (the partner's screening is distance-blind, because a channel's
  contribution to the ambient has unit magnitude at any range).
  **Nothing pulls.**

The interpretive claim, stated plainly: the web reproduces the 2+1
situation *exactly*, including its dynamical character. In 2+1
gravity there is no gravitational attraction and no propagating
geometry; matter moves as it moves, and geometry responds by
bookkeeping. The web now has all three pieces of that structure: the
field equation (K = πs), the response law (the continuity equation,
inherited from the divergence identity), and the absence of a pair
force (measured). O1 was posed as "find the missing dynamics of
geometry"; the answer the proof gives is that **in this regime
geometry has no autonomous dynamics to find** — the dynamical
question moves up a tier, to what drives the matter movie itself
(the interaction algebra of the tetrahedron thread) and to the
Lorentzian step (O3), which is now the last structural gap standing
between the web and a genuine 2+1 statement.

## Honest limits

- The proof is the linear tier: exact statements about the cone and
  the flux, plus superposition; the nonlinear regime is measured and
  bounded (§2) but has no closed law.
- The continuity checks are quasi-static (a family of static metrics
  indexed by source position); no retardation or signal speed enters
  — that is O3's territory, untouched.
- δ = πw/√det A₀ is derived for the uniaxial case and measured for
  the general one; a two-line invariant-theoretic derivation of the
  det form should exist and is open.
- "No autonomous dynamics" is a statement about this 2+1 static
  regime, not a theorem about every extension (3+1 defect strings
  can radiate; nothing here speaks to that).

## Open

1. **The nonlinear law**: the gradient contribution to K/(πs) —
   the natural ansatz is a covariant expression in A and ∇A
   (screened density plus a ∇·(A⁻¹∇A)-type term); the data of §2
   is the target curve.
2. **The det-law derivation**: invariant-theoretic one-liner for
   δ = πw/√det A₀.
3. **Retardation** (O3 meets O1): replace the quasi-static channel
   field with a c-bounded update rule for u(x,t) and measure what
   the continuity law becomes — the first place a light cone could
   enter the geometry.
4. **The movie as the driver**: couple source motion to the
   tetrahedron thread's event algebra, so that the matter dynamics
   the geometry bookkeeps is the interaction structure the rest of
   the repo already studies.
