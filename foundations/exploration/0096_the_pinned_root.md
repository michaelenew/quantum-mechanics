# 0096 — The pinned root: the homomorphism's first row

New arc, per the program owner's redirect: Z_N has done its job (its
trust/content split is degenerate by our own polar and freeze
theorems — it was the right toy for ledger arithmetic and cannot be
the toy for the fusion tier); the escalation target is now a
**homomorphism to the lucid-filter family**, and the predicted minimal
dynamics-carrying object was *the filter's bias computation*. Their
repo was read directly this session (ode-filter workstream, 57
explorations; random-walk-filter, the "walking" parent). The
prediction was right — and the first row of the homomorphism is a
theorem both programs proved independently without knowing it. Code:
`output/0086_the_pinned_root.py`.

---

## 1. Their theorem, in their objects

The ODE filter (their 0040/0041): a climbing or declining bias in a
tracked series can live **only in a characteristic root pinned at
z = 1 exactly** (d = 1 the constant offset, d = 2 the linear climb).
A free maximum-likelihood fit *cannot hold* a root there — it lands at
1 ± ε, ε = O(1/n) — and since a root is an exponent, the additive
climb is rendered as **geometric growth or decay**, overshooting at
horizon worse than ignoring the drift entirely. The cure is
structural: write the polynomial as (z−1)^d × quotient and fit only
the quotient. Underneath is a symmetry: forecast equivariance under
y → y + c *is* Σα = 1; under y → y + rt it *is* the double root. And
their prequential ledger: **the right pin is free (+0.0003 nats), the
wrong pin is loud (−0.148), never subtle.**

Reproduced minimally here (s1): free AR(2) on walk-plus-drift lands
its root at |z| − 1 ≈ 0.005 and takes ~5× the h = 60 bias of the
pinned fit.

## 2. The physics mirror, exact

Read "root of the transfer polynomial" as "channel transfer
eigenvalue r_j" and the same theorem is this program's masslessness
structure (s2, all exact):

- **r₀ = 1 for *any* positive weight** — conservation of probability
  is the automatic pin: the physics' d = 1, held by construction
  always (their Σα = 1, our normalization).
- **Every nontrivial channel of a generic weight has r_j < 1
  strictly** — mass is generic. A free measure cannot hold a
  nontrivial unit root, exactly as a free fit cannot.
- A nearly-symmetric weight gives r = 1 − ε: the channel survives
  ~1/ε steps and dies — the root-is-an-exponent catastrophe in
  physics dress. This program *lived* this: 0056's graviton was
  massive off criticality (tuned ≈ pinned-by-hand ≈ free fit), and
  0063's continuum graviton is massless **by construction** — the
  arc's own free-vs-pinned dichotomy, resolved the same way theirs
  was.
- A weight supported on a single center element holds **|r_j| = 1
  for every j exactly** — topological ('t Hooft) channels are pinned
  roots: persistence at any distance, by symmetry, not by fit.

So the row:

| lucid filter | this program |
|---|---|
| root pinned at z = 1 by construction | gauge/budget-protected massless mode |
| free fit's 1 ± ε displacement | mass generation by imperfectly-held symmetry |
| d (how many pins) | number of exactly-protected modes (the budget deleted exactly one — 0086's global mode — their d = 1) |
| right pin free / wrong pin loud | true constraints cost nothing; false ones move Q̂ (couplings) by orders — "damage lands in Q̂ and long-horizon variance," their words, renormalization's |
| the u = e₁ commitment's casualty (a deterministic slope inexpressible at any d) | a frame commitment making a sector unexpressible — candidate cousin of the (1,0) story; flagged, not claimed |

## 3. Two more rows the reading surfaced

**The AR(1) assumption ↔ the heat-kernel family.** Their walking
filter's one irreducible assumption is the *shape of trust dynamics*:
the log-variances evolve as AR(1), λ_t = φλ_{t−1} + noise — a
one-parameter-family closure for how confidence moves. This program's
irreducible closure is the heat-kernel family: after one blocking the
whole measure is one scalar τ with a flow map (0092/0093, closure
measured at 1e−4). Both programs found that the minimal honest
assumption is *a closed one-parameter family for the confidence
field, plus its persistence map*. Their φ is the doppelgänger of our
flow's contraction; their "s_P = 0 is an absolute claim, not a small
one" (their 0039) rhymes with our "exactly massless vs slightly
massive" — zero as a structural assertion, never a fitted value.

**The prequential floor ↔ where to stop j.** Their order question —
what p? — is answered *from below*: prequential log-loss climbs to a
floor (p ≥ 3 on ODE data, p = 1 on walk data) and is **flat above
it**, and they explicitly refuse AIC/BIC because a complexity penalty
imports a free parameter into the question being asked (their version
of our no-knobs rule). Ported to the bridge: **the cutoff J should be
posed as a floor, not a matched value** — the Gauss-matching linear
system's *minimal-support solution* is the floor; countings with
extra zero rows above it change nothing (flatness above); nothing is
fitted. This reframes 0094's bridge: derive J_min by existence, expect
blindness above, and feed J_min to the hierarchy chain. The filter
already owns the epistemology; the physics supplies the equations.

## 4. The noodle, sharpened

The owner's hunch — "a pretty large integer at which to stop
counting" smells like the finite sporadic groups. The aimed version
of that instinct in *this* program's exact context: the finite
subgroups of SU(2) are classified (cyclic, binary dihedral, and three
exceptional: binary tetrahedral/octahedral/**icosahedral**, order
120), and the **McKay correspondence** ties each to an ADE Dynkin
diagram — the binary icosahedral group to E₈ — with the
correspondence running *through exactly our objects*: how the spin-j
representations decompose on the finite subgroup. A "large,
distinguished, finite stopping structure inside SU(2)" exists, it is
E₈-shaped, and the bridge's restriction demand (evaluate the counting
on a finite subgroup) is *literally a McKay-type question* — our
cyclic-subgroup restriction is the A-series case, and the noodle asks
about the exceptional series. Filed as a real open, not a vibe.

## Honest limits

- s1 is a minimal reproduction of their measured phenomenon, not a
  use of their shipped filter; their numbers (−6.6 to −13.2 bias,
  +0.052 nats) are theirs, cited from their SUMMARY read this
  session.
- The homomorphism is at the level of transfer/one-step structure
  (state-space semigroup ↔ chain transfer semigroup). The fusion
  tier — influence combining interacting distributions, the part the
  owner identified as the hard core — is *not yet* in the map; this
  row is the dynamics anchor it hangs from.
- The u = e₁ ↔ (1,0) row is a flagged resemblance, unverified.

## Open

1. **The fusion row**: their oracle-gap/IMM machinery vs the vertex's
   context coupling (0088) — the influence tier proper. The
   discriminator experiment (Kalman fusion's enslaved weights vs
   superposition's free weights) is the designed first probe.
2. **The floor computation**: run the bridge as minimal-support
   existence (J_min per admissible level), the prequential posture.
3. **The McKay question**: restrict the counting to the binary
   icosahedral subgroup instead of the cyclic one — does the E₈
   structure select a counting?
4. Their φ ↔ our flow-contraction: make the AR(1)/heat-kernel row
   quantitative (F2's regret-vs-c cross-check inherits this).
