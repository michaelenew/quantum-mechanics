# 0012 — Curvature from crossings: the defect ledger

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0011 established that a knot diagram *is* a consistency web. This
note tests the next claim — **interactions are crossings and
curvature is the holonomy of the loop around them** — at the one
place physics can adjudicate it: the 2+1 gravity boundary, where
conical defects *are* matter. Four computations, nothing asserted
that is not computed. Code: `output/0005_curvature_from_crossings.py`.

The verdict in one line: **the claim is exactly right, and it comes
with a conservation law the proposal did not anticipate — curvature
cannot be created by interactions, only redistributed, and the total
budget is the known mass bound of closed 2+1 gravity.**

---

## 1. Holonomy *is* the angle defect — computed, not asserted

On real polyhedra (tetrahedron, cube, octahedron, icosahedron),
parallel transport around a vertex is composed honestly: build the
vertex star, take the unfolding isometry across each edge as a 3×3
rotation, multiply them around the loop, extract the rotation angle.

| solid | vertices | defect/vertex | measured holonomy | total |
|---|---|---|---|---|
| tetrahedron | 4 | 3.141593 | 3.141593 | 4π |
| cube | 8 | 1.570796 | 1.570796 | 4π |
| octahedron | 6 | 2.094395 | 2.094395 | 4π |
| icosahedron | 12 | 1.047198 | 1.047198 | 4π |

Agreement to 1e-8 at *every* vertex. The surface is flat everywhere
else, so all curvature sits at the defects and **is** the loop
holonomy. This is the proposal's core clause, verified: you perceive
the turning by going around; there is nothing to perceive anywhere
along the way.

## 2. The curvature budget is topological

Knot projections built from actual plane curves (torus projections
with 1, 3, 5, 7 crossings), self-intersections found geometrically,
the planar map traced from the rotation system, combinatorial
curvature computed in exact rationals
(κ(v) = 1 − deg/2 + Σ_corners 1/|face|):

| diagram | V | E | F | κ per crossing | total |
|---|---|---|---|---|---|
| limaçon | 1 | 2 | 3 | 2 | **2** |
| trefoil T(2,3) | 3 | 6 | 5 | 2/3 | **2** |
| cinquefoil T(2,5) | 5 | 10 | 7 | 2/5 | **2** |
| T(2,7) | 7 | 14 | 9 | 2/7 | **2** |

Two readings, both load-bearing:

- **The total is pinned at χ = 2 regardless of crossing count.**
  Adding an interaction adds a vertex *and* a face; the ledger
  closes. So **interactions redistribute curvature; they cannot
  create it.** Any "curvature from crossings" dynamics is a
  transport law, not a source law — the source is topology.
- **The per-crossing curvature is exactly 2/V** for these symmetric
  diagrams: interactions *dilute* curvature. The knot-dependent
  physics is in the distribution, never the sum.

## 3. The budget is the mass bound

Descartes/Gauss–Bonnet (verified in §1): total defect on a spherical
surface = 4π, always. With the 2+1 dictionary (Deser–Jackiw–'t Hooft)
δ = 8πGm:

```
Σ 8πG mᵢ = 4π   ⟹   Σ mᵢ = 1/(2G)
```

and per-defect δ ≤ 2π ⟹ m < 1/(4G) — a single mass that large would
close the space. Two maximal defects saturate the budget exactly
(the degenerate spindle). Both bounds are the *same ledger* that
bounds a diagram's curvature.

The identification is tighter still: the rotation parts of all
defect holonomies compose to the **identity** precisely because the
deficits sum to 0 mod 2π (verified for 4, 6, 12 equal defects). The
loop enclosing everything is contractible on the far side of the
sphere — so **Gauss–Bonnet is exactly the condition that the global
holonomy can be trivial.** The curvature budget and the consistency
of the web are one constraint.

## 4. Masses add; centres braid

Two conical defects (deficits d₁, d₂ at points p₁, p₂) have ISO(2)
holonomies. Verified numerically against a closed-form derivation:

- the product's **rotation is d₁ + d₂ in either order** — masses add,
  and that addition is precisely the *abelianization* of ISO(2);
- the two orders differ by the **pure translation**
  `(I − R_{d₁})(I − R_{d₂})(p₁ − p₂)`, vanishing iff a defect is
  massless or the two coincide.

So **"mass" is the abelian shadow of the holonomy, and the
nonabelian residue is a real relative displacement** — 2+1
gravitational scattering, the Aharonov–Bohm-like shift from carrying
one defect around another. This is the braided tier of the
arithmetic bridge (0011 §2; `arithmetic/0066`) arriving as physics:
gravity's nonlinearity *is* the noncommutativity of defect holonomy,
and the linear "masses add" law is exactly the part that forgets
order.

## What this settles and what it does not

**Settles.** The proposal's mechanism is correct in 2+1: interactions
as defects, curvature as loop holonomy, and the nonabelian
composition as interaction. It also supplies the constraint the
proposal was missing — a conservation law making curvature
topological in total and dynamical only in distribution.

**Does not settle — the honest gap at the gravity boundary:**

- **2+1 has no local attraction and no waves.** Two static conical
  defects do not attract; there is no propagating degree of freedom.
  So "curvature from crossings" reproduces 2+1 *kinematics* exactly
  and delivers no Newtonian limit. A 3+1 version must produce
  attraction, which this mechanism alone does not.
- **In 3+1 the defects are strings, not points.** Regge curvature
  lives on codimension-2 hinges: in 3+1 that is *edges*, so a
  conical defect is a cosmic string. The literal 3+1 reading of
  "interactions are crossings in a knotted structure" is a knotted
  string network (Vachaspati–Vilenkin; Faddeev–Niemi hopfions) — a
  real research area, and the honest form of the proposal in our
  dimension.
- **Combinatorial curvature is not metric curvature.** §2's κ is a
  discrete ledger on the diagram's face structure; the identification
  with §1's metric defect is by shared Gauss–Bonnet accounting, not
  by a derivation that assigns a metric to a diagram.
- **The web's Fisher/Bures metric (0005) is untouched here.** This
  note computes the *defect* geometry; whether the information
  metric around a high-degree interaction node reproduces a deficit
  angle is still the open computation (0011 open item 3).

## Open

1. **The deficit from the information metric.** Compute the Fisher
   geometry of a web neighbourhood around an interaction node of
   degree k and ask whether it has a deficit angle growing with k.
   That would connect §1's defect to 0005's metric and turn
   "correlation sources curvature" from analogy into a formula —
   the repo's flagged open row.
2. **Where attraction could come from.** In 2+1 attraction is absent
   because the defect budget is rigid. Testing whether a *dynamical*
   redistribution (interactions moving curvature between crossings,
   §2) produces an effective force is a concrete calculation and the
   only route from this mechanism to a Newtonian limit.
3. **Spin as framing.** The path-to-self holonomy (writhe/framing,
   Călugăreanu) is the one quantity in §2's ledger that R1 moves;
   in 2+1 gravity a spinning defect adds exactly a translation along
   the axis to the holonomy. Matching the framing anomaly to spin is
   a well-posed next computation.
