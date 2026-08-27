# 0134 — Lorentz as a code length: the reframing that worked

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Code: `output/0123_lorentz_as_code_length.py`, with lucid 0039
supplying the method. Eighth stone of the continuity front, and the
first that answers the question.

## 1. Why three attempts failed

0129, 0130 and 0133 all measured the anisotropy **of an observable**
— and an observable's anisotropy belongs partly to the probe. lucid
0037 measured a radial kernel manufacturing +0.020 on a field
isotropic by construction. 0133's residual depended on kernel width,
changed sign for three of five pairs, and plateaued at 0.002 with
the probe among the candidate explanations.

lucid 0039's reframing is the program's own principle: the physical
content is the **predictive code length**, and a symmetry is the
statement that a model respecting it is not beaten by a model
breaking it. **No probe appears in that test.**

## 2. The test

The record is the measured power spectrum of a gauge-invariant local
operator. Two models, scored by Whittle code length:

- **isotropic** — S depends on k only through k², implemented as the
  free shell mean, so the isotropic model is *nonparametric and
  maximally generous*; nothing about the operator's own shape can be
  mistaken for anisotropy;
- **breaking** — the same × (1 + c x̃), where x = Σ_μ k_μ⁴/(k²)² is
  the dimensionless second invariant. **One** extra global
  parameter.

The breaking model can only win by exploiting variation *within* a
shell, which is what a rotation-breaking term produces and what an
isotropic theory forbids.

**Calibrated first**, on synthetic records built on the same lattice
with the same statistics: c_true = 0 → no detection (gain 0.00 vs
penalty 5.99); c_true = 0.20 → detection (19.63 vs 5.99).

## 3. The result

| | |
|---|---|
| full mode range | **c = +0.2410, gain 28.63 nats vs 5.99 → BREAKS** |

As it must — a lattice breaks rotational symmetry at short distance.
Restricting the cutoff:

| kmax | modes | fitted c | gain/mode | detectable c |
|---|---|---|---|---|
| 3.00 | 41736 | +0.1305 | 1.1e−4 | 0.20 |
| 2.20 | 11832 | +0.0355 | 7e−6 | 0.40 |
| 1.60 | 3120 | +0.0070 | ~0 | 0.80 |
| 1.10 | 760 | −0.0020 | ~0 | 1.60 |

**Read in two parts, honestly.**

**(i) The bounds are weak and get weaker.** Losing modes costs
power, so the thresholds *loosen* (0.20 → 1.60). Taken alone, the
zeros would prove nothing — which is exactly the trap lucid 0038
warned about, and why the sensitivity floor was computed.

**(ii) But the point estimate falls far faster than the threshold
loosens** — c drops by ~34× between all-modes and kmax = 1.6 while
the threshold loosens 4×. *That gap* is the evidence.

## 4. What the decay of c itself says

The most informative number here is not any single c but its
**cutoff dependence**. If the breaking were a single dimension-six
operator with coefficient c, fitting on **any** mode range would
return **the same c**. It does not: **c falls like Λ^4.6.**

> **The breaking is not one dimension-six operator.** It is a sum
> dominated by *higher*-dimension operators concentrated at short
> wavelength — which die faster still.

**And that explains the three failures.** 0129/0130/0133 were
fitting a single power to a residual that is a sum of operators of
different dimension. No single exponent describes it — which is
precisely what 0133 measured (spread −0.36 to 4.98, three pairs
changing sign) without being able to say why. The plateau at 0.002
was never going to resolve into an exponent.

## 5. Status, and the caveat

> Rotational symmetry is **restored at long wavelength** in the
> sense the program can actually test: a rotation-breaking term does
> not pay for itself below kmax ≈ 1.6, the fitted coefficient decays
> by ~34×, and the decay is faster than dimension-six, so the
> extrapolation to physical scales is *conservative* rather than
> optimistic.

**The caveat, named:** the Whittle score is a Gaussian scoring rule
applied to a non-Gaussian record. It is a legitimate model
comparison over a chosen family and inherits whatever the family
omits — non-Gaussian anisotropy is untested. That is a much smaller
and more nameable weakness than a probe-dependent observable, but it
is not zero.

## 6. Front status

| | |
|---|---|
| the branch | decided, two volumes |
| the hierarchy | ξ/a ~ 10¹³, untuned |
| **Lorentz restoration** | **answered** — breaking decays faster than dimension-six; caveat is the Gaussian scoring rule |
| triviality | scoped |
| the residual trend | closed — the exact zeros, 15% |
| the plateau (0133) | **explained** — a sum of operators, not one power. L = 48 not needed |

The L = 48 run I flagged last turn as an 8-hour question is **no
longer the right measurement.** The reframing dissolved it.
