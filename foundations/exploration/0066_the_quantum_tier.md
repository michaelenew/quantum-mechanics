# 0066 — The quantum tier: the deficit law survives, and where it splits

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0065's open 1: replace the Gaussian channel with a quantum carrier,
Fisher with Bures, mutual information with whatever survives — does
δ = 2π(1 − e^{−I}) hold, and with which information measure? Model:
a qubit records the relative coordinate as a rotation
|ψ_θ⟩ = e^{−iκθσ_y/2}|0⟩, Gaussian prior, everything computed
exactly or by deterministic quadrature. The law survives in two
regimes and splits, sharply and instructively, in the third. Code:
`output/0060_the_quantum_tier.py` (0.26 s).

---

## 1. The metric derivation survives quantization

For a network whose channels write κ × (line-of-sight separation)
into qubit rotations, the **Bures** metric on configuration space —
computed numerically from fidelity, no formula assumed — is

```
g_B = (QFI/4) · u uᵀ   per channel,   additive over channels
```

(max deviation 8×10⁻⁷ for two channels on a product carrier). The
weight identification survives quantization: **w_Q = QFI**, the
quantum precision. And it is worth saying where Bures comes from:
fidelity is |⟨ψ|φ⟩|² — **the quantum metric tier is built on the
ledger's own rule, probability = amplitude².**

## 2. The weight is attainable, and the Gaussian tier is the weak limit

The σ_x readout has classical Fisher = QFI = κ² at *every* θ (machine
precision) — w_Q is the precision of the best measurement, not an
abstract bound. And at weak coupling the record's mutual information
matches 0065's classical law ½ln(1 + QFI) to 0.3%. The Gaussian tier
is the weak limit of the quantum tier, as it must be.

## 3. The bijection splits into a tower

Classically w and I determine each other (w = e^{2I} − 1). At the
quantum tier, at strong coupling:

| κ | I_record | χ (Holevo) | classical law ½ln(1+κ²) | ln 2 |
|---|---|---|---|---|
| 0.1 | 0.0050 | 0.0174 | 0.0050 | 0.6931 |
| 1.0 | 0.2618 | 0.4958 | 0.3466 | 0.6931 |
| 3.0 | 0.3069 | **0.6931** | 1.1513 | 0.6931 |
| 30.0 | 0.3069 | **0.6931** | **3.4018** | 0.6931 |

**I_record ≤ χ ≤ ln d, all saturating, while QFI grows without
bound.** A single qubit's extractable correlation is capped by its
dimension; its distinguishability is not.

This is the trust split, one level deeper: **the two things the
classical tier merged — trust (precision/QFI) and correlation
(extractable MI) — come apart exactly where quantum mechanics
begins.** Kalman merges confidence into variance; the Gaussian tier
merges trust into information; the quantum tier is where the merger
finally fails, and the failure is the dimension bound.

## 4. The deficit law: two survivals and one split

**(i) Weak coupling** — survives, all measures coinciding (0.3%).

**(ii) Persistent channels** — survives *exactly in the limit*. For n
uses (wrap-free, κ = 0.3), the accumulated record's MI converges to
½ln(1 + n·QFI): ratio 0.9973 → **1.0000** by n = 600. The web's
channels are persistent — this is the physical regime — and there

```
δ = 2π(1 − e^{−I_record})
```

holds with no quantum correction. The classical law is the many-use
limit of the quantum law.

**(iii) A single strong carrier — the split.** Geometry follows the
QFI weight: δ → 2π as κ → ∞. The information law is capped by the
carrier's dimension:

```
δ_info ≤ 2π(1 − e^{−ln d}) = 2π(1 − 1/d)
```

For a qubit, **exactly π: one maximally-informative qubit can close
at most half the circle by correlation accounting**, while its
distinguishability can close nearly all of it. Measured: at κ = 10,
δ_QFI = 5.66 against the χ-law's 3.1416.

**The mass reading sharpens.** 0065's m = (1 − e^{−I})/4G becomes,
at the quantum tier, a *distinguishability* bound rather than a
correlation bound: a defect approaching the extremal mass 1/4G
requires unboundedly many carriers or unbounded carrier dimension —
per carrier, correlation buys at most (1 − 1/d)/4G. Mass counts
carriers, not just correlation strength. (Resonant with holographic
entropy-bound intuitions; cited as flavor, not claimed as
equivalence.)

## A postulate-level caveat, recorded

0005 states "Chentsov (classical) / Petz (quantum) uniqueness fixes
the metric up to scale." The classical half is right. The quantum
half needs a caveat: **Petz classifies a family of monotone metrics
on mixed states, not one** — uniqueness holds on *pure* states
(where every monotone metric restricts to Fubini–Study) and via the
operational Cramér–Rao selection of Bures as the attainable-precision
metric. The channel families used here are pure-state, so downstream
results are unaffected; but the postulate's phrasing overstates, and
any future *mixed-state* channel construction must choose its metric
and say why.

## Honest limits

- **One-sided model**: classical latent, quantum carrier. This
  quantizes the *carrier* of the correlation, not both ends. The
  fully relational version — entangled ρ_AB, both ends quantum,
  entanglement entropy in place of MI — is the true RT-shape
  question and remains open. This is the most important scope line
  in the document.
- I_record's strong-coupling plateau (0.307) is specific to the σ_x
  readout under wrapping; the rigorous cap is χ ≤ ln 2
  (measurement-independent). The accessible information (optimal
  POVM) was not computed; the tower's ordering is what is used.
- The many-copy survival is shown wrap-free (κ = 0.3); at κ = 1 an
  identifiability gap (bounded, from the sine channel's two-branch
  ambiguity) persists in absolute terms while the ratio still → 1.
- The deficit composition inherits 0019/0020's 2+1 static scope
  throughout.

## Open

1. **The two-sided quantum tier**: entangled ρ_AB with both nodes
   quantum — which correlation measure takes I's place, and does
   2π(1 − e^{−I}) survive with entanglement entropy? The precise
   modern form of the repo's oldest flagged row, one level up.
2. **The π ceiling as physics**: if the web ever realizes
   single-strong-carrier channels, the model predicts a *half-circle
   deficit ceiling* per quantum — is that visible in the quantum
   lattice (0054's deficit was 2πn/N, built from many plaquettes)?
3. **d-dimensional carriers**: the cap 2π(1 − 1/d) is a one-line
   prediction — verify at qutrit, and note d → ∞ recovers the
   classical law's reach.
4. Standing: t and N; the τ A/B; the bond's h² from redundancy; the
   nonabelian Dirichlet square.
