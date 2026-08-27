# 0133 — The exponent fails, the criterion holds, and the residual has a plateau

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Code: `output/0122_the_exponent_at_L32.py`, with lucid 0038 supplying
the method. Seventh stone.

## 1. The criterion was written first, and it worked

Twice running, my acceptance test had been the weak link. So this
run's criteria went into the module's docstring **before launch**:
usability (resolved at 3σ, free baseline < 0.1, probe fits the box
r + 2w ≤ L/2), entry (≥ 4 usable widths, lever ≥ 2.5×, no sign
change), and verdict (**≥ 3 pairs, every exponent in [1, 3], spread
≤ 1.5 — no mean-based test**).

lucid 0038 priced that change: under a null matching what was
actually seen, the old `|mean − 2| < 0.8` test is wrong **51%** of
the time and the per-item test **0.5%** — a factor 99.

**It also caught a mis-diagnosis of mine before the run.** 0132
blamed the L = 20 failure on lever arm. The statistical errors on
those slopes were ±0.06, ±0.68, ±0.49 against a spread of −0.36 to
4.98, and one slope was **3.31 ± 0.06 — significantly not 2.** The
scatter was systematic, so more lever arm could not fix it. The
L = 32 run's purpose was corrected in the docstring accordingly:
decide whether the per-pair slopes are finite-volume or physical.

## 2. The verdict: FAIL

| pair | outcome |
|---|---|
| (4,0,0,0) vs (2,2,2,2) | 8 widths, lever 3.2×, exponent **4.70** |
| (4,0,0,0) vs (3,2,1,1) | EXCLUDED — residual changes sign |
| (6,0,0,0) vs (3,3,3,3) | EXCLUDED — residual changes sign |
| (6,0,0,0) vs (4,4,2,0) | EXCLUDED — residual changes sign |
| (8,0,0,0) vs (4,4,4,4) | EXCLUDED — lever arm 2.00 < 2.5 |

≥3 pairs: **1 — FAIL.** Exponents in [1,3]: **4.70 — FAIL.**

> **The bound does not propagate.** It stands where measured — the
> interacting contribution to rotational-symmetry breaking is ≤1.4%
> at r ≈ 5a — and the step to physical scales rests on Symanzik's
> theorem alone, premise unverified.

The pre-registered **secondary finding** fired: three pairs changing
sign means the residual is not a single-power quantity, so
Symanzik's premise here is not merely unverified but **actively
unsupported at these scales**.

## 3. The shape (post-hoc, labelled as such)

Not a pre-registered test — reported because the pattern is
consistent across pairs and is more informative than the FAIL.

| pair | residual across w = 1.25 … 4.0 | tail |
|---|---|---|
| (4,0,0,0) vs (2,2,2,2) | +0.0310 +0.0119 +0.0044 +0.0014 +0.00004 +0.00019 +0.00026 +0.00024 | **plateau** |
| (4,0,0,0) vs (3,2,1,1) | +0.0022 −0.0017 −0.0031 −0.0033 −0.0027 −0.0023 −0.0022 | **plateau** |
| (6,0,0,0) vs (3,3,3,3) | −0.0535 −0.0212 −0.0108 −0.0029 −0.0001 +0.0006 +0.0008 | falling |
| (6,0,0,0) vs (4,4,2,0) | +0.0093 −0.0068 −0.0074 −0.0044 −0.0026 −0.0020 −0.0019 | **plateau** |
| (8,0,0,0) vs (4,4,4,4) | −0.1089 −0.0147 −0.0009 +0.0020 +0.0030 | falling |

> **Two components.** A steeply falling piece — what an O(a²)
> artefact looks like — and then a **plateau at |residual| ≈ 0.002
> that does not shrink further.** Three pairs cross zero on the way,
> and the two crossings at r = 6 and r = 8 both land near w ≈ 3.05.

**The plateau is the finding.** Its origin is open, with three
candidates:

1. a genuinely non-vanishing anisotropy at the 0.2% level;
2. an inadequacy of the free-field baseline at large w;
3. the onset of wrap-around — the largest widths sit at the
   *boundary* of criterion (iii), r + 2w ≤ L/2.

(3) is the one I would bet on and cannot exclude: at w = 4, r = 8,
r + 2w = 16 = L/2 exactly. Discriminating needs **L = 48**, roughly
5× this run's cost.

## 4. Front status

| | |
|---|---|
| the branch | decided, two volumes |
| the hierarchy | ξ/a ~ 10¹³, untuned — *why gravity is weak* |
| Lorentz restoration | ≤1.4% at r ≈ 5a; **does not propagate**, and the residual is **not a single power** |
| triviality | scoped |
| the residual trend | closed — the exact zeros, 15% |
| **the plateau** | **new, open — needs L = 48** |

Worth stating plainly: this turn's headline is a **failed test that
was allowed to fail**. The criterion held, the exclusions were
reported rather than tuned away, and what came out is a structural
feature nobody was looking for. That is the machinery working, not a
setback — but the Lorentz debt is no closer to propagating than it
was two stones ago, and it should not be described as if it were.
