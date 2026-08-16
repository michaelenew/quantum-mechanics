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

## The arrow and the branch wall (0017)

0016's opens executed (`exploration/0017`, `output/0012`). **The decay
law is derived and confirmed**: isotropic ambient information has zero
radial/angular score correlation, so the correlation share of the
deficit is second order in the anisotropy — with O(1/k) relative
fluctuation this predicts 1/k (anisotropy) vs 1/k² (correlation);
measured over k = 4…44 the fitted exponents are −0.98 and −1.97.
Dense webs are anisotropy-priced only; **score correlation is a
luxury of sparse company**. **The arrow of time, exhibited**: each
chiral (4,4) weight satisfies the forward tetrahedron identity on all
64 states and *fails* the reversed identity on 32 — backward, the
score is order-dependent, i.e. not defined; the weight is a
set-theoretic arrow of time (existence, not value, detects
orientation). Coordinate reversal (x,y,z) → (z,y,x) maps chiral
orbit 1 onto chiral orbit 2: the two are **mirror twins**, a
parity-conjugate pair — the shape of a framing anomaly, locus and
exchange both matching. **The branch wall**: imposing the CJKLS
branch-point condition θ(x,x,y) = θ(x,y,y) = 0 (the level-2 sibling
of the quandle degeneracy that 0006 measured to be R1-safety) on the
bidirectional systems leaves **2/21 orbits at p = 2 and 3, both
abelian — every nonabelian orbit is annihilated**. A set-theoretic
invariant from this census cannot be both braided and
branch-point-safe; the measured-shut naive road forks into
branch-point-free movie presentations (where the 19-orbit census
stands) or nonabelian weight targets. Open: state sums over
branch-point-free presentations of real 2-knots; tying the 32-state
failure pattern to an anomaly class; weights valued in the order-384
placement group.

## The wall theorem (0018)

0017's opens executed (`exploration/0018`, `output/0013`). **The
movie state sum exists**: branch-point-free abstract movies carry
Z(movie) = the weight distribution over all initial colorings —
tetrahedron-move invariant at any embedding (verified through an
arbitrary strand injection after a prefix, all 256 states),
distant-commutation invariant, and separating. The chiral arrow is
**fiberwise**: the reversed movie's fiberwise flips split 16/16, so
Z is ordering-independent even where the per-state functional is
ill-defined — the local anomaly cancels in the aggregate, the arrow
lives one level below the partition function. **The anomaly is a
polynomial**: F(s) = left ⊕ right fits exactly at degree 1
(orbit 1: 1+s₁+s₃+s₅; orbit 2: 1+s₀+s₃+s₄ — each reading one
placement's strand slots), is *canonical* (every nonconstant forward
weight gives the same F), balanced (32/64 — which is why the
aggregate cancels), and the mirror-twin relation descends to F as a
strand relabeling (swap 0↔1, 4↔5). **The wall is a theorem over
every group**: branch-point degeneracy leaves only two free weight
values, turning the bidirectional identities into word equations
valid over any target; universal cancellation alone forces
a = b = e on all 19 walled orbits (chiral systems contain e = a,
e = b outright); the abelianized lattice (|Z²/L| = 1, perfect-
subgroup argument) independently walls all solvable targets; brute
force over Z₂,Z₃,Z₅,S₃,D₄,Q₈,S₄,A₅ confirms, matching 0012's kernel
dims exactly. The two unwalled orbits' full systems are ab = ba and
a = b: **zero noncommuting weight pairs exist across the census and
every group** — the escape is branch-point-free surfaces or
twisted (beyond-group) coefficients, not a bigger group. Open: the
spun-trefoil test with real movie presentations; whether F pulls
back along embeddings (globalizing the arrow); the wall at |X| = 3;
twisted coefficients.

## The continuum limit (0019)

O2 pressed from both framings (`exploration/0019`, `output/0014`).
**The atom of a weighted channel**: a lone channel of strength w is an
exact cone, δ(w) = 2π(1−(1+w)^(−1/2)) (transport-verified); weak law
δ → πw (correction −3w/4); saturation δ → 2π as w → ∞ — the extremal
per-defect bound m < 1/4G as a single channel's asymptote; and
**ambient screening with a discovered closed form**: a weak atom
inside ambient I + a·eeᵀ is reduced by f(a) = (1+a)^(−1/2) (matched
<2e−3; isotropic case f = 1/c exact by algebra) — ambient information
renormalizes the coupling downward. **Fuzzing dissolves the atom**: a
Gaussian-fuzzed source has finite central curvature, interior T(R)
tracking π×enclosed strength, and exterior transport matching the
point atom to <2% at 3σ and 5σ — the shell property for information
webs. **The two framings meet**: quadrature refinements and random
clouds both converge (errors → 0.0017 / 0.0088) to the transport of
the continuous-source metric (per-point polar integration, no source
discretization) — the limit of points and the fuzzed distribution are
the same object. **The local law**: Brioschi curvature against
strength density s(x) = Sρ(x): K/(πs) = 0.9802 at S = 0.02, → 1 as
S → 0, spatially uniform (0.94–0.95 across the profile at S = 0.05),
finite-S correction negative (slope ≈ −0.93 — screening at the field
level). **K(x) = π s(x) in the weak limit ⇔ K = 8πG ρ_mass with
ρ_mass = s/8G: participation density is mass density — the flagged
"correlation sources curvature" row is now a measured equation.**
Open: the two analytic derivations (linearized K = πs; the screening
form); the nonlinear law (determinant/screening candidate); dynamics
on top of the equation (O1); the Lorentzian step (O3).

## The divergence and the current (0020)

O2's rigor and O1 pressed together (`exploration/0020`,
`output/0015`). **K = πs is proved at the linear tier**, every step
machine-checked: the weighted cone is exactly flat off-apex;
linearized curvature is a total divergence K_lin = div V, whose flux
for a point channel is πw at every radius (closed form V·n =
w·cos²θ/R) — so K_lin = πw·δ² and superposition gives K = πs;
Richardson extrapolation pins the constant (1.0002). **The screening
law is derived** (δ = πw/√(1+a), two circle integrals) and its
general form δ = πw/√det A₀ measured to <2e−3 including correlated
ambients: the local coupling is 1/√(information volume). **The trace
identity**: tr h(x) = S_total everywhere (machine precision) — the
web stores its total strength locally at every point; only the
traceless anisotropy sector varies and curves. **Honest negative**:
bare pointwise screening under-corrects the finite-S field ratio at
every S — ambient gradients carry the rest; the nonlinear law is
bounded, open. **O1/O5 read off the proof**: K_lin = div V makes
∂ₜK + div J = 0 structural for any motion (the linearized
Bianchi/conservation pair is free); verified as the jump law (a
moving defect changes a loop's ∫K only on crossing, by exactly its
atom), the continuity law ∂ₜK + div(πsv) = 0 (moving fuzzed source,
6 stations, <3%), and **no pair force** (atom independent of partner
distance to 1.6e−6; nothing pulls — exactly 2+1). Geometry has no
autonomous dynamics in this regime: field equation + conserved
response + free matter motion is the complete 2+1 structure; the
dynamical question moves up to the matter movie and to the
Lorentzian step. Open: the gradient (nonlinear) law; the det-law
one-liner; retardation (c-bounded channel updates — where a light
cone could first enter); coupling source motion to the tetrahedron
event algebra.

## The retarded web (0021)

