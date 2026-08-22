# 0077 — The continuum scaling: the fixed structure is the heat kernel, and the graviton channel goes gapless

The stone after 0076. A fixed structure with t < 1 means finite
correlation length — *unless* t → 1 as the frame scale grows. So the
decisive computable is the scaling of the fixed structure's tensions
with the bin scale s₀ (s₀ ~ 1/L²: smaller = larger frames = closer to
the continuum). Two results; the second has a name. Code:
`output/0069_the_continuum_scaling.py` (17 s).

---

## 1. The graviton channel goes gapless

| s₀ | 1.5 | 0.75 | 0.375 | 0.1875 |
|---|---|---|---|---|
| μ(1,1) | 0.437 | 0.124 | 0.033 | 0.011 |

Power fit μ ~ s₀^p with p = 1.82, 1.90 on the converged intervals —
consistent with **μ ∝ s₀² ~ 1/L⁴ = ε, the regulator**. The graviton
channel's gap is a regulator artifact, vanishing exactly as the
regulator is removed. (Convergence checked: t(1,1) moves 0.02%
between (NG, JBIG) = (240, 30) and (320, 40).)

## 2. The fixed structure is the heat kernel

The tension *ratios* are quadratic-Casimir ratios to three digits at
**every** scale:

| ratio to μ(1,1) | measured | C₂ ratio |
|---|---|---|
| (2,2) | 3.000 | 12/4 |
| (1,0) | 0.500 | 2/4 |
| (2,0) | 1.500 | 6/4 |
| (2,1) | 2.000 | 8/4 |
| (3,3) | 6.000 | 24/4 |

> **μ_R = τ·C₂(R) with τ ∝ s₀²: the MK fixed structure of the healed
> weight is the heat kernel on Spin(4), with diffusion time → 0.**

The mechanism is the central limit theorem on compact groups: the
flow's repeated products Gaussianize any weight in the weak-coupling
basin, and only τ remembers where you started. This also **resolves
0064's standing tension**: the arithmetic, heavy-tailed ledger is the
**UV completion**; the heat kernel is the **IR universality class**.
0063's "chosen" heat-kernel weight is justified a posteriori as the
IR form — and the derivation now says what completes it in the UV.
(It also answers 0076's basin question in the affirmative for this
family: four different starting profiles land on one structure.)

## 3. What this means for A3

At a gapless Gaussian (heat-kernel) point, the quadratic-order
momentum structure is the standard 1/k². The momentum half's *mass*
question is answered: **the (1,1) channel is a gapless carrier in the
continuum-frame limit.**

Two scope lines, stated plainly:

1. **0076's residual drift is now legible as the running of τ** —
   the 4D Yang–Mills shadow (asymptotic-freedom-like logs MK cannot
   resolve). True gaplessness requires the ε → 0 limit to outrun the
   running; that is the standard 4D story, not a defect specific to
   this program.
2. **The (1,1) channel is the carrier the graviton needs — not yet
   the graviton.** Whether the physical metric mode rides this
   channel is the frame/vertex question (the standing intertwiner
   open), which channel kinematics cannot settle.

## Honest limits

- All of 0076's MK caveats inherit (uncontrolled recursion, measured
  deconfinement bias, Euclidean).
- s₀ = 0.1875 is the least converged point (stationarity 1e−3); the
  power fit uses the middle intervals.
- "Heat kernel" is asserted from six tension ratios at four scales —
  strong numerics, not a proof; a fixed-point argument (CLT on
  compact groups, made precise for this recursion) is the natural
  theorem to extract.
- The τ ∝ s₀² dictionary ties to the level dictionary N ~ L² of
  0072; the composed claim (gap ∝ ε exactly) is a two-step inference.

## Open

1. **The vertex** (now the last wall-stone standing): frames and
   intertwiners at a true 4-valent vertex — does the physical
   graviton ride the gapless (1,1) carrier, and does the (1,0)
   interleaving lift?
2. The CLT fixed-point theorem for this recursion (turn six ratios
   into a proof).
3. The running of τ: extract the beta function from the drift and
   compare its sign/size against the 4D Yang–Mills shadow.
4. Standing: Λ1, C1, the arithmetic-branch pass, the sign-problem
   toy.
