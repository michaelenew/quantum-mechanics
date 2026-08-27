# 0084 — The capacity cut: the web's own count across the horizon

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Fifth stone: **C3** of path C (0070) — cut the same surface as
C1/C2, but count what the *web* says crosses it. 0067 chose the
correlation measure at pair level (curvature couples to tangle, not
entropy); 0068 decomposed the budget and warned, via GHZ, that
capacity can be collective — invisible to every pair. This stone runs
both lessons at field level. Done-criterion ("cut capacity ∝ area,
coefficient in ledger units"): **met** — and the pairwise account
fails in exactly the way 0068 predicted. Code:
`output/0075_the_capacity_cut.py`.

---

## 1. The cut is a stack of collective squeezed channels

For the pure Gaussian vacuum the reduced states of the two sides
share one symplectic spectrum — verified to 5.6e−16 — so the cut
decomposes into **collective two-mode-squeezed (TMS) channels**, one
per ν_k > ½, with ν = ½cosh 2r. Each is a genuine relational channel
in 0067's sense: the phase θ written between the correlated branches
of Σ λⁿe^{inθ}|nn⟩ has QFI = 4·Var(n) = sinh²(2r) — the
continuous-variable heir of C² (both are four times the generator's
variance). So the program's whole ledger chain applies verbatim, per
channel:

```
capacity  W_k = sinh²(2r_k) = 4ν_k² − 1
record    I_k = ½ ln(1 + W_k) = ln(2ν_k)          (0065's w–I map)
deficit   δ_k = 2π(1 − e^{−I_k}) = 2π(1 − 1/(2ν_k))
```

Three accounts — entropy S, capacity W, deficit δ — as three charges
on **one spectrum**.

## 2. The pairwise account fails, exactly as the GHZ lesson said

Two-site log-negativity across the cut, in the vacuum:

| pair separation | adjacent | all others tested |
|---|---|---|
| E_N | 0.306 (chain) / 0.074 (3D) | **exactly 0** |

Only the single adjacent pair is entangled — at distance 2 and beyond
the two-site reduced states are *separable*, in the chain and in 3D
alike (even diagonal neighbors). The adjacent pair carries 12% (in
capacity units; 15% in contangle units) of the cut's total. Meanwhile
the collective channels carry a robust area law.

> **The field vacuum is GHZ-like, not W-like.** Its cut capacity is
> collective; the literal-pairs reading of P1 undercounts it by an
> order of magnitude at range and misses it entirely beyond one
> lattice spacing. 0068's refinement — P1 as node-vs-rest
> bipartitions — is not optional; the free graviton vacuum forces it.

Site-level bookkeeping in a single currency (Gaussian contangle):
the CKW-shaped inequality Σ_pairs E_N² ≤ contangle(node|rest) holds
with room (0.033 ≤ 0.089), and the collective share at site level is
**63%** — a majority, though not the ~99% I first guessed; the module
records the corrected number. (Consistent with Adesso–Illuminati's
Gaussian contangle monogamy, cited not re-proven.)

## 3. Three area laws, and the ledger-unit coefficient

All three accounts converge per unit cut area (N⊥ = 16 → 32, NN
stencil, per polarization):

| account | coefficient |
|---|---|
| entropy S/A | 0.0244 (C1's number) |
| capacity W/A | 0.0179 |
| **deficit δ/A** | **0.0522 rad per plaquette** |

So the program's own horizon charge is: **the graviton vacuum's flat
cut carries 2 × 0.0522 ≈ 0.104 radians of deficit per plaquette of
horizon** (two polarizations). That is C3's done-criterion — the cut
charge in the theory's native units, ready to face A/4G in C4. (Both
sides of that confrontation are regulator-dependent; 0082 §4's
renormalized-G framing applies to the ledger side equally.)

## 4. The discriminator now runs — capacity is not entropy

Adding a uniform mass and re-measuring the ratios of the accounts:

| M² | 0 | 0.09 | 0.5 |
|---|---|---|---|
| W/S | 0.787 | 0.678 | 0.614 |
| δ/S | 2.183 | 2.053 | 1.897 |

The ratios are **not constants**: W/S drifts 1.28× across the scan.
At pair level 0067's discriminator was a table of numbers; at field
level it is a *response function* — a horizon charge coupled to
capacity responds differently to the field's mass/IR content than one
coupled to entropy. Any construction that fixes the horizon charge
(C4, or the saturated-channel conjecture) will therefore *decide*
between the two couplings rather than straddle them. That is the
sharpest in-model falsification surface path C has produced.

## Honest limits

- **The field-level capacity is an extension, not yet a derivation.**
  At pair level 0065 *derived* w = precision from the Fisher metric
  of an explicit inference network. Here W_k = 4ν_k² − 1 is the
  natural TMS-QFI extension of that chain — well-motivated (same
  4·Var structure, same w–I–δ ledger), but no field-level inference
  network has been constructed to derive it. This is the gap between
  "the program's count" and "a count in the program's spirit."
- Free theory, NN stencil, modest sizes (L = 64, N⊥ ≤ 32; the W/A
  drift at N⊥ = 16 → 32 is 10%, the slowest of the three accounts —
  its k⊥ → 0 behavior is more IR-sensitive, (ln ξ)² per mode vs ln ξ
  for entropy).
- Mixed-pair entanglement measured by log-negativity (the Gaussian
  contangle proxy); other mixed-state tangles could shift the small
  pairwise shares, not the exact zeros.
- Contangle monogamy is cited from the literature for the s5
  inequality's interpretation, not re-proven.

## Open

1. **Derive the field-level capacity**: lift 0065's inference-network
   construction to the Gaussian field so W_k is *derived* rather than
   extended. Closing this would make §3's 0.104 rad/plaquette a
   theorem of the postulates.
2. **C4** — confront δ/A (and S/A) with A/4G under the κ-unit
   reading, renormalized-G framing on both sides.
3. The saturated-channel conjecture with C2's modular target and
   this stone's charge: does I → ∞ produce exactly 2π per channel?
   (Note δ_k → 2π as ν → ∞ — the per-channel deficit *saturates at
   2π*, the full-turn cap of 0066, which is suggestive enough to
   check properly.)
4. The decoherence tier (0068 open 1): does measurement literally
   discharge W into bias at field level?