O3 engaged directly (`exploration/0021`, `output/0016`): channel
directions point at **retarded** source positions (c-bounded update),
one change, three results. **Discovered exact law**: the moving
atom's deficit is δ = πw(1 − v²) — six-digit match at five speeds via
the 0020 flux integral (R-independent to 1e−13), transport-confirmed.
Motion suppresses gravity in the Euclidean web; under v → iv the law
continues to πw(1 + v²) — the Lorentzian moving mass gravitates more.
**The signature lives in one coefficient's sign, set by the update
rule; the state metric stayed Riemannian.** **The fan**: uniform
motion is exactly scale-free, so the wake is K = f(θ)/r² (K·r²
angle-only to 4 decimals) — negative ahead/side, positive astern,
vanishing angular average (transport R-independent). This exposed a
correction: 0014's cone formula assumes a developable apex (B = E′/2)
— false for the aberrated atom (0.528 vs transport's 0.475) and
slightly violated at beacon apexes (0014's 0.04% gaps were real model
error, not numerics); transport and flux are ground truth. **The
light cone, measured**: a kicked source's finished move leaves a
distant loop unchanged (<1e−3) until the news shell arrives; blip on
crossing; exact return (conservation through the transient); K = 0
beyond r = ct to 1e−6; front edge tracks ct with fitted speed
0.988c. **O3's reframe**: the causal cone lives in the response
dynamics over a Riemannian state space — P2's two-tier split computed
in curvature; what O3 still owes is deriving the c-bound itself
(plausibly from the event structure: influence one crossing at a
time). Open: closed-form fan; net radiation from accelerating
sources; deriving c from the interaction algebra; the retarded
two-body problem (velocity-dependent forces?).

## The cone from the web (0022)

O3 closed at the causal-structure level (`exploration/0022`,
`output/0017`): 0021's c-bound is **derived** from P1 + the movie
premise (all change at interactions ⇒ strictly local update). Four
computed steps. **The exact cone**: news occupies precisely the
graph-metric ball (set-equal to BFS, zero tail); the cone's shape is
the connectivity's — polygonal on lattices (anisotropy √2, measured
1.408/1.414 on N4/N8), **round on the random web** (1.127, 1.073):
isotropy of the light cone = statistical isotropy of connectivity,
emergent not axiomatic. **The retarded rule emerges**: gossiped
freshest-records of a moving source converge to the retarded field
y(t − ρ/c) with c the web's own measured front speed (error 6.3% →
4.3% of the move as the web densifies) — 0021's rule is the
continuum shadow of "a node knows only what its channels told it,"
so the light cone, δ = πw(1−v²), and the fan now stand on the
postulates alone. **One web, one cone**: two payloads arrive at
identical ticks at all 2500 nodes (= graph distance) — c's
universality is one interaction graph for all influence; its value
is the a/τ unit conversion (exactly physical c's status). **The two
tiers are sectors**: mid-transient with three sources, tr h =
S_total at every node at every tick (2e−16) while the traceless part
is frozen until arrival then changes — correlational tier = trace
(exact, signal-free), actionable tier = traceless (c-bounded,
carries all curvature by 0020): P2's split is an exact sector
decomposition of the field. Remaining: **O3′ — boost symmetry**
(cone ≠ full Lorentz invariance; the clean (1−v²) law is evidence).
Open: covariance test of the fan/two-body in boosted frames;
radiation; retarded two-body forces; the first-passage constant
(~0.83r/tick) behind c's stability.

## The compass and the flyby (0023)

O3′ decided (`exploration/0023`, `output/0018`). **The covariance
test**, run as the operational relativity principle with a calibrated
floor (7e−9): the screened moving atom in a constant ambient at angle
ψ to the motion is direction-blind at rest (1e−6) but splits in
motion — **pure cos2ψ, scaling exactly as v²** (ratio 4.01), three
orders above floor; a co-moving pair adds a fore-aft **dipole**
(+3.0e−3) from aberration of the partner's direction. **Verdict: the
bare retarded web is causal but not boost-invariant** — an internal
quadrupole compass reads absolute motion at order v². Diagnosis by
exact EM analogy: a retarded scalar sector alone always fails this
way; covariance needs the velocity-coupled gravitomagnetic (h₀ᵢ)
sector, and the measured multipoles specify the counterterm. A
second, independent derivation of the same conclusion: |u| = 1
blocks the anisotropic-strength profile that makes EM's moving field
Lorentzian rather than Galilean — the completion must make channel
strength velocity-dependent. **Radiation**: no wave zone (far
curvature dies as 1/R^3.07; 2D radiation would be R^(−1/2)); the
enclosed budget cycle-averages to the static atom exactly
(0.15142 = 0.15142, breathing <1%) — the (1−v²) suppression is
near-zone redistribution, not loss; eternal uniform motion shows it
at every radius only because its compensating front left in the
infinite past; the web is radiation-free like 2+1 GR. **The
flyby**: a moving probe passing a static partner traces a
velocity-only orientation coupling (spread 1.4e−3 vs static baseline
flat at 1.3e−6), asymmetric between approach and recession — the
web's gravitomagnetism, measured. Open: build the covariant
completion (velocity-dependent strength; does cancellation force the
Lorentzian profile uniquely?); the Galileo/Lorentz dial (bare
retarded = ether, extrapolated = Galileo, strength-corrected =
Lorentz?); closed forms for the quadrupole coefficient and fan;
matter dynamics (does the coupling deflect?).

## The three completions (0024)

0023's prescription executed (`exploration/0024`, `output/0019`): the
velocity-dependent-channel completions are **built** and measured.
**Galilean pole**: channels point at the extrapolated present
position (retarded data only — causal): for uniform motion the field
equals the static field exactly; compass dead; and the c-cone
survives extrapolation (kicked source: K = 0 beyond r = ct) —
Galilean relativity with a light cone, no velocity structure.
**Lorentz pole**: the isometric boost in closed form — channel
w·mmᵀ/(γ²X²+Y²) with m = (γ²X, Y) (anisotropic strength, the 2D
Liénard–Wiechert profile) **plus the boosted baseline**
I + (γ²−1)v̂v̂ᵀ: atom speed-invariant (= static to 5e−5 at v = 0.3,
0.6, 0.8), **no curvature fan** (0021's fan was the ether rule's
artifact), co-moving pair orientation spread 2.8e−7 with ratios equal
to the static pair's — the relativity principle exact, with velocity
structure in strength + baseline. **The baseline is not optional**:
boosted channels over unboosted I give 24.5% atom drift and compass
spread 6.5e−2 — the self-channel/h₀₀ sector must transform; Lorentz
structure requires a dynamical baseline (the Euclidean model carries
by hand the γ² factor a Lorentzian η would absorb — where the minus
sign lives, constructively). **The dial**: ether (compass + fan +
δ = πw(1−v²)) / Galileo (trivially covariant) / Lorentz
(nontrivially covariant) — all three share the derived causal cone;
causality never chooses the symmetry. Open: the composition
experiment (two boosts: velocity addition/Wigner analog — the
model-internal Lorentz-vs-Galileo discriminator); the mixed-velocity
baseline prescription (true two-body at the Lorentz pole); deriving
the pole from a web-native principle; the honest 2+1 packaging
(η + h_μν, linearized-GR correspondence).

## Noether on the web (0025)

The symmetry audit (`exploration/0025`, `output/0020`), run in
Noether's operational form (no action yet: symmetry ↔ measured
conserved object). **Inventory**: translations/rotations exact;
**dilation exact at field level** (g_λ(λx,λt) = g(x,t) to 1e−16,
causal sector included) with the cone pinning z = 1 — the
Schrödinger z = 2 scaling breaks the field (0.08); no-pair-force =
the dilation Ward identity; mass is dimensionless. Time reversal
broken by retardation (0.144 mid-transient, 0 in statics) — the
web's arrow. Mass-broadcast test: ether/Galileo channel trace = w
exactly (mass = central charge); Lorentz trace direction-dependent
(mass mixes into motion) — Bargmann's dichotomy in the field.
**Charges are holonomies**: loop development implemented — rotation
part = mass (calibrated), translation part = mass moment
(2sin(δ/2)×proper distance, <2%), and under interior motion energy
is conserved (3e−5) while the moment drifts perfectly linearly
(bend 0.000) at rate 2sin(δ/2)√(1+w)|v| (0.02%) — **momentum = mass
× proper velocity, read off the monodromy**. Conservation laws are
quasi-local monodromies (the 2+1 ADM structure), conserved by the
causal cone — the jump law is Noether conservation. **The choice
that's not a choice**: in-model Michelson–Morley — signals ride the
derived, rule-independent cone, so only the length standard can
respond: T_∥/T_⊥ = γ at baseline I (ether AND Galileo poles fail:
Galileo's covariance was static-sector only), **null exactly and
uniquely at β = γ²** — the Lorentz pole's boosted baseline. Three
convergent verdicts: operational (MM), algebraic (z = 1 dilation +
massive central charge = Schrödinger-incompatible; Poincaré fine),
central-charge (the trace-broadcast poles are the failing ones).
Open: composition/Thomas–Wigner as confirmation; the action whose
Noether charges are these monodromies (Chern–Simons-shaped);
spacetime monodromy (boost charge, angular momentum); the arrow
here vs 0017's census chirality.

## The action and the Wigner rotation (0026)

Both queued items delivered (`exploration/0026`, `output/0021`).
**The action**: the web's geometric sector is discrete BF theory,
S[θ,B] = Σ_f B_f(curl θ − src_f) — verified lattice-exactly: varying
B gives curl θ = sources (the measured local law K = πs as an EOM);
varying θ gives ∂S/∂θ_e = B_left − B_right, so stationarity forces B
constant — **the second EOM is the conservation law**; gauge
invariance exact; the boundary Wilson loop equals the enclosed
deficit sum exactly and obeys the jump law exactly (Noether
conservation with no numerics). **The action's charges are the
measured charges**: the ISO(2) boundary monodromy (basepoint-framed)
matches 0025's developed-loop measurement on the Fisher web to ~3%/1%
(rotation/moment) at w = 0.05, with the gap growing super-linearly in
w — the screening + halo as the measured non-topological dressing
over the BF skeleton (the dressing, not the core, hosts 0019's open
nonlinear law). **Thomas–Wigner confirmed on solutions**: the
slice-map realization of boosts factorizes as S = R(ω)·P with P =
the single boost to the relativistically-added velocity (8e−17;
|v₃|² = v₁²+v₂²−v₁²v₂²) and ω = the Thomas–Wigner formula (1e−12),
order-reversal flipping the rotation; the twice-boosted two-defect
web equals the once-boosted Wigner-rotated web pointwise (4e−16);
the Galileo pole is abelian. The loop closes: cone derived (0022) →
symmetry forced (0025) → structure constants confirmed on solutions
→ action written with the conserved monodromies as its Noether
charges — the web's geometric sector is 2+1 defect gravity in BF/CS
form, end to end. Open: ISO(2,1) lattice BF (full Poincaré multiplet
variationally); deriving the dressing from an extended functional;
the matter term (dynamics for participants); the quantum tier (BF/CS
quantization meeting the forced U(1) compensator).

## The quantum tier (0027)

0026's action quantized, written as *shape* — the 3+1 prototype
(`exploration/0027`, `output/0022`; all exact algebra). **The Weyl
algebra of holonomies**: at level N the cycle-holonomies obey
UV = ωVU and Wilson operators W(c₁)W(c₂) = ω^(c₁×c₂)W(c₂)W(c₁),
operator-exactly — **the quantum deformation is the intersection
form**: the classical monodromy charges stop commuting and their
noncommutativity is pure topology. **The deficit spectrum**: θ is a
phase, so its conjugate B is discrete — deficits {2πn/N}, insertions
shift by one unit exactly; masses in units 1/(4GN) (participation
quantized by amplitude single-valuedness; the 4π budget caps atoms
at 2N). **The minimal web is a qubit**: N = 2 gives U = Z, V = X
exactly with spectrum {0, π} — **the measured flip δ(2) = π (0014)
is the minimal quantization's only nontrivial deficit**; the ±
double-cover sectors are X eigenstates; φ = π − δ binary at {π, 0};
one bit, two carriers, now as the N = 2 representation of the
action; densification = large-N limit. **Braiding**: W measures the
deficit, WAW⁻¹ = ωA — defects are abelian anyons (quantum face of
"centres braid"); N = 2 circuit phase −1 = the spinor sign.
**The 3+1 template**: B becomes a 2-form, defects strings, charges
on loops and surfaces, intersection becomes **linking** (Hopf Gauss
integral = 1.0000): the 3+1 quantum algebra is the linking/braiding
algebra of loops and surfaces — **which is the movie/census
formalism: the gravity thread and the knot thread are one theory in
3+1**, with the census results (incl. the wall theorem) as its
selection rules. The shape, end to end: holonomy state space,
monodromy charges, BF action (conservation = second EOM), forced
Poincaré symmetry, derived cone, intersection-deformed quantum
algebra, quantized participation, anyonic matter, Fisher dressing.
Open: derive the level N; quantize the dressing (BF + Fisher
kinetic term); the 3+1 build with the template; P5/measurement on
the holonomy Hilbert space.

## Completing the prototype (0028)

The three remaining items (`exploration/0028`, `output/0023`).
**The level**: evenness is a theorem (π ∈ {2πn/N} iff N even — the
measured flip forces it); level 2N is a **central Z₂ (deck)
extension** of level N ((U²,V) obey the level-N relation with
C = V^N central, C² = 1), and the 4→2 deck sectors carry periodic
(Z,X) vs **antiperiodic (spinor)** shift, operator-exactly — the
tower 2→4→8… is the chain of double covers with cat/spinor sector
pairs, and by the arithmetic thread's never-closing theorem the full
object is the inverse limit: **the 2-adic odometer as the level
structure** (structure pinned; the finite rung is the remaining
freedom — plausibly set by the 4π budget). **The dressing closed**:
the exact nonlinear law is **K = πs/det g** — ratios K·det/(πs) =
1.0000–0.99 across the strength sweep, spatial profile, and an
anisotropic two-lump test; the atom law is its proper-area integral
(δ = π∫s/√det = πS/√det A₀ — the det^{−1/2} vs det^{−1} tension was
proper-vs-coordinate bookkeeping); 0020's gradient hypothesis dies;
the far-tail residual is the strength-free tidal halo. Participation
buys curvature at rate π/det g. **The measurement rule reduced to
one bit**: on the web's own degenerate observable (Z⊗Z total-deficit
parity, rank-2 outcome) with a coherent prior, the MRE update
exp(P log σ P)/Z (verified minimal against 200 perturbations)
differs from Lüders PσP/tr by trace distance **0.158**, while
agreeing exactly (6e−17) for rank-1 outcomes and commuting priors
(both = Bayes classically). P5's content: MRE on **states**
(falsifiable departure, sequential-measurement signature) vs on
**instruments** (recovers textbook QM). The 2+1 prototype is
complete: metric → field equation with exact nonlinearity →
conservation-as-EOM → derived cone → forced Poincaré → BF action →
quantized holonomy algebra with 2-adic level tower → measurement
pinned to one testable bit. Open: what truncates the tower; the
halo's law; deciding the measurement bit; then 3+1.

