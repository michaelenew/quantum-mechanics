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
✓, and **mass apparently continuous** ✓. **The split between "mass is
continuous" and "spin is quantized" falls out of the causal type of the winding
plane.** Apparent continuity need not mean genuine continuity: sweeping a plane
toward null gives orbit frequency `ω = √(1−a²)`, so the **level spacing
collapses to zero** while the spectrum stays discrete (`exploration/0005`).

The exchange calculation (`exploration/0005`, 48/48) then lands the gravity
claim. A winding plane is a bivector, and its unique symmetric rank-2 bilinear
`T^{μν} = F^{μα}F^ν_α − ¼η^{μν}F²` is **traceless for every plane type**.
Since scalar exchange contracts as `(tr T)(tr T′)`, **the scalar channel
vanishes identically** — scalar gravity is not disfavoured here, it is
unavailable, and spin-2 is the lowest available universal channel. This is the
same fact that makes Nordström gravity predict zero light bending. And the
trace is the mass: free null ray → traceless → massless; confined →
`∫T^μ_μ = Mc²` by the tensor virial theorem, so **mass is the trace that
trapping generates**.

The factor of 2 is largely resolved by the model's own premise: a null vector
is a **spinor squared**, so rotating 360° about it fixes the vector and negates
the spinor. The object on the loop is a spinor, antiperiodic modes are
admissible, and the lowest is `½` → `L = ħ/2`. Residual: that the dynamics
*select* that sector, rather than permit it, is not shown.

The photon then broke the naive formulation and improved it (`exploration/0006`):
at `v = c` the transverse component is zero, so `L = 0` — against a measured
helicity of `±1`. The fix was the unused third case. **A null plane carries no
timelike direction at all** (`w·w = −b² ≤ 0`), so it spins spatially with no
mass — and writing down `F = k ∧ x` *is* a photon field, with `|E| = |B|`,
`E ⊥ B`, and both invariants vanishing, in every frame. Helicity's two states
follow from `k` being orthogonal to **itself**: `k^⊥` is degenerate, and
quotienting the null direction leaves a 2D polarization plane carrying only
`SO(2)`. The missing longitudinal state is the direction quotiented away.

The fix is **one object, not three** (`exploration/0007`). In the split
quaternions (`i² = −1`, `j² = k² = +1`), every pure element satisfies

```
v² = −(b² − c² − d²)·1  ≡  −Q(v)·1
```

so the square of a pure element is a **scalar**, and the whole trichotomy is
the sign of `Q` on a single element. Since `i` is the rotational direction and
`j,k` are boost directions, a **nilpotent** (`Q = 0`) has nonzero rotational
component with zero invariant — **genuine spin, no mass**. That is the photon,
as a boundary case rather than a bolted-on third structure: **the nilpotents
are the light cone of the algebra.** It also absorbs `0004`'s `4×4` nilpotent
(symmetric square of this `2×2` one) and `0005`'s level spacing (mass `~ √Q` is
distance from the cone).

In 3+1 (`sl(2,ℂ)`) the identity survives but `det` is complex, adding a fourth
class — **loxodromic** — and that is where mass and spin coexist in one object
(`exploration/0008`). Writing `X = (ζ/2)(n̂·σ)` with `ζ = η − iθ` the complex
rapidity, `det X = −ζ²/4`, and:

- `det X` carries **both** bivector invariants — `Re ~ F·F`, `Im ~ F·F̃` — which
  gives `0005`'s homeless parity-odd invariant a home and exposes that `0004`
  classified by only one of them.
- A massive spinning particle is a **non-simple** bivector, whose *canonical*
  decomposition into two orthogonal planes (boost in `span{t,z}`, rotation in
  `span{x,y}`) makes the imposed `S^{μν}u_ν = 0` automatic.
- **Mass is having an axis**: `det X ≠ 0` → two eigendirections → a rest frame.
  `det X = 0` → they **collide** → massless. "Has a rest frame" and "is
  diagonalizable" are the same statement.
- The flow factors **compact × non-compact** — phase returns exactly every
  period while the modulus never does — so one object yields a **quantized spin
  and a continuous momentum**, needing no gluing.

