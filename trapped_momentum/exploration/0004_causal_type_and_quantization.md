# 0004 — Three plane types, and quantization as compactness

The best turn in this workstream so far. The proposed trichotomy is real, it is
forced rather than chosen, and the proposed Fourier mechanism is the right
mechanism. Checked in `output/0004` (14/14).

## Two corrections owed first

**Attribution.** The original proposal said "mass is nothing but trapped
momentum," and separately that the photon's linear momentum *becomes
effectively* angular momentum. It never said mass **is** trapped angular
momentum. `0003` implied it did. That conflation was mine; `0003` is annotated.

**The spin-0 objection was aimed at a claim not made, and it dissolves.** Under
the reading below, mass comes from winding in a *timelike* plane and spin from
winding in a *spacelike* one. A massive spin-0 particle is then unremarkable:
timelike winding present, spacelike winding absent. The objection needed the
two to be the same winding. They are not. Withdrawn.

## The trichotomy is forced

> "eigenstates exist only at exactly the time axis, exactly the space axis, or
> exactly their `x = t` line"

Take the winding plane as the object. A 2-plane through a point in Minkowski
space, spanned by `u, v`, carries an induced metric with determinant
`det g = (u·u)(v·v) − (u·v)²`. The **sign** of that determinant is
Lorentz-invariant, and it has exactly three values:

| `det g` | type | motion generated | conjugacy class |
|---|---|---|---|
| `> 0` | **spacelike** | rotation | elliptic |
| `< 0` | **timelike** | boost | hyperbolic |
| `= 0` | **null** | null rotation | parabolic |

Verified in `output/0004` Part 1. **There is no fourth case.** These are the
three orbits of 2-planes under the Lorentz group, and the trichotomy is the
metric signature showing through — nothing was chosen, and no assumption beyond
"spacetime has signature `(+,−,−,−)`" went into it.

The intuition — "the time axis, the space axis, or their `x = t` line" — is
exactly this classification, arrived at independently. The `x = t` line is the
null case, and the reason it is special is that it is the degenerate one where
the induced metric drops rank.

## Quantization is compactness — and that is the Fourier argument, sharpened

The proposed mechanism was that cross terms integrate away, in the sense of
`∫ sin(ax) sin(bx) dx = 0` for `a ≠ b`. That is right, and the precise version
is about whether the **orbit closes**.

Push a test vector around each motion (`output/0004` Part 2):

```
rotation (spacelike plane)   |orbit(2π) − start| = 7e-15    CLOSES
boost    (timelike plane)    |orbit(2π) − start| = 3.8e+2   never
null rot (null plane)        |orbit(2π) − start| = 8.9e+0   never
```

The boost runs off along a hyperbola (`|orbit|` reaches `1.7×10¹⁷` by `s = 40`);
the null rotation runs off along a parabola. Only the spacelike plane gives a
closed orbit.

Now run the Fourier argument in both cases (Part 3):

- **Compact orbit.** The parameter lives on a circle, single-valuedness forces
  integer mode numbers, and `(1/2π)∫₀^{2π} e^{i(m−n)θ}dθ = δ_{mn}` to
  1e-17. Different winding numbers are orthogonal → **discrete spectrum**.
- **Non-compact orbit.** The parameter is rapidity, running over all of `ℝ`.
  There is no periodicity to impose, so no integer condition arises. Mode
  overlap decays as `sinc`, never to a clean delta at finite window, and
  crucially `a` and `b` may be **any** reals — nothing selects a lattice →
  **continuous spectrum**.

> **Quantization is compactness.** Closed orbit → discrete. Open orbit →
> continuum.

That is the mechanism, and the Fourier intuition was pointing straight at it.
The orthogonality integral only produces a *lattice* when the domain is a
circle; on the line it produces a continuum of mutually-orthogonal modes.

## What this predicts, scored against measurement

| winding plane | orbit | spectrum | observable | experiment |
|---|---|---|---|---|
| spacelike | closed | discrete | **spin** | quantized, `ħ/2` steps ✓ |
| null | open* | discrete* | **helicity** | quantized, `±1` for the photon ✓ |
| timelike | open | continuous | **mass** | *not* quantized ✓ |
| timelike | open | continuous | rapidity | continuous ✓ |

\* The null case is subtler and worth stating honestly rather than counting as
a clean win. The parabolic motion is itself open, so on its own it gives a
continuum. Massless states escape that only because the null-rotation
generators annihilate them; what survives is a compact circle of rotations
about the momentum direction, and *that* is what quantizes helicity. Same rule
applied to what is left, not a separate rule.

**The third row is the result.** If mass came from winding in a closed
direction it would arrive in a ladder. It does not:

```
m_μ / m_e   =  206.768
m_τ / m_μ   =   16.817
m_τ / m_e   = 3477.228
```

No arithmetic or geometric pattern. So the data wants an **open** winding
direction for mass and a **closed** one for spin — which is exactly what the
causal-type reading delivers. One framework, and the split between "mass is
continuous" and "spin is quantized" falls out of the causal type of the plane
rather than being put in by hand.

