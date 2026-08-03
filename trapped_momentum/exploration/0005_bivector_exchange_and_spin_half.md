# 0005 — The exchange calculation, and two corrections that improve it

The plane-to-plane calculation, done. Plus your correction on the null plane
(which resolves the factor of 2 using the model's own premise) and your point
about apparent mass continuity (which turns out to have a clean mechanism).

Checked in `output/0005_bivector_exchange_and_spin_half.py` (48/48).

**A bug worth recording:** the first run of the stress-tensor routine applied
the metric twice in the `F^{μα}F^ν_α` contraction, producing nonzero traces and
inverting the headline conclusion. The self-checks caught it. The numbers below
are post-fix; the analytic result (tracelessness) was right and the code was
wrong, which is the failure mode to keep watching for.

## The calculation

A winding plane `span{u,v}` is a bivector `F^{μν} = u^μv^ν − u^νv^μ`. The only
symmetric rank-2 object bilinear in a bivector is

```
T^{μν} = F^{μα}F^ν_α − ¼ η^{μν} F^{αβ}F_{αβ}
```

This has the Maxwell-stress *form*, reached by the algebra of 2-forms — nothing
electromagnetic assumed. Verified symmetric and **traceless for every plane
type**, spacelike, timelike, null, and generic. In 4D the trace cancels
identically because `η_{μν}η^{μν} = 4` kills it against the `¼`.

Symmetric + traceless + rank-2 is the graviton's index structure. "Right shape
for spin-2" is now checked rather than hoped.

### The discriminator, and it is decisive

Exchange between two sources contracts them differently depending on the
mediator:

```
scalar (spin-0):   A ∝ (tr T)(tr T′)
tensor (spin-2):   A ∝ T^{μν}T′_{μν} − ½(tr T)(tr T′)
```

Since every source built this way is traceless, **the scalar amplitude vanishes
identically** — zero in every pair checked, and not by a tunable cancellation:
each trace is separately zero, for all plane types at once.

> **A particle whose fundamental object is a winding plane cannot couple to a
> scalar mediator at all.** Scalar gravity is not disfavoured here; it is
> unavailable. The lowest available universal long-range channel is spin-2.

This is the same fact as the classic empirical discriminator. Nordström's
scalar gravity predicts **zero** light deflection, and it predicts zero for
exactly this reason: radiation's stress tensor is traceless, so there is
nothing for a scalar to couple to. Measured deflection at the solar limb is
1.75″, not zero.

So the light-bending falsifier flagged in `0002` is **passed in the only sense
currently available**: the model cannot produce the Nordström answer even in
principle. Getting the *coefficient* right requires dynamics the model does not
have. Do not read this as deriving 1.75″.

### One subtlety, so the table is not misread

Some spin-2 entries also vanish (e.g. `x∧y` against `t∧x`). That is **not**
gravity switching off. The full contraction is orientation-dependent — which is
what having a tensor rather than a scalar *means* — and can cancel for
particular relative plane orientations. The static Newtonian limit is governed
by `T⁰⁰T′⁰⁰`, which is **nonzero in every row**. So universal attraction
survives while the sub-leading structure is orientation-sensitive, which is the
expected shape of spin–spin coupling in GR rather than a defect.

## Mass is the trace, and trapping is what generates it

This closes the standing "what confines the ray" gap by at least saying what
the confinement is *for*.

- A free null ray has a traceless stress tensor → **massless**.
- For any **stationary bound** system the tensor virial theorem gives
  `∫T^{ij}d³x = 0`, hence `∫T^μ_μ d³x = ∫T⁰⁰d³x = Mc²`.

Verified on the photon-gas-in-a-box arithmetic: radiation has `p = ρ/3` so
`ρ − 3p = 0` exactly (traceless, massless); add wall tension balancing the
pressure and the volume integral of the spatial stress vanishes, leaving
`∫T^μ_μ = E = Mc²`.

> **"Mass is trapped momentum" = mass is the trace that trapping generates.**

Free → traceless → massless. Confined → trace `= Mc²` → massive. This is the
same claim from the first turn, now as an identity in the stress tensor, and it
ties the confinement question to something the calculation actually uses.

## Your correction on the null plane — accepted, and it resolves the factor of 2

The claim was that a particle winding in the null plane is what shows half
states. It holds, and the mechanism is better than the group-winding fork I
offered last turn because it uses the model's own premise rather than an extra
choice.

**A null vector is a spinor squared.** For `k = (1,0,0,1)`, the matrix
`K = k^μσ_μ` has `det K = k·k = 0`, so it is **rank 1**, and rank-1 Hermitian
matrices factor as `K = ξξ†` — verified with `ξ = (√2, 0)` to 4e-16. The square
root is two-valued: `ξ` and `−ξ` give the same `k`.

Rotating about the null direction, the two objects come apart exactly as
predicted — vectors see `φ`, spinors see `φ/2`:

| `φ` | null vector | spinor factor |
|---|---|---|
| 0° | fixed | `+1` |
| 360° | **fixed** | **`−1`** |
| 720° | fixed | `+1` |

At 360° the null vector is exactly unchanged while the spinor has gone to minus
itself. **The half is not inserted; it is the square root relating the two.**

The consequence for the outstanding defect: `0002` obtained `L = nħ` by
demanding single-valuedness of a *vector-like* wave on the loop. If the object
on the loop is the null ray's **spinor**, antiperiodic boundary conditions are
admissible and the modes are half-integers — verified orthogonal at
`(½, 1½, …)`. The lowest antiperiodic mode is `½`, giving **`L = ħ/2`**.

> The factor of 2 is resolved by the model's own premise. The circulating object
> is null; null vectors have spinor square roots; spinors on a loop admit the
> antiperiodic spin structure; the lowest mode is `½`. Nothing was added.

**Caveat, and it is real:** this fixes the *kinematic* mode numbers — it shows
half-integers are **permitted**. Showing the dynamics *select* the antiperiodic
sector rather than merely allowing it is not done. That is now the residual
form of the factor-2 problem, and it is much smaller than the original.

This supersedes both earlier candidates: the counter-circulating beat (`0003`)
and the winding-in-the-group fork (`0004`). Those remain on the record as
alternatives, but the null route is preferable because it requires no choice —
the object was already null.

## Your point on mass continuity — there is a clean mechanism

The suggestion: apparent mass continuity is an effect of the time axis changing
angle, derived from the implied geometry rather than intrinsic to the particle
— which would let mass be genuinely quantized while looking continuous.

That works, and it is computable. Take the one-parameter family of planes

```
span{ (a,0,0,1), (0,1,0,0) },       det g = 1 − a²
```

which sweeps through all three causal types: `a<1` spacelike, `a=1` null, `a>1`
timelike. The generator's eigenvalues are `0, ±i√(1−a²)` for `a<1` — so the
orbit is **closed with angular frequency `ω(a) = √(1−a²)`**, period `2π/ω`.

| `a` | type | `ω = √(1−a²)` | period |
|---|---|---|---|
| 0.0 | spacelike | 1.0 | 6.3 |
| 0.9 | spacelike | 0.436 | 14.4 |
| 0.99 | spacelike | 0.141 | 44.5 |
| 0.9999 | spacelike | 0.0141 | 444 |
| 1.0 | null | 0 | **infinite** |
| 1.2 | timelike | — | no period |

The level spacing of a closed orbit goes as its frequency, so

> **spacing ∝ √(1−a²) → 0 as the winding plane approaches null.**

The spectrum stays genuinely discrete — the winding number is still an integer
— while the spacing collapses, so it *looks* continuous. Continuity becomes a
property of how the plane sits relative to the time axis, an effect of the
implied geometry, exactly as proposed.

It also softens `0004`'s conclusion in a useful way. `0004` said the absence of
a mass ladder favours an open (timelike) winding over a compact one. With this
mechanism, a **near-null** winding is also compatible with the data: still
closed, still quantized, but with spacing too fine to resolve. Kaluza–Klein is
back in play provided the winding plane is near-null rather than cleanly
spacelike. The earlier verdict was too quick, and this is the correction.

**Where it stands as physics.** With both `n` and `a` free per particle,
`m = n√(1−a²)·scale` fits any mass whatsoever, so as it stands the mechanism
explains *how* apparent continuity can arise from real quantization but
predicts no value. It becomes predictive only if something independent fixes
`a`. That is the next question — and it is a much better question than "why are
the masses what they are," because it is a question about geometry rather than
about a list of numbers.

## Next

1. **What fixes `a`?** The whole predictive content of the mass sector now sits
   here. If `a` is determined by the particle's relation to the rest of the web
   — which is what the differential-relativity framing would want — then
   generations might be different values of `a` at the same `n`.
2. **Do the dynamics select the antiperiodic sector?** The residual factor-2
   question, now sharply posed.
3. **The coefficient in light bending.** Passing the sign/structure test is not
   passing the magnitude test, and the magnitude needs dynamics.
4. Charge is still untouched. A bivector has two invariants (`F·F` and
   `F·F̃`); only the first has been used. The second is parity-odd, which is at
   least the right character for a charge-like quantum number. Unexplored.
