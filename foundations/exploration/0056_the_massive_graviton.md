# 0056 — The graviton's mass, the price as a kernel, and the shared frame

0055's three opens. The first turns up the quantum arc's most
consequential structural fact — **the lattice graviton is massive
off criticality, so the long-range Newtonian limit is a critical
point** — and the second gives the simplicity price a one-line
geometric meaning that supersedes the Pfaffian bookkeeping. Code:
`output/0051_the_massive_graviton.py`.

---

## 1. The graviton is massive; Newton lives at a critical point

The curvature quantum carries the price V per quantum (0055:
V = 2 log N for geometric curvature) and hops with amplitude t (the
electric term). Its pair gap is Δ(t) = 2V − 4t, measured on a long
ring:

| t/t_c | 0.20 | 0.60 | 0.90 | **1.00** | 1.10 |
|---|---|---|---|---|---|
| gap (N = 3) | +3.52 | +1.76 | +0.44 | **+0.0005** | −0.44 |
| gap (N = 5) | +5.15 | +2.58 | +0.64 | **+0.0008** | −0.64 |

Three phases:

- **t < t_c — gapped**: a massive quantum, so the force it mediates
  is **Yukawa**, with range 1/Δ;
- **t = t_c — critical**: the gap closes, the quantum is massless,
  and the force becomes long-ranged;
- **t > t_c — condensed**: the flat vacuum is unstable to
  curvature-pair creation.

The critical coupling is exactly **t_c = V/2 = log N**.

This is the honest quantum status of 0036's classical Newton. The
classical chain gets 1/r because it already sits at the continuum
point; **the quantum model must be tuned there.** That is not a
defect — it is how a lattice theory acquires a continuum limit at
all, and it makes a sharp statement: *long-range gravity is a
critical phenomenon in this theory*, with the critical coupling set
by the level N.

It also sharpens 0055 §3's null. The 2+1 model showed exactly zero
force between masses; we now know the generic lattice force is
short-ranged for a different reason (a massive mediator), and the
2+1 zero is the stronger, exactly-topological statement.

## 2. The price counts what the curvature leaves alone

The simplicity kernel of 0055 factorizes exactly:

```
K(F) = N⁴ · |ker F|,     ker F = { b : ε_IJKL b^J F^KL = 0 }
```

— the null space of the curvature viewed as a map on frame vectors.
Measured at N = 3:

| curvature | \|ker F\| | K |
|---|---|---|
| flat | N⁴ (leaves everything alone) | N⁸ |
| simple, Pf = 0 | **N²** (acts in a plane, leaves 2) | N⁶ |
| non-simple | N⁰ (acts on everything) | N⁴ |

So 0055's 0 / 2 log N / 4 log N hierarchy is precisely the
**codimension of the kernel**, and "geometric" means **"acts in a
plane."** The Pfaffian was the symptom; the rank is the cause.

That is a more physical statement of Plebanski's constraint than the
invariant: a curvature that rotates one plane and leaves the
transverse plane alone is what a tetrad can produce, and the measure
charges by how much of the frame the curvature disturbs.

## 3. The shared frame correlates neighbours

Two plaquettes sharing a frame vector have joint weight

```
K₂(F₁, F₂) = N⁸ · | ker F₁ ∩ ker F₂ |
```

so their prices are **not independent**: measured mutual information
**0.0265 bits** between adjacent plaquette costs (independent
plaquettes would give exactly 0). Cheap-*together* means the two
curvature planes share an untouched direction — the lattice's
version of *"all the curvature 2-forms come from one tetrad."*
0053 §4 measured this correlation in the budgets; here it is
resolved into its geometric cause.

## Honest limits

- §1's gap uses the pair dispersion of 0054 (nearest-neighbour
  hopping, one spatial dimension for the relative coordinate). The
  linear form Δ = 2V − 4t and hence t_c = V/2 are exact for that
  model; a full 3+1 lattice would renormalize t_c, though the
  *existence* of a gapped/critical/condensed structure is generic.
- §1 identifies the massless point but does not demonstrate that
  the critical theory's long-range force is **1/r** with the right
  coefficient — that is the remaining step to quantum Newton.
- §2's kernel statement is exact over Z_N; "acts in a plane" is the
  rank-2 reading, which over a ring (N composite) has divisor
  subtleties not explored (the N = 4, 8 gcd structure of 0053).
- §3's mutual information is measured on a 60-configuration sample
  of a two-plaquette junction, not on a full complex.

## Open

1. **Quantum Newton**: at t_c, compute the static potential V(d)
   between two sources and test for 1/d. This is now the single
   sharpest open in the quantum arc — the critical point exists,
   and the question is what force lives there.
2. **The critical theory's polarizations**: at t_c, count the
   massless modes — the real spin-2 test, now with a specific
   coupling to sit at.
3. **Composite N**: the divisor structure of 0053 (N = 4, 8) inside
   the kernel picture of §2 — does the 2-adic grading survive as a
   kernel statement?
4. Standing from 0048: the Lorentzian arena, P4 → Tsirelson, matter
   beyond scripted sources, the arithmetic bridges.
