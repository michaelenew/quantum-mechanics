# 0014 — Self-gravity result: the march to Kerr, and the geon numbers

The Stage 3 first piece registered in `0013`, run.
`output/0013_selfgravity_and_geon.py`, 11/11 checks. One registered
justification withdrawn before computing, one registered sub-prediction
falsified by the run — both on the record. The headline result stands.

## The audit first (R1)

`0013` registered: "a self-gravitating confinement lands at `Y = Ea²` because
the exterior it must match is Kerr." **That justification was wrong and is
withdrawn**: there is no Birkhoff theorem for rotation. Rotating material
sources generically have non-Kerr exteriors — neutron stars carry
`M₂ = −q·J²/M` with `q ≈ 2–10`, not 1 **[K]**. Caught before computing, which
is the pre-registration practice doing its job on my own reasoning.

The corrected mechanism needs no exterior theorem, and it is better:

> **Material tension is the only agent that subtracts stress second moment.**
> With gravity supplying fraction `f` of the confinement, the hoop tension
> scales as `(1−f)`, so `Y(f) = f·Ea²` and `M₂(f) = −(1+f)Ea²/2` — a linear
> march from the hoop's half-Kerr at `f = 0` to **exactly Kerr at `f = 1`**,
> because full self-confinement removes the tension and the ring's own null
> pressure supplies `+Ea²` by itself.

The registered question — does self-gravity push `Y` toward Kerr — comes back
**yes, at leading order**, by force-balance bookkeeping. Endpoint caveat kept
prominent: at `f = 1` the compactness `GE/a ≈ 0.59` is not small; second-order
field stresses are uncontrolled there, and the neutron-star `q ≠ 1` fact says
they generically shift the endpoint. Leading order only.

## The self-force: two routes, one number, no cutoff

The hand-derived kernel (registered in the header before running) reduces the
null ring's gravitational self-force per unit length to

```
f_inward = (2Gσ²/a)∮[2sin(ψ/2) − sin³(ψ/2)]dψ = (32/3)·Gσ²/a,   σ = E/2πa
```

An independent first-principles route — component-wise
`∂h̄_{μν} → trace reversal → Γ → f` — reproduces it to 8 digits, with the
tangential component zero to `1e-17`.

**Finding 1: the null ring's gravitational self-interaction is finite in the
thin limit, with no thickness cutoff.** Neighbouring elements are parallel
null movers, and parallel null rays do not interact
(Tolman–Ehrenfest–Podolsky), so the coincidence singularity is suppressed.
The contrast is computed side by side: the *static* massive ring's self-force
grows as `ln(1/δ)` without bound, while the null ring is `δ`-independent.

> **Nullness regularizes.** A material ring needs a thickness; a null ring
> does not. This is a structural virtue of the trapped-light picture that the
> workstream had not noticed before: the model's self-energy problem is milder
> than a charged-shell electron's, for a reason specific to its null premise.

**Falsification en route (R3c):** the registered sector decomposition
`1 : −2 : 1` (from the interaction-energy contraction `(l'·l)² = 1−2c+c²`) is
wrong for the *force* — measured slopes are `1 : +2 : −3`. The force adds the
momentum-flux term `(l·∂)(h_{iβ}l^β)` to the coupling gradient, and it
redistributes the sectors. What survives is the physics: each sector diverges
logarithmically and **the sum cancels exactly** (to `3e-3` relative). The
apportionment was guessed wrong and is now measured.

## The geon numbers

```
confinement fraction   f = (16/3π)·GE/a ≈ 1.698·GE/a
geon condition f = 1:  a* = (16/3π)·GE ≈ 1.70 GE
extremal Kerr:         a  = GM
```

**Finding 2: the linearized geon sits at the extremal-Kerr scale times
`16/3π ≈ 1.70`.** Order unity, not 1 — and at that point `GE/a* ≈ 0.59`, so
the number is a leading-order estimate of a strong-field quantity. What it
honestly supports: a fully self-confined null ring is a Planck-compactness
object sitting near the extremality relation, which is the geon picture's
natural home.

## The electron is not a geon (R5)

```
a/GE = (m_Planck/m_e)²/2 ≈ 2.85×10⁴⁴        f_electron ≈ 3.5×10⁻⁴⁵
```

Gravity supplies ~`10⁻⁴⁴` of the electron's needed confinement. **The geon
reading cannot confine the electron**, by 44 orders of magnitude. Consequences
assembled across the workstream:

- The `0013` constraint (zero stress second moment, if minimal coupling = Kerr
  [K]) must be met by **non-gravitational** structure.
- The electron as a Kerr-type object is *super-extremal* (`a ≫ GM`, no
  horizon) — consistent with the Kerr–Newman electron reading (`0001`), and
  the reason the minimal-coupling=Kerr statement lives in amplitude-land
  rather than in horizon physics.
- Self-confinement by gravity is a statement about Planck-scale objects. For
  the electron, "what confines the ray" remains open and is now sharply
  constrained: non-gravitational, pre-stressed, vanishing stress second
  moment.

## Where the GR road now stands

| stage | status |
|---|---|
| SR from the null loop | done (`0001`–`0003`) |
| MPD force from the loop average | done, coefficient −1/2 exact (`0012` note / `output/0011`) |
| Kerr quadrupole | ring is half; confinement carries the rest (`0013`) |
| self-gravity direction | **confirmed at leading order: full self-confinement lands exactly on Kerr's `M₂`** (this note) |
| the honest wall | strong-field endpoint (`f → 1` corrections) and true interaction — Souriau still gates the latter |

The pattern across Stages 2–3 is consistent and worth stating once: **gravity
sees the trapped-light model exactly as it sees any spinning body at low
multipole order, and starts distinguishing it precisely where the model's own
unknown — the confinement — becomes the dynamical object.** Every GR probe so
far has converted "what confines the ray" from a philosophical gap into a
quantitative constraint: load-bearing for the weight (`0012`n/`output/0011`),
zero stress second moment for Kerr (`0013`), non-gravitational for the
electron (this note), finite self-energy in the null limit (this note).

## Next

1. **The strong-field endpoint**: does `f → 1` stay at Kerr beyond leading
   order? The Neugebauer–Meinel disc → extreme Kerr result [K] is the anchor
   to check against when the literature is reachable; a 1PN iteration of the
   present computation is the tractable next rung.
2. **Souriau** — still gates the interaction formalism (Stage 3 proper).
3. The `16/3π` coefficient: is it stable under ring→torus thickening?
   (The finiteness result suggests yes; verify.)
