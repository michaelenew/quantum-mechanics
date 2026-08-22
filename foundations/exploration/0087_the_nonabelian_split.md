# 0087 — The nonabelian split: the two ledgers survive the lift

Eighth stone, the bridge back up the ladder: does 0086's polar
theorem survive the nonabelian lift? SU(2)'s characters are real, so
the abelian phase cannot lift *as a phase* — and it doesn't. It lifts
as something better organized: a **character-indexed factorization**,
verified exactly at the algebra level and validated end-to-end by a
gauge-unfixed link Monte Carlo, on the 2D rung with the program's own
Born counting weight (0074: W = A², A = Σ_{j≤2} χ_j). Code:
`output/0078_the_nonabelian_split.py`.

---

## 1. The record envelope is fusion arithmetic

The per-plaquette transfer coefficient of the ledger — the nonabelian
f(N) — is pure counting:

```
r_j = c_j / (d_j c₀),   c_j = #{(m,m′) in the counting² : m⊗m′ ∋ j}
```

For the flat counting to j = 2: **r = 1, 4/5, 2/3, 1/2, 9/25, 1/5** —
exact rationals (quadrature agrees with the fusion count to 1e−8).
The abelian jitter f(N) = φ(N)/P(N) was arithmetic; its SU(2) heir is
the Born weight's fusion table. The record ledger stays counting all
the way up.

## 2. The factorization, and the reading theorem

With a source of holonomy class h₀ enclosed by a loop of area A (2D
gluing; the standard convolution identity does the work):

```
⟨χ_j(loop)⟩  =  [χ_j(h₀)/d_j]  ×  d_j r_j^A
                 └─ source ─┘      └ record ┘
```

per representation, exactly. The consequence with the physics in it:

> **The reading theorem.** ⟨χ_j⟩(A, h₀) / ⟨χ_j⟩(A, e) = χ_j(h₀)/d_j
> at *every* area. The record damps the signal (r_j^A) but cannot
> distort the reading — a loop reads the enclosed source's class
> angle exactly, through any amount of vacuum record. 0086's "records
> damp, sources twist" survives with "twist" generalized to "imprint
> the character spectrum."

Validated with no gauge sleight: a 7-link, 2-plaquette open lattice,
Haar-sampled SU(2) links (quaternions), weight-reweighted MC —
vacuum ⟨χ_j⟩ = d_j r_j² within error bars, frustrated readings match
χ_j(h₀)/d_j (j = ½: 0.6212 vs 0.6216), and **the class angle
reconstructs from the MC readings to θ̂ = 0.9005 against true 0.9.**

## 3. Where the abelian phase went

The lift redistributes the polar decomposition:

| abelian (0086) | SU(2) (here) |
|---|---|
| phase e^{2πi n_enc/N} — full source ledger | **shrinks to the center Z₂**: a center twist reads (−1)^{2j}, exactly, modulus untouched — the 't Hooft sector, SU(2)'s only true phases |
| — | **the continuous deficit migrates into the reading spectrum** χ_j(h₀)/d_j: the source ledger is a spectrum, not a phase; the class angle is recovered by rep scan |
| modulus f^A | envelope r_j^A, fusion-rational |

Physical corollary worth keeping: **integer-j probes are
center-blind** — the graviton channel (1,1) reads class angles
(geometry) and never the Z₂ flux, while half-integer (fermionic)
probes read both. If the program ever carries matter, fermions see a
topological sector gravity cannot.

## Honest limits

- **2D rung.** The factorization's exactness uses 2D character
  gluing (coefficients multiply). The 4D theory shares the ledger
  measure but glues through the vertex (0078-the-vertex's 16D
  machinery), where the split is a motivated conjecture, untested.
- One counting (flat, j ≤ 2). The r_j rationals are specific to it;
  the factorization structure is counting-independent (any positive
  class function), which the algebra shows but only this weight was
  run.
- The MC validates A = 2 with one h₀ and three reps; error bars ~1–4%
  (j = 2 reading sits 1.5σ off — noise, not signal, by the batching
  estimate).
- The frustration model (plaquette weight W(gh₀⁻¹)) is the toy's
  source; the full theory's sources are boundary states, not
  frustrations.

## Open

1. **The 4D split**: test source-vs-record factorization on one
   vertex — insert a class twist into 0078's 16D shared-frame
   Gaussian and check whether the vertex weight factorizes into
   (source character) × (simplicity record). The natural next
   heavy-adjacent stone, now with a precise question.
2. The 't Hooft sector's physics: the Z₂ flux is invisible to
   gravity but not to fermions — does the program's matter thread
   (when it exists) inherit a superselection rule here?
3. The mixed case: sources at multiple plaquettes with non-commuting
   classes — 2D gluing handles it (readings multiply as class
   convolutions); the ordered/path-dependent version is where 4D
   will differ. Quantify on a 3-plaquette chain.
4. Reading-theorem operational form: the record-independence of the
   reading is a channel-capacity statement (the vacuum is a
   non-distorting, purely attenuating channel for class information)
   — connect to the filter program's oracle-gap decomposition (F1's
   dictionary row).
