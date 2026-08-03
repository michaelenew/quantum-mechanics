# 0006 — The photon forces the reorganisation, and where α stands

The photon objection is correct and it is the most productive break so far: the
fix was already sitting unused in the trichotomy, and repairing it also
dissolves an earlier problem structurally rather than case-by-case.

Checked in `output/0006_photon_null_plane_and_alpha.py` (12/12).

## The contradiction, confirmed

Original formulation: total speed pinned at `c`, split by `sin θ = v/c`.

| `v/c` | `θ` | `p_⊥/p` | `L` |
|---|---|---|---|
| 0.00 | 0° | 1.000 | 1.000 |
| 0.90 | 64.2° | 0.436 | 0.436 |
| **1.00** | **90°** | **0.000** | **0.000** |

At `v = c` the transverse component is exactly zero, so `L = r·p_⊥ = 0`. **The
naive model predicts a spin-0 photon.** Measured helicity is `±1`. This is a
genuine internal failure, not a missing detail.

## The object required — and it was already in the trichotomy

The requirement: a 2-plane that can look like it spins in a spatial direction
while carrying **no** time-direction content. Scanning every direction inside
each plane type:

| plane | type | timelike dirs | null dirs | spacelike dirs |
|---|---|---|---|---|
| `span{x,y}` | spacelike | 0 | 0 | 3600 |
| `span{t,x}` | timelike | 1798 | 4 | 1798 |
| **`span{k,x}`**, `k = t+z` | **null** | **0** | **2** | 3598 |

(sampled over a full turn, so each null *line* appears twice as `±k`)

The timelike plane is disqualified — it contains timelike directions, hence
time-axis content, hence mass. The **null plane** is the answer: no timelike
direction anywhere in it, exactly one null line (the propagation direction
itself), everything else spacelike.

Algebraically: for `w = ak + bx`, `w·w = a² − b² − a² = −b² ≤ 0`, with equality
only along `k`. Never timelike.

> **This is not an extension bolted on. It is the third case of `0004`'s
> trichotomy, which had been labelled and never used.** The framework already
> had the slot; the photon is what sits in it.

## The null plane *is* a photon field

Not "can model" — is. Writing down `F = k ∧ x` with `k = (1,0,0,1)`:

```
E = (−1, 0, 0)        |E| = 1
B = ( 0,−1, 0)        |B| = 1
E · B    = 0
E × B    = (0,0,1)  =  spatial direction of k
F·F      = 0          both Lorentz invariants
F·F̃      = 0          vanish
```

Both invariants vanishing is the signature of a **radiation field**: `|E| = |B|`
and `E ⊥ B` hold in *every* frame, because no frame can remove either. The
Poynting vector points along the propagation direction. Nothing was fitted —
`k ∧ x` was written down and a free electromagnetic wave came out.

The contrast is instructive: `x∧y` gives `|E| = 0, |B| = 1, F·F = +2` (pure
magnetic); `t∧x` gives `|E| = 1, |B| = 0, F·F = −2` (pure electric). Each of
those has a frame where the other component vanishes. **Only the null case has
no such frame** — which is exactly why it describes something that moves at `c`
for everyone.

## Why helicity is one number and spin is a 3-vector

This falls out for free and it was not anticipated.

Spin planes must be orthogonal to the particle's own direction. So look at the
orthogonal complement:

| | `w·w` | `dim(w^⊥)` | rank of induced metric | degenerate dirs |
|---|---|---|---|---|
| massive `u = (1,0,0,0)` | `+1` | 3 | 3 | **0** |
| massless `k = (1,0,0,1)` | `0` | 3 | 2 | **1** |

**A null vector is orthogonal to itself.** So `k^⊥` is 3-dimensional but
*degenerate* — it contains `k`. Quotienting that direction out leaves a
2-dimensional spacelike plane: the polarization plane, carrying only `SO(2)`.
One number, two signs.

> The photon has helicity `±1` rather than three states `m = −1,0,+1` because
> the longitudinal state is the direction that got quotiented away. It follows
> from `k·k = 0`, not from a rule imposed on top.

Massive particles have a nondegenerate 3-dimensional complement → a full
`SO(3)` of spin planes → spin as a 3-vector with `2s+1` states.

## The reorganisation this forces — **RETRACTED, see `0007`**

> **This section is withdrawn.** What follows is Frenkel–Pirani, i.e. standard
> relativistic spinning-particle theory, asserted rather than derived from the
> mechanism. It matches observation by construction and explains nothing — it
> replaced one object that covered many cases conceptually with three
> structures fitted to what is already measured. `0007` does the job properly:
> a single split-quaternion element whose square `v² = −Q(v)·1` reproduces the
> whole trichotomy, with the photon as the **nilpotent** case — nonzero
> rotational component, zero invariant. Kept below only as the record of a
> wrong turn.