Massive spin-0 is just `θ = 0` in that family. The particle taxonomy becomes
the conjugacy classification of one-parameter subgroups of `SL(2,ℂ)` with no
case-splitting. No *values* are claimed — that needs representations.

**Status, stated plainly** (`exploration/0009`, `0010`). This is a kinematic
taxonomy with no dynamics, and essentially every piece of its mathematics is
standard: Möbius conjugacy, the Riemann–Silberstein vector, Wigner's little
groups, Penrose's flagpole — and the organising claim is **Souriau's
coadjoint-orbit programme (1970)**, stated first and carried much further.

The first test with predictions recorded *before* computing
(`output/0009_thomas_precession.py`) confirmed three and **falsified one**. A
product of two boosts is **hyperbolic**, not loxodromic — the Wigner rotation
lives in the *polar* decomposition, not the *conjugacy class*. So:

> The **representation** (`SL(2,ℂ)`, Pauli algebra, spinors) earns its keep —
> Thomas precession is one visible term in one product, and `2π(γ−1)` is the
> holonomy of curvature-`−1` velocity space. The **classification** was the
> wrong instrument here and remains untested.

That distinction matters: the pedagogical payoff rests on the first, which is
decades-old standard material, while everything novel-sounding sits in the
second. Standing practice adopted: no framework result claimed without a
prediction recorded before the computation.

**Reframed as the starting point** (`exploration/0011`): from Einstein's "what
if a photon were the clock" the workstream arrived by its own route at
Souriau's structure — the route validated the destination. His *orbit*
classification is the right instrument where our *conjugacy* taxonomy failed
the Thomas test, and his framework supplies what we lack (phase spaces,
dynamics in external fields, quantization). The **factor-2 question is now
closed** (`output/0010`, 4/4 pre-registered): the spin sphere's symplectic area
is `4πs`, single-valuedness of the patch transition forces `2s ∈ ℤ`, so
`s = 0, ½, 1, …` is *exhaustive* — non-half-integer spin is forbidden by
topology, and the factor 2 is `area(S²)/period(S¹)`. Quantization, final form:
**integrality of curvature over a compact surface.** The road back: Souriau →
SR (done in reverse — tail-chasing *constructs* massive orbits from the
massless one) → external gravity → GR (the honest wall: interaction).

**Stage 2 came back clean** (`exploration/0012`, `output/0011`, 20/20, 5/5
pre-registered). The confined photon ring's loop-averaged force in a generic
random stationary metric is exactly Mathisson–Papapetrou, coefficient **−1/2**
to machine precision. The confinement is load-bearing: the photon alone
mis-weighs by its pressure term, and the hoop tension (`τ = E/2πr` — the
null-string condition) restores weight `E` and makes `T^{jk} ≡ 0` pointwise.
Universality both validates and silences the guide at this order — gravity
reads only `(E,S)` — and the two sub-claims falsified en route both failed on
the same object, the ring's mass quadrupole, thereby promoting it: at fixed
`(E,S)` trapped light has the *minimum* quadrupole `S²/2E` at radius
`r = S/E = ` Kerr's `a = J/M`.

**Stage 2b answered the registered question: factor 1/2, not 1**
(`exploration/0013`, `output/0012`, 21/21). The bare ring carries half of
Kerr's `M₂ = −J²/M`, and the other half is carried by the **confinement
stresses**: `M₂ = −½(Ea² + Y)` with `Y` the total stress second moment, so
Kerr ⟺ the confinement's own stress second moment vanishes. Computed ladder:
hoop 1/2, membrane 3/4, spokes 5/6 of Kerr. If minimal coupling = Kerr
multipoles [K], the electron sits at Kerr — so gravity hands the model a
concrete constraint on its oldest gap: whatever traps the circulating momentum
must be pre-stressed with zero stress second moment. Exact Kerr requires the
Israel disk (negative interior sheet + positive rim), re-derived from the
Appell branch cut. Stage 3 is thereby reframed: **the confinement is the
dynamical object.**

