# Relational–Epistemic QM: a knowledge-first, consistency-first reading

**Thesis.** Take the viewpoint of a single particle *A*. Everything *A* can act
on is a probability distribution over the *relative* positions and momenta of
other particles — *A*'s **knowledge state**. Other particles are bumps in that
distribution; none are exact Dirac deltas. **Mutual consistency** of the whole
web of pairwise knowledge distributions is the fundamental law. It is nonlocal
by nature: sharpening one edge instantaneously re-settles the whole connected
component. Under this reading, **measurement is the exact coincidence of
particles** (a split or a merge) — the event that makes a relative coordinate
sharp and triggers the global re-projection.

## The two-tier structure that reconciles instantaneous updates with relativity

Knowledge splits into two kinds:

- **Actionable knowledge** — what a system can use to *do* something
  differently (forces, signals). *c*-bounded, standard relativity.
- **Correlational knowledge** — the mutual consistency of the web. Updates
  **instantaneously, nonlocally**, because it is the satisfaction of a global
  constraint, not a propagation. Non-signalling because outcomes are random
  and average to zero in every distant marginal.

That firewall is the resolution of the c-vs-instantaneous puzzle from *inside*
the posit.

## The central derivation

The consistency law, read faithfully, requires that the web be **locally
consistent on every overlap** but need **not** admit a **single global joint
distribution of definite values**. By Fine's theorem, that is exactly the
sheaf-theoretic signature of quantum contextuality/nonlocality — and it
automatically forces departure from the classical Bell polytope. So the
posit's own "no absolute source of truth" *derives* the fact that reality
must be non-classical.

Demonstrated numerically in `testability/output/0002_global_section_test.py`:
Tsirelson (S=2√2) correlators are pairwise legitimate but have no global
section; classical (S=2) correlators have one.

## Recursive consistency is the heart

P4 is not just variance-additivity — it is a **cocycle condition** on the
web (`foundations/exploration/0004`). Composition of pairwise knowledge along
any two paths between the same endpoints must agree; composition around any
loop must be trivial-up-to-phase. That is Čech cohomology of a constraint
sheaf on the interaction graph. The obstruction to a global consistent state
is the graph's first cohomology `H¹`.

- Tree-shaped webs (no loops) → trivial cocycle → classical.
- Loop-containing webs → nontrivial cocycle possible → frustration (classical
  composition) or contextuality (quantum composition).
- The **composition rule on edges selects the theory**: convolution → classical
  probability; symplectic/unitary → QM; other rules → other GPTs.

Classical frustration (spin-glass triangles) and quantum contextuality
(Kochen–Specker, Bell) are proposed to be the *same* mathematical structure
(non-vanishing `H¹`) differing only in composition rule. Verified numerically
for the compatible-observable triangle in `testability/output/0003`: the
polytope is exactly the classical tetrahedron (1/3 of the cube). Contextuality
requires **choice of incompatible measurement basis** — the "context" in
"contextuality" is a choice, not merely a graph topology.

## The frontier

Non-extendability alone rules classical out but does not pick quantum over
super-quantum. Two live candidates inside the posit for tightening `4 → 2√2`:

1. **P4-as-cocycle-on-Wigner-functions ⇒ information causality** (Pawłowski
   et al. 2009 derives Tsirelson from an information-processing axiom;
   whether the recursive-consistency cocycle entails it is the concrete open
   theorem).
2. **MRE projection inside a PR-box scenario** — check whether the update rule
   over-constrains super-Tsirelson correlations in a way the quantum update
   does not.

Neither shown; both concrete and tractable.

## Geometry of the web (the GR-analog, made literal)

Saying "knowledge is a distribution" already commits us to a Riemannian
geometry on the space of knowledge states — with no freedom of choice: the
Fisher–Rao metric (Chentsov 1972) classically and the Bures / Fubini–Study
metric (Petz 1996) quantum-mechanically are the *unique* metrics invariant
under sufficient statistics / CPTP maps. That fixes:

