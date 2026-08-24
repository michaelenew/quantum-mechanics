# 0102 — The coupling scan: the scale field along the flow, and the nodes as barriers

0101's opens, run with the compiled kernel: does the dressed vacuum's
scale field grow toward strong coupling, and is its short range a
finite-size artifact? The coupling axis is the theory's own: the bare
Born weight flowed by the SU(2) heat kernel,
W_τ = Σ_j c_j e^{−τ j(j+1)} χ_j (c_j the integer fusion counts,
c_0 = 6) — τ = 0 is the bare stack, growing τ walks toward the IR of
the flow (0092/0093), ending at Haar. Positivity is automatic.
Code: `output/0092_the_coupling_scan.py`.

**The kernel.** The sweep is now a C kernel (embedded in the module,
compiled at import): 0.46 μs per link-update, 26× the numpy
reference, with the xoshiro RNG state round-tripping through the same
atomic checkpoints as 0091. Gates: (g1) 20 sweeps == 10 +
save/restore + 10, bitwise; (g2) free theory reproduces Haar (0.5%);
(g3) the L = 4, τ = 0 ordered run reproduces 0091's Python reference
**exactly** — ⟨θ²⟩ 0.0968 vs 0.0968, SD(ln θ) 0.475 vs 0.475. The
Python module stays the correctness reference.

---

## 1. Found by the gate: the amplitude's nodes are ergodicity barriers

The first pass failed g3 — and the failure was physics. A hot-started
(Haar-random) chain at τ = 0 lands in a branch **8× broader** than
the ordered-start reference and stays there:

```
τ = 0:  ordered start   ⟨θ²⟩ = 0.0968 ± 0.0001
        disordered start ⟨θ²⟩ = 0.7789 ± 0.0004  (relaxes 1.10 → 0.74
        over ~10k sweeps, then plateaus through 40k: metastable)
τ = 0.05:  ord 0.132  vs  dis 0.457   — still split (hysteresis)
τ = 0.15:  ord 0.2124 vs  dis 0.2125  — agree to 4 digits
```

The bare weight W = A² has exact zeros (the roots of the summed
character A); local Metropolis effectively never crosses them, so the
configuration space fractures. Any τ > 0 lifts the zeros; by
τ = 0.15 both starts give one answer. And the ordered branch is the
one continuous with the unique τ > 0 equilibrium — the primary curve
⟨θ²⟩ = 0.097, 0.132, 0.213, 0.349, 0.684, 1.607 is monotone through
the hysteresis window. **The flow selects 0091's branch**, retroactively
validating the dressed-vacuum measurement.

Filter reading, offered as a hypothesis: an amplitude node is a
hypothesis with exactly zero weight, and local model-search cannot
cross it; smoothing (coarse-graining) is what makes hypothesis space
connected. The sharp weight traps; the flowed weight anneals.

## 2. The flow scan: a plateau, then trivialization

L = 6 (L = 4 agrees throughout; primary branch shown):

| τ | bare ⟨θ²⟩ | dressed ⟨θ²⟩ | kurt | SD(lnθ)/ctl | s_P-excess | c(1) |
|---|---|---|---|---|---|---|
| 0.00 | 0.417 | 0.097 | 2.90 | 0.475/0.483 | +0.0120 | +0.049 |
| 0.15 | 0.605 | 0.213 | 3.02 | 0.483/0.483 | +0.0131 | +0.056 |
| 0.30 | 0.784 | 0.350 | 3.07 | 0.486/0.483 | +0.0133 | +0.057 |
| 0.60 | 1.114 | 0.687 | 3.14 | 0.490/0.483 | +0.0131 | +0.060 |
| 1.20 | 1.655 | 1.609 | 2.98 | 0.485/0.483 | +0.0040 | +0.019 |

Three statements, all volume-stable (L = 4/6/8 agree):

- **The scale field's amplitude does not grow toward strong coupling
  — it holds a plateau** (~0.013 log-units, gentle maximum near
  τ ≈ 0.3) across a coupling range where the bare width changes 4×,
  then collapses at τ = 1.2 as the weight trivializes toward Haar.
  The field is a property of the flow's *transition region*, not of
  either endpoint (bare = stiff, Haar = structureless).
- **The marginal crosses from slightly sub-Gaussian to slightly
  super-Gaussian along the flow** (kurt 2.90 → 3.14, SD(ln θ)
  0.475 → 0.490 vs control 0.483): the radial mixture 0097 expected
  does weakly reappear at stronger coupling — at the percent level,
  never as fat tails.
- **The correlation range grows, slightly.** At L = 8 (distances to
  4): τ = 0 gives c(2) = +0.0004 ± 0.0003 — the short range of 0101
  is physical, not finite-size; τ = 0.6 gives c(2) = +0.0021 ± 0.0002
  — small but unambiguous growth of the correlation length with
  coupling.

## 3. The answer to "which sector wins"

None does, this side of trivialization. The sector-carrying
coordinate (the scale field) stays weak-but-persistent — s_P ≈ 0.013,
nearest-neighbor φ ≈ 0.05–0.06, range ~1 lattice unit growing
mildly — until the flow erases the stack structure altogether. The
dressed vacuum never develops a strong mixture at any coupling; the
sector physics is perturbative everywhere along the flow. These are
the physical trust-channel parameters, now measured as *functions of
coupling*, handed to the wall-correspondence.

## Honest limits

- W_τ is the heat flow of the *weight*, the same smoothing the RG
  applies (0092), but the lattice ensemble under W_τ is not literally
  the blocked theory — it is the natural one-parameter family the
  program owns, used as the coupling axis.
- The hysteresis window is bracketed (0.05 < τ* < 0.15), not located;
  the order of the transition is uncharacterized.
- Product measure over plaquettes, as in 0091; vertex corrections
  untested.

## Open

1. Locate τ* and characterize the transition (first-order-like
   hysteresis vs slow crossover); does the metastable branch's
   lifetime diverge with volume?
2. The node-barrier ↔ filter correspondence: what is the filter-side
   experiment for "zero-weight hypotheses fracture local search,
   smoothing anneals it"? (Candidate: prequential comparison of
   sharp vs tempered hypothesis banks under local model-search.)
3. Feed (s_P(τ), φ(τ)) to wall-correspondence — done alongside this
   stone (lucid 0004).