## Nailing the prototype (0029)

The closing pass (`exploration/0029`, `output/0024`). **The
measurement bit, decided by P3**: the sheaf/chain condition — an
unread coarse measurement must not disturb compatible fine statistics
— is satisfied exactly and *uniquely* by Lüders (6e−17; matching in
every outcome-block basis forces PσP/tr), while state-MRE breaks the
gluing (total-variation shift 0.040, basis mismatch 0.147). The
web's oldest postulate selects the instrument tier for P5: MRE at
the channel level reproduces Lüders — **no rift with textbook QM; P5
is a derivation, and the standing quantum-MRE⇔Lüders gap closes.**
**The square-root ledger**: measured log-slopes in det g — density
tier −0.9995, loop tier −0.5000: the holonomy observable screens at
exactly half the density exponent, the same ½ as trust=√information
(stat-tracker) and amplitude=√probability (Born); registered
conjugate square: time↔trust (loop tier, energy) as space↔
distribution (density tier, momentum). **The rung dissolves**: on a
closed web Σδ = 4π = 2N quanta with atoms 1..N−1; N = 2 admits a
UNIQUE universe — four π-atoms, the pillowcase; ≥3 atoms at higher
rungs (no two-body closed universe); counts 1, 13, 81 at N = 2, 3, 4
— the level is the resolution of the world's ledger, content not
law. **The halo's law**: exterior residual exponent −3.92→−4, S²
scaling (3.64/4), σ² scaling (1.89/1.96), coefficient ≈ 0.50:
K_halo ≈ −S²σ²/(2r⁴) — a second-order quadrupole vacuum dressing,
invisible to the linear tier by construction; the classical field
content is fully catalogued. **The 2+1 prototype is nailed**: every
fundamental element forced (metric, cone, symmetry, action, quantum
algebra, update rule); the only freedoms are the world's content and
ledger resolution. Deferred to 3+1: ISO(2,1) variational multiplet,
spacetime monodromy, the movie as matter dynamics, the conjugate
square as design constraint.

