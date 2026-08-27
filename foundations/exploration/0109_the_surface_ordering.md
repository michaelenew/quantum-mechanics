# 0109 — The surface ordering: chosen by the Gauss law, and then it does not matter

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

The 4D residue of the nonabelian boundary (0108) — which composition
scheme a closed 2-surface uses — settled at the 3-cell tier, by the
strategy of working gravity backwards: the filter-space gravity
program (lucid 0010–0011) requires the boundary to read *exactly*
the enclosed content (else the trust field has fake sources), and
that requirement turns out to both select the lawful schemes and
prove the selection empty of further physical choice.
Code: `output/0099_the_surface_ordering.py`.

1. **A lawful scheme exists, constructively.** The cube's six
   coherently-oriented faces glue by word substitution (polygon
   gluing); the glued boundary word **freely reduces to the empty
   word** — a symbolic, configuration-independent proof that the
   transported (lassoed) composite of the six faces is exactly 1.
   The gluing algorithm *finds* the lattice Bianchi identity rather
   than recalling it, and logs the lasso transports as it goes.
   Numerically: |C − 1| = 1.8e−15 on random Haar configurations.
   The closed boundary of an empty region reads 1: the Gauss law.
2. **The scheme is gauge.** Two different gluings (different root
   face, different absorption order) both reduce to empty; with a
   source g inserted on a face, their composites are *conjugates*
   of g — elements differing by O(1), classes equal to 4.4e−16, and
   equal to class(g). Every class observable — including the
   boundary capacity of 0108 — is scheme-independent among lawful
   schemes. **The 4D "choice" is a gauge choice.**
3. **Unlawful schemes fake mass.** The transport-free product of
   the six faces reads a nonzero class on an *empty* cube — 0.16 to
   0.64 rad RMS as the link scale grows, at the commutator scale —
   exactly the fake enclosed sources the filter-gravity Gauss
   requirement forbids. The desired gravity outcome excludes them;
   among the lawful schemes, statement 2 says nothing physical
   remains to choose.

Reconciliation with 0108's order channel: no tension. The order
channel is information carried by the *record's own arrival order*
relative to a fixed lawful reading; the scheme-gauge statement says
the *reader's bookkeeping* drops out of every class observable. The
message is physical; the notation is not.

**What this closes**: the boundary-state-vertex heavy's geometric
half. The 2D tier was exact (0108); the 3-cell tier is now exact
(here); larger closed surfaces tile by cubes (each interior face
appears twice, inverse-conjugate, cancelling in the glued word — the
same substitution algorithm applies, stated not run). What remains
of the old heavy is dynamical, not geometric: the vertex's
*interacting* content — the TC insertions (0107) and the context
spectrum (0089) — on a boundary now known to be well-defined.

## Honest limits

- Proven at the single 3-cell; the tiling extension is an argument
  (the algorithm generalizes verbatim), not yet a run.
- "Chosen by the Gauss law" imports the filter-gravity requirement
  as a physical principle; within this program that principle is
  itself derived (trust field statics, lucid 0011), but the import
  should be remembered as the one place gravity entered the
  boundary question.

## Open

1. Run the tiling (2×1×1 and 2×2×2 blocks) through the same gluing
   algorithm — expected empty words, machine-precision composites.
2. The dynamical vertex on the now-well-defined boundary: TC
   insertions at the boundary state (0107's port).
3. The multiplicity scan of the order channel (0108's open 2) on
   lawful readings.
