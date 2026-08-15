# 0032 — The correspondence test: the web waves in the wrong channel

0031 gave existence: the 3+1 web radiates. This exploration asks
the refined question — **which wave theory is it?** — against
linearized Einstein gravity, in three independent probes. The
answer is decisive, and the failure is *localized*: the web waves,
but in the one polarization channel Einstein gravity forbids, and
the channel Einstein gravity requires is exactly where the web has
nothing dynamical. Code: `output/0027_the_correspondence_test.py`.

---

## 1. The discriminators: what GR waves look like to the instrument

Plane-wave test metrics pushed through the validated Ricci
pipeline, amplitude-scaling measured:

| mode | Ricci response |
|---|---|
| TT (h₊) | exponent **2.00** — zero at linear order |
| scalar / trace | exponent **1.00** — linear |
| vector (h_xz, z-propagating) | **identically zero** |

Two consequences. Einstein radiation (pure TT) is *invisible* to
the linear spatial Ricci scalar — so the web's measured Ricci wave
(0031) is already suspicious, and the real question must be asked
of the metric wave itself.

## 2. The polarization: pure vector, in closed form

The far-field metric perturbation δg(t), decomposed
Frobenius-orthogonally against the propagation direction n̂
(longitudinal / vector / transverse-trace / TT):

- **The wave is pure vector**: amplitude = **w A / R exactly**
  (9.94e-3 measured vs 1.00e-2 predicted at R = 3; halves exactly
  to 4.97e-3 at R = 6), oscillating at the fundamental Ω
  (harmonic purity |H1|/|H2| ≈ 6×10⁹).
- All other channels — TT included — sit at ~1% and fall as
  **1/R²**: second order, not radiation.
- Coherence check: the Ricci wave is **quadratic** in the wiggle
  amplitude (exponent 1.89) at 2Ω — exactly as it must be, since
  the linear wave is vector and a vector wave carries no linear
  Ricci (§1). The 0031 frequency doubling is explained: the Ricci
  wave is the vector wave's second-order composite.

The closed form is the channel rule read directly:
δg = δ(w uuᵀ) = w(δu n̂ᵀ + n̂ δuᵀ) with δu the transverse jitter
of the retarded direction field, |δu| = A/R. Nothing else *can*
move: |u| = 1 slaves the channel and w is frozen.

## 3. Traveling vs standing: the selection rule inverts

GR (literature import): a traveling wave on a straight string is
an **exact non-radiating solution** (Vachaspati 1986; Garfinkle
1990); standing waves radiate. The web:

| shape | Ricci amplitude decay | strength at R = 4 |
|---|---|---|
| traveling | 1/R^1.01 | 9.47e-3 |
| standing | 1/R^1.07 | 2.72e-3 |

Both radiate at 1/R, and the traveling wave — exactly silent in
GR — is **3.5× stronger**. The web does not reproduce GR's
selection rule for string radiation.

## The verdict

**Correspondence fails at linear order, and the failure is one
named object.** The web's propagating degree of freedom is the
direction field u — a vector wave, forbidden in Einstein gravity.
Einstein's TT gravitons would have to live in a **propagating
strength tensor**, and the web's strength sector (w, the baseline)
is frozen: TT appears only as the vector wave's second-order echo.

This converges with three independent 2+1 diagnoses of the *same*
object: the compass anomaly (0023), the necessity of the boosted
baseline (0024), and the in-model Michelson–Morley (0025) all
demanded strength-tensor structure beyond unit channels — and the
Lorentz completion (0024) already built its kinematic form (the
mmᵀ channel + boosted baseline). The web-native content of
Plebanski's simplicity constraint is now a sharp program, not a
metaphor:

> **Make the strength sector dynamical, and check that its
> radiative modes are the two TT gravitons.**

The battery grew three reusable instruments: the plane-wave
discriminator modes (`mode_metric`), the polarization decomposer
(`polarization_channels`, Frobenius-orthogonal, exact), and the
general string-shape retarded metric (`string_wave_metric` — any
string motion → its channel field).

## Honest limits

- The GR traveling-wave fact is imported from the literature, not
  re-derived here; our side of the comparison is measured.
- The decomposition uses one propagation direction and one wiggle
  family; the vector law δg = w(δu n̂ᵀ + n̂ δuᵀ) is verified in
  amplitude and harmonic content, not component-by-component over
  the sphere.
- "Strength sector frozen" is a statement about the current rule
  (unit channels, constant w); 0024's Lorentz completion shows the
  kinematic slot exists but no dynamics has been written for it.

## Open

1. **The strength dynamics**: write the update rule (or action
   term) that lets w / the baseline propagate — the candidate is
   0024's mmᵀ structure promoted from kinematics to a field — and
   re-run this module's polarization decomposition on it.
2. **The vector wave's fate**: in GR-like theories vector modes
   are pure gauge or constraint-killed; determine whether the
   web's vector wave carries energy (the ledger's budget) or is a
   coordinate artifact of the slaved-channel description.
3. **The quadrupole coefficient**: once TT propagates, extract the
   radiated-power coefficient and compare with the quadrupole
   formula.