## The 3+1 build (0030)

The template executed one dimension up, to the stopping condition
(`exploration/0030`, `output/0025`). **Built, lattice-exact**: the
3+1 action — discrete BF with a **2-form budget** (first EOM: flat
off strings; second EOM: dB = 0, the budget a closed 2-form);
**strings cannot end** (signed source flux through any closed box
vanishes from the lattice's own curls — atom conservation as a
geometric identity); the loop charge = total string flux **linking**
it (Stokes exact, jump law exact, gauge invariance exact). **The
gravity sector lifts transversally**: a straight string's metric is
(2D cone) × ℝ exactly, so every 2+1 law applies per transverse plane
— plus a new closed form: **string–string screening f(α) =
1/√(1 + w cos²α)** — parallel strings screen maximally, orthogonal
strings are mutually transparent. **The cone is dimension-blind**
(3D random web: front = graph ball exactly, octant anisotropy 1.23).
**The quantum deformation is linking** (per-edge Weyl exact; signed
crossing counts = linking on explicit configurations including the
enters-and-exits null case) — and its representation theory is the
movie/census formalism with the wall theorem as selection rule: the
gravity and knot threads are now one construction. Lorentz
kinematics, the level tower, and the measurement rule are inherited
(dimension-generic). **The obstruction, named**: 4D BF is
topological and the web's channels are slaved — no gravitons; the
bridge is Plebanski's simplicity constraint (B = e∧e), and the
web-native candidate is **the Fisher dressing made load-bearing**
(inert in 2+1, necessarily dynamical in 3+1). Second obstruction:
nonabelian string matter walled by 0018 (escapes known); third:
matter still scripted. The program's frontier is one question: what
in an information web plays the simplicity constraint — the
condition that turns topological bookkeeping into gravity that
waves.

## Testing the candidate (0031)

0030's frontier question, answered at the existence tier
(`exploration/0031`, `output/0026`): **the Fisher dressing is
load-bearing in 3+1 — the web waves.** Instrument: a full 3D Ricci
pipeline validated on exact geometries (3-sphere R = 6 to 1e−5;
global monopole closed form to 1e−5; straight string flat to 1e−6).
**Statics**: a point channel in 3D is a global monopole,
R = 2w/((1+w)r²) exact — bulk curvature off-source, impossible in
pure BF; the codim ladder splits the sectors (strings flat = BF;
points curve the bulk = dressing). **Dynamics**: a wiggling string
(retarded nearest-point channels) emits **outgoing curvature
waves** — amplitude 1/R^1.03 (a wave zone; the same rule gave
1/R^3.07 in 2+1: dimension switched the dressing on),
**frequency-doubled** (2nd harmonic ×17,714 over the fundamental —
the quadrupole doubling of GR's binary radiation), **propagating at
c** (radial phase advance 3.968 vs outgoing prediction 4.000, 0.8%;
instantaneous control 1.498 and 10.7× weaker). The web did not need
the simplicity constraint imposed to gain local degrees of freedom;
3 spatial dimensions freed its slaved geometry. The frontier
reframes from existence to **correspondence**: does the wave sector
match Plebanski-constrained BF (two TT polarizations, the quadrupole
formula), or is it a different wave theory? Open: TT/polarization
extraction; the dressing's effective wave equation (the divergence
identity one dimension up); the status of codim-3 point participants.

## The correspondence test (0032) — verdict corrected by 0034

The refined frontier question, answered (`exploration/0032`,
`output/0027`) — **but see 0034: the verdict below is reversed
gauge-invariantly; the measurements stand.** As measured at the
metric level: **the web waves, but not in Einstein's channel — and
the failure is one named object.** Discriminators (plane-wave modes
through the validated pipeline): TT waves carry zero spatial Ricci at
linear order (amplitude-scaling exponent 2.00), scalar/trace respond
linearly (1.00), a vector plane wave is identically zero — so
Einstein radiation is invisible to the linear Ricci scalar, and the
question must be asked of the metric wave. **Polarization**: the
web's far-field wave, decomposed Frobenius-orthogonally against the
propagation direction, is **pure vector** — amplitude = wA/R exactly
(0.6% at R = 3 and 6), at the fundamental (harmonic purity 6×10⁹);
TT/longitudinal/trace all second order (1/R², ~1%). Coherently, the
Ricci wave is quadratic in the wiggle amplitude (1.89) at 2Ω —
0031's frequency doubling explained: it is the vector wave's
second-order composite. **Selection rule inverts**: GR's traveling
string wave is exactly non-radiating (Vachaspati/Garfinkle, imported)
while standing waves radiate; in the web both radiate at 1/R and the
traveling wave is 3.5× stronger. **Verdict**: what propagates is the
direction field u — the only unfrozen piece of I + w uuᵀ; Einstein's
TT gravitons would live in a **propagating strength tensor**, which
is frozen. Same object three 2+1 diagnoses demanded (0023 compass,
0024 baseline, 0025 MM), whose kinematic form 0024 built (mmᵀ +
boosted baseline). Plebanski's simplicity constraint, web-natively:
make the strength sector dynamical; check its radiative modes are
the two TT gravitons. Battery: `mode_metric`,
`polarization_channels`, `string_wave_metric` (any string shape →
retarded channel field). Open: the strength dynamics; whether the
vector wave carries budget or is gauge; the quadrupole coefficient.

## The 3+1 battery (0033)

The computational battery brought to parity with 2+1
(`exploration/0033`, `output/0028`) — and each new instrument
returned an exact law on first use. **The charge reader**
(`develop_loop3`, affine holonomy in 3D): around a string, rotation
angle = the exact atom δ(w) to 1e−5, rotation **axis = the string's
direction**, translation = the 2D moment law 2sin(δ/2)·(proper
distance) to 0.01%; non-linking loops develop to the identity —
charge = linking at the geometric tier, matching 0030's operator
statement. **The codimension ladder**: a 3D point carries a
shell-independent solid-angle deficit Ω = 4π/(1+w) exactly; with the
2D atom this is one law — deficit fraction of a codim-c source =
1 − (1+w)^(−(c−1)/2) — the square-root ledger stacked once per
transverse dimension. **Momentum**: displacing the string leaves the
rotation charge invariant while the translation drifts at exactly
2sin(δ/2)√(1+w) — the 0025 law read natively in 3D. **Additivity**:
two parallel strings give 0.862 of the naive charge sum (constant-
ambient screening estimate 0.897). Parity census: every 2+1
instrument now has a 3+1 counterpart or is dimension-generic; the
one instrument without a target is a dynamical-strength-sector
meter — because the sector doesn't exist yet (0032). Open: the
strength dynamics; boosted-string charges; the ladder at general c.

