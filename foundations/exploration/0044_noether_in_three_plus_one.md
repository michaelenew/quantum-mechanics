# 0044 — Noether in 3+1: charges, balance, and what the action must be

0025 ran Noether on the 2+1 web operationally — symmetry ↔ measured
conserved object — and found the charges were **holonomies**: loop
monodromies whose rotation part is mass and translation part is
momentum. That reading is what fixed the action (0026: discrete BF,
whose *second* EOM is the conservation law). This exploration runs
the same programme in 3+1, where loops become 2-spheres — and turns
up the structural fact that constrains the action. Code:
`output/0039_noether_in_three_plus_one.py`.

---

## 1. The channel ansatz linearizes the field equations

For the web's own metric form g = η + w·k⊗k with k null and
geodesic, the mixed Einstein tensor **G^μ_ν is exactly linear in the
channel amplitude**: G/λ is constant over an 8× range at three
different profiles (deviations 2e−6 to 1e−5 relative — the
finite-difference floor).

| profile | max\|G/λ\| | deviation from linear |
|---|---|---|
| p = 0.5 | 0.171117 | 6e−6 |
| p = 0 | 0.333335 | 2e−6 |
| p = 2 | 0.370366 | 1e−5 |

Two consequences, and they retroactively explain everything measured
since 0035:

- **a single channel of any strength solves the full nonlinear
  theory** — which is why the vacuum profile is exact, and why
  bending, precession and Kepler came out exactly right rather than
  approximately;
- **all the nonlinearity lives in how channels superpose** — the
  bond sector, and nowhere else.

(This is the Kerr–Schild linearization property, standard in GR —
imported, not derived here. What is new is the *identification*: the
web's channel form **is** that ansatz, so the theory's entire
nonlinearity is displaced onto correlation.)

## 2. The ten charges, measured as surface integrals

0025's loop monodromies lift to 2-sphere integrals (new battery
instruments: `adm_energy`, `adm_momentum`, `adm_angmom`). All ten
Poincaré charges exist and take their special-relativistic values:

| configuration | measured | expected |
|---|---|---|
| static | E = 0.020000 | m = 0.02 |
| boosted v = 0.3 | E = 0.020962, P = 0.006289 | γm = 0.020966, γmv = 0.006290 |
| boosted v = 0.6 | E = 0.024970, P = 0.014982 | γm = 0.025000, γmv = 0.015000 |
| binary | J_z = 1.0242e−3, J_x,y ~ 2e−14 | 2γmav = 1.0206e−3 |
| binary | **E = 0.039214** | 2γm + binding = **0.039225** |

That last row is the one that matters: **the ADM integral sees the
bond's energy.** 2γm alone would be 0.040825 — off by 4%. The bond
enters the metric as *stress only* (spatial block), and the
Hamiltonian constraint converts it into exactly the binding energy
in the total charge. Which is precisely why adding it as matter
*as well* (0042 §3) double-counts by 2. **That thread closes here**:
the bond's energy was never missing, it was in the constraint.

## 3. The conservation laws, explicitly

- **Energy**: dE/dt = −L with L = 4.1947e−5 measured against GR's
  quadrupole 4.1943e−5 (0035).
- **The wave's mode structure, measured**: face-on, |h₊| = |h_×| to
  ratio **1.0000** with phase difference **90.0°** — exactly
  circular polarization at ω = 2Ω, i.e. **pure m = 2**. So each
  quantum carries E = ω and J_z = 2, giving **dJ/dE = 2/ω = 1/Ω** as
  a *measurement* rather than an assumption.
- **Angular momentum**: dJ/dt = −L/Ω = −2.62e−5.
- **The balance**: the orbit's own dE_orb/dJ_orb = Ω, so the
  radiated fluxes come off in exactly the ratio that keeps the orbit
  circular as it decays.

Noether's three inputs — symmetry, charge, flux — are all measured
in 3+1.

## 4. What the action must be

The 2+1 route was: charges measured (0025) → action written whose
Noether charges they are (0026). The 3+1 data now constrain the
action from the same direction:

1. **It must reduce, per channel, to a form whose field equation is
   linear in that channel's amplitude** (§1). In 2+1 BF supplied
   this *trivially* — BF is linear outright. In 3+1 it must be
   supplied *nontrivially*, and the Kerr–Schild structure is what
   does it.
2. **It must generate the pair sector's stress −(F·d)n̂n̂ᵀ as the
   bond** (0040), whose energy the constraint then reports as the
   binding energy (§2).

What is **not** written: the functional itself. The gap is narrow
and named — a first-order (BF-like) form whose B-variation gives the
channel equation and whose pair sector gives the bond, reducing to
0026's S = Σ B(curl θ − src) when a dimension is removed.

## Honest limits

- §1 imports the Kerr–Schild linearization from GR; the measurement
  here confirms it holds for the web's channel form, at three
  profiles and one direction.
- The ADM instruments are linear-order (N ≈ 1, K_ij to first order)
  and their sign convention is **fixed by calibration** on the
  boosted source — stated rather than derived.
- §2's binary values are at v = 0.2 with the scripted orbit; the
  0.3% J residual and 0.03% E residual are consistent with O(v²)
  and the finite surface radius (R = 20), not resolved further.
- §3's dJ/dE = 1/Ω follows from the measured m = 2 mode structure
  plus the standard quantum counting; the angular-momentum flux is
  not measured independently by a separate surface integral.

## Open

1. **The functional** — the single remaining item on the action
   front, now boxed in from three sides (linear per channel; bond
   as pair stress; reduces to 0026 in 2+1).
2. **Independent J flux**: measure dJ/dt by its own surface
   integral rather than inferring it from L and the mode structure.
3. **The constraint as the bond's home**: §2 suggests the bond may
   be a *constraint* phenomenon rather than a source — worth
   testing by deriving the binding term from the Hamiltonian
   constraint directly.
4. **Boost charges**: the center-of-mass/boost generators (the
   remaining three of the ten) are inferred rather than measured
   here; 0025's 2+1 analogue was the translation part of the
   monodromy.
