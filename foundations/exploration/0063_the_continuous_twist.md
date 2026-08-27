# 0063 — The continuous twist: the graviton counted

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0061/0062 named the move: lift the quantum sector from the finite
alphabet Z_N to a **continuous** twist group — continuity, not
non-commutativity, being the operative property. This is the first
exact step: the linearized continuous theory on the lattice, where
everything is rational linear algebra, and where the four standing
polarization opens (0054/1, 0055/3, 0056/2, 0057/1) close **at the
linearized level**: the count is **2**, and what the two modes carry
is **pure Weyl**. Code: `output/0057_the_continuous_twist.py` (2 s).

Gate check first: the finite tile's remaining opens (the symplectic
reframing, composite N) are refinements, not blockers, and the
falsification-carrying items — deriving t and N — live upstream of
both tiles. Nothing obstructs the lift.

---

## 1. The mode count

Central differences turn every derivative into the symbol
s_μ = sin k_μ, and the linearized vacuum equations become a 10×10
matrix E(s) over the rationals — so "how many things propagate" is a
rank computation, done in exact arithmetic at exact rational shell
points ((5,3,4,0), (13,3,4,12); off-shell (1,2,3,5), (1,1,1,1),
(2,1,0,0)):

| | ker E | gauge | physical |
|---|---|---|---|
| off shell (η·s² ≠ 0), n = 4 | **4** | 4 | 0 |
| **on shell (η·s² = 0), n = 4** | **6** | 4 | **2** |
| on shell, n = 3 | **3** | 3 | **0** |

Off the shell, every solution is pure gauge. On the shell, exactly
two more appear. In 2+1, none do — the dimensional trade (0043) at
the propagating level, with no sampling and no limits taken.

## 2. What the modes carry

**Gauge modes have Riemann ≡ 0 identically** — all components, any
s, exact. They carry no geometry, which is the cleanest possible
statement of why they don't count.

The two physical modes — the TT polarizations h₊, hₓ at
s = (5,3,4,0) — have, exactly over Q:

- linearized Einstein tensor **= 0** (they solve the equations),
- linearized **Ricci = 0** while **Riemann has 72 nonzero
  components** — their curvature is **pure Weyl**,
- and their curvature operator **commutes with the Lorentzian Hodge
  star** — the Einstein criterion of 0061 §2, satisfied by the
  graviton in physical signature.

> 0061's target — "produce a curvature operator whose Weyl block is
> nonzero" — is delivered by the graviton itself. The thing the
> finite sector could never carry is exactly what the continuous
> theory's two propagating modes are made of.

In n = 3 every on-shell solution has Riemann ≡ 0: nothing
propagates, exactly — 2+1's topological character re-derived in one
line of linear algebra.

## 3. The Lorentzian criterion, proven — 0061 open 3 closed

0061 proved [R, ⋆] = 0 ⟺ traceless Ricci = 0 in Euclidean signature
(⋆² = +1) over Z_N and left the Lorentzian version open. Here:
⋆² = **−1** verified, and over **Q** on the 20-dimensional Riemann
space the maps M ↦ [M, ⋆] and M ↦ traceless Ricci have **identical
kernels** (rank 9 = 9 = stacked 9), with the vacuum pair
([R, ⋆] = 0 ∧ s = 0) matching the full Ricci map (10 = 10 = 10).
Same proof shape as 0062's, new signature, real coefficients.

## 4. The lattice grounding

The symbol algebra is not an idealized continuum statement. Applying
the **literal central-difference stencil** to a discrete TT wave at a
real lattice momentum (ω = k_x = arcsin 3/5) on the lattice shell

```
sin²ω = Σᵢ sin²kᵢ
```

gives max|E| = **0.0 to machine precision** — and 1.1×10⁻¹ off the
shell. The discrete wave solves the discrete equations exactly. The
shell's small-k limit is ω = |k|: a **massless** graviton, this time
by construction rather than by tuning — the linearized theory has no
analogue of the Z_N arc's t → t_c adjustment. (Central differences
carry doublers at the zone edge; a known artifact, counted per
branch.)

## 5. The quantum tier

The linearized action is quadratic, so quantization is *exact*
(Gaussian): each of the two modes per momentum is a harmonic
oscillator. The equal-time zero-point variance on an Nt-site time
lattice sums to

```
⟨|h|²⟩ = 1/(2ω√(1 + ω²/4))  →  1/(2ω)
```

matched to 6 digits at ω = 0.1, 0.5, 1.0. **The graviton's zero-point
jitter** — the continuous heir of 0054's |⟨W⟩| < 1, now attached to
the Weyl modes themselves.

And the compact-U(1) plaquette with the heat-kernel weight
W(θ) = Σₙ e^(−n²/2β) e^(inθ) shows the shape of a continuous-alphabet
quantum theory: ⟨W⟩ = e^(−1/2β) exactly (verified to 9 digits at
β = 0.5, 1, 2) — a jitter tension **1/(2β), continuous in the
coupling**, where Z_N's was the arithmetic sequence f(N) — while the
dual variables in the character expansion are **integers**. The
alphabet is continuous; the labels are whole numbers. Discreteness
as output, not ingredient — the 0061-correction (b) point, now a
computation.

## Honest limits

- Everything here is the **linearized, free** theory. No
  interactions, no nonperturbative measure — the mode count "2" is
  the free count, and the interacting/nonperturbative count (the
  spin-2 question Hamber's program addresses by Monte Carlo, 0058)
  remains open.
- The U(1) heat-kernel weight is **chosen** (the standard Villain
  form), not derived from the ledger. The continuous analogue of the
  ledger weight gcd(F,N)/N is unknown — gcd has no smooth large-N
  limit, so whatever the ledger's continuum form is, it is not a
  naive limit. This is now the sharpest structural open of the
  continuous arc.
- Central-difference doublers are noted, not removed.
- The shell analysis is per-momentum (a symbol statement); the
  lattice grounding (§4) ties it to the real operator at one
  momentum, not globally.
- The zero-point statement quantizes each mode independently —
  legitimate for a free theory, silent about backreaction.

## Open

1. **The continuous ledger weight** — **answered at the abelian tier
   by 0064**: the Fourier dual of gcd(·,N) at divisibility-saturated
   N is exactly τ(n), the number-of-divisors function, and τ = 1∗1 is
   the Dirichlet square of the BF weight. The derived continuum
   ledger is arithmetic and heavy-tailed, not the heat kernel used
   here. Remaining: the nonabelian (representation-ring) version.
2. **First interaction**: expand ε e∧e∧F one order past quadratic —
   the cubic graviton vertex from the web's own functional; check it
   against GR's (the two-body bond, 0060, is its static face).
3. **The nonperturbative count**: whether to enter Monte Carlo
   territory (Hamber's) or find an exactly solvable continuous
   sector beyond the free one.
4. Standing: deriving t and N (the falsification targets); the
   correlation gap (0058); the bond's h² (0060); composite N and the
   symplectic reframing (0062).
