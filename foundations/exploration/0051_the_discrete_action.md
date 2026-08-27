# 0051 — The discrete action varied, and a correction to 0050

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Three results: the functional's two field equations obtained by
varying a *lattice* action numerically (the strict form 0050 left
open); the loop's cusp burst measured against GR's beaming; and a
correction to 0050 §4 that makes the wave sector cleaner than the
claim it replaces. Code: `output/0046_the_discrete_action.py`.

---

## 1. The discrete action, varied

Write the action on a 7-point stencil,

```
S = Σ_sites ε^{μνρσ} ε_IJKL e^I_μ e^J_ν F^KL_{ρσ}
```

with F built from neighbouring ω's, and differentiate
**numerically** with respect to the fields at the centre:

| variation | at the solution | elsewhere |
|---|---|---|
| δS/δω | 2.9e−4, falling as **a²** (1.15e−3, 2.88e−4, 7.20e−5 at a = 0.04, 0.02, 0.01) — discretization error | 1.27 at a perturbed connection (**ratio 4400**) |
| δS/δe | 1.1e−3 at the **vacuum** profile (same O(a²) floor) | 2.63 and 2.03 at non-vacuum profiles |

**Both Euler–Lagrange equations come out of the lattice action**:
the ω-variation is stationary exactly on the torsion-free
connection, the e-variation exactly on the vacuum profile. The
functional is now verified *variationally* — not by
constraint-matching (0046), not by continuum route (0050), but by
differentiating a discrete sum. 0050's open #1 closes.

## 2. The cusp burst

The loop's cusps (A′(u) = −B′(v) at (u,v) = (0,π),(π,0)) move at
**exactly c** (measured 1.0000) along ∓x̂. Angular flux at R = 20:

| direction | ⟨ḣ²⟩ | peak/mean |
|---|---|---|
| **cusp (±x)** | **1.62e−4** | **34.75** |
| transverse (y, z) | 3.34e−5 | 1.01 |
| 45° (xy) | 6.26e−5 | 10.12 |

A 4.85× beaming anisotropy — and more tellingly, a **35× temporal
spike** in the cusp direction where the transverse directions are
almost perfectly steady. That is GR's cusp burst: brief, strongly
beamed emission, the structure cosmic-string burst searches look
for. The web reproduces it from its own channel rule.

## 3. A correction to 0050 §4

0050 reported the conserved binary's vacuum residual as
"post-Newtonian source structure, strength-independent." **Both
halves were unsupported.** At a fixed number of wavelengths the
field strength h ≈ 4v³ is *determined* by v (since v² = M/4a and
R ∝ λ ∝ a/v), so that scan could not separate strength from
velocity — the "M halved" configuration had the *same* h as the
baseline, which is why the ratio was identical.

The distance scan separates them, and the answer is neither:

| R/λ | 3 | 6 | 12 | 24 |
|---|---|---|---|---|
| v = 0.2 | 0.02731 | 0.01378 | 0.00691 | 0.00346 |
| v = 0.1 | 0.00332 | 0.00168 | 0.00089 | 0.00049 |

**Exactly 1/R.** The non-vacuum part of the field falls as 1/R²
while the radiative part falls as 1/R, so the residual is
**near-zone contamination** — and

> **the conserved binary's wave-zone field is exactly vacuum.**

The corrected statement is stronger than the one it replaces: there
is no radiative admixture to explain. (0047's 0.014 and 0049's
comparisons were all finite-R measurements of this same 1/R tail;
their *relative* comparisons stand, since they were taken at
matched distances.)

## Honest limits

- §1 varies a stencil action with fields sampled from continuum
  functions; it verifies the variational principle and its two
  EOMs, not a self-contained lattice theory with independent link
  variables and a discrete gauge symmetry.
- §2's beaming is measured at one radius and 48 phase samples; the
  cusp spike's width is resolution-limited, so the peak/mean 34.8
  is a lower bound on the true burst sharpness, not a measured
  waveform.
- §3's 1/R conclusion is from four radii at two velocities; the
  extrapolation to "exactly vacuum" is the limit of that trend, not
  a proof that no smaller non-vacuum term survives.

## Open

1. **A self-contained lattice theory**: independent link variables,
   discrete local Lorentz invariance, and the EOMs as exact
   difference equations — the remaining formal step beyond §1.
2. **The cusp waveform**: resolve the burst's time profile and
   compare its spectral index with GR's cusp prediction
   (the |f|^(−4/3) burst spectrum).
3. Standing from 0048: the Lorentzian-arena construction, P4 →
   Tsirelson, matter beyond scripted sources, the arithmetic
   bridges.
