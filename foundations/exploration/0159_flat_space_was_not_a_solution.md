# 0159 — Flat space was never a solution, and γ = −1 was an artifact of that

> **AI-generated, not peer-reviewed.** Code:
> `output/0148_the_counterterm.py`, `output/0149_the_graviton_mass.py`.
> Corrects 0146/0156 again, and further than 0158 did.

I set out to test the constrained (double-copy) sector that 0158
identified. Re-deriving the setup first turned up something more
basic, and it changes the answer without needing that test.

## The omission

**A Hessian is only parametrisation-independent at a stationary
point.** 0146 expanded the induced action around W = I and never
checked whether that is one. It is not:

    Γ⁽¹⁾[A] = tr(BA),  and for uniform A = εI this is rank(B)·ε

Measured at L = 4: **tr(B) = 1020.0000 = 4(V−1)** exactly. That is the
**induced cosmological constant**, of order the cutoff, and it was
left in. So 0146's Hessian is a second derivative at a
*non-stationary* point — which is not the graviton kinetic operator,
and is not even parametrisation-independent.

The tell was visible and I missed it: in the **linear** variable W the
same Γ is *concave* (ln det is concave, ln Z convex), while in the
**exponential** variable A it came out convex. A sign that flips with
the choice of variable is not a physical sign.

## The fix, which is forced rather than tuned

Add the bare cosmological term and fix its coefficient by demanding
flat space be stationary. With `√g = det(W)^{1/2} = exp(tr A)`:

    S_ct = c Σ_x exp(tr A(x)),   c = −L,  L = 4β₀ = (V−1)/V

measured as 0.99995177 against the closed form 0.99995177. Its
second-order part, `c(tr A)²/2` per site, is **negative in the trace
direction** — the conformal mode.

## What that does to the spectrum

| k | without counterterm | with counterterm |
|---|---|---|
| (0,1,0,0) | 0 negative | **1 negative** |
| (0,2,0,0) | 0 negative | **1 negative** |
| (0,1,1,0) | 0 negative | **1 negative** |
| (0,2,1,1) | 0 negative | **1 negative** |
| (0,3,0,0) | 0 negative | **1 negative** |

**Exactly one negative mode at every momentum** — the Einstein-Hilbert
signature (nine positive, one negative), not an arbitrary
indefiniteness. The PSD obstruction of 0146/0156 was an artifact of
the expansion point.

## What it does to γ

| k | γ (no ct) | γ (with ct) |
|---|---|---|
| (0,1,0,0) | −0.86556 | **+0.51133** |
| (0,2,0,0) | −0.62164 | +0.50798 |
| (0,1,1,0) | −0.76944 | +0.51194 |
| (0,2,1,1) | −0.52934 | +0.51316 |
| (0,3,0,0) | −0.43233 | +0.49881 |

> **γ = +0.50864 ± 0.00521.** Light deflection (1+γ)/2 = **0.754 × GR**.

Those are not arbitrary numbers. **van Dam-Veltman-Zakharov**: a
*massive* graviton gives **γ = 1/2** and deflection **3/4** of GR,
discontinuously, however small the mass.

And the program said so already. **0056**: *"the lattice graviton is
massive off criticality, so the long-range Newtonian limit is a
critical point."* Two independent routes, same conclusion.

## Measuring the mass

Fit `H(k) = H₀ + k̂²H₂ + k̂⁴H₄` element-wise. **‖H₀‖/‖H₂‖ ≈ 21.6**,
direction-independent to 2.7e−3 — there is a real non-derivative
piece, i.e. a graviton mass term. A lattice is free to induce one: it
breaks diffeomorphism invariance, which is exactly what would have
forbidden it.

**Isolating the massless kinetic operator is beyond this volume**, and
that is stated rather than papered over:

- subtracting H₀ is a catastrophic cancellation (‖H₀‖ ≈ 80‖H₂‖ at the
  available momenta) and gave γ = **0.25 ± 1.56** — a spread larger
  than the answer, so not a measurement;
- fitting the slope avoids the cancellation but the result is
  direction-dependent — 0.134, 0.192, 0.171, 0.428 — giving
  γ = **0.231 ± 0.115**. The gate passes exactly (the same procedure
  on a pure Einstein-Hilbert kernel returns **+1.000000**), so the
  method is right and the lattice's broken rotational invariance at
  k̂² ≳ 0.27 is the limit.

## The sequence — the actual answer to "what is the difference"

| construction | γ | reading |
|---|---|---|
| induced action, no counterterms | **−1** | Nordström, zero bending |
| + zero cosmological constant *(forced)* | **+0.509** | vDVZ, massive graviton, 3/4 GR |
| + massless limit | *unresolved at this volume* | 0056's criticality condition |
| **classical tier** (0037) | **+1** | Einstein, 0.008046 vs 0.008000 |

**The difference is diffeomorphism invariance.** The classical tier
builds it in: the metric is the square of a null Maxwell channel
(Kerr-Schild double copy) and the action is Palatini/BF with the
simplicity constraint. A lattice does not have it, so it induces both
a cosmological constant and a graviton mass. Cancelling the first is
**forced** — flat space must be a solution or there is no graviton to
discuss — and it moves γ from −1 to the vDVZ value. The second is
0056's criticality condition.

## Status, stated plainly

0156 said the program fails the classical tests. That was wrong twice:
wrong sector (0158) and wrong expansion point (this stone). The
current honest position is **not** a pass either — γ = 0.509 is
excluded by Cassini as it stands. It is: **the induced route sits at
the vDVZ value, and the gap to Einstein is a graviton mass the program
had already identified as an off-criticality effect.**

The next test is the one 0158 named and this stone deferred: the
constrained double-copy sector, where diffeomorphism invariance is
built in rather than tuned back.
