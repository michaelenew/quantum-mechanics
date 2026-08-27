# 0031 — Testing the candidate: the web waves

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0030 ended on one question: what, in a web of information channels,
plays Plebanski's simplicity constraint — the thing that turns
topological bookkeeping into gravity that waves? The named candidate
was the Fisher dressing, inert in 2+1. Tested, at both tiers.
**It passes — the 3+1 web radiates.** Code:
`output/0026_testing_the_candidate.py`.

---

## 1. The instrument

A full 3D Ricci-scalar pipeline (finite-difference Christoffels and
their derivatives, contracted Riemann), validated on exact
geometries: the unit 3-sphere (R = 6 to 10⁻⁵), the global monopole
(closed form, 10⁻⁵), and the straight string (flat off-string to
10⁻⁶ — the codim-2/BF sector behaving as it must).

## 2. Statics: the dressing carries bulk curvature

In 3D, a **point** channel field (u radial from a participant) is a
**global monopole**:

```
R = 2w / ((1+w) r²)      — exact, verified at two radii, two strengths
```

Bulk curvature off-source — something pure BF *cannot* produce (its
curvature lives on defects). The codimension ladder splits the
theory's two sectors cleanly: **strings (codim 2) stay flat
off-source — the topological/BF sector; points (codim 3) fill the
bulk with curvature — the dressing sector.** In three spatial
dimensions the dressing is load-bearing already in statics.

## 3. Dynamics: the web radiates

A string with a traveling transverse wiggle (A sin(kz − Ωt),
retarded nearest-point channels — the same update rule as 0021,
lifted). The far-field Ricci oscillation:

- **A wave zone**: amplitude ~ 1/R^1.03 over R = 2 → 8. The same
  rule in 2+1 gave 1/R^3.07 — near-field only. *The dimension
  itself switched the dressing on.*
- **Frequency-doubled**: the second harmonic dominates the
  fundamental by ×17,714 — the wave oscillates at 2Ω, the
  quadrupole-like doubling familiar from GR's binary radiation.
- **Outgoing at c**: radial phase advance 3.968 vs the outgoing
  prediction 2Ω·ΔR = 4.000 (0.8%). The instantaneous control fails
  the phase test outright (1.498 — no outgoing structure) and is
  10.7× weaker: what propagates is retardation-made, genuinely
  radiated, not a translating near-zone pattern.

## The verdict, and the reframed frontier

**The candidate passes the existence tier.** The Fisher dressing —
inert decoration in 2+1 (screening + a static quadrupole halo) — is
load-bearing in 3+1: statically (monopole bulk curvature) and
dynamically (outgoing curvature waves). The web did not need the
simplicity constraint *imposed* to acquire local degrees of freedom;
three spatial dimensions gave its slaved geometry room to propagate.
The 2+1 no-radiation result (0023) was correct dimensional physics,
not a structural defect.

The obstruction therefore reframes, favorably: no longer "does the
web have wave dynamics at all" but **which wave theory is it** —
does the wave sector match Plebanski-constrained BF (Einstein
gravity: two transverse-traceless polarizations, the quadrupole
formula's coefficients), or is it a different consistent wave
theory? Correspondence, with waves in hand, is a much better
frontier than existence.

## Honest limits

- The wave measurements use the Ricci scalar of the *spatial* slice
  at one field direction and one wiggle family (luminal, Ω = k);
  polarization decomposition (TT projection, the h₊/h₊ count) and
  the quadrupole-formula coefficient are not extracted.
- "Nearest retarded point" is one lift of the channel rule to
  extended sources; smooth alternatives (integrated channels) could
  shift coefficients, though the phase/decay structure is
  kinematically robust.
- The static monopole law is exact; its registration (a codim-3
  "particle" in 3D is not a BF object — what matter it corresponds
  to in the movie formalism) is open.

## Open

1. **Correspondence**: extract polarizations (TT projection of the
   wave field around the string) and the radiated power's scaling
   (quadrupole formula) — the direct test against linearized GR.
2. **The wave equation**: derive the dressing's effective field
   equation in 3D (the analog of 0020's divergence identity, one
   dimension up) — if it is the linearized Einstein equation on the
   constraint surface, the simplicity question closes analytically.
3. **The monopole's role**: whether codim-3 point participants are
   physical in the 3+1 web (the movie formalism's punctures) or
   forbidden (strings only), and what the bulk-curvature cloud
   means informationally.
