# 0043 — The dimensional trade: charge for force, and the atom recovered

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0042 measured that the web's vacuum principle selects the harmonic
profile in every dimension. Running that ladder **down**, to d = 2,
returns the program's own founding object — and shows what the
dimension is actually trading. Code:
`output/0038_the_dimensional_trade.py`.

---

## 1. The atom is the d = 2 vacuum

In two spatial dimensions the harmonic exponent is p = d − 2 = **0**
— constant channel strength. Measured:

- **vacuum at p = 0** (1.5e−6) and nowhere else (p = 0.5, 1 fail at
  1.7e−1, 4.7e−1);
- the test particle feels **no force** (machine zero at two radii);
- the deficit is **0.772467**, against the exact atom
  2π(1−(1+w)^(−1/2)) = **0.772467**.

**The founding object of this program — 0014's cone, 0019's atom —
is the d = 2 case of the same field law that gives Schwarzschild at
d = 3.** And 0020's measured "no pair force in 2+1" is now
*derived* from the vacuum principle rather than observed as a
curiosity of the dimension.

That closes a loop opened very early: the conical atom was found by
Fisher-metric transport around an interaction node; it is the same
object the 4D vacuum principle produces when you set d = 2.

## 2. Topological versus geometric holonomy

The charge reader around a source, as a function of loop radius:

| source | R = 0.6 | 1.0 | 2.0 | 4.0 | character |
|---|---|---|---|---|---|
| codim 2 (string / 2+1 point) | 0.772467 | 0.772467 | 0.772467 | 0.772467 | **topological** (spread 4e−12) |
| codim 3 (point in 3D) | 0.4661 | 0.2924 | 0.1514 | 0.0771 | **geometric** (→ 2πM/R) |

**The codimension decides whether a charge is a topological
invariant or a curvature integral.** Same instrument, same kind of
loop; only the source's codimension differs.

## 3. The trade

Combining §1, §2, and 0041/0042:

| dim | vacuum profile | force | bond's charge |
|---|---|---|---|
| d = 2 | constant w (**the atom**) | none (measured 0) | topological deficit |
| **d = 3** | w = 2M/ρ | **Newton** | **zero** |
| d ≥ 4 | w = 2M/ρ^(d−2) | yes | nonzero |

> **Three spatial dimensions is where the bond has traded its
> charge for a force** — the unique dimension in which correlation
> acts without registering as participation.

This also refines 0042's operator claim, honestly. The braiding
phase ω^(n_a n_b) is the **2+1 realization** of the bond's product
structure — the dimension where the bond is topological and
forceless. In 3+1 the same bilinearity appears **dynamically**, as
m_a m_b/d. One product structure, two carriers, chosen by
dimension. (For *string* participants in 3+1 the topological
carrier returns — linking, 0030 — since strings are codim 2 again.
The carrier follows codimension, not dimension as such.)

## 4. The half is kinematics, not gravity

0039's 50/50 split of Ï between the kinetic tensor and the bond
holds for **every** force law — ratio 1.000000 at p = 0.5, 1, 2, 3.
The identity behind it is

```
m Ω² a = F   ⟹   2 m v² = F d
```

which uses circular motion *alone*: no force law, no dimension.
The "missing half" that led to the bond was never a gravitational
coincidence — **it is what binding means for a closed orbit**. That
strengthens rather than deflates 0039: the bond had to exist for
kinematic reasons, and gravity's job was only to say what its
tension is.

## Honest limits

- §1's d = 2 vacuum is measured over power-law profiles at one
  strength, like the d = 3, 4, 5 cases in 0042.
- §2's codim-3 holonomy tracks 2πM/R to ~10% at R = 0.6 and ~2% at
  R = 4 — the deviations are the geometric (nonlinear) corrections,
  not error; no closed form is extracted here.
- §3's table mixes measured entries (d = 2 force and charge, d = 3
  force, the d ≥ 4 profile) with entries derived in 0041/0042; the
  d ≥ 4 *force* is inferred from the profile, not integrated.
- The braiding refinement is a statement about which structure
  carries the bilinearity, not a derivation of either carrier from
  an action — the standing open since 0042.

## Open

1. **The bond's action** (carried, unchanged): the term whose
   variation gives tension = force classically and ω^(n_a n_b) in
   the topological sector. Both ends remain pinned; the middle is
   unwritten.
2. **Codimension as the real variable**: §3 suggests restating the
   whole ladder in terms of codimension rather than dimension —
   codim 2 objects carry topological charge in any d, codim 3
   objects carry geometric charge. The 3+1 string sector should
   then behave like 2+1 gravity transversally, which 0030 already
   measured (the transverse lift). Worth a unified statement.
3. **The two-body metric** (carried): a genuine second-order solve.
4. **d ≠ 3 radiation**: with the half now known to be kinematic,
   the remaining dimensional question is the propagator, not the
   source — does the wave zone in d ≥ 4 still carry the bond's
   half at the same weight?
