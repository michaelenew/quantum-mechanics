# 0060 — Does the web's construction solve Einstein at second order?

The measurement 0059 pointed at, run — plus a correction to how 0059
framed it. Code: `output/0054_the_second_order_test.py`.

---

## 0. The correction first: there is no classical falsifier of GR here

0059 §3 called the two-body rule a binary against
Einstein–Infeld–Hoffmann: reproduce EIH and the theory equals GR at
1PN, miss and |β−1| ~ O(1) is excluded by 10⁴. **That framing was
wrong, and it was wrong because I did not check what the action
already fixes.**

0046 identified the classical functional as
S = (1/2κ)∫ε_IJKL e∧e∧F, and 0050 *verified* it: the torsion equation
has rank 24 of 24 (ω algebraic in e, so the theory is second-order in
e alone), the dof count is 2, and the Palatini route reproduces the
metric route's Ricci to 1e−6 on three non-vacuum profiles.

**That is the Palatini action of general relativity.** If the action
is GR's, the field equations are Einstein's, and the two-body
dynamics is EIH *necessarily* — not as a test outcome but as a
consequence. There is no binary, and **no classical measurement in
this program can falsify general relativity**, because classically
the program *is* general relativity.

The question that does have a real failure mode is a different one:

> **Can the web's construction — superposed channels, plus the bond —
> actually generate Einstein's solutions?**

That is a question about the construction's expressive power, not
about GR, and it can fail. This document measures the first piece of
it.

## 1. The diagnostic, validated

The criterion: if a trial metric is correct at first order but has no
second-order term, its off-source residual max|R_μν| scales as M².
Supply the *correct* second-order term and the leading residual
becomes O(M³). So the log-log slope of residual against mass reads
out whether h² is right — provided the diagnostic actually works.

Validated on harmonic-coordinate Schwarzschild, where every order is
known in closed form:

```
g₀₀ = −(r−m)/(r+m),  g_ij = ((r+m)/r)² δ_ij + m²(r+m)/(r²(r−m)) n_i n_j
```

| M | 1st-order trunc. | 2nd-order trunc. | exact |
|---|---|---|---|
| 0.0200 | 3.469e−2 | 9.528e−4 | 2.761e−6 |
| 0.0100 | 8.809e−3 | 1.267e−4 | 1.387e−6 |
| 0.0050 | 2.224e−3 | 1.677e−5 | 6.949e−7 |
| 0.0025 | 5.589e−4 | 2.382e−6 | 3.481e−7 |
| **slope** | **1.985** | **2.885** | **0.996** |

- first-order truncation → **1.985** ≈ 2 (h² missing) ✓
- correct second order → **2.885** ≈ 3 (h² supplied) ✓
- exact solution → **0.996**: the residual is a pure
  finite-difference truncation floor scaling as **M¹**, so it cannot
  masquerade as an M² signal.

The instrument works, and the last row matters as much as the others:
it tells us the noise floor has a *different* slope from any signal
we care about.

## 2. No pointwise cross term supplies the second order

0046 found the frame-square cross term
¼w₁w₂(k₁·k₂)(k₁k₂ᵀ + k₂k₁ᵀ) reduces the two-body violation ~2×, and
conjectured the residual was "the genuine second-order bond
iteration, which no pointwise ansatz supplies — that is the field
equation's own job." That conjecture is now confirmed.

Scanning the cross-term coefficient c over [−2, +4] at M = 0.01:

| c | −1.0 | 0.0 | 1.0 | **1.5** | 2.0 | 3.0 |
|---|---|---|---|---|---|---|
| max\|R\| | 8.89e−3 | 5.16e−3 | 2.97e−3 | **2.51e−3** | 3.56e−3 | 6.15e−3 |

and measuring the mass slope at three of them:

| c | 0.0 (superposition) | 1.0 | 1.5 (optimum) |
|---|---|---|---|
| slope | **2.015** | **2.022** | **2.042** |

**The minimum over c reduces the coefficient by 2× and leaves the
order untouched.** Slope 2 everywhere, against the validated target
of 3. At the smallest mass the signal sits **433×** above the
single-mass floor, so this is not a noise artefact.

> No scalar multiple of the frame-dictated cross term is the
> second-order solution. The pointwise-ansatz path is closed.

## 3. What this is, and what it is not

**It is a confirmation, not a falsifier.** 0046 predicted exactly
this, and it closes 0046's open item — "iterate the e-equation once
to confirm the two-body residual drops an order" — with the answer
that *the pointwise ansatz does not drop an order, so a genuine
field-equation iteration is required and has not been done.*

The web's own claim is that the second order comes from the **bond**
(0040–0042), not from any metric ansatz. Worth recording a structural
correspondence noticed here and not previously stated in the repo:
**the bond is the Weyl strut.** In GR two static masses cannot be in
equilibrium without a strut or string holding them apart, and the
strut's tension is exactly the Newtonian attraction. The bond's
virial law ∫S = −F·d is precisely a strut of tension
F = Gm₁m₂/d² over length d. The web independently reconstructed the
object GR requires at this order.

Whether the bond supplies the *correct* h² is the sharp open
question, and §1 now gives it a pass/fail criterion.

## Honest limits

- §2 scans one scalar degree of freedom (the coefficient of a fixed
  tensor structure). It shows *that* structure cannot be the second
  order at any weight. It does **not** prove no pointwise ansatz of
  any form can work — a different tensor structure is untested.
- §1's second-order slope is 2.885, not 3.000, because at the
  smallest masses the FD floor begins to contribute (2.38e−6 against
  a floor of 3.48e−7, only 7×). The separation from 2 is what the
  test uses, and that is unambiguous.
- R_μν ≠ 0 is a gauge-invariant statement (vacuum is
  gauge-invariant), so the violation is real and not a chart
  artefact. But R_μν's *magnitude* is coordinate-dependent, so the
  numbers are comparable across this family (same coordinates) and
  not across gauges.
- §3's strut identification is structural — the virial law's form
  matched against the known strut tension — and is **not** a
  numerical verification. It should be measured before being relied
  on.
- The residual is evaluated at four off-axis field points, not
  integrated over a surface. A different point set could change the
  coefficients; it should not change a slope.

## Open

1. **The bond's h²** — does adding the bond's stress contribution
   move the two-body slope from 2 to 3? This is now the program's
   sharpest well-posed classical test, with a validated criterion
   and a real failure mode.
2. **Verify the strut identification numerically**: compute the
   bond's tension from 0040's machinery and check it equals
   Gm₁m₂/d² at leading order.
3. A genuine e-equation iteration (rather than an ansatz), which is
   what 0046 said was needed and what nobody has run.
4. Standing: the correlation gap (0058), the quantum sector's free
   parameters t and N (0057/0059) — the graviton-mass route remains
   the only place an *observational* falsifier could live.
