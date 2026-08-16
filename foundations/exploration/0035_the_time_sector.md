# 0035 — The time sector: the covariant null-channel metric

0034 named the time sector (lapse/shift) as the program's sharpest
missing construction. Built here — and one construction absorbs
three fronts at once: **the time sector, the strength dynamics, and
the velocity-statics anomalies of 0023/0024/0025**. Code:
`output/0030_the_time_sector.py`.

---

## 1. The construction, derived

For a source worldline z(τ) with 4-velocity u, let ℓ = x − z_ret be
the retarded null vector (past-light-cone intersection), and
normalize the channel by the **sender's clock**:

```
k_μ = ℓ_μ / (u·ℓ)              (covariant components)
g_μν = η_μν + w k_μ k_ν         (Kerr–Schild form)
```

Three consequences follow by algebra, each machine-verified:

1. **The web is the slice.** Static source: u·ℓ = ℓ⁰, so
   k = (−1, n̂) and the t = const spatial block is exactly
   I + w n̂n̂ᵀ (verified to 1e−12). The spatial theory of
   0031–0034 was the slice of this object all along.
2. **The strength law is derived, not chosen.** Moving source:
   u·ℓ = γℓ⁰(1 − n̂·v), so k = D(−1, n̂_ret) with
   D = 1/(γ(1 − n̂·v)) — the moving slice is I + wD²n̂n̂ᵀ
   (verified exactly): **w_eff = w·D², the Doppler-squared law.**
   The strength sector's dynamics is the retarded kinematics of the
   sender's proper time. Another choice that's not a choice.
3. **Boost covariance is automatic.** Light cones and proper time
   are Lorentz constructions, so the machinery run on the boosted
   worldline equals the Lorentz pullback of the static metric —
   verified pointwise to 4e−16. No baseline, no counterterm:
   **0024's boosted baseline was the slice shadow of the null
   structure**, and the compass (0023), baseline-necessity (0024),
   and in-model Michelson–Morley (0025) anomalies dissolve by
   isometry. (An index lesson en route: the assembly must use
   covariant components — kkᵀ built from contravariant components
   passes every static test and fails the boosted one, caught by
   the pullback identity.)

The instrument behind these checks is the new 4D pipeline
(Riemann/Ricci/Einstein), validated on flat (exact), static
Schwarzschild–Kerr–Schild (vacuum to 5e−7), and **boosted (v = 0.5)
Schwarzschild built by the covariant machinery itself** (vacuum to
3e−7) — the pipeline and the normalization validated together on
the GR side.

## 2. The implied matter — closed forms

- **The constant-w point channel is exactly the global monopole**:
  G^t_t = G^r_r = −w/r² to five digits at two radii, zero
  tangential stress — the global monopole equation of state.
  Coordinate reduction (algebra): completing the square in the
  cross term gives ds² = −(1−w)dt′² + dr²/(1−w) + r²dΩ².
- **The static string's lift is flat off-axis** (1e−6): the
  cosmic-string spacetime — pure tension on the axis, the BF
  sector's exact GR counterpart.
- **GR's point mass is the same Kerr–Schild form with
  w = 2M/(u·ℓ)**: web-vs-GR statics is a strength *profile*
  (constant participation vs 2M/ρ), not a structure. The Newtonian
  question — what makes w run as 1/ρ — is now one sharp question.
- **The codim ladder, general c** (closes 0033's open #3):
  transverse-sphere tangents are orthogonal to r̂, hence
  unstretched, while proper radius is √(1+w)·r; so the deficit
  fraction of a codim-c source is 1 − (1+w)^(−(c−1)/2) for *every*
  c — 0033's measured c = 2, 3 laws are instances of a one-line
  theorem.
- Side note (algebra, unverified numerically): the optical spatial
  metric γ_ij = g_ij − g_0i g_0j/g_00 of the static lift is
  I + (w/(1−w))·n̂n̂ᵀ — channel form preserved, strength
  renormalized w → w/(1−w), diverging at w → 1.

## 3. The detector response — and a measured normalization fork

E_ij = R_{0i0j} is what an interferometer arm feels. The lift of
the wiggling string forced a real modeling decision, and
measurement made it:

- **Element clock** (each string element meters by its own
  instantaneous proper time): the element's γ(t_ret) broadcasts at
  full strength at any distance — a **non-decaying trace wave**
  (E amplitude 4.4e−2 at R = 3 *and* 4.8e−2 at R = 6;
  Ricci/Riemann ratio ~1). This is the photon-rocket pathology
  (an accelerating Kerr–Schild point radiates null dust), and it
  is observationally fatal. **Rejected by measurement.**
- **System clock** (the string system's rest frame): E_ij is
  **TT at fraction 0.982–0.992**, TT channel decaying exactly 1/R
  (1.993), vector channel second order (3.97 = 1/R²), and the 4D
  Ricci wave is **0.19–0.20 of the Riemann wave** — the wave is
  dominantly Weyl (vacuum-like), with a ~20% effective radiative
  stress as the quantified departure from exact vacuum GR.

0034's time-sector caveat closes: **detectors see the TT wave; the
gauge vector wave is absent from the observable at leading order.**

## The state of the wave/statics program

| question | status |
|---|---|
| time sector (lapse/shift) | **built** — covariant Kerr–Schild null channels |
| strength dynamics | **derived** — w_eff = wD² from the sender's clock |
| velocity statics (compass/baseline/MM) | **dissolved** — covariance automatic (4e−16) |
| detector response | **TT at 0.98+**, 1/R, vector absent |
| statics vs GR | same form; differs by strength profile (monopole vs Schwarzschild) |
| radiative vacuum-ness | 80% Weyl; ~20% Ricci admixture, measured |

## Honest limits

- The nearest-retarded-point channel rule for extended sources
  remains a modeling choice; the ~20% Ricci-wave admixture may be
  its artifact rather than physics — undecided here.
- The system-clock normalization is selected *by measurement*
  (pathology exclusion), not yet derived from a web principle
  ("which clock meters a channel" is a real open).
- E_ij is reported unnormalized by (−g_00)^(−1); at these
  strengths that is a smooth O(w) overall factor.
- The Schwarzschild-profile observation is exact GR algebra
  (Kerr–Schild), not a web derivation of attraction; the web's
  constant-w point does not attract.

## Open

1. **The Newtonian limit**: what makes channel strength run as
   1/ρ? Candidates: screening by the ambient web (the 1/√det law
   integrating over channels), or participation density of
   composite sources. This is now the sharpest gap between the web
   and observed gravity.
2. **The clock principle**: derive the system-clock normalization
   (or replace the nearest-point rule with an integrated channel
   that makes the fork moot).
3. **The 20%**: decide whether the radiative Ricci admixture is
   rule-artifact (test: integrated channels, other wiggle
   families) or fundamental (then it is the falsifiable
   prediction).
4. **Energy flux and the quadrupole coefficient**: with the time
   sector built, both are now computable.
