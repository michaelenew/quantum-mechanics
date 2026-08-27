# 0089 — The context spectrum: the vertex charges the (1,0) mode

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Tenth stone: 0075's standing interleaving, tested with 0078/0088's
vertex. At the bare one-plaquette chain the unbalanced (1,0)
multiplet — purely self-dual curvature, the connection/2-form mode —
propagates 0.10–0.30 nats/step *more lightly* than the graviton
(1,1), and 0075 filed that as "the measured job description for
vertex-level simplicity." The vertex was built since; here it is
asked the specific question. **It charges exactly the right thing,
at 4–12× the size of the gap — support for the conjectured lift,
honestly sized short of a decisive one.** Code:
`output/0080_the_context_spectrum.py`.

---

## 1. The anchor: the vertex kit in self-dual variables

The single-plaquette eigenvalue structure closes in (|F⁺|, |F⁻|):
the eight nonzero eigenvalues are ±(|F⁺| ± |F⁻|)/(2√2) fourfold, and
2·Pf = |F⁺|² − |F⁻|² (0057 §4's invariant, re-verified inside the
vertex machinery). So the *isolated* price of a plaquette depends
only on its balance — the (1,0)/(1,1) distinction is exactly the
η = |F⁻|/|F⁺| axis, and the vertex question is well-posed in the
measure's own variables.

## 2. The unbalance curve

Shift the geometric slot of a common-tetrad six-pack by a unit-norm
F(η), with the SD/ASD pair fixed per seed so the sweep is paired
(64 seeds):

| η = \|F⁻\|/\|F⁺\| | 0.00 | 0.25 | 0.50 | 0.75 | 1.00 |
|---|---|---|---|---|---|
| context Δprice | **5.050** | 4.862 | 4.417 | 4.014 | **3.885** |
| isolated Δprice | 3.358 | 3.222 | 2.956 | 2.763 | 2.791 |

Monotone in the mean: **pure self-dual content is the most expensive
thing you can hand a geometric vertex; balanced (simple) content the
cheapest.** The paired SD-over-balanced penalty is

```
+1.17 ± 0.12 nats/site   (59/64 seeds positive; isolated +0.57 ± 0.31;
                          context amplification ≈ 2×)
```

And the ladder position (s4): the self-dual insert sits at or above
0078's generic non-simple rung (+5.32 vs +4.26 mean context charge) —
pure (1,0) content is the *extreme case* of non-simplicity and the
vertex treats it accordingly.

## 3. The verdict, honestly sized

The context penalty exceeds the bare-chain lightness gap by **4–12×**
and clears its upper bound at ~7σ. So: any 4D assembly that charges
vertex prices at ≳ half a vertex per chain step **lifts (1,0) above
(1,1)** — the interleaving is a bare-chain artifact, as 0075
conjectured, and the mechanism is specifically the shared-frame
integral's dislike of unbalanced curvature (not a generic damping).

What this is *not*: a decisive lift. The currencies differ (chain
nats/step vs vertex nats/site), the assembly share of vertex charge
per plaquette in a genuine 4D complex is not fixed here, and the
shift-design's noise floor is recorded alongside the signal. The
decisive computation remains the assembled complex — A3's completion
— which now has both its ordered candidate list (0075) and its
per-site charge sheet (this stone).

## 4. Placement in the arc

This is one measured entry of 0088's coupling tensor — the entry
0075 ordered in advance. Read together: the vertex's context
coupling (0088) is not an undifferentiated nonlinearity; it has a
*spectroscopy*, and its strongest single preference measured so far
is balanced over unbalanced curvature — the simplicity constraint
acting as a mode filter. The spin-foam program imposes that filter
by hand at the vertex (EPRL/FK); here it is generated, with a
measured strength, by the same frame integral that generated the
kernel, the cross-simplicity, and the insertion ladder.

## Honest limits

- Shift design on one slot of one vertex; ε′ = 0.01; unit-norm
  sources on unit-norm packs. Ordering robust across all of it;
  absolute nats are convention-scaled.
- The (1,0) ↔ pure-self-dual identification is the standard
  Spin(4) = SU(2)×SU(2) content match, exact for the multiplet's
  curvature content, but the chain tension and the vertex price are
  different observables — the comparison is scale-against-scale, not
  a unified transfer matrix.
- 64 seeds; the η-curve's monotonicity is a statement about means
  (per-seed curves fluctuate).

## Open

1. **The assembled complex** (A3 completion): chain + vertices with
   the measured charge sheet — the one computation that converts
   "support" to "lift," and the same object the momentum half of the
   propagator needs. This is the program's standing heavy stone,
   now with every input measured.
2. The full coupling tensor (0088 open 1) beyond this entry.
3. The coherent-state (unbinned) refinement of both spectra
   (0074 open 3).