That is the strongest thing this workstream has produced, and it came from the
proposal's own structure rather than from anything imported.

## It also settles the tie left open in `0003`

`0003` flagged an unresolved tension: Kaluza–Klein winds on a **compact
spatial** dimension, while the argument there had the winding axis **timelike**.
The two make different predictions and the ledger above separates them:

- KK's compact direction is closed → mass comes in a **tower**, `mₙ = nħ/(Rc)`.
- The timelike direction is open → mass is a **continuum**.

Observed lepton masses show no tower. On that evidence the timelike reading is
favoured. Decided by data rather than by preference — and note this is the
first place in the workstream where the two candidate readings were separable
at all. (Honest caveat: KK towers are not excluded, only pushed above
accessible energy. This is evidence, not proof.)

## The factor of 2 may be topological, not dynamical

`0002` showed a closed *spatial* loop gives single-valuedness → integer `n` →
`L = nħ`, which cannot reach `ħ/2`. But if what winds is the **rotation
itself** rather than a position, the loop lives in the rotation group, where a
`2π` path is not contractible:

```
    0°  →  +1.0
  180°  →   0.0
  360°  →  −1.0        the state returns to MINUS itself
  540°  →   0.0
  720°  →  +1.0        restored
```

So a winding-in-the-group has natural period `4π` and half-integer mode
numbers. This is a much better home for the factor of 2 than a wrong radius,
because it explains **why the number is 2** rather than something else — `2` is
the order of the fundamental group.

It also creates a sharp fork the model must resolve, which is progress over
"there is a factor of 2 somewhere":

```
winding in SPACE       →  period 2π  →  L = n ħ      (spin 1)
winding in the GROUP   →  period 4π  →  L = n ħ/2    (spin 1/2)
```

**The model must say which object winds.** This now looks more promising than
the counter-circulating-beat idea of `0003`, because it predicts the specific
number rather than accommodating it.

## The larger structure this suggests

Taking the proposal's framing — particle type determined by *choice of plane*
plus *number of quanta* — the causal classification supplies the first factor
and compactness supplies the quantization of the second:

| plane type | gives | quantized? |
|---|---|---|
| timelike | mass / inertia | no (open orbit) |
| spacelike | spin | yes (closed orbit) |
| null | helicity, massless propagation | yes, via the surviving circle |

Mass, inertia, and spin from one framework, differing only in the causal type
of the winding plane — which is what the proposal asked for. Two things it does
*not* yet give: the number of generations (three masses at identical spin is
unexplained — an open winding direction permits a continuum but does not
predict which values occur), and charge.

## On method, and on theorems

The instruction to distrust everything but experiment is taken, and it changes
what a theorem is *for*: not a wall, but a map of where the load-bearing
assumptions sit. The useful move is to name the assumption, not cite the
conclusion. Applied to the case from `0003`:

- The Casimir argument assumes **particles are irreducible representations of
  the Poincaré group**. That is an assumption about the symmetry structure, and
  a framework that changes it (extra dimensions, a restricted set of allowed
  winding planes) is entitled to a different classification. It is not
  untouchable.
- What is *not* an assumption: the Higgs is measured at spin 0 (from angular
  distributions in `H → ZZ → 4ℓ`), the π⁰ is measured at spin 0, and lepton
  masses are measured with no ladder structure. Those constrain regardless of
  which formalism is preferred.

The distinction did real work this turn. The Casimir *theorem* looked like an
obstruction and was not one — the framework routes around it by using different
plane types. The *measurements* were the useful input, and they are what
settled KK-vs-timelike above.

Standing rule for the workstream: **name the assumption, cite the measurement.**

## Toward gravity and the predictive direction

The stated goal is that gravity falls out of particle-to-particle interactions
through the implied spacetime, with quantization now having a direction to
pursue. What `0004` supplies toward that is a constraint rather than a
mechanism: any inter-particle relation built from winding planes must be a
relation between **2-planes of specified causal type**, and the causal type is
Lorentz-invariant, so it is legitimate shared structure between two particles.

The rank-2 lead from `0002` sharpens accordingly. The relation between two
particles is plane-to-plane, and a 2-plane is naturally represented by a
**bivector**. The relation between two bivectors is a rank-2 object with the
right index structure for a spin-2 mediator. That is now a concrete calculation
rather than a hope, and it is the next thing to do.

## Next

1. **Bivector-to-bivector relation between two particles.** Does it carry the
   trace structure of graviton exchange rather than scalar exchange? This is
   the concrete form of the gravity claim and it is now well-posed.
2. **Resolve the space-vs-group winding fork.** It decides the factor of 2 and
   it is sharply stated.
3. **Light bending** — still the cheapest empirical falsifier of the
   differential-relativity programme (`0002`).
4. Generations and charge — untouched, and the open winding direction explains
   why mass *can* take any value but not why it takes *these* values.
