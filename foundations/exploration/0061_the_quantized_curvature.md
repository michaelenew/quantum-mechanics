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

> **Audited by 0062 — verification upgraded to exact.** The
> 3000-sample check above contained *zero positive cases* (a random
> curvature is essentially never Einstein), so as shipped it tested
> only the generic direction. 0062 proves the equivalence exactly:
> the linear maps M ↦ [M, ⋆] and M ↦ traceless Ricci(M) have
> identical kernels on the 20-dimensional Riemann space (rank 9 =
> rank 9 = stacked rank 9, at N = 5 and 7). One wording sharpened:
> [R, ⋆] = 0 is **Einstein-with-Λ** — the witness Weyl + λ·Id
> commutes with ⋆ while Ricci = (s/4)δ ≠ 0 — and *vacuum* is the
> pair [R, ⋆] = 0 ∧ s = 0, equally arithmetic (its kernel equals the
> full Ricci map's kernel, rank 10).

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

### What the price actually is, and why it cannot be Einstein

The weight comes from integrating the frame out of the action's
ε·B·F term, with B = e∧e built from two frame vectors:

```
K(F) = Σ_{a,b ∈ Z_N⁴} ω^{ ε_IJKL a^I b^J F^KL }
```

This is a sum of **phases**, and the mechanism matters. The exponent is
linear in a, so the a-sum is a character sum: it returns N⁴ when the
vector m^I = ε_IJKL b^J F^KL vanishes and **exactly zero otherwise**.
The whole sum collapses to

```
K(F) = N⁴ × #{ b : the curvature annihilates b }
```

which is 0056's kernel count, now with its derivation. Measured at
N = 3: 6561 / 729 / 81 for flat / simple / non-simple, matching
N⁴|ker F| exactly.

**A tempting misreading, checked and rejected**: K is *not* the number
of frame pairs whose pairing with F vanishes. That count is 2673 for a
simple curvature where K = 729 — the other 1944 pairs carry nonzero
phases that cancel among themselves. The price is interference, not
tallying.

So the tiers have a concrete geometric meaning: a curvature 2-form
rotates the frame, and the price counts **how many independent planes
it rotates in.** Flat turns none and is free; simple turns one plane
and leaves a whole plane fixed; non-simple turns two planes at once
and leaves nothing.

Two reasons this cannot coincide with Einstein:

1. **Different objects.** The price interrogates a *single bivector*
   (6 numbers, one plaquette) and asks its rank. Einstein interrogates
   the *operator* R: Λ² → Λ² (20 numbers) and asks whether it commutes
   with ⋆. Both involve the Hodge star — the simplicity invariant is
   ⟨⋆F, F⟩, the Einstein condition is [R, ⋆] = 0 — but one is a
   quadratic form on a vector and the other a commutator of operators.
2. **A measure is not an equation of motion.** Integrating out the
   frame produces a *weight* summing over every frame, including all
   the non-stationary ones. The Einstein equation comes from *varying*,
   which selects stationary points. Asking whether the measure's cheap
   configurations are the equation's solutions asks whether a
   distribution's peak coincides with a variational solution set.
   There was never a reason it must.

That kills a hypothesis the arc had been drifting toward since 0055,
and it is worth killing cleanly. 0057's mode selection (geometric vs
non-geometric) is a real gap structure; it is *not* Ricci vs Weyl.

## 4. Ambrose–Singer says why

**A smooth metric whose holonomy group is finite is flat** — the
holonomy algebra is spanned by the curvature (Ambrose–Singer). So a
literal Z_N-holonomy lattice does not describe a curved geometry at
all: it describes **piecewise-flat geometry with conical defects.**

| | Weyl dim | what a finite-holonomy sector can carry |
|---|---|---|
| n = 3 | 0 | point defects — exactly Deser–Jackiw–'t Hooft, and 0054's deficit |
| n = 4 | 10 | **string** defects — but not the radiation field around them |

In 2+1 that is not a limitation, it is the whole theory: flat
everywhere off the sources, all content in the holonomy. 0054's
Wilson-loop deficit is the abelian sector doing exactly the job it can
do, and doing it exactly right.

