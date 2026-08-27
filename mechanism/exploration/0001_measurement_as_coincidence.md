# 0001 — Measurement as coincidence (split / merge)

> **AI-generated, not peer-reviewed.** Prior art credited in [`ATTRIBUTION.md`](../../ATTRIBUTION.md) — results are re-derivations of
> established work unless explicitly marked otherwise.

The proposal's mechanical core: **measurement is the exact coincidence of two
particles**, and coincidence is the same event as a split or a merge. This note
makes that precise and corrects one detail in the original framing.

## The split/merge event in relative coordinates

Two one-dimensional particles. Change to center-of-mass and relative variables:

    Q = (q1 + q2)/2      P = p1 + p2        (center of mass / total)
    q = q1 - q2          p = (p1 - p2)/2    (relative)

Canonical structure (verified symbolically in `output/0001`):

    [Q, P] = i ħ      [q, p] = i ħ      [Q, p] = [q, P] = 0

The key fact: **`q` (relative position) and `P` (total momentum) commute**, so
they can be simultaneously sharp.

At a split (one system becomes two) or a merge (two become one) the participants
are at the *same place*, so the relative position is sharp: `q → 0`,
`Var(q) → 0`. Simultaneously, momentum conservation fixes the total momentum
`P`, which is sharp too. Because `q` and `P` commute, both being sharp is
allowed — this is exactly the **EPR state** (EPR 1935 used precisely `q1−q2` and
`p1+p2`).

## Correction to the original framing

The original idea said: at a split "they knew the position exactly, so they must
have known the momentum not at all." The precise statement is:

> A split/merge makes the **relative position `q`** and the **total momentum
> `P`** sharp (the latter by conservation). Complementarity then forces the
> conjugate pair — **CoM position `Q`** and **relative momentum `p`** — to be
> broad.

So it is not momentum *per se* that is unknown; it is the **relative** momentum.
The **total** momentum is sharp. This is a strict improvement, not a
reinterpretation: it is consistent with conservation laws and it is what is
actually produced in the lab. Spontaneous parametric down-conversion creates
photon pairs that are position-correlated and momentum-anti-correlated — sharp
`q` and sharp `P` — and Howell et al. (PRL 2004) used exactly these pairs to
demonstrate the EPR paradox, with the *relative* position–momentum product
driven below the single-particle Heisenberg bound (an EPR/Reid-criterion
signature). The mechanism therefore has direct, existing experimental support.

## Why a sensor sees a spike

When system *S* and detector *D* coincide (interact), the event sharpens
`q = q_S − q_D`. From *D*'s knowledge state, `S` is now localized relative to
*D* — a single position, a spike — regardless of how broad `ρ_{D→S}` was before.
No collapse of an absolute wavefunction is invoked; only the relative coordinate
of the pair that actually interacted is sharpened. This is the relational
content of "click."

## Why a buckyball arrives whole

The atoms of a bound molecule have, a priori, an extremely sharp *internal*
relative state `ρ_internal` (tight binding = small `Var(q_internal)`). The
environment can and does decohere the molecule's *center-of-mass* which-path
information — that is the loss of interference — but it never needs to
re-localize the already-sharp internal coordinates. So the molecule's parts are
overwhelmingly likely to be found together: the environment "loses track of"
`Q`, not of `q_internal`. (Matches matter-wave interferometry with large
molecules.)

## Recursive collapse = marginalization

Original observation, now precise. Suppose *A*'s knowledge of *C* is carried
through *B*: `ρ_{A→C}` is built from `ρ_{A→B}` and (what *A* takes to be)
`ρ_{B→C}`. If *A* then loses certainty about *B*, *A*'s picture of *C* is the
**marginal** over *B*:

    W_{A→C}(q_AC) = ∫ W_{A→B}(q_AB) · W_{B→C}(q_AC − q_AB) d q_AB

— a **convolution**. No extra "where is B?" uncertainty is injected beyond what
the two links already carry; the links' variances simply add
(`Var(q_AC)=Var(q_AB)+Var(q_BC)`, the P4 result). "Collapse of recursively
consistent knowledge into a measurement" = replacing a chain by its convolved
marginal. Checked in `output/0001` (part 2).

## Fusion when two knowledge states meet

When two states describe the *same* coordinate (e.g. *A*'s own view of *C* and
the view relayed through *B*), coincidence combines them. In the classical
Gaussian reading this is **Bayesian fusion**: precisions (inverse variances)
add, the fused mean is the precision-weighted average, and the result is sharper
than either input (`output/0001`, part 3). "If A thought C was over there and B
thought the other way, combine to the most coherent picture" = product of the
two Gaussians. In the quantum reading the analogue is the state-update
(Lüders) rule; whether these agree is the subject of the fork in `testability/`.

## Status

- Commuting-pair claim and the EPR refinement: **confident** (derived + checked;
  matches EPR/SPDC).
- Marginalization/convolution and Gaussian fusion: **confident** for the
  classical/Gaussian reading; the quantum-reading equivalence is open.
- "Only coincidences reduce uncertainty": consistent with P4/P5 but is a
  *postulated* dynamical statement, not yet derived.
