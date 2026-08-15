# 0017 — The arrow and the branch wall

0016's three opens, executed. Two clean confirmations and one honest
wall: the correlation share's decay law is derived and measured, the
chiral weights are exhibited as concrete set-theoretic arrows of time
(and turn out to be mirror twins), and the first cup/cap condition —
branch-point degeneracy — annihilates every nonabelian weight in the
census. Code: `output/0012_decay_chirality_cupcap.py`.

---

## 1. Score correlation is a luxury of sparse company

The decay law conjectured from 0016's table, now derived and measured.

**Derivation.** For an *isotropic* ambient information matrix the
radial/angular score correlation vanishes identically (B = 0 at every
angle — checked, and obvious from symmetry). So the correlation part
of the deficit is **second order in the anisotropy**. The ring web's
anisotropic fluctuation is O(1/k) relative, so the correlation part
must scale like δ·O(1/k) ~ 1/k², while the anisotropy part carries
the full δ ~ 1/k.

**Measurement** (k = 4 … 44):

| k | anisotropy part | correlation part |
|---|---|---|
| 4 | 1.37226 | 0.083578 |
| 9 | 0.64943 | 0.017671 |
| 20 | 0.30330 | 0.003750 |
| 44 | 0.14046 | 0.000794 |

Fitted large-k exponents: **anisotropy −0.98, correlation −1.97**.

So the split is confirmed: in dense webs the compensator is
anisotropy-priced only; the mutual-information term is an
intrinsically **few-party effect** — score correlation between the
radial and angular channels is a luxury of sparse company. The
two-party web (where δ = π, the flip) is the regime where the
information-currency part of the price is largest; densification
kills it a full power of k faster than the geometric part.

## 2. The arrow of time, exhibited — and it comes in mirror twins

0016 found that exactly the two (4,4) orbits — the census's most
braided solutions — lose their weights under time reversal. This
section makes the arrow concrete:

- **Forward**: each chiral orbit's weight satisfies the tetrahedron
  identity on **all 64 states** — the two orderings of the four
  triple-point events always accumulate equal total weight. A movie
  run forward gets a well-defined score.
- **Backward**: the reversed system (inverse events) **fails on 32 of
  64 states** for each orbit. Concretely, at the state
  (0,0,0,0,0,0), the two orderings of the reversed movie score 0 vs 1
  (orbit 1) and 1 vs 0 (orbit 2). Backward, the "score" depends on
  the order you process the events in — it is not a number at all.

So the chiral weights are **set-theoretic arrows of time**: a
functional of the movie that exists for one orientation of the film
and is *ill-defined* — not merely different — for the other. This is
the sharpest census-level answer to 0016's open 2: yes, they detect
orientation, in the strongest possible sense (existence, not value).

**The mirror test.** Coordinate reversal (x,y,z) → (z,y,x) applied to
chiral orbit 1's table is again a tetrahedron solution — and it lands
in **orbit 2**, not back in orbit 1. The two chiral orbits are
**mirror twins**: each scores one time direction, and spatial
reversal exchanges them. The census contains not one anomalous object
but a parity-conjugate pair — exactly the shape of a
framing/orientation anomaly, where the two chiralities are separately
consistent and swapped by reflection. (Whether this *is* the census
shadow of the framing anomaly stays open; the structure now matches
it in both respects: locus on the deepest braiding, and exchange
under reversal.)

## 3. The branch wall: degeneracy annihilates the nonabelian census

The cup/cap staging, first condition. In CJKLS surface theory the
branch-point move forces the weight to vanish on degenerate triples:

```
θ(x, x, y) = θ(x, y, y) = 0
```

— the level-2 sibling of the quandle degeneracy axiom that 0006
showed *is* Reidemeister-I safety, one level up. Imposing this on top
of the forward + time-reversed systems, per orbit:

- Survivors at p = 2: **2 of 21**. At p = 3: **2 of 21**. The
  survivors are the identity orbit (dim 2) and a single abelian
  (2,2,2,2) orbit (dim 1) — which is also one of the few whose
  operation maps degenerate triples to degenerate triples ("preserves
  cups" at the color level).
- **Every one of the 13 nonabelian orbits is killed.** The witness
  block for a degenerate-safe bidirectional nonabelian weight finds
  nothing, because nothing exists.

This is the batch's honest negative finding, and it mirrors 0006's
rack-vs-quandle measurement one level up: there, dropping the
degeneracy axiom (rack, not quandle) broke R1-invariance; here,
*imposing* the level-2 degeneracy breaks every braided weight. The
interpretation, stated carefully:

**A set-theoretic surface invariant built from this census cannot be
both braided and branch-point-safe.** The routes forward are exactly
the ones surface theory already knows: (a) restrict to
**branch-point-free surfaces** — every orientable 2-knot has a
branch-point-free movie presentation (Kamada; lifting to embedded
surfaces without branch points), on which the 19-orbit bidirectional
census of 0016 is the right starting set and the wall never applies;
or (b) **richer weight targets** than Z_p — the CJKLS literature's
own move to nonabelian coefficient groups and twisted cohomology.
The census result says the naive road (abelian weights, branch points
allowed, braiding retained) is closed — measured shut, not assumed
shut.

What survives the full local gauntlet — tetrahedron move, time
reversal, branch points — is the abelian core, and for that core the
only thing standing between the weights and an actual surface state
sum is global movie bookkeeping (frame conventions and
normalization), no further local condition.

## Honest limits

- §1's derivation is an order-of-magnitude argument made exact by
  measurement (fitted exponents), not a closed-form constant; the
  1/k and 1/k² laws are established, their coefficients are not.
- §2's "arrow" is a property of weights over the specific 4-event
  placement complex (the Zamolodchikov staging), not yet a theorem
  about arbitrary movies.
- §3 imposes branch-point degeneracy as the CJKLS vanishing
  condition; the full cup/cap/saddle move calculus (births and
  deaths as morphisms) is represented here only through this local
  condition plus time reversal — the frame category is deliberately
  not staged.

## Open

1. **Branch-point-free state sums.** Run the 19-orbit bidirectional
   weights over branch-point-free movie presentations of actual
   2-knots (spun trefoil vs unknotted sphere) — the direct test of
   whether the braided census weights detect knotted surfaces.
2. **The anomaly identification.** The mirror-twin structure of §2
   matches the framing anomaly's shape; a sharp statement would tie
   the 32-state failure pattern to a computable anomaly class
   (H³ of the placement group?).
3. **Nonabelian targets.** Rebuild the weight systems with values in
   a nonabelian group (the census's own order-384 placement group is
   the natural candidate) and re-test the branch wall.
