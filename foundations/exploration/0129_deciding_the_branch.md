# 0129 — Deciding the branch, and what a failed Lorentz test costs

Code: `output/0116_deciding_the_branch.py`,
`output/0117_the_lattice_is_invisible.py`. Second and third stones of
the continuity front.

0128 left the front with one question carrying fourteen orders of
magnitude: at τ = 0 the derived measure appeared to have two states
local updates cannot connect, at β_eff = 15.5 and 2.9 — **ξ/a ~ 10¹⁷
versus ~10³**. Which is the equilibrium *is* the scale hierarchy.

## 1. Three things I got wrong, in the order I found them

**(i) "Tempering can't work here."** I argued the τ = 0 weight's
exact zeros make lnW₀ ≈ −55 wherever a τ > 0 configuration wanders,
so one such plaquette kills any swap. **Measured acceptance from
τ = 0.004 into τ = 0: 0.44.** The argument priced the barrier between
*distant* τ; between *adjacent* τ the smoothing is far too small to
push a plaquette past a zero, so the barrier never enters. The
decisive tool was available all along.

**(ii) "The disordered branch is a real state" (0128 §3).** Off
τ = 0 it is not. Relaxing hot starts at fixed τ with a 15k burn gives
⟨θ²⟩ = 0.195, 1.081, 0.834, 0.417, 0.398, 0.313, 0.235, 0.156 across
τ = 0.005…0.08 — **jumping around instead of tracing a curve**, while
the ordered branch over the same window is smooth (0.100 → 0.156).
Those runs are not equilibrated. The free-energy route this module
first took has no well-defined branch to integrate along.

**(iii) The whole of 0117's measurement.** Below.

## 2. The ladder, and the answer

The ladder stops at τ = 0.062 **on purpose**: the barrier is the
τ = 0 zeros, and by τ ≈ 0.05 (0113's τ\*) they are smoothed away, so
higher rungs buy nothing. A first pass ran to τ = 0.28; those extra
rungs accepted at 0.007–0.010 and **blocked every round trip**.

| rung | acceptance |
|---|---|
| 0 → 0.004 | 0.440 |
| 0.004 → 0.008 | 0.458 |
| 0.008 → 0.014 | 0.275 |
| 0.014 → 0.022 | 0.177 |
| 0.022 → 0.032 | 0.087 |
| 0.032 → 0.045 | 0.037 |
| 0.045 → 0.062 | **0.007** ← bottleneck |

Round trips: **2**. Weak but real.

> **Tempered ⟨θ²⟩ in the τ = 0 replica: 0.1254 ± 0.0030**, against
> candidates 0.097 (ordered) and ~0.51 (disordered).

The range over measured blocks is 0.090 → 0.440: the τ = 0 replica
*does* visit disordered configurations, but is dominated by the
ordered value. **The second state is a subdominant fluctuation of
the equilibrium, not a competing phase** — and the free-energy
difference is extensive, so at larger volume the domination can only
strengthen. An untempered hot chain sits at 0.51 through 40k sweeps,
so the tempering is doing real work.

> **β_eff = 11.96 → ξ/a ~ 1.7 × 10¹³. The hierarchy is the large
> one.** The derived measure sits at weak coupling, asymptotic
> freedom supplies the scale separation, and **no dial was turned.**

Limitations, plainly: L = 4 only; mixing is weak (2 round trips)
and bottlenecked at the top rung; the L = 6 run did not complete.
More rungs between 0.045 and 0.062 would cost almost nothing and are
the first thing to fix.

## 3. The Lorentz test failed, and the reason is the result

0117 tried to measure rotational invariance directly — the
connected action-density correlator at matched |r| and different
orientations. At 240 configurations on L = 12:

| \|r\| | axis | diagonal | measured anisotropy |
|---|---|---|---|
| 2 | (2,0,0,0) | (1,1,1,1) | +5.61 ± 4.81 |
| 3 | (3,0,0,0) | (2,2,1,0) | −19.70 ± 459.47 |
| 4 | (4,0,0,0) | (2,2,2,2) | +4.64 ± 9.82 |

**Every row is consistent with anything.** The reason is worth as
much as the result would have been: at β_eff ≈ 12–15 the connected
plaquette correlator is O(g⁴), so the statistics needed scale as
g⁻⁸. **The theory is too weakly coupled to see its own interacting
correlator at reachable cost** — which is the same fact that makes
its lattice invisible.

What *is* exactly computable is the free-field kinematic anisotropy,
no Monte Carlo required:

| \|r\| | anisotropy (L = 48) | × (r/a)² |
|---|---|---|
| 2 | +0.746 | 2.99 |
| 4 | +0.240 | 3.84 |
| 6 | +0.100 | 3.61 |
| 8 | +0.059 | 3.78 |
| 10 | +0.045 | 4.51 |

Flat to 51% across r = 2…10 — **the artefact is O((a/r)²) with
coefficient ≈ 3.7.** (L = 32 drifts upward past r ≈ 8; an earlier
pass of this module ran at L = 16 and read that finite-volume drift
as signal.)

Extrapolated at ξ/a ~ 10¹³–10¹⁷ this gives rotational — hence,
through Osterwalder–Schrader, Lorentz — violation of order
**10⁻²⁷ to 10⁻³⁴**.

> **That is not a bound the program has earned.** It is the
> free-field artefact extrapolated under an assumption §3's
> measurement was too noisy to check. The standing "continuum
> Lorentz invariance, never tested" debt **stays open**. What is
> established is the shape of the answer, the coefficient of the
> kinematic part, and the honest cost of the rest: an operator whose
> connected correlator is not O(g⁴) — a smeared operator, or the
> Wilson-loop static potential.

## 4. Where continuity stands

| | |
|---|---|
| the target, restated | no dial exists, so continuity means ξ/a is *already* large at the derived coupling |
| the coupling | β_eff ≈ 12–15, weak, confirmed against 0094's independent Gaussian prediction |
| the branch | **decided: ordered dominates** (tempered, L = 4) |
| the hierarchy | **ξ/a ~ 10¹³–10¹⁷, untuned** |
| Lorentz restoration | **open** — direct test unaffordable at this coupling; kinematic part exact |
| triviality | **untouched** — is the limit interacting or free? |

The front is not closed. But its shape has changed: continuity is no
longer a question about whether a critical point exists. It is a
question about **whether a theory this weakly coupled has anything
left at long distance** — which is the triviality question, and that
is the next stone.
