# 0007 — One object: split quaternions and the nilpotent photon

> **AI-generated, not peer-reviewed.** Prior art credited in [`ATTRIBUTION.md`](../../ATTRIBUTION.md) — results are re-derivations of
> established work unless explicitly marked otherwise.

**Retracts `0006` Part 5.** The "massive particle = 4-velocity `u` + spin
bivector `S` with `S·u = 0`" move was Frenkel–Pirani, i.e. standard
relativistic spinning-particle theory reached by assertion rather than by the
mechanism. It matched observation by construction and explained nothing. The
criticism is accepted: it replaced one object that conceptually covered many
cases with three structures fitted to what we already measure.

What survives from `0006`: the null plane *being* a photon field
(`|E| = |B|`, `E ⊥ B`, both invariants zero), and helicity's two states coming
from the degeneracy of `k^⊥`. Those are explanatory. The two-structure
decomposition is not, and is withdrawn.

This note takes the other route. Checked in
`output/0007_split_quaternion_one_object.py` (44/44).

## The instinct was right: nilpotents supply the projection freedom

Split quaternions, basis `{1, i, j, k}` with

```
i² = −1        j² = k² = +1        ij = k,  jk = −i,  ki = j
```

Square a **general** pure element `v = bi + cj + dk`:

```
v² = −(b² − c² − d²) · 1  ≡  −Q(v) · 1
```

Verified across cases; the pure part of `v²` vanishes identically. **The square
of any pure element is a scalar.** So a single number `Q(v)` controls everything
that element can do.

That single identity is the whole trichotomy of `0004`. Not three structures —
the sign of `Q` on one object:

| | `v²` | `exp(θv)` | orbit |
|---|---|---|---|
| `Q > 0` | `−Q` | `cos(θ√Q) + v sin(θ√Q)/√Q` | **closed**, period `2π/√Q` |
| `Q < 0` | `+\|Q\|` | `cosh + v sinh` | open, exponential |
| `Q = 0` | `0` | **`1 + θv` exactly** — the series *terminates* | open, only **linear** |

Computed by raw series in every row, with no branching in the code — the
behaviour comes out of `Q` alone.

The nilpotent is the knife edge: it neither oscillates nor blows up. `exp(θv)`
at `θ = 1, 10, 100` gives exactly `1 + θv`. **That marginality is the resource.**

## The point: spin in space, nothing in time

Read the components for what they are. `i² = −1`, so the `i`-part is genuinely
**rotational**. `j² = k² = +1`, so `j,k` are **boost** content — time-mixing.
Then `Q = b² − c² − d²` is rotation-squared minus boost-squared.

| object | `b` (rotation) | boost `\|c,d\|` | `Q ~ mass²` | reading |
|---|---|---|---|---|
| pure rotation `i` | 1.0 | 0.0 | +1.0 | massive, spinning |
| pure boost `j` | 0.0 | 1.0 | −1.0 | no spin at all |
| **nilpotent `i+j`** | **1.0** | 1.0 | **0.0** | **spin, no mass** |
| nilpotent `5i+3j+4k` | 5.0 | 5.0 | 0.0 | spin, no mass |
| near-null `1.01i+j` | 1.01 | 1.0 | 0.020 | spin, tiny mass |

**Row 3 is the object.** The rotational component is nonzero — there is genuine
spin — while `Q = 0`, so there is no mass and no rest frame. The rotation is
exactly balanced against boost content, so it never appears in the invariant.

> "No projected evidence of rotation in time but spinning in space" is
> precisely `b ≠ 0` with `b² − c² − d² = 0`.

And this is **not a third structure**. It is one element of one algebra sitting
on the cone `Q = 0`. Massive particles are off the cone, photons are on it.
**The nilpotents are the light cone of the algebra** — `b² = c² + d²` is a cone
in `(b,c,d)`. The lightlike character of the photon and the nilpotency of its
generator are the same fact, not two facts that happen to agree.

This is what `0006` should have produced and did not.

## It is the same object `0004` already found, in its primitive rep

Split quaternions are the `2×2` real matrices. Under
`i → [[0,1],[−1,0]]`, `j → [[1,0],[0,−1]]`:

```
N = i + j  →  [[1,1],[−1,−1]]        N² = 0        det N = 0,  tr N = 0
```

