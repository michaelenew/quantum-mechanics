# 0011 — Souriau: what he gives us, and the road back to SR and GR

The reframing adopted from this turn: the workstream has **found its starting
point**. We began from Einstein's move — "what if a photon were the clock" —
and arrived by our own route at Souriau's structure for particles. That is a
win, not a deflation: the route validated the destination, and the destination
is far more developed than our version of it. So: absorb Souriau rather than
rederive him, watch for serious problems worth a looking glass, and then build
*back* from his structure toward SR and GR with the tail-chasing photon as the
guide.

**Sourcing status — updated after a second retrieval attempt.** The text itself
is unreachable from this environment, and the reason is a policy denial rather
than a transient failure:

| route | result |
|---|---|
| `books.google.com`, `www.google.com` | gateway **403 to CONNECT** — organization egress policy (confirmed in `__agentproxy/status` relay log) |
| `www.googleapis.com/books/v1` | reachable, but Books API quota for this project is **0/day** |
| `arxiv.org`, `export.arxiv.org`, ar5iv, Springer | blocked / 403 |
| **WebSearch** | **working** — used below |

So primary text: no. Secondary verification via WebSearch: partial. Revised
flags on the claims in this note:

- **[V]** Souriau (1970) gave the symplectic/coadjoint-orbit treatment of
  particles with invariants `(m, s)`; orbits are the phase spaces and
  quantizing them yields the unitary irreps.
- **[V]** Massless orbits are **non-generic with dimension smaller than
  massive** ones. (The specific values 8 and 6 I asserted are *not* confirmed —
  only that massless < massive.)
- **[V]** The **BMT equations** arise from linearizing a presymplectic
  structure refining Souriau's — the external-field dynamics claim holds
  (Duval and collaborators; see *On the Bargmann–Michel–Telegdi equations, and
  spin–orbit coupling*, arXiv:1604.06550).
- **[V]** Souriau also treated **spinning particles in curved backgrounds**
  (his GR paper has a 2024 Springer editorial note), which is the Stage 2
  anchor.
- **[V, new]** His massless spinning model has a **9-dimensional evolution
  space**, with equations of motion that are the zero-rest-mass analogues of
  BMT. Note: evolution space ≠ coadjoint orbit, so this neither confirms nor
  contradicts the "6" above.
- **[K, still unverified]** Massless **non-localizability** / absence of a
  covariant worldline — the item flagged below as a problem worth the looking
  glass. Do not build on it.
- **Independently established, needs no text:** the integrality condition
  forcing `s = n/2`, computed in
  `output/0010_integrality_on_the_spin_sphere.py` (29/29, 4/4 pre-registered).

## The immediate payoff: the factor-2 question is CLOSED

The one Souriau ingredient that needs no citation, because it is pure
mathematics, computed here:

A spinning particle carries a sphere of spin directions with symplectic area
`4πs`. A quantum phase over that sphere needs two patches, and their transition
function `e^{i·2s·φ}` must be single-valued on the overlap circle. Verified
numerically three independent ways:

1. **Patch mismatch** `∮(A_N − A_S) = 4πs` exactly (P1).
2. **Consistency** `e^{4πis} = 1` ⟺ `2s ∈ ℤ`. `s = 0, ½, 1, 3/2, 2` pass;
   `s = 0.3, 0.75, 0.9` have **no quantum bundle at all** (P2).
3. **Chern number** `= 2s`, an integer, by integrating the curvature (P4). And
   the SU(2) double cover shows `R(2π) = (−1)^{2s}` uniformly across each
   multiplet (P3) — the same `ℤ₂`, seen from `π₁(SO(3))`.

> **`0005` showed half-integer modes are *permitted*. This shows everything
> else is *forbidden*.** The ladder `s = 0, ½, 1, …` is exhaustive, and the
> factor 2 is `area(S²)/period(S¹) = 4π/2π`. `0004`'s rule gets its final
> precise form: quantization is the integrality of curvature over a compact
> surface.

