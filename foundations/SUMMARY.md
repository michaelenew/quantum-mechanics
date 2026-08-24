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
Petz (quantum) uniqueness fixes the metric up to scale. *(0066 caveat:
on mixed states Petz gives a __family__ of monotone metrics; uniqueness
holds on pure states — all coincide with Fubini–Study — and by the
Cramér–Rao selection of Bures. Pure-state channels, as used throughout,
are safe.)* Immediate
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

## The closed loop (0049)

Two post-consolidation residues closed (`exploration/0049`,
`output/0044`). **The exact loop**: a Kibble–Turok Nambu–Goto
solution (unit left/right movers, closed, period 2π; conformal
gauge to 4e−17) — compact, exactly conserved, no ends. **The
measurement**: Ricci/Riemann of its Green-function field = **0.032
and 0.034** at two wave-zone probes — a **14× collapse** from the
truncated open string's 0.46–0.53, joining the conserved binary's
0.014–0.042. The string sector obeys the same law: the
Green-function field is vacuum iff the source is conserved. Two
anomaly threads resolve together: 0032's "inverted selection rule"
was a wrong source model (no tension, open ends), not wrong field
dynamics; and Vachaspati's traveling-wave silence is correctly an
infinite-string statement — a loop cannot carry a traveling-only
mode (both movers must close). **κ is a unit, N is the physics**:
8πG·m_q = 8πG/(4GN) = 2π/N identically — G cancels from the
quantized ledger (the participation→deficit conversion unit, as c
is ticks→length), leaving the level N as the coupling's only
physical datum — already classified (0029) as content, not law.
0048's residues #1 and #4 close. Open: the lattice Palatini (the
last constructive gap); the residual separation; cusp radiation vs
GR's burst structure; loop decay power vs Γ·Gμ².

## The Palatini construction (0050)

The chain's last constructive gap closed, plus two quantitative
fronts (`exploration/0050`, `output/0045`). **The simplicity
constraint counts the gravitons**: 0030's obstruction was a
dof claim, so it is settled by rank — free BF leaves 1 solution per
internal pair against a 1-dimensional gauge orbit (**0 physical
dof**); Palatini's torsion equation on ω has **rank 24 of 24** (ω
determined *algebraically* by e, so the theory is second-order in e
alone); the resulting system gives 10 − 4 − 4 = **2 dof**.
Imposing B = e∧e takes the count from 0 to 2 — the simplicity
constraint is what releases the gravitons, and by 0046 it *is* the
ledger. **The construction on the web's own solution**: solving the
torsion equation numerically for the channel tetrad gives torsion
residual ~5e−17 (machine), and the functional's variables (e, ω)
reproduce the metric route's Ricci to **1e−6 relative on three
non-vacuum profiles** (vacuum profile flat both ways) — 0046's
identification is now a construction. **Loop decay measured**:
Γ = P/(Gμ²) = **45.8 (R = 20), 45.4 (R = 30)** — stable in radius to
1%, against GR's Γ ~ 40–100 for Kibble–Turok loops. **The residual** was
reported here as velocity-not-nonlinearity (0.0138 → 0.0017 when v
halves, identical when M halves) — **corrected by 0051**: that scan
cannot separate the two (h ≈ 4v³ at fixed R/λ), and a distance scan
shows the residual is near-zone contamination falling as 1/R. Battery: `spin_connection`,
`torsion_residual`, `ricci_palatini`, `rank`, `loop_power`. Open:
the strictly discrete action (vary S = Σ ε e∧e∧F on 0030's lattice);
cusp beaming; which PN term gives the v³; and 0048's standing
items (Lorentzian arena, P4 → Tsirelson, matter, arithmetic
bridges).

## The discrete action (0051)

The functional varied on a lattice, the cusp burst, and a
self-correction (`exploration/0051`, `output/0046`). **The discrete
action, varied**: writing S = Σ ε^{μνρσ}ε_IJKL e e F on a 7-point
stencil and differentiating numerically — δS/δω = 2.9e−4 at the
solved spin connection, **falling as a²** (1.15e−3, 2.88e−4,
7.20e−5) so it is discretization error, against **1.27** at a
perturbed connection (ratio 4400); δS/δe = 1.1e−3 at the **vacuum**
profile against 2.63 and 2.03 at non-vacuum profiles. **Both
Euler–Lagrange equations come out of the lattice action** — the
functional is verified variationally, not only by
constraint-matching (0046) or the continuum route (0050). 0050's
open #1 closes. **The cusp burst**: the loop's cusps move at exactly
c (1.0000) along ∓x̂; flux in the cusp direction is 4.85× the
transverse, and the **temporal peak/mean is 34.75 against 1.01
transverse** — GR's beamed cusp burst, the structure cosmic-string
burst searches target. **A correction to 0050 §4**: that section's
"post-Newtonian source structure, strength-independent" was
unsupported — at fixed R/λ, h ≈ 4v³ is determined by v, so the scan
could not separate them. A distance scan can: the residual falls as
**exactly 1/R** (0.02731, 0.01378, 0.00691, 0.00346 at R/λ = 3, 6,
12, 24; same at half velocity), i.e. it is **near-zone
contamination** — the non-vacuum part falls as 1/R² while the
radiative part falls as 1/R, so **the conserved binary's wave-zone
field is exactly vacuum**. Stronger than the claim it replaces.
Open: a self-contained lattice theory (independent link variables,
discrete local Lorentz, exact difference EOMs); the cusp waveform's
spectral index vs GR's |f|^(−4/3); and 0048's standing items.

## The lattice theory (0052)

0051's two opens closed (`exploration/0052`, `output/0047`). **A
self-contained lattice theory**: SO(3,1) group elements on every
link (Λᵀη Λ = η to 7e−16) plus frame vectors, with
S = Σ_x ε^{μνρσ}ε_IJKL e^I_μ e^J_ν F^KL_ρσ built from plaquette
holonomies on a 3⁴ web of **random** links. Under a *large* local
Lorentz transformation at one site, **|ΔS| = 7.1e−15 (relative
4.8e−15) — machine zero**: a discrete theory with a discrete gauge
symmetry, no linearization or continuum limit invoked (ε_IJKL is an
invariant tensor and every factor is based at the same site).
**The field equation is exact on the lattice**: numerical δS/δe =
6.5535113389 against the analytic
2ε^{μνρσ}ε_IJKL e^J_ν F^KL_ρσ = 6.5535113340 (5e−9, the
finite-difference floor) — the discrete Einstein equation holds as
a *difference equation*, not to O(a²); the ω-variation remains the
O(a²) one (0051). **The cusp spectrum**: GR predicts cusp bursts
with harmonics ~ n^(−4/3); measured in the cusp direction the slope
**brackets −4/3**, crossing it in the n = 8–32 decade (−1.224,
−1.302, −1.416, −1.478 over rising windows; low end pre-asymptotic,
high end steepened by finite element count), while the **transverse
direction falls exponentially** (1.63e−3 → 1.6e−16 over n = 2–16,
effective slope −14.6). *Power law only where the cusp beams* — GR's
cusp phenomenology, the basis of cosmic-string burst searches,
reproduced from the channel rule alone. Battery: `lattice_action`,
`plaquette_F`, `rand_lorentz`, `harmonics`. Open (standing from
0048): the Lorentzian arena; P4 → Tsirelson; matter beyond scripted
sources; the arithmetic bridges. Newly available: **the lattice's
quantum tier** — the level-N Weyl algebra on these link variables,
where "budget = frame squared" should become an operator statement
about the measure.

## The quantum lattice (0053)

The lattice theory quantized at level N, full bore
(`exploration/0053`, `output/0048`) — four exact results. **The
ground space derives the Weyl algebra**: the level-N gauge sector on
T² is the Z_N quantum double; degeneracy N² two independent ways
(rank formula; brute enumeration 243/27 = 9 at N = 3); Wilson and
dual loops built from the model satisfy W_x T_x = ωT_x W_x (6.5e−16)
and commute across cycles — **0027's postulated cycle algebra is now
a theorem of the lattice model**. **The 2-form tier is homology**:
on T³ the chain identities d∘d = 0 hold exactly over ℤ (dB = 0 is
the complex's own identity); b₁ = b₂ = 3, so the charge sector has
degeneracy N³ and the budget sector N³ — Poincaré-dual partners
paired by linking. **The square measure prices curvature** (the
headline): the plaquette weight K(F) = Σ_B m(B)ω^{BF} is N·δ_{F,0}
for the uniform budget (curvature *forbidden* — free BF,
topological) but **N·gcd(F, N)** for the squared budget B = e·e
(exact, N = 3, 4, 5, 7, 8) — curvature *priced* at
log(N/gcd(F,N)) per plaquette: **one curved plaquette costs one
level-N symbol of the ledger**. The quantum mechanism of the
graviton release (0050's 0 → 2 count, now as a change of measure),
and the quantum ancestor of K = πs. On the tower N = 2^k the price
is graded by the **2-adic valuation** of the curvature (N = 8:
64, 8, 16, 8, 32, 8, 16, 8) — 0028's odometer arithmetic in the
action. **The measure is a correlated web**: under B = e·e,
budgets sharing an edge carry MI = 0.118/0.143/0.143 bits (N = 3,
5, 7) while disjoint budgets are exactly independent — the
conservation law's quantum seed is correlation; the budget field
has bonds; the web quantizes into a web. Battery: `rank_modp`,
`t2_complex`/`t3_complex`, `K_square`, `mi_shared`. Open: the
constrained model's spectrum (the lattice graviton via a transfer
matrix over the N·gcd weights); the correlated-measure feedback
into K(F); the 2-adic action vs the deck sectors; 0048's standing
items.

## The lattice graviton (0054)

**A gravitational effect derived from the quantized lattice and
computed in it** (`exploration/0054`, `output/0049`). **The
derivation**: integrating out the links leaves an exact measure on
plaquette fluxes, P({F}) ∝ Π_p W(F_p − n_p) with Σ_p F_p = 0 (the
Jacobian is the uniform gauge volume) — and the constraint *is*
0029's closed-universe budget (a mass must be compensated), while a
Wilson loop measures ω^(Σ_R F) by lattice Stokes. **The deficit,
computed**: exact enumeration on a 3×3 torus with a neutral source
pair gives phase **exactly 2πn/N for every loop enclosing the mass**
— independent of the loop's size and shape (p0, p0+p1, the 2×2
block all give +2.09440 = 2π/3) — and **exactly zero** for every
loop that doesn't; verified at N = 2, 3, 4, 5, → 0 as N → ∞. The
conical defect of 0014/0027 recovered as a quantum expectation
value: the chain's oldest object arriving from its newest end.
**The quantum correction**: the identical computation under free BF
gives **|⟨W⟩| = 1.0000 exactly at every loop** — same deficit,
*rigid* geometry — while the ledger's squared measure gives |⟨W⟩|
falling with the loop's **area** (0.4007, 0.1618, 0.0361). The
magnitude is a purely quantum observable with no classical
counterpart: **the square is what makes geometry jitter.** **The
lattice graviton**: in the flux basis V(F) = log(N/gcd(F,N)) is a
curvature quantum's on-site energy and the electric term is its
hopping; Σ F = 0 forces quanta into **± pairs**; diagonalizing the
pair's centre-of-mass motion on a ring gives a dispersion with
**bandwidth 3.86 and group velocity 1.91 — a propagating mode**,
where free BF (V = ∞) leaves the band *empty*. 0050 counted the
release (0 → 2), 0053 found it in the measure, and here it is a
spectrum. Battery: `flux_expectations`, `weight_fn`,
`pair_dispersion`. Open: polarizations (quantize the nonabelian
links — the real spin-2 test); the area law's coefficient; two
masses (the bond's quantum ancestor); 0048's standing items.

## Three quantum fronts (0055)

0054's opens closed (`exploration/0055`, `output/0050`), the first
being the quantum arc's sharpest result. **The quantum simplicity
constraint**: summing the frame factors of B = e∧e inside the action
gives a Gauss sum over *simple bivectors*,
K(F) = Σ_{a,b} ω^{ε_IJKL a^I b^J F^KL}, whose weight depends only on
the simplicity invariant Pf(F) = ε_IJKL F^IJ F^KL/8 — with an exact,
level-independent hierarchy: **flat costs 0, simple (geometric)
curvature costs 2 log N, non-simple costs exactly 4 log N** (N = 2
and 3). *Non-geometric curvature costs exactly twice what geometric
curvature costs*, and nothing is forbidden (no K = 0) — the
constraint is a **suppression by N² per plaquette, not a delta
function**: Plebanski's constraint is *priced, not imposed*. The arc
closes — 0046 identified simplicity with the ledger, 0053 showed the
ledger prices curvature, and here the price resolves **by
simplicity**, the sector where the polarizations live. **The
jitter's tension**: 0054's area law gets its derived coefficient —
the single-plaquette factor f(N) = Σ_F gcd(F,N)ω^F / Σ_F gcd(F,N),
a normalized Ramanujan-type sum (1/3, **2/5**, 1/4, 4/9, 6/13 at
N = 2, 3, 4, 5, 7) — with ⟨W(R)⟩ = f^|R| measured 0.4007/0.1618
against 0.4000/0.1600 (the 4-plaquette value carries the torus's
global-constraint correlation). Geometry's zero-point jitter has a
string tension. **No pair force, quantum mechanically**: the
interaction energy of two sources is **exactly zero at every
separation**, reproducing 0020's classical no-pair-force and 0043's
dimensional trade — the quantization introduced no spurious
dynamics, and the null is sharp because the same measure *does*
produce a deficit and a propagating quantum. Battery:
`simplicity_kernel`, `pfaffian`, `single_plaquette_factor`,
`log_partition`. Open: the **3+1 quantum force** (where the
classical theory gives Newton — the sharpest remaining test);
folding shared-frame correlations into the kernel; counting
polarizations in the constrained measure (the real spin-2 test);
0048's standing items.

## The graviton's mass and the kernel price (0056)

0055's opens closed (`exploration/0056`, `output/0051`); the first
is the quantum arc's most consequential structural fact. **The
graviton is massive; Newton lives at a critical point**: the
curvature quantum carries price V (= 2 log N for geometric
curvature) and hops with amplitude t, giving pair gap Δ = 2V − 4t —
measured +3.52/+1.76/+0.44/**+0.0005**/−0.44 at t/t_c = 0.2, 0.6,
0.9, 1.0, 1.1 (N = 3; same pattern at N = 5). Three phases: **gapped**
(massive quantum ⇒ Yukawa force of range 1/Δ), **critical** at
**t_c = V/2 = log N** (gap closes, massless, long-ranged), and
**condensed** (flat vacuum unstable to curvature pairs). So *the
theory has a Newtonian limit only at criticality* — how a lattice
theory acquires a continuum limit at all, and the honest quantum
status of 0036's classical Newton: the classical chain already sits
at the continuum point; the quantum model must be tuned there. **The
price counts what the curvature leaves alone**: the simplicity
kernel factorizes exactly as **K(F) = N⁴·|ker F|** with
ker F = {b : ε_IJKL b^J F^KL = 0} — flat leaves N⁴ directions,
simple curvature N² (acts in a plane), non-simple N⁰ — so 0055's
0/2/4 log N hierarchy is the **codimension of the kernel** and
"geometric" means "acts in a plane." The Pfaffian was the symptom;
the rank is the cause. **The shared frame correlates neighbours**:
two plaquettes sharing a frame have joint weight
N⁸·|ker F₁ ∩ ker F₂|, giving **0.0265 bits** of mutual information
between adjacent costs (independent would be exactly 0) — cheap
together means their curvature planes share an untouched direction,
the lattice's form of "all curvature 2-forms come from one tetrad";
0053 §4's correlation resolved into its geometric cause. Battery:
`pair_gap`, `kernel`, `m_of`. Open: **quantum Newton** (at t_c,
compute V(d) and test for 1/d — now the sharpest open in the
quantum arc); the critical theory's polarizations (the real spin-2
test, with a specific coupling to sit at); composite-N divisor
structure inside the kernel picture; 0048's standing items.

## Quantum Newton and the selective critical point (0057)

0056's sharpest open closed (`exploration/0057`,
`output/0052_quantum_newton.py`). **The critical dispersion is
quadratic**: on a 3D lattice with on-site price V and hopping t to
six neighbours, E(k) = V − 2t Σ cos k_i closes at t_c = V/6, where
E(k) = 2t Σ(1 − cos k_i) → t k² — ratio E/(t k²) = 0.9867, 0.9967,
0.9992, 0.9998 at k = 0.4, 0.2, 0.1, 0.05. A quadratic dispersion is
a 1/k² propagator, and in three spatial dimensions that is Newton.
**Quantum Newton**: the static potential is the lattice Green
function G(r) = (1/L³) Σ_{k≠0} cos(k·r)/E(k), and *the removed zero
mode is not a regularization choice but the closed-universe budget*
Σ F = 0 (0029/0054). Fitting G = A/r + B on L = 56 gives
A/(1/4πt) = 1.0996, 1.0237, **0.9907** on windows r = 2..8, 4..10,
6..14; holding the window at 6..14 and growing the box separates
short-r lattice structure from long-r periodic images, converging
monotonically **0.8744 → 0.9482 → 0.9907 → 1.0023** at L = 32, 40,
56, 72 with the offset shrinking −0.0145 → −0.0084. So **the
critical quantum theory mediates a 1/r force with the Newtonian
coefficient 1/(4πt) to 0.2%**, and the coupling law is exact —
doubling t halves A, ratio **2.0000**. 0036's classical Newton,
obtained from the quantized model. **Only the geometric sector is
massless**: two price tiers (2 log N geometric, 4 log N non-, per
0055/0056) mean two critical couplings, and at the geometric one the
simple gap is **0.000000** while the non-simple gap is **exactly
2 log N** (2.197225 at N = 3, 3.218876 at N = 5) — the geometric
price itself. That is the mode selection Plebanski's constraint is
supposed to perform, **obtained as a gap rather than an
imposition**. **The priced direction is the self-dual imbalance**:
splitting the curvature bivector over Z_N, Pf(F) is a function of
**|F⁺|² − |F⁻|² alone** (verified over all N⁶ curvatures at N = 3
and 5), so since the price depends only on Pf, exactly **one** of
the six internal directions is priced and the balanced cone is free
— |F⁺| = |F⁻| is not imposed here, it is the statement that the
theory charges for imbalance. Battery: `green_line`, `fit_coulomb`,
`hodge`, `sd_asd`. Honest limits: §1–2's t_c = V/6 is the
single-quantum 3D convention, not 0056's pair convention t_c = V/2
(both correct for their model, neither the full interacting
lattice's); §2 verifies the lattice sum converges to its own
continuum limit under a physically forced zero-mode removal rather
than deriving 4π; §2's propagator is free; §3 plugs the exact tier
structure into a model dispersion; §4 needs 2 invertible, so even N
is excluded. Open: polarization count at t_c (the spin-2 test, now
with a specific coupling and surviving sector); the first
post-Newtonian correction from the lattice; composite N inside the
self-dual reading; 0048's standing items.

## The falsification audit (0059)

`exploration/0059`, `output/0053`. Asks what the program actually
predicts *differently* from GR, and whether data kills it. **The
one-body sector is exactly Schwarzschild — the delta is zero.**
0037's perihelion advance exceeded 6πM/p by 1.053 (M/p = 0.011) and
1.021 (M/p = 0.0044) and flagged the excess as "the second-order
term"; integrating the exact Schwarzschild orbit equation on the same
orbit (e = 0.5, p = 0.45) gives **1.0532** and **1.0205**, excess
coefficients 4.84/4.67 against the measured ~4.8. The excess *is*
GR's own second-order term — as it must be, since the Kerr–Schild
point channel is Schwarzschild, so β = γ = 1 by construction.
**Therefore the screening law is not a physical varying G, and the
naive reading is already dead**: G_eff = G(1−U) with U = GM/(rc²)
would have Earth's eccentricity modulate U_sun by 3.30e−10 annually,
breathing the lunar orbit by **127 mm** against LLR's ~1 mm —
excluded **127×**; an O(1) shift in PPN β is excluded **12500×**
(|β−1| < 8e−5). Two internal facts already pointed here and were not
joined up: 0020's own note that a **constant ambient is flat**, and
0012's exact **deficit additivity** (Deser–Jackiw–'t Hooft) — a flat
background cannot change a Gauss–Bonnet deficit. So δ = πw/√(det A₀)
is **bookkeeping in the w-parameterization**, not new gravity; this
**corrects 0058 §3.1**, which had listed it as the best
modified-gravity prediction. **The falsifiable surface is the
two-body rule**: 0037's O(M₁M₂) field-equation violation (48.7/48.3/
48.2 over a 4× mass range, 1.03% spread) is the only unfixed
dynamical freedom, and the theory makes no two-body prediction yet.
It is binary — reproduce Einstein–Infeld–Hoffmann and the theory
equals GR at 1PN; miss and |β−1| ~ O(1), excluded by ~10⁴ — with **no
free parameter in the classical sector to absorb the difference**.
Battery: `exact_advance`, `potential`. Honest limits: §1 is a
test-particle comparison and says nothing about two bodies; §2's LLR
figure is order-of-magnitude (δa/a ~ ΔG/G, not a fitted ephemeris),
though the margin will not reverse; §2 refutes the naive reading and
reaches the subtler one by elimination. Open: **the two-body rule vs
EIH** (now the single highest-value computation, and the only one
that can falsify the program); the closed form of the ~48
coefficient; fixing t or N in the quantum sector (a derived t
predicts a graviton mass, bounded by LVK).

