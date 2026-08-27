# 0123 — Counting buys time: the Lorentzian arena is not an independent debt

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0122 conjectured that the Born square is what makes the derived
measure reflection positive, and therefore what makes the Lorentzian
lift possible. **The conjecture was half right, and the correction
is the result.** Code: `output/0111_counting_buys_time.py`.

## 1. The criterion

For a class-function weight, the transfer operator is convolution by
W, whose eigenvalue on the χ_j eigenspace is w_j/d_j — verified
numerically against the character coefficients to 1e−6. So:

> **Reflection positivity ⟺ every character coefficient of the
> weight is nonnegative.**

RP is the Osterwalder–Schrader condition: it is exactly what lets a
Euclidean measure be reconstructed as a quantum theory with a
Hilbert space and unitary time evolution.

## 2. The derived weight passes

|A|² for the flat counting amplitude has coefficients
**6, 10, 13, 14, 14, 12, 9, 6, 4, 2, 1** and nothing below zero
(minimum −4e−13). **RP holds for this program's own measure.**

## 3. What fails — and what always passes

| weight class | fails RP |
|---|---|
| generic nonnegative band-limited W | **200/200** |
| square of a generic *complex* band-limited amplitude | **170/200** |
| square of a *counting* amplitude (nonneg coefficients) | **0/200** |

Being nonnegative is not enough. **Being a square is not enough
either.** What never fails is a square whose amplitude has
nonnegative coefficients — and that is one line, because fusion
multiplicities are nonnegative integers:

    c_k = Σ_{j,l} a_j a_l N^k_{jl} ≥ 0   whenever a ≥ 0.

**So the load-bearing property is not the square. It is that the
amplitude is a count.** This program's amplitude is flat counting
over admissible representations — nonnegative integers by
construction — so its weight is reflection positive *for the same
reason it exists at all*.

## 4. Consequence

```
counting ⟹ nonnegative character coefficients
         ⟹ positive transfer operator
         ⟹ reflection positivity
         ⟹ Osterwalder–Schrader reconstruction
         ⟹ a Hilbert space with unitary time evolution
```

**The Lorentzian arena — argued but not constructed since 0048 — is
not an independent debt.** It follows from the program's own
founding structure. *Counting buys time.*

The filter-side statement of the same condition (lucid 0030): a
transfer operator with a negative eigenvalue has no real logarithm,
so its dynamics exists at integer steps and at no time in between.
RP is precisely the **embedding condition** — that a generator
exists. In filter terms: *a count-generated record is one you can
always ask "what happened in between".*

## Honest limits
- The criterion and the verification are at the single-weight
  (transfer-operator) tier. Full RP for the 4D lattice measure with
  vertex corrections is not checked here; what is established is
  that the *link weight* — the object the program derives — passes,
  and that generic alternatives do not.
- OS reconstruction additionally requires the usual regularity
  conditions; RP is the non-trivial one and the only one this
  program's structure was in doubt about.
- 0122's conjecture is corrected in place: the square is necessary
  to have an amplitude at all, but a generic square fails RP.