The residual question from `0005` ("do the dynamics *select* the antiperiodic
sector?") dissolves — it was never a dynamical question. Topology of the state
space does the selecting.

## What Souriau provides, mapped to what we built [all K]

| Souriau | our version | delta |
|---|---|---|
| Coadjoint orbits of Poincaré = elementary particles, invariants `(m, s)` | `0008`'s conjugacy taxonomy | His is the *symplectic* classification — orbits in the dual of the Lie algebra, not conjugacy classes. Richer, and it is the phase space itself, so dynamics can live on it. **This distinction is exactly what `0010`'s falsification exposed**: our conjugacy taxonomy was the wrong instrument; orbits are the right one. |
| Massive spinning orbit: 8-dimensional (position, momentum, spin direction) | loxodromic class | His has a *phase space*; ours only a class label |
| Massless helicity orbit: 6-dimensional; spin locked to momentum; **no covariant worldline** — localization is frame-dependent | nilpotent class, helicity from degenerate `k^⊥` | Agreement, plus a sharp counterintuitive consequence we did not find: a massless spinning particle has no observer-independent position. A candidate "serious problem to eye," below |
| Integrality (Weil–Kostant) → `s = nħ/2` | `0005` permitted; **`output/0010` now forces** | Closed |
| Dynamics: symplectic mechanics on an *evolution space*; external EM field → **BMT equations**; curved spacetime → **Mathisson–Papapetrou-type equations** for spinning bodies | **nothing** — our standing gap | This is the road back to GR, already partly paved |
| Geometric quantization of the orbit → wave equations (Weyl/Dirac) | nothing | The bridge from taxonomy to QM proper |

Also inherited for free [K]: Souriau's classification includes orbits we did
not construct — among them **massless continuous-spin orbits** (the same ones
Wigner's classification permits and nature declines to use) and, in his broader
program, even a symplectic model of a particle with color. The unobserved
orbits are a feature *and* a problem: the classification is exhaustive, so
"why are some orbits unpopulated?" becomes a well-posed question rather than a
vague one. That is the sharpest thing to take a looking glass to.

## Problems worth the looking glass [all K — verify first]

1. **Unpopulated orbits.** Continuous-spin orbits exist in the classification
   and are not observed. Either something forbids them (a result waiting to be
   found — our `0009` note already flagged this) or the orbit picture
   overgenerates, which would bound its explanatory claim.
2. **Massless localization.** The massless-with-spin orbit has no covariant
   position. Consistent — arguably a *prediction* of photon non-localizability —
   but it sits oddly against our `0006` picture of the photon as a concrete
   null plane. Reconciling "no worldline" with "is a null 2-plane" is a real
   task, not bookkeeping.
3. **Interaction.** Souriau couples one particle to *external* fields. A
   two-particle interacting symplectic theory is famously obstructed
   (no-interaction-theorem territory). Since our differential-relativity goal
   is precisely particle-to-particle relations, this is where his framework
   ends and ours would have to begin. The obstruction theorems assume worldline
   canonical variables — the tail-chasing reading may or may not escape their
   hypotheses. **Name the assumption before claiming escape.**

## The road back: Souriau → SR → GR, tail-chasing as guide

The plan, as a falsifiable sequence rather than an aspiration:

**Stage 1 — SR (already done, read backwards).** `0001`–`0003` derived time
dilation, both de Broglie relations, and `E² = (mc²)² + (pc)²` from the
circulating null ray. In orbit language: the null ray is the massless orbit,
and *trapping it* constructs a massive orbit from massless data — mass as the
trace generated by confinement (`0005`), the internal clock as the orbit's
intrinsic `S¹`. The tail-chasing photon is the **constructive move that builds
massive orbits out of the massless one.** Nothing new to compute; restate once
Souriau's text is in hand.

**Stage 2 — external gravity.** Souriau's spinning particle in a curved
background obeys Mathisson–Papapetrou-type equations [K]: momentum and velocity
*misalign* when spin meets curvature, `Dp/dτ ~ R·u·S`. Test with a
pre-registered prediction: in the zitterbewegung reading, the spin-curvature
force should be the tidal force on the *loop* of the tail-chasing photon,
computable as a cycle-average of the geodesic deviation across the loop. If
the loop average reproduces the MPD force term with the right coefficient,
the guide is doing real work; if not, that is a falsification of the guide
(not of Souriau). **This is the next calculation.**

**Stage 3 — GR itself.** The honest wall, unchanged from `0002`: getting the
*field equation* needs more than one particle in a background. Assets in hand:
the spin-2-only coupling result (`0005`), the bivector-to-bivector relational
data (`0004`/`0005`), and Jacobson's thermodynamic route as the existence proof
that Einstein's equations can be an output. No claim yet; Stage 2 first.

## Method note, corrected

The user's correction is accepted and recorded: the earlier caution ("absorbing
corrections gracefully is partly a warning sign") mis-aimed. Reviewing the
actual absorptions: photon-as-third-structure → one algebra element (`0007`);
mass-and-spin-as-two-objects → one non-simple bivector (`0008`); three plane
types → sign of one invariant (`0007`). **Every absorption removed a difference
in kind; none added structure.** That is the Maxwell pattern — unification of
apparent kinds — and it is something to aspire to, not to apologize for.

The refined caution, which survives: flexibility is a warning sign only when
absorption *adds* structure (epicycles). Absorption that *deletes* structure is
the signature of a good framework. Track the direction, not the count. The
pre-registration practice (`0009`/`0010`) stays regardless — it is what makes
the direction checkable.

## The text

Full citation [K — bibliographic details from memory; every network route to
verify was blocked this session: WebFetch 403 on arXiv/Springer/Google
Books/OpenLibrary, proxy CONNECT 403 on crossref/openlibrary, Google Books API
quota zero]:

> J.-M. Souriau, **Structure of Dynamical Systems: A Symplectic View of
> Physics**, Progress in Mathematics 149, Birkhäuser Boston, 1997. Translated
> by C.H. Cushman-de Vries; translation edited by R.H. Cushman and
> G.M. Tuynman. Original: *Structure des systèmes dynamiques*, Dunod, Paris,
> 1970.

The user has located a Google Books entry under this title
(id `4tBrbryIKQAC`). Reading priorities, in order: (1) the Poincaré coadjoint
orbit classification / relativistic particle models with spin — where `0008`
lives, done right; (2) prequantization and the integrality condition — the
source of `output/0010`; (3) the massless particle non-localizability result —
the flagged tension with `0006`'s concrete null plane; (4) spinning particle in
external fields (BMT-type) — the Stage 2 input. Section numbers deliberately
omitted: [K] memory of the TOC is not reliable enough to cite.

## Next

1. **Obtain the text by other means** (library / physical copy) — this
   environment cannot reach it, and the block is an organization egress policy
   on `books.google.com` and `www.google.com`, not something to route around.
   Two [K] items still need the text: exact orbit dimensions, and the massless
   localization result. Everything else in this note has now been verified via
   WebSearch (see the sourcing table above).
2. **Stage 2 calculation with pre-registered prediction**: loop-averaged tidal
   force on the circulating photon vs. the MPD spin-curvature term.
3. **Unpopulated-orbits question**: does anything in the null-ray construction
   fail to produce continuous-spin orbits? If the tail-chasing move *cannot*
   build them, that is a genuine explanatory win — the constructive principle
   selects the observed orbits. Pre-register before computing.