## The second-order test (0060)

`exploration/0060`, `output/0054`. **Corrects 0059 §3.** 0046
identified the classical functional as S = (1/2κ)∫ε_IJKL e∧e∧F and
0050 verified it (torsion rank 24/24, ω algebraic in e, 2 dof,
Palatini route matching the metric route's Ricci to 1e−6) — **that is
the Palatini action of general relativity**, so the field equations
are Einstein's and EIH follows necessarily. **No classical
measurement in this program can falsify GR, because classically the
program is GR.** The question with a real failure mode is instead
whether the web's *construction* (channels + bond) can generate
Einstein's solutions. **The diagnostic, validated**: truncating
harmonic-coordinate Schwarzschild at successive orders and measuring
the log-log slope of the off-source residual against mass gives
**1.985** (first order, h² missing), **2.885** (second order, h²
correct), **0.996** (exact — a finite-difference floor scaling as M¹,
so the noise has a different slope from any signal). The instrument
reads out whether h² is right. **The measurement**: scanning 0046's
frame-square cross-term coefficient c over [−2,+4] gives a minimum at
c = 1.5 (2.51e−3 vs superposition's 5.16e−3) — but the mass slope is
**2.015 / 2.022 / 2.042** at c = 0 / 1.0 / 1.5, signal 433× above the
floor. **The optimum reduces the coefficient 2× and leaves the order
untouched**: no scalar multiple of the frame-dictated cross term is
the second-order solution, and the pointwise-ansatz path is closed.
This **confirms** 0046's conjecture ("no pointwise ansatz supplies it
— that is the field equation's own job") and closes its open item
with the answer that a genuine iteration is required and has not been
run. Recorded structural correspondence, not yet measured: **the bond
is the Weyl strut** — GR needs a strut to hold two static masses
apart, and the bond's virial law ∫S = −F·d is exactly a strut of
tension F = Gm₁m₂/d² over length d. **The diagnostic is gauge-dependent** (adversarial review,
incorporated): "truncate at first order" is not coordinate-independent
— Kerr–Schild Schwarzschild *terminates* at first order while harmonic
does not, and an M-dependent diffeo with ξ = O(M) shifts a truncated
metric at O(M²), the very order measured, so the leading residual
coefficient is not an invariant. What survives: **R_μν ≠ 0 at
O(w₁w₂) is gauge-invariant** (confirmed analytically — on the axis the
bilinear Ricci is exactly 4w₁w₂d²/(r₁³r₂³) ℓ_μℓ_ν, null dust with
positive energy density); the measurement is about the web's own
construction in its own coordinates; and the test certifies h² only
modulo ker R⁽¹⁾. The floor is separately verified to be
finite-difference *truncation* (slope 1, ratio 2.00 per halving down
to 8.7e−8 at M = 6.25e−4) and not roundoff (392× above ε/h²), so it
cannot flatten the tail and fake a slope change. **The strut is
independently corroborated**: the same review, reasoning from GR alone,
concluded a static pair's second-order source carries a net force
Gm₁m₂/d² per body, so the repair either accelerates the bodies or
reintroduces the Bach–Weyl/Israel–Khan strut. Battery: `log_slope`,
`worst_residual`, `harmonic_schwarzschild`, `two_body_residual`.
Honest limits: §2 scans one scalar on a fixed tensor structure, so it
kills *that* structure at any weight, not every possible ansatz; the
*order* statement is relative to the coordinate presentation;
§1's 2.885 falls short of 3 because the FD floor contributes at the
smallest masses (only 7× separation there); R_μν ≠ 0 is
gauge-invariant so the violation is real, but its magnitude is
coordinate-dependent; the strut identification is structural, not
numerical. Open: **does the bond's contribution move the slope from 2
to 3** (the sharpest well-posed classical test, now with a validated
criterion and a real failure mode); verify the strut tension
numerically; a genuine e-equation iteration; and the quantum sector's
free parameters, which remain the only place an *observational*
falsifier could live.

## Curvature from the quantized 3+1 model (0061)

`exploration/0061`, `output/0055`. The 3+1 analogue of 0054's quantum
deficit — two positives and one sharp negative. **The split is exact
in finite arithmetic**: building the Riemann operator on bivectors over
Z_N (symmetric 6×6 plus first Bianchi) and decomposing by
Kulkarni–Nomizu (needs N coprime to 6) gives **Riemann 20, Ricci 10,
Weyl 10 in n = 4** and **6, 6, 0 in n = 3**, matching the continuum
n²(n²−1)/12, n(n+1)/2, n(n+1)(n+2)(n−3)/12 exactly at N = 5 and 7.
**Weyl exists in 3+1 and vanishes identically in 2+1 — the graviton's
existence, and its absence one dimension down, as finite-field
arithmetic with no continuum limit taken.** **The vacuum Einstein
equation is arithmetic too**: with the Hodge star on bivectors
(Euclidean, ⋆² = 1), **[R, ⋆] = 0 ⟺ traceless Ricci = 0**, verified
3000/3000 at N = 5, with pure-Weyl curvatures commuting 300/300 — in
block form R = [[W⁺+s/12, r̊],[r̊ᵀ, W⁻+s/12]] and Einstein is exactly
the vanishing off-diagonal block, so "this curvature is Einstein" is a
finite decidable predicate on Z_N data. **But the measure does not
select it** — the honest negative, killing the hypothesis the arc had
drifted toward since 0055. Lifting the per-plaquette price (kernel
codimension 0/2/4) to an operator by summing its six plaquette
columns: price changed in **220/300** when Ricci varied at fixed Weyl
and **209/300** when Weyl varied at fixed Ricci, so it factors through
neither; and the cheapest-tier fractions are **0.0087 (pure Weyl) /
0.0002 (generic) / 0.0605 (pure Ricci)** — both special sectors beat
generic (44× and 300×) but **pure Ricci beats pure Weyl, the opposite
of vacuum selection**. The simplicity price is not the Einstein
equation; what imposes vacuum is the action's variation, not the
measure's weight. **Ambrose–Singer says why**: a smooth metric with
finite holonomy is flat, so a literal Z_N-holonomy lattice carries
piecewise-flat geometry with conical defects — in 2+1 that is the
whole theory (Deser–Jackiw–'t Hooft, and 0054's deficit is the abelian
sector doing exactly its job), and in 3+1 it gives **string defects but
not their radiation field**. **Three corrections recorded**: (a)
strings DO radiate — 0050 measured **Γ = 45.8** for an oscillating
Kibble–Turok loop against GR's 40–100 (0049 built the loop; citation
fixed by 0062), so the finite sector holds the
*defect*, not the *radiation field* (a straight static string is flat
outside itself and radiates nothing; an oscillating one radiates
strongly); (b) **quantum does not mean finite** — quantization
discretizes spectra, not the group (lattice QCD keeps SU(3), LQG keeps
SU(2) with discrete representation labels), so Z_N was a *tractability*
choice and is exactly what made 0053–0057 enumerable; (c)
**"nonabelian" is the wrong word for the fix** — a finite nonabelian
group is still forced flat, and Lorentzian pp-waves have *abelian*
holonomy while being Ricci-flat and curved, so the operative property
is **continuity** (the classical lattice already uses SO(3,1); only the
quantum sector shrank). **What the price actually is**: the weight
comes from integrating the frame out of ε·B·F, and the a-sum is a
*character sum* returning N⁴ when ε_IJKL b^J F^KL vanishes and exactly
zero otherwise, so **K(F) = N⁴ × #{b : the curvature annihilates b}** —
0056's kernel count, now derived. A tempting misreading was checked and
rejected: K is *not* the count of frame pairs pairing to zero (2673 vs
K = 729 at N = 3 simple); the surplus phases cancel. So the tiers count
**how many independent planes the curvature rotates in** — none, one,
or two. It cannot be Einstein for two reasons: the price interrogates a
*single bivector*'s rank while Einstein interrogates the *operator*'s
commutator with ⋆; and **a measure is not an equation of motion** —
integrating out sums over every frame, varying selects stationary
points. The Weyl sector exists in the
arithmetic and a Z_N gauge sector cannot carry it — **one obstruction
underlying four standing opens** (0054/1, 0055/3, 0056/2, 0057/1). The
2+1 quantum success was not a warm-up for 3+1; it was the abelian
ceiling, reached. Battery: `Curv`, `hodge_matrix`, `operator_price`,
`rank_modp`. Honest limits: §1–3 use formal Riemann tensors over Z_N
with the symmetries imposed **by hand**, so the tetrad and
torsion-freedom are assumed rather than produced; Euclidean signature
throughout (the real 5+5 SD/ASD split is Riemannian — Lorentzian Weyl
is 5 *complex* NP scalars); N = 5, 7 only; the six-columns↔six-plaquettes
lift is a modelling choice ignoring 0056 §3's shared-frame correlation;
the tail statistic is on 6000 samples/sector with means within 1.5%;
and Ambrose–Singer is about smooth metrics, so §4 constrains what the
continuum limit can be rather than being a lattice theorem. Open: **what the price is
tensorially** — now the sharpest conceptual open in the quantum arc,
since §3's negative is a question rather than a dead end: the tariff
sorts by *rank* (0/2/4), both it and Einstein are built on ⋆
(⟨⋆F, F⟩ vs [R, ⋆] = 0) and may be shadows of one structure, **the
ratio is exactly 2 at every N** (resolved by 0062: price =
rank(F)·log N, the parity theorem for alternating forms), and
there may be a *different* observable (correlation function, saddle
point) that encodes the field equation even though the pointwise weight
does not; **lift the quantum sector to a continuous twist group**
(continuity, not non-commutativity — resolving all four standing opens,
target a nonzero Weyl block and a mode count against 2); Lorentzian
⋆² = −1.

## The quantization audit (0062)

`exploration/0062`, `output/0056` (14 s). Model-switch audit of the
quantized-curvature arc (0061 and revision, spot-rechecks of 0057;
0059/0060 were adversarially audited in-session when written).
**Everything substantive held; one verification was hollow and is now
exact; one wording and one citation were wrong; and the audit produced
a theorem.** **Projectors exact**: on all 20 basis elements (N = 5, 7)
the Weyl output is symmetric, Bianchi-satisfying, Ricci-annihilated,
idempotent; image rank 10 = kernel of the rank-10 Ricci map — 0061's
spot checks become identities. **The Einstein criterion proven**:
0061 §2's "3000/3000 agree" contained **zero positive cases** (a
random curvature is Einstein with probability ~N⁻⁹), so it tested only
the generic direction — a true statement verified by a procedure that
could not have caught its falsity. Now exact: the maps M ↦ [M,⋆] and
M ↦ traceless Ricci have **identical kernels** (rank 9 = 9 = stacked
9, N = 5 and 7). Sharpened: [R,⋆] = 0 is **Einstein-with-Λ**, not
vacuum — witness Weyl + 2·Id commutes while Ricci = (s/4)δ ≠ 0;
vacuum is [R,⋆] = 0 ∧ s = 0 ⟺ Ricci = 0 (rank 10 = 10 = stacked 10).
**The price is the rank — a theorem**: the kernel map b ↦ ε b F *is*
the alternating matrix ⋆F acting on frame vectors (verified against
the shipped `m_of`), so |ker| = N^(4−rank) and **price(F) =
rank(F)·log N**; alternating forms have **even rank in every
characteristic**, so the tiers 0/2/4 are the even ranks of a 4×4
alternating form and **the exactly-2 ratio is the parity theorem** —
0061's open resolved, verified exhaustively at N = 3, 5, 7
(729/15 625/117 649 configurations, tier ⟺ Pf exact in every one).
This unifies 0055's Pfaffian, 0056's kernel codimension, and 0057's
self-dual imbalance as shadows of one invariant: the rank of the
curvature bivector. **Seed-stable**: the sector ordering pure Ricci >
pure Weyl ≫ generic reproduces at seeds 7/99/12345 — 0061 §3's
negative stands. **0057 rechecked**: Pf a function of the SD/ASD
imbalance alone (all N⁶, N = 3 and 5); dispersion arithmetic exact.
**Corrections applied**: Γ = 45.8 was measured in **0050**
(`loop_power`), not 0049 (which built the loop) — fixed in 0061, the
0055 module, and this file; "vacuum Einstein equation" → Einstein.
Battery: `alt_matrix`, `make_rand`. Honest limits: 0061's own limits
(hand-imposed symmetries, Euclidean signature, the six-columns lift)
are inherited, not discharged; the rank theorem is proven for prime N;
seed stability is three seeds, adequate for a 5–100× ordering only.
Open: **is the whole measure symplectic** — rank stratification of ⋆F
as the answer to "what the tier structure is tensorially" (candidate:
nothing tensorial — the symplectic stratification is finer than any
curvature decomposition); composite N via Smith form of ⋆F over
Z_{2^k}; standing: continuous-twist lift, Lorentzian star, the
correlation gap, the bond's h².

