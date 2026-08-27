# 0111 — The vertex response: the deficit selects among vertex operators

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Front #4's port attempt, with a discriminating negative as the
result. Code: `output/0101_the_vertex_response.py`.

The plan: connect the vertex tier (0107: the vertex is the dropped
total correlation) to the dressed vacuum's measured ~10% deficit
below its Gaussian baseline (0104) via linear response to the
*leading isotropic* TC insertion, exp(+ε Σ_sites Σ_{p<q} F_p·F_q).
Measured (8 chains × 2240, ordered branch, C kernel):

- the marginal responds cleanly: d⟨θ²⟩/dε = +0.0015 ± 0.0001;
- **both scale-field responses are null**: |d sP/dε| < 0.0013,
  |d c(1)/dε| < 0.0033 (3σ bounds). Closing the deficits with this
  operator would need |ε| ≳ 1–4 — outside linear response.

**Verdict: the isotropic leading TC term is disfavored as the
deficit's source.** The correction to the scale field must enter
through orientation-dependent vertex structure — exactly what 0088
measured as orientation lensing (the vertex charges how a source
*sits* in the local frame, not just how much) — or at higher order.
The deficit has become an instrument: it selects among vertex
operators. A first preliminary signal (+0.0019 ± 0.0008 at 4-chain
statistics) collapsed under 7× more data — kept in the record as a
reminder of why we crank statistics before claiming bridges.

## Open
1. The orientation-dependent insertion (0088's lensing operator,
   Σ (F_p·F_q)² or frame-aligned forms): same linear-response
   harness, one operator swap.
2. If that also nulls: the deficit is nonperturbative in the vertex
   — reweighting at finite ε with ESS control.
