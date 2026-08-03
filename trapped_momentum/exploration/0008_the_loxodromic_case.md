# 0008 — The loxodromic case: one object carrying mass and spin

The calculation `0007` pointed at. It works, and it retires `0006`'s hack
properly rather than merely withdrawing it.

Checked in `output/0008_loxodromic.py` (46/46). Two bugs caught en route, both
recorded below.

## Setup

`X ∈ sl(2,ℂ)`, traceless, written `X = (ζ/2)(n̂·σ)` with `ζ = η − iθ` the
**complex rapidity**: `η` a boost rapidity and `θ` a rotation angle, **about the
same axis**. Then

```
det X = −ζ²/4
```

verified exactly in every case. The four classes are four regions of one
complex parameter:

| | `det X` | class |
|---|---|---|
| `θ` only | real **positive** | elliptic (rotation) |
| `η` only | real **negative** | hyperbolic (boost) |
| both | **complex** | **loxodromic (screw)** |

### The nilpotent is a different kind of axis, not a limit

Worth stating because it explains why `0006` felt forced into a separate case.
`det X = 0` is **not** `ζ = 0` — that is just `X = 0`. Nilpotency requires a
**complex null axis**, `n̂·n̂ = 0`, e.g. `n̂ = (1, i, 0)`, so that
`(n̂·σ)² = (n̂·n̂)I = 0`. Verified: `X² = 0`, `det X = 0`.

> Masslessness is not a small value of a parameter — it is a different kind of
> axis. No amount of tuning `η` and `θ` reaches it.

## `det X` carries **both** bivector invariants

`0005` flagged that a bivector has two invariants and that only the first had
been used, with the parity-odd second one homeless. It has a home:

```
Re(det X) = (θ² − η²)/4    ~   F·F    ~  B² − E²
Im(det X) = ηθ/2           ~   F·F̃    ~  E·B
```

Both verified across cases. The complex determinant is the self-dual packaging
of the pair, and **`Im(det X)` is nonzero exactly on the loxodromic class.**

This exposes a real limitation in `0004`: that classification read off **one**
invariant, so it was blind to everything the second one sees. A loxodromic
element with `θ = η` has `Re(det X) = 0` but `Im(det X) = 0.5` — it would have
been misfiled as "null" there, when it is neither null nor massless.

### The sharpest form: a massive spinning particle is not a plane

A bivector is **simple** (i.e. a single plane `u∧v`) exactly when `F·F̃ = 0`.

| class | `Re det` | `Im det` | a single plane? |
|---|---|---|---|
| elliptic | +0.25 | 0 | yes |
| hyperbolic | −0.25 | 0 | yes |
| **loxodromic** | 0 | **+0.5** | **no — two planes** |
| nilpotent | 0 | 0 | yes |

> A massive particle **with** spin is not a plane at all. It is a **non-simple
> bivector** — and a non-simple bivector has a *canonical* decomposition into
> two orthogonal simple pieces, one timelike and one spacelike.

That decomposition is a **theorem about the single object**, not a case-split
imposed on it. This is the answer to "one object or two": one object, which
happens not to be a plane, and whose canonical form has two orthogonal parts.

## The two invariant planes, explicitly

Acting on 4-vectors via `δH = XH + HX†` with `η = 1.3`, `θ = 0.7`, axis `z`:

```
t  →  (0, 0, 0, 1.3)          δz = η t
z  →  (1.3, 0, 0, 0)          δt = η z
x  →  (0, 0, 0.7, 0)          δy = θ x
y  →  (0, −0.7, 0, 0)         δx = −θ y
```

`span{t,z}` is closed, and the action there is a **boost** of rapidity `η`.
`span{x,y}` is closed, and the action there is a **rotation** by `θ`. The two
planes are orthogonal complements.

> `0006` wrote down a 4-velocity `u` plus a spin bivector `S` and **demanded**
> `S^{μν}u_ν = 0` to keep them orthogonal. Here that condition is not a
> postulate — it is the statement that the two invariant planes of one element
> are orthogonal complements, which they are automatically.

The hack is retired, not merely retracted.

## Mass is *having an axis*; masslessness is eigenvector degeneracy

The sharpest reading of mass so far, and better than `0007`'s
distance-from-the-cone (with which it agrees, since `|det X|` *is* that
distance).

| case | `det X` | eigenvalues | `\|v₁ × v₂\|` |
|---|---|---|---|
| elliptic | `+0.25` | `±0.5i` | 1.00 |
| hyperbolic | `−0.25` | `±0.5` | 1.00 |
| loxodromic | `+0.5i` | `±(0.5−0.5i)` | 1.00 |
| loxodromic, tilted axis | `+0.5i` | `±(0.5−0.5i)` | 0.60 |
| **nilpotent** | `0` | `±0` | **0.00** |