## The continuous twist: the graviton counted (0063)

`exploration/0063`, `output/0057` (2 s). The lift 0061/0062 demanded —
finite Z_N → continuous twist — taken at the linearized level, where
everything is exact rational linear algebra, closing the four standing
polarization opens (0054/1, 0055/3, 0056/2, 0057/1) at that level.
**The mode count**: central differences make every derivative the
symbol s_μ = sin k_μ, so the linearized vacuum equations are a 10×10
matrix over Q; at exact rational points, ker = **4** off the shell
(all pure gauge), **6** on the shell (η·s² = 0, e.g. (5,3,4,0),
(13,3,4,12)) — **physical = 2**; in n = 3, ker = 3 = gauge —
**physical = 0**. Two propagating modes in 3+1, zero in 2+1, the
dimensional trade at the propagating level with no sampling and no
limits. **What they carry**: gauge modes have **Riemann ≡ 0
identically** (they carry no geometry); the TT modes h₊, hₓ have
E = 0, **Ricci = 0 with Riemann ≠ 0 (72 components) — pure Weyl** —
and their curvature operator **commutes with the Lorentzian star**:
0061's target ("a curvature operator whose Weyl block is nonzero")
delivered by the graviton itself. In n = 3 every on-shell solution
has Riemann ≡ 0. **The Lorentzian criterion proven** (0061 open 3
closed): ⋆² = −1, and over Q the kernels of [·,⋆] and traceless
Ricci are identical (9 = 9 = stacked 9; vacuum pair 10 = 10 = 10).
**Lattice grounding**: the literal central-difference stencil on a
discrete TT wave at a real lattice momentum gives max|E| = **0.0
(machine zero)** on the lattice shell sin²ω = Σ sin²kᵢ and 1.1e−1 off
it; the shell's small-k limit is ω = |k| — **massless by
construction**, no t → t_c tuning (doublers noted). **The quantum
tier**: quantization is exact (Gaussian) — two oscillators per
momentum, equal-time zero-point variance = 1/(2ω√(1+ω²/4)) → 1/(2ω)
matched to 6 digits — the graviton's zero-point jitter, 0054's
|⟨W⟩| < 1 continued to the continuum; and the compact-U(1)
heat-kernel plaquette gives ⟨W⟩ = e^(−1/2β) exactly — tension
**continuous in the coupling** where Z_N's was the arithmetic f(N),
with **integer dual labels** in the character expansion: discreteness
as output, not ingredient. Battery: `riem_sym`, `einstein_of`,
`Ematrix`, `null_space`, `star6`, `riem_to_op`. Honest limits:
linearized and free — the count "2" is the free count, the
nonperturbative spin-2 question (Hamber, 0058) stays open; the U(1)
heat-kernel weight is chosen (Villain), not derived — **the
continuous analogue of the ledger weight gcd(F,N)/N is unknown**
(gcd has no smooth limit; its Fourier dual is the object to take a
limit of), now the sharpest structural open of the continuous arc;
doublers noted; zero-point per-mode, silent on backreaction. Open:
the continuous ledger weight (**answered at the abelian tier by
0064**: it is τ, the Dirichlet square of BF); the cubic vertex from
ε e∧e∧F (whose static face is 0060's bond); the nonperturbative count
(Monte Carlo or an exactly solvable sector); standing: t and N
derivations, the correlation gap, the bond's h², composite N, the
symplectic reframing.

## The divisor ensemble (0064)

`exploration/0064`, `output/0058` (0.24 s). The ledger weight
gcd(F,N)/N — a black box since 0053 — opened by Cesàro's identity
**gcd(F,N) = Σ_{d|N} φ(d)[d|F]** (verified exactly, all N ≤ 60): the
per-plaquette weight is a φ-weighted mixture of **flatness constraints
at every level d | N**, so the partition function is a sum over
**divisor fields** — **the quantization level is a local dynamical
variable**, distributed by Euler φ. On a closed 2-plaquette universe
the budget couples levels through their **lcm**
(Z = Σ φ(d₁)φ(d₂)N/lcm(d₁,d₂), exact at N = 6, 12) — 0053 §4's
correlation as a formula. **Closed forms for the measured arc**:
0055's jitter base is exactly **f(N) = φ(N)/P(N)** (Pillai), matching
every measured value (1/3, 2/5, 1/4, 4/9, 6/13), and it *is* the
probability that the local level is maximal — classical rigidity is
the d = N sector, **quantum jitter is the φ-probability of
sub-maximal local levels**; tension = log(P/φ). Prime N → two-level
ensemble (BF + free, weights → ½, ½; continuum tension **log 2**);
dyadic N = 2^k → **uniform distribution over the dyadic tower**
(1/(k+2) per level, exact) — 0053's 2-adic grading resolved as the
divisor lattice. **The continuum ledger, derived** (0063 open 1
answered at the abelian tier): the Fourier dual is
Ŵ(n) = Σ_{e|gcd(n,N)} e·φ(N/e), and at divisibility-saturated
N = lcm(1..K)², **Ŵ(n)/Ŵ(1) = τ(n) exactly** for n ≤ K (K = 6, 10,
14; N up to 10¹¹) — the number-of-divisors function, with
**τ = 1∗1**: probability = amplitude² becomes **Dirichlet
convolution** in the charge basis — the continuum ledger is the
Dirichlet square of the topological theory, arithmetic and
heavy-tailed, not the heat kernel 0063 chose. The divergent zero mode
Ŵ(0)/Ŵ(1) = P/φ (68 → 4328) is exactly the mode the closed-universe
budget removes — the measure's one divergence and the budget's one
deletion are the same object. **First observable**: the closed
2-plaquette ⟨W⟩ falls slowly (0.350 → 0.239 over N = 144 → 7×10⁵);
Στ² diverges logarithmically, so the strict limit needs the budget's
zero-mode care — a trend, not a limit. Battery: `phi`, `divisors`,
`pillai`, `dual_weight`, `lcm_range`. Honest limits: abelian tier
only; τ-exactness is along the saturated sequence (primes give the
two-level structure instead); §4 unresolved; novelty caveat per
0058's method (Cesàro is 19th-century; Στ(n)qⁿ is Eisenstein-adjacent
— the arithmetic bridge may be knocking). Open: the **nonabelian
Dirichlet square** (convolution square of the trivial weight on the
representation ring — bridge to EPRL machinery); redo quantum Newton
and the mode count under the derived τ weight (controlled A/B vs heat
kernel); the Eisenstein/E₂ connection (0048's arithmetic bridge);
queued next: the correlation/trust tier.

## The correlation tier (0065)

`exploration/0065`, `output/0059` (0.02 s). Closes the gap 0058 called
the program's highest-value structural open — "correlation sources
curvature" was claimed with participation delivered — at the
classical/Gaussian tier, by derivation. **The metric is derived, not
posited**: for an explicit inference network (nodes, line-of-sight
channels of precision λ, isotropic prior), the numerically computed
Hessian of the expected log-likelihood equals **A₀ + Σ λ·uuᵀ** to
3.7e−11 — the web's metric ansatz (0019/0020) is the Fisher metric of
an estimation model, with **w = λ = the precision of the pairwise
knowledge**; K = πs and the screening law now rest on a derived
object. **Precision is the trust axis**: λ = n/σ² is the effective
sample count — 0008's trust, the axis Kalman folds into variance and
a distribution-tracker must carry separately; here the metric carries
it, and it is what curves. And **λ = e^{2I} − 1** exactly (verified
against direct entropies): participation = precision = trust = a
monotone bijection of mutual information. **The deficit law**:
composing with 0019's exact cone (re-verified geometrically),
**δ = 2π(1 − e^{−I})** — weak limit δ ≈ 2πI (curvature *linear* in
MI — the first-law shape; shape-match only, cited not claimed), the
πw − ¾πw² expansion recovering 0019's measured correction, and
saturation I → ∞ ⇒ δ → 2π giving **m = (1 − e^{−I})/4G**: the
extremal defect is complete information and the mass cap m < 1/4G is
the statement that mutual information is never infinite. The
complement reads best: 2π − δ = 2π e^{−I} — the surviving angle is
the exponential of the unknown. The screening law is an information
statement verbatim: πw/√det A₀ = πw e^{−J}, J = ½ln det A₀ = the
ambient's **total information** (bookkeeping per 0059, but now
legible). **The bond tier is the redundancy tier**: precisions add
(Fisher additivity = 0041's "charges add," derived); the information
redundancy I₁+I₂−I_joint ≈ w₁w₂/2 sits exactly at the bond's O(w₁w₂)
tier, and the geometric interaction of collinear deficits is
**−3π × redundancy** at leading order (−9.31/−9.20/−9.12 → −3π).
Battery: `fisher_numeric`, `fisher_analytic`, `expected_nll`. Honest
limits: Gaussian/classical throughout — the quantum tier
(Bures/entanglement, whether δ = 2π(1−e^{−I}) survives) is now the
sharpest open on this front; measurement model chosen to match the
radial channel structure; inherits 0019/0020's 2+1 static scope; §4
is leading-order with slow convergence, tied to the 3+1 bond by tier
not construction. Open: the quantum tier (Bures for Fisher,
entanglement for MI) — **taken by 0066**: the law survives at weak
coupling and for persistent channels (ratio → 1.0000), and splits for
single strong carriers at the dimension cap 2π(1−1/d); build the
bond's h² *from* redundancy (0060 open 1 with a new handle); an
information reading of the Z_N deficit 2πn/N via the divisor ensemble;
standing: t and N, the τ A/B, the nonabelian Dirichlet square.

## The quantum tier (0066)

`exploration/0066`, `output/0060` (0.26 s). 0065's open 1 taken: the
channel's carrier lifted to a qubit (|ψ_θ⟩ = e^{−iκθσ_y/2}|0⟩,
Gaussian prior), Fisher → Bures, and the question of which
information measure keeps δ = 2π(1 − e^{−I}) alive. **The metric
derivation survives quantization**: the Bures metric on configuration
space, computed from fidelity with no formula assumed, is
**(QFI/4)·uuᵀ per channel, additive** (8e−7, two channels, product
carrier) — and fidelity is |amplitude|², so the quantum metric tier
is built on the ledger's own rule; **w_Q = QFI**. **The weight is
attainable**: the σ_x readout has classical Fisher = QFI at every θ
(machine precision), and at weak coupling the record's MI matches the
classical law to 0.3% — the Gaussian tier is the weak limit. **The
bijection splits into a tower**: I_record ≤ χ ≤ ln d all *saturate*
(χ → ln 2 exactly, record → 0.307) while ½ln(1+QFI) grows without
bound (3.40 at κ = 30) — a single qubit's extractable correlation is
capped by its dimension, its distinguishability is not: **trust and
correlation, merged at the classical tier, come apart exactly where
quantum mechanics begins**. **The deficit law: two survivals and one
split** — (i) weak coupling: holds, all measures coinciding; (ii)
**persistent channels** (n uses, wrap-free): the record's MI
converges to ½ln(1+n·QFI), ratio 0.9973 → **1.0000** at n = 600, so
δ = 2π(1−e^{−I_record}) holds with no quantum correction — the web's
channels are persistent, so this is the physical regime; (iii) a
single strong carrier: geometry follows QFI (δ → 2π) while the
information law caps at **2π(1−1/d) — exactly π for a qubit**: one
maximally-informative qubit can close at most half the circle by
correlation accounting (measured: δ_QFI = 5.66 vs χ-law 3.1416 at
κ = 10). **Mass reading**: m = (1−e^{−I})/4G becomes a
*distinguishability* bound — approaching the extremal 1/4G needs
unboundedly many carriers or unbounded dimension; per carrier,
correlation buys at most (1−1/d)/4G. **Postulate caveat recorded**:
0005's "Petz uniqueness" overstates — Petz classifies a *family* of
monotone metrics on mixed states; uniqueness holds on pure states
(Fubini–Study) and by Cramér–Rao selection of Bures; pure-state
channels as used are safe (SUMMARY 0005 section annotated). Battery:
`_mi_single`, `_mi_record`, `_holevo`, Bures-Hessian pattern. Honest
limits: **one-sided model** (classical latent, quantum carrier) — the
fully relational entangled-ρ_AB version is the true RT-shape question
and remains open, the most important scope line; the record's plateau
is σ_x-specific (rigorous cap is χ); many-copy survival shown
wrap-free; 2+1 static scope inherited. Open: the two-sided tier — **taken
by 0067**: for relational records the weight is κ²·C² (the tangle),
separable pairs source no geometry, and the deficit tracks the tangle
rather than entanglement entropy; the π ceiling as physics in the
quantum lattice; qutrit check of 2π(1−1/d); standing: t and N, τ A/B,
bond h² from redundancy, nonabelian Dirichlet square.

