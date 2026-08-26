# 0150 — κ = 16 is a Wilson β, and asymptotic freedom turns it into 10¹⁸

> **AI-generated, not peer-reviewed.** Code: `output/0141_the_scale.py`.
> Depends on: 0142 (κ derived), item 5 (ℓ_P = 0.507a), 0149 (the null
> this explains).

## κ is a Wilson β — measured, not asserted

Wilson's action is `S = β(1 − cos θ) ≈ βθ²/2`, so β *is* the quadratic
coefficient of the plaquette action at the identity. Read it off the
derived weight instead of assuming the identification:

| quantity | value |
|---|---|
| ∂²S/∂θ₊² | **16.0001** |
| ∂²S/∂θ₋² | **16.0001** |
| ∂²S/∂θ₊∂θ₋ | **−0.0000** |
| closed form (2/3)·Σn²(n²−1)/Σn² | **16.0000** |

> The derived weight is, to quadratic order, **two independent SU(2)
> Wilson actions at β = κ = 16.000**. The cross term vanishes: the two
> records do not mix in the *coupling*. They mix only in the
> *observable* — which is exactly 0142's result that the graviton is
> the synergy, 5 of 9, spread 1.0000 given either stream alone and
> 0.0000 given both.

Second, independent handle: weak-coupling SU(2) has
`⟨½ tr U_p⟩ = 1 − 3/(4β)`. The measured spatial plaquette is
**0.957234**, giving **β_eff = 17.54**. The gap from 16.00 is the
higher-character part of the weight, and it is the honest error band.

## The scale

Two-loop, `aΛ_L = (b₀g²)^{−b₁/2b₀²} exp(−1/(2b₀g²))`, `g² = 4/β`,
`b₀ = 11/24π² = 0.046439`, `b₁ = 17/96π⁴ = 1.8179e−3`:

| β | source | aΛ_L | **ξ/a** |
|---|---|---|---|
| 16.00 | weight curvature | 1.293e−18 | **7.73e+17** |
| 17.54 | measured plaquette | 2.145e−20 | **4.66e+19** |

The lattice spacing is this program's Planck length (item 5:
ℓ_P = 0.507a). So the theory's confinement scale sits **10¹⁸–10²⁰
Planck lengths out**, i.e. a mass of order **10⁻²⁰–10⁻¹⁸ M_Planck**.

For reference, `M_Planck / 1 GeV = 1.22e+19`.

**Nothing here was tuned to that.** κ is fixed by the band (M = 6
characters) and the double copy; the rest is one- and two-loop
asymptotic freedom, which was already in the program.

## The sensitivity, before anyone quotes a digit

`d ln(aΛ)/dβ = 2.69`, so **one unit of β is a factor 15 in the scale.**
The two handles on β differ by 1.5, which is the entire spread above.

> **The order (10¹⁷–10¹⁹) is robust. The digit is not.** This is a
> two-decade band, not a measurement, and there is a further scheme
> ambiguity (Λ_lattice vs Λ_MS̄) of order 20 sitting on top of it that
> is not included.

Anyone who wants this sharper has a concrete job: pin β
non-perturbatively rather than by these two proxies.

## Why this matters more than the null it explains

Three things land at once.

**1. It explains item 2 completely.** An 8⁴ box is 10⁻¹⁷ of a
correlation length. The spin-2 null (0149) was the *expected* result
and was predictable from the plaquette alone, without running a single
correlator. Three estimator diagnoses bought 24× against a deficit of
10¹⁸.

**2. It is the "why is gravity weak" answer in this program.** The
coupling is not chosen — it is **derived**, κ = 16, from the band and
the double copy. Asymptotic freedom then exponentiates a derived O(10)
number into a derived O(10¹⁸) hierarchy. Weakness is not put in; it
comes out of dimensional transmutation applied to a coupling the
program had no freedom to pick.

**3. It is the first quantity here that is both derived and large.**
Against 0069's bar the derived-knob count has been **zero** for the
whole program. This is the first candidate. It is *not* yet a knob at
the bar's standard — a two-decade band is not a prediction — but it is
the first thing with a prediction's shape, and the path to sharpening
it is ordinary lattice work rather than new theory.

## What this does not claim

- Not that Λ_QCD has been derived. This is pure-gauge SU(2)×SU(2),
  not QCD, and the number is a confinement scale for *this* theory.
- Not that a graviton has been found. 0149 measured a null and this
  explains why the null was uninformative — that is not evidence for
  the pole, it is removal of evidence against it.
- Not a sharp number. See the sensitivity section; two decades.

## Next

The scaling window is now the whole game, and it is a different
computation from the one item 2 assumed: not a bigger box at this
coupling — no reachable box helps at ξ/a ~ 10¹⁸ — but the *response*
route (item 4), where G is a response rather than a fluctuation
(lucid 0047), and where the Planck-scale lattice is an advantage
rather than an obstruction.
