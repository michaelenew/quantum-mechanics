# 0013 — Probing the movie synthesis: three fronts, three verdicts

The synthesis (conversation record, following 0011/0012): reality as
a movie of loops in 3-space; interactions as the singular points of
its projection; knowledge concentrated in the decorations; round
trips trust-lossy; recovery = closing the holonomy word. Three
computational probes, all axioms-forward (nothing recalled where it
could be derived). Code: `output/0006`–`0008`.

---

## Front 1 — Cocycle localization: knowledge is *forced* onto the interactions
(`output/0006_cocycle_localization.py`)

The quandle coboundary operator implemented generically (δ∘δ = 0
verified exhaustively), cohomology computed by exact elimination:

```
H²_Q(R₃; Z₃) = 0        — no invariant content at double curves
H³_Q(R₃; Z₃) = Z₃       — invariant content exists at triple points
```

For 2-knot state sums, 2-cocycles weight double curves and
3-cocycles weight triple points — so with dihedral colors, the
surface invariant *cannot* live on the particle paths and *can* live
on the interaction events. "All recoverable knowledge concentrates
at interactions" is, at this tier, a computed statement about where
nontrivial cohomology sits.

Supporting machinery, all verified: quandle colorings reproduce
0011's Fox counts; with the GF(4) Alexander quandle H² ≠ 0 and the
*derived* 2-cocycle separates trefoil from unknot while surviving a
Reidemeister-I kink; a rack cocycle violating the degeneracy axiom
satisfies the cocycle equation yet **fails** R1 — the degeneracy
axiom *is* diagram-move safety, demonstrated by measurement. The
published triple-point value for the 2-twist-spun trefoil (CJKLS;
Satoh–Shima) uses exactly the H³ class derived here; recomputing it
needs an explicit broken surface diagram (cited, not recomputed).

## Front 2 — The interaction algebra: loop braids and the tetrahedron
(`output/0007_loop_braids_and_the_tetrahedron.py`)

The movie's event algebra, computed as free-group automorphisms
(exact reduced-word arithmetic):

- **The loop braid presentation emerges from the action itself**:
  braid relations for the leapfrog σ, symmetric relations for the
  exchange ρ, both standard mixed relations hold — and the third
  candidate (`ρ₁σ₂σ₁ = σ₂σ₁ρ₂`) **fails**: the forbidden move,
  isolated by computation. Consistency at events is a real algebra
  with exactly one illegal symmetry.
- **Recovery can be impossible**: σ₁'s action has infinite order
  (word length grows linearly to depth 40, never returning). The
  "traverse the dual path to recover" principle generalizes to
  "close the holonomy word" — and for infinite-order monodromy
  there is no closing word. The odometer limit, at the group level.
- **The tetrahedron census**: consistency of triple events is the
  Zamolodchikov tetrahedron equation (the axiom of braided monoidal
  2-categories). Exhaustive over GF(2): Yang–Baxter holds for
  **5/24** bijections of X²; the tetrahedron for **7/168** invertible
  linear maps and **26/40320** bijections of X³. Consistent triple
  interactions are ~350× rarer than consistent pairwise ones —
  measured: raising the event order collapses the space of
  admissible interaction rules.

## Front 3 — The Fisher deficit: an integrable spike, not a conical atom
(`output/0008_fisher_deficit.py`)

The open row's first number. Setup: localization through k range
channels (beacons on the unit circle), Fisher metric
g = Σ uᵢuᵢᵀ, curvature by the Brioschi formula — the pipeline
validated first on three exact cases (flat 0, sphere +1, and the
Gaussian-knowledge metric of 0005 at −1/2, all to 1e-4).

Findings, as measured:

- Approaching a beacon, **K ~ 1/d**: local scaling exponents
  −0.81, −0.91, −0.95, −0.99 as d halves from 0.2 to 0.0125, with
  d·K → 0.082. The interaction *is* visible in the smooth
  information geometry — a genuine curvature concentration —
- — but it is an **integrable spike, not a conical atom**: total
  curvature in the annulus 0.02 < d < 0.2 around a beacon is 0.004,
  smaller than a control patch at the web's centre (0.059, angular
  cancellation included). A conical defect would put a finite
  deficit *at the point*; the measured field puts a finite, small,
  spread deficit near it.
- Symmetry flattens: 6 beacons give K ≈ 0 at the centre; 3 give
  exactly 1/3 (measured 0.3333).

**Verdict for the open row**: at the smooth level, "correlation
sources curvature" is real but soft — interactions curve the
knowledge geometry with a 1/d halo and no atom. The Z₂ defect of
0012 lives in the *discrete decoration* (the over/under bit), which
the smooth Fisher metric does not see. The two-instrument picture
survives exactly: **trust-loss and curvature are the same holonomy;
the metric reads the halo, the decoration carries the atom.** The
concrete next object is therefore not a better metric but a
*connection with monodromy* on the web — Fisher geometry plus a
discrete gauge field coupling to the decorations.

## Honest limits

- Front 1: cohomology fully derived at (R₃, Z₃) and (GF4, Z₂);
  R-move invariance checked for R1 (structural) and not staged for
  R2/R3 diagrams; the level-2 state-sum value remains literature.
- Front 2: censuses are at |X| = 2 — fractions may drift with
  alphabet size; the conjugation action is one (the standard)
  representation of the loop braid group.
- Front 3: one measurement model (range channels); curvature probed
  to d = 0.0125 with step-size control but no exact solve; the
  1/d law is a fit over four octaves, not a derivation. An analytic
  computation of K for the k-beacon metric is likely tractable and
  would settle the exponent.

## Open

1. **Analytic K for the beacon web** — confirm K ~ c/d and compute
   c(k): if c has a clean form, the halo law is a theorem.
2. **Fisher + monodromy**: define the web's geometry as (metric,
   discrete connection) with the decoration as gauge field; the
   defect ledger of 0012 then sits *inside* the information
   geometry rather than beside it — this is now the sharpest form
   of the "correlation sources curvature" program.
3. **The tetrahedron solutions found**: classify the 26 — which are
   permutation-conjugates of maps built from Yang–Baxter solutions,
   and does any carry a nonabelian invariant usable as a triple-
   point weight (a set-theoretic shadow of the level-2 invariant)?
4. **R2/R3 staging** for the state-sum machinery, completing the
   diagram-move verification the R1 demonstration began.