`0004` built the null-rotation generator in the `4×4` **vector** rep and found
`N³ = 0` rather than `N² = 0`. Both are correct: the vector rep is the
**symmetric square** of this `2×2` one, and squaring a representation takes
nilpotency order 2 to order 3. Verified — `sym²(N)` has `max|N²| = 4 ≠ 0` and
`max|N³| = 0`.

So the earlier 4×4 computation and this one are the same object seen twice, and
the `2×2` is the primitive. (The first run of this check had the induced
derivation matrix wrong — transposed with bad coefficients — and reported
`|N³| = 4` while calling it zero. Caught by the self-check.)

## `0005`'s level spacing, recovered from the algebra

For `Q > 0` the orbit closes with period `2π/√Q`, so level spacing goes as
`√Q`:

| `(b,c,d)` | `Q` | period |
|---|---|---|
| `(2,1,0)` | 3.0 | 3.6 |
| `(1.1,1,0)` | 0.21 | 13.7 |
| `(1.01,1,0)` | 0.0201 | 44.3 |
| `(1.0001,1,0)` | 2.0e-4 | 444 |
| `(1,1,0)` | 0 | **infinite** |

`0005` obtained this collapse by sweeping a family of *planes*. Here it is one
element approaching the cone. Same result, better reason:

> **Mass ~ `√Q` is the distance from the nilpotent cone**, and masslessness is
> sitting exactly on it. Apparent continuity near the cone and exact
> masslessness on it are one phenomenon, not two.

## Honest scope, and the thing this opens

Split quaternions have a 3-dimensional pure part with signature `(+,−,−)`.
That is **2+1 spacetime, not 3+1.** The right toy for the mechanism, not yet
the real thing.

The 3+1 version is `sl(2,ℂ)` — traceless `2×2` **complex** matrices — and the
master identity survives verbatim by Cayley–Hamilton, verified on all four
classes:

```
X traceless  ⟹  X² = −det(X) · 1
```

But `det X` is now **complex**, so there are **four** classes, not three:

| `det X` | class | reading |
|---|---|---|
| real `> 0` | elliptic | rotation |
| real `< 0` | hyperbolic | boost |
| **zero** | **parabolic / nilpotent** | **massless** |
| **genuinely complex** | **loxodromic** | **rotation *and* boost, same axis — a screw** |

**The fourth class is new and it is the generic one.** A loxodromic element
rotates and boosts about the same axis simultaneously. That is what a massive
particle *with* spin should look like — one object doing both — which is
exactly what the two-structure hack in `0006` was working around.

> **Open question, and the right next calculation: is the loxodromic class
> where mass and spin coexist in a single object?** If so, the whole particle
> taxonomy is the conjugacy classification of one-parameter subgroups of
> `SL(2,ℂ)`, with no case-splitting anywhere:
>
> - elliptic → massive, no boost content
> - hyperbolic → boost only
> - **loxodromic → massive with spin** (generic)
> - nilpotent → massless with helicity (the cone)
>
> The 2+1 toy cannot see the loxodromic case at all, which is why this note
> stops short of claiming it.

## What is and is not claimed

**Claimed and checked:** the trichotomy reduces to the sign of one invariant on
one algebra element; the nilpotent has nonzero rotational content with zero
invariant, which is the requested "spins in space, not in time"; the nilpotent
cone *is* the light cone; `0004`'s and `0005`'s results both follow from the
same identity.

**Not claimed:** that this derives the photon's helicity value `±1` (that needs
the representation, not just the algebra element); that it gives dynamics; or
that 2+1 suffices. `sl(2,ℝ)` and `sl(2,ℂ)` are standard mathematics — the
content here is that the framework's own trichotomy, its mass-spacing result,
and its photon problem all collapse into one algebraic identity, which is the
unification that was asked for rather than three structures fitted to data.

## Next

1. **The loxodromic case.** Does one element with complex `det` carry both mass
   and spin? This is the calculation that would retire `0006`'s hack properly
   rather than merely retracting it.
2. **Get the helicity value.** The algebra gives "massless with a rotational
   component"; `±1` requires the representation. Connects to `0005`'s spinor
   square root, since `sl(2,ℂ)` is where both live.
3. Still open: what fixes `a` / `Q` (the mass sector's entire predictive
   content), charge quantization as a winding number, and whether dynamics
   select the antiperiodic sector.
