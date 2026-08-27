# 0017 — The extremality result does not survive the invariant redo

> **AI-generated, not peer-reviewed.** Prior art credited in [`ATTRIBUTION.md`](../../ATTRIBUTION.md) — results are re-derivations of
> established work unless explicitly marked otherwise.

`0016` flagged its own strongest new claim as resting on a Boyer–Lindquist
degeneracy and named the redo as the top next task. Done here, without needing
Souriau. **The claim fails.** `output/0016_extremality_invariant_redo.py`,
22/22 checks, 5 predictions registered and 5 confirmed — P3 being the
falsification of `0016`'s headline.

## The degeneracy is worse than "a caveat"

At extremal Kerr the horizon and the prograde photon orbit sit at the same
BL `r = M` **and at the same circumferential radius `2M`.** Neither the
coordinate nor the circumference distinguishes them. Only proper radial
distance does, and it diverges logarithmically:

| from `r` | proper distance to `3M` |
|---|---|
| `1.01 M` | 7.29 |
| `1.0001 M` | 11.90 |
| `1.000001 M` | 15.75 |

So comparing BL `r` values at extremality compares nothing physical. `0016`'s
`R = r_ph` was an equation between a coordinate label and an asymptotic
invariant.

## The invariant statement, and its failure

The coordinate-independent "size" of a circular photon orbit is its **impact
parameter** `b = L/E`, not any radius. Deriving the equatorial Kerr null
circular orbits from `R(r) = R'(r) = 0`:

```
R' = 0  ⟹  b² = a² + 3r²
R  = 0  ⟹  (b − a)² = r³/M
      ⟹  u³ − 3Mu ± 2a√M = 0   (u = √r),    b = a ± r^{3/2}/√M
```

Verified against all three known values — `b = 3√3 M` at `a = 0`, `b = 2M` for
extremal prograde, and `r = 4M`, `b = −7M` for extremal retrograde — plus an
independent closed-form cross-check `r/M = 2[1 + cos((2/3)arccos(−a/M))]`
agreeing to 8 digits.

Now the physics. Each constituent photon carries `L/E = b`, so `J = b·ΣE`; with
`M = ΣE` the generated Kerr parameter is `a = J/M = b`. **Both `a` and `b` are
invariants**, so `a = b` is the honest form of `0016`'s `R = r_ph`. But

```
b_ph − a = r^{3/2}/√M  >  0   for every r > 0
```

| `a/M` | `b_ph/M` | gap |
|---|---|---|
| 0.00 | 5.196 | 5.196 |
| 0.50 | 4.096 | 3.596 |
| 1.00 | 2.000 | 1.000 |

**The gap never closes.** The only root is the trivial `r = 0`. `0016`'s P5 is
falsified, and with it that note's claim to have answered `0014`'s strong-field
endpoint — **that endpoint is open again.**

### It fails a second, independent way

A ring on the extremal prograde orbit has `b = 2M`, so it would generate
`a = 2M`: **super-extremal.** And super-extremal Kerr has no circular photon
orbit at all — the cubic's local minimum is `2√M(a − M)`, positive for `a > M`,
so no positive root exists. The configuration is inconsistent both in the
fixed-point equation and in the regime that equation would land it in.

### Robust to the obvious objection

`M = ΣE` ignores gravitational binding. Restoring it, `M < ΣE`, so with
`k = ΣE/M > 1` the generated spin is `a = kb > b` — moving *further above* `b`
while consistency needs `b_ph(a) = b` and `b_ph(a) > a`. **Binding energy makes
the inconsistency worse**, so the negative result does not hinge on
test-particle mass bookkeeping.

## What survives

Unaffected, because none of it depended on the extremality claim:

- `0011` — MPD force at coefficient `−1/2` (external field, exact)
- `0013` — the ring is half of Kerr; `M₂` reads the confinement
- `0014` — null-ring self-force is finite; the electron is not a geon
- `0015` — the all-tension bound, fraction ∈ [1/2, 5/6]
- `0016` P1–P4 — link-1 verification, the spin-½ quadrupole vanishing
  identically, and confinement-as-geometry

**The geodesic-confinement mechanism survives intact.** It says a closed null
geodesic needs no matter stress, hence `Y_conf = 0` and `M₂ = −Ea²`. What is
falsified is only the further claim that a *self-generated* Kerr geometry can
supply such an orbit to its own source.

## The remaining gap, stated honestly

This analysis treats each photon as a **test particle in the total field**,
which double-counts its own contribution. A ring element should move in the
field of the *others* only. `0014` established that the null-ring self-field is
finite (parallel null neighbours don't interact), so the correction is
well-defined and bounded — but it is not computed here, and it is O(1) in
exactly this regime.

> **Status of self-confinement: unresolved, not refuted.** The mean-field
> version is dead; the self-field-corrected version is untried.

## Method

Two bugs caught by the checks, both recorded rather than quietly fixed:

1. `photon_r` bracketed `(0, √3M]`, which has roots at *both* endpoints when
   `a = 0`, and converged to the spurious `u = 0` — returning `r = 0` at `a = 0`
   and `r = 3M` at extremality, i.e. exactly inverted. Caught because the known
   values (`3√3M`, `2M`, `−7M`) were in the table as an explicit column. Fixed
   by bracketing `[√M, √3M]` where `f` is monotone, plus a closed-form
   cross-check.
2. The same run's P1 table showed the photon orbit at `r = 3M` for extremal
   Kerr, which is visibly wrong and was the first symptom.

The lesson is the one from `0015`, reinforced: **put known values in the output
as a column, not in a comment.** Both bugs were caught by a printed comparison,
not by a passing assertion.

Pre-registration tally for the session now: six rungs, five of which falsified
something, and three of the falsifications were of my own headline claims from
the immediately preceding rung.

## Next (none of it needs the book)

1. **Self-field-corrected confinement** — the actual open question. `0014`'s
   finite null self-force is the input; the object is a ring element moving in
   the field of the rest of the ring.
2. `0015` P4's self-consistency fixed point (confinement energy shifting
   `a = S/E`) — now more interesting, since the geodesic case has *zero*
   confinement energy.
3. Charge quantisation as a winding number (`0006`), untouched.
