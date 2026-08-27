# 0052 — The lattice theory, self-contained, and the cusp spectrum

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0051's two opens, both closed. The functional now exists as a
genuine lattice gauge theory with group-valued links and **exact**
discrete local Lorentz invariance; and the loop's cusp harmonics are
measured against GR's n^(−4/3) law. Code:
`output/0047_the_lattice_theory.py`.

---

## 1. A self-contained lattice theory

Variables: an **SO(3,1) element U_μ(x) on every link** (verified
Λᵀη Λ = η to 7e−16) and a frame vector e^I_μ(x) on every link.
Plaquette holonomy U_μν(x), its algebra part F^IJ_μν, and

```
S = Σ_x ε^{μνρσ} ε_IJKL e^I_μ e^J_ν F^KL_ρσ
```

on a 3⁴ web of **random** links. Under a *large* local Lorentz
transformation at one site (scale 0.4, acting on its four outgoing
links, its four incoming links, and its frames):

| | |
|---|---|
| S before | 1.4753951510 |
| S after | 1.4753951510 |
| \|ΔS\| | **7.1e−15** (relative 4.8e−15) — machine zero |

**A discrete theory with a discrete gauge symmetry** — no
linearization, no continuum limit, no smallness assumption. The
invariance is exact because ε_IJKL is an invariant tensor of the
group and every factor in the summand is based at the same site
(the neighbouring links' transformations cancel inside the
holonomy).

## 2. The field equation is exact on the lattice

Differentiating the lattice action numerically with respect to one
frame component, against the analytic form:

| | |
|---|---|
| numerical δS/δe^I_μ(x₀) | 6.5535113389 |
| analytic 2ε^{μνρσ}ε_IJKL e^J_ν F^KL_ρσ | 6.5535113340 |
| agreement | 5e−9 (the finite-difference floor) |

So the discrete Einstein equation holds **as a difference
equation**, not to O(a²). Together with 0051's ω-variation (which
converges as O(a²) to the torsion equation, since the connection
equation is where the continuum limit lives), the functional's two
field equations are now established at the lattice level.

## 3. The cusp spectrum

GR predicts cusp bursts with harmonic amplitudes falling as
n^(−4/3). Measured in the cusp direction (R = 40, 800 elements,
320 phases):

| window | slope |
|---|---|
| n = 4..16 | −1.224 |
| n = 8..32 | **−1.302** |
| n = 16..64 | −1.416 |
| n = 24..72 | −1.478 |

The slope **brackets −4/3 = −1.333**, crossing it in the n = 8–32
decade (2.5%); the low end is pre-asymptotic and the high end is
steepened by the finite element count (the discretized source
smooths the cusp).

The decisive contrast is with the transverse direction, where the
same harmonics fall **exponentially**: 1.63e−3, 4.8e−6, 7.9e−10,
1.6e−16 at n = 2, 4, 8, 16 — an effective slope of −14.6.

> **Power law only where the cusp beams.**

That contrast *is* GR's cusp phenomenology — the reason cosmic-string
burst searches look for beamed, power-law-spectrum transients rather
than steady tones. The web reproduces it from the channel rule
alone.

## Honest limits

- §1 establishes exact gauge invariance and a well-defined discrete
  action; it does not construct the theory's measure, its
  constraint algebra, or a proof that the continuum limit is
  Einstein gravity (the continuum route was 0050, and 0051's
  stencil version showed the ω-equation converging as O(a²)).
- §2's exactness is for the **e**-variation, which is algebraic in
  the frames; the ω-variation is a genuine difference equation
  whose continuum limit is the torsion equation — exactness there
  is not claimed.
- §3's slope is measured over harmonic windows, so "brackets −4/3"
  is a statement about a trend crossing the predicted value, not a
  fit with an error bar. The high-n steepening is diagnosed as
  source resolution but not separately quantified.
- The cusp comparison is with GR's *analytic* cusp law, not with a
  numerical GR waveform for the same loop.

## Open

Standing from 0048, unchanged by this turn:

1. **The Lorentzian arena**: the Euclidean-web → Lorentzian-
   spacetime step is argued (via 0025's forced Lorentz pole) but
   not constructed.
2. **P4 → Tsirelson**: whether recursive consistency pins the
   quantum bound — the program's oldest open.
3. **Matter beyond scripted sources**: worldlines and worldsheets
   are prescribed, not solved for; the movie/census sector
   (0018/0030) has its selection rules but no dynamics.
4. **The arithmetic bridges**: continuum versions of the 0010
   finite-frame results.

Newly available with the lattice theory in hand:

5. **The lattice's quantum tier**: the level-N Weyl algebra (0027)
   on *these* link variables — the natural next construction, and
   the place where "budget = frame squared" (0047 §4) should become
   an operator statement about the measure.