## The gauge audit (0034)

The severity question — does 0032's wrong polarization force
falsified predictions? — answered by auditing gauge-invariance
(`exploration/0034`, `output/0029`): **no, and the verdict of 0032
reverses — the invariant wave is Einstein's.** New instrument: the
full 3D **Ricci-tensor** pipeline (validated: 3-sphere Einstein
condition to 1e−5; TT plane waves have *linear* Ricci tensor −½∇²h
to 0.1% — invisible to the scalar, visible to the tensor; vector
plane waves identically zero). The decisive 3D fact: Weyl ≡ 0, so
Ricci determines Riemann — zero tensor = flat = pure coordinates.
**The audit**: the web wave's Ricci-tensor polarization is
**TT-dominant, fraction 0.977 at R = 3 and 6** (channel halving
exactly: 1/R); the metric-level vector wave carries 1–2% of the
invariant curvature — gauge dressing. **The linear TT wave**: the
dominant component R_xz (TT, in the jitter×string-axis plane) is
linear in A (0.98), fundamental-pure (>1e3), exactly 1/R
(1.170 vs 7/6), outgoing at c (1.998 vs 2.000; instantaneous
control 337× weaker) — a genuine linear TT curvature wave from the
cross-derivative (radial retardation × string-axis structure) that
plane-wave intuition and the scalar instrument both miss; the
diagonal 2Ω quadratic tier is the quadrupole echo 0031 saw.
**Severity verdict**: a physical vector wave would have been fatal
(LIGO polarization, pulsar dipole bounds, waveform frequency), but
no gauge-invariant observable at linear order transmits it; what is
invariant has the Einstein signature. 0032's strength-sector claim
corrected: the direction field alone carries TT radiation; the
strength tensor is demanded by velocity statics (0023/0024/0025),
not by waves. Remaining risks, named: second-order scalar admixture
(long 0.19/trace 0.10); luminal traveling wiggle radiating where
Nambu–Goto exactly does not (matter sector, unconstrained by data);
and the unbuilt **time sector** (lapse/shift) — now the program's
sharpest missing construction. Battery: `ricci_tensor`.

## The time sector (0035)

0034's sharpest missing construction, built — and it absorbs three
fronts at once (`exploration/0035`, `output/0030`). **The covariant
null-channel metric**: k_μ = ℓ_μ/(u·ℓ) (retarded null vector,
normalized by the *sender's clock*), g = η + w·kkᵀ — Kerr–Schild
form. Three derived consequences, machine-verified: (1) **the web is
the slice** — static k = (−1, n̂), spatial block = I + w·n̂n̂ᵀ
exactly; (2) **the strength law is derived, not chosen** — moving
slice = I + wD²n̂n̂ᵀ exactly, D the Doppler factor: w_eff = wD²;
(3) **boost covariance is automatic** — machinery on the boosted
worldline = Lorentz pullback of static to 4e−16, so 0024's baseline
was the slice shadow of the null structure and the 0023/0024/0025
statics anomalies dissolve by isometry. Instrument: 4D
Riemann/Ricci/Einstein pipeline validated on flat, static
Schwarzschild–Kerr–Schild (vacuum 5e−7), and boosted Schwarzschild
built by the covariant machinery itself (3e−7). **Implied matter in
closed form**: constant-w point = global monopole equation of state
exactly (G^t_t = G^r_r = −w/r², zero tangential); static string =
cosmic-string spacetime (flat off-axis 1e−6); **GR's point mass is
the same form with w = 2M/(u·ℓ)** — web-vs-GR statics is a strength
profile, not a structure; codim ladder derived for general c
(one-line theorem). **Detector response**: a measured normalization
fork — element-clock metering broadcasts γ(t_ret) undecayed
(non-decaying trace wave, Ricci/Riemann ~1: the photon-rocket
pathology, rejected); system-clock metering gives E_ij = R_{0i0j}
**TT at 0.982–0.992, exactly 1/R, vector second order** — 0034's
caveat closes: detectors see the TT wave. The 4D Ricci wave is
0.19–0.20 of the Riemann wave: dominantly Weyl, with a measured
~20% radiative stress admixture as the quantified departure from
vacuum GR. Open: the Newtonian limit (what makes w run as 1/ρ —
now the sharpest gap); the clock principle; whether the 20% is
rule-artifact or falsifiable physics; energy flux/quadrupole
coefficient. Battery: `riemann4`/`ricci4`, `ks_metric`, `cov_k`,
`E_and_ric`.

## The Newtonian limit (0036)

0035's sharpest gap closed from the web's own field law
(`exploration/0036`, `output/0031`). The 2+1 measured law K = πs
says curvature lives only at participation — flat off-source.
Lifted to the 4D null-channel metric (G_μν = 0 off-source), that
principle **selects the strength profile**: for w ∝ ρ^(−p), the
off-source Ricci vanishes at **p = 1 only** (8e−7; p = 0, 0.5, 1.5,
2 all fail by 4–5 orders) — w = 2M/ρ, **the Schwarzschild profile**
(uniqueness beyond power laws = Birkhoff, imported). Geodesics:
the bare constant-w point exerts **zero force** (the 2+1
no-pair-force lifted, machine-zero at two radii); the selected
profile gives **a = −M/r² to six digits** and **Kepler ω²r³ = M
exact** — attraction is the profile, and the profile is the field
law. The constant-w monopole of 0031 rereads as a violation of the
web's own law (a stress halo everywhere), not a virtue. Registered
(no assert): strength = √(diluted flux) gives exactly 1/ρ in 3D —
the ½ exponent's **fifth** appearance (trust = √info, amplitude =
√prob, det^(−1/2) screening, codim-ladder step, now Newton): the
ledger that prices measurement may price gravity. Open: the 4D
field equation (turn selection into derivation); the √flux
mechanism; precession/light-bending (one command away); two-body
post-Newtonian.

## The classical tests (0037)

The Einstein-vs-Newton discriminators, run through the
vacuum-selected metric, plus the first two-body measurements
(`exploration/0037`, `output/0032`). **Light bending**: null
geodesics give 4M/b to 0.6%/0.3% at b = 1, 2 — Einstein's full
deflection, twice Newton's; the 1919 factor of 2 lives in the null
channel structure. **Perihelion precession**: prograde, exactly
repeatable (spread 6e−8), ratio to 6πM/p = 1.053 at M/p = 0.011 and
1.021 at M/p = 0.0044 with the *same* excess coefficient (~4.8×M/p)
— the gap is the second-order term; the advance converges to
Einstein's formula as M → 0. **Two bodies** (superposed
vacuum-profile channels): the off-source violation scales exactly
as M₁M₂ (48.7/48.3/48.2 over a 4× range) — the web's nonlinearity
localized, where the post-Newtonian sector lives; far-field masses
add (−(M₁+M₂)/r² to 0.4% at r = 10); **channel nullity** — a single
channel is exactly null in the metric it creates (2e−16, the
Kerr–Schild identity: each channel rides the very cone it builds),
and fails at O(w₁w₂) with two sources: **interaction is
cone-bending**. Battery: `geodesic_step`, `future_u0` (the
past-directed-root trap), `light_bending`, `run_orbit`, `g_two`.
Open: the two-body fix rule (candidate: 0020's screening one tier
up — check against Einstein–Infeld–Hoffmann); orbiting-pair
radiation vs the quadrupole formula (strongest correspondence test
now in reach); the 4D field equation whose nonlinearity is the
measured O(M₁M₂) term.

