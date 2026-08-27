# 0036 — The Newtonian limit: the vacuum principle selects the profile

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0035 ended on the sharpest gap between the web and observed
gravity: the constant-w point channel is a global monopole —
g_00 = −1 + w constant, hence **no attraction** — while GR's point
mass is the *same* Kerr–Schild form with profile w = 2M/(u·ℓ).
This exploration closes the gap from the web's own field law.
Code: `output/0031_the_newtonian_limit.py`.

---

## 1. The principle, and the selection

The 2+1 web's measured field equation was K = πs/det g (0020,
0028): **curvature lives exactly where participation is; the field
is flat off-source.** Lift that principle to the 4D null-channel
metric: off-source, the implied matter G_μν must vanish.

Measured, for w(ρ) = w₀(r₀/ρ)^p:

| p | max\|R_μν\| off-source (two radii) |
|---|---|
| 0 (constant — the bare web) | 9.5e−2, 3.9e−2 |
| 0.5 | 4.6e−2, 1.5e−2 |
| **1** | **7.6e−7, 8.3e−8 — vacuum** |
| 1.5 | 5.1e−2, 1.1e−2 |
| 2 | 1.3e−1, 2.5e−2 |

Within power laws, flat-off-participation forces **w = 2M/ρ — the
Schwarzschild profile**. (Uniqueness beyond power laws is
Birkhoff's theorem, imported not derived.) The 0031 celebration of
the constant-w monopole's "bulk curvature off-source" reads
differently now: a bare constant-strength point *violates* the
web's own field law — it implies a stress halo everywhere. The
law runs the strength.

## 2. Attraction is the profile

Geodesics, measured:

- **Constant w: a test particle at rest stays at rest** (radial
  acceleration 0 to machine precision at two radii) — the 2+1
  "no pair force" lifted intact. The bare web point does not
  attract.
- **w = 2M/ρ: a = −M/r² to six digits** at both radii — Newton,
  exactly.
- **Kepler's third law exact**: circular-geodesic angular velocity
  gives ω²r³ = M to six digits at both radii.

So the chain closes: *the web's field law (curvature only at
participation) → vacuum off-source → w = 2M/ρ → Newtonian
attraction and Kepler orbits.* Gravity's pull, in this frame, is
not a new force — it is the strength profile that the consistency
of the off-source field demands.

## 3. The ledger's fifth half-exponent

In 3D, an isotropically diluting information flux falls as 1/ρ².
A strength that runs as the **square root of flux** runs as 1/ρ —
exactly the selected profile. The ½ exponent has now appeared five
times across the program:

1. trust = √information (stat-tracker),
2. amplitude = √probability (Born),
3. loop-tier screening det^(−1/2) (0029),
4. the codim ladder's (1+w)^(−1/2) per transverse dimension
   (0033/0035),
5. strength = √flux ⇒ Newton (here).

Whether the web *derives* the profile this way — channel strength
as the amplitude of diluted participation flux — is the open
derivation; the selection itself is measured. If it holds, the
same square-root ledger that prices measurement (Born) prices
gravity (Newton).

## Honest limits

- "Vacuum off-source" as the 4D form of K = πs is a lift of a
  measured 2+1 law, not yet a 4D web derivation (the 4D field
  equation itself is unwritten).
- The selection is tested over power-law profiles at one strength;
  Birkhoff supplies general uniqueness on the GR side only.
- Kepler/Newton checks are static-source, weak-field-scale
  numerics (M = 0.005); strong-field orbits (precession, ISCO) not
  yet run — they are now one command away with this machinery.
- The √flux hypothesis is registered, not derived: no web
  mechanism yet says why strength is an amplitude.

## Open

1. **The 4D field equation**: write the web-native law whose
   off-source content is G_μν = 0 (the 4D K = πs) — this would
   turn the vacuum *selection* into a *derivation* and subsume
   Birkhoff's role.
2. **The √flux derivation**: derive w ∝ 1/ρ from participation
   flux + the amplitude ledger; a composite-source version
   (N participants at density ρ_s) would also fix G in web units.
3. **Strong field**: perihelion precession and light bending
   through the same pipeline (both now trivially computable) —
   the classical tests.
4. **Two-body**: two vacuum-profile sources with the covariant
   channel rule — does the web's superposition reproduce the
   post-Newtonian sector?
