# 0076 — The MK flow: 4D is where the healed weight goes critical

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

A4: which sector of the healed weight survives coarse-graining in
four dimensions? Instrument: the Migdal–Kadanoff recursion —
bond-moving (pointwise power ζ = b^(d−2)) then decimation (t → t^b²
per representation) — calibrated against both exact anchors this
program owns, with its bias *measured*, after the naive
implementation was caught lying. Code: `output/0068_the_mk_flow.py`
(4.7 s).

---

## 1. Calibration, and a methods save

- **2D anchor (MK exact there)**: the Z₃ ledger collapses to free —
  matches 0071's exact blocking. ✓
- **4D abelian anchor**: N = 3, 5 flow to BF/deconfined — matches
  0071's self-duality placement. ✓ But **N = 2 also flows to BF**,
  where the exact answer is *confined*: **MK is
  deconfinement-biased near transitions.** Recorded and used: an MK
  "confined" is trustworthy; a marginal MK "deconfined" is suspect.
- **The pitfall**: the first implementation (fusion algebra truncated
  at jmax) *flipped its 4D verdict as jmax grew* — drifting down at
  jmax = 8, up at 10 and 12. The fix: do bond-moving exactly
  (pointwise, on a class-angle grid) and truncate only the
  *decimated reconstruction*, where t⁴ decay makes the cutoff
  harmless. The naive and controlled forms disagree qualitatively;
  only the controlled one is reported.

## 2. The 4D flow is near-stationary with a stable hierarchy

| step | t(1,0) | t(1,1) | t(2,2) | t(3,3) | t(6,6) |
|---|---|---|---|---|---|
| 1 | 0.9369 | 0.8779 | 0.6771 | 0.4594 | 0.0680 |
| 5 | 0.9378 | 0.8794 | 0.6801 | 0.4625 | 0.0673 |
| 12 | 0.9360 | 0.8761 | 0.6725 | 0.4523 | 0.0622 |

t(1,1) drifts **< 1% over steps 3–12**; 0075's mode ordering holds at
every step; high spins are suppressed and stay suppressed. This is a
**nontrivial (near-)fixed structure** — not the free/confined sink,
not the BF/topological point, but a hierarchical spectrum frozen
between them.

## 3. The 3D contrast is total

Same instrument, ζ = 2: t(1,1) ≈ 3×10⁻⁷¹ by step 8. **Three
dimensions confine absolutely; four go critical.** 0071's abelian
dichotomy — rigidity begins at D = 4 — survives the nonabelian lift,
now in the strongest available form: the same recursion, the same
weight, annihilation in 3D and near-stationarity in 4D.

## 4. The reading

Within MK: the healed weight in 4D sits at or near a nontrivial fixed
structure whose light sectors are the low-spin multiplets — **the
graviton multiplet among the survivors at t ≈ 0.88** — while high
spins die. The measured deconfinement bias means "marginal" could
shade toward "slowly confining"; what is robust is the 3D/4D
dichotomy and the surviving hierarchy. And the flow has answered
where A3's momentum half should be posed: **at this fixed
structure** — the continuum candidate now has an address.

## Honest limits

- MK is uncontrolled everywhere and *measured* to err toward
  deconfinement near transitions; the 4D near-stationarity is an
  MK statement, not a theorem.
- One bin scale (s₀ = 0.75) for the starting weight; the fixed
  structure's basin was not mapped.
- Euclidean, class-function truncation at JBIG = 24 in the
  reconstruction (harmless by t⁴ decay, but stated); NG = 200 grid.
- "Critical" here means near-stationary transfer eigenvalues under
  MK — momentum-space masslessness (A3's second half) is the real
  test and remains open.

## Open

1. **A3's momentum half at the fixed structure**: correlations on a
   4D complex (or its transfer-matrix slice) with the fixed-point
   weight — the 1/k² comparison against 0063, now with an address.
2. Map the basin: does the fixed structure attract nearby bin
   scales / profiles (universality), or is it a knife-edge?
3. The drift's sign at higher precision: marginal vs slowly
   confining — a finer instrument than MK (e.g., the exact
   2-plaquette transfer object) could settle the direction.
4. Standing: the vertex/intertwiners; Λ1; C1; the arithmetic-branch
   pass; the sign-problem toy.
