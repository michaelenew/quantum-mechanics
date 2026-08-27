# 0145 — Burndown items 2 and 5: one retired, one obstructed

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Code: `output/0133_the_graviton_propagator.py`, with lucid 0047.

## Item 5 — retired, not reconciled

lucid 0047 asked the prior question nobody had: **are the two routes
to G the same quantity?** Given the field a mass, on one lattice with
one regulator, **πp/α runs 2.64 → 123.07 — a factor 46.7.**

> The ratio is not a constant, so a cut and a deformation are not one
> measurement. **The factor 20 was a category error, not a
> discrepancy.**

They coincide only under a fluctuation–dissipation relation, and
lucid 0019 measured long ago that this program has none — white
vacuum, Coulomb response.

**G is a response**, so it is read off the induced-stiffness route.
The entanglement number is a different observable wearing the same
units.

**And the consequence improves things.** 0105's ℓ_P = 2.27a came from
the retired route. Recomputed from the response route:

| fields | ℓ_P/a | 0143's N-inversion gap |
|---|---|---|
| 1 | 0.717 | **−5.5%** |
| 2 | 0.507 | **−4.8%** |
| 6 | 0.293 | **−3.6%** |

0143 reported κ = 16 against a required 17.37, **7.9% low**. On the
response route the gap is **3.6–5.5%** and is now nearly independent
of the field count. **Item 5 closed.**

## Item 2 — obstructed

The spin-2 correlator on the rebuilt Spin(4) lattice, L = 8,
acceptance 0.416, 170 measurements.

**Unsmeared:** all three sectors sit at the shuffle floor —
spin 2 peaks at 1.6× floor with the sign alternating across r. Not a
decaying correlator; noise.

**Smeared** (0118's kernel, the medicine that took an unmeasurable
anisotropy from 0.1σ to 49σ):

| w | spin 0 (r=1) | spin 1 | spin 2 | floor |
|---|---|---|---|---|
| 1.0 | +0.7704 | +0.7678 | **+0.7692** | **0.3423** |
| 1.6 | +0.8828 | +0.8794 | **+0.8827** | **0.6042** |

> **All three sectors become identical and the floor rises with
> them.** The kernel's own correlation dominates the measurement.

**Why the medicine failed here, and it is worth naming:** in 0118 the
signal was a *ratio* against a large disconnected piece, so
suppressing variance won. Here the observable *is* the connected
correlator, which is O(g⁴) at κ ≈ 17 — smearing shrinks the signal
along with the noise. The graviton propagator is below
per-configuration noise, not merely spread thin.

**The cost of pushing through:** connected-correlator SNR grows as
√n, and we are at ~1× floor with 170 configurations. Five sigma needs
roughly **25× more statistics** — feasible, but it needs a C kernel
rather than the numpy Metropolis, or a variance-reduction method
(multilevel, link integration) the program does not have.

## Where the burndown stands

| | |
|---|---|
| ✅ 1 | Spin(4) rebuild |
| ⛔ **2** | **graviton propagator — obstructed on statistics** |
| 3 | source as lattice code — blocked by 2 |
| 4 | measure the response — blocked by 2, 3 |
| ✅ 5 | the factor 20 — **retired as a category error** |
| 6 | classical tests from Q4 — blocked |

**The obstruction is not conceptual.** Everything needed exists: the
lattice, the sector, the observable, the projection. What is missing
is throughput. That is the honest blocker, and it is the first purely
computational one this program has hit.
