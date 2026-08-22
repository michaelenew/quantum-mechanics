# 0085 — The quarter: two ledgers, one horizon

Sixth stone: **C4** — confront the measured horizon accounts (C1's
entropy, C3's capacity and deficit) with Bekenstein–Hawking's A/4G.
0070 said the 1/4 is the hard part and to treat a mismatch as a
finding. There is a mismatch, it is structural, and it is the most
clarifying thing path C has produced: **the program keeps two ledgers,
and only one of them can be Bekenstein–Hawking.** Code:
`output/0076_the_quarter.py`.

---

## 1. The 1/4 is located, not derived

Setting the measured vacuum-cut entropy equal to A/4G fixes the
regulator, and it lands at the Planck scale with an O(1) measured
coefficient:

| account | graviton coeff | ⇒ a/ℓ_P |
|---|---|---|
| entropy, NN stencil | 0.0487/a² | **0.441** |
| capacity, NN | 0.0358/a² | 0.379 |
| entropy, CD (program stencil) | 0.0987/a² | 0.628 |
| capacity, CD | 0.0743/a² | 0.545 |

Since G is *registered* in this program (0058 §2.2b), these are
consistency conditions, not predictions: **if** the horizon's
thermodynamic entropy is the vacuum record crossing it, **then** the
lattice spacing is 0.4–0.6 ℓ_P, with the regulator and account choice
moving the number by O(1). That is exactly the Sakharov/induced
position 0082 §4 predicted C4 would be forced into. No bare match
exists; the 1/4 lives in the renormalized sector. The honest summary:
the program *accommodates* the 1/4 the same way every cutoff QFT
does, and earns no extra credit here.

## 2. The finding: the deficit ledger cannot be the BH charge

The program's own deficit additivity (0012, exact) says a mass M
sources total deficit 8πGM, however arranged. On a Schwarzschild
horizon, A = 16πG²M², so

```
δ_source  =  8πGM  =  2√(πA)        — G drops out; scales as √A
```

while the measured vacuum-cut deficit (0084) is **area-extensive**:
δ_record/A = 0.0522 rad/plaquette, drift 5% across N⊥ = 16 → 32. Two
different scalings mean two different objects:

> **The deficit is the source ledger** — extensive in mass,
> counting what the horizon has *recorded as matter*.
> **The entropy/capacity is the record account** — extensive in
> area, counting the zero-point relational structure crossing the
> cut. Only the record account has the A-scaling of
> Bekenstein–Hawking. The program does not identify δ with S_BH,
> and after this stone it cannot: they disagree at every scale
> above the crossing point A* ≈ 1.2×10³ a² (R* ≈ 4 ℓ_P).

The corollary is the deepest structural statement of the arc. Above
~5 ℓ_P, every horizon's zero-point record dwarfs its sourced deficit
by arbitrarily many orders. If the vacuum's area-extensive record
*sourced* deficit, every cut in empty space would curve
catastrophically — the cosmological-constant problem reappearing at
every surface. It does not, and the program already owns the reason:
**the budget/zero-mode deletion (0069 §2, 0080)** — the uniform
record does not gravitate; only structure above it does. Path Λ's
constraint is what makes path C's vacuum safe. The two falsifiability
paths protect each other, and neither was designed to.

## 3. The saturated-channel picture, sharpened to a falsifiable shape

Per collective channel the deficit 2π(1 − 1/2ν) saturates at the full
turn, with **99% saturation at a record of I = ln 100 ≈ 4.6 nats** —
a channel is essentially extremal once it has recorded five nats. In
3+1 the saturated object is a **string defect of extremal tension
μ = 1/4G** (δ = 8πGμ = 2π closes the cone completely — the same
extremal cap as 0065's m → 1/4G). Then a mass M's worth of extremal
string has total length

```
L  =  M/μ  =  4GM  =  2R_s        — the diameter, G-independent
```

So the sharpened conjecture, stated for falsification rather than
comfort: **a horizon's source structure is one-dimensional — of order
R_s/ℓ_P saturated string-channels, the string defects Ambrose–Singer
left to the finite sector (0061 §4) — while its record structure is
two-dimensional, A/ℓ_P² of vacuum entanglement.** Holography counts
the area; this program's *source* count is a diameter. Those are
different enough to kill one of them eventually, which is what a
conjecture is for.

## Honest limits

- The flat cut is a Rindler proxy for a horizon throughout; no black
  hole geometry was constructed. C2's thermality licenses the proxy
  for near-horizon statements only.
- "δ_source of a horizon = 8πGM" chains the program's deficit
  additivity with GR's horizon-area relation (legitimate — the
  program is classically GR, 0060 — but it is a chained
  interpretation, not a lattice measurement).
- The extremal-string reading of a saturated 3+1 channel imports the
  cosmic-string deficit formula δ = 8πGμ; the bundle picture of §3 is
  a conjecture shape with two measured anchors (the 2π cap, the 4.6
  nats), not a derivation.
- §1's a/ℓ_P numbers inherit every C1 caveat (free theory, stencil
  dependence, Srednicki-from-memory unverified).
- The mutual-protection argument of §2 is structural, not yet a
  calculation: nobody has computed a cut's *sourced* curvature with
  the budget constraint imposed and watched the cancellation happen.
  That computation is well-posed in the Z_N toy (0080's machinery
  plus a defect) and is the right next test of the claim.

## Open

1. **The protection calculation**: impose the budget on an open Z_N
   lattice containing a cut plus a defect; verify the vacuum record
   contributes no deficit while the defect's does. (First C4 item
   that is *cheap* — toy-sized.)
2. The saturated-channel bundle: build one extremal channel through a
   cut and check C2's modular structure survives saturation.
3. The decoherence tier (0068): measurement as discharge from record
   account to source ledger — the two-ledger split makes this
   question precise for the first time: *collapse moves an entry
   between the ledgers.*
4. Path C standing items now closed or transformed: C1 ✓, C2 ✓,
   C3 ✓, C4 ✓ (as located-plus-finding). The path's remaining life
   is items 1–3 above plus the interacting versions.