- `det X ≠ 0` → distinct eigenvalues → **two independent eigendirections** → a
  genuine axis → an invariant timelike plane → **a rest frame exists** →
  massive.
- `det X = 0` (`X ≠ 0`) → repeated eigenvalue → the eigendirections **collide**
  → no axis → no rest frame → **massless**.

> Masslessness is the matrix being **defective** — a Jordan block rather than a
> diagonalizable element. "Has a rest frame" and "is diagonalizable" are the
> same statement.

(The tilted row is there because `σ_z` is diagonal and the first version of this
check was an artifact of that — see the bug note.)

## The flow factors: compact × non-compact

`exp(sX)` has eigenvalues `exp(±sλ)` with `λ = a + ib`. With `η = 0.8, θ = 2.0`:
`λ = 0.5 − 1.0i`, so drift rate `a = 0.5` and winding rate `b = −1.0`.

Tracking along the flow: **the phase returns to zero exactly at every multiple
of the period, while the modulus grows without bound and never returns.**

One element, and its flow factors into a compact circle and a non-compact line.
Applying `0004`'s rule — quantization *is* compactness — **to each factor
separately**:

```
compact factor      → closed orbit → DISCRETE   → spin
non-compact factor  → open orbit   → CONTINUOUS → momentum
```

> A massive particle with spin is exactly that: a **quantized spin and a
> continuous momentum, carried by one object**. They do not need gluing because
> they are the two factors of one flow.

## The whole taxonomy from one family

| | reading |
|---|---|
| `θ → 0` | pure boost — massive, **spin 0** |
| `η → 0` | pure rotation — spin, no boost content |
| axis → null | nilpotent — **massless**, helicity only |
| both nonzero | **loxodromic** — massive **with** spin (generic) |

Massive spin-0 — the case that forced the retracted hack in `0006` — is now
just `θ = 0` inside one family, not a separate construction.

So the particle taxonomy is the conjugacy classification of one-parameter
subgroups of `SL(2,ℂ)`, with **no case-splitting anywhere**. That is the
unification that was asked for.

## Bugs caught

Both by the self-checks, both recorded because the failure modes recur:

1. **`eigen()` had no branch for diagonal matrices.** `X = (ζ/2)σ_z` is
   diagonal, so `q = r = 0` and the fallback returned two *parallel* vectors —
   making every case look degenerate, including the massive ones. The headline
   of Part 4 was inverted until fixed. A tilted-axis row was added so the result
   is not an artifact of the diagonal form.
2. **Two rotation-sense checks had flipped signs.** The derivation and the
   output both give `x → +θŷ`, `y → −θx̂` (the standard counterclockwise
   rotation for `ζ = η − iθ`); the check *labels* had been written from a mental
   image rather than the derivation. The physics was unaffected — it is a
   rotation in `span{x,y}` either way — but the assertions were wrong.

## What is and is not claimed

**Checked:** `det X = −ζ²/4`; the four classes as four regions of one complex
parameter; `det X` packaging both bivector invariants; loxodromic ⟺ non-simple
bivector; the two orthogonal invariant planes with boost in one and rotation in
the other; mass ⟺ diagonalizability; the compact × non-compact factorization of
the flow.

**Not claimed:** any *value* — not the spin magnitude, not `±1` helicity, not a
mass. This is the kinematic classification, and it says which structures exist
and how they relate, not what numbers they carry. Getting values needs
representations and dynamics, neither of which is here.

**Also honest:** `sl(2,ℂ)` conjugacy classes and the Frenkel–Pirani condition
are standard mathematics. The content is that the framework's own trichotomy,
its photon problem, its mass-spacing result, and the orthogonality condition it
had been *imposing* all fall out of one classification, with the retracted
two-structure hack appearing as the canonical decomposition of a single
non-simple element.

## Next

1. **Representations, for values.** The algebra gives structure; `±1` and `ħ/2`
   need the rep. This is where `0005`'s spinor square root should reconnect —
   `sl(2,ℂ)` is where both live.
2. **What fixes `ζ`?** Same question as "what fixes `a`" in `0005`, now sharper:
   the mass sector's entire predictive content is the value of one complex
   number per particle. Generations would be different `ζ` — and `ζ` is
   *complex*, so there are two real numbers per particle to explain, not one.
3. **Charge quantization** as a winding number (`0006`) — still open, and the
   `Im(det X)` invariant is a candidate home for it, being parity-odd.
