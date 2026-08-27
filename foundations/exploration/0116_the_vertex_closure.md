# 0116 — The vertex closure: c(1)'s carrier, and the reach of linear response

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0112's two residuals, closed. Code:
`output/0106_the_vertex_closure.py` (6 chains × 1640 measurements).

**c(1)'s carrier is a neighbour operator — as its own character
required.** c(1) is a *neighbour* observable, so no site-local
operator has reason to move it, and none did. Adding two
neighbour-coupling operators:

| operator | d⟨sP_exc⟩/dε | d⟨c(1)⟩/dε |
|---|---|---|
| S_mag (site-local) | +0.00218 ± 0.00020 \* | +0.00034 ± 0.00046 |
| **S_nnmag** (neighbour scale–scale) | −0.00103 ± 0.00154 | **+0.03070 ± 0.00549** \* |
| **S_nnalign** (neighbour orientation) | −0.00019 ± 0.00057 | **+0.01021 ± 0.00175** \* |

Both neighbour operators move c(1) at >5σ (ε\* = −0.134 and −0.402
respectively), while leaving the site-local scale observable alone.
The division of labour is clean: **site-local magnitude pairs drive
the scale field, neighbour couplings drive its correlation.**

**Linear response is validated at the coupling where the operators
were identified.** Reweighting the ensemble at finite ε (an exact
measurement, paid for in effective sample size):

```
  ε      ESS/N     ⟨sP_exc⟩ exact   linear pred   ratio
 −0.05   0.990       0.011534        0.011532     0.98
 −0.20   0.854       0.011231        0.011204     0.94
 −0.66   0.227       0.010414        0.010199     0.85
 −1.50   0.008       0.008981        0.008365     0.81
```

At ε\* = −0.66 reweighting is still usable (ESS/N = 0.23) and the
exact response is **85% of the linear prediction** — mild
saturation, no qualitative change. 0112's identification rests on
solid ground. (My prior expectation that ESS would collapse before
ε\* was wrong; it does not, and the check is therefore stronger than
planned.)

**Scope, stated precisely.** This exercise identifies *which
operators can generate deviations of the observed size and sign*. It
is an identification of structure, not a fit of a missing term: the
measured deviation is the product measure's own anharmonicity
against the free Gaussian bank, and a genuine vertex term would be
an *additional* correction beyond it. What is established is the
channel the interaction acts through.
