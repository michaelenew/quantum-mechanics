*Follows `0009` (orientation). This is the first test proposed there.*

# 0010 — The cheapness test: Thomas precession

First calculation in this workstream where the answer was **written down before
computing it**. Four predictions stated up front; three confirmed, **one
falsified**. The falsified one is the important result.

`output/0009_thomas_precession.py`, 16/16 checks.

## The predictions, as stated

1. Wigner angle for two boosts:
   `tan(Ω/2) = sinθ·s₁s₂ / (c₁c₂ + cosθ·s₁s₂)`, `c = cosh(η/2)`, `s = sinh(η/2)`
2. Thomas angle per circular orbit: `Δ = 2π(γ − 1)`, exactly, radius-independent
3. Slow limit: `Δ → πβ²` — the famous factor of ½ in spin–orbit coupling
4. **The conjugacy class of a product of two boosts is loxodromic** — a rotation
   appears that neither factor had, which is what `0008`'s taxonomy appears to say

Prediction 4 is what made this a test of *the framework* rather than of
`SL(2,ℂ)`. If a product of two boosts were loxodromic, `0008`'s classification
would predict Thomas precession outright.

## 1–3: confirmed

The Pauli algebra gives the whole thing in one product:

```
[c₁ + s₁n̂₁·σ][c₂ + s₂n̂₂·σ]
   = (c₁c₂ + s₁s₂ n̂₁·n̂₂)          scalar
   + (c₁s₂n̂₂ + s₁c₂n̂₁)·σ          real vector — the boost part
   + i s₁s₂ (n̂₁ × n̂₂)·σ           IMAGINARY — the rotation
```

The rotation term is present iff `n̂₁ × n̂₂ ≠ 0`, visible before any
calculation. Polar decomposition matches the closed form to `1e-9` across
rapidities and angles, including exact vanishing at `θ = 0`.

Circular motion, accumulating `L(φ+dφ)L(φ)⁻¹` around the loop:

| `β` | `2π(γ−1)` | `N = 6000` | rel. err |
|---|---|---|---|
| 0.1 | 0.0316535268 | 0.0316536020 | 2.4e-6 |
| 0.5 | 0.9720121498 | 0.9720119058 | 2.5e-7 |
| 0.8 | 4.1887902048 | 4.1887884960 | 4.1e-7 |

Error falls as `1/N²` through `N = 6000`. The `N = 60000` rows are *worse* —
arithmetic, not physics: each step's angle is `~1e-6` rad and `acos(x)` near
`x = 1` loses half the significant digits. Best accuracy is where
discretisation and round-off cross over.

### A cross-check worth keeping

Rapidity space is hyperbolic 3-space with curvature `−1`, so the holonomy
around a closed velocity loop is the enclosed area, and the hyperbolic area of
a disc of radius `η` is `2π(cosh η − 1)`. Since `cosh η = γ`, that is
`2π(γ − 1)` — matching to machine precision at every `β` tested, out to 0.99.

> **Thomas precession is the curvature of velocity space.** That reframing —
> from anomaly to holonomy — is the kind of thing this workstream is for, and
> it costs nothing.

## 4: FALSIFIED, and this is the finding

```
η₁    η₂    θ        tr A                class
1.00  1.00  1.5708   2.5430806348 + 0j   hyperbolic
0.50  1.50  1.0472   2.8784339348 + 0j   hyperbolic
2.00  2.00  1.1000   6.0151169432 + 0j   hyperbolic
```

`tr A` is **real** and `> 2` in every case, so a product of two boosts is
**hyperbolic** — conjugate to a pure boost. Analytically:
`tr A = 2[c₁c₂ + s₁s₂cos θ]`, manifestly real for real rapidities. Not
loxodromic, ever.

**Where the reasoning went wrong.** The Wigner rotation lives in the **polar**
decomposition (`A = RB`), not in the **conjugacy class**. Those are different
decompositions, and `0008` classified by the second. A product of two boosts
genuinely contains a rotation factor *and* is still conjugate to a pure boost —
no contradiction, but the taxonomy cannot see it.

## What this does to the assessment

The workstream has **two separable assets**, and this test separates them
cleanly for the first time:

| asset | status after this test |
|---|---|
| **Representation** — `SL(2,ℂ)`, Pauli algebra, spinors, bivectors | **Earns its keep.** The rotation is one visible term in one product; the standard route is a page of tensor algebra. This is a real computational win. |
| **Classification** — `0008`'s four conjugacy classes | **Not applicable here, and untested elsewhere.** It is the wrong instrument for this question. |

That distinction matters more than the confirmed predictions, because the
"saves students memorising equations" hope rests entirely on the first column,
and essentially everything novel-sounding in `0004`–`0008` sits in the second.

**Restated honestly:** what has been demonstrated to be cheap is standard
spinor formalism — Penrose–Rindler material, decades old. The framework's own
distinctive contribution, the conjugacy taxonomy, has now had one chance to
predict something and turned out to be the wrong tool. It is not refuted; it
was simply not engaged.

## What would engage the classification

The taxonomy makes claims about *which structures can exist*, so it should be
tested against existence questions rather than dynamical ones. Candidates:

1. **Does the four-class taxonomy forbid anything observed, or explain anything
   absent?** The sharpest target named in `0009`: Wigner's classification
   permits continuous-spin representations that are not observed. If the
   loxodromic/nilpotent structure says why, that is a genuine result. If it says
   nothing, the taxonomy is decorative.
2. **Composition closure.** Products of boosts stay hyperbolic. What *does*
   generate loxodromic elements from physically meaningful inputs? If nothing in
   a realisable process produces them, the generic class is generic only
   formally — a serious problem for a taxonomy that puts massive spinning
   particles there.
3. **`g = 2`.** Still the best value-target, and Carter's Kerr–Newman result
   suggests the geometry knows something.

Item 2 is new, follows directly from this failure, and is cheap. It should
come first.

## Method note

Stating predictions first worked exactly as intended: prediction 4 is one I
would otherwise have asserted as a framework success — the reasoning "products
of boosts generate rotations, therefore loxodromic" is superficially clean and
wrong. Retrofitting would have hidden it.

**Adopt as standing practice: no result claimed for the framework without a
prediction recorded before the computation.**