## The entanglement tier (0067)

`exploration/0067`, `output/0061` (0.2 s). 0066's sharpest open
taken: both ends quantum. The relative coordinate is recorded
**relationally** — |ψ⟩ = √p|00⟩ + √(1−p)e^{iκθ}|11⟩, a phase between
the correlated branches — and **ρ_A = diag(p,1−p) is exactly
θ-independent**: neither end alone sees the coordinate, postulate P1
as a density matrix (contrast: |+⟩|0⟩ with local encoding carries
QFI = κ² at zero entanglement — 0066's one-sided mechanism, distinct).
**The weight is the tangle**: the Bures configuration metric is
(QFI/4)·uuᵀ with QFI = 4κ²p(1−p) (numeric Hessian, ~6e−7), and
Wootters' C = 2√(p(1−p)), so **w = κ²C² exactly** —
separable ⇒ C = 0 ⇒ **an unentangled pair sources no geometry**;
maximal entanglement recovers the full one-carrier weight; the
program's squares align again (probability = amplitude², bond =
charge², ledger = Dirichlet square, weight = concurrence²). **The
discriminator**: at weak coupling, δ/(πκ²) tracks **C² to 3–4
digits** (0.0396/0.0396 at p = 0.01; 0.5095/0.5100 at p = 0.15)
while entanglement entropy E and quantum MI 2E are far off (E/C² >
1.4 at small p) — **curvature couples to the tangle, not to
entanglement entropy**: the RT shape is not this program's pair-level
prediction, stated as a sharp falsifiable-in-model selection (RT's
own setting is a duality with boundary-QFT entropy — the contrast
says what this model selects, not that RT errs). **The
persistent-pair law**: the Bell-basis readout attains κ²C² at the
phase reference (2e−15); the n-pair record's MI converges to
½ln(1+nκ²C²) (ratio 0.955 → 0.986 at n = 600, monotone), so
**δ = 2π(1−e^{−I_record}) with per-pair capacity = the tangle**:
entanglement is the capacity, the record is the account, the deficit
follows the account. Across the tiers: trust = precision (0065) →
QFI with the dimension-capped split (0066) → per-pair precision =
tangle (0067). Battery: `fid`, `concurrence`, `_mi_record`. Honest
limits: one family (Schmidt-aligned; local-coherence records are a
separate mechanism, no decomposition theorem); two qubits; pure
states; 2+1 static scope inherited; one (p,κ) for the convergence.
Open: **weight monogamy and the
local+tangle decomposition — both taken by 0068** (one theorem: the
Bloch budget); mixed states (w ≤ κ²C²(ρ)?); standing: t and N, τ A/B,
bond h², nonabelian Dirichlet square.

## The weight decomposition (0068)

`exploration/0068`, `output/0062` (0.08 s). 0067's opens 1 and 2
close as **one theorem**. **The Bloch budget**: for a qubit carrier
with Bloch vector r and pointer n̂, exactly
**(r·n̂)² + (|r|²−(r·n̂)²) + C² = 1** — bias + local coherence +
tangle — verified to 1e−15 (one line: C² = 1−|r|² pure two-qubit,
plus Pythagoras). **The decomposition theorem**:
**w = κ²(1−(r·n̂)²) = κ²(tangle + local coherence)** — QFI from
fidelity matches to 2.8e−7, the algebra to 7e−16 — equivalently
w = κ²·Var(pointer): **the weight is the carrier's undecidedness**;
the decided part is inert (|0⟩|χ⟩ sources nothing). Covariance: the
tangle part is **encoding-independent**, the coherence part rotates
with n̂. 0066 (pure coherence) and 0067 (pure tangle) were the two
poles all along. **Geometry is blind to privacy**: same-w states with
opposite splits (all tangle vs all coherence) give identical Bures
metrics (1.1e−6, FD floor) — the deficit charges undecidedness
wherever it lives; who can read the record leaves no geometric
trace. **The ladder and mass monogamy**: for any pure global state
the tangle reads as node-vs-rest (4 det ρ_A), and CKW splits it:
**w/κ² = coherence² + C²_AB + C²_AC + τ₃** — verified on 200 random
3-qubit states, 0 violations (mixed Wootters via char-poly
eigenvalues with zero-root deflation, validated exactly on pure
states, W's 2/3, GHZ's 0); poles GHZ (w all three-tangle, pairwise
0) and W (all pairwise, τ₃ = 0, CKW saturated). Consequences:
**the ladder** — private, shared, and collective capacity each
charged equally; **mass monogamy** — a node's pairwise relational
weights are capped by its total weight ≤ κ², the per-node sourcing
bound, now inherited from CKW as a theorem; and a **P1 refinement**
— GHZ's weight has no pairwise carrier, so "all content is pairwise"
must be read as node-vs-rest bipartitions: collective entanglement
sources geometry no pair accounts for. Battery: `bloch_and_C`,
`conc_mixed` (`_eig4` with deflation), `_ptrace_*`. Honest limits:
pure global states (mixed conjecture untested); qubit carriers and
qubit-CKW; 2+1 static scope inherited. Open: **the mixed tier — is
decoherence literally the transfer of weight from capacity to bias,
collapse as geometric discharge?** (sharpest next); higher tangles
(does the ladder continue?); P1 formalization; standing: t and N,
τ A/B, bond h², nonabelian Dirichlet square.

## The bar (0069)

