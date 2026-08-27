# 0162 — The obstruction is the carrier, not the theory and not the scale

> **⚠️ SUPERSEDED by 0163.** The claim that 'a fixed grid has no infinitesimal diffeomorphisms', and hence that the carrier is the blocker (R4′), over-generalises from the induced kernel to every construction on the same grid. It is false: 0152 measures the **constrained** sector's diffeomorphism violation on the *same* hypercubic lattice as an O(a²) artifact — (k̂²)^{+1.12}, and machine zero for a large class of momenta — against the induced kernel's 0.30, flat in k. **R4′ is retired.** The measurements here about the induced kernel stand.

> **AI-generated, not peer-reviewed.** Code: `output/0151_the_carrier.py`.
> Corrects 0161's R4 claim.
> Prior art credited in [`ATTRIBUTION.md`](../ATTRIBUTION.md).

"How can we derive something that then can't be simulated?" — the
right question, and the answer is that **it can be**, just not on the
carrier we have been using.

## First, 0161 was wrong about the scale

0161 said ξ/a ≈ 10²⁰ blocks a simulation of gravitational dynamics.
**Item 4 is the counterexample.** The static metric response was
measured cleanly at that same coupling — 1/r to **1.68% across a
factor 15 in r** (0143). A background-field response is not a
bound-state correlator and does not need the correlation length.

> The scale killed item 2, which wanted a **pole**. It does not kill a
> **response**, and a geodesic is built from responses.

## What actually blocks it

0150 measured the obstruction without naming it. Trace what the
violating kernel is built from:

    O.hessian(vh, k, L)  ←  vh = O.vhat(L)  ←  v_μ(q) = e^{iq_μ} − 1

That is the **flat lattice**. No link variables, no weight W, no κ, no
Spin(4). It is the free scalar determinant on a hypercubic grid — a
quantity identical in *any* program that used the same grid.

> **The 0.30 diffeomorphism violation contains nothing from this
> theory. It is a property of the carrier.**

### Is it the discretisation?

If the breaking were a discretisation artifact, changing the
derivative would move it:

| derivative | k=(0,1,0,0) | k=(0,2,1,1) |
|---|---|---|
| forward | 0.3020 | 0.3506 |
| central | 0.3139 | 0.3058 |
| improved | 0.2997 | 0.3420 |

**Unmoved.** Combined with 0150's finding that it is flat in k
(exponent +0.029 where an O(a²) artifact needs +1):

> It is structural. **A fixed grid has no infinitesimal
> diffeomorphisms.** There is no symmetry there to be invariant under.

## Why that is fatal *to the derivation's engine*

0150 s1 proved the derivation runs on invariance: the general local
two-derivative quadratic form that annihilates gauge modes is
**unique**, and it is (1, −1, −2, 2) — linearised Einstein-Hilbert,
momentum-independent to 3.77e−15.

So the regulator destroys exactly the symmetry that forces the answer.
With nothing protecting it, a cosmological constant and a graviton
mass appear at the cutoff — and 0159 found both, at rank(B) = 4(V−1)
exactly and ‖H₀‖/‖H₂‖ ≈ 21.6. γ = −1 → +0.509 (vDVZ) is the whole
visible consequence.

## The situation, correctly stated

> Not "derived but unsimulable". **Derived, and simulated so far on a
> carrier that breaks the symmetry the derivation runs on.**

And the program's own amplitude names the carrier it wants. The
derived weight

    A(U⁺,U⁻) = Σ_j n_j χ_j(U⁺) χ_j(U⁻)

is a sum over **balanced** representations — a spin foam amplitude
with simplicity imposed (0160 s3: weight-table rank 6 not 1; 0142's
synergy). Spin foams live on simplicial 2-complexes where the
representation labels **are** the geometry: j is an area. Nothing is
frozen, and there is no background metric to break diffeomorphisms
against.

The hypercubic lattice was the right instrument for everything through
item 5 — it produced κ = 16.0001, the band limit, the double copy, the
synergy, and the scale. **It is the wrong instrument for a geodesic**,
and s2 says so quantitatively rather than as a matter of taste.

## Revised remaining list

| | | state |
|---|---|---|
| R1 | 0160 residual — diffeo test on the constrained-BF kernel | one run |
| R2 | source in the constrained sector | not started |
| R3 | response in the constrained sector | not started — and **not scale-blocked** |
| **R4′** | **a carrier with dynamical geometry** (simplicial / spin-foam) | **the real blocker** |
| R5 | nonlinearity — second order | not started |
| R6 | Lorentzian real time | not started |
| R7 | matter content, no spinors | half |

R4 as written in 0161 ("the scale") is retired. R4′ replaces it, and
unlike a scale separation it is a **build**, not an impossibility.
