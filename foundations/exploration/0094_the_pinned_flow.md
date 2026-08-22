# 0094 — The pinned flow: a hierarchy with no continuous knob

Fifteenth stone. 0093 closed with the bar's knob-derivation demand:
pin τ₀ and the transmutation formula predicts a hierarchy. This
stone assembles the pin — and the result is **the program's first
chain from postulate-derived constraints to a dimensionless number
with no continuous dial anywhere in it.** Every link is derived or
measured except exactly one, which is now the arc's sharpest open.
Code: `output/0084_the_pinned_flow.py`.

---

## 1. The chain

```
constraint stack (0081/0090)  →  admissible levels N = 5, 13, 17, 25, 29…
level cutoff (quantum-group admissibility)  →  J(N)   [the one bridge]
the DERIVED Born counting weight at J  →  bare W — no dial
one MK blocking (0092's localization)  →  τ₁(N), heat-kernel exact
the one-loop flow (0093)  →  ln(L*/a) = ln 2 / (c·τ₁)
```

The bare weight is the program's own Born counting (0074) — it has
no coupling constant. Its only discrete datum is where the counting
stops, and the natural identification is the level: quantum-group
admissibility, in its two standard conventions (j ≤ N/2 and
j ≤ (N−2)/2), both carried throughout.

## 2. The table

| N | convention | τ₁ | ln(L*/a) | hierarchy |
|---|---|---|---|---|
| **5** | k=N / k=N−2 | 0.139 / 0.304 | 39 / 18 | **10¹⁷ / 10⁸** |
| **13** | k=N / k=N−2 | 0.027 / 0.036 | 202 / 150 | **10⁸⁸ / 10⁶⁵** |
| 17 | k=N / k=N−2 | 0.017 / 0.021 | 330 / 262 | 10¹⁴³ / 10¹¹⁴ |
| 25 | k=N / k=N−2 | 0.008 / 0.009 | 679 / 580 | 10²⁹⁵ / 10²⁵² |
| 29 | k=N / k=N−2 | 0.006 / 0.007 | 899 / 785 | 10³⁹¹ / 10³⁴¹ |

(heat-kernel flatness after the single blocking ≤ 0.0025 in every
row — the τ₁ values are clean family members, not fits.)

Scaling law: τ₁ ≈ 1.2/J², so **the hierarchy exponent is quadratic
in the level**: ln(L*/a) ≈ (ln 2/1.2c)·J² ≈ 4.5·J². The smallest
admissible level gives particle-physics-sized hierarchies; the
second gives cosmological-sized ones; each further level squares
away into numbers nature doesn't obviously use.

## 3. What may and may not be claimed

**May be claimed**: the program, with zero continuous knobs, now
produces a *discrete menu* of exponentially large pure numbers, one
per admissible level, from a chain whose links are individually
derived (stack), measured (τ₁, c), or theorem-backed (localization,
one-loop shape). No other part of the program — and few quantum
gravity programs anywhere — has produced a dimensionless hierarchy
from first structure. This is 0069 (D)'s demand met *in shape*.

**May not be claimed**: any identification with observed numbers.
The near-misses are recorded because honesty cuts both ways —
N = 5 (k=N) gives 10¹⁷ ~ M_Planck/M_EW's neighborhood, and N = 13
(k=N−2) gives 10⁶⁵ ~ the horizon/Planck ratio's neighborhood — but
the error budget forbids excitement: c is MK-scheme-dependent
(±30% on the *exponent*), the convention choice moves small-N
exponents by 2×, and above all **the level↔cutoff identification is
a modeling bridge, not a derivation**. That bridge is now the
chain's single unproven link, and therefore the sharpest open item
in the RG arc: derive the representation cutoff from the ledger
itself (the Z_N → SU(2) lift ought to know its own admissibility),
and the menu becomes a prediction.

## 4. Falsifiability shape

The chain is falsifiable-shaped in a way the program has not had
before: *if* the cutoff bridge is derived and *if* one measured
hierarchy is matched to fix the level, then every other admissible
level's hierarchy is a prediction with a ±30%-exponent error bar
that better schemes (a controlled RG in place of MK) can tighten.
The menu structure — hierarchies quantized by N², not tunable —
is itself a claim nature could have refused and did not obviously
refuse.

## Honest limits

- The single bridge (cutoff = level admissibility) is motivated by
  the quantum-group structure of Chern–Simons/spin-network theories
  at finite level, not derived here. Both standard conventions
  carried; neither privileged.
- c = 0.127 inherits MK's uncontrolled scheme error; the *quadratic
  law* and the *menu structure* are the robust content, individual
  exponents are not.
- τ₁ computed from the flat counting (n_j = 1); the derived healed
  weights (0075/0076) would shift τ₁ by O(1) factors — same class,
  different digits.
- The identification of L* with a physical scale (which hierarchy
  is this?) is untouched: the flow says *a* scale emerges; which
  observable rides it awaits the assembled complex.

## Open

1. **Derive the bridge**: the representation cutoff from the ledger
   itself — the arc's sharpest open. (The even wall's cover
   arithmetic (0090) and the Lorentzian congruence (0081) both show
   the arithmetic "knows" more than was assumed; the cutoff may
   already be implicit in the Born counting's own consistency.)
2. Replace MK's c with a controlled scheme (the assembled complex
   again — everything converges there).
3. The healed-weight τ₁ (swap flat counting for 0075's derived
   profile).
