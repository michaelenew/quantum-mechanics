# 0135 — Continuity, closed: the Gaussian caveat retired

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Code: `output/0124_the_nongaussian_direction.py`, with lucid 0040
supplying the method. Ninth and final stone of the continuity front.

## 1. The one thing left

0134 answered the Lorentz question and named its weakness: the
Whittle score is a **Gaussian** rule, so it reads only the two-point
function. A record with an isotropic spectrum but anisotropic higher
moments would pass it while being anisotropic.

lucid 0040 established that the weakness is **real**, not
theoretical. On a field whose power spectrum is forced back to the
isotropic shell mean mode by mode — so the two-point function is
isotropic *by construction* while the phases carry the anisotropy —
the Whittle test scores **exactly 0.00 at every amplitude** while a
directional test rises monotonically to 0.0147.

(A first attempt at that construction failed and is recorded there:
putting the anisotropy in the three-point at O(ε) and the two-point
at O(ε²) was not enough — Whittle caught it at 26 nats.)

## 2. The test, with no probe and no baseline

Sample the gauge-invariant local operator along rays stepping by
lattice vectors of **equal length, different orientation** —
(2,0,0,0) vs (1,1,1,1), (4,0,0,0) vs (2,2,2,2), (6,0,0,0) vs
(3,3,3,3) — discretise, fit an order-2 Markov predictor to one
ensemble, code the other, symmetrise.

If the theory is rotationally invariant at that scale the two
ensembles are statistically identical **at every order**. There is
no kernel to manufacture a signal and no free-field baseline to get
wrong: the two ensembles are each other's control.

## 3. The result

| | value |
|---|---|
| noise floor (same-direction splits of the record) | 0.000002 nats/site |
| excess at length 2 | +0.000001 — **at the floor** |
| excess at length 4 | +0.000001 — **at the floor** |
| excess at length 6 | +0.000001 — **at the floor** |
| order check (1 and 3) | agrees; the predictor is not the limit |

**And the injection, which is what makes the zeros mean anything.**
Known anisotropy added to the real configurations:

| ε | excess | vs floor |
|---|---|---|
| 0.02 | −0.000000 | 0.2× |
| **0.05** | +0.000011 | **5.1×** |
| 0.10 | +0.000214 | 96× |
| 0.40 | +0.008309 | 3741× |

The test responds steeply. **So the zeros are bounds, not
blindness** — the same discipline 0123 §4 applied, and the one lucid
0038 priced at a factor 99.

## 4. It reconciles with 0134 rather than contradicting it

0134 *did* detect breaking on this same measure — c = 0.241 at 28.6
nats. The two statistics probe different scales: that test ran over
**all** modes, including the highest, where a hypercubic lattice is
of course anisotropic. These rays step by **two lattice spacings at
minimum**, so they never sample spacing-1 structure. The ray test
starts where the lattice artefact has already largely gone.

> **The Gaussian caveat is closed.** A test that reads every order,
> with no kernel and no baseline, finds no anisotropy at any
> separation it can probe, bounded below an ε = 0.05 injection.

## 5. The continuity front, closed out

| item | status |
|---|---|
| the target | **reframed** — no dial exists, so continuity means ξ/a is already large |
| the coupling | β_eff ≈ 12, weak — and this is *why gravity is weak* |
| the branch | **decided**, two volumes, tempered |
| the hierarchy | **ξ/a ~ 10¹³, untuned** |
| Lorentz restoration (2-point) | **answered** — breaking decays faster than dimension-six |
| Lorentz restoration (all orders) | **answered** — at the floor, injection-calibrated |
| triviality | **scoped** — inherits the standard expectation; directly untestable |
| the residual trend | **closed** — the exact zeros, 15% |
| 0133's plateau | **explained** — a sum of operators, not one power |

**Continuity is closed.** It was the last open conjunct of 0069's
wall ("the interacting, *continuous*, 3+1 quantum measure"), and it
closed not by a bigger run but by asking the question the way a
filter asks it — twice, on two different weaknesses.

What remains named rather than closed: the ray test probes
separations ≥ 2a, so nothing here speaks to spacing-1 structure
(where the lattice *is* anisotropic, correctly); and the
extrapolation from measured separations to physical ones still rests
on effective-field-theory reasoning, now with the O(a²) premise
supported at two-point order and untested above it.
