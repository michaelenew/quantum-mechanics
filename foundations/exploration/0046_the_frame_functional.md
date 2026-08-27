# 0046 — The frame functional: the ledger writes the action

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

The instruction: take a critical pass through the action derivation,
find the most likely path to the full functional, pursue it. The
pass found a flaw in 0045's negative; correcting it reversed the
verdict; and the corrected direction converges with the prototype
path on one functional — the one the program has been circling since
0026, with the ledger as its missing constraint. Code:
`output/0041_the_frame_functional.py`.

---

## 1. The critical pass

Weaknesses found in 0045:

- **§4's off-shell test used the wrong map.** The cross term was
  given weight √(w₁w₂) — a guess. If the metric is a square, the
  additive object is the **frame** e (g = e·η·eᵀ), and the frame
  *dictates* its cross term: squaring e₁+e₂−𝟙 gives
  ¼w₁w₂(k₁·k₂)(k₁k₂ᵀ+k₂k₁ᵀ) — weight w₁w₂ and the null inner
  product, neither of which the tested ansatz had. So 0045's
  negative stood only against its own ansatz.
- The "prototype path" was declared but not followed to its
  conclusion: 0026's 2+1 action S = ΣB(curl θ − src) was never
  asked *which* standard functional it is. It is ∫e∧F — 2+1
  gravity's first-order form with **B = e**. That question, asked,
  answers the 3+1 one.

## 2. The exact tetrad: the channel is the frame

**e = 𝟙 + ½w·kkᵀη squares to the Kerr–Schild metric exactly** —
residual 1e−15 including w = 3 (strong field) and Doppler-scaled k —
because k's nullity kills the quadratic term: (kkᵀη)² = (k·k)kkᵀη = 0.

Three exact consequences:

- **the channel is the frame perturbation**, linear at *any*
  strength (0044's linearization is now an identity, not just a
  measurement);
- **the ledger's ½ is the literal coefficient**: e = 𝟙 + ½(channel);
- **collinear channels superpose exactly** (same k ⇒ cross term
  carries k·k = 0): mass additivity at a point is an identity.

## 3. The corrected off-shell test

| c (frame cross coefficient) | 0.0 | 0.5 | **1.0** | 1.5 | 2.0 |
|---|---|---|---|---|---|
| max\|R_μν\| | 5.16e−3 | 3.44e−3 | **2.97e−3** | 2.51e−3 | 3.56e−3 |

The frame-square cross term **reduces the two-body violation by
~2×** where 0045's wrong-weight term increased it at every c ≠ 0.
The frame is the better additive variable; the residual (minimum
~2.5e−3 near c = 1.5) is the genuine second-order bond iteration,
which no pointwise ansatz supplies — that is the field equation's
own job.

## 4. The functional

The frame-first reading and the prototype path converge:

```
3+1:   S[e, ω] = (1/2κ) ∫ ε_IJKL  e^I ∧ e^J ∧ F^KL(ω)
2+1:   S[e, ω] = (1/κ)  ∫ ε_IJK   e^I ∧ F^JK(ω)
```

Checked against everything measured:

| requirement | status |
|---|---|
| reduces to the 2+1 prototype | the 2+1 form **is** 0026's BF with B = e (budget = frame, linear) |
| conservation as second EOM | ω-equation d_ω(e∧e) = 0 = 0030's measured lattice dB = 0 |
| linear per channel | §2's exact tetrad |
| the bond | the e-equation's second-order iteration; its integrated cross stress **is** the virial bond (0040 §2, measured) |
| matter | S_m = m∫\|e(ẋ)\|dτ — proper time metered by the frame = 0035's sender-clock normalization, as a variational principle |

And 0030's frontier question — *what plays Plebanski's simplicity
constraint in an information web* — gets the ledger's answer:

> **B = e∧e is "probability = amplitude²" at the action level.**

In 2+1 the tiers coincide (B = e, linear): topological BF, additive
charges, no gravitons — the prototype exactly as measured. In 3+1
the budget is the *square* of the frame, and that single squaring is
where gravitons, multiplicative bonds, and bond quantum = (charge
quantum)² all come from. The simplicity constraint is not an
external bridge to import; it is the square-root ledger stated as an
equation between the theory's two tiers.

## Honest limits

- The Palatini and Plebanski forms are imported from the GR
  literature; the identification rests on constraint-matching plus
  the measured keystones (exact tetrad; lattice dB = 0; bond
  stress; 2+1 reduction), not on a lattice re-derivation of the
  full nonabelian action.
- The tetrad e = 𝟙 + ½wkkᵀη is one local-Lorentz gauge choice of
  square root; the identity is exact but not unique.
- §3's minimum at c ≈ 1.5 rather than 1 says frame superposition is
  better but still not the two-body solution (nothing pointwise
  is); whether the optimal c carries meaning or is gauge noise is
  undetermined.
- The matter term's equivalence to the sender-clock rule is noted
  structurally, not yet verified by variation.

## Open

1. **The lattice Palatini**: put e on 0030's lattice, impose
   B = e∧e, and verify the torsion equation numerically — the
   constructive completion of the identification (and the honest
   replacement for the imported continuum forms).
2. **Vary the matter term**: derive the sender-clock channel rule
   (0035) from δS_m — if it falls out, the covariant channel stops
   being an ansatz.
3. **The quantum square**: B = e∧e as an *operator* identity on the
   level-N tower — the bond operator ω^(n_a n_b) (0042) should be
   its holonomy shadow.
4. **The c ≈ 1.5 residual**: iterate the e-equation once
   numerically (the true second order) and confirm the violation
   drops an order — the direct demonstration that this functional's
   iteration is the two-body rule.
