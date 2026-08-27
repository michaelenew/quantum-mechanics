# 0024 — Velocity-dependent channels: the three completions

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0023 diagnosed the compass and prescribed velocity-coupled channel
data. Here the prescription is executed: the completion family is
*built*, not proposed, and measured on the same instruments that
convicted the bare model. The result is a three-position dial —
ether, Galileo, Lorentz — realized as three update rules on one web,
plus a theorem-shaped necessity result about the baseline. Code:
`output/0019_velocity_dependent_channels.py`.

---

## 1. The Galilean pole: extrapolated channels

Channels point at the **extrapolated present position** — retarded
position + retarded velocity × delay. This is causal (retarded data
only), and for uniform motion it reproduces the static field as an
exact identity: compass dead, δ(v) = δ(0), moving systems literally
indistinguishable. The relativity principle, Galileo's way.

The important check: **the causal cone survives extrapolation.** On
the kicked worldline, the extrapolated field still updates only
inside r = ct (K = 0 beyond the front to 10⁻⁶; K = 1.19 just
inside). Prediction is not prescience: extrapolating from stale data
is wrong exactly until the news arrives. So this pole delivers
Galilean relativity *with* a light cone — and no velocity structure
anywhere in the field.

## 2. The Lorentz pole: the boosted solution, baseline included

The isometric boost of the static solution, in closed form:

```
channel:   w · m mᵀ / (γ²X² + Y²),   m = (γ²X, Y)
baseline:  I  →  I + (γ² − 1) v̂ v̂ᵀ
```

— anisotropic channel *strength* (the 2D Liénard–Wiechert profile
that |u| = 1 used to forbid), direction along (γ²X, Y), **and the
baseline transformed**. Measured:

- **Atom speed-invariant**: 0.772419/0.772427/0.772437 at
  v = 0.3/0.6/0.8 against static 0.772467 (equal to numerical
  tolerance; exact by construction).
- **No fan**: off-apex K ~ 10⁻⁸ at every speed. 0021's curvature
  fan was the *ether rule's artifact*, not a property of moving
  mass.
- **Compass dead at all orders**: co-moving pair orientation spread
  2.8×10⁻⁷ (floor), with the screened ratio equal to the static
  pair's 0.818509 exactly.

The moving system is globally isometric to the static one: the
relativity principle holds exactly, with nontrivial velocity
structure carried in strength + baseline.

## 3. The baseline is not optional

Drop the baseline boost — keep ambient I, boost only the channels:

```
solo atom drift from static:        24.5%
co-moving orientation spread:       6.5 × 10⁻²
```

The compass comes back *worse than the bare model's*. **Channel
velocity-coupling alone cannot restore covariance: the node's own
baseline — the self-channel, the h₀₀ sector — must transform with
the boost.** This is 0023's missing-sector diagnosis landing on a
specific constructed object: Lorentz structure requires the
baseline (proper-time) sector to be dynamical. In spacetime terms:
the ambient γ² factor is exactly what a Lorentzian background
metric η would absorb into the slice geometry — the Euclidean model
must carry it by hand, which is one more way of saying where the
minus sign lives.

## 4. The dial, assembled

One web, three update rules, same causal cone (w = 0.3, v = 0.6):

| rule | atom | off-apex K | compass |
|---|---|---|---|
| ether (bare retarded) | 0.4749 = πw-tier (1−v²) | −0.182 (fan) | v²cos2ψ + dipole |
| Galileo (extrapolated) | 0.7724 = static | 0 | none |
| Lorentz (boosted) | 0.7724 = static | 0 | none |

Three standing conclusions:

1. **Causality never chooses the symmetry.** All three rules share
   the derived c-cone (0022); the ether/Galileo/Lorentz choice is
   made entirely by the update rule's velocity coupling.
2. **The relativity principle is available in two flavors** —
   trivially (Galileo: no velocity structure) or nontrivially
   (Lorentz: anisotropic strength + dynamical baseline). The bare
   retarded rule is the one option that *fails* it, and its
   signature law δ = πw(1−v²) and fan are the price of the failure.
3. **What distinguishes Lorentz from Galileo inside the model is
   composition**, not single-boost experiments — two successive
   boosts (velocity addition, aberration chains, Wigner-rotation
   analogs) are where the two poles must diverge. That is the
   flagged next experiment, and it is the model-internal version of
   "why is the world Lorentzian rather than Galilean" — which is no
   longer a signature question but a symmetry-selection one.

## Honest limits

- Both completions are constructed for uniform (common-velocity)
  systems in closed form; mixed-velocity webs (the flyby with
  velocity-dependent channels) need a superposition prescription
  for the baseline — the model-building frontier.
- The Lorentz pole is verified isometric operationally (atoms,
  curvature, pair ratios); "all orders" refers to these instruments,
  exact by the construction's logic.
- The Galilean pole's front test uses the kicked worldline; the
  claim "extrapolation is causal" is general, but only this
  worldline was measured.
- Nothing here yet derives *which* pole the postulates prefer;
  P1/P2 gave the cone, not the symmetry.

## Open

1. **The composition experiment**: two successive boosts on the
   Lorentz and Galileo poles — measure velocity addition and the
   Wigner-rotation analog; find the model-internal discriminator.
2. **Mixed velocities**: the baseline prescription for sources in
   relative motion (the true two-body problem at the Lorentz pole);
   whether the flyby coupling of 0023 survives, transforms, or
   vanishes there.
3. **Deriving the pole**: is there a web-native principle (channel
   symmetry, information bound, consistency of the movie's event
   composition) that selects the Lorentz rule — making the
   signature *and* the symmetry both theorems?
4. **The spacetime packaging**: promote the constructed baseline
   transformation to an honest 2+1 object (η + h_μν) and check the
   linearized-GR correspondence of the full completed model.
