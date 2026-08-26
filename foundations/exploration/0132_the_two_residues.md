# 0132 — The two residues: the zeros cost 15%, and the exponent did not measure

Code: `output/0120_the_residual_trend.py`,
`output/0121_the_symanzik_exponent.py`. Sixth stone, taking the two
items 0131 left. One closed decisively; the other returned a
negative, including a false positive in my own verdict logic.

## 1. The residual trend belongs to the weight

0131 found the derived measure tracks SU(2) perturbation theory's
⟨1 − cos θ⟩ = 3/(4κ) to 15% at the derived point, with the relative
residual *growing* with κ. Three candidates were named: **(a)** the
weight's exact zeros, **(b)** the higher-order lattice series,
**(c)** the Gaussian bank prediction itself.

They separate by one control, because (c) is about the **lattice**
and (a)–(b) are about the **weight**. Three families at **matched
κ**, same lattice, same kernel, κ computed from each weight with no
Monte Carlo:

| κ | 3/(4κ) | Wilson | heat kernel | **Born (derived)** |
|---|---|---|---|---|
| **13.34** | 0.05622 | **1.0153** | **0.9843** | **0.8510** |
| 6.93 | 0.10823 | 1.0334 | 0.9724 | 0.9529 |
| 4.43 | 0.16930 | 1.0599 | 0.9576 | 0.9834 |
| 2.43 | 0.30864 | 1.1748 | 0.9390 | 1.0078 |

The informative comparison is at the **weak-coupling end**, where
3/(4κ) is supposed to hold. Deviation there: **Wilson 1.5%, heat
kernel 1.6%, Born 14.9%.**

- **(c) is dead**: the Gaussian bank prediction is good to ~1.5% for
  two different smooth weights at the same κ on the same lattice.
- **(b) is dead**: the heat kernel is smooth, strictly positive, and
  *not* Wilson — an entirely different higher-order series — and it
  agrees to 1.6%.
- **(a) survives alone.** What the Born weight has that neither
  reference has is **exact zeros**: it is band-limited and vanishes
  at θ = 2π/7 and beyond.

> **The derived weight's exact zeros cost 15% in ⟨1 − cos θ⟩ at the
> derived point.** Not a universality problem — lattice actions in
> one class may differ by O(1) in short-distance quantities at finite
> spacing — but a real, quantified signature of the derived measure.
> 0131's worry does not dissolve; it sharpens and gets a number.

A note on my own logic: the first version of this module compared
the families' *drift* across κ and concluded "all three drift the
same way, so it's (c)." The drift toward strong coupling is where
perturbation theory fails for every family and separates nothing.
The verdict was reversed once the comparison was made where the
theory applies.

## 2. The Symanzik exponent did not measure — and my test said it did

The plan: bound the extrapolation from r ≈ 5a to physical scales by
verifying the exponent in Symanzik's argument (rotational-breaking
operators are dimension six ⇒ effect O((a/s)²)). Seven kernel widths
at L = 20, residual = measured anisotropy minus its exact free-field
baseline.

| pair | widths | exponent |
|---|---|---|
| (4,0,0,0) vs (2,2,2,2) | 7 | **4.15** |
| (4,0,0,0) vs (3,2,1,1) | 6 | **−0.36** |
| (6,0,0,0) vs (3,3,3,3) | 5 | **4.98** |
| (6,0,0,0) vs (4,4,2,0) | 5 | **1.02** |

Mean 2.45; **spread −0.36 to 4.98**. Two pairs fall steeply, one is
flat, and one is *negative* because its residual **changes sign**
(+0.0082, +0.0030, +0.0005, −0.0014, −0.0044, −0.0070) — which no
power law describes.

> **The exponent is not measured.** The mean landing near 2 is
> arithmetic, not evidence — and the first version of this module
> tested `|mean − 2| < 0.8` and **passed on exactly that**. A test
> that ignores the spread is not a test.

Restricting to the clean window w ∈ [1.25, 2.0] — where the free
baseline is small and falling, before it grows again at w ≥ 2.5 as
kernel-plus-separation begins to span the box — does not help: 3.3,
7.4, 2.2, and the fourth still changes sign.

**Why it failed, nameably:** the usable window in w is bounded below
by statistics and above by the box, and on L = 20 those two leave
barely a factor 1.6 — no lever arm for a power law. **This wants
L = 32 or more.**

## 3. Where that leaves the bound

> The bound stands **where it was measured**: the interacting
> contribution to rotational-symmetry breaking is ≤ 1.4% at r = 4–6
> with a probe of width ~2. **It does not propagate.** The step to
> physical separations rests on Symanzik's theorem alone, with its
> premise unverified here.

That is weaker than 0131 hoped. The theorem is solid and standard;
what is missing is the check.

## 4. Front status

| | |
|---|---|
| the branch | decided, two volumes |
| the hierarchy | ξ/a ~ 10¹³, untuned — and this is *why gravity is weak* |
| Lorentz restoration | **≤1.4% at r ≈ 5a; does not propagate** |
| triviality | scoped; inherits the standard expectation |
| the residual trend | **closed — it is the exact zeros, 15%** |
| the exponent | **open — needs L ≥ 32** |
