# foundations — SUMMARY

State of the formalization. **Reframed** around consistency as the fundamental
law; nonlocality embraced (see `exploration/0003`, which supersedes P2 of
`0001`).

## Current postulates

- **P1 Relational states** — all content is pairwise knowledge states
  `{ρ_{A→B}}` over relative coordinates; no absolute frame.
- **P2 Two-tier knowledge** *(reframed)*.
  - **Actionable** knowledge (usable to do something differently — forces,
    signals) is *c*-bounded.
  - **Correlational** knowledge (the mutual consistency of the web) updates
    **instantaneously and nonlocally** — not as a propagation, but as global
    re-satisfaction of a constraint. Non-signalling because the outcome is
    random and averages away in every distant marginal.
- **P3 Pairwise consistency, no global section** *(reframed)*. Every pairwise
  overlap agrees, but the family need **not** admit a single global joint
  distribution of definite values. Demanding such a joint = local
  hidden-variable model (Fine's theorem) → falsified. Local consistency
  *without* a global section is the sheaf-theoretic content of
  contextuality/nonlocality — the mathematical name for "no god's-eye view."
- **P4 Recursive consistency** — chains compose; variance additivity /
  data-processing inequality on relative coordinates. Interpreted now as a
  candidate quantum-selecting principle (see `testability/`).
- **P5 Measurement = coincidence + minimum-relative-entropy projection.** A
  split/merge sharpens one edge; the whole connected component re-settles by
  projecting onto the consistency manifold with minimum relative entropy — the
  unique rule matching the posit's own desiderata (reduces to Bayes, injects no
  extra uncertainty, order-independent). Classical version solid; quantum
  equivalence to the Lüders/Born update is open and concretely tractable.

## The corrected central story

- Consistency is fundamental and global; nonlocality is its shape.
- The two-tier structure (actionable vs. correlational) resolves the
  c-vs-instantaneous tension without violating no-signalling.
- The consistency law read *without* a global section automatically forces
  non-classical (Bell-violating) correlations — a derivation from the posit's
  own words. Demonstrated numerically in `testability/output/0002`.
- Whether it forces *quantum* (S ≤ 2√2) rather than merely *non-classical* is
  the frontier; concrete open leads listed there.

## Positioning (`exploration/0002`)

Inherited: relational stance (RQM), epistemic/Bayesian state (QBism, Spekkens),
decoherence (Zurek — now re-read as *dilution*, not destruction), relative-frame
states (QRF/Giacomini), sheaf-contextuality (Abramsky–Brandenburger),
information-causality (Pawłowski) as a candidate cousin of P4.

Contributed: the two-tier resolution of the c-vs-instantaneous puzzle;
MRE-projection as the specific update rule; the framing that P4/MRE *might*
select the quantum set (open, do not overclaim); consistency-first packaging
that turns "no god's-eye view" from a slogan into the sheaf-theoretic
non-extendability condition.

## Recursive consistency as a cocycle (`exploration/0004`)

Pressing on P4 directly. Model the web as a graph, edges = pairwise knowledge
states. Recursive consistency = composition along any two paths agrees =
**cocycle condition** (Čech cohomology). Nontrivial `H¹` of the constraint
sheaf = "no god's-eye view" made mathematically precise.

- **Tree-shaped webs** have vacuous cocycle → always classical.
- **Loop-containing webs** admit nontrivial holonomy → frustration (classical)
  or contextuality (quantum), depending on the composition rule.
- The **composition rule on edges selects the theory** (convolution → classical
  probability; symplectic/unitary → QM; other rules → other GPTs).
- Frustration and contextuality are proposed to be the *same* `H¹` structure
  with different composition rules. Target, not yet proven.
- Verified in `testability/output/0003`: compatible-observable triangle has
  polytope = classical (1/3 of cube), so pure-graph-topology contextuality
  requires **choice of context** (incompatible observables) — an important
  localization of where quantumness enters.

## Geometry of the web (`exploration/0005`, `output/0001`)

The moment we say "knowledge is a distribution," the web inherits a
Riemannian geometry with **no axiomatic freedom**: Chentsov (classical) /
Petz (quantum) uniqueness fixes the metric up to scale. Immediate
consequences:

- Gaussian knowledge `(μ, σ)` → hyperbolic upper half-plane
  (constant negative curvature).
