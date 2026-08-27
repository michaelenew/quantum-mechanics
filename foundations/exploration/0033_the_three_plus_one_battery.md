# 0033 — The 3+1 battery: parity, and three exact laws for free

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

The instruction: round out the theory while bringing the 3+1
computational battery to parity with 2+1. This exploration builds
the missing native-3D instruments — and each one, switched on,
immediately returned an exact law. Code:
`output/0028_the_three_plus_one_battery.py`.

---

## 1. The charge reader: `develop_loop3`

The 2+1 program's workhorse was `develop_loop` (0025): the affine
holonomy of a loop, whose rotation part is mass and translation part
is momentum/moment. The 3D version — parallel-transport an
orthonormal frame, develop the tangent — reads, around a string:

- **rotation angle = the exact 2D atom** δ(w) = 2π(1−(1+w)^(−1/2))
  to 1e−5;
- **rotation axis = the string's direction** — the monodromy carries
  the orientation as well as the charge;
- **translation = the 2D moment law verbatim**:
  |T| = 2sin(δ/2)·(proper distance), 0.01%;
- loops that do not link the string (beside it, or in a
  perpendicular plane) develop to the **identity**.

Charge = linking at the *geometric* tier — the same statement the
quantum algebra made operatorially in 0030, now measured with a
frame and a loop of string.

## 2. The atom's codimension ladder

A point participant in 3D carries a **solid-angle deficit**, exact
and shell-independent (measured at two radii, 1e−5):

```
Ω = 4π/(1+w)        ΔΩ/4π = w/(1+w)
```

Set beside the 2D atom, this is **one law**:

> **deficit fraction of a codimension-c source = 1 − (1+w)^(−(c−1)/2)**

| source | codim | deficit fraction |
|---|---|---|
| 2D point / 3D string | 2 | 1 − (1+w)^(−1/2) — the atom |
| 3D point | 3 | 1 − (1+w)^(−1) — the monopole |

The ½-exponent ladder is the square-root ledger again: each extra
transverse dimension multiplies the screening by another
(1+w)^(−1/2) — the loop tier's det^(−1/2), stacked once per
codimension step.

## 3. Momentum, read natively

Displacing the string leaves the rotation charge invariant (mass,
0.77247 at all three positions) while the translation holonomy
drifts at exactly **2sin(δ/2)√(1+w)** per unit displacement — the
0025 momentum law, lifted verbatim to the transverse plane and read
by the 3D instrument (0.01%).

## 4. Additivity and screening

Two parallel strings through one loop: total rotation = **0.862 of
the naive sum** 2δ. The constant-ambient estimate from the
inclination law (each string in the other's parallel ambient,
f(0) = (1+w)^(−1/2)) gives 0.897; the residual is the
finite-separation nonuniform ambient. Charges add, screened — the
holonomy reader sees the same mutual screening the field-level law
predicts.

## 5. The parity census

Every 2+1 instrument now has a 3+1 counterpart or is
dimension-generic: metric-from-channels (generic), atom/deficit
(`develop_loop3` + ladder), charge reader (+ axis = orientation),
Gauss law (shell-independent solid angle + monopole closed form),
retarded web (`string_wave_metric`, any string shape), cone
(dimension-blind), Lorentz/Wigner (transverse lift + generic
polar), harmonic analyzer (shared), curvature (Ricci pipeline),
polarization decomposer (3D-native), BF lattice (2-form), quantum
deformation (intersection → linking).

**The one instrument with no target**: nothing measures a dynamical
strength sector — because none exists yet. That is 0032's verdict
seen from the toolbox side: the next step is a construction, not a
tool.

## Honest limits

- `develop_loop3` uses Euler transport at 4000 steps with
  finite-difference Christoffels; accuracy measured at 1e−5 on the
  known laws, not proven.
- The additivity check is one configuration; the constant-ambient
  estimate is a ballpark, not a derived finite-separation law.
- The codimension-ladder law is verified at c = 2, 3 — the general-c
  statement is a closed-form conjecture from two data points plus
  the ledger pattern (a codim-4 check would need 4 spatial
  dimensions).

## Open

1. **The strength dynamics** (carried from 0032): the only missing
   construction; once written, the battery measures it immediately
   (polarization decomposer + charge reader).
2. **Boosted-string charges**: read mass/momentum of a *moving*
   string with `develop_loop3` under the Lorentz completion's
   mmᵀ + boosted baseline, checking the charge calculus is
   boost-covariant in 3D.
3. **The ladder at general c**: derive 1 − (1+w)^(−(c−1)/2) from
   the constant-ambient integral in arbitrary codimension.
