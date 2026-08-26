# 0158 — The difference is one sign, and 0156 named it as narrow when it is the wide one

> **AI-generated, not peer-reviewed.** Code: `output/0147_the_missing_sign.py`.
> Corrects the verdict scope in 0156/0157.

Same program, opposite answers:

| tier | measurement | result |
|---|---|---|
| **classical** (0037) | light bending at b = 1 | **0.008046** vs GR 4M/b = 0.008000 — *twice Newton* |
| **quantum** (0146) | γ from the induced action | **−1.07** — zero bending |

This isolates why.

## s0 — The gate I should have run first

Feed a genuine linearised Einstein-Hilbert kernel (de Donder gauge,
`Q(h) = (k²/2)[tr(h²) − ½(tr h)²]`) through the **same solver, same
source, same γ convention**:

| k² | h_00 | h_spatial | γ |
|---|---|---|---|
| 0.50 | −0.500000 | +0.500000 | **+1.000000** |
| 1.00 | −0.250000 | +0.250000 | **+1.000000** |
| 4.00 | −0.062500 | +0.062500 | **+1.000000** |

**Exactly +1.** The pipeline is correct: given Einstein, it returns
Einstein. So 0146's −1 is a property of the *kernel it was given*, not
of the machinery — and note where the +1 comes from: **h_00 and
h_spatial have opposite signs.**

## s1 — The two spectra

Eigenvalues on the 10-dimensional space of symmetric h:

| kernel | spectrum | negative modes |
|---|---|---|
| Einstein-Hilbert | [−2, 2,2,2, 4,4,4,4,4,4] | **1** |
| induced, k=(0,1,0,0) | — | **0** (min +6.19e+02) |
| induced, k=(0,2,0,0) | — | **0** (min +2.07e+03) |
| induced, k=(0,1,1,0) | — | **0** (min +1.10e+03) |
| induced, k=(0,2,1,1) | — | **0** (min +2.67e+03) |

EH is an involution up to scale — nine +1 and one **−1**, and the −1
*is* the conformal mode. The induced kernel has none, at any momentum,
and 0146 proved that is identical: `Γ″[A] = ‖(1−B)AB‖²_F ≥ 0`.

## s2 — The difference, in one line

Since γ = −h_s/h_00:

> **γ > 0 ⟺ the spatial and temporal metric responses have opposite
> signs.**

In Einstein-Hilbert the trace term `−½(tr h)²` flips the trace mode,
and that flip is exactly what returns the spatial response with the
opposite sign to the temporal one. Remove it and a source pushes every
component the same way — a conformal response, γ = −1, no bending.

> **The entire difference is one sign: the sign of the conformal
> mode.** A positive-semidefinite action cannot have it, and a matter
> determinant is positive semidefinite identically.

## s3 — Where the classical tier gets that sign

It never builds the metric by inverting a Hessian. From 0045 and 0050:

- the channel is a **Maxwell field** `A_μ = w k_μ` — exactly
  Liénard-Wiechert, agreeing to 1e−8;
- **the metric is its square**, `g = η + w k⊗k` — the **Kerr-Schild
  double copy**, with k *null*;
- the action is Palatini/BF with the **simplicity constraint
  B = e∧e**, and 0050 counted what that does: free BF has **0**
  physical degrees of freedom; imposing simplicity gives **2**. The
  constraint is what releases the gravitons.

**0146 has neither.** It varies a symmetric metric *freely* over all
ten components — the unconstrained sector, the one 0050 says carries
zero gravitons — and reads a determinant's response.

And the quantum tier **does** have the missing structure. 0142's
graviton is traceless-sym(B⁺⊗B⁻): a double copy, pure synergy, 5 of 9,
residual spread 1.0000 given either stream alone and 0.0000 given
both. lucid 0045 measured |B⁺| = |B⁻| machine-exact for a simple
bivector — **which is the simplicity constraint B = e∧e on the
lattice, already verified.**

## The correction to 0156

The quantum theory has **two objects that both get called the
metric**:

1. **The background weight** `W = √g g^{μν}` that matter couples to.
   Its induced action is PSD ⟹ γ = −1. **This is what items 3, 4 and
   6 measured.**
2. **The composite double copy** B⁺⊗B⁻ — the program's actual
   graviton, and the quantum image of the classical Kerr-Schild
   square. **This is what item 2 tried to measure and could not, for a
   scale reason (ξ/a ~ 10²⁰), not a structural one.**

**The classical tier's GR lives in (2). 0146 measured (1).**

0156 listed "the metric identification" as escape 1 and called all
three escapes narrow. **That was wrong: escape 1 is the wide one.**
The falsification stands for the *induced* route and does not touch
the double-copy route — which is the route the classical tier actually
uses to pass the classical tests.

Item 6 is therefore not a verdict on the program. It is a verdict on
one of its two gravitational sectors, and on the one the classical
tier does not use.

## The concrete next test

Not "rescue γ". Build the quadratic form of the **constrained**
sector — B⁺⊗B⁻ with |B⁺| = |B⁻| imposed — and count its negative
modes. GR needs **exactly one**. The induced sector has zero. If the
constrained sector has one, the two tiers agree and item 6 reopens as
a pass; if it also has zero, the failure is real and general.

That is a well-posed lattice calculation, and it is now the sharpest
open question in the program.
