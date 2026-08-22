# 0073 — The nonabelian plaquette: the derived weight meets the sign problem

Path A's third stone (0070's A2, first half). 0072's continuum kernel
is lifted to a class function on Spin(4) = SU(2)⁺ × SU(2)⁻ and
expanded in characters — the nonabelian analogue of the dual weights.
Three findings; the third is the wall bleeding exactly where 0071 said
the bleed-line had moved. Code:
`output/0065_the_nonabelian_plaquette.py` (1.3 s).

---

## 1. The center is blind

Every half-integer-spin coefficient vanishes identically (machine
zero, seven pairs checked). The weight is a function of f² and cannot
see θ → 2π−θ, so only integer spins survive: **vector frames see
SO(4), not Spin(4)** — the derived vertex has no spinorial sector.
Recorded, not lamented: matter that needs spinors will need a
spinorial B, which is a statement about the matter thread (0069's E),
not a defect of the gravity sector.

## 2. The simple representations dominate, heavy-tailed

At ε = 0.01 the balanced diagonal carries the weight —
c(j,j)/c(0,0) = 0.62, 0.45, 0.34, 0.27 at j = 1..4 — while
off-diagonal entries are an order smaller. **Barrett–Crane's simple
representations emerge softly**, exactly as 0072's Cauchy
concentration predicted. And the diagonal decays far slower than any
heat kernel: matching e^{−xj(j+1)} on the first step predicts 0.14 at
j = 4 where the actual is 0.27. The τ-lesson — arithmetic heavy tail,
not Gaussian — at the nonabelian tier.

## 3. The sign problem arrives

The weight is pointwise positive. Its character expansion is **not**:

| ε | c(1,0)/c00 | c(2,0)/c00 |
|---|---|---|
| 1.0 | +0.147 | **−0.008** |
| 0.1 | +0.042 | **−0.070** |
| 0.03 | **−0.065** | −0.061 |
| 0.003 | **−0.267** | +0.056 |

Both lifts develop negativity (chord: c(1,0) crosses near ε ≈ 0.05;
angle: c(2,0) = −0.078 at ε = 0.01) — *which* coefficient differs by
lift, *that* some coefficient goes negative does not. Grid-stable to
10⁻¹⁷ under NG 400 → 600.

Character positivity of the plaquette weight is the standard
Osterwalder–Seiler route to a positive transfer matrix. Its failure
means **the naive one-plaquette lift does not obviously define a
reflection-positive theory** — negative "probabilities" in the
rep-basis sum, the sign problem, the disease interacting
quantum-gravity measures die of. Met on schedule, at the wall, in the
first genuinely nonabelian computation.

(Notably, "the sign problem" is one of the four probes named in the
sibling arithmetic branch's final commit — a cognate wall, hit
independently from the other side.)

## 4. The cure has the ledger's shape

This is why the finding is a direction, not a death. The U(1)
continuum ledger's dual weight was **τ = 1∗1 — a Dirichlet square —
and squares are coefficient-positive automatically** (rechecked). A
nonabelian weight built as a *dual square* has character coefficients
(amplitude)² ≥ 0 by construction.

The naive kernel lift is not that object. Its negativity is evidence
that **the kernel alone was never the whole weight** — the Z_N chain
had K per plaquette *and* the Dirichlet-square structure in the dual;
the class-function lift kept the first and dropped the second. A2's
disease independently demands exactly 0064's open 1: **the nonabelian
Dirichlet square**. The next stone is forced, not chosen — which is
the best possible outcome of hitting a wall.

## The filter loop, closed this turn

- The τ = s² boundary cure was written up in lucid-filter's own
  conventions (`research/oracle-gap/0010_the_square_chart.py` + a
  SUMMARY pointer) and pushed on branch
  **`claude/square-chart-boundary`** — verified there on the one-step
  toy with analytic scores (I(s)/s² → 1.597; I(τ) → 0.399 flat; MLE
  demo: clean one-sided boundary piling at s = 0). Their harness
  tests (GPB1/IMM likelihood in τ; the kick-control price) left to
  them, as flagged in the note.
- Scan of lucid-filter for this thread: the shipped `WalkingFilter`
  (moving quadrature grids that re-center on the posterior) is an
  *adaptive-frame* idea worth remembering when the web's frames
  become dynamical; the convergence-proofs workstream's
  "AI-generated, not peer-reviewed" banner is a convention this repo
  should consider adopting for its own theorem-shaped claims.

## Honest limits

- The lift from the algebra kernel to a class function is a choice
  (chord vs angle tested; both diseased); the negativity conclusion
  is about the *naive lifts*, and OS character-positivity is
  sufficient, not necessary — a positive transfer matrix by another
  route is not excluded, just not exhibited.
- One plaquette, no intertwiners, no vertex assembly; Euclidean
  Spin(4); ε finite throughout (the ε → 0 trend is the BC limit, not
  the program's own regime — N ~ L² is finite here).
- The heat-kernel contrast matches one step and compares one point;
  it is a shape statement, not a fit.

## Open

1. **The nonabelian Dirichlet square** — now doubly demanded (0064
   open 1; §4's cure). Concretely: build the dual-square weight on
   the subgroup/representation lattice of SU(2) and check it (a)
   reproduces the kernel's invariant structure, (b) is
   coefficient-positive by construction, (c) still concentrates on
   simple reps.
2. **A3 with the positive weight**: the graviton-propagator test
   belongs *after* the square, not before — running it on a
   non-positive weight would test the wrong object.
3. The positivity-restoring role of intertwiners at a true 4-valent
   vertex (the one-plaquette lift may be the wrong unit).
4. Standing: Λ1; C1; the arithmetic-branch pass (its "sign problem"
   probe now directly relevant).
