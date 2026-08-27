# 0117 — Linear agreement, the mode count, and what the Born square buys

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Three standing obstructions, each moved. Code:
`output/0107_the_square_and_the_modes.py`.

## 1. The scalar/tensor factor is a strong-field difference

The completion's transmission is ψ = 1 − GM/r **exactly**; GR's
lapse is N = √(1 − 2GM/r). Their difference is second order:
(ψ − N)/x² → **0.5005, 0.5051** at x = GM/r = 0.001, 0.01 — the two
agree at *first order*, same Newtonian potential and same redshift.
So the "named factor 2" (horizons at GM vs 2GM) is not a
discrepancy in the regime where the correspondence was built; it is
a statement about how the two theories continue into strong field.
The residue is sharper than it was: **the scalar completion is GR
to first order and differs only in its nonlinear continuation.**

## 2. The mode count reaches 2, with every ingredient named

```
   local frame components e_i^a              9
   local frame rotation (0026, exact)       −3   [frame ↔ metric redundancy]
   ⇒ symmetric precision/metric field        6
   node relabelling (no preferred names)    −3   [the diffeomorphism analogue]
   Gauss law (0109: boundary = enclosed)    −1   [constraint]
   propagating                               2
```

Every ingredient is an object this program already owns, and the
count lands on GR's 2. **Reconciling with 0026**: that stone
quotiented a *single* node's precision by local rotation and was
left with its eigenvalues — the frame↔metric redundancy. In the
field theory that quotient is spent identifying P with the metric
and must not be subtracted twice. (My earlier sketch made exactly
that double-count and produced −1; the correction is recorded
because the arithmetic was the check.) This is a **counting**
argument: the tensor field equations remain underived, and the
count has to survive them.

## 3. What the Born square buys: band limiting

In the character basis, |A|² (J = 2.5) has coefficients
**6, 10, 13, 14, 14, 12, 9, 6, 4, 2, 1** — nonnegative integers
(fusion counts) — and **exactly zero above 2J** (max |coefficient|
8e−16). A heat kernel, which is all record noise can make (0027),
has coefficients e^{−τj(j+1)}: positive at *every* j, never zero
(9.5e−6 at j = 8).

**The real-space nodes are the dual-space cutoff.** The Born square
is what implements the level cutoff — and the standing question
*"why squared?"* becomes *"why band-limited?"*, which is a question
in this program's own currency (the level N, priced at 58 samples
in 0106). The deepest obstruction is not dissolved, but it is
restated inside the theory instead of outside it.

## 4. A consistency check on induced gravity

The induced-gravity identification (0115) fixed ℓ_P = 2.27 a from
the measured area-law coefficient. Independently, the information
and geometry mass bounds cross at √3 = 1.73 a — a number containing
no α at all. **Two Planck-scale estimates from unrelated inputs
agree to 31%.** That is evidence for the identification, not proof;
a factor that could have been astronomically wrong is not. Recorded
as such.

## Open
1. The tensor field equations themselves (the count must survive).
2. "Why band-limited" — the restated form of the Born question.
3. An independent determination of G, which would turn §4 from
   consistency into a test.