- Pure qubit knowledge → `CP¹ = S²` with the Fubini–Study metric
  (constant positive curvature). Fidelity `= cos²(α/2)`. Verified in
  `output/0001_qubit_geometry.py`, including Gauss–Bonnet excess to
  machine precision.
- Composition of knowledge along the web = parallel transport.
  Loop-holonomy = curvature = the differential-geometric statement of the
  cocycle obstruction (`0004`).
- Uncertainty relations = curvature bounds on the state manifold
  (Anandan–Aharonov speed limit is the canonical example).

The GR analog is literal, not metaphor: general covariance ↔ sufficient-
statistics invariance; light-cone causal structure ↔ two-tier
actionable-vs-correlational split; mass sources curvature ↔ (open)
correlation/entanglement sources information-manifold curvature (holography /
Ryu–Takayanagi territory, cited-not-claimed).

## Two-tier structure & the FTL barrier (`exploration/0006`)

Taking the user's precise reading of SR seriously: relativity forbids
*continuous* crossing of `c`, not FTL per se. That leaves a clean slot for
discrete, non-continuous, non-signalling correlational updates. Geometrically:

- **Actionable knowledge = dynamics on the manifold** (timelike/null,
  continuous, ≤ c).
- **Correlational knowledge = spacelike constraint structure on the manifold**
  (not a propagation, no speed applies).

The "instantaneous distant update" is the spacelike-slice re-shaping to keep
the constraint satisfied. Nothing crosses `c` because nothing crosses at all.
Tachyons are not needed and come with their own baggage; the cleaner slot is
constraint-structure vs. dynamics. Removes the paradox-flavor of "collapse is
instantaneous but SR is respected" — the two describe different geometric
objects.

## Reconstruction route (`exploration/0007`)

Candidate axiom list combining P1–P5 with Fisher/Bures uniqueness,
purification, and continuous reversibility. Existing reconstructions
(Hardy 2001; Chiribella–D'Ariano–Perinotti 2011; Masanes–Müller 2011) already
derive standard finite-dim QM from information-theoretic axioms; what the
consistency-first packaging may add is a **single unifying physical picture**
motivating all of them at once, plus the two-tier resolution of the
c-vs-instantaneous puzzle. Concrete milestones ordered by tractability; the
crux step is showing that (1)–(8) collectively imply the CDP/Hardy axiom set.

## Kernel from stat-tracker: distribution / trust / influence (`exploration/0008`)

The sibling `michaelenew/stat-tracker` project turned up three portable
findings:

1. **Three-level split** — separate the *distribution* (what I believe about
   the state), the *trust* (how much I trust my model of the state's
   dynamics), and the *influence* (how strongly a new observation should
   move my estimate). Standard QM conflates these in the density matrix;
   making the split explicit clarifies decoherence (trust erosion), effective
   Hamiltonians (learned trust structure), and error correction.
2. **Influence = √(information)** — verified to full float precision in
   `output/0002_amplitude_shadow.py` across four orders of magnitude in `q`
   for the Kalman random-walk-plus-noise model. This is the amplitude-vs-
   probability structure of the Born rule showing up in a purely classical
   Bayesian tracker: `P = |ψ|²` is what any Fisher-metric optimal inference
   forces, not a QM-only axiom. Lines up with Wootters (1981) but
   demonstrated from the outside.
3. **"Trustworthy" is contextual** — `Λ^robust = min_{h' ∈ ℋ} KL(P_h||P_h')`.
   Trust in `h` depends on the alternative set; there is no
   context-independent nat count. Classical Bayesian shadow of quantum
   contextuality; usable as an engineering-tractable contextuality witness.

## The two-layer split (`exploration/0009`, `output/0003`)

Refines the whole framework: a **core** (layer 1) of losslessly, *locally*
composable frame transforms (`T_ab·T_bc = T_ac`, conjugates cancel), an
**overlay** (layer 2) of path-dependent informational structure whose
consistency is only *global* (sum over every intermediate `X`, with conjugate
symmetry `∫(a→X→c) = [∫(c→X→a)]*`), and all irreversibility in their
**interplay**.

- **Anchor theorem:** Stinespring dilation — every lossy quantum channel is
  exactly lossless-on-a-larger-system + coarse-graining. The split is a
  theorem in QM, not a hope; standard open-system theory just discards the
  dilation and carries the lossy composite as primitive.
- **Identification:** layer 1 = stationary-phase/Hamilton–Jacobi skeleton
  (pointwise composition); layer 2 = the full path sum, whose required
  global consistency is *verbatim* the kernel composition law
  `K(a,c)=∫K(a,X)K(X,c)dX` plus hermiticity `K(a,c)=K(c,a)*`; interplay =
  what stationary phase discards (Gell-Mann–Hartle decoherence functional).
- **Computed witness** (`output/0003_two_layer_dephasing.py`): pure
  dephasing with one environment qubit. Joint purity exactly 1 (layer 1
  lossless), pointer weights frozen (layer 2 lossless), Schmidt spectrum
  carries 100% of the decoherence (interplay) — and fully **recurs** at
  t=π/2, so the loss is displacement, not destruction; irreversibility is
  the many-mode dilution limit (`mechanism/0002`).
- **Self-frames:** the ladder principle ("maximally coherent to itself",
  uncertainty saturated, layer 2 empty) lands on coherent states — which
  are Zurek's einselected pointer states. Structural match; derivation open.
- **W1 (working hypothesis):** entropy-producing curvature lives in the
  interplay only; Berry phase is quarantined as reversible layer-1
  holonomy. Break condition stated.

## The arithmetic bridge (0010)

A parallel workstream (`michaelenew/formal-languages`, `arithmetic/`
0056–0066) measured, in a finite revision-dynamics frame, several things
posited here: the graded cost of P3's obstruction (forced entropy =
log₂|holonomy|, Haar floor), the classical/amplitude ledger (k bits →
1 bit → 0), the epistemic-restriction boundary (stabilizer fragment
recovered, stops at the parity), negativity 1/2 located on the phase
fiber, the relational-sheet gauge structure supporting P1, the
double-cover reading of contextuality, where holonomy goes non-abelian
(second loop through a shared multi-valued edge), and the logic face
(incompleteness as the same no-global-section structure). See
`exploration/0010_the_arithmetic_bridge.md` for the dictionary and
cautions.