A massive particle is **not one bivector**. It is two objects:

```
a 4-velocity u        (timelike)              → mass
a spin bivector S with S^{μν}u_ν = 0          → spin
```

The second is the **Frenkel–Pirani condition**, and it says `S` is purely
spatial in the rest frame. Verified: `S = x∧y` with `u = (1,0,0,0)` gives
`S^{μν}u_ν = 0` exactly.

Two independent objects, so **mass and spin are independent**, and a massive
spin-0 particle is just `u` with `S = 0`. The worry raised in `0003` now
dissolves *structurally* rather than being handled case-by-case with
counter-circulation. That earlier repair is superseded.

For a photon there is no `u` to be orthogonal to, the condition degenerates
onto the null plane, and only helicity survives. One framework, three regimes,
selected by causal type:

| structure | gives |
|---|---|
| timelike direction present | mass |
| spacelike plane orthogonal to it | spin (3-vector, `2s+1` states) |
| null plane, no timelike direction | helicity (one number, two signs) |

The photon: no timelike direction → massless ✓; null plane with spacelike
quotient → helicity `±1` ✓. Both halves of the original observation, recovered.

## Where α stands

Asked directly, so answered directly, including the part that is unwelcome.

### The decisive fact is experimental: α runs

```
α⁻¹ at q² = 0     = 137.035999
α⁻¹ at q² = M_Z²  = 127.951        (MS-bar)
difference        ≈ 9.1
```

**α is not a constant.** Any "derivation of 137" is a derivation of the
zero-momentum limit of a scale-dependent coupling — a dynamical quantity, not a
geometric one. A kinematic framework of the kind built here has no mechanism
that could produce a running quantity's endpoint. This is measurement, and it
is what sinks most α programmes before they start.

The cautionary case worth keeping in view: Eddington argued for 136 from
counting degrees of freedom, then revised to 137 when measurements improved.
The revision is what the episode is remembered for. **Any derivation flexible
enough to be adjusted afterwards was never a derivation** — which is the
relevant discipline for a framework that has, as of this note, several free
structural choices still open.

### What *is* plausibly in reach: charge quantization

By the mechanism the framework already owns from `0004`: **compactness → closed
orbit → discrete winding number.** If charge is a winding number on a compact
direction, integer charge is automatic, by exactly the argument that gave
quantized spin. That is a real structural result and it is worth pursuing.

Note it is the same shape as Dirac's monopole argument and as charge
quantization in Kaluza–Klein — the framework would be rediscovering a known
mechanism, which by the standing method is a success condition rather than a
disappointment.

### What geometry gives instead of a value: a relocation

In Kaluza–Klein the coupling ties to the compactification radius, roughly
`α ~ (l_P/R)²`, so

```
R = l_P / √α ≈ 11.7 l_P
```

(order of magnitude only — the coefficient is convention-dependent). So the
geometric route converts "why 137" into "why `R ≈ 12` Planck lengths." That is
honest progress of a kind, and it should not be sold as more.

**Recommendation: pursue charge quantization; do not pursue the value of α.**
The first is a structural question the framework is built to answer. The second
is a dynamical question it has no machinery for, and the running of α says the
target is not the kind of thing being looked for.

## Status of the workstream after this

The photon break improved things. Current standing:

- Three causal types, all now used: timelike → mass, spacelike → spin,
  null → helicity/massless propagation.
- Mass and spin structurally independent (`u` and `S`), superseding `0003`'s
  counter-circulation repair.
- Helicity's two states derived from the degeneracy of `k^⊥`.
- Spin ½ from the spinor square root of a null vector (`0005`).
- Scalar gravity unavailable, spin-2 forced (`0005`).

## Next

1. **Charge quantization as a winding number.** The one α-adjacent target with
   a real chance. Needs a compact direction the framework can motivate rather
   than assume.
2. **What fixes `a`** (the plane's tilt) — still the whole predictive content
   of the mass sector, from `0005`.
3. **Does the dynamics select the antiperiodic sector** — residual factor-2
   question.
4. The original circulating-null-ray picture now needs restating. `0003`'s
   "null helix winding about a timelike worldline" describes the *massive*
   case only; the massless case is a null plane with no winding at all. Whether
   one geometric object covers both, or the model is genuinely two-case, is
   unresolved and should be settled before building further.
