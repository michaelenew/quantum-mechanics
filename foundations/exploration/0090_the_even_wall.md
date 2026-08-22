# 0090 — The even wall: frames are indivisible, and the cover cures

Eleventh stone, the sign-problem toy packaged (0069's queue item) —
and it repackaged itself into something better than a boundary
marker. 0074 found the ledger is a Born square, gcd(F,N) =
|Σ_e ω^{e²F}|²/N, *for odd N only*, and filed even N as "the N = 2
degeneracy family at the root." This stone settles what kind of wall
even N is, and finds its door. Code: `output/0081_the_even_wall.py`.

---

## 1. The wall, exhaustively

A *counting amplitude* is A(F) = Σ_e c_e ω^{eF} with c_e nonnegative
integers — frame multiplicities. |A|² = N·gcd demands the
autocorrelation c⋆c = Ŵ (the integer dual ledger). Exhaustive search
over all counting vectors:

> **N = 2, 4, 6, 8, 10: no integer solution exists.** (Odd N: the
> quadratic count c_e = #{x : x² = e} works, re-verified at
> 3, 5, 7, 9, 15.)

## 2. It is not a positivity wall — it is quantization itself

Real *nonnegative* solutions exist at every even N up to 16
(constructed exactly via the PSD square root of the autocorrelation
spectrum; all entries positive). At N = 2 the entire failure is one
equation:

```
2 c₀ c₁ = 1        — the ledger would need half a frame.
```

So the even wall is **integrality**: the obstruction is not sign,
not positivity, but the indivisibility of frames. The thing that
rejects even levels is the same thing the program is made of —
counting comes in wholes. (A pleasing inversion: the sign problem's
cure was the Born square; the Born square's own boundary is
quantization.)

## 3. The cure is the double cover

Double the frames on the 2-part of N (odd part untouched):

```
A(F) = [Σ_{x ∈ Z_{2·2^a}} ω_{2^{a+1}}^{x²(F mod 2^a)}] × [odd Gauss at F mod m]

⟹   |A|² = 4·N·gcd(F, N)     exactly, at every flux
```

verified for N = 2, 4, 8, 16 (pure 2-powers) and 6, 10, 12, 24
(mixed, CRT with reduced arguments). The factor 4 is the cover
degree squared. **Frames come back whole upstairs.**

## 4. The reading: even levels are spin levels

Even N admits no frame counting on Z_N and a perfect one on its
double cover — which is the arithmetic shadow of a **spin
structure**, sitting beside the Lorentzian congruence (0081/0072:
mod 4, i, Frobenius-as-conjugation) as the *second* place this
program's arithmetic independently discovers spin. The two shadows
even compose: the Lorentzian split wants −1 to be a square (a
quarter-turn to exist); the even ledger wants frames to halve their
phase step (a half-turn of the phase lattice). Both are the
arithmetic cost of orientation-entanglement.

Constraint-stack consequence, recorded precisely: the Born
constraint "N odd" **softens from an exclusion to a covering
instruction** — even levels are not broken, they are spin-covered,
at the price of the 4× normalization. The stack's smallest
admissible level stays **N = 5**, because the Lorentzian congruence
(every prime factor ≡ 1 mod 4) rejects even N independently and does
not soften.

## Honest limits

- Exhaustive nonexistence is for N ≤ 10; the pattern is clean but
  even N ≥ 12 undoubled is unproven (finite search grows fast; a
  parity proof — the F-odd dual coefficients of Ŵ force an odd
  off-diagonal autocorrelation entry, impossible for integer c —
  is visible at N = 2 and plausibly general, not written down).
- "Spin structure" is a structural identification (double cover
  curing a counting obstruction), not a construction of spinors on
  the lattice.
- The 4× normalization changes the weight's overall constant only;
  nothing downstream (which used odd N throughout) shifts.

## Open

1. The parity proof of nonexistence for all even N (small, clean
   target).
2. Do the two spin shadows meet? The doubled-frame ledger at
   N ≡ 1 (mod 4) composed with the Lorentzian i — is there a single
   arithmetic structure (Z_{4N}? Gaussian integers mod N?) carrying
   both.
3. Whether the covered even ledger changes any RG statement (0071's
   N ≥ 3 bound was derived for the odd family; the covered family's
   f-value differs by the 4× and the doubled support).
