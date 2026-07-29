# mechanism — SUMMARY

What a measurement *is*, mechanically, under the knowledge-first reading.

## Current state

**Measurement = coincidence = split/merge** (`exploration/0001`). When two
systems reach the same place, their relative coordinate `q = q1 − q2` becomes
sharp. In CoM/relative variables `Q,P,q,p`:

    [Q,P] = [q,p] = iħ,   [q,P] = [Q,p] = 0

so **relative position `q` and total momentum `P` commute and can be sharp
together** — the EPR state. Verified symbolically in
`output/0001_relative_coordinate_checks.py` (all checks pass).

**Refinement of the original mechanism (a real correction):** a split/merge does
not make "momentum unknown." It makes relative position `q` *and* total momentum
`P` sharp (the latter by conservation); complementarity forces the conjugate
pair — CoM position `Q` and **relative** momentum `p` — broad. This is exactly
what SPDC produces and what Howell et al. (2004) used to demonstrate EPR, so the
mechanism has direct experimental grounding.

**Consequences derived/illustrated:**
- Sensor "spike" = sharpening of the detector–system relative coordinate (no
  absolute collapse).
- Buckyball arrives whole = internal relative state is a priori sharp; only the
  CoM which-path info decoheres.
- Recursive collapse = marginalizing a knowledge chain (convolution; variances
  add). Bayesian/Gaussian fusion when two states describe one coordinate.

## Artifacts

- `output/0001_relative_coordinate_checks.py` — pure-stdlib checks of (1) the
  commutator algebra, (2) chain variance additivity, (3) Gaussian fusion.
  Run: `python3 output/0001_relative_coordinate_checks.py`. All pass.

## Known gaps

- The classical-Gaussian fusion vs. quantum (Lüders) update equivalence is
  unresolved — this is precisely the Bell fork (`testability/`).
- "Only coincidences reduce uncertainty" is postulated, not derived from a
  dynamics.
