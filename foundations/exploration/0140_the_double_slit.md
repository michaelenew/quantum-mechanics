# 0140 — The double slit, built from the derived measure

Code: `output/0128_the_double_slit.py`. North-star target 2.

Not a toy of quantum mechanics bolted on. Every object is computed
from this program's own weight, and the Hamiltonian is
**reconstructed**, not posited.

## 1. The derived Hamiltonian, and a finite Hilbert space

The chain was already proved, stone by stone, and had never been run
end to end: the weight W = A² has nonnegative character coefficients,
so the transfer operator (convolution by W, eigenvalue w_j/d_j) is
**positive**; a positive transfer operator is exp(−H) for real
self-adjoint H — the Osterwalder–Schrader reconstruction.

| n | w_n | w_n/d_n | E_n = −ln(w/d) |
|---|---|---|---|
| 1 | 6 | 6.000 | 0.0000 |
| 2 | 10 | 5.000 | 0.1823 |
| 4 | 14 | 3.500 | 0.5390 |
| 6 | 12 | 2.000 | 1.0986 |
| 8 | 6 | 0.750 | 2.0794 |
| 11 | 1 | 0.091 | 4.1897 |

And a consequence worth stating on its own: **w_n = 0 above the band,
so those modes have infinite energy.**

> **The reconstructed Hilbert space is finite dimensional — dim = 11
> for the N = 5 stack.** Not an approximation. It is 0108's band
> budget showing up as the dimension of the state space.

## 2. The fringe

Two localised states on the group manifold at θ = 1.05 and 2.05,
evolved to t = 2.6 by exp(−iHt) in the derived spectrum:

| | |
|---|---|
| visibility (max fractional difference, coherent vs incoherent) | **0.511** |
| sign alternations across the screen | **6 fringes** |
| code length, coherent | −0.51902 nats |
| code length, incoherent | −0.31737 nats |
| **gap** | **+0.20165 nats/event** |

**The control**, which makes it a measurement rather than a picture:
randomise the relative phase and average. Visibility falls **0.511 →
0.0163**. The fringe was the relative phase, not the envelope.

## 3. What it shows, and what it does not

**Shows:** this program's own weight, reconstructed through
Osterwalder–Schrader, produces a finite-dimensional Hilbert space
with a derived spectrum in which two alternatives interfere and beat
the incoherent model by 0.20 nats/event. Nothing posited — the
Hamiltonian came from the transfer operator, which came from the
weight, which came from counting.

**Does not show:** anything a sceptic should count as evidence *for*
the theory. The Born rule was **derived** here (0114/0119), so
recovering interference is the chain closing on itself — a
consistency check, not a discriminator. It cannot distinguish this
theory from standard quantum mechanics and is not meant to.

Its value is that it is **assembled**. The pieces were proved
separately across many stones and had never been run together. They
fit.

## 4. Note on the weight

0139 established that the coupling is not derived — the
multiplicities are a family, not a vector. That does **not** touch
this result: any nonnegative counting gives a positive transfer
operator and hence a Hilbert space, so the *structure* demonstrated
here is insensitive to which member of the family is right. What
would move is the spectrum's spacing, hence the fringe pitch — not
the existence of fringes.