- Gaussian knowledge → hyperbolic plane (constant negative curvature).
- Qubit knowledge → the Bloch sphere with the Fubini–Study metric (constant
  positive curvature). Fidelity is `cos²` of half the geodesic angle.
  Verified in `foundations/output/0001_qubit_geometry.py` including a clean
  Gauss–Bonnet check on a spherical triangle.

The GR-parallel becomes literal: general covariance ↔ invariance under
sufficient statistics; light-cone causal structure ↔ two-tier
actionable-vs-correlational split; parallel transport around a loop = the
cocycle holonomy of `foundations/exploration/0004`; uncertainty relations
are curvature bounds on the state manifold (Anandan–Aharonov speed limit).
"Correlation sources curvature" — the analog of Einstein's equations — is
the honest open frontier (holography / Ryu–Takayanagi territory).

The engineering payoff is immediate: fidelity, coherence, control, and
optimal estimation are all geodesic / curvature quantities on the same
manifold, so the framing lines up with existing quantum-info tooling and
hopefully makes it feel less arbitrary.

## The two-tier structure & the FTL barrier

Taking the user's precise reading of SR: relativity forbids *continuous*
crossing of `c`, not FTL per se. That leaves a clean geometric slot for
discrete, non-signalling correlational updates:

- Actionable knowledge = dynamics on the manifold (timelike/null, ≤ c).
- Correlational knowledge = spacelike constraint structure of the manifold.

The distant instantaneous edge update is spacelike-slice re-shaping, not
signal transmission. Nothing crosses `c` because nothing crosses at all. See
`foundations/exploration/0006`.

## Reconstruction route

`foundations/exploration/0007` lays out a candidate axiom set — P1–P5 plus
Fisher/Bures uniqueness, purification, continuous reversibility — as a
concrete route to deriving standard finite-dim QM, drawing on Hardy (2001),
CDP (2011), and Masanes–Müller (2011). What the consistency-first packaging
may add is a single unifying physical picture motivating those axioms at
once, plus the two-tier resolution of the c-vs-instantaneous puzzle.

## Mass as trapped momentum (`trapped_momentum/`)

A side workstream on a reframing: a particle as a massless excitation closed on
itself. The premise is not a departure from established theory — the Dirac
velocity operator `cα` has eigenvalues `±c` only, so a free electron already
moves at `c` instantaneously, with zitterbewegung at `2mc²/ħ` and amplitude
`ħ/(2mc)`. Taking that as fundamental, three things drop out exactly
(`output/0001`, 39/39 checks):

- **Spin, with no free parameter.** `L = mcr = mc·ħ/(2mc) = ħ/2` — the mass
  cancels identically.
- **Both de Broglie relations.** An internal clock at `ω₀ = mc²/ħ`,
  Lorentz-transformed, *is* a plane wave: `E = ħω` and `p = ħk` become
  theorems rather than postulates. Exact at every speed tested.
- **Time dilation**, from `sin θ = v/c` on the helix — total speed `c` split
  between circulating and translating.

Pressing on whether a boost should reduce the trapped angular momentum
(`exploration/0002`) produced the sharpest form of the claim:

```
m c = p_⊥      p = p_∥      E² = (p_⊥c)² + (p_∥c)² = (mc²)² + (pc)²
```

`L = r·p_⊥ = r·mc` is then invariant for the same reason rest mass is; the two
statements are one. That split is frame-adapted though, and the covariant form
(`exploration/0003`) is better: the ray's worldline is a **null helix winding
about the particle's own timelike centre-of-mass worldline** — `ds² = 0`
throughout, spacetime pitch exactly 45°. "Rotation around the time axis" is
literal; the spatial circulation plane is only its 3D shadow, which is why
choosing a spatial axis felt arbitrary. Boosting **tilts that axis**, and
inertia is resistance to the tilt: a boost can always remove the spatial
momentum but **never** the rest energy, so `mc²` is the irreducible timelike
component of `P^μ`.