## Interactions as crossings (0011)

Knot theory is a *sub-case* of this repo's web formalism, verified
computationally (`exploration/0011`, `output/0004`): arcs = channels,
crossings = three-party constraints, global sections = Fox colorings =
flat dihedral connections; the section counts (trefoil 9 at p=3,
figure-eight 25 at p=5, granny 27 distinguishing it from the trefoil)
are the knots' holonomy invariants, and the modulus where sections open
divides |Δ(−1)| = |H₁(branched double cover)| — the knot's tax lives on
its second loop, like the arithmetic frame's paradox tax. det T(3,5) = 1
shows abelian shadows can vanish for nontrivial knots: complete
detection needs nonabelian holonomy (Kronheimer–Mrowka: every
nontrivial knot has irreducible SU(2) representations). Curvature
clause pinned: discrete Bianchi (bulk face-holonomies cancel pairwise —
every edge borders two faces) plus flat-but-holonomied torus classes
(|H¹| = 4 by exact GF(2) rank) — holonomy is the primitive, curvature
its local density, concentratable entirely at defects; in 2+1 gravity
this is the whole theory (conical defects, Chern–Simons form). Open:
the composition-rule dial on knot webs (convolution → colorings;
unitary → Jones-tier?); det-1 webs as abelian-invisible test cases;
deficit-angle geometry from the web's information metric.

## Curvature from crossings: the defect ledger (0012)

