# 0012 — Stage 2 result: the loop average is exactly Mathisson–Papapetrou

The pre-registered test from `0011` (the road-back plan), run. **Stage 2 comes
back clean.** Per the standing instruction, that means the book chase is not
forced — Souriau remains queued for Stage 3, not blocking.

`output/0011_stage2_loop_vs_mpd.py` — 20/20 checks, 5/5 predictions confirmed,
with one sub-claim falsified en route and kept on the record.

## The setup, in one paragraph

A photon of energy `E` circulates on a ring of radius `r`, confined by a hoop
under tension `τ = E/2πr` (fixed by static equilibrium — and `τ` = energy per
length is exactly the **null-string** condition). Spin `S = Er`. The background
is a *generic* stationary linearized metric: every component of `h_{μν}` an
independent seeded-random polynomial, no symmetry anywhere, both sides of the
comparison computed from the same `h` by the same code — no convention imports
possible. The total force is `dP^i/dt = −∫Γ^i_{αβ}T^{αβ}` (exact at linear
order), compared against MPD's `F^i = −½R^i_{0jk}S^{jk}`.

## The five predictions, and what happened

**P1 — Weight (confirmed).** The photon alone does *not* weigh `E`: it carries
a pressure term `−E(Γ^i_{xx}+Γ^i_{yy})/2` — light couples to spatial curvature.
The hoop tension cancels it pointwise and the system weighs exactly `E`. The
confinement is load-bearing, literally: this is the box-of-light classic
appearing as a force statement, and it is `0005`'s trace result in mechanical
form.

**P2 — MPD coefficient (core confirmed; sub-claim falsified).** I pre-registered
that for cubic `h` the match would be exact and `r`-independent. **The first run
falsified the sub-claim**: the residual scaled exactly as `r` (factor 4.001
between `r = 0.2` and `0.05`). The culprit is real physics I had waved away —
the ring's **mass quadrupole** `⟨ξξT^{00}⟩ = (Er²/2)diag(1,1,0)`, which couples
to `∂∂Γ^i_{00}` and which pole-dipole MPD legitimately omits. With it handled,
the core claim lands at machine precision, **two independent ways**:

- explicit subtraction of the computed quadrupole force
  `F_quad^i = −(Er²/8)∂_i(∂_{xx}+∂_{yy})h_{00}` → diffs `~1e-16`;
- model-free Richardson extrapolation in `r` → diffs `~1e-15`.

> **The `r → 0` loop-averaged force is `−½R^i_{0jk}S^{jk}` with the coefficient
> `−1/2` exact.** The tail-chasing photon ring gravitates as a Mathisson–
> Papapetrou spinning body.

**P3 — Null-string structure (confirmed).** `τ = ε` makes the combined `T^{jk}`
vanish *pointwise*, so the spin force couples solely through the energy-flux
moment `T^{0j}` against `∂Γ^i_{0j}` — purely gravitomagnetic. The random
spatial `h_{ij}` planted in the metric as a distractor drops out of the dipole
entirely, as it must: linearized `R^i_{0jk}` contains only `h_{0μ}` derivatives
in a stationary field.

**P4 — Energy (confirmed).** `dP^0/dt = 0` to `3e-17`. Mechanism worth keeping:
photon and hoop exchange energy *pointwise* (each `f^0 ≈ ±4e-2`), and the
photon's own `h_{00}` coupling dies because `∮∇h_{00}·t̂ dl` is a closed-loop
integral of a gradient.

**P5 — Universality (confirmed, and its failure mode was the finding).** A
flywheel 100× heavier and 100× slower with the *same* `S` feels the identical
dipole force. Its first run also failed — its mass quadrupole is 100× the
photon's and drowned the dipole; subtracting each body's own quadrupole, the
dipole parts agree exactly.

## What Stage 2 establishes

1. **The guide is validated as consistent.** The tail-chasing photon, with its
   confinement treated honestly, is a legitimate relativistic spinning body:
   its gravitational coupling is exactly MPD, with the spin force carried by
   the energy-flux moment — precisely what "mass is trapped momentum" says the
   spin *is*.
2. **Universality cuts both ways.** At pole-dipole order gravity reads only
   `(E, S)`; it cannot see that the spin is trapped light. Clean = consistent =
   silent. The guide's *distinctive* content cannot appear at this order — by
   theorem, not by failure.
3. **The distinguishing observable announced itself.** Both falsified sub-runs
   failed on the same object: the mass quadrupole. At fixed `(E, S)` the light
   ring sits at `r = S/E` and carries `Q_ring = S²/2E` — the **minimum**
   quadrupole of any classical body with that energy and spin (a slow flywheel
   with the same `S` needs `Q = S²/2Ev²` — `1/v²` bigger). Trapped light is the
   *most compact way to carry spin*.

## Stage 2b, pre-registered now

`r = S/E` is exactly the Kerr parameter `a = J/M` — the same half-Compton
radius coincidence Carter's `g = 2` result flagged in `0001`, now arrived at
from force bookkeeping.

> **Prediction (registered before computing):** the trace-free quadrupole of
> the equilibrium light ring matches the Kerr quadrupole `M₂ = −J²/M` in
> magnitude and sign, up to an order-unity factor reflecting ring vs. oblate
> distribution — and the interesting outcome is whether that factor is exactly
> 1. If it is, the tail-chasing photon reproduces the leading external
> multipole structure of the Kerr solution, which is the strongest available
> hint that the guide knows something about GR rather than merely surviving it.

Named hazard, registered alongside: at `S²` order the choice of centroid (spin
supplementary condition) enters the multipole definitions. Any Stage 2b
computation must fix the SSC explicitly before comparing, or the factor is
convention, not physics.

## Method note

Pre-registration caught two wrong sub-claims in one session, both mine, both
recorded in the output file rather than rewritten. Both failures were the same
omission (the quadrupole), and the omission turned out to be the next target.
That is the practice working exactly as intended: the falsifications were more
informative than the confirmations.

## Next

1. **Stage 2b**: ring trace-free quadrupole vs Kerr `M₂`, SSC fixed explicitly,
   prediction above already registered.
2. **Stage 3** (GR itself) still gated on interaction — and on reading Souriau,
   which Stage 2's clean result leaves recommended rather than forced.
