# 0170 — The null space: one integer in, everything else out

> **AI-generated, not peer-reviewed.** Code: `output/0160_where_it_sits.py`.
> Prior art credited in [`ATTRIBUTION.md`](../ATTRIBUTION.md).
>
> **Prior art.** The methodology — characterise the admissible region
> rather than enumerate models — is that of generalized probabilistic
> theories (Barrett; Hardy 2001; Chiribella, D'Ariano & Perinotti
> 2011), the conformal and S-matrix bootstrap, positivity bounds
> (Adams et al. 2006) and the swampland programme (Vafa 2005). The
> selection argument at the end is Weinberg's (1987).

Not "what other theories exist", but the answerable version: **given
everything this program forces, what is left free, and what shape is
the residual?**

The chain is level N → band B = 2N+1 → M = N+1 characters → flat
multiplicities (forced by capacity) → the double copy (measured) → κ.
Everything is forced **except N**.

## The ladder

0081's admissibility condition — N odd with x² ≡ −1 (mod N) — gives

    1, 5, 13, 17, 25, 29, 37, 41, 53, 61, 65, ...

and the classical characterisation holds on every odd N to 120:
**solvable exactly when every prime factor of N is 1 mod 4.** The
level is not free. It is confined to a discrete arithmetic ladder.

## κ along it

    κ = (2/3) Σ n²(n²−1) / Σ n²  =  (2/5)(M+2)(M−1)  =  (2/5) N(N+3)

Gated at N = 5: exact 16.000000, closed form 16.000000, measured
16.0001 (0141).

| N | M | κ |
|---|---|---|
| 1 | 2 | 1.600 |
| **5** | **6** | **16.000** |
| 13 | 14 | 83.200 |
| 17 | 18 | 136.000 |

**κ is derived given N. It is not derived.**

## The hierarchy along it

Using 0155's matched ratio β/κ = 1.1023 (measured at N = 5, assumed
to carry — flagged, not established):

| N | β_W | ξ/a |
|---|---|---|
| 1 | 1.764 | 10^1.6 |
| **5** | **17.637** | **10^19.8** |
| 13 | 91.712 | 10^106.1 |
| 17 | 149.915 | 10^174.0 |

> **Adjacent rungs differ by 86 orders of magnitude.**

## The flip side, which is the interesting half

The hierarchy has to land near 10¹⁹–10²⁰. The ladder offers 10^1.6,
10^19.8, 10^106. **Only one rung is physical**, and the spacing is so
violent that the selection is unambiguous.

Whether that is a derivation or a one-bit fit is exactly the question
— and it is the same epistemic move as **Weinberg's anthropic bound
on Λ**: a constraint plus an observation, selecting a value nothing
derives. Weinberg's got the number right *before* it was measured and
remains the least-loved successful prediction in physics.

## Verdict

**Not a line** — the arithmetic condition kills the continuum.
**Not a point** — nothing selects a rung, and 0127 says so in its own
words: the level is "the world's data, not the law's", and "No knob
has been derived." 0120 found the one argument that looked like it
selected N = 5 to be a coincidence at a single point, the ratio
drifting 7.2× across the ladder.

**It is an archipelago with one habitable island.**

So the honest form of the headline claim is not "a derived coupling".
It is:

> **One integer in, everything else out.**

Better than it sounds, and weaker than "derived". Better, because the
Standard Model takes nineteen real numbers and this takes one integer
from a constrained ladder. Weaker, because a free integer that swings
the answer by 86 orders is not a prediction, and 0069's conversion bar
asked for a derived knob.

**And it names the one computation worth more than all the others: a
reason for the rung.** Not a better lattice run.