## The binary test (0038)

The strongest correspondence test, run (`exploration/0038`,
`output/0033`): two vacuum-profile sources on a circular orbit
(v = 0.2), covariant retarded channels superposed, against GR's
retarded quadrupole formula computed numerically from the same
worldlines (predictor sanity: face-on/edge-on = 2.000, circular
polarization on axis). **The quadrupole formula is missed:
face-on ratio 0.014 (70× too weak), edge-on 0.47 — and the pattern
inverts** (GR loudest face-on; the web nearly silent there; the
dipole cancellation itself works). Vacuum structure splits the same
way: the on-axis wave is a vacuum wave (Ricci 1.9e−8); the orbital
plane radiates large non-vacuum stress (4.8e−3 > the Riemann wave)
— the O(M₁M₂) interaction zone radiating. **Diagnosis**: linearized
GR's moving-source solution is the tensor Liénard–Wiechert
potential 4m·u_μu_ν/(u·ℓ) — momentum flux in the tensor structure;
w·kkᵀ lacks the m·v_iv_j sector at order v², which is exactly the
quadrupole's order (they agree exactly for uniform motion —
acceleration is where they part). Third appearance of the
anisotropic-strength object (0024 kinematics, 0034 statics, now
radiation). Scoreboard: **single-source sector fully Einstein;
the two-body rule is the program's frontier**, its failure measured
(0.014/0.47/O(M₁M₂)). Open: the fix rule — channels carrying the
momentum-flux tensor (test: tensor-LW channel pair sector, re-run
this module; note momentum is already a monodromy charge the
channel must broadcast); then in-model Hulse–Taylor energy balance.

## The momentum channel and the bond (0039)

