# 0101 — The dressed vacuum: the discriminator answers, and revises both sides

The catalogue's named discriminator, run: 4D SU(2) lattice gauge
theory with the derived Born plaquette weight (flat counting to
J = 2.5, the N = 5 stack's cutoff), Metropolis over links,
compactness intrinsic. Four independent chains, 4000 sweeps each,
atomically checkpointed and resumable (`output/mc0091/`); correctness
gates: exact gauge invariance (1.5e−15) and the free theory
reproducing Haar (0.2%). Code: `output/0091_the_lattice_mc.py`.

The 0100 split — group-level says the vacuum is a scale mixture,
algebra-level says it isn't — was a point to revisit, and the lattice
revises **both** positions rather than crowning either.

---

## 1. What the dressed vacuum is

| statistic | bare Born | dressed (measured) | Gaussian ref |
|---|---|---|---|
| ⟨θ²⟩ | 0.417 | **0.0968 ± 0.0001** | — |
| kurtosis proxy | 12.5 | **2.90 ± 0.00** | 3 |
| SD(ln θ) | 0.620 | **0.475 ± 0.000** | 0.483 (matched) |

Link-sharing does two things at once. It **stiffens** the vacuum
(each link serves six plaquettes; the dressed marginal is 4× narrower
than the bare weight) and it **Gaussianizes** it: the fat tails that
defined the bare Born ensemble (kurtosis 12.5) are gone — the dressed
marginal sits *at* the Gaussian reference in both kurtosis and the
radial-mixture statistic. **The one-point radial mixture does not
survive dressing.** 0097's expectation, already refuted at the
boxed-algebra level, is now refuted at the honest lattice level too —
by a different mechanism (averaging over shared links, the same
CLT-flavored Gaussianization 0092 found in the RG's pointwise
products), which is worth more than the boxed result because nothing
artificial produces it.

## 2. What survives: a weak, genuinely spatial scale field

The per-site scale field ρ_x (RMS of the six plaquette angles based
at x) carries structure the marginal cannot show:

```
SD_sites(ln ρ) = 0.1767 ± 0.0003   vs   shuffle control 0.1646
        → clustering excess +0.0120

spatial correlation of ln ρ:  d = 1: +0.0453 ± 0.0005   d = 2: −0.004
```

Small — but at these error bars, unambiguous. **The dressed vacuum
has a wandering-scale field**: weak (s_P-excess ≈ 0.012 log-units),
short-ranged (nearest-neighbor persistence, gone by distance 2 at
this lattice size). In the filter's hardware: the physical s_P is
positive but small, and the physical φ is short.

## 3. The reconciliation

Both local models of 0100 were wrong in complementary ways, and the
lattice says how:

- The **group-level bare weight** overestimated the mixture: its fat
  tails are a *bare* feature that dressing averages away.
- The **boxed algebra ensemble** underestimated the structure: it had
  no link-sharing, so it could not show the clustering field at all
  (and its cutoff dominance was an artifact of the box).
- The **true vacuum**: Gaussian one-point marginal + a weak,
  spatially correlated log-scale field.

This lands the marginalization story (0097) in a sharper place: the
coordinate that carries sector discrimination — the scale mixture —
exists in the dressed vacuum *as a spatial field, not as marginal
tails*, and its amplitude at this coupling is ~1% in log-units. The
sector physics at weak coupling is correspondingly weak; if it grows
anywhere, it grows where the scale field does — toward strong
coupling (larger effective τ), which is where the flow (0093) drives
the IR anyway. Consistent, and now measured rather than argued.

## Honest limits

- One coupling (J = 2.5), one volume (L = 4); the d = 2 correlation
  is at the lattice's midpoint, so "short-ranged" is bounded by
  finite size. A J-scan and L = 6–8 run are the natural follow-ups
  (compiled kernel recommended there — see module notes).
- The scale field's absolute normalization depends on the ρ
  definition (six plaquettes per site); the *excess over shuffle* and
  the spatial correlation are the invariant content.
- Product measure over plaquettes (the ledger tier); vertex
  corrections (0078) are not in this measure — their effect on the
  scale field is untested.

## Open

1. The coupling scan: does the scale field's amplitude grow toward
   strong coupling (tracking the flow), and does its correlation
   length grow with it? (This is the dressed version of "which
   sector wins" — 0095's remaining question, now phrased in the
   filter's coordinates.)
2. L = 6–8 with a compiled sweep kernel (durable harness already in
   place; the Python implementation stays as the correctness
   reference).
3. Feed the measured (s_P ≈ 0.012, φ short) back to the
   wall-correspondence: the physical trust-channel parameters, first
   values.