The "interactions are crossings, curvature is their loop holonomy" claim
tested at the 2+1 boundary, all computed (`exploration/0012`,
`output/0005`). **Holonomy IS the angle defect**: parallel transport
composed honestly from unfolding isometries around every vertex of the
tetrahedron/cube/octahedron/icosahedron matches 2π − Σ face angles to
1e-8, with the surface flat elsewhere — curvature sits at defects and is
the loop holonomy. **The budget is topological**: on knot projections
built from real plane curves (1/3/5/7 crossings, map traced from the
rotation system, exact rationals) the combinatorial curvature totals
χ = 2 always, with κ per crossing exactly 2/V — **interactions
redistribute curvature, they cannot create it**; adding a crossing adds
a face and dilutes. **The budget is the mass bound**: with δ = 8πGm,
Σδ = 4π gives Σm = 1/(2G) and per-defect m < 1/(4G); and the rotation
parts of all defect holonomies compose to the identity exactly when the
deficits sum to 0 mod 2π — Gauss–Bonnet *is* the condition for trivial
global holonomy, so the curvature budget and web consistency are one
constraint. **Masses add, centres braid**: two defects compose with
rotation d₁+d₂ either way (mass = the abelianization of ISO(2)) but the
orders differ by the pure translation (I−R_{d₁})(I−R_{d₂})(p₁−p₂) —
gravity's nonlinearity is the noncommutativity of defect holonomy, the
braided tier as physics. Honest gaps: 2+1 has no attraction and no
waves (no Newtonian limit from this mechanism alone); in 3+1 conical
defects are *strings*, so the literal reading is a knotted string
network; combinatorial κ is a ledger, not a metric. Open: derive a
deficit angle from the Fisher metric around a degree-k node (this
would close the repo's flagged "correlation sources curvature" row);
whether dynamical redistribution yields an effective force; framing
(writhe) ↔ defect spin.

## Probing the movie synthesis (0013)

Three computational probes of the movie/interaction synthesis
(`exploration/0013`, `output/0006`–`0008`). **Cocycle localization**:
quandle cohomology solved by exact elimination — H²_Q(R₃;Z₃) = 0,
H³_Q(R₃;Z₃) = Z₃ — so with dihedral colors the 2-knot invariant cannot
live on double curves (particle paths) and must live at triple points
(interactions): "knowledge concentrates at interactions" as a computed
cohomological fact; the derived GF(4) 2-cocycle separates trefoil from
unknot and the degeneracy axiom is shown by measurement to *be*
Reidemeister-I safety. **The interaction algebra**: the loop braid
presentation emerges from the free-group conjugation action (both
standard mixed relations hold; the forbidden move ρ₁σ₂σ₁ = σ₂σ₁ρ₂
fails); the leapfrog has infinite order (some round-trip losses are
never recovered — no closing word); and the tetrahedron census over
GF(2) gives 5/24 Yang–Baxter vs 26/40320 tetrahedron solutions —
consistent triple interactions are ~350× rarer than pairwise.
**The Fisher deficit** (the open row's first number, pipeline validated
on flat/sphere/Gaussian-knowledge exact cases): approaching a beacon
the knowledge curvature scales as K ~ 1/d (exponents → −0.99, d·K →
0.082); symmetric webs flatten the centre (k=6 → 0; k=3 → exactly
1/3). Verdict revised by 0014: the halo is the tidal dressing of a
genuine conical atom at the apex. Open: analytic K for the beacon web;
the (metric, monodromy) formulation; classifying the 26 tetrahedron
solutions; R2/R3 staging.

## The cone at the interaction (0014)

All four sharp opens of 0013 chased (`exploration/0014`,
`output/0009`). **The cone theorem**: near a beacon the Fisher metric
is e_r e_rᵀ + A(φ) + O(d) — a flat cone plus a tidal O(d) correction,
which *derives* the 1/d halo exponent and gives the deficit in closed
form, δ = 2π − ∮√(EC−B²)/E dφ, validated against honest parallel
transport (1.93515 vs 1.93439 at k=3; 0.98508 vs 0.98490 at k=6). The
minimal web has **δ(2) = π**: transporting a frame once around a
pairwise interaction *negates* it — "the round trip puts you in your
dual state" is now a theorem of information geometry, with
densification washing the flip out as δ(k) → 2π/(k−1) (measured to
k=20). This revises 0013 ("no conical atom" — the annuli could only
see the halo) and closes the open row: **an interaction node is a
conical defect of computable deficit in knowledge geometry.**
**Metric ⊗ decoration**: the composite ISO(2)×Z₂ holonomy of the free
loop group computed; the dual path x² is trivial in every instrument
(full recovery), the commutator displaces while rotation- and
flip-trivial (pure braided residue), and at k=2 the metric's π-flip
and the decoration's bit are the *same* Z₂ — one bit, two carriers,
traded under densification. **The 26 tetrahedron solutions**: 21
orbits under inverse × bit-flip; 13 nonabelian placement groups
(orders to 384) — braided triple-interaction substrate exists at
|X|=2, cataloged. **R2/R3 staged**: signed state sum (inverse op +
negated weight at negative crossings); formal R2 leaves the trefoil
sum identical; R3 verified as the cocycle equation over all 64
triples — all three move families now matched to their funding
axioms (R1 ↔ degeneracy, R2 ↔ signs, R3 ↔ cocycle). Open: the
sparse–dense transition as a decoherence dial; deriving the
decoration as the discrete remnant of the metric flip; a 3-cocycle
on the order-384 placement group.

## The forced compensator (0015)

0014's opens executed (`exploration/0015`, `output/0010`). **No third
channel preserves the flip**: the deficit is pure shape (scale-
invariance verified by transport), and sweeping all two-direction
environments plus channel multiplicity, δ < π strictly everywhere
except the two-party web (max 2.4619; orthogonal channels minimize at
1.8403; doubled ≠ single — measurement intensity reshapes the cone).
So the residual π − δ lies strictly inside (0, π) for every
intermediate web: a binary carrier cannot hold the flip, and **if
round-trip trust is binary, densification forces a continuous U(1)
compensator — the amplitude tier as geometry's change-maker**,
mirroring the arithmetic result that amplitudes complete the paradox
buy-back. **The ledger closes at 0.016%**: unwrapped transport around
the 3-ring (6.2644) = atomic deficits (5.8054) + halo integral
(0.4579) — atoms + halo and nothing else; compensator table
φ(k) = π − δ(k): 0, 1.206, 2.157, 2.636, 2.835 → π. **Tetrahedral
weights exist for every orbit** (nonconstant, all 21 orbits, p = 2,
3, 5; p = 2 enhancements on several; nonabelian witness verified on
all 64 states): the census is a nonempty enumerated starting set for
a level-2 state sum. Open: φ as a mutual-information quantity (the
exchange-rate law); deriving binary trust from the causal-order
decoration; staging the movie move set over census weights.

## The exchange rate (0016)

0015's opens executed (`exploration/0016`, `output/0011`). **The
compensator is an information functional**: the cone angle factors as
Θ = ∮√(J_ang|rad/J_rad)·dφ = ∮√(C/E)e^{−I}dφ with I the Gaussian
mutual information between radial and angular score errors — the
deficit splits exactly into an anisotropy part and a correlation part
(k=2: 2.758 + 0.384; k=12: 0.495 + 0.010), anchored by two exact
facts: any constant SPD information matrix is flat (∮√detA/A_rr = 2π,
verified over random A), and **removing the beacon's own channel
removes the atom (transport 0.00000): participation curves,
spectating does not** — the apex exists only for participants, and
the amplitude phase is priced in the web's own currency. **Binary
trust derived**: generic double points have two-point fibers
(Whitney), monodromy acts through Sym(2) = Z₂ (model cover verified:
sheet flips iff winding odd), triple points are unlinkable — 0015's
conditional discharged; the U(1) compensator is forced with value
pinned to π − δ by continuity (max step 0.049 over the family).
**Time reversal**: 19/21 orbits keep nonconstant bidirectional
weights; the two casualties are exactly the (4,4) orbits (placement
group 384) — **chiral weights live precisely on the deepest
braiding**; a nonabelian bidirectional witness verified both
directions. Open: the correlation share's decay law (two-party
effect?); chiral weights as an arrow-of-time invariant / framing-
anomaly shadow; the cup/cap algebra — the last unstaged move family.

## Known gaps

- Whether P4 (or MRE inside a PR-box) tightens the bound to Tsirelson — the
  quantum-selection question. Open and tractable (`exploration/0007` step 3).
- Quantum-MRE equivalence to Lüders / Petz recovery — open.
- Frustration ≅ contextuality as cohomological structures — now shown in the
  finite revision-dynamics frame (`exploration/0010`): the liar-detection
  parity and the context obstruction are computationally the same class,
  the obstruction dies on the double cover, and its cost is measured
  (forced entropy = log₂ of the holonomy group's smallest orbit; Haar
  floor; negativity 1/2 on the phase fiber). Continuum case still open.
- "Correlation sources curvature" as an Einstein-like equation on the
  information manifold — speculative; standing candidate. Sharpened by
  `exploration/0012`: in the defect reading the *total* curvature is
  topological (a conservation law, not a source law), so any such
  equation must be a redistribution law. The concrete missing step is
  a deficit angle computed from the Fisher metric around a degree-k
  interaction node.
- No dynamics yet; only kinematics and the update rule.
