# mechanism — SUMMARY

> **AI-generated, not peer-reviewed.** Prior art credited in [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results are re-derivations of
> established work unless explicitly marked otherwise.

What a measurement *is*, mechanically, under the corrected (nonlocal,
consistency-first) reading.

## Current state

**Measurement = coincidence = split/merge** (`exploration/0001`). When two
systems reach the same place, their relative coordinate `q = q1 − q2` becomes
sharp. In CoM/relative variables:

    [Q,P] = [q,p] = iħ,   [q,P] = [Q,p] = 0

Relative position `q` and total momentum `P` commute and are sharp together —
the EPR state. Verified symbolically in
`output/0001_relative_coordinate_checks.py`; matches SPDC + Howell (2004).

**Reframed:** the sharpening of one edge is not a local event whose
consequences race outward at *c*. It triggers a **global re-satisfaction of
the consistency constraint** across the whole connected component of the
interaction graph — instantaneously (`exploration/0002`,
`foundations/0003`).

## The dilution law (`exploration/0002`)

Two mechanical claims driven by monogamy:

- **Reach:** the update touches every particle in the same connected component
  of the interaction graph. Combinatorial, not metric — hence no "speed."
- **Strength:** on a distant particle *X*, bounded by residual pairwise
  correlation `I(A:X)`. Correlation is monogamous, so a particle that has
  since interacted with many others has diluted its correlation with any old
  partner to ~`C_total / N` at most — often astronomically less. That is the
  quantitative skeleton of the posit's "small / random / very-hard-to-detect."
- **Decoherence re-read as dilution, not destruction:** the correlation
  carrying which-path information is not annihilated by the environment —
  it is spread across so many partners that any local subset can no longer
  recover it. Global consistency is preserved; local interference is lost
  because the local subsystem no longer contains a global section.
- **Firewall:** the outcome of each measurement is random, so the
  instantaneous distant update averages to zero in every marginal → no
  signalling. The Heisenberg-scale randomness is *exactly* the amount needed
  to guarantee this.

## Consequences

- Sensor "spike" = sharpening of the detector–system relative coordinate;
  distant partners' knowledge of that system updates instantly (dilutedly),
  but nothing is signallable.
- Buckyball intact = internal `ρ_internal` is a priori sharp; environment
  dilutes only CoM which-path correlation.
- "Could have known" = the correlation was already shared into the environment.

## Artifacts

- `output/0001_relative_coordinate_checks.py` — commutator algebra, chain
  variance additivity, Gaussian fusion. Pure stdlib. Runs; all pass.

## Known gaps

- Dilution scaling (~`1/N`) is heuristic; deriving a sharp bound
  `update(X) ≤ f(I(A:X))` from a monogamy inequality is a concrete open target.
- Quantum-MRE equivalence to Lüders — still open (see `foundations/`).
