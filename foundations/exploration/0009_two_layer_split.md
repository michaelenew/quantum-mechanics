# 0009 — The two-layer split: two lossless layers, one lossy interplay

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Crystallizes the riff: physical reality as a **core** of losslessly composable
frame transforms (layer 1), an **overlay** of path-dependent informational
structure (layer 2), and all irreversibility — and, working hypothesis, all
*entropy-producing* curvature — living in their **interplay**. This note pins
each piece to a mathematical home and reports one worked computation.

## The posit, as clarified

- **Layer 1 (core).** Frame transforms compose as a groupoid:
  `T_ab · T_bc = T_ac`, conjugate transforms cancel to the identity
  (`T_ab · T_ba = 1`). Lossless, *locally* composable: a statement about
  `a→c` needs only `a→b` and `b→c`.
- **Layer 2 (overlay).** Path-dependent. Consistency is only **global**: the
  effective `a→c` object is the *sum over every intermediate* `X` of
  `a→X→c`, and the constraint is conjugate symmetry
  `∫_X (a→X→c) = [∫_X (c→X→a)]*`. Internally lossless, but not locally
  composable.
- **Interplay.** The only lossy term. Working hypothesis **W1**: the
  entropy-producing, loop-biasing curvature lives here, not in either layer.
- **Ladder principle (self-frames).** A particle's own frame is not a point
  but the family of frames in which it is **maximally coherent** — layer 2
  empty, only the irreducible uncertainty-saturating distribution left. No
  layer-1 transform reaches a frame where self-knowledge beats the
  uncertainty limit; the uncertainty-limited distribution plays the role the
  classical point-particle used to play, one level up.

## Anchor theorem: the split is not a conjecture in the quantum case

**Stinespring dilation** (1955): every lossy quantum channel (CPTP map) is
exactly a *lossless* unitary on a larger system followed by discarding part
of it. So "lossy = lossless + lossless + interplay" is not a hope — it is a
theorem about quantum dynamics. The user's diagnosis has a precise referent:
standard open-system theory works at the level of the already-traced-out
Lindblad/CPTP description, i.e. it **carries the lossy composite as
primitive** and discards the dilation. The two-layer program is: *never
discard the dilation; do the accounting in the split form.*

## The layer-1 / layer-2 identification that surprised me

Write the quantum propagator as a path integral. Then:

- **Layer 1 = the stationary-phase skeleton.** Classical action along
  extremal paths (Hamilton–Jacobi / van Vleck). It composes *pointwise* —
  action along `a→b` plus action along `b→c` gives the action along the
  joined path; the groupoid law holds without any sum over intermediates.
  Geodesic/ray structure; lossless.
- **Layer 2 = the full path sum.** The composition law of the propagator is
  `K(a,c) = ∫_X K(a,X) K(X,c) dX` — **exactly** the "consistency only under
  the integral over every intermediate X" the posit demands. And hermiticity
  `K(a,c) = K(c,a)*` is exactly the conjugate-symmetry constraint. These
  were stated in the riff *before* noticing they are verbatim the
  Chapman–Kolmogorov law and hermiticity of the quantum kernel. That
  coincidence is evidence the split is carving at a real joint.
- **Interplay = what stationary phase discards**: interference between
  fluctuation contributions of distinct skeleton paths. In decoherence
  language this is the Gell-Mann–Hartle decoherence functional between
  coarse-grained histories.

## Worked computation: pure dephasing (`output/0003_two_layer_dephasing.py`)

Qubit S + one environment qubit E, `H = g Z_S Z_E`, `|+⟩_S|+⟩_E`. Computed,
not asserted:

| object | layer | behavior |
|---|---|---|
| joint norm / purity of `|Ψ(t)⟩` | 1 | exactly 1 at all t — lossless |
| pointer-basis branch weights | 2 | frozen at (½, ½) — lossless |
| Schmidt spectrum across S–E cut | interplay | the *only* moving entropy; equals spectrum of ρ_S; carries 100% of observed decoherence |
| recurrence at t = π/2 | interplay | purity returns to 1.000000000000 — the loss is **recoverable** |

Two lessons, one of them at my own expense:

1. An earlier draft of the script labeled the frozen branch weights "Schmidt
   weights." Wrong — the Schmidt spectrum is the spectrum of ρ_S and it
   oscillates. The corrected accounting is sharper: **the gap between the
   pointer weights (layer 2) and the Schmidt spectrum is precisely the
   interplay.** Conflating them is exactly the conflation the split exists
   to prevent, and it is easy to commit even while writing the demo of it.
2. With one environment mode, the interplay loss **recurs** — nothing is
   destroyed, only displaced. Irreversibility enters solely in the
   many-mode limit where the recurrence time diverges: the **dilution**
   mechanism of `mechanism/exploration/0002`. Entropy = interplay
   correlation that has spread past any accessible subset. The arrow of
   time is the direction of dilution.

## Self-frames = coherent states = pointer states

The ladder principle has an established landing spot: the states that
saturate the uncertainty limit and are dynamically stable are **coherent
states**, and Zurek's einselection results show the environment's preferred
(pointer) states in quantum Brownian motion are precisely (near-)coherent
states. So "the family of frames in which the particle is maximally coherent
to itself" = the coherent-state family = the einselected basis. The posit's
self-frame and decoherence theory's pointer basis appear to be the same
object reached from opposite directions. **Status: strong structural match,
not yet a derivation** — showing that layer-2-emptiness *implies*
einselection would be a real result.

## Curvature: the honest partition (W1 refined)

Two kinds of loop-bias, kept separate:

- **Layer-1 holonomy** — Berry/geometric phase. Real, measured, *reversible*,
  entropy-free. Lives in the core; does not threaten W1 because it biases
  loops without producing entropy.
- **Interplay curvature** — the loop-bias that *does* produce entropy:
  decoherence rates, contraction of the state-space metric under the traced
  dynamics. W1 says this — and only this — is the "gravitational" analog to
  chase in the web geometry (`0005`).

W1 is adopted as the working start (highest reward), with the explicit break
condition: if entropy production is ever demonstrated from layer-1 structure
alone, W1 falls.

## Why this might make something tractable (the engineering thread)

The split reproduces, and organizes, the semiclassical machinery: layer 1 is
cheap (ODEs along rays — Hamilton–Jacobi transport), layer 2 is structured
(Gaussian fluctuation determinants), and the hard physics is confined to the
interplay term (decoherence functional). The promise worth testing: **error
budgets that don't mix** — bound the interplay contribution once, and the
lossless layers carry no accumulating error by construction.

**Next concrete computation:** double slit with environmental coupling.
Layer 1 = two stationary paths; layer 2 = fluctuations about each; interplay
= the decoherence functional between the paths. Check that fringe visibility
factorizes as `V = |⟨E_1|E_2⟩|` (the overlap of environment states dragged
along each path) — the same object as `⟨η_0|η_1⟩` in `output/0003` — so the
buckyball story of `mechanism/0001` becomes a computed two-layer statement
rather than a narrative.

## Status

- Stinespring anchor: **theorem, cited** — the split exists in QM exactly.
- Path-integral identification (layer 2's global consistency = kernel
  composition + hermiticity): **exact match of form**; elevating it from
  match to derivation requires defining layer 2 independently and *deriving*
  the kernel rules. Open.
- Dephasing accounting + recurrence: **computed, passes** (`output/0003`).
- Self-frames = coherent/pointer states: **structural match**, derivation open.
- W1 (curvature in the interplay): **working hypothesis** with a stated break
  condition; Berry phase explicitly quarantined as reversible layer-1
  holonomy.