0038's deficit closed in two steps, ending on the founding claim
(`exploration/0039`, `output/0034`). **The momentum channel**: the
sender broadcasts its stress tensor metered by its clock,
h = [4m·uuᵀ + 2m·η]/(u·ℓ) (tensor Liénard–Wiechert); static limit =
linearized isotropic Schwarzschild exactly; for uniform motion it
agrees with the null channel at the gauge-invariant E_ij tier to
O(m) — the broadcasts part only under acceleration. **Wave zone**
(R/λ ≈ 6; 0038's R = 3 was near zone): null channel face-on ratio
0.001 — no quadrupole radiation at all; momentum channel **0.528 =
one half, by theorem** — free particles radiate from ∫T_ij = Σmγvvᵀ
while the quadrupole formula's ½Ï uses source conservation, and for
circular orbits the vvᵀ term is exactly half of Ï. **The missing
half is the bond**: the binding interaction's stress must radiate —
the pair's mutual channel, their *correlation*, carries budget and
sources curvature: the program's founding claim is quantitatively
the other half of the quadrupole formula (it also explains 0037's
O(M₁M₂) static violation and 0038's in-plane non-vacuum radiation).
**The bond channel, built and verified**: its integrated stress is
the conservation deficit S = ½Ï − Σmγvvᵀ (from the worldlines, no
model), broadcast retarded from the pair's center — **the
quadrupole formula is reproduced: face-on 1.017/0.988, edge-on
0.978/1.005 (~2% = O(v))**. The channel ontology at this tier:
(i) participation → statics/Newton; (ii) momentum flux → the free
half; (iii) the bond (correlation) → the other half. Open: resolve
the bond spatially and check it cancels the O(M₁M₂) static
violation; derive S_ij web-natively (virial = force × proper
separation, both 0025 charges); in-model Hulse–Taylor;
self-consistent motion.

## The bond is a string (0040)

What the bond *is*, in closed form, confirmed by two independent
routes (`exploration/0040`, `output/0035`). **The virial law**:
the conservation deficit closes as **S_ij = −(m₁m₂/d)n̂ᵢn̂ⱼ =
−(F·d)n̂ᵢn̂ⱼ** (1e−8) — the bond's integrated stress is a pure
tension along the line joining the participants, magnitude force ×
separation (0039's 2% residual identified as γ−1). **Measured from
the field itself**: in prolate spheroidal coordinates (masses at
the foci) the field-stress cross-terms reduce to two universal
integrals — trace = 1.000000 (the exact calibration) and
longitudinal = 0.000000 (the result) — giving ∫t_ij = −(m₁m₂/d)n̂n̂ᵀ,
*identically* the virial bond: **the bond is not an add-on, it is
the field between the participants**, and its integrated stress is
a stretched string. **The anti-string**: tension T = m₁m₂/d² =
exactly the force; energy μ = −m₁m₂/d² = the binding energy; so
**μ = −T**, and since a string's deficit is 4π(μ+T) (verified on
four string types with the 0033 charge reader: cosmic string
0.25129, mass line/strut 0.12564, **bond 0.00000**), the bond has
**zero conical deficit while carrying the whole binding energy**.
The theory's two string species are one equation of state's
extremes — cosmic string (μ=+T): all deficit, no attraction; bond
(μ=−T): all attraction, no deficit. The bond carries budget but
**no holonomy charge** — invisible to the charge reader, exactly as
correlation (not participation) must be: P2's two tiers as two
string equations of state. **In-model Hulse–Taylor**: radiated
power 4.1947e−5 vs GR's quadrupole 4.1943e−5 — **ratio 1.0001**;
the γ-bond variant gives 0.980, the spread being γ−1 = v²/2 (the
1PN correction the formula doesn't capture — the honest floor).
Battery: `gauss_legendre`, `radiated_power`, `tt_project`,
`bond_stress_closed`. Open: does the bond cancel 0037's O(M₁M₂)
static violation (completing the two-body rule); the web-native
derivation of T = F; N-body pair sums; the bond's quantum (no
deficit ⇒ not charge-quantized — candidate: entanglement, the ½
ledger).

## The bond ledger (0041)

0040's opens, three answered and one registered
(`exploration/0041`, `output/0036`) — with a coincidence that turns
out to be a condition. **The local negative**: 0037's static
O(M₁M₂) violation is *not* locally the bond's field stress (pointwise
G_ij/t_ij scatters −603..+618 against 8π = 25.1) — the bond is an
integrated, gauge-invariant object and the superposition's local
residual is pseudotensor gauge; 0037's "violation" is the two-body
gauge problem, not a local defect. **Tension is the force, always**:
for F = k/d^(p+1) the virial deficit is −(F·d)n̂n̂ᵀ at every exponent
(p = 0.5, 1, 2, 3; 1e−8). **But μ/T = −1/p exactly**, so μ + T = 0 —
zero deficit, verified through the charge reader at five exponents —
happens **only at p = 1, the inverse-square law**, which is exactly
what the web's vacuum principle selected (0036). *The web's field
law is the one for which correlation carries no participation
charge*: a theory whose two tiers must stay distinguishable has one
force law available. **The dimensional selection**: in d spatial
dimensions the harmonic profile gives p = d−2 and the transverse
charge (μ+T)/T = (d−3)/(d−2) — **zero only at d = 3**, which is also
the only dimension where a bond (a line) is codimension 2 and the
missing charge is a conical deficit at all. The two-tier postulate,
the inverse-square law, and three spatial dimensions are one
condition. **N bodies**: the 3-body conservation deficit is exactly
the pair sum of bonds (2e−16) — participation additive (Σm_a,
holonomy charge), bonds bilinear (Σ_{a<b} m_a m_b): **charges add,
bonds multiply** — marginals vs joints, entropy vs mutual
information. **The bond's quantum** (registered): no deficit ⇒ no
2πn/N charge, but bilinear in participations ⇒ weights n_a n_b, the
multiplication table — the shape of entanglement, not of charge;
the open construction is the bond's operator with classical limit
tension = force. Open: that operator; beyond power laws; a
constructive two-body solution; the d ≠ 3 measurement (would upgrade
the dimensional selection from extension to theorem).

## The bond operator and the dimension theorem (0042)

0041's three fronts moved (`exploration/0042`, `output/0037`).
**The dimension theorem, measured**: a general-dimension curvature
pipeline (`ricci_nd`) shows the point channel's off-source Ricci
vanishes at **p = d−2 and only there** (d = 3: 3e−7 at p=1; d = 4:
7e−7 at p=2; d = 5: 1e−6 at p=3, against 1e−2-scale failures
elsewhere) — the web's vacuum principle selects the **harmonic
profile in every dimension**, so with μ/T = −1/p the bond's
transverse charge (μ+T)/T = (d−3)/(d−2) vanishes only at d = 3:
**three spatial dimensions is the unique dimension in which
correlation carries no participation charge**. 0041's extension is
now a measurement. **The bond's operator**: 0041 predicted a
product structure on the charge lattice, and the quantum tier
already had exactly one — the **mutual braiding phase ω^(n_a n_b)**
of two defects (0027's abelian anyons), built from the level-N Weyl
algebra. Verified at N = 5: its spectrum is the **multiplication
table** where the charge's is the addition table, and it
**separates states the total charge cannot** (every charge sector
holds three distinct bond values) — correlation is not a function
of the marginals. With m = n/(4GN), bond energies go as n_a n_b:
**the bond's quantum is the square of the charge quantum**, one
tier apart in the ½-ledger. **Where the bond's energy lives (a
trap)**: modelling the bond as independent *matter* overshoots the
binding energy by exactly 2.000 — the bond is field; its stress is
a legitimate source (the quadrupole's missing half) while its
energy is already in the field's nonlinearity. The 0034/0035
channel adds 4S_ij/r to the **spatial block only** — the
construction that reproduced Einstein's luminosity is exactly the
one that avoids the trap, with the reason now measured. Battery:
`ricci_nd`, `ks_point_nd`, `bond_phase`. Open: the bond's action
(both ends now pinned — tension = force classically, ω^(n_a n_b)
quantum-mechanically); d ≠ 3 radiation; a genuine second-order
two-body solve; whether the binding energy is the braiding phase's
semiclassical limit.

## The dimensional trade (0043)

0042's ladder run **down** to d = 2 returns the program's founding
object and shows what dimension trades (`exploration/0043`,
`output/0038`). **The atom is the d = 2 vacuum**: the harmonic
exponent there is p = 0 — constant channel strength — measured as
vacuum (1.5e−6) and nowhere else; the test particle feels **no
force** (machine zero); the deficit is **0.772467** against the
exact atom 2π(1−(1+w)^(−1/2)) = 0.772467. 0014's cone and 0019's
atom are the two-dimensional case of the same field law that gives
Schwarzschild at d = 3, and **0020's "no pair force in 2+1" is now
derived** from the vacuum principle rather than observed.
**Topological vs geometric holonomy**: the charge reader around a
codim-2 source is *exactly* R-independent (0.772467 at R = 0.6, 1,
2, 4; spread 4e−12) while around a codim-3 point it dilutes as
2πM/R (0.4661 → 0.0771) — **the codimension decides whether a
charge is a topological invariant or a curvature integral.** **The
trade**: d = 2 has topological charge and no force; d = 3 has
Newton's force and **zero** bond charge; d ≥ 4 has both. *Three
spatial dimensions is where the bond has traded its charge for a
force* — the unique dimension in which correlation acts without
registering as participation. This refines 0042 honestly: the
braiding phase ω^(n_a n_b) is the **2+1 realization** of the bond's
product structure, while in 3+1 the same bilinearity appears
dynamically as m_a m_b/d — one product structure, two carriers,
selected by codimension (3+1 *strings* get the topological carrier
back: linking, 0030). **The half is kinematics**: 0039's 50/50
split holds for every force law (ratio 1.000000 at p = 0.5, 1, 2,
3), following from mΩ²a = F ⟹ 2mv² = Fd — circular motion alone.
The "missing half" was never gravitational: it is what binding
means for a closed orbit, and gravity only set its tension. Open:
the bond's action (both ends pinned, middle unwritten);
restating the ladder in terms of **codimension** rather than
dimension; the second-order two-body solve; d ≠ 3 radiation (now a
propagator question, not a source one).

## Noether in 3+1 (0044)

0025's programme (symmetry ↔ measured conserved object → action) run
one dimension up (`exploration/0044`, `output/0039`). **The channel
ansatz linearizes the field equations**: for g = η + w·k⊗k with k
null and geodesic, G^μ_ν is *exactly linear* in the channel
amplitude (G/λ constant over an 8× range at three profiles,
deviations 2e−6–1e−5) — so a single channel of any strength solves
the full nonlinear theory (why the vacuum profile is exact and the
classical tests came out exact), and **all nonlinearity lives in how
channels superpose: the bond sector alone**. (Kerr–Schild
linearization, imported from GR; the content is that the web's
channel form *is* that ansatz.) **The ten charges, as 2-surface
integrals** — the 3+1 lift of 0025's loop monodromies (new battery:
`adm_energy`, `adm_momentum`, `adm_angmom`): static E = 0.020000 =
m; boosted E = γm and P = γmv to 0.1% at v = 0.3, 0.6; binary
J_z = 1.0242e−3 vs 2γmav = 1.0206e−3 with J_x,y ~ 2e−14; and
**binary E = 0.039214 vs 2γm + binding = 0.039225** (2γm alone would
be 0.040825). **The ADM integral sees the bond's energy**: the bond
enters as *stress only*, and the constraint converts it into exactly
the binding energy — which is why adding it as matter as well (0042
§3) double-counts by 2. That thread closes. **The conservation laws,
explicitly**: dE/dt = −L with L measured (4.1947e−5 vs GR's
4.1943e−5); the face-on wave is exactly circularly polarized at
ω = 2Ω (amplitude ratio **1.0000**, phase **90.0°**) = pure m = 2, so
**dJ/dE = 2/ω = 1/Ω is measured, not assumed**, giving dJ/dt =
−L/Ω = −2.62e−5; and the orbit's dE_orb/dJ_orb = Ω, so the fluxes
come off in exactly the ratio that keeps the orbit circular. **What
the action must be**: (i) reduce per channel to a form whose field
equation is linear in that channel's amplitude — supplied
*trivially* by BF in 2+1, *nontrivially* by Kerr–Schild in 3+1; (ii)
generate the pair stress −(F·d)n̂n̂ᵀ as the bond, whose energy the
constraint reports as binding. The functional itself is the one
unwritten item, now boxed in from three sides (and must reduce to
0026's S = ΣB(curl θ − src) on removing a dimension). Open: the
functional; an independent J-flux surface integral; whether the bond
is a *constraint* phenomenon rather than a source; the boost
charges.

## The functional (0045)

The action attempted (`exploration/0045`, `output/0040`): **half
written cleanly — resolving 0030's obstruction — half falling back
to the prototype path.** **The channel is a Maxwell field**: the
web's own channel one-form A_μ = w·k_μ has *exactly* the
Liénard–Wiechert field strength (1e−8 static, 2e−8 boosted; the
potentials differ by a pure gradient) — the metric's building block
is a linear gauge field. **The metric is its square** (the
Kerr–Schild double copy, imported from GR, verified for the web's
channel), and that one fact explains four standing measurements:
0044's linearization (gravity is linear per channel because the
gauge theory is), 0041's charges-add/bonds-multiply (addition in the
single copy, multiplication in the square), 0042's bond quantum =
(charge quantum)², and the ½-ledger at the top of the theory — **the
channel is the amplitude, the metric is the probability**. Measured:
the single copy's harmonic vacuum selects p = d−2 for d ≥ 3, the
same ladder gravity selected (0042). **0030's obstruction
resolved**: the 3+1 single copy is not BF but **Maxwell** — genuine
field strength, radiative, double-copying to gravity *with*
gravitons; in 2+1 the correspondence degenerates (gravity takes
constant w — the conical defect, no force — where Maxwell gives a
logarithm with force), matching 0023's measured no-radiation. The
obstruction was an artefact of taking BF as the 3+1 single copy.
**The honest negative**: off-shell squaring fails — scanning the
metric cross-term coefficient leaves the two-body violation minimal
at c = 0 (5.2e−3, rising to ~5e−2 at c = ±1), so the double copy is
a *solution-level* correspondence and the bond enters as source
stress (the verified route). **State of the action**: single copy
written — S = −¼∫F²d⁴x + Σ q∫A·dx with g = η + φk⊗k, A = φk, k null
geodesic, linear per channel, degenerating in 2+1 to 0026's
S = ΣB(curl θ − src); gravitational functional on the **prototype
path**, fixed by its charges and conservation laws (0044) rather
than derived by squaring. Open: an off-shell squaring map (now
sharply constrained); verifying the single copy for *accelerated*
sources; k-null as the one axiom the double copy needs and the web
supplies (0037); sharpening the 2+1 degeneracy into a statement
about which gauge theories double-copy to topological gravity.

