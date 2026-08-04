# 0013 — Stage 2b result: the ring is half of Kerr, and the other half is the confinement

The pre-registered Kerr-quadrupole test from `0012`, run.
`output/0012_stage2b_kerr_quadrupole.py`, 21/21 checks. Everything numeric is
from scratch (potentials, Legendre projection, branch-cut jump); the two [K]
anchors are flagged where used.

## Verdict on the registered question

> Does the light ring's trace-free quadrupole match Kerr's `M₂ = −J²/M`, with
> the order-unity factor exactly 1?

**No. The factor is exactly 1/2.** Sign correct, magnitude order-unity correct,
`M₂_ring = −Ma²/2` against Kerr's `−Ma²` — both verified by two independent
routes each (far-field Legendre projection of the computed potential vs direct
moment integrals; the Appell form reproduces the famous
`M_l = M·Re[(ia)^l]` pattern through `l = 4` including the odd-moment zeros).

The SSC hazard registered in `0012` does not bite: the source is static,
axisymmetric, reflection-symmetric, so the centroid is unambiguous and the 1/2
is physics, not convention.

Pre-registration scorecard now stands at three falsified hopes across Stages
2/2b — and each one identified the next object. This one identified the most
important one yet.

## What the failure teaches: `M₂` reads the confinement

Weak-field stationary mass moments are sourced by the Tolman effective density
`ρ_eff = T⁰⁰ + T^kk`. The photon ring's own null flow has `T^kk = +E` at
`ρ = a` (pressure = energy density, the null signature from `0005`). The virial
theorem forces `∫T^kk_total = 0` — so `M₀ = E` always, the weight is protected
— but the **second moment of stress** `Y = ∫T^kk_total ρ² dA` is free, and:

```
M₂ = −½(Ea² + Y)             Kerr  ⟺  Y = +Ea²
```

Since the ring's own pressure supplies `+Ea²` exactly, **Kerr is equivalent to
the confinement's own stress second moment vanishing.** Every architecture that
distributes tension between hub and rim eats into it, and the ladder is
computable:

| confinement | `Y/Ea²` | `M₂` as fraction of Kerr |
|---|---|---|
| hoop at the rim | 0 | **1/2** |
| spanning membrane | 1/2 | **3/4** |
| radial spokes | 2/3 | **5/6** |
| (Kerr requires) | 1 | 1 |

The pattern `1 − 1/2n` for `n = 1, 2, 3` is noted and not explained. Simple
single-sign tension structures cannot close the gap — tension must be
transmitted across intermediate radii, and transmission costs second moment.
**Pre-stressed** architectures (self-equilibrated compression + tension, whose
net stress integrates to zero but whose second moment has either sign) can
reach `Y = Ea²` with ordinary positive-energy material. So matching Kerr's
`M₂` is *achievable but not automatic*: it is a one-functional condition on
structure that the model does not yet fix from any principle.

## The extracted constraint — the sharpest product of Stage 2b

Modern amplitude results identify **minimal coupling with Kerr's multipoles**
(the "black holes as elementary particles" line: the minimally-coupled spin-`s`
three-point amplitude reproduces `M_l + iS_l = M(ia)^l`). **[K — search quota
exhausted this session; verify before leaning on it.]** If that holds, the
physical electron sits *at* Kerr, not at the rigid-ring value.

Then gravity is telling us a structural fact about whatever confines the
zitter motion:

> **The electron's confinement mechanism must carry zero stress second
> moment.** Whatever traps the circulating null momentum, its stresses must be
> arranged so that `∫T^kk_conf ρ² = 0` — the pre-stressed case, not the hoop,
> membrane, or spokes.

That is a concrete, falsifiable constraint on an unknown mechanism, extracted
from a quadrupole. It is the first time in this workstream that GR has
*returned* information about the model's missing piece rather than merely
tolerating it.

## How exact Kerr does it: the Israel disk, recovered from scratch

For *all* moments (not just `M₂`), the Appell potential's source is its branch
cut — the disk spanning the ring. Computing the surface density numerically
from the jump `σ = ∂_zΦ|₀₊/2π` and confirming against the closed form:

```
σ(ρ) = −Ma / 2π(a² − ρ²)^{3/2}
```

**Negative everywhere inside**, diverging toward the rim, with a positive rim
ring carrying the balance; interior mass `→ −∞`, rim `→ +∞`, and their moments
sum to exactly `M` and `−Ma²` (verified as a distributional limit). This is
Israel's 1970 Kerr-source disk, re-derived here from the branch cut, and it is
the structure Burinskii builds the Dirac–Kerr electron on **[K]**.

So the exact-Kerr price is a negative-energy interior sheet. For an
electron-scale object that is quantum-vacuum territory (Casimir-type negative
energy densities are physical), which is registered as a direction, not
claimed as a resolution.

## Where this leaves the road to GR

Stage 2 said: at dipole order, gravity reads only `(E, S)` — the guide is
consistent and silent. Stage 2b says: at quadrupole order gravity reads the
**confinement architecture** — and the confinement was already the workstream's
oldest standing gap ("what traps the ray", open since `0001`).

These now converge with the force results (`0011`: the hoop is load-bearing
for the *weight*; here it sets the *quadrupole*): **the confining structure is
not a scaffold to be idealized away; it is where the model's GR content
lives.** Stage 3 (interaction / field equations) should treat the confinement
as the dynamical object, not the photon.

Candidate principle worth registering before anyone computes it: if the
confinement is *itself* gravitational (the geon reading — the trapped photon
bound by its own field, `0001`'s Wheeler thread), then its "stresses" are
field stresses, and the question "what architecture does nature pick?" becomes
"what does the Einstein field equation pick?" — which is exactly a Stage 3
question. **Registered prediction for that calculation, whenever it becomes
tractable: a self-gravitating configuration lands at `Y = Ea²` (the Kerr
value), because the exterior it must match *is* Kerr.** That would close the
loop: the factor 1/2 is the signature of a *material* scaffold, and its
correction to 1 is the signature of gravity doing the confining.

## Next

1. **Stage 3 reframed**: the dynamics of the confinement, not of the photon.
   First tractable piece: linearized self-field stress of the spinning ring —
   does the field's own `T^kk` push `Y` toward `+Ea²`?
2. Verify the two [K] anchors when network returns: minimal-coupling = Kerr
   multipoles; Israel 1970 / Burinskii disk structure.
3. Souriau still queued (gates the interaction formalism, not this line).
