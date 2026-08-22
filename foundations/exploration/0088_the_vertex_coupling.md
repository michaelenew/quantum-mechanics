# 0088 — The vertex coupling: where the two ledgers meet

Ninth stone: 0087's open 1, run against the real 4D object — the
16-dimensional shared-frame vertex (0078). The question: does the
two-ledger split (source factor × record factor, exact on the free
and 2D tiers) survive at the vertex? **It fails, measurably, from
first order — and the failure is the physics.** Code:
`output/0079_the_vertex_coupling.py`.

---

## 1. The test, and the free-tier control

Factorization has an operational meaning in the vertex's own
variables: shift one plaquette's curvature by a fixed source δF and
ask whether the price response depends on the *other five* plaquettes
(the context). If source and record factor, the response is local.

Control first: under the **per-plaquette product weight** the
response is identical across arbitrary contexts to 1e−12 — exact
locality, the precondition of 0087's reading theorem, confirmed in
these variables.

## 2. At the vertex the split fails, by measurable nats

Same base plaquette, same source, three context types (common-tetrad,
unrelated simples, random packs), six seeds:

- the response to the *same* source ranges over contexts by
  **0.17–1.5 nats (mean spread 0.72)** per unit-norm source — even
  flipping sign (a source that costs +0.78 in a geometric context is
  *paid* −0.68 in another);
- central-difference linear response, converged in step size:
  coefficients **+1.113 / +0.061 / +0.543** across the three
  contexts. The coupling is present from **first order** — not a
  large-source artifact.

## 3. Orientation lensing

At a geometric vertex, rotating the inserted source's plane from its
own slot (e₀∧e₁) toward a foreign slot (e₀∧e₂) traces a smooth price
curve (2.172 → 1.695 nats over 90°): **the vertex charges the
source's orientation relative to the ambient frame.** The measure
reads not just how much source, but how it sits in the local
geometry.

## 4. What the failure means

Assembling the arc:

| tier | gluing | split | physics |
|---|---|---|---|
| abelian 2D (0086) | character product | **exact** (polar) | topological — nothing propagates |
| SU(2) 2D (0087) | character convolution | **exact** (per-rep) | still topological |
| 4D vertex (here) | shared-frame integral | **fails, O(1) nat, 1st order** | interaction |

> **The two-ledger separation is a free-tier theorem, and the vertex
> is precisely where it must break.** A theory in which sources were
> read identically through any record would be linear — signals
> superpose, geometry never reacts to geometry. The vertex's
> context-dependent reading is the measure-level seed of
> gravitational nonlinearity: *geometry reads geometry*, which is
> what "gravity gravitates" looks like from inside the ledger. The
> 2D tiers are distortion-free because 2D gravity is topological;
> the distortion arriving exactly at the 4D vertex is the right
> theory being itself.

Two downstream consequences now have a named mechanism:

1. **Decoherence as inter-ledger transfer** (0068/0085/0086): the
   free tiers keep the ledgers separate, so nothing could move
   entries between them; the vertex couples them. Collapse-as-
   discharge, if it happens anywhere, happens at vertices.
2. **The reading theorem's domain**: 0087's "record damps but never
   distorts" governs propagation *between* interactions —
   asymptotic channels — while readings *through* interacting
   regions pick up context. That is lensing's information-theoretic
   shape: attenuation stays honest, orientation gets charged.

## Honest limits

- The vertex here is 0078's Gaussian-regulated shared-frame integral
  (ε′ = 0.01), not a boundary-state 4-simplex; "context" means the
  other five plaquettes at one site.
- The source model is an algebra-valued shift F → F + δF (holonomy
  near identity), not a finite class insertion; the center/'t Hooft
  sector is invisible at this level by construction.
- Sample sizes are modest (6 seeds, 3 context types, one δF per
  trial); the *existence* of O(1)-nat first-order coupling is robust
  across all of them, the coefficients' distribution is not mapped.
- "Lensing" names a structural resonance, not a derived deflection
  angle; no propagator was computed here.

## Open

1. Quantify the coupling tensor: the linear coefficient as a
   function of (source slot, source plane, context tetrad) — the
   vertex's "susceptibility," which is the measure-level cousin of
   the cubic graviton vertex (0063 open).
2. The in-context tension spectrum (0078 open 2) — now sharpened:
   the (1,0) mode's context cost is one entry of this susceptibility.
3. The decoherence mechanism made concrete: a record-carrying
   channel through a vertex — does its modulus leak into phase?
   (First stone of the measurement thread proper.)
4. Standing queue: boundary-state vertex + propagator, even-N
   packaging, arithmetic-branch pass, matter.
