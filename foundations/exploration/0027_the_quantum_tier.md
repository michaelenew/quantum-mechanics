# 0027 — The quantum tier: the shape of the theory

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Quantizing 0026's action — and, per the standing directive, writing
the result as *shape*: the point of the Noether/action program is
the template it hands us for 3+1. Everything here is exact algebra
(one numerical integral). Code: `output/0022_the_quantum_tier.py`.

---

## The fundamental shape, as it now stands

The 2+1 web, assembled across 0019–0027, is this object:

```
state space   flat connections; all content in holonomies
charges       boundary monodromies (mass = rotation part,
              momentum = the moment's drift) — quasi-local, no densities
action        topological pairing:  S = Σ B·(F − src)   (BF/CS)
EOM           (1) F = src : curvature lives only at participants
              (2) dB = 0  : the conservation law — the action's other half
symmetry      the geometry's gauge group (ISO(2) → Poincaré at the
              Lorentz pole), selected, not chosen (0025)
causality     the cone, derived from locality (0022); rule-independent
quantum       the holonomy Weyl algebra; deformation = intersection form
matter        Wilson insertions; deficits quantized; abelian anyons
dressing      the Fisher metric's non-topological decoration
              (screening + halo) over the topological core
```

## 1. The Weyl algebra of holonomies

Quantizing the torus phase space of flat connections at level N:
the two cycle-holonomies become clock and shift with
UV = ωVU (ω = e^(2πi/N)), and general Wilson operators obey —
operator-exactly, verified across a family of cycles —

```
W(c₁) W(c₂) = ω^(c₁ × c₂) W(c₂) W(c₁)
```

**The commutator is the intersection number.** The classical charges
of 0025–0026 stop commuting when quantized, and their
noncommutativity is pure topology — quantization adds no local
structure, it deforms the holonomy algebra by how loops cross. (For
the program's oldest thread: noncommuting observables — the starting
point of quantum mechanics — appear here as the intersection
geometry of the very loops the charges live on.)

## 2. The deficit spectrum: participation is quantized

θ is an angle (the compensator is a phase), so its conjugate — B,
the budget, the deficit — has discrete spectrum {2πn/N}, and the
participant-insertion operator shifts it by exactly one unit
([D, A] = (2π/N)A, matrix-exact). Through δ = 8πGm: **masses come
in units 1/(4GN)** — the amplitude tier's single-valuedness prices
matter in integer atoms. (The mass bound Σδ = 4π then caps the
number of atoms the universe can hold at 2N: a finite-dimensional
world at any level.)

## 3. The minimal web is a qubit

At the minimal level N = 2: the Weyl pair **is** the Pauli pair
(U = Z, V = X, exactly; ZX = −XZ), and the deficit spectrum is
**{0, π}**.

This is the batch's centerpiece consistency: **the only nontrivial
deficit the minimal quantization admits is π — the measured flip
δ(2) = π of the two-party web** (0014's theorem of information
geometry). The geometry's measured spectral gap and the minimal
quantum's spectrum are the same number, arrived at from opposite
ends of the program. The ± double-cover sectors are the X
eigenstates; the compensator φ = π − δ takes exactly the binary
values {π, 0} — "one bit, two carriers" (0014) is now the N = 2
representation of the quantized action, and densification's
continuous φ (0015) is the large-N/classical limit. The minimal web
is a qubit; the amplitude tier and the gravity tier now share a
mechanism, a symmetry, an action, and a quantization.

## 4. Braiding

The Wilson loop measures the deficit (W|n⟩ = ωⁿ|n⟩), and
conjugation gives the Aharonov–Bohm algebra W A W⁻¹ = ωA: carrying
a unit participant around a defect yields the topological phase.
Defects are abelian anyons — the quantum face of "masses add,
centres braid" (0012). At N = 2 the unit defect's circuit phase is
−1: the spinor/double-cover sign, a third time.

## 5. The 3+1 template

Read the shape forward one dimension:

| | 2+1 (built) | 3+1 (the template) |
|---|---|---|
| B | scalar | **2-form** |
| defects | points | **strings** (codim 2 — as 0012 required) |
| charge carriers | loops | loops **and surfaces** |
| algebra deformation | intersection of cycles | **linking** |
| matter insertions | Wilson points | Wilson **lines** (knotted) |

The Gauss linking integral of a Hopf pair computes to 1.0000 — the
exponent the 3+1 algebra runs on: Wilson loops and B-surface
operators commute up to ω^(linking). So **the quantum algebra of
the 3+1 web is the linking/braiding algebra of loops and surfaces —
which is the movie/census formalism** the knot thread has been
building since 0006: its state sums are representations of this
algebra, its tetrahedron census enumerates the consistent triple
events, and its wall theorem (0018) is a selection rule on which
surface representations exist. **The gravity thread and the knot
thread are one theory in 3+1.** That is the strong guide the
program wanted before making the jump: the 3+1 construction is not
open-ended — its kinematics (strings, movies), its algebra
(linking), its selection rules (the census results), and its shape
(BF with 2-form budget, charges as monodromies, conservation as the
second EOM) are all already fixed by the prototype.

## Honest limits

- The level N is an input, not derived. Candidates for what fixes
  it: the compensator's 2π-periodicity plus the mass bound
  Σδ = 4π (a finite budget wants a finite level); not settled.
- This quantizes the topological core; the dressing (screening,
  halo — 0019's nonlinear sector) is classical decoration here, and
  its quantization (the Fisher metric as a kinetic term) is open.
- The qubit identification is structural (algebra + spectrum); the
  Born-rule side of the amplitude tier lives in the arithmetic
  thread (influence = √information; the amplitude shadow) and is
  not rederived here.
- §5's template is an exact statement about abelian BF; the census
  results suggest the 3+1 web wants *nonabelian* structure at
  triple points — where the template will need its first genuine
  extension.

## Open

1. **Derive the level**: N from the web's own constraints (budget
   4π + phase single-valuedness), which would make mass units a
   theorem.
2. **Quantize the dressing**: BF + Fisher kinetic term; target =
   0019's nonlinear curve as the semiclassical correction.
3. **The 3+1 build proper**, now with the guide: 2-form lattice BF,
   string defects, surface charges; check the census/wall selection
   rules appear as representation constraints.
4. **The measurement tier**: P5 (minimum-relative-entropy
   projection) meeting the holonomy Hilbert space — the repo's
   original measurement problem, now with a concrete state space to
   pose it on.