The central result (`exploration/0004`): a 2-plane in Minkowski space has an
induced-metric determinant whose **sign is Lorentz-invariant and takes exactly
three values** — spacelike (rotation), timelike (boost), null (null rotation).
"The time axis, the space axis, or their `x = t` line" is that classification,
forced by the signature rather than chosen. And **quantization is compactness**:
only the spacelike plane gives a closed orbit, so only it yields a discrete
spectrum. Running the Fourier argument both ways — `δ_{mn}` on a circle,
`sinc` with no admissible lattice on the line — makes that exact.

Scored against measurement: spin quantized (closed orbit) ✓, helicity quantized
✓, **mass not quantized** (open orbit) ✓ — `m_μ/m_e = 206.768`,
`m_τ/m_μ = 16.817`, no ladder. **The split between "mass is continuous" and
"spin is quantized" falls out of the causal type of the winding plane.** It
also decides KK-vs-timelike on data: a compact spatial dimension would give a
mass tower, and none is seen.

Blocked on a real defect: the loop radius giving spin `ħ/2` makes the
circulating quantum carry `2mc²`, and the radius giving `mc²` predicts spin 1.
**Right spin or right energy, never both.** Now a sharp fork rather than a
mystery — a loop *in space* has period `2π` → `L = nħ`, a loop *in the rotation
group* has period `4π` → `L = nħ/2`. The model must say which object winds, and
this version predicts the number 2 rather than accommodating it.

Method rule adopted here: **name the assumption, cite the measurement.** It
earned its keep — a Casimir argument that looked like an obstruction was not
one, while measurements (Higgs spin, the absent mass ladder) did the real work.

Substantial prior art, named in the summary — Hestenes' zitterbewegung
interpretation is the same model, developed over thirty years, and Carter's
Kerr–Newman electron gets `g = 2` exactly at the same half-Compton radius.
Nothing here is new physics; the value is that one geometric premise reaches
spin, de Broglie, time dilation, and the equivalence principle at once.

The one possible contribution back to the main line: a closed null curve has
**zero proper length**, which suggests the timelike/spacelike two-tier split of
`foundations/0006` may want a **null middle term**.

## On Bell

Treated as a strong checkpoint, not a settled wall (`testability/exploration/0004`).
Bell rules out theories that keep all four of {local causality, measurement
independence, outcome independence, realism}; the consistency-first theory
gives up realism and outcome independence in the minimal way compatible with
experiment. Escape routes Bell does not close (superdeterminism,
retrocausality) are named openly; retrocausality is naturally compatible with
the fixed-point / time-symmetric reading of consistency-first and deserves its
own workstream.

## Workstreams

| Folder | Question | State |
|---|---|---|
| `foundations/` | Postulates and formal objects. | P1–P5 reframed around consistency-first (`exploration/0003`). |
| `mechanism/` | What *is* a measurement, mechanically? | Coincidence / split-merge + EPR refinement + a dilution law from monogamy (`exploration/0002`). |
| `testability/` | What confirms or breaks it? | The Bell fork reframed (`exploration/0003`); non-classicality now a derivation; quantum-selection open. Numerical demonstration in `output/0002`. |
| `trapped_momentum/` | Is a particle a closed null ray? | Spin, both de Broglie relations, and time dilation drop out exactly; blocked on a factor of 2 (`exploration/0001`). |

Each folder has a `SUMMARY.md` (current state), `exploration/` (numbered notes,
later = more recent), and where applicable `output/` (checkable artifacts).

## Honesty note

- **Contributed here (with real confidence):** the two-tier resolution of the
  c-vs-instantaneous puzzle; consistency-first packaging that turns "no
  god's-eye view" into the sheaf-theoretic non-extendability condition and
  *derives* non-classicality from the posit; the dilution reading of
  decoherence; the EPR refinement of the split/merge mechanism.
- **Proposed, not shown:** that P4 or MRE-projection tightens the bound to
  Tsirelson (would upgrade the theory from re-framing to partial derivation).
  Do not cite as fact.
- **Inherited (explicitly named):** the relational stance (RQM), epistemic
  reading (QBism, Spekkens), QRF formalism, decoherence, Fine's theorem,
  Abramsky–Brandenburger sheaves, information causality. Each labelled in
  `foundations/exploration/0002`.
