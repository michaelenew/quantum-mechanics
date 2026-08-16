# 0037 — The classical tests: bending, precession, two bodies

0036 gave Newton and Kepler from the vacuum-selected profile. This
exploration runs the tests that historically *distinguished*
Einstein from Newton through the same machinery, then takes the
first two-body measurements — where the web's nonlinearity lives.
Code: `output/0032_the_classical_tests.py`.

---

## 1. Light bending: the 1919 factor of 2

Null geodesics past the mass (new battery instrument: the geodesic
integrator, with the future-directed-root lesson — g_00 < 0 makes
the naive quadratic root past-directed; the fix is `future_u0`):

| b | measured | GR 4M/b | Newtonian 2M/b |
|---|---|---|---|
| 1 | 0.008046 | 0.008000 | 0.004000 |
| 2 | 0.004011 | 0.004000 | 0.002000 |

**Einstein's full deflection — twice Newton's** — to 0.6%/0.3%.
The factor 2 lives in the null structure of the channel form (the
g_0i sector the time sector supplied; a metric with Newtonian g_00
alone bends half as much).

## 2. Perihelion precession: converging to Einstein's rate

Bound orbits from periapsis, parabolic-interpolated apsides:

- prograde advance, exactly repeatable (spread 6e−8 across orbits);
- M = 0.005: +0.21527/orbit vs 6πM/p = +0.20452 (ratio 1.053 at
  M/p = 0.011); M = 0.002: ratio 1.021 at M/p = 0.0044;
- the excess normalized by M/p is the *same coefficient* (4.84 vs
  4.67): the gap is the **second-order term**, and the advance
  converges to GR's leading-order formula as M → 0.

With 0036's Newton/Kepler and §1's bending, the web's
vacuum-selected point now passes the classical solar-system tests
wholesale — unsurprising once the profile is Schwarzschild
(these are theorems on the GR side), but the point is *which side
supplied the profile*: the web's own flat-off-participation law.

## 3. Two bodies: the nonlinearity, localized

Superposing two vacuum-profile channels (the web's natural
two-body ansatz):

- **The superposition violation is exactly O(M₁M₂)**: off-source
  max|R_μν|/M² = 48.7 / 48.3 / 48.2 over a 4× mass range. Single
  sources are vacuum; pairs imply an interaction stress at second
  order — this is where the post-Newtonian sector lives, now
  localized and scaled.
- **Masses add**: far-field attraction = −(M₁+M₂)/r² to 0.4% at
  r = 10 (the residual is the pair's quadrupole + the interaction
  term).
- **Channel nullity**: a single source's channel vector is exactly
  null in the metric it creates (2e−16 — the Kerr–Schild identity
  g^ab k_a k_b = η^ab k_a k_b = 0): **each channel rides the very
  cone it builds**, an exact self-consistency of the covariant
  channel form. With two sources, each channel fails nullity in
  the full metric at O(w₁w₂): **interaction is cone-bending** —
  one channel's geometry deflects the other's causal structure.
  The web's gravity-couples-to-gravity nonlinearity has a
  channel-native mechanism.

## The state of the classical sector

| test | result |
|---|---|
| Newton / Kepler | exact (0036) |
| light bending | 4M/b, 0.3–0.6% |
| perihelion precession | 6πM/p + measured 2nd order, converging |
| mass additivity | 0.4% at r = 10 |
| nonlinearity | O(M₁M₂), coefficient measured (48 at this geometry) |
| channel self-consistency | nullity exact (single), broken O(w₁w₂) (pair) |

## Honest limits

- All of §1–2 is geodesics of the exact Schwarzschild metric in
  Kerr–Schild coordinates — the content is that the *web's law
  selected this metric*, not new GR.
- The two-body superposition is an ansatz, not a solution: the
  O(M₁M₂) violation says the web's true two-body field must
  correct it (in GR the correction is the interaction potential;
  here the fix rule is unwritten).
- The cone-bending nullity failure and the Ricci violation are two
  faces of the same O(w₁w₂) term; neither is yet matched
  quantitatively to GR's post-Newtonian coefficients.
- The interaction coefficient (48) is geometry-specific (d = 1,
  midpoint-ish probe), not a universal number.

## Open

1. **The two-body fix rule**: what web-native update restores
   vacuum off-source for pairs? (GR's answer: the nonlinear field
   equation. The web's candidate: iterate the vacuum principle —
   let each channel's strength respond to the other's ambient, the
   0020 screening law one tier up.) Check its first correction
   against the Einstein–Infeld–Hoffmann sector.
2. **Radiated two-body waves**: orbit two vacuum-profile sources
   with retarded channels and measure the quadrupole formula's
   coefficient against GR — the strongest correspondence test now
   in reach.
3. **The 4D field equation** (carried from 0036): the object whose
   linearization already gave K = πs, whose vacuum selected the
   profile, and whose nonlinearity should be the measured O(M₁M₂)
   term.