Stage 3's first piece is done (`exploration/0014`, `output/0013`, 11/11). The
registered "exterior must be Kerr" justification was withdrawn before
computing (no Birkhoff for rotation) and replaced by the correct mechanism:
material tension is the only negative-second-moment agent, so as self-gravity
supplies fraction `f` of the confinement, `M₂(f) = −(1+f)Ea²/2` — **a linear
march from half-Kerr to exactly Kerr at full self-confinement**, at leading
order. En route: the null ring's gravitational self-interaction is **finite
with no thickness cutoff** (parallel null neighbours don't interact — nullness
regularizes, where a static massive ring diverges logarithmically), the
linearized geon sits at `a* = (16/3π)GE ≈ 1.70 GE` (extremal-Kerr scale ×
order-unity), and **the electron is not a geon** — gravity supplies `~10⁻⁴⁴`
of its confinement, so the zero-stress-moment constraint must be met by
non-gravitational structure. Every GR probe so far has converted "what
confines the ray" into a quantitative constraint.

That line reaches a **theorem** (`exploration/0015`, `output/0014`, 17/17,
5/5 pre-registered). Reducing the stress second moment to the transmitted
radial force `u(ρ) = 2πρS^{ρρ}` collapses it to one quadrature
`Y_tot = −2∫uρ²dρ`, and all-tension confinement then forces

> **M₂ fraction ∈ [1/2, 5/6] — Kerr is outside the reachable set.**

The bound is tight at both ends (`u ∝ ρⁿ` gives `(1+2/(n+3))/2`, sweeping
spokes→hoop). Reaching Kerr needs 50% more internal tension than the load
transmitted, closable only by **hoop compression** — a pre-stressed
tensegrity, whose energy DEC bounds below by `~πE`, comparable to the ring
itself. So the `0013` ladder's 5/6 is a hard ceiling for *matter*, and
self-gravity reaches 1 precisely because it removes matter stress rather than
rearranging it: **Kerr's quadrupole is a signature of non-material
confinement.**

Link 1 was then **verified, and it broke the electron application**
(`exploration/0016`, `output/0015`, 9/9). Minimal coupling does generate Kerr's
full multipole series — *in the infinite-spin limit*. But a spin-`s` state
carries multipoles only to rank `2s`, and the spin-induced quadrupole operator
**vanishes identically as a matrix for `s = ½`**: the electron has no
quadrupole at all, so the inference drawn from it is withdrawn. The theorem
stands; only its application dies. Surviving: `g = 2` at dipole order — and a
correction to `0001`/`0013`, that the Kerr–electron coincidence is weaker
evidence than they treated it as, since spin-½ truncates the series.

What replaces it is the **positive** mechanism: covariantly, a photon on a
**closed null geodesic is unforced** — the "confining force" of flat
coordinates is the connection (not a boost effect; `∂_μT^{μν} = 0` is
covariant, so the content is curvature). Such confinement carries no matter
stress, so `Y_conf = 0` and `M₂ = −Ea²` is **exactly Kerr with no free
parameter**. A further claim — that self-consistency fixes the scale at extremal Kerr — was
**falsified by its own flagged redo** (`exploration/0017`, `output/0016`,
22/22). Stated invariantly, the size of a photon orbit is its impact parameter
`b = L/E`, and since `a = J/M = b` the condition is `a = b`; but
`b_ph − a = r^{3/2}/√M > 0` always, so no fixed point exists — and a ring on
the extremal orbit would generate `a = 2M`, super-extremal, where no photon
orbit exists at all. Binding energy widens the gap rather than closing it.
**`0014`'s strong-field endpoint is open again.** The geodesic-confinement
mechanism survives; only the claim that a self-generated geometry supplies the
orbit to its own source is dead. Self-confinement is **unresolved, not
refuted** — the mean-field treatment double-counts each photon's own field, and
the self-field-corrected version (finite, per `0014`) is untried.

This bridges to `foundations/`: a **consistency constraint carries no
stress-energy**, so it evades the bound exactly as geometry does — and "what
confines the ray?" may be a category error like "what force keeps a free
particle moving straight?"

Method rule adopted here: **name the assumption, cite the measurement.** It
earned its keep — a Casimir argument that looked like an obstruction was not
one, while measurements (Higgs spin, the absent mass ladder) did the real work.
A companion habit that also paid: `0005`'s first run had a metric applied twice
in the stress-tensor contraction, which inverted the headline result. The
self-checks caught it. Every claim above is post-fix.

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
