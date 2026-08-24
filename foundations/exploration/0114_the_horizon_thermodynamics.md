# 0114 — Horizon thermodynamics from the nonlinear completion

The filter side completed gravity nonlinearly (lucid 0022): the
trust field sources itself, the self-coupling is *forced* to β = 1
by consistency between the field's own code and its gravitating
mass, and the static solution is Schwarzschild-shaped,
ψ = 1 − MG(r), with ψ the transmission (redshift) factor. This
stone works out the thermodynamics and confronts it with this
program's own measured constants. Code:
`output/0104_the_horizon_thermodynamics.py`.

## 1. The horizon has a temperature, and it is Hawking's

Measured content: the saturated field's profile *is* 1 − M·G(r) with
the same M as the region's capacitance (fit recovers M to <1%:
22.98/39.07/52.82 against 22.98/39.17/52.88), and the lattice
horizon radius (where G(r_h) = 1/M) tracks the body's surface
(1.92/2.94/3.78 for R = 2/3/4). The temperature is then analytic:

    r_h = M/4π,  κ = |ψ′(r_h)| = 4π/M,  **T = κ/2π = 2/M**

**Hawking's scaling T ∝ 1/M falls out of the completion with no
input beyond β = 1** — which was itself forced, not fitted. Combined
with lucid 0021 (the half-web observer's β = 2π boost temperature,
verified to 1e−4), the program now has both the Unruh and the
Hawking side of horizon temperature in filter-space form.

## 2. Extremality is the hoop shape, not the entropy bound

Saturated mass = capacitance (lucid 0022), so for a ball
C = 4πR gives **M_max·G(R) = 1 exactly** (measured 1.000 at
R = 1..4): the extremal body's surface is its own horizon, and
M ≤ 4πR bounds mass by a **length**. That is the hoop-conjecture
shape — gravity's characteristic bound — and it is *distinct* from
the entropy bound this program derived separately (0082's area
law, S = αA). The two coexist: one caps mass by radius, the other
caps information by area.

## 3. The first law would close the κ-normalization debt

With S = αA and T = 2/M: S = αM²/4π, so T·dS/dM = α/π. The first
law dM = T·dS therefore holds **identically in shape** (S ∝ M²,
T ∝ 1/M — verified exactly at several masses) and fixes the
coefficient: consistency **requires α = π in the completion's
units**. The measured lattice-graviton value is 0.0242 (0082), so
the required bridge factor is **129.8**.

This is not a discrepancy to explain away — it is a *use* for a
standing debt. The bridge must be supplied by the κ normalization
(the Known-gaps item that has been open since the geometric arc)
together with the graviton's polarization count. **The first law is
therefore a new instrument for closing κ**: measure both sides in
one convention and the normalization is determined, not chosen.
Recorded as a prediction with its bridge attached, not as agreement.

## Honest limits

- The scalar trust field is the Newton→Schwarzschild axis of the
  theory; the graviton's tensor structure enters the bridge factor
  and is exactly what is not yet converted.
- κ = |ψ′| at the horizon is the field-theoretic surface gravity of
  a transmission factor, not a metric surface gravity computed from
  a derived line element.
- The Dirichlet box biases the lattice Green function at large r
  (45% at r ~ 10); the horizon radius is read from the lattice G
  rather than the continuum M/4π for this reason.

## Open

1. Close the bridge: express 0082's α and this T in one convention
   (needs the polarization count and κ) — would settle a standing
   gap and turn the first law from consistency into a measurement.
2. The interior (lucid 0022's open 1): the level cutoff N as the
   regulator of ψ ≤ 0 — a maximum representable mass per level.
3. Radiation: 0014's source-tier waves + this horizon = the
   evaporation question, now well-posed on both sides.