Orientation pass, no module (`exploration/0069`). The requirement
list for "a quantum gravity theory" with brutal status per item:
(A) interacting quantum geometry — partial at the toy tier, **the
wall is the interacting continuous 3+1 measure**, unattempted, with
one unique asset (the derived Dirichlet-square measure); (B) GR
classical limit — done modulo the bond's h²; (C) semiclassical
benchmarks (Hawking/Unruh/area laws) — **untouched, the largest
silent gap**, though the information tier is area-law-shaped;
(D) UV story — N is the regulator and (per 0049) the coupling's only
physical datum: deriving N = deriving the hierarchy; (E) matter —
dormant; (F) the arena — the manifold–spacetime identification and
3+1 Lorentzian remain the deepest unpriced assumptions; (G) the
measurement problem jointly — this program's unique obligation, now
concrete as collapse-as-geometric-discharge (0068). Path order:
wall → matter → semiclassics → derive N → arena → falsifiables. A
skeptic converts at (A)+(C)+one derived knob. **Falsifiability,
vacuum energy first**: the mechanism already exists — the Λ mode is
the zero mode, deleted by the closed-universe budget (0029 = 0057's
removed k = 0 = 0064's sole divergence), giving unimodular-flavor
phenomenology (uniform vacuum energy does not gravitate; the 10¹²⁰
problem does not arise in standard form); the continuation: mod-N
budget ⇒ **quantized Λ residual** in units set by N — steps: budget
off the torus (compactness currently does real work), zero mode in
the τ theory, residual spectrum, confront Λ_obs·V with the quantum
and cross-check N against the hierarchy. Other lines: graviton mass
possibly dissolved (0063 massless without tuning), tangle-vs-entropy
sharp but in-model, monogamy/π-cap Planck-scale, EP deviations dead
(0059). **Program comparison table recorded** (string/KLT = our
double copy; LQG = nearest cousin, our arc an exactly solvable
abelian spin foam with weak simplicity as the priced ledger;
CDT/Hamber = our reproduced phase structure; Jacobson/RT = same
territory, opposite measure per 0067's discriminator). Distinctive:
fewest knobs (two, one dissolving; G and c units), derived measure,
machine-verified, the measurement-gravity unification obligation.
Missing: the wall, semiclassics, matter, the arena — and scrutiny
(one builder; 0062 found real errors, more exist unfound).

## The three paths (0070)

Orientation doc, no module (`exploration/0070`). Straight-line plans
to 0069's bar. **Path A (the wall)**: A0 the exact RG probe of the
derived measure (executed, 0071) → A1 the continuum frame kernel
(ℝ⁴ Gauss integral: expected delta-on-simple + 1/Pf² tail — BC's
delta *plus a derived correction*) → A2 one-vertex SU(2) with the
derived weight (character expansion, exact partial sums) → A3 the
graviton-propagator test vs 0063 (where BC bled, EPRL survived).
Then: nonabelian blocking; SL(2,C); sources; marry substrate to
0063's modes. Alternatives: Hamiltonian/transfer-matrix route;
adopt-EPRL-and-test-our-observables; strong-coupling organization.
**Path C (semiclassics)**: C1 graviton half-space entanglement
(Gaussian, exact — area law + coefficient) → C2 thermality
(Bisognano–Wichmann on the lattice) → C3 entropy = lost pairwise
capacity (deficit law + monogamy) → C4 the 1/4 confrontation. Then:
the saturated-channel-is-a-horizon conjecture (0065's I → ∞ =
extremal defect). Alternatives: topological entanglement entropy of
the 4D deconfined phase; Unruh deferred to matter. **Path N/Λ**: Λ1
budget with boundary (open-lattice link integration: Σ F = boundary
holonomy, exact) → Λ2 zero mode in the τ theory → Λ3 residual
spectrum 2πn/N → Λ4 confront Λ_obs and cross-check N against the
hierarchy. Alternatives: P4/Tsirelson (dormant), t-renormalization
via A3 — and 0071 already delivers the first constraint: **N ≥ 3**.
The pick: A0 first (executed); next stones by cost: A1 and Λ1, then
C1, then A2–A3.

## The RG probe (0071)

`exploration/0071`, `output/0063` (0.04 s). Path A's first stone:
the derived measure has no coupling knob, so its phase is a fact —
computed exactly in the abelian sector. **The ensemble is
RG-closed**: 2D blocking = 4-fold convolution = dual weight → 4th
power (exact, integers, N = 12); gcd-functions close under powers,
so the divisor ensemble is an RG-invariant family with the pure
levels as fixed points — the flow is exactly followable on the
divisor simplex. **2D: the jitter wins totally** — free-sector share
0.300 → 0.914 → 1.000 in two blockings: 0055's area law as an RG
flow; D = 2 gravity is empty anyway. **3D: confined** — Wegner
duality maps the ledger exactly to spin models at couplings ½ln 3 =
0.549 (Ising, K_c ≈ 0.222) and ln(5/2) = 0.916 (Potts, K_c ≈ 0.551)
— deep in the ordered phase, Wilson area law at all scales, **no
long-range rigid geometry in the 3D vacuum** (cited K_c's, flagged).
**4D: rigidity begins at N = 3** — the two-valued family is closed
under the exact self-duality r ↦ (r−1+N)/(r−1), r* = 1+√N; the
ledger sits at r = N: **confined for N = 2, deconfined for every
N ≥ 3** ((N−1)² > N). Under the single-transition assumption, **the
derived measure first supports long-range rigid geometry in four
dimensions, and only for N ≥ 3** — the program's first internal
evidence selecting D = 4, and the first derived constraint on its
knob (N = 2's failure joins its standing degeneracies). **Where it
bleeds**: D ≤ 3 bled (jitter wins); D = 4 N ≥ 3 survives its first
test, but deconfined Z_N is topological order — rigidity without
gravitons (0061 §4's ceiling stands); the substrate is rigid, the
modes need the continuous group, and the marriage is 0070's A1–A3.
Battery: `ledger`, `conv`, `level_shares`, the duality involution.
Honest limits: 3D K_c cited; 4D single-transition assumed; N ≥ 5
intermediate-phase caveat open; abelian, Euclidean, hypercubic;
Wilson magnitude as the criterion. Open: the N ≥ 5 window question;
topological entanglement entropy of the 4D phase; A1; Λ1; C1;
nonabelian blocking.

## The continuum kernel (0072)

`exploration/0072`, `output/0064` (3 s). Path A's second stone (A1):
the Z_N frame Gauss sum redone with continuous Gaussian-regulated
frames (a, b ∈ ℝ⁴, scale L) collapses to a rational closed form in
the two simplicity invariants: **K_L(F) = (2π)⁴/(ε² + ε|F|² +
Pf(F)²), ε = 1/L⁴**. Mechanism: canonical form of ⋆F splits the 8D
integral into four atomic integrals ∬e^{iλxy−(x²+y²)/2L²} =
2π/√(ε+λ²) (quadrature, 7 digits), and the canonical pair satisfies
x⁴ + |F|²x² + Pf² exactly (machine, 50 curvatures); an 8D seeded MC
bridge confirms a generic F (0.03%). **The Z_N structure returns with
a dictionary**: simple curvature at |F| = 1 costs exactly 4 ln L, the
non-simple/simple ratio → 2 (1.85/1.92/1.95 at L = 10/100/1000) —
the parity echo — so 0/2logN/4logN corresponds under **N ~ L²**: the
level is the square of the frame scale. **What Barrett–Crane never
had**: Pf = (|F⁺|²−|F⁻|²)/2 exactly, so the kernel is a **Cauchy
suppression of the self-dual imbalance**, concentrating on the
balanced cone as ε → 0 (off/on 4.8e−2 → 4.9e−6 at L = 3 → 30) — BC's
delta as the singular limit, but with a **derived on-cone measure**
(∝ 1/(ε+|F|²), log-uniform), a **derived off-cone tail** (∝ 1/Pf²,
nothing forbidden), and a **canonical regulator** (ε = 1/L⁴). BC bled
at the bare delta; EPRL chose a spread; here the spread is derived —
whether its profile passes the graviton-propagator test is exactly
A2–A3, and this kernel is A2's per-plaquette weight. **The filter
correspondence** (recorded): the sibling stat-tracker's new math
(code-length optimality/Theorem A′; the GPB1→IMM ridge repair with a
96.3% causal ceiling; the s_P = 0 boundary ill-posed because Fisher
vanishes ∝ s²; fractional order ν) resonates three ways
(grid-of-worlds = divisor ensemble; everything priced in nats;
categorical-made-continuous = 0063's lesson) and two give-backs are
logged: **τ = s² reparameterization makes the boundary Fisher finite
(= 1/4)** — the ledger's square applied to their chart, one line,
checkable; and coherent (amplitude-mixing) IMM, speculative. Also
logged: formal-languages carries an unmerged arithmetic branch
(0057–0066, ~14.6k lines: "no finite ħ," "paradox tax," "epistricted
wall," "braided holonomy") — queued for a pass. Battery:
`star_matrix`, `pf`, `K_closed`, `_char_poly`. Honest limits:
Euclidean, Gaussian regulator (profile not proven
regulator-independent; structure should be); per-plaquette
independent frames (0056 §3 correlation not folded in); MC bridge
seeded and labeled; filter give-backs are suggestions, nothing run
in their harness. Open: A2 (one-vertex nonabelian with this kernel);
A3 (the propagator test where BC bled); regulator-independence; the
arithmetic-branch pass.

## The nonabelian plaquette (0073)

`exploration/0073`, `output/0065` (1.3 s). Path A's A2 (first half):
0072's kernel lifted to a class function on Spin(4) = SU(2)⁺×SU(2)⁻
(chord and angle lifts) and expanded in characters. **The center is
blind**: every half-integer coefficient vanishes identically — vector
frames see SO(4), no spinorial sector (matter needing spinors needs a
spinorial B; recorded for 0069's E). **Simple reps dominate,
heavy-tailed**: at ε = 0.01 the balanced diagonal carries the weight
(0.62/0.45/0.34/0.27 at j = 1..4) — Barrett–Crane's simple reps
emerging softly, with a tail far above any heat kernel (matched at
step one, predicted 0.14 vs actual 0.27 at j = 4) — the τ-lesson
nonabelian. **The sign problem arrives**: the weight is pointwise
positive but NOT character-positive — c(2,0) < 0 at every ε tested
(−0.008 even at ε = 1), c(1,0) crosses near ε ≈ 0.05 reaching −0.27
by ε = 0.003; both lifts diseased (which coefficient differs, the
negativity doesn't); grid-stable to 1e−17. Osterwalder–Seiler
positivity fails for the naive one-plaquette lift: **the disease
interacting QG measures die of, met on schedule at the wall** (the
sibling arithmetic branch's probes name "the sign problem" — a
cognate, hit independently). **The cure has the ledger's shape**: the
U(1) dual ledger was τ = 1∗1 — a Dirichlet square, coefficient-
positive automatically — so a nonabelian dual-square weight has
coefficients (amplitude)² ≥ 0 by construction; the naive kernel lift
kept the kernel and dropped the square, and its negativity says the
kernel alone was never the whole weight. **A2's disease independently
demands 0064 open 1 — the nonabelian Dirichlet square. The next stone
is forced, not chosen.** Also closed this turn, the filter loop: the
τ = s² boundary cure pushed to lucid-filter as
`research/oracle-gap/0010` on branch `claude/square-chart-boundary`
(verified there: I(s)/s² → 1.597, I(τ) → 0.399 flat, one-sided MLE
demo; their-harness tests flagged as theirs); scan noted the shipped
WalkingFilter's moving grids (adaptive frames) and the
"AI-generated, not peer-reviewed" banner convention worth adopting.
Battery: `dual_coeffs`, `chi`. Honest limits: the class-function lift
is a choice and OS-positivity is sufficient-not-necessary (another
route to a positive transfer matrix is not excluded, only not
exhibited); one plaquette, no intertwiners, Euclidean, ε finite (ε→0
is BC's limit, not the program's). Open: **the nonabelian Dirichlet
square** (build the dual-square weight; check invariant structure,
automatic positivity, simple-rep concentration); A3 only after the
square (testing a non-positive weight tests the wrong object);
intertwiners as positivity restorers at a true vertex; standing: Λ1,
C1, the arithmetic-branch pass (its sign-problem probe now directly
relevant).

## The nonabelian Dirichlet square (0074)

`exploration/0074`, `output/0066` (0.6 s). 0073's demand met — and
outbid. **The ledger is a Born square, exactly**: for every odd N
tested (3..61, all fluxes), **gcd(F,N) = |Σ_e ω^(e²F)|²/N** — the
Z_N ledger weight is the squared magnitude of a quadratic Gauss sum,
the Born rule applied to a single-frame amplitude (B = e² as the
abelian shadow of B = e∧e). The measure 0053 took as given was
|amplitude|² from the start. Even N fails at most fluxes — N = 2's
degeneracy family traced to the root. The positivity mechanism is
visible: the amplitude's dual expansion **counts frames**
(r(m) = #{e: e² = m} ≥ 0), so the weight's dual is the
autocorrelation of a nonnegative function — verified exactly
(dual(gcd) = r⋆r, N = 15, 21); τ = 1∗1 was the arithmetic face, the
Born structure its cause. **The positivity theorem (fusion form)**:
W = A² with a counting amplitude A = Σ n_j χ_j (n ≥ 0) has
c_j(W) = Σ n n′ N^j ≥ 0 — 200 random countings, min exactly 0 — and
the necessity is exhibited: the *virtual* amplitude χ₁ − χ₀ (an
Adams image, the natural nonabelian-divisor candidate) has
c₁(A²) = −1: Adams lifts carry signs, Born lifts don't — **the right
square is the Born square**. **The derived amplitude is diagonal**:
a∧b is simple and simple = balanced (1e−14), so
A(U⁺,U⁻) = Σ n_j χ_j(U⁺)χ_j(U⁻) with n_j the Gaussian frame
counting (deterministic quadrature, two bin scales); W = A² has
**every coefficient ≥ 0**, diagonal dominance (2.71 vs 1.00),
positive-small off-diagonal (nothing forbidden, signs healed), a
peaked diagonal profile following the radial counting, and a
pointwise balanced ridge of 240× — the kernel's concentration
preserved. **Wall status**: 0073 lifted the weight → sign problem;
0074 lifts the amplitude and squares on the group → positive by
fusion. The cure is the program's own rule at the right tier; the
healed object is **Barrett–Crane as an amplitude** with a derived
radial profile; **A3 is unblocked**. And the abelian tier is exactly
solvable — the program owns a closed-form **toy of the sign problem**
(the sibling arithmetic branch's cognate probe). Battery:
`born_coeffs`, `su2_admissible`, the quadratic-Gauss identity.
Honest limits: Born identity verified ≤ 61, not proven (classical
Gauss-sum territory — cite or derive next); n_j is bin-scale-
dependent (positivity and diagonality are not); one plaquette, no
intertwiners, Euclidean, integer bins; the A²-vs-K convention
(price-doubling bookkeeping) noted unresolved. Open: **A3 on the
healed weight** (the decisive stone); the Born identity's proof and
the even-N obstruction; the coherent-state unbinned amplitude
(EPRL-shaped); packaging the 2+1 abelian sign-problem toy;
arithmetic-branch cross-reference.

## The tension spectrum (0075)

`exploration/0075`, `output/0067` (0.9 s). A3's tensorial half — the
half Barrett–Crane's propagator failed — computed exactly on the
healed weight. **The instrument**: for W = Σ c_R χ_R, a plaquette
chain propagates mode R with t_R = c_R/(d_R c₀), tension −ln t_R
(Schur; the orientation-average identity verified numerically at
1e−3). **The spectrum**: finite, positive, rising — (1,0) 1.100 <
(1,1) 1.201 < (2,0) 1.611 < (2,1) 1.725 < (2,2) 1.879 < (3,3) 2.452
at s₀ = 0.75; ordering bin-scale-stable, numbers not. **The graviton
multiplet leads the simple tower**: within the balanced sector,
(1,1) < (2,2) < (3,3) strictly at both scales, and (1,1) is the
9-dim symmetric-traceless SO(4) tensor — the covariant graviton —
with the derived profile supplying the **high-spin damping BC
lacked**. Measured alongside: the unbalanced (1,0)
(connection/2-form) interleaves below (1,1) by 0.10–0.30 — the
measured job description for vertex-level simplicity, absent at one
plaquette; a pointer, not a hidden failure. **The failure modes**:
BC's bare balanced delta gives t(j,j) = 1 for every j (all balanced
modes massless-degenerate — the high-spin pathology as a flat
spectrum); the naive 0073 lift gives t(1,0) = −0.055 (undefined
tension — the sign disease as an unphysical spectrum). **Only the
Born square has a physical spectrum.** Scope: these are 1D-chain
tensions (the nonabelian rep-resolved f(N)), not 4D masses — 0071's
lesson; A3's momentum half needs the 4D complex, and its
sector-resolved input is now ordered: **the 4D question is which
multiplet deconfines first, with the graviton leading the simple
tower**. Battery: `spectrum`, `density`, the transfer identity.
Honest limits: one plaquette/chain, no intertwiners, Euclidean,
integer bins; s₀ moves numbers not ordering; the interleaving is a
bare-chain fact; BC here = the bare delta representative. Open: **4D
sector-resolved deconfinement** (A4 — nonabelian 0071 with an
ordered candidate list); the vertex (does the interleaving lift?);
the coherent-state amplitude; standing: Λ1, C1, arithmetic-branch
pass, sign-problem toy.

## The MK flow (0076)

`exploration/0076`, `output/0068` (4.7 s). A4: what survives
coarse-graining in 4D. **Calibration with the bias measured**: 2D
anchor exact (Z₃ ledger → free ✓ 0071); 4D abelian N = 3, 5 → BF ✓,
but N = 2 → BF where the exact answer is confined — **MK is
deconfinement-biased near transitions** (a "confined" verdict is
trustworthy, a marginal "deconfined" suspect). **Methods save
recorded**: the truncated-fusion implementation *flipped its 4D
verdict with jmax* (down at 8, up at 10, 12); the controlled form
does bond-moving exactly on a class-angle grid and truncates only
the decimated reconstruction (t⁴ decay ⇒ harmless cutoff); only the
controlled form is reported. **The 4D flow is near-stationary**:
t(1,0) 0.937, t(1,1) 0.878, t(2,2) 0.68, t(3,3) 0.46, t(6,6) 0.065
with t(1,1) drifting < 1% over steps 3–12, 0075's ordering preserved
at every step — a **nontrivial fixed structure** between the free
sink and the BF point, hierarchical, high spins suppressed. **The 3D
contrast is total**: ζ = 2 gives t(1,1) ~ 1e−71 by step 8 — three
dimensions confine absolutely, four go critical: **0071's dichotomy
survives the nonabelian lift** in its strongest form (same
recursion, same weight). Reading: within MK the healed weight in 4D
sits at/near a fixed structure whose light sectors are the low-spin
multiplets, the graviton multiplet among the survivors at t ≈ 0.88;
the bias means "marginal" could shade to "slowly confining"; robust
content = the dichotomy + the surviving hierarchy. **A3's momentum
half now has an address**: pose it at the fixed structure. Battery:
the grid MK step (`_step`), the Z_N calibration step. Honest limits:
MK uncontrolled and bias-measured; one bin scale; Euclidean; JBIG
24/NG 200; "critical" = near-stationary transfer eigenvalues, not
yet momentum-space masslessness. Open: A3's momentum half at the
fixed structure; map the basin (universality vs knife-edge); settle
the drift's sign with a finer instrument; standing: vertex, Λ1, C1,
arithmetic-branch pass, sign-problem toy.

## The continuum scaling (0077)

`exploration/0077`, `output/0069` (17 s). The stone after 0076: a
fixed structure with t < 1 is a finite correlation length unless
t → 1 as frames grow — so the decisive computable is the tension
scaling with bin scale s₀ ~ 1/L². **The graviton channel goes
gapless**: μ(1,1) = 0.437 → 0.124 → 0.033 → 0.011 across s₀ = 1.5 →
0.1875, power fit p = 1.82–1.90 — consistent with **μ ∝ s₀² ~ ε, the
regulator**; convergence 0.02% under grid refinement. **The fixed
structure is the heat kernel**: tension ratios are quadratic-Casimir
ratios to three digits at every scale — (2,2) 3.000, (1,0) 0.500,
(2,0) 1.500, (2,1) 2.000, (3,3) 6.000 — so **μ_R = τ·C₂(R), τ ∝ s₀²
→ 0**: the MK fixed structure of the healed weight is the heat
kernel on Spin(4) with vanishing diffusion time, by the CLT on
compact groups (only τ remembers the start; four different starting
profiles land on one structure — 0076's basin question answered for
this family). **0064's tension resolved**: the arithmetic heavy-
tailed ledger is the **UV completion**, the heat kernel the **IR
universality class** — 0063's chosen weight justified a posteriori.
**For A3**: the momentum half's mass question is answered — the
(1,1) channel is a **gapless carrier** in the continuum-frame limit,
with standard 1/k² at quadratic order; scope stated plainly: 0076's
drift is the **running of τ** (the 4D Yang–Mills shadow, logs MK
cannot resolve — gaplessness must outrun the running, the standard
4D story), and the gapless channel is the carrier the graviton
*needs*, not yet the graviton — whether the metric mode rides it is
the frame/vertex question. Battery: `run_fixed`. Honest limits: all
MK caveats inherit; smallest scale least converged; "heat kernel" is
six ratios at four scales, not a proof; the τ ∝ s₀² ∝ ε claim is a
two-step inference via the N ~ L² dictionary. Open: **the vertex —
the last wall-stone standing** (does the graviton ride the carrier;
does the (1,0) interleaving lift); the CLT fixed-point theorem; the
τ beta function vs the YM shadow; standing: Λ1, C1,
arithmetic-branch pass, sign-problem toy.

## The vertex (0078)

`exploration/0078`, `output/0070` (8 s). The wall's last standing
stone. At a site six plaquettes share the same four tetrad columns,
so the frame integral must be done jointly — a 16-dimensional
Gaussian that closes: **W_vertex = Π_k(ε′+s_k²)^(−1/2)**, s_k the
eigenvalues of the joint coupling S (blocks (⋆F_μν)/2). **Anchored**:
single-plaquette reduction recovers 0072's invariants (±λ/2 fourfold,
Σλ² = |F|², Πλ² = Pf²); Σs² = Σ|F|² to 1e−6; 16D MC bridge within
5%. **Cross-simplicity emerges**: six individually-simple plaquettes
cost ~14–15 nats from a common tetrad vs ~22–23 unrelated — **+7.4
nats mean for incompatibility** — while the one-plaquette product is
exactly blind (equal to 1e−6): the shared-frame integral generates
the off-diagonal Plebanski constraints the spin-foam program imposes
by hand. **The insertion ladder**: into a tetrad six-pack, geometric
+0.00 / foreign-simple +4.16 / non-simple +4.88, vs isolated 0 / 0 /
+1.87 — context amplifies the constraint tier ~3× and charges
compatibility itself: **cheap means geometric together** — the
suppression 0075 found missing at the bare chain, delivered. **The
honest non-flip**: Weyl vs Ricci at matched norm — Ricci still
cheaper in 22/24 trials, no systematic reversal: the vertex does not
make the measure select vacuum (0061 §3's measure-≠-equation lesson
survives where it should); what it establishes is the operational
riding — the measure concentrates on tetrad-geometric curvature, so
the gapless (1,1) carrier's favored content IS metric fluctuation,
with the vacuum question left to the action as the classical arc
always said. **The wall arc closes**: 0071 (abelian phases, D = 4,
N ≥ 3) → 0072 (kernel) → 0073 (sign problem) → 0074 (Born cure) →
0075/0076/0077 (spectrum, 4D criticality, heat-kernel fixed point,
gapless graviton channel) → 0078 (vertex simplicity) — six stones,
every one off the derived measure, no knob turned. Battery:
`build_S`, `jacobi_eig`, `vertex_price`. Honest limits: joint frame
integral, not yet a boundary-state 4-simplex with intertwiner
labels; ε′ = 0.01, seeded trials 8–24; six-columns lift for
Weyl/Ricci; Euclidean. Open: the boundary-state vertex and its
propagator (spin-foam-grade A3 completion); the in-context tension
spectrum (does (1,0)'s lightness survive shared-frame coupling?);
standing: Λ1, C1, arithmetic-branch pass, sign-problem toy, CLT
theorem, τ beta function.

## The filter adoption plan (0079)

Plan doc, no module (`exploration/0079`). Two decisions. **The
escalation protocol**: each outstanding wall piece is checked in the
full theory first; intractable pieces pivot to the Z_N toy (iterate —
multiple solutions likely live there). **The reframe**: the deeper
toy is the **lucid filter** — it hit the same blocks from the
opposite direction (this thread derived superposition-with-weights
from information postulates; the filter discovered the lit grid is
forced by tracking data), and it owns exactly the instruments the
physics side lacks: causality, real data, and an exact operational
loss. Dictionary recorded (seven established rows: trust = precision;
grid = superposition; Born = τ = s² (ported); nats both sides;
GPB1→IMM = product-blind→vertex; local level = fractional ν;
CLT→heat kernel = Gaussianization). **Six adoption rows**, each with
filter formulation, minimal extension, port-back, and trigger: F1
vertex propagator = coupled-bank cross-stream transfer function (+
the oracle-gap decomposition method applied to the propagator); F2
running of τ = prequential regret growth via a temporal-decimation
cascade — **filter-first, the instrument is exact where MK is not**;
F3 Lorentzian lift = causal attainability of the batch posterior
(their measured 96.3% ceiling as the template); F4 Born utility =
coherent IMM (amplitude-mixing vs probability-mixing, scored in code
length — highest upside, runnable on curiosity); F5 tangle =
cross-spectral tracking with CKW as a cross-information budget; F6
Λ/zero mode = the unobservable common mode that (1−B)^ν removes.
Seeded in lucid-filter as `research/wall-correspondence/` on branch
`claude/wall-correspondence`. Honest limits: structural
correspondence, not isomorphism — port-backs are candidate
principles; F5/F6 thin; the filter house rules bind work done there.

## The open budget (0080)

0069 §2's step 1 (budget off the compact torus) done exactly
(`exploration/0080`, `output/0071`, all enumeration/integer, no
sampling). **A disk has no budget**: all N⁴ flux combos attained with
identical multiplicity N^(V−1) — Σ F ≡ 0 was the closure of the
surface, not dynamics. **Frozen boundary restores it as Stokes mod
N**: Σ F ≡ hol(∂) exactly, every trial; torus control recovers Σ F ≡ 0
with the H¹ = Z² Wilson-moduli count. The budget is a topological
ledger: Λ-residual is exactly 0 (closed), a boundary datum
(Dirichlet), or a quantized observable (free). On the free disk the
exact distribution P(Σ F = h) = (1/N)Σ (Ŵ(n)/Ŵ(0))^P ω^{nh} with the
integer dual Ŵ(n) = Σ_{d|N,(N/d)|n} φ(d)(N/d): quantized at 2πh/N,
approaching **uniform** at area-law rate r_max^P with r_max = φ(N)/P(N)
= f(N) at prime N — the universe forgets its total curvature at the
confinement-tension rate (0064). Composite N: the coarsest subgroup
dies last (N=15: mod-5 residue survives at (4/9)^P, verified at
P=256). Consequence for the Λ path: the measure does **not** prefer
Λ = 0 on a free arena — smallness must come from closure or boundary
data; the program predicts quantization always, zero only for closed
universes. 0064's zero-mode divergence resolved: on the open arena
Ŵ(0)^P is just Z_disk — the divergence was the closed budget eating
the zero mode, not a pathology. Open: the 4D/nonabelian analogue
(connects to the boundary-state vertex), the continuum-τ zero mode
(step 2), the arena question (step 4).

## The Lorentzian congruence (0081)

The Lorentzian lift's kinematic shell, exact (`exploration/0081`,
`output/0072`). The Lorentzian star obeys S² = −I mod p, so the SD/ASD
split — the 4D program's working coordinates — exists over the base
ring iff √−1 does: **p ≡ 1 (mod 4)** (for composite N: every prime
factor ≡ 1 mod 4; 9 fails despite 9 ≡ 1). At p ≡ 3 (mod 4) the split
forces F_{p²} = F_p[i] — the continuum's complexification (why
Ashtekar variables are complex) in arithmetic dress — and **reality
conditions are Frobenius invariance**: x ↦ x^p maps SD onto ASD, 6/6
verified over F₄₉. The Einstein predicate is signature-blind: 0062's
kernel identity re-proved with η (rank 9 = 9 = 9; vacuum rank 10,
kernel = Weyl) at both congruence classes — and the price K(F) =
N⁴|ker F| and Pf(F) are metric-free, so the ledger never saw the
signature. The same congruence sets the amplitude's phase (Gauss):
g_p = √p real for p ≡ 1 (mod 4), i√p for p ≡ 3 — the amplitude whose
square is the ledger is real exactly where the SD split is real; the
arithmetic needs no Wick rotation to know about signature.
**Constraint stack on the level: odd (Born) + ≥3 (deconfinement) +
prime factors ≡ 1 mod 4 (Lorentzian) → smallest N = 5**; admissible
primes are exactly the sums of two squares. Honest limits: kinematics
only — no real-time measure, no causal structure, no claim the
dynamics selects the real class (the F_{p²}+Frobenius option stays
open, as complex variables do in the continuum). Open: the dynamical
lift (F3's causal-attainability doppelgänger now has a sharp target:
does the dynamics prefer the real-amplitude class?), the SU(2)
analogue, folding the stack into the bar's knob-derivation.

## The half space (0082)

C1 of path C done (`exploration/0082`, `output/0073`): the free
graviton's (0063) zero-point entanglement across a flat cut, exact
Gaussian covariance algebra, machinery certified against CFT first
(half-chain S = −(1/6)ln m to 0.2% at L=2048). **Area law measured,
coefficient extracted**: α = 0.0242 per polarization (NN stencil,
N⊥→64 extrapolants agree to 0.5%), S_graviton/A = 2α = 0.0484;
memory-flagged anchor Srednicki '93 spheres 0.30/4π ≈ 0.0239 — same
scale. The gapless channel (0077) signs the entanglement: the
subleading term is (1/6)ln L/N⊥², measured 0.1638 vs c=1 CFT's 1/6 —
the massless graviton line's central charge, the third independent
instrument to see the same massless thing. The coefficient is
**regulator-dependent**: the program's own central-difference stencil
factorizes exactly into doubler sublattices (S_cd(L) = 2S_sub(L/2) to
1e−9) and gives α_cd = 0.0482 (ratio 1.99, z-factor exactly 2,
transverse net ≈1 measured not proven) — the species problem on
schedule, so **C4 must be a renormalized-G (Sakharov) confrontation,
never a bare match**. Massive control monotone. Framing: this stone
is deliberately the standard side of 0067's tangle-vs-entropy
discriminator — the entropy side is present and textbook-correct in
this vacuum, so the program's difference must live at the coupling
(0067), to be confronted by C3/C4. Limits: free TT sector only, flat
cut not horizon, Srednicki from memory. Open: C2 thermality
(Bisognano–Wichmann, still Gaussian), C3 web-native capacity across
the same cut, C4 as renormalized-G, interacting/deconfined-phase
entanglement.

## The wedge temperature (0083)

C2 done: **Unruh for the free graviton, measured**
(`exploration/0083`, `output/0074`). Methods note: the inverse route
(reconstructing the modular Hamiltonian matrix) fails in double
precision — deep modular modes at ε ≳ 30 sit 1e−16 from ν = ½ and the
log divergence turns rounding into O(10) matrix contamination — so
the test is forward: build the lattice boost explicitly, compute its
exact β-thermal Gaussian state, compare states. Results: at β = 2π
the boost-thermal state reproduces the reduced half-space state near
the cut to 4.3e−5 relative (S to 0.026%, ν₁ to 6e−5); fitting β gives
**β*/2π = 0.9999** at m² = 0.0025 with deviation linear in m²a²
(coefficient ≈ 0.06) — a lattice artifact, β → 2π in the continuum;
fitting the horizon offset gives **s* = 0.5000** (the horizon sits
half a spacing beyond the last site, measured); the transverse tower
sees one geometric temperature (β*/2π = 1.0002 → 0.9811 as k⊥ = 0 →
0.4, both polarizations identical). Path C now holds both Clausius
inputs measured in-model: area-law entropy (C1) + Unruh temperature
(C2); missing is the coupling (source + first law = C3/C4). The
saturated-channel conjecture (is I → ∞ a horizon?) now has a modular
target. Limits: free theory only, near-cut window (deep modular
spectrum untested), k⊥ = 0 line IR-regulated, boost discretization
choice absorbed into measured s. Open: C3 (discriminator at field
level), C4 renormalized-G, saturated channel, interacting thermality.

## The capacity cut (0084)

C3 done (`exploration/0084`, `output/0075`): the web's own count
across C1/C2's cut. The cut decomposes exactly (spectra of the two
sides match to 5.6e−16) into **collective two-mode-squeezed
channels**, each a relational channel with QFI = sinh²(2r) = 4ν²−1 —
the CV heir of C² — so the whole ledger chain applies per channel:
W_k = 4ν_k²−1, I_k = ln 2ν_k, δ_k = 2π(1−1/(2ν_k)). **The pairwise
account fails exactly as 0068's GHZ lesson predicted**: two-site
negativity across the cut is nonzero ONLY for the adjacent pair
(exact zeros at every other separation, chain and 3D), carrying
12–15% of the cut; the field vacuum is GHZ-like, P1's node-vs-rest
reading is forced. Site-level CKW-shaped monogamy holds (0.033 ≤
0.089), collective share 63% (correcting a first guess of ~99%).
Three area laws on one spectrum, coefficients per polarization:
S/A = 0.0244, W/A = 0.0179, **δ/A = 0.0522 rad/plaquette** → the
graviton's horizon charge 0.104 rad per plaquette (ledger units —
C3's done-criterion). The discriminator now RUNS: W/S drifts 0.79 →
0.61 across a mass scan — capacity- and entropy-coupled horizon
charges respond differently to mass/IR, so C4 will decide between
them, not straddle. Noted: δ_k saturates at 2π per channel as ν → ∞ —
0066's full-turn cap reappearing at the cut (feeds the
saturated-channel/horizon conjecture). Limits: W_k is the natural
TMS-QFI *extension* of 0065's derived pair capacity, not yet derived
from a field-level inference network (the gap); free theory; W/A is
the most IR-sensitive account ((ln ξ)² per mode). Open: derive the
field capacity from the postulates, C4, saturated channel = 2π per
channel?, decoherence tier.

## The quarter (0085)

C4 done as located-plus-finding (`exploration/0085`, `output/0076`).
**Located, not derived**: S/A = A/4G fixes a = 0.44 ℓ_P (NN entropy;
0.38–0.63 across account/stencil) — a consistency condition (G is
registered), the Sakharov/induced position exactly as 0082 §4
predicted; no bare match exists. **The finding**: the program keeps
two ledgers. Deficit additivity (0012) gives a horizon's sourced
deficit δ = 8πGM = 2√(πA) — G-independent, ∝√A — while the measured
vacuum-cut deficit is area-extensive (0.0522 rad/plaquette): the
deficit is the SOURCE ledger (mass-extensive), entropy/capacity the
RECORD account (area-extensive), and **only the record account can be
Bekenstein–Hawking**; they cross at R* ≈ 4 ℓ_P. Corollary: above
~5 ℓ_P the zero-point record dwarfs the sourced deficit, so the
vacuum record must not source (else curvature catastrophe at every
cut) — the budget/zero-mode deletion (0069/0080) is the protection:
**path Λ's constraint makes path C's vacuum safe; the two paths
protect each other undesigned**. Saturated-channel picture sharpened:
99% of the 2π cap at I = ln 100 ≈ 4.6 nats; extremal 3+1 channel = a
string of tension 1/4G; a mass M's extremal string totals L = 4GM =
2R_s — **the horizon's source structure is one-dimensional (~R_s/ℓ_P
strings, 0061 §4's Ambrose–Singer defects), its record structure
two-dimensional (A/ℓ_P²)** — stated for falsification against
holography's area count. Limits: Rindler proxy; chained
interpretation for 8πGM; bundle is conjecture-shaped; the
mutual-protection argument is structural, not yet computed. Open: the
protection calculation (cheap, Z_N-toy-sized: budget + defect on an
open lattice — vacuum record sources nothing, defect does), extremal
channel through a cut vs C2's modular structure, decoherence as
transfer between the two ledgers.

## The two ledgers (0086)

0085's protection calculation, run in the Z_N toy — **the first
pivot down the escalation ladder**, and the toy *corrected* the
story (`exploration/0086`, `output/0077`; dual t-sum vs brute flux
enumeration at 1e−12 throughout). **The polar theorem** (exact, open
lattice): ⟨W⟩ = e^{i·2π Σ_enc n_p/N}·f(N)^A — 0085's two ledgers are
the polar decomposition of one complex number: phase = source ledger
only (additive, area-independent), modulus = record only (area law,
blind to sources). The vacuum record cannot twist categorically — no
budget needed; |⟨W⟩| is the confidence channel, arg⟨W⟩ the content
channel (the seed split materialized). **The budget does NOT delete
uniform sources**: at N|P a uniform frustration passes untouched
(phase = 2πA/3 exactly — a quantized-Λ leak); at coprime N,P the
budget subtracts one localized quantum (fluxes are discrete, no
smearing), uniform curvature appears at ~full strength, and the
smeared trace-removal guess (1−A/P) is rejected by measurement. The
budget's one job: the A = P loop reads 0 exactly — **Λ·V quantized in
2π/N units** (0069's spectrum, 0080's residual, now dynamical).
Revision recorded for 0085 §2: layer (i) record-safety = polar
theorem (constraint-free), layer (ii) budget = global Λ quantization
only. Small-universe effects measured: vacuum complementarity
|W(A)| = |W(P−A)| bends the f^A law by A ~ P/2; an enclosed defect
keeps 99.9% of its deficit at A/P = 1/9, eroding to 72% at 4/9.
Limits: abelian toy (the factorization's exactness is special to the
product measure); frustration as the source model; continuum limit
open. Open: the nonabelian polar split (central phase × class
modulus — bridge back to the full theory via 0078's machinery),
Λ-leak phenomenology (Λ ∝ (Pn mod N)/P·2π/N into 0069 step 4), the
2+1 continuum limit, decoherence as modulus→phase transfer.

## The nonabelian split (0087)

The two ledgers survive the lift (`exploration/0087`, `output/0078`;
2D rung, the program's Born counting weight W = A², A = Σ_{j≤2}χ_j).
SU(2) characters are real so the abelian phase can't lift as a
phase — it lifts as a **character-indexed factorization**:
⟨χ_j(loop)⟩ = [χ_j(h₀)/d_j]·d_j r_j^A, source and record exactly
separated per rep. **The record envelope is fusion arithmetic**:
r_j = c_j/(d_j c₀) with c_j the fusion count — flat counting gives
exact rationals 1, 4/5, 2/3, 1/2, 9/25, 1/5 (quadrature = counting at
1e−8); f(N) = φ/P's heir is the Born weight's fusion table. **The
reading theorem**: ⟨χ_j⟩(A,h₀)/⟨χ_j⟩(A,e) = χ_j(h₀)/d_j at every
area — the record damps but cannot distort; validated by
gauge-unfixed 7-link MC (vacuum d_j r_j² within errors, readings
match, θ₀ reconstructed 0.9005 vs 0.9). **Where the phase went**: the
abelian phase shrinks to the center Z₂ (center twist reads (−1)^{2j}
exactly — 't Hooft sector, SU(2)'s only true phases) and the
continuous deficit migrates into the reading spectrum. Corollary:
integer-j probes (the graviton channel) are center-blind — fermions
would see a topological sector gravity cannot. Limits: 2D gluing
(4D = the vertex, untested conjecture); one counting; MC at A=2.
Open: test the split on one 16D vertex (class twist into 0078's
Gaussian), 't Hooft superselection for the matter thread,
non-commuting multi-source ordering, reading theorem as a
channel-capacity statement (F1's dictionary row).

## The vertex coupling (0088)

0087's open 1 against the real 4D object (`exploration/0088`,
`output/0079`): **the two-ledger split fails at the vertex,
measurably, from first order — and the failure is the physics.**
Test: shift one plaquette by a fixed source δF, ask whether the price
response depends on the other five (context). Free-tier control:
under the product weight the response is context-independent to
1e−12 (locality = the reading theorem's precondition). At the vertex:
the same source's response ranges over contexts by 0.17–1.5 nats
(mean spread 0.72), even flipping sign; converged central-difference
linear coefficients +1.113/+0.061/+0.543 across geometric/foreign/
random contexts — coupling present from first order. Orientation
lensing: rotating the source's plane from its own slot toward a
foreign one traces a smooth 2.17 → 1.69 nat curve — the vertex
charges orientation relative to the ambient frame. Reading: the
ledger separation is a free-tier theorem (2D = topological =
distortion-free), and the vertex is precisely where it must break —
context-dependent reading is the measure-level seed of gravitational
nonlinearity (geometry reads geometry). Mechanisms named: decoherence
-as-transfer can only happen at vertices (free tiers keep ledgers
separate); 0087's reading theorem governs propagation between
interactions, while readings through interacting regions pick up
context (lensing's information shape: attenuation honest, orientation
charged). Limits: Gaussian-regulated vertex not boundary-state;
algebra-valued sources (center sector invisible); 6 seeds. Open: the
coupling tensor/susceptibility (cousin of the cubic graviton vertex),
in-context tension spectrum as one entry of it, the measurement
thread's first stone (does a channel's modulus leak into phase at a
vertex?).

## The context spectrum (0089)

0075's standing interleaving tested at the vertex
(`exploration/0089`, `output/0080`). Anchor: the vertex kit closes in
SD/ASD variables — single-plaquette eigenvalues ±(|F⁺|±|F⁻|)/(2√2)
fourfold, 2Pf = |F⁺|²−|F⁻|², so the (1,0)/(1,1) distinction is the
η = |F⁻|/|F⁺| axis in the measure's own variables. **The unbalance
curve** (64 paired seeds, geometric context): context Δprice falls
monotonically 5.05 → 3.89 as η: 0 → 1 — pure self-dual is the most
expensive content a geometric vertex can be handed, balanced the
cheapest; paired SD-over-balanced penalty **+1.17 ± 0.12 nats/site**
(59/64 positive, isolated +0.57 ± 0.31, amplification ~2×); the SD
insert sits at/above the non-simple rung of 0078's ladder (extreme
non-simplicity, charged accordingly). **Verdict, honestly sized**:
the penalty exceeds the 0.10–0.30 nats/step bare-chain gap by 4–12×
(clears the upper bound at ~7σ) — any assembly charging ≳ half a
vertex per chain step lifts (1,0) above (1,1); the interleaving is a
bare-chain artifact as 0075 conjectured, mechanism = the shared-frame
integral's specific dislike of unbalanced curvature (simplicity as a
mode filter, EPRL's hand-imposed constraint generated with measured
strength). NOT decisive: different currencies (nats/step vs
nats/site), assembly share unfixed — the decisive object is the
assembled 4D complex (A3 completion), which now has its ordered
candidate list (0075) and its per-site charge sheet (here). Limits:
one slot/one vertex shift design, ε′ = 0.01, means-level
monotonicity. Open: the assembled complex, the full coupling tensor,
coherent-state refinement.

## The even wall (0090)

The sign-problem toy packaged, and upgraded (`exploration/0090`,
`output/0081`). **The wall**: no integer counting amplitude (frame
multiplicities c_e ≥ 0 with autocorrelation = Ŵ) exists for even
N — exhaustive at N = 2, 4, 6, 8, 10; odd N's quadratic count
re-verified. **Not positivity**: real nonnegative amplitudes exist at
every even N ≤ 16 (PSD square root, exact) — at N = 2 the entire
failure is 2c₀c₁ = 1, half a frame. The wall is INTEGRALITY:
quantization itself (frames come in wholes) rejects even levels.
**The cure is the double cover**: doubling the frames on the 2-part
gives |A|² = 4·N·gcd exactly at every flux (verified N = 2, 4, 8, 16
and 6, 10, 12, 24) — cover degree squared as normalization, frames
whole upstairs. Reading: even levels are the ledger's SPIN levels —
the second independent arithmetic shadow of spin beside the
Lorentzian mod-4 congruence. Constraint stack: "N odd" softens from
exclusion to covering instruction; smallest level stays N = 5 (the
Lorentzian congruence rejects even N independently). Limits:
exhaustive only to N = 10 (parity proof sketched, not written);
spin-structure is structural not spinor-constructed. Open: the parity
proof, whether the two spin shadows compose in one structure
(Gaussian integers mod N?), covered-family RG.

## The arithmetic pass (0091)

Audit stone, no module (`exploration/0091`): the formal-languages
arithmetic branch's late probes (0064–0066: epistricted wall, sign
problem, reference tower, braided holonomy) walked and reconciled.
Verdict: **nothing load-bearing is stranded**; two items carried
forward. (1) **The mandatory-amplitude boundary** (their epistricted
theorem, ported as an honesty theorem about our foundations): a
knowledge-restriction alone reproduces exactly the stabilizer
fragment and cannot cross the contextual fraction — so whatever
carries this stream past that line (the Fisher/Bures amplitude
structure) is doing irreducible work; P1–P5 is not a hidden epistemic
restriction. (2) **Two streams, one door at 2**: their "binary fibers
cannot braid (S₂ abelian); the door is a doubled shared channel"
independently matches 0090's even wall + double-cover cure — two is
degenerate and doubling opens the door, found from opposite sides.
Echoes recorded: their conserved reference coin ↔ the budget's one
global mode (0086); their negativity-on-the-phase-fiber ↔ 0073/0074's
sign problem and Born cure; their noncommuting-loop quantization open
= 0088's ordered multi-source open (jointly filed). Limits: late
probes read in full, interior 63 explorations at summary level;
finding 1 imported, not re-run.

## The heat-kernel theorem (0092)

The queue's "CLT fixed-point theorem" attempted — **false as filed,
replaced by better** (`exploration/0092`, `output/0082`). True part:
second-moment universality — any light-tailed class weight of width s
has −ln r_j = (2/3)⟨θ²⟩C₂(j) + O(s⁴) (verified: Gaussian and window
collapse with dev ∝ s², τ to 0.1–0.3%). False part: **the freeze
lemma** — convolution powers coefficients, so log-ratios never move:
no convolution CLT can reshape a spectrum toward Casimir ratios. And
the ledger needs reshaping: the Born counting weight has kurtosis
13–25 (Fejér-squared tails), flatness dev 0.63–0.67 at any width —
the bare ledger never resembles the heat kernel. **True mechanism:
the MK bond move (pointwise power) is a Laplace localization** — ONE
blocking takes flatness 0.633 → 0.0016; the flow thereafter moves
only τ. 0077's Casimir ratios are an RG-localization result with the
entry mechanism identified and its speed measured. Bonus: the freeze
lemma retroactively unifies 0086/0087/0088 — free tiers can neither
distort sources nor renormalize themselves for the same reason
(convolution preserves everything); structure moves only where
nonlinearity lives. Consequence: **the τ beta function is now cheap**
— structure frozen after one blocking ⇒ the flow is a scalar map
dτ/d(block). Limits: basin boundary (kurtosis threshold) unmapped;
2/3 is χ-normalization convention. Open: basin boundary, the scalar
τ flow (F2's in-theory version, now cheap), the assembled complex.

## The τ flow (0093)

The running of τ — one of the wall's three outstanding pieces, filed
heavy, delivered cheap via 0092 (`exploration/0093`, `output/0083`).
The flow is one-dimensional (heat-kernel leak ≤ 1.2e−4 per step,
measured then relied on): the 4D MK recursion is a scalar map. **The
beta function has the one-loop shape**: β = c·τ²(1+O(τ)), c(b=2) =
0.127 ± 3% over τ ∈ [0.05, 0.2], POSITIVE — τ = 0 is the UV fixed
point: **asymptotic freedom in the ledger's one continuum coupling**,
with the confining runaway (super-quadratic β) at strong coupling.
Scheme test b = 3: sign and quadratic order stable, coefficient
±30% (MK-typical; continuum b₀ = 22/3 memory-flagged, MK overshoots
3–4× as usual). **Dimensional transmutation verified by direct
integration**: strong coupling at n = 152 blockings vs one-loop pole
prediction 157 — ln(L*/a) = ln b/(cτ₀): an invariant scale from a
scale-free start, the program's first emergent dimensionful quantity
and an unforced hierarchy-generation mechanism (pin τ₀ and the
formula predicts a hierarchy — the RG arc's sharpest
falsifiable-shaped statement, feeding 0069 (D)). Reconciliations:
0076's "near-stationary" = slow one-loop flow below their
resolution; 0077's gapless channel untouched (ratios preserved, τ
scale runs); F2's filter-first call updated — the theory got there
first via 0092, and the filter row keeps a sharpened numeric target
(regret coefficient vs c). Limits: MK uncontrolled (30% = floor of
the error bar), τ-to-physical-normalization unfixed, Euclidean.
Open: pin τ₀ (vertex normalization or N = 5), the two-coupling flow
(τ + vertex susceptibility), F2 cross-check, the assembled complex —
now the wall's last outstanding piece.

## The pinned flow (0094)

The knob-derivation attempted (`exploration/0094`, `output/0084`):
**the program's first no-continuous-knob chain to a dimensionless
number**. Chain: constraint stack → admissible N (5, 13, 17, 25,
29) → level cutoff J(N) (quantum-group admissibility, both
conventions k=N and k=N−2 carried) → the DERIVED Born counting
weight (no dial) → one MK blocking → τ₁(N) (heat-kernel flat ≤
0.0025) → ln(L*/a) = ln2/(c·τ₁). **The menu**: N=5 → 10⁸–10¹⁷;
N=13 → 10⁶⁵–10⁸⁸; N=17 → 10¹¹⁴–10¹⁴³; exponent quadratic in the
level (τ₁ ≈ 1.2/J², ln L* ≈ 4.5 J²). May be claimed: a discrete
menu of exponentially large pure numbers from derived structure —
0069 (D)'s demand met in shape. May NOT be claimed: matches to
observed numbers (near-misses recorded honestly: 10¹⁷ ~ M_P/M_EW at
N=5, 10⁶⁵ ~ horizon/Planck at N=13 k=N−2 — but c is ±30% on the
EXPONENT, conventions move small-N exponents 2×, and the
level↔cutoff identification is a modeling bridge, NOT derived — now
the arc's sharpest open). Falsifiability shape: derive the bridge +
match one level, and every other level is a prediction; the
N²-quantized menu is itself refusable. Open: derive the cutoff from
the ledger's own consistency (the cover/congruence arithmetic
suggests it knows), controlled scheme for c, healed-weight τ₁.

## The assembled momentum (0095)

A3's momentum half attacked perturbatively — the perturbative half is
DONE (`exploration/0095`, `output/0085`). From Σs² = Σ|F|²: price =
Σ|F_p|²/2ε′ − trS⁴/4ε′² + O(s⁶) (verified by exact halving). **Tree
level = six independent massless lattice Maxwells**: the propagator
is 1/k̂², massless, sector-blind — the momentum half at leading
order. **The one-loop isotropy theorem (exact)**: the quartic's
tadpole is Q_ab = 4.75δ_ab (machine-exact polarization), and with
the TRUE same-site lattice covariance (off-diagonals ±0.108, phases
included) Q(SD) = Q(ASD) = Q(bal) to 1e−9 — the off-diagonal
covariance decouples exactly. At one loop in the assembled vacuum:
no graviton mass (protected, not tuned), NO sector splitting (the
(1,0) lift is not a weak-coupling vacuum effect), and the vertex's
whole content is isotropic field-strength renormalization with the
confining sign (0093's β diagrammatically). **Where the sector
physics lives**: finite content on geometric backgrounds — 0089's
+1.17 nat split is real but the infinitesimal Hessian split is
pack-noisy consistent with zero, with a sign crossover at amp ~
√ε′: masslessness and sector-democracy for vacuum fluctuations,
simplicity enforcement for content (0078's non-flip, sharpened).
A3 ledger: tensorial half done (0075/0089), momentum tree + one loop
done (here); open: strong-coupling sector fate (scoped: heavy
nonperturbative MC — the honest boundary of this run), two-loop
sunset (where isotropy could break), boundary-state vertex.

## The pinned root (0096)

New arc: the homomorphism to the lucid-filter family (owner's
redirect: Z_N has done its job — its trust/content split is
degenerate by our own polar/freeze theorems; the fusion tier needs
the filter). Their repo read directly; the predicted minimal
dynamics object — their bias computation — delivered the first row
as a theorem both programs proved independently
(`exploration/0096`, `output/0086`). **Their 0041**: a bias lives
only in a root pinned at z = 1 exactly; a free ML fit lands at 1±ε
and a root is an exponent (additive drift → geometric catastrophe);
cure = factor (z−1)^d by construction; right pin free, wrong pin
loud. **The mirror, exact**: r₀ = 1 for any weight (conservation =
the automatic pin), every nontrivial channel of a generic weight has
r < 1 strictly (mass is generic; a free measure cannot hold a
nontrivial unit root), near-symmetric weights give the 1/ε-horizon
catastrophe (0056's massive graviton = the free fit; 0063's
by-construction masslessness = the pin), and single-center-element
weights hold |r_j| = 1 exactly (topological channels are pinned
roots). Both sides verified in miniature (free AR(2) root at
1±0.005, 5× h=60 bias vs pinned; physics side exact). Two more rows:
their AR(1) trust-dynamics assumption ↔ our heat-kernel closure
(both: minimal honest assumption = closed one-parameter confidence
family + persistence map; their "s_P = 0 is an absolute claim" = our
exactly-massless-vs-slightly); their prequential floor for p (flat
above, AIC/BIC refused = no-knobs) ↔ **the bridge reposed: J is a
floor (minimal-support existence), not a matched value**. Noodle
sharpened: the sporadic-groups instinct aims, in SU(2), at the McKay
correspondence — binary icosahedral/E₈ as the distinguished finite
stopping structure; the bridge's cyclic restriction is the A-series
case. Open: the fusion row (oracle-gap/IMM vs 0088; discriminator
experiment designed), the floor computation, the McKay restriction,
φ ↔ flow-contraction quantitative.

## The marginalized vacuum (0097)

Step 1 of the crossing plan executed: the filter's marginalization
built in the physics on analogy alone (`exploration/0097`,
`output/0087`) — **the ridge tilts, and the tilted coordinate is the
scale**. Design: 0095's isotropy theorem is the physics' ridge (the
point vacuum's Gaussian summary makes sector structure exactly flat);
replace the point vacuum with hypothesis-set vacua at MATCHED second
moments. Three ensembles, one covariance: H1 geometric mixture
(tetrad packs, kurtosis 5.95), H0 its Gaussian collapse (2.99), H2
scale mixture (no geometry, 6.02). Result: sector split of a t = 0.5
probe = +1.71 isolated; **+0.004 ± 0.003 under the collapsed vacuum
(flat — the mean-strength bath erases even the isolated splitting)**;
**+0.47 ± 0.006 under the geometric mixture (75σ)**; +0.50 ± 0.012
under the scale mixture. Attribution: H2 ≈ H1 — the information rides
the RADIAL mixture (weak-bath epochs), not orientation: the
marginalized coordinate is the vacuum's SCALE. The analogy snaps onto
the filter's hardware: sector-carrying channel = their wandering-scale
s_P > 0; collapsed vacuum = their self-confirming s_P = 0; their next
item (marginalize the (φ_P, s_P) grid) is what the physical vacuum
needs. Closes a loop with 0092 (the kurtosis localization kills for
universality is the structure carrying sector information —
universality and sector-blindness are one phenomenon) and reframes
0095 (one-loop no-splitting was diagnostic of the collapse, not the
theory); the strong-coupling question sharpens to: measure the
interacting vacuum's radial mixture — the physical s_P. Limits: one
observable/one bath shape; ensembles hand-built not derived;
analogy-first by design. Open: step 2 — the homomorphism proper
(transfer semigroups with confidence channels; catalogue the
isomorphism gap = the toy-to-prototype upgrade list), the derived
scale distribution (MC's sharper target), then regime-hazard as the
blueprint's pressure point.


## The homomorphism (0098)

Step 2 delivered (`exploration/0098`, `output/0088`): both families
stated as one algebraic object — a polar transfer semigroup with a
predict/update cycle — the map proved where it holds, the failure
located and quantified. **Theorem 1 (free tiers isomorphic)**: Kalman
predict on modes = e^{ikμ}e^{−qk²/2} (drift in phase, noise in
modulus — the polar theorem on ℝ, verified 5e−16); ledger chain =
ω^{nf}e^{−τn²} on Z_N (9e−16); additive composition both sides: one
object, two groups. **Theorem 2 (one MK blocking = one Kalman
cycle)**: bond move = Bayes update on ζ−1 parallel replicas (exact),
decimation = predict; the RG is a self-measuring filter, τ its
posterior variance, conjugate families correspond
(Gaussian ↔ heat-kernel); on ℝ with ζ = b² the cycle is EXACTLY
marginal: β_ℝ = 0. **Theorem 3 (the gap is noncommutative curvature,
not compactness)**: the same cycle on ℝ / U(1) / SU(2) gives β = 0
exactly / < 1e−6 for τ ≤ 0.4 (winding invisible) / 0.127τ² —
running, transmutation, and confinement are the residue of
noncommutative group curvature alone: **asymptotic freedom is the
homomorphism's defect, with a measured coefficient**. The catalogue
(toy→prototype upgrades): 1 group curvature (build: filtering on S³ —
a walking filter on a sphere would have a running regret); 2 external
innovations (the physics only self-conditions — "who supplies the
innovation?" = the measurement/causal layer); 3 the hypothesis bank
(0097's cure); 4 discrete sectors (superselection ↔ regimes: pressing
regime-hazard IS building this tier — the owner's pressure point =
catalogue row 4). Transports proved: free tier, cycle, conjugate
closure, pinned roots, marginalization. Limits: MK-hierarchical
exactness; mechanism identified not dissected; gaps 2/4 located not
built. Open: the S³ prototype brick, regime-hazard, the innovation
question formalized, the MC as a bank-tier computation.

## The S³ filter (0099)

Gap 1's prototype brick, and the run's sharpest quantitative result
(`exploration/0099`, `output/0089`). **The fusion tax**: Bayes fusion
of two heat kernels on SU(2) fails the flat precision law by a
WIDTH-INDEPENDENT constant — p_post = p_a + p_b − δ, δ = 0.1686 ±
0.9% (equal and unequal widths, τ = 0.02–0.4), drifting to 1/6 =
0.1667 at small τ (DeWitt a₁ = R/6 candidate, flagged); U(1) tax ≤
1.6e−4, ℝ zero by algebra — curvature's alone. **The beta law
derived**: a bond move is ζ−1 fusions ⇒ β = (1−1/b²)·δ·τ²,
predicting c(b=2) = 0.1264 and c(b=3) = 0.1499 vs 0093's measured
0.127/0.151 — 0.4% and 0.8%: the MK "scheme dependence" is the exact
factor (1−1/b²), δ is the scheme-independent core, and **the beta
function is the information the geometry's self-measurement loses to
curvature per fusion**; if δ = 1/6 exactly, β = (1−1/b²)τ²/6 closed
form. **The running filter**: the S³ cycle's stationary width exceeds
the flat Kalman fixed point, excess growing with noise scale — the
walking filter on S³ runs (0098's prediction, run). **Family
breakdown** past τ ~ 1 (leak 2e-2 at 1.5): the curved filter's
strong-coupling scale. Upstream: 0093's c upgraded to a law; 0094's
error budget collapses to the δ identification; 0098's gap now has a
measured magnitude, measurable from the filter side by any S³ fusion
experiment. Limits: 3% constancy drift; 1/6 numerical not derived;
symmetric updates (width recursion, not tracking); U(1) bound
numerical. Open: prove δ = 1/6 (the (j+½)²−¼ shift, likely
three lines), filter-side δ measurement, gap 2 (the innovation
question), the S³ association problem.

## Known gaps

Superseded in detail by `exploration/0048`'s "honest residue" (the
maintained list). Standing items in brief: κ normalization; lattice
Palatini; the Lorentzian-arena step; the closed-loop test; the
two-body residual; content/level-rung freedom; P4 → Tsirelson
(`exploration/0007` step 3); continuum versions of the 0010
arithmetic-frame results; matter dynamics beyond scripted sources
and the frame field's full quantum dynamics.
