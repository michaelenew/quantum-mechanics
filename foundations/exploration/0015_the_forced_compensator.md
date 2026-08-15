# 0015 — The forced compensator: densification buys the phase

0014's three opens, executed. The first two combine into the
strongest structural claim the web program has produced; the third
turns the tetrahedron census into a starting set for level-2
invariants. Code: `output/0010_the_transition_and_the_weight.py`.

---

## 1. No third channel preserves the flip

First, the deficit is **pure shape**: scale-invariant (verified by
transport on a 4× scaled configuration — 1.934 both ways), depending
only on the *directions* of the other channels. Then the sweep over
all two-direction environments (angle θ between the two other
channels, plus the coincident-channel case):

| environment | δ |
|---|---|
| one other channel | **π** (the flip) |
| same channel, doubled | 2.4619 |
| θ = π/2 (orthogonal channels) | 1.8403 (minimum) |
| θ = π (opposite) | 2.4619 |
| maximum over the whole sweep | 2.4619 < π |

**The π-flip belongs to the two-party web alone.** Every third
channel — at any angle, coincident or opposite — pulls δ strictly
below π. (Channel *multiplicity* matters, not just direction: a
doubled channel is not a single channel. "How hard you've been
measured" reshapes the cone.)

The consequence is the structural claim: the residual π − δ sits
strictly inside (0, π) for every web except the two endpoints. The
metric can carry the binary flip only at δ = π (the two-party web);
the decoration alone carries it only at δ = 0 (the infinite-density
limit). Everywhere between, **a binary carrier cannot hold the
flip — if round-trip trust is to remain binary, the compensator is
forced to be continuous**. The minimal continuous carrier is a U(1)
phase. This is the same shape as the arithmetic result that
amplitudes complete the paradox buy-back (formal-languages 0059 §5),
now arriving from pure information geometry: **densification forces
the amplitude tier as geometry's change-maker.**

## 2. The compensator and the ledger

The forced compensator φ(k) = π − δ(k):

```
k:      2       3       6       12      20
φ:    0.000   1.206   2.157   2.636   2.835   →  π
```

Sparse webs pay the flip out of geometry; dense webs pay it entirely
out of the phase; the exchange rate is the closed-form deficit.

And the web's curvature ledger closes, hard: unwrapped parallel
transport around a radius-3 loop enclosing the 3-ring gives 6.2644;
the atomic deficits sum to 5.8054 (independent transport check
5.8032) and the integrated halo curvature is 0.4579 — total 6.2634,
a closure gap of **0.0010 (0.016%)**. Gauss–Bonnet on the punctured
disk: **atoms + halo, and nothing else, carry the geometry.** With
§1, the full inventory of carriers is: conical atoms and tidal halo
in the metric, the binary flip in the decoration, and the U(1)
compensator bridging them with φ = π − δ.

## 3. Tetrahedral weights exist, orbit by orbit

For each of the 21 tetrahedron-solution orbits, the triple-point
weight system (θ: X³ → Z_p with equal total weight on the two sides
of the tetrahedron move, arguments taken at incoming triples) was
solved exactly at p = 2, 3, 5. Findings:

- **Every orbit admits nonconstant weights** (dimension ≥ 1 at every
  modulus) — including all 13 nonabelian orbits.
- Several orbits show p = 2 enhancements (dims 2–3 vs 1 at odd p) —
  a Z₂-preference echoing everything else in this thread.
- A witness on a nonabelian orbit (placement group order 12) is
  exhibited with its move identity verified on all 64 states.

The set-theoretic starting set for a CJKLS-style level-2 state sum
over census solutions is nonempty and now enumerated by orbit and
modulus.

## Honest limits

- §1's sweep covers two-direction environments at resolution π/20
  plus multiplicity-2; higher channel counts follow by the same
  monotone mechanism but are not exhaustively swept. "Forced U(1)"
  is conditional on the posit that round-trip trust is binary.
- §2's ledger is one configuration at one radius (but the closure is
  0.016%, far inside the numerical error budget).
- §3's weights satisfy the tetrahedron-move identity; building an
  actual surface invariant from them still requires the full movie
  formalism (births/deaths/saddles and their move set), not staged
  here.

## Open

1. **The exchange-rate law.** φ(k) = π − δ(k) is measured and
   closed-form per configuration; is there a universal statement —
   e.g., φ as the information the *other* channels hold about the
   loop's interior (a mutual-information reading of the
   compensator)? That would make the amplitude phase an information
   quantity outright.
2. **Binary-trust as a theorem.** §1 conditions on binary round-trip
   trust; the projection argument (over/under = causal order along
   the ray) suggests it is derivable, which would make the forced
   U(1) unconditional within the synthesis.
3. **The movie move set** for §3's weights: stage births/deaths/
   saddles over the census solutions and check which weights survive
   — the direct set-theoretic road to a surface state sum.