## The frame functional (0046)

The critical pass through the action derivation, and the path it
opened (`exploration/0046`, `output/0041`). **The flaw in 0045**:
its off-shell negative used a cross term of weight √(w₁w₂) — a
guess; if the metric is a square the additive object is the *frame*
(g = e·η·eᵀ), which dictates its own cross term
¼w₁w₂(k₁·k₂)(k₁k₂ᵀ+k₂k₁ᵀ). **The exact tetrad**: e = 𝟙 + ½w·kkᵀη
squares to Kerr–Schild *exactly* (1e−15, including w = 3 and
Doppler-scaled k — nullity kills the quadratic term). The channel
is the frame perturbation, linear at any strength (0044's
linearization becomes an identity); **the ledger's ½ is the literal
coefficient**; collinear channels superpose exactly (mass additivity
at a point is an identity). **The corrected off-shell test**: the
frame-square cross term *reduces* the two-body violation ~2×
(5.16e−3 → 2.97e−3 at c = 1; minimum 2.5e−3 near c = 1.5) where
0045's wrong-weight term increased it — the frame is the additive
variable; the residual is the genuine second-order bond iteration.
**The functional**: first-order tetrad gravity —
S = (1/2κ)∫ε_IJKL e∧e∧F in 3+1, S = (1/κ)∫ε e∧F in 2+1 — checked
against everything measured: the 2+1 form **is** 0026's BF with
B = e; the 3+1 form is BF with **B = e∧e** (Plebanski satisfied
identically) whose ω-equation d_ω(e∧e) = 0 is 0030's measured
lattice dB = 0; linear per channel by the exact tetrad; the bond as
the e-equation's second-order iteration (integrated cross stress =
the virial bond, 0040); matter S_m = m∫|e(ẋ)|dτ = the sender-clock
rule as a variational principle. **0030's frontier question
answered in the ledger's vocabulary: B = e∧e is "probability =
amplitude²" at the action level** — in 2+1 the tiers coincide
(B = e: topological, additive, no gravitons); in 3+1 the budget is
the square of the frame, and that one squaring is where gravitons,
multiplicative bonds, and bond quantum = (charge quantum)² come
from. Battery: `channel_tetrad`, `square_frame`, `g_frame_cross`.
Open: lattice Palatini (e on 0030's lattice, B = e∧e imposed,
torsion equation verified); derive the sender-clock rule from
δS_m; B = e∧e as an operator identity on the level tower; iterate
the e-equation once to confirm the two-body residual drops an
order.

## The derived channel (0047)

0046's matter-variation front closed, and the principle underneath
it found (`exploration/0047`, `output/0042`). **The channel rule is
the functional's retarded Green function**: varying the action, the
A-sector gives A = q·u/(u·ℓ) — the Liénard–Wiechert potential, which
*is* the channel (1e−8) — and the e-sector at linear order gives the
tensor LW, which *is* the momentum channel (0039's ansatz, now δS).
**The sender-clock normalization u·ℓ is the Jacobian of the retarded
projection — derived, not chosen**; 0035's clock-principle open
closes and the element-vs-system fork dissolves (integrate the Green
function over the conserved source — no per-element choice exists).
**Conservation is the operative principle, measured**: wave-zone
Ricci/Riemann ratios — conserved binary (LW + bond) **0.014
face-on, 0.042 at 45°**; non-conserved (LW only) 0.067 and **0.909**
— the Green-function field is vacuum iff the source is conserved,
failing hardest exactly where the bond radiates. The bond (binary)
and the internal tension (string) are the *same*
conservation-completing term at two source types; 0035's ~20%
admixture retro-diagnosed as the nearest-point (non-conserved
effective source) artifact. **The string's tension** (partial): the
Nambu–Goto tension term halves the wiggling string's admixture
(1.14 → 0.46 traveling, 1.13 → 0.53 standing), but truncated open
ends break conservation (ratio non-convergent in window size) — the
Vachaspati test stays open pending a **closed-loop** source, with
the sharp prediction: traveling modes silent, standing modes
radiating. **The operator square**: the budget operator as the
symmetrized square of the frame operator has holonomy spectrum
ω^(n_a n_b) = 0042's bond table — "budget = frame squared" now
holds at every tier: metric (exact tetrad), charges
(add/multiply), action (B = e∧e), operators. Open: the closed
loop; the lattice Palatini (carried); separating O(v) from O(h²)
in the 1–4% conserved residual; a consolidation pass stating the
full derivation chain postulates → metric → cone → Lorentz →
functional → channel rule with each link's evidence.

## The chain (0048) — consolidation

The derivation stated end to end (`exploration/0048`), with an
executable table of contents (`output/0043`): **twelve keystones,
one suite, 0.7 s, all passing** — ledger (influence = √info, slope
0.500) → atom (0.772467 exact) → codim ladder (4π/(1+w)) → cone
(front = ball, set-exact) → Lorentz (pullback 1e−15) → frame
(e = 𝟙+½·channel squares exactly) → quantum tier (UV = −VU at N=2;
bond = n_a n_b) → vacuum selection (1/ρ vacuum 3e−7, 1/ρ² not) →
classics (Kepler exact; bending 4M/b) → waves (luminosity 0.99 of
quadrupole at reduced quadrature) → bond (virial 1e−8; anti-string
deficit 8e−8) → Green rule (channel = LW 2e−8). Each link tagged
[FORCED/MEASURED/DERIVED/IMPORTED] with its evidence; the one-
sentence statement of the theory recorded; the ½-ledger counted
through every tier (trust = √info, amplitude = √prob, channel =
√metric, frame = √budget). **The honest residue, renumbered**: κ
unfixed (candidate: tied to level N); the lattice Palatini unbuilt;
the Lorentzian η of the 4D lift motivated (L6) but assumed as
arena; the closed-loop Vachaspati test open; the 1–4% two-body
residual unseparated (O(v) vs O(h²)); content and rung (world's
data, not law); P4 → Tsirelson untouched; the arithmetic/continuum
bridges standing.

## Known gaps

Superseded in detail by `exploration/0048`'s "honest residue" (the
maintained list). Standing items in brief: κ normalization; lattice
Palatini; the Lorentzian-arena step; the closed-loop test; the
two-body residual; content/level-rung freedom; P4 → Tsirelson
(`exploration/0007` step 3); continuum versions of the 0010
arithmetic-frame results; matter dynamics beyond scripted sources
and the frame field's full quantum dynamics.
