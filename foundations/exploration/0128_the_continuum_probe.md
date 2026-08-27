# 0128 — The continuum probe: the program has no dial, and the branch ambiguity is the hierarchy

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Code: `output/0115_the_continuum_probe.py`. First stone of the
continuity front — 0127's last open conjunct of 0069's wall.

## 1. The reframing, which changes the target

A lattice theory usually reaches the continuum by **tuning** a
coupling to a critical point where ξ/a diverges. **This program
cannot do that.** Its weight is *derived*, so its coupling is a
fixed number — the Born weight's local precision κ = 13.34. (τ is a
heat-flow probe, not a dial; the physical theory sits at τ = 0.)
There is nothing to tune.

So "continuous" here cannot mean a tuned limit. It has to mean the
other thing: does the theory, **at its own derived coupling**,
already have ξ ≫ a, so the lattice is invisible with nobody tuning
anything? For a nonabelian gauge measure that is not a hope — it is
what asymptotic freedom does. The question is quantitative.

## 2. The derived point is at weak coupling

κ is *exactly* a Wilson β in this program's own convention
(cos θ = ½ tr U_p, so −d²lnW/dθ²|₀ = β). 0094's Gaussian bank
predicts ⟨θ²⟩ = 3R/κ with R = ½ in 4D: **0.1125**.

| L | ⟨θ²⟩ (ordered) | β_eff |
|---|---|---|
| 6 | 0.0969 | 15.48 |
| 8 | 0.0970 | 15.47 |
| 12 | 0.0970 ± 0.0000 | 15.46 |

Within 14% of the prediction and **flat in L**. Weak coupling,
confirmed independently of the flow.

## 3. One certification failed — recorded, not smoothed

The intended positive control was the family's deconfinement line,
located by a Polyakov susceptibility peak growing with volume.
**It did not certify.** At 3000 sweeps the peak lands at
inconsistent τ across L (L=6: 0.15, L=8: 0.15, L=10: 0.05) and
|⟨P⟩| is not monotonic in L. Every point was started hot; the scan
is not converged. It needs ~10× the statistics and a protocol that
does not start each point from a hot configuration.

What *did* work is the direct question — relax a hot start at τ = 0
and watch where it goes:

| L | 1k | 4k | 10k | 20k | 40k | ordered branch |
|---|---|---|---|---|---|---|
| 4 | 1.937 | 0.825 | 0.517 | 0.518 | **0.510** | 0.0967 |
| 6 | 1.894 | 0.929 | 0.621 | 0.644 | **0.647** | 0.0969 |

It falls fast, then **plateaus**, nowhere near the ordered branch.
The disordered branch is a real state, not a slow transient.

> **Corollary that caught an error in my own first pass**: the L = 12
> hot run reads 1.41 not because the branch sits there but because
> 3000 sweeps is *a point on this curve*. The branch value is the
> plateau. The first version of s4 used the unrelaxed number.

Caveat on the plateau itself: it drifts with volume (0.510 → 0.647),
so whether it survives to infinite volume — or drifts to Haar's
2.79 — is not settled here.

## 4. The derived point never disorders

| L | \|⟨P⟩\| ordered | \|⟨P⟩\| disordered |
|---|---|---|
| 6 | 0.858 | 0.028 |
| 8 | 0.818 | 0.014 |
| 12 | 0.724 | 0.010 |

The ordered branch stays ordered at every reachable volume, so its
correlation length exceeds the box at every box. **That is a lower
bound, not a measurement.**

## 5. The number, and what it now depends on

Two-loop SU(2): a Λ_L = (b₀g²)^{−b₁/2b₀²} exp(−1/(2b₀g²)), g² = 4/β.

| source | β_eff | ξ/a |
|---|---|---|
| the weight's own κ | 13.34 | 6.4e+14 |
| **ordered branch** (0091's protocol) | 15.46 | **1.9e+17** |
| **disordered branch** (relaxed plateau) | 2.94 | **8.6e+02** |

> **Ratio between the branches: 2.2e+14 — fourteen orders of
> magnitude.**

0092 found the Born weight's exact zeros are impassable barriers and
filed the branch split as an ergodicity nuisance. **It is not a
nuisance.** Which branch the τ → 0⁺ equilibrium selects *is* the
scale hierarchy — and 0069's (D) asked for exactly one thing, "why
is gravity weak," which is a question about a hierarchy. This is the
first time that question has had a computable handle attached.

Caveats, named: the two-loop formula is Wilson's, and the derived
weight is band-limited with hard zeros. Universality fixes the
continuum theory but not the Λ-parameter ratio, an O(1)–O(10)
multiplicative unknown sitting on a number of order 10¹⁵. §4's bound
is measured; §5 is an estimate.

## 6. The next stone

Decide the branch. Two routes, both standard and both affordable:
**thermodynamic integration** in τ down each branch to compare free
energies at τ = 0, or **parallel tempering** in τ so the τ = 0
replica samples the true equilibrium. The second doubles as a test
of whether the τ → 0⁺ limit connects to the τ = 0 measure at all —
if swaps into τ = 0 are never accepted, the discontinuity is
itself the finding.