In 3+1 it is a ceiling. The Weyl sector exists in the arithmetic (§1)
and a finite-holonomy sector cannot carry it. That is a structural
reason the abelian quantum arc reached Newton (0057, via a
*dispersion* model rather than genuine curvature) and keeps not
reaching polarizations — 0054's open 1, 0055's open 3, 0056's open 2,
0057's open 1 are all the same obstruction, now named.

### Three corrections to how this was first stated

**(a) Strings radiate — this repo measured it.** An earlier phrasing
said 3+1 creases give "no Weyl to carry gravitons," which read as
*cosmic strings cannot emit gravitational waves.* That is false, and
0050 refutes it directly (`output/0045`'s `loop_power`; 0049 built
the loop and left decay power as its open — citation fixed by 0062):
an oscillating Kibble–Turok loop radiates with
**Γ = P/(Gμ²) = 45.8**, against GR's 40–100 for that family. A
*straight, static* string is flat outside itself and radiates nothing;
an *oscillating* one radiates strongly. The correct statement is
narrower and more interesting: **the finite sector can hold the defect
but not the radiation field.** The geometry around a static string
really is flat, so Z_N represents it exactly; the wave the loop emits
carries genuine curvature spread through space, which finite holonomy
cannot represent.

**(b) Quantum does not mean finite.** Quantization discretizes
*spectra*, not the symmetry group — the rotation group is continuous
while angular momentum eigenvalues are discrete. Lattice QCD keeps
SU(3); loop quantum gravity keeps SU(2) and gets discrete areas and
volumes from *representation labels*, not from a finite group. **Z_N
was a tractability choice, not a consequence of quantization** — it is
what made 0053–0057 exactly enumerable. It bought exactness and cost
generality.

**(c) "Nonabelian" is the wrong word for the fix.** A finite
*nonabelian* group is still finite and Ambrose–Singer still forces
flatness, so going nonabelian-but-finite buys nothing. And abelian
does not imply no waves: Lorentzian pp-waves have abelian holonomy
(generated by null rotations) while being Ricci-flat and genuinely
curved. The operative property is **continuity**, not
non-commutativity. The classical lattice (0047) already uses
continuous SO(3,1) links; only the quantum sector shrank to Z_N.

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

1. **What the price is, tensorially** — the sharpest conceptual open
   in the quantum arc, and the reason §3's negative is a question
   rather than a dead end. The tariff sorts curvature by **rank**
   (0 / 2 / 4), which is a statement about a bivector, not about a
   metric's curvature tensor. Sub-questions:
   - What is the rank grading's meaning on a full lattice geometry,
     as opposed to one plaquette?
   - Both the tariff and Einstein are built on ⋆ — ⟨⋆F, F⟩ and
     [R, ⋆] = 0. Is there one structure they are both shadows of?
   - **The ratio is exactly 2 at every level N — resolved by 0062.**
     The price is **rank(F) · log N**: the kernel map is the
     alternating matrix ⋆F, alternating forms have even rank in every
     characteristic, so the tiers 0/2/4 are the even ranks of a 4×4
     alternating form and the ratio 2 is the parity theorem. Verified
     exhaustively at N = 3, 5, 7 (every configuration).
   - Is there a *different* observable in the measure — a correlation
     function, a saddle point — that does encode the field equation
     even though the pointwise weight does not?
2. **Lift the quantum sector to a continuous twist group** — the move
   §4 actually requires (continuity, not non-commutativity), and the
   common resolution of four standing opens (0054/1, 0055/3, 0056/2,
   0057/1). The classical lattice already carries SO(3,1) links. The
   target is sharp: produce a curvature operator whose Weyl block is
   nonzero, and count its propagating modes against 2.
3. **Lorentzian signature**: redo §2 with ⋆² = −1 and the complex
   SD/ASD split; the Einstein criterion should survive as a statement
   about the complexified operator.
4. Standing: the correlation gap (0058); the bond's h² (0060).
