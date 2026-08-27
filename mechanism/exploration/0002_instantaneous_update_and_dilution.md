# 0002 — Instantaneous update and the dilution law

> **AI-generated, not peer-reviewed.** Prior art credited in [`ATTRIBUTION.md`](../../ATTRIBUTION.md) — results are re-derivations of
> established work unless explicitly marked otherwise.

Two mechanical questions the corrected (nonlocal) posit raises:
1. When an edge is sharpened, *how far* does the update reach, and *how strong*
   is it on a distant particle?
2. Why does the nonlocal update look "small / random / very-hard-to-detect"
   rather than a dramatic distant lurch?

## The reach: the whole connected component

Sharpening one edge projects the web onto the consistency manifold
(`foundations/0003`), which moves every node in the same connected component of
the interaction graph — i.e. every particle that ever interacted, directly or
indirectly, with a participant. This matches the posit exactly. The reach is
*combinatorial* (graph connectivity), not metric (distance), which is why it is
independent of separation and instantaneous.

## The strength: a dilution law from monogamy

The magnitude of the update on a distant particle *X* is bounded by how
correlated *X* still is with the measured particle *A*. Correlation is a
conserved-ish, **shareable-but-monogamous** resource:

- Monogamy (e.g. Coffman–Kundu–Wootters for entanglement; subadditivity for
  mutual information) bounds the *total* pairwise correlation a particle can hold
  across all partners.
- A particle that has interacted with `N` others has, generically, spread its
  correlation across all of them. The residual pairwise correlation with any one
  old partner scales like `~ C_total / N` at most — often far less, because
  correlation localizes onto the most-recent / most-strongly-coupled partner.

So the instantaneous update on a randomly chosen distant particle is bounded by
its residual per-partner correlation, which for a well-connected ("thermalized")
particle is astronomically small. **That is the quantitative skeleton of "small
and hard to detect."**

*Testable-ish shape:* update strength on `X` ≲ (mutual information `I(A:X)`),
which for a system that has since interacted with many others decays with the
number/strength of `A`'s intervening interactions. A concrete falsifiable
version would predict a specific decay of recoverable correlation vs.
interaction count — worth trying to derive from a monogamy inequality.

## Decoherence, re-read as dilution (not destruction)

Standard decoherence says interference is "lost to the environment." The posit's
nonlocal frame sharpens *why*: the correlation that carried the interference is
not destroyed — it is **diluted** across so many environmental partners that the
residual per-partner share drops below detectability. The information is still
there in the global web (consistency is exact); it is merely unrecoverable from
any local subset. This is compatible with the usual account but re-centers it:
collapse-appearance = dilution of correlation past the local detection floor.

This also explains the double slit cleanly in the posit's terms: the apparatus +
air + everything incidental provides an enormous set of partners for the
particle's which-path correlation to dilute into. It doesn't matter whether
anyone read it; the correlation left the two-slit subsystem, so the *local*
(subsystem) description loses its global section → no interference. "Could have
known" = "the correlation was already shared out."

## The "random" half of the firewall

Why does the huge, instant, nonlocal update never let us signal? Because the
sign/content of each distant edge-update is fixed by the measurement *outcome*,
which is random and unpre-selectable. Average over outcomes → every distant
marginal returns to its prior (law of total probability). So:

- **Instantaneous + nonlocal:** yes (globality of the constraint).
- **Usable to signal:** no (randomness averages the distant effect away).

The uncertainty principle is thus not an annoyance to be explained away; in this
frame it is the *guarantee* of the firewall — the exact amount of irreducible
randomness needed to make instantaneous consistency non-signalling.

## Status

- Reach = connected component: **confident** (direct from the constraint being
  global).
- Dilution law from monogamy: **plausible, partially rigorous.** The `~1/N`
  scaling is heuristic; deriving a sharp bound (update ≤ some monotone of
  `I(A:X)`) is an open, tractable target.
- Decoherence-as-dilution: **confident as a reframing**, consistent with the
  standard account.
