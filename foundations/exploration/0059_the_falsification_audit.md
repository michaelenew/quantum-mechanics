# 0059 — The falsification audit: what the delta is, and whether data kills it

A theory is an interpretation until it is falsifiable. This asks, for
the one place the program looked like it deviated from general
relativity — 0020's ambient screening δ = πw/√(det A₀) — exactly what
the delta is and whether current data already excludes it. The answer
is sharper than expected and **corrects 0058 §3.1**, which listed the
screening law as the program's best modified-gravity prediction. It is
not a prediction of new gravity. Code:
`output/0053_the_falsification_audit.py`.

---

## 1. The one-body sector is exactly Schwarzschild — the delta is zero

0037 measured a perihelion advance exceeding Einstein's 6πM/p by a
factor **1.053** at M/p = 0.011 and **1.021** at M/p = 0.0044, with a
common excess coefficient ~4.8×(M/p), and flagged it as "the
second-order term." That reading is now confirmed exactly.

Integrating the exact Schwarzschild orbit equation

```
(du/dφ)² = 2M (u − u₁)(u₂ − u)(u₃ − u),   u₃ = 1/2M − 2/p
```

on 0037's own orbit (r_p = 0.3, a = 0.6, so e = 0.5, p = 0.45):

| M/p | exact GR ratio | 0037 measured | excess/(M/p) |
|---|---|---|---|
| 0.011 | **1.0532** | 1.053 | 4.84 |
| 0.0044 | **1.0205** | 1.021 | 4.67 |

**The model's "excess over Einstein" is general relativity's own
second-order term.** There is no deviation in the one-body sector at
all. That is not luck: the Kerr–Schild point channel *is*
Schwarzschild (0047's derived channel, 0037's exact nullity at
2e−16), so β = γ = 1 identically and every classical test — bending,
perihelion, redshift — is passed by construction.

This retires a hope and a worry at once. The hope that 0037's excess
was a signature: it wasn't. The worry that it was an integrator
artefact: it wasn't that either.

## 2. So the screening is not a physical varying G — and if it were, it is already dead

Read naively, δ = πw/√(det A₀) with ambient a ≈ 2GM/(rc²) says

```
G_eff = G (1 + 2U)^(−1/2) ≈ G (1 − U),      U = GM/(r c²)
```

— the local coupling runs with the **ambient Newtonian potential**.
That is a definite, testable claim. It is excluded twice over.

**Lunar laser ranging.** Earth's orbital eccentricity e = 0.0167
modulates U_sun by 3.30×10⁻¹⁰ over a year, so the lunar semi-major
axis would breathe by a·ΔG/G = **127 mm** against LLR's ~1 mm
precision — excluded by a factor **127**.

**PPN.** An O(1) shift in β is excluded ~12500× by the LLR Nordtvedt
bound |β−1| < 8×10⁻⁵, and γ by Cassini at 2.3×10⁻⁵.

| ambient | U = Φ/c² |
|---|---|
| Earth surface (own potential) | 7.0×10⁻¹⁰ |
| Sun at Earth's orbit | 9.9×10⁻⁹ |
| Galaxy at the Sun | 5.4×10⁻⁷ |

Combined with §1, the conclusion is forced. The one-body sector is
exactly GR, so there is no room for a physical coupling that runs;
and the naive reading that would use that room is independently dead.
**The screening law is bookkeeping in the w-parameterization, not a
modification of gravity.**

Two internal facts already pointed here and were not joined up:

- 0020 §1 step 5 notes that **constant SPD metrics are flat**. The
  screening's ambient A₀ *is* constant, hence flat — and a flat
  background cannot change a defect's Gauss–Bonnet deficit, which is
  a topological invariant.
- 0012 proved deficits **add exactly** (holonomy rotation d₁ + d₂,
  mass = the abelianization of ISO(2)) — the Deser–Jackiw–'t Hooft
  result. Exact additivity and physical screening cannot both hold.

So δ = πw/√(det A₀) describes how much *coordinate* perturbation w
corresponds to a given physical deficit when the frame is stretched.
That is a real property of the parameterization — and worth keeping —
but it carries no observational content.

## 3. Where falsifiability actually lives: the two-body rule

> **CORRECTED BY 0060.** The binary below is wrong. 0046 identified
> the classical action as S = (1/2κ)∫ε_IJKL e∧e∧F and 0050 verified
> it (torsion rank 24/24, 2 dof, Ricci matched to 1e−6) — that is
> the **Palatini action of general relativity**, so the field
> equations are Einstein's and EIH follows *necessarily*, not as a
> test outcome. **No classical measurement in this program can
> falsify GR, because classically the program is GR.** The question
> with a real failure mode is whether the web's *construction*
> (channels + bond) can generate Einstein's solutions; 0060 runs the
> first piece and validates a pass/fail criterion for the rest. The
> section below is retained as written for the record.

The program's only unfixed dynamical freedom is 0037's measured
O(M₁M₂) violation of the field equation by superposed channels —
coefficient 48.7 / 48.3 / 48.2 over a 4× mass range, a **1.03%**
spread, so the M₁M₂ scaling is clean and the coefficient is a real
number waiting to be explained.

**The theory currently makes no two-body prediction.** 0037 lists the
fix rule as open, with screening only a candidate. That is the whole
falsifiable surface — and it is binary:

- if the fixed two-body rule reproduces **Einstein–Infeld–Hoffmann**,
  the theory equals GR at 1PN and is not falsifiable there;
- if it does not, the mismatch enters at |β−1| ~ O(1), excluded by
  ~10⁴.

There is no third option and **no free parameter to absorb the
difference** — the program's self-containedness, which has been its
aesthetic virtue, is here an experimental liability in the good sense.
One computation decides it.

## Honest limits

- §1 compares against exact Schwarzschild for a *test particle*. It
  establishes the one-body metric is GR; it says nothing about the
  two-body sector, which is §3's business.
- §2's LLR estimate is order-of-magnitude: δa/a ~ ΔG/G is the leading
  response of the lunar orbit to a coupling modulation, not a fitted
  ephemeris. The margin (127×) is large enough that a more careful
  treatment will not reverse the sign of the conclusion, but the
  factor itself should not be quoted precisely.
- §2 refutes the *naive* reading G_eff = G(1−U). A subtler reading in
  which the screening acts only on non-gauge-invariant intermediate
  quantities is exactly what §1 forces, and is not tested here — it is
  argued for by elimination.
- §3's binary is only as sharp as the claim that no free parameter
  exists. The level N and the coupling t are free in the *quantum*
  sector (0057); the classical 1PN sector has none, which is what the
  argument uses.

## Open

1. **The two-body rule vs EIH** — now the single highest-value
   computation in the program, and the only one that can falsify it.
   Fix the O(M₁M₂) correction; integrate a two-body orbit; compare
   periastron advance to the 1PN result.
2. What the coefficient ~48 *is*, in closed form.
3. Whether the quantum sector's free parameters (N, t) can be fixed —
   0057's open 3. A derived t predicts a graviton mass, directly
   bounded by LVK; that is the quantum arc's falsification target.
4. Standing from 0058: closing the correlation gap (`s` as a
   correlation measure) remains the highest-value *structural* item,
   distinct from the highest-value *falsification* item above.
