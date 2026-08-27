# 0118 — Why band-limited: the level is what a finite record can pay for

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0117 restated the Born question as "why is the weight band-limited
in the character basis?". The answer is in this program's own
currency — but not where I first looked. Code:
`output/0108_the_resolvable_level.py`.

## 1. One read barely sees the sector

Sector j is read through p(θ|j) ∝ |χ_j|²sin²θ. Adjacent sectors
(j = 0, ½) have Bhattacharyya overlap **0.849**, and a single
class-angle read carries only:

| resolution σ | nats/read about the sector |
|---|---|
| 0.00 (perfect) | 0.244 |
| 0.10 | 0.140 |
| **0.31** (the dressed vacuum's own √⟨θ²⟩) | **0.034** |
| 0.60 | 0.007 |

**My first pass expected the cutoff to come from resolution; it
does not.** Even perfect reads are weak, because the sector laws
genuinely overlap. The correction is the result — and it is the
same fact this program measured from the data side as *"sector
identity is a slow observable"* (lucid 0003) and as a fixed ~8% of
the ceiling per read (lucid 0015). Three independent routes to one
statement.

## 2. So the cutoff is a budget, not a resolution

Supporting N sectors costs ln N nats of sector information, which at
i nats per read takes ln(N)/i reads. At the program's own vacuum
resolution:

```
   N = 2      0.693 nats     20 reads
   N = 5      1.609 nats     47 reads
   N = 13     2.565 nats     75 reads
```

Supporting the derived level **N = 5 costs ~47 reads**. Independently,
0106 computed **n\* = 58 samples** to pin the level prequentially —
two unrelated calculations of what a level costs, agreeing **within
a factor of 1.2**.

## 3. The statement, and its limit

**Band-limiting is forced**: a filter cannot carry sectors it has
not paid for, so the representable weight has finite character
support — and the Born square is exactly the weight that implements
that truncation (0117). The chain

> *why squared* → *why band-limited* → *because sector information
> is bought by the read, at a measured price*

now terminates **inside** the theory.

**Not shown**: that the affordable count equals the *admissible*
level of 0081 (x² ≡ −1 mod N, plus the even wall). An arithmetic
constraint and a budget constraint are different arguments; that
they agree on a small integer (~47 reads for N = 5 against 58 to
pin it) is *measured, not derived*. That agreement is now the sharp
remaining target — and a far better one than "why squared".
