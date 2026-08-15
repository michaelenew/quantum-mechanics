# 0030 — The 3+1 build: the template executed, and where it stops

The prototype declared complete (0029), the instruction was to
proceed through 3+1 until complete or obstructed on all major
fronts. Result: **four fronts built and verified — the action, the
gravity sector, the causal cone, the quantum algebra — and one
front obstructed with the missing piece named precisely.** Code:
`output/0025_the_three_plus_one_build.py`.

---

## 1. The 3+1 action — built, lattice-exact

Discrete BF with a **2-form budget** on a 3D lattice:
S = Σ_plaquettes B_p(curl θ − src_p), strings sourcing the
plaquettes they pierce. Every check to machine zero:

- **First EOM** (vary B): curl θ = string flux — flat off strings.
- **Second EOM** (vary θ): (dB)_edge = 0 — **the budget is a closed
  2-form**. The conservation law again arrives as the action's
  other half, one degree up.
- **Dual closure**: the signed source flux through any closed box
  vanishes (computed from the lattice's own curls) — **strings
  cannot end**: the 3+1 form of atom conservation, now a geometric
  identity of dB rather than a postulate.
- **The loop charge**: a Wilson loop reads exactly the total string
  flux **linking** it (Stokes, exact); the jump law and gauge
  invariance are exact.

Charges on loops, budget on surfaces, conservation from closedness
— the template's kinematics, standing.

## 2. The gravity sector — lifts transversally, with a new law

A straight string's channel field is purely transverse, so its 3D
metric block-decomposes as (2D cone) × ℝ *exactly* (field-level).
Every 2+1 result — the exact atom (verified by transverse
transport: 0.7724 vs 0.7725), K = πs/det g, screening, retardation,
the compass and its Lorentz cure — applies in the transverse plane
of each string.

And the third dimension adds genuinely new physics, in closed form:
**string–string screening depends on relative inclination**:

```
f(α) = 1/√(1 + w cos²α)
```

verified against the constant-ambient integral at α = 0, π/4, π/2:
parallel strings screen maximally (0.8164), **orthogonal strings
are mutually transparent** (0.9999). Orientation enters the
coupling exactly through the transverse projection — the
distribution (shape) sector of the conjugate square doing its job.

## 3. The causal cone — dimension-blind

The 0022 theorem ports without modification: on a 3D random web the
one-event front equals the graph ball *exactly* (BFS set-equality
at two horizons), the front is round (octant anisotropy 1.23 at
average degree 14), and c is the web's own front speed. Locality
gives the cone in any dimension; isotropy is still statistical
isotropy of connectivity.

## 4. The quantum algebra — linking, as demanded

Per-edge Weyl pairs (matrix-exact) imply the operator law
W(γ)·X(S) = ω^(signed crossings)·X(S)·W(γ) for any Wilson loop γ
and dual-surface operator X(S) — and the signed crossing count *is*
the linking number, verified on explicit configurations:

```
linked rectangle          +1
disjoint rectangle         0
enters-and-exits           0   (2 crossings, net zero — correctly unlinked)
two linked loops           2
```

The 3+1 quantum deformation is **linking**, exactly as 0027's
template predicted. Its representation theory is the movie/census
formalism the knot thread built: the tetrahedron census enumerates
consistent string events, and the wall theorem (0018) acts as a
selection rule — abelian weights coexist with branch points;
nonabelian string statistics requires branch-point-free
presentations or richer coefficients. The two workstreams are now
one construction, not just one claim.

(Lorentz kinematics is dimension-generic: 0026's slice-map
factorization — boost × Wigner rotation — is the same polar
decomposition one row larger, inherited rather than re-proven.)

## 5. The obstruction — named, with its candidate key

What the direct lift does **not** give, stated as sharply as the
build allows:

**4D BF is topological — zero local degrees of freedom — and the
web's channels are slaved (|u| = 1: no independent radiative
modes, measured in 0023). In 2+1 that was the *correct* physics:
2+1 gravity has no gravitons. In 3+1 it is the gap: Einstein
gravity has two propagating polarizations.** The web as lifted is a
consistent quantum theory of *topological* 3+1 gravity — strings,
linking charges, conservation, causal cone, Lorentz kinematics —
but it is not yet Einstein gravity.

The bridge is known on the GR side: 4D BF becomes general
relativity under the **Plebanski simplicity constraint** (B = e∧e),
which breaks topological invariance and releases the gravitons. The
web-native candidate for what enforces it: **the Fisher dressing.**
In 2+1 the dressing was inert decoration (the 1/det screening and
the S² quadrupole halo, fully catalogued and carrying no dynamics).
The structure of the 3+1 problem says the dressing cannot stay
inert — the metric's non-topological content is exactly what must
become load-bearing for local curvature dynamics to exist. That is
a precise, falsifiable program: derive a simplicity-type constraint
from the Fisher structure of 3D channel webs, and check whether the
released modes are the web's two graviton polarizations.

Second obstruction: braided (nonabelian) string matter is walled by
0018 except on branch-point-free presentations. Third: matter is
still scripted — no variational worldsheet term.

## The state of the program

| front | 3+1 status |
|---|---|
| action, charges, conservation | **built** (lattice-exact) |
| string conservation | **built** (dB geometric identity) |
| transverse gravity + inclination law | **built** (+ new closed form) |
| causal cone | **built** (dimension-blind) |
| linking quantum algebra | **built** (census = its rep theory) |
| Lorentz kinematics | inherited (dimension-generic) |
| level tower / measurement rule | inherited (Hilbert-space arguments dimension-free) |
| **gravitons / Einstein dynamics** | **obstructed**: needs the simplicity constraint; candidate = the dressing made load-bearing |
| nonabelian string matter | obstructed by the wall theorem (escape routes known) |
| variational matter | open (worldsheet term unwritten) |

Per the stopping condition: the template is executed everywhere it
reaches, and the fronts that remain are obstructed with named
missing pieces, not open-ended. The frontier of the whole program
is now one question: **what, in a web of information channels,
plays Plebanski's simplicity constraint** — the condition that
turns topological bookkeeping into gravity that waves.

## Honest limits

- The lattice action is abelian BF with straight-string sources;
  knotted lattice strings and the nonabelian version are not
  constructed (the latter is where the census constraints bind).
- The linking-algebra verification is local relations + exact
  combinatorics on explicit configurations, not a general theorem
  proved here (it is standard, but our proof is by instance).
- The inclination law is derived for the transverse block of
  straight skew strings at the constant-ambient tier.
- The obstruction statement imports the Plebanski correspondence
  from the literature; the web-native derivation of the simplicity
  constraint is the open program, not a result.
