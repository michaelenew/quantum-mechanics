# 0029 — Nailing the prototype

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

The closing pass before 3+1: the measurement bit decided (by the
web's oldest postulate — and the answer is *no rift*), the
square-root ledger made a theorem-shaped statement, the rung
resolved, and the halo's law measured. With this, every open thread
of the 2+1 prototype is either closed or explicitly deferred to
3+1. Code: `output/0024_nailing_the_prototype.py`.

---

## 1. The measurement bit, decided — by P3

The discriminating principle was already in the repo, in its oldest
postulate. P3 — pairwise/sheaf consistency, compatible contexts
agree on overlaps — has a sequential reading: **an unread coarse
measurement must not disturb the statistics of a compatible finer
one.** That is the sheaf gluing condition applied to refinement
contexts, the same Abramsky–Brandenburger structure the whole
program was built on. Computed, on the web's own observable
(total-deficit parity, then individual deficits):

- **Lüders satisfies the chain law exactly** (deviation 6×10⁻¹⁷),
  and is the **unique** update that does: requiring refinement
  statistics to match in *every* basis of the outcome block forces
  the block to PσP/tr (Lüders matches random bases at 10⁻¹⁶;
  state-MRE fails at 0.147).
- **State-MRE violates it**: after an unread coarse measurement the
  fine statistics shift by total variation **0.040** — a broken
  sheaf gluing on compatible contexts.

So the web's own consistency requirement selects the **instrument
reading** of P5: minimum-relative-entropy lives at the channel
tier, where it reproduces Lüders. The state-tier reading is refuted
*from inside the theory* — no appeal to experiment needed. **No
rift with textbook QM**: P5 graduates from potential rival to
derivation of the update rule. (This also answers the standing
"quantum-MRE ⇔ Lüders" gap: equivalent, once P3 fixes the tier at
which the entropy is minimized.)

## 2. The square-root ledger: trust/information, everywhere

The observation that prompted this section: det^(−1) vs det^(−1/2)
is exactly the trust/information relationship. Made precise and
measured:

```
density tier (pointwise K):    log-slope in det g = −0.9995
loop tier (transport atom):    log-slope in det g = −0.5000
```

The holonomy observable screens with **exactly half** the exponent
of the density observable, mediated by the metric's own proper-area
factor √det g. The same one-half now stands in three registered
places:

1. **trust = √information** — the stat-tracker's forced split;
2. **amplitude = √probability** — the Born rule;
3. **loop-screening = √(density-screening)** — gravity's coupling,
   here.

One exponent, three faces: the loop/holonomy tier is everywhere the
square root of the density tier.

And the conjugate square, registered: as energy/momentum pair with
time/space, **trust pairs with time and distribution pairs with
space** — and the web's Noether structure already sits in that
arrangement: energy is the *rotation charge of loops* (measured by
round trips — trust operations; the deficit is read by going around
in time-like circulation), while momentum is the *spatial drift of
the moment* (the density/anisotropy sector — the distribution's
shape). One fixes distance, the other shape. Registered as
structure; the 3+1 build should treat it as a design constraint —
the trust sector rides the loop/time algebra, the distribution
sector rides the surface/space algebra.

## 3. The rung: the level is the resolution of the world's ledger

On a closed web, Gauss–Bonnet fixes Σδ = 4π = 2N quanta, with each
atom carrying 1..N−1 quanta (the per-defect bound δ < 2π). Counted:

- **N = 2: the closed universe is unique** — four atoms of π: the
  **pillowcase orbifold**. The minimal quantum world is the
  two-party flip, four times over.
- Closed universes need ≥ 3 atoms at every higher rung (and exactly
  4 at N = 2) — 2+1 GR's "no two-body closed universe," from
  counting.
- Ledger counts grow with the rung: 1, 13, 81 at N = 2, 3, 4.

So the rung question resolves by dissolving: **N is not a law of
the web; it is the resolution of the world's ledger.** Content
picks the level; the 2-adic tower's inverse limit is the ideal
completion housing every world at once.

## 4. The halo's law

The one undescribed classical structure. The exterior residual
K − πs/det g of an isolated lump, measured:

- radial exponent **−3.92 → −4**: a quadrupole tail;
- strength scaling **3.64 ≈ 4** for doubled S: **second order**;
- width scaling 1.89 ≈ σ² = 1.96;
- coefficient c = |K_halo|·r⁴/(S²σ²) ≈ **0.50**.

```
K_halo ≈ − S²σ² / (2 r⁴)
```

Second order in strength — which is exactly why the linear tier
never saw it (0020's flux was R-independent to 10⁻¹³), and the
gravitational face of the exchange-rate result that correlation
structure is second order in anisotropy. The classical field
content is now fully catalogued: **K = πs/det g (sourced, exact) +
the O(S²) quadrupole vacuum dressing.**

## The prototype, nailed

Every thread from the curvature program is now closed or
consciously deferred:

| thread | status |
|---|---|
| field equation + nonlinearity | closed: K = πs/det g |
| vacuum dressing | closed: −S²σ²/2r⁴ quadrupole |
| conservation | closed: the action's second EOM |
| causal cone | derived (locality) |
| symmetry | forced (Lorentz; MM + z=1 + central charge) |
| algebra | confirmed (Thomas–Wigner on solutions) |
| action | written (BF; charges = monodromies) |
| quantization | done (intersection-deformed Weyl; anyons) |
| level | structured (even, 2-core, 2-adic tower); rung = content |
| measurement | decided (P3 ⇒ instruments ⇒ Lüders; no rift) |
| trust/distribution | registered (the ½-exponent, three faces) |
| deferred to 3+1 | ISO(2,1) variational multiplet; spacetime monodromy; the movie as matter dynamics |

## Honest limits

- The measurement decision rests on reading P3's sheaf condition as
  applying to sequential refinement contexts; that reading is the
  natural one (it is the same gluing), but it is a reading — the
  doc states it, and the falsifiable alternative remains documented
  in 0028 for anyone who wants to reject the reading.
- The halo coefficient ≈ 0.50 is suggestive of exactly 1/2 but
  measured at one configuration family; the analytic derivation
  (second-order perturbation of the divergence identity) is the
  natural short proof and is left open.
- The conjugate square (trust/time, distribution/space) is
  registered structure with measured exponents, not a derived
  duality; the 3+1 build is where it earns theorem status or
  doesn't.

## Next

3+1 proper, with the completed prototype as the guide: 2-form
lattice BF with string defects, surface charges, linking-deformed
algebra; the census as representation theory; the movie as matter;
the trust/distribution square as a design constraint. The
prototype's last word: everything fundamental was forced — the
metric, the cone, the symmetry, the action, the quantum algebra,
the update rule. The only free things left in 2+1 were the world's
content and its ledger resolution. That is the standard 3+1 should
be held to.
