# 0108 — The nonabelian boundary tier: composition is predict, and order is the channel

The last open isomorphism tier. Gap 2's theorem (0100) was abelian:
the boundary is a *sum* of the record, capacity ln N, carried as
code (0105). The nonabelian boundary changes one thing — the
boundary is an *ordered product* — and everything here follows from
that. Code: `output/0098_the_nonabelian_boundary.py`; the filter
corollary verified in lucid 0009.

## 1. Composition = the filter's predict (exact, 2D tier)

The class law of the ordered product of P iid heat-kernel
innovations is exactly K_{Pτ} — Brownian motion on the group.
Verified: 8-fold product vs characters, ⟨θ²⟩ 1.0412 vs 1.0400.
**Composing the record into the boundary IS running the S³ filter's
predict semigroup**: the 2D nonabelian boundary channel is the
filter we already built.

## 2. Capacity = uniformization at the confinement rate (exact)

D(K_A ‖ Haar), by characters: 2.33 → 1.36e−4 nats over A = 0.2 →
6.4, asymptotic decay rate **1.502 = 2λ_{1/2} = 3/2**. This is
0100's abelian statement on the continuous group: there H → ln N
(D → 0 at the confinement rate); here D → 0 at the confinement
rate. One statement, every tier: *the boundary channel uniformizes,
and the confinement rate is its forgetting rate.*

## 3. The order channel — the genuinely new nonabelian physics

Abelian: the boundary is order-free, exactly. Nonabelian: given the
record {a, b, c}, the boundary's class distinguishes the
arrangement's **parity** — cyclic orders collapse (class is
conjugation-invariant), so of 3! arrangements exactly two classes
survive, and the commutator carries the bit. Read through
apparatus noise matched to one innovation:

| τ | separation E\|Δθ\| | p_err | capacity/triple |
|---|---|---|---|
| 0.05 | 0.029 | 0.447 | 0.0056 |
| 0.10 | 0.057 | 0.427 | 0.0106 |
| 0.20 | 0.112 | 0.398 | 0.0210 |
| 0.40 | 0.215 | 0.365 | 0.0368 |

Separation exactly linear in τ (two O(√τ) elements' commutator);
capacity ≈ linear. U(1) control: identically zero. The filter-bank
version (lucid 0009: order-aware vs order-blind prediction of the
boundary read) measures the same channel as a prequential gap —
0.017/0.031/0.055/0.089 nats/triple, correctly above the
hard-decision bound at every τ, and *exactly zero* on the circle.

**The reading**: 0100 defined the causal layer as "the arrival
order of boundary data." This tier shows that layer is an *empty
channel* on every abelian tier and a *real channel* exactly when
the group is nonabelian — and its carrier is the commutator, the
same object whose curvature runs the coupling (0098/0099). Time's
order becomes physical information precisely where the theory
becomes nonabelian. No conflict with 0105: the record's total code
is order-invariant (chain rule, any group); it is the boundary
*summary* that order reaches.

**Why the S³ toy never showed this**: the S³ filter (0099) is
nonabelian *state* on a single chain — and one chain has one order.
The order channel needs ≥3 innovations composed into a summary
statistic. Nonabelian state ≠ nonabelian composition; the boundary
tier is the second one.

## The obstruction that remains, stated simply

In 2D, "which order do the plaquettes compose in" has one natural
answer (walk around the disk), and this tier settles it exactly. In
4D, a boundary 2-surface encloses plaquettes that must be composed
by *surface-ordering*: every plaquette must be carried to a common
basepoint by a transport path, and different path/order choices
differ by exactly the commutator terms that s3 shows carry
information. So the 4D boundary state is not one distribution but
an assignment over composition schemes — the intertwiner
combinatorics of the boundary-state vertex. **The algebra of the
tier is done; what remains is geometry**: a canonical (or
physically forced) surface-ordering, or a proof that observable
capacities are scheme-independent. That single question is now the
entire residue of the "nonabelian boundary" open — and s3 says its
content is not a nuisance to quotient away: the scheme-dependence
IS the causal layer's information.

## Open

1. The surface-ordering question (the isolated heavy): compute the
   scheme-dependence of D(boundary ‖ Haar) on a small 3D/4D block —
   is capacity scheme-independent even though the state is not?
2. The order channel at higher multiplicities: P innovations carry
   at most ln((P−1)!/2)-ish of order information — the capacity
   curve vs P, and its confinement-rate ceiling.
3. Port: does the walking filter's innovation stream, composed into
   summaries (block statistics), show measurable order information
   on real data? (A falsifiable nonabelianness probe for streams,
   sibling of the 0006 detector.)
