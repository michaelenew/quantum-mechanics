# 0061 — Curvature from the quantized 3+1 model

The 2+1 quantum arc got its curvature as a Wilson-loop deficit (0054).
3+1 is richer: Riemann splits into Ricci and Weyl, vacuum kills Ricci
and leaves Weyl, and **that split is the graviton**. This asks whether
the quantized model reproduces it. Two positives and one sharp
negative, and the negative explains something the arc has been
bumping into for five explorations. Code:
`output/0055_the_quantized_curvature.py`.

---

## 1. The split is exact in finite arithmetic

Build the Riemann operator on bivectors over Z_N — a symmetric 6×6
with the first Bianchi identity imposed — and decompose by the
Kulkarni–Nomizu subtraction. That needs 2 and 3 invertible, so N
coprime to 6.

| | dim Riemann | dim Ricci | dim Weyl |
|---|---|---|---|
| **n = 4** (N = 5, 7) | **20** | **10** | **10** |
| **n = 3** (N = 5, 7) | **6** | **6** | **0** |

matching the continuum n²(n²−1)/12, n(n+1)/2 and n(n+1)(n+2)(n−3)/12
exactly — independently confirmed against the standard results.

> **Weyl exists in 3+1 and vanishes identically in 2+1** — the
> graviton's existence, and its absence one dimension down, as a
> statement of finite-field arithmetic. No continuum limit is taken
> to say it.

This is the sharpest form yet of the repo's dimensional trade (0043):
2+1 is topological because there is nothing for the field equations to
leave undetermined, and that is an *arithmetic* fact about the
bivector operator, not an analytic one.

## 2. The vacuum Einstein equation is arithmetic too

With the Hodge star on bivectors (Euclidean, so ⋆² = 1 over Z_N):

```
[R, ⋆] = 0   ⟺   traceless Ricci = 0
```

verified **3000/3000** on random curvatures at N = 5, and pure-Weyl
curvatures commute with the star **300/300**. In block form the
curvature operator is

```
R = [ W⁺ + s/12      r̊      ]
    [    r̊ᵀ      W⁻ + s/12  ]
```

and Einstein is exactly the vanishing of the off-diagonal block.
So **"this curvature is Einstein" is sayable exactly inside the
quantized model** — a finite, decidable predicate on Z_N data rather
than a differential equation.

## 3. But the measure does not select it — the honest negative

The attractive hypothesis was that the ledger's simplicity price
(0055/0056) *is* the Einstein equation in disguise: charge for Ricci,
leave Weyl free, and vacuum falls out of the measure. **It does not.**

Lift the per-plaquette price (kernel codimension: 0 flat, 2 simple, 4
non-simple) to a curvature operator by summing over its six plaquette
columns, and test what it is a function of:

| test | result |
|---|---|
| same Weyl, Ricci changed → price changed | **220/300** |
| same Ricci, Weyl changed → price changed | **209/300** |

It factors through **neither**. And the Einstein sector is not the
cheap one:

| sector | mean price | fraction at the cheapest tier |
|---|---|---|
| pure Weyl (Ricci = 0) | 21.478 | 0.0087 |
| generic | 21.535 | **0.0002** |
| pure Ricci (Weyl = 0) | 21.216 | **0.0605** |

Both algebraically special sectors are far likelier to be cheap than
generic (44× and 300×), so the measure *does* prefer special
curvature — but it prefers **pure Ricci over pure Weyl**, the opposite
of vacuum selection.

> **The simplicity price is not the Einstein equation.** What imposes
> vacuum in this theory is the action's variation, not the measure's
> weight.

That kills a hypothesis the arc had been drifting toward since 0055,
and it is worth killing cleanly. 0057's mode selection (geometric vs
non-geometric) is a real gap structure; it is *not* Ricci vs Weyl.

## 4. Ambrose–Singer says why

**A smooth metric whose holonomy group is finite is flat** — the
holonomy algebra is spanned by the curvature (Ambrose–Singer). So a
literal Z_N-holonomy lattice does not describe a curved geometry at
all: it describes **piecewise-flat geometry with conical defects.**

| | Weyl dim | what a Z_N sector can carry |
|---|---|---|
| n = 3 | 0 | point defects — exactly Deser–Jackiw–'t Hooft, and 0054's deficit |
| n = 4 | 10 | **string** defects, and no Weyl to carry gravitons |

In 2+1 that is not a limitation, it is the whole theory: flat
everywhere off the sources, all content in the holonomy. 0054's
Wilson-loop deficit is the abelian sector doing exactly the job it can
do, and doing it exactly right.

In 3+1 it is a ceiling. The Weyl sector exists in the arithmetic (§1)
and **a Z_N gauge sector cannot carry it.** That is a structural
reason the abelian quantum arc reached Newton (0057, via a
*dispersion* model rather than genuine curvature) and keeps not
reaching polarizations — 0054's open 1, 0055's open 3, 0056's open 2,
0057's open 1 are all the same obstruction, now named.

**The 2+1 quantum success was never a warm-up for 3+1.** It was the
abelian sector's ceiling, reached. The next move is the one 0054
already wrote down: **quantize the nonabelian links.**

## Honest limits

- §1–3 work with **formal Riemann tensors over Z_N** — symmetric
  bivector operators with first Bianchi imposed **by hand**. They are
  not derived from lattice holonomies, so the tetrad and the
  torsion-free condition are *assumed*, not obtained. This sidesteps
  the objection that Ricci is a functional of (e, ω) rather than of
  the connection alone, at the cost of assuming what a real
  construction would have to produce.
- **Euclidean signature throughout.** The real 5+5 self-dual /
  anti-self-dual split is a Riemannian statement; in Lorentzian
  signature Weyl does not split over the reals — the 10 components are
  5 *complex* Newman–Penrose scalars. §2's ⋆² = +1 uses the Euclidean
  form. The Lorentzian version is not done here.
- N coprime to 6 is required for the Kulkarni–Nomizu inverses;
  measured at N = 5 and 7 only. Composite N (0053's divisor structure)
  is untouched.
- §3's lift — six columns of one operator ↔ six lattice plaquettes at
  a site — is a modelling choice. The repo's measure treats plaquettes
  as independent up to shared frames (0056 §3); that correlation is
  not folded in.
- §3's "fraction at the cheapest tier" is a tail statistic on 6000
  samples per sector; the means are within 1.5% of each other and
  should not be read as a signal on their own.
- §4 applies Ambrose–Singer to *smooth* metrics with finite holonomy.
  The lattice is not a smooth metric, so this is an argument about
  what the continuum limit can be, not a theorem about the lattice.
  It is nonetheless the right constraint to respect.

## Open

1. **Quantize the nonabelian links** — the single move that §4 says is
   required, and the common resolution of four standing opens
   (0054/1, 0055/3, 0056/2, 0057/1). The target is now sharp: produce
   a curvature operator whose Weyl block is nonzero, and count its
   propagating modes against 2.
2. **Lorentzian signature**: redo §2 with ⋆² = −1 and the complex
   SD/ASD split; the Einstein criterion should survive as a statement
   about the complexified operator.
3. If the price is not the Einstein equation (§3), what *does* the
   measure's geometric/non-geometric tier correspond to
   tensorially? It is not Ricci/Weyl; 0056's kernel codimension says
   it is "acts in a plane," which deserves its own decomposition.
4. Standing: the correlation gap (0058); the bond's h² (0060).
