# 0034 — The gauge audit: the wave was Einstein's after all

The question this exploration answers: **how severe is 0032's
"wrong polarization" — does it force falsified predictions?** The
question demanded a gauge audit before any new construction, and
the audit **reverses 0032's verdict**: the vector metric wave is
gauge dressing; the gauge-invariant wave is TT-dominant with the
full Einstein signature, including a linear TT component 0032's
scalar-only instrument could not see. Code:
`output/0029_the_gauge_audit.py`.

---

## 1. The instrument: the Ricci *tensor*

0032 used the Ricci scalar; the audit needed the tensor. The new
pipeline (`ricci_tensor`), validated:

- unit 3-sphere: Einstein condition R_ij = 2g_ij to 1e−5;
- TT plane wave: **linear** Ricci tensor = −½∇²h to 0.1% — TT is
  invisible to the linear *scalar* (0032/s1) but visible to the
  linear *tensor*;
- vector plane wave: Ricci tensor **identically zero**.

The decisive 3D fact: **Weyl vanishes identically in three
dimensions, so Ricci determines Riemann.** Zero Ricci tensor =
flat = pure coordinates. The Ricci tensor is therefore a complete
gauge-invariant meter for spatial waves — exactly what the
severity question needed.

## 2. The audit: the invariant wave is TT

The web wave's Ricci-tensor polarization, decomposed against the
propagation direction (same decomposer as 0032, now applied to the
invariant object):

| channel | R = 3 | R = 6 | fraction |
|---|---|---|---|
| **TT** | 3.19e−2 | 1.59e−2 (halves: 1/R) | **0.977** |
| longitudinal | 6.0e−3 | 3.1e−3 | 0.19 |
| trace | 3.3e−3 | 1.7e−3 | 0.10 |
| vector | 6.3e−4 | 1.6e−4 | **0.01–0.02** |

The metric-level "pure vector wave" of 0032 carries 1–2% of the
invariant curvature. It was the *gauge dressing* of a TT wave: the
slaved form I + w·uuᵀ writes TT curvature in vector metric
components, because the direction field's z-structure (K along the
string) crossed with its radial retardation (Ω) is curvature that
a plane-wave decomposition cannot see (R_xz ⊃ ∂_radial∂_z h_xy).

## 3. The linear TT wave

The dominant invariant component is **R_xz — TT, polarized in the
(jitter, string-axis) plane** — and it is:

- **linear** in the wiggle amplitude (exponent 0.98),
- at the **fundamental** Ω (harmonic purity > 1e3),
- decaying as exactly **1/R** (amp(6)/amp(7) = 1.170 vs 7/6 = 1.167),
- **outgoing at c** (radial phase advance 1.998 vs Ω·ΔR = 2.000;
  instantaneous control 337× weaker with no outgoing phase).

The diagonal components are quadratic at 2Ω — the quadrupole tier,
which is all 0031's Ricci-scalar instrument could see (the scalar
wave's A² and 2Ω are now explained: the scalar is blind to the
linear TT piece).

## The severity verdict

**No falsified predictions are forced.** Itemized:

1. *Had the vector wave been physical*, it would have been fatal —
   not a coefficient patch: LIGO's multi-detector polarization
   tests favor tensor over vector; binary-pulsar orbital decay
   forbids a dominant dipole channel; observed chirps sit at twice
   the orbital frequency. Wrong channel + wrong frequency + wrong
   multipole.
2. *It is not physical.* Its invariant curvature content is 1–2%.
   No gauge-invariant observable at linear order transmits it.
   (Exact for spatial geometry; the full detector response — strain
   via R_{0i0j} — needs the time sector, which is unbuilt. That is
   the honest residual caveat.)
3. *What is invariantly there has the Einstein signature*:
   TT-dominant (0.98), linear radiation at the source's frequency
   plus quadratic at its double, 1/R, speed c, retardation-made.

**Correction to 0032** (recorded there too): the claim "Einstein's
TT modes would have to live in a propagating strength tensor, and
nothing propagates there" is wrong — the direction field alone
carries linear TT curvature. The strength tensor remains genuinely
demanded, but by the velocity-*statics* anomalies (0023 compass,
0024 baseline, 0025 MM), not by radiation. 0032's discriminator
and metric-polarization *measurements* stand; the verdict drawn
from them confused gauge with geometry.

Remaining genuine risks, named:

- the **second-order scalar admixture** (longitudinal 0.19, trace
  0.10 of the invariant wave) — a surviving scalar channel would be
  Brans–Dicke-like and constrained; whether it survives requires
  the time sector;
- the **luminal traveling wiggle radiates** where Nambu–Goto
  strings exactly do not (Vachaspati/Garfinkle) — a matter-sector
  difference, unconstrained by any current observation, not a
  field-dynamics failure;
- the **time sector** (lapse/shift) — the one construction full
  detector correspondence cannot proceed without.

## Honest limits

- "Gauge" here means spatial-diffeomorphism content on constant-t
  slices; the physical-slicing question (whether web matter rides
  the coordinate wave) is precisely the open time sector.
- The linear TT wave's closed-form coefficient (the ½ΩK·wA/R-type
  cross-derivative estimate matches to ~50%) is not extracted; the
  quadrupole coefficient of the 2Ω tier likewise.
- Scalar-channel fractions are measured at one wiggle family and
  two radii.

## Open

1. **The time sector**: lapse/shift for the web — after which
   strain, energy flux, and the scalar-channel question all become
   answerable. Now the program's sharpest missing construction.
2. **The strength dynamics**, refocused: its target is the
   velocity-statics anomalies, not the wave sector; success =
   compass/baseline anomalies cured with the TT wave sector left
   intact.
3. **Coefficients**: the linear TT coefficient and the 2Ω
   quadrupole coefficient against linearized GR's values for the
   same source.
