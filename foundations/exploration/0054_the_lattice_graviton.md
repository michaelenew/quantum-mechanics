# 0054 — The lattice graviton, and gravity computed from the quantum model

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

The milestone: **a gravitational effect derived from the quantized
lattice and then computed in it.** The effect is the conical
deficit — the web's oldest object (0014's atom, 0027's quantized
spectrum) — obtained here as the expectation value of a Wilson loop
in the interacting quantum ground state, with a quantum correction
that has no classical counterpart. And the excitation that carries
gravity turns out to have a dispersion. Code:
`output/0049_the_lattice_graviton.py`.

---

## 0. The derivation

Integrate the link variables out of the level-N partition function.
The link → flux Jacobian is the gauge volume, uniform, so nothing
survives but the plaquette weights and the closure of the surface:

```
P({F_p}) ∝ Π_p W(F_p − n_p),      Σ_p F_p = 0 (mod N)
```

with n_p the inserted source (a quantized mass) and W the budget
weight of 0053: **W = δ_{F,0}** for the free BF measure,
**W = gcd(F,N)/N** for the ledger's squared measure B = e∧e.

Two things arrive for free. The constraint Σ F = 0 is the
**closed-universe budget** (0029's Σδ = 4π): on a closed web a mass
must be compensated. And a Wilson loop around a region R measures
ω^(Σ_{p∈R} F_p) — lattice Stokes, exact — so the loop *is* the
holonomy that 0033's charge reader measures classically.

## 1. The deficit, computed

Exact enumeration of all N^(P−1) flux configurations on a 3×3 torus
with a neutral pair of sources (+1, −1 on opposite corners), squared
measure:

| loop | \|⟨W⟩\| | phase |
|---|---|---|
| p0 (encloses the mass) | 0.4007 | **+2.09440** |
| p0 + p1 | 0.1618 | **+2.09440** |
| 2×2 block with mass | 0.0361 | **+2.09440** |
| p1 (encloses nothing) | 0.4007 | −0.00000 |
| 2×2 block, empty | 0.0361 | +0.00000 |

2π/3 = 2.09440. **The phase is exactly the classical deficit
2πn/N for every loop enclosing the mass — whatever its size or
shape — and exactly zero for every loop that does not.** The
conical defect of 0014/0027, recovered as a quantum expectation
value. Verified at N = 2, 3, 4, 5: the phase tracks 2π/N to machine
precision, and → 0 as N → ∞ — the classical continuum.

That is the chain's oldest object arriving from its newest end.
0014 measured δ(w) by parallel-transporting a frame around a Fisher
beacon; 0027 quantized it to 2πn/N by single-valuedness; here it is
the phase of a Wilson loop in an interacting quantum ground state,
and the three agree.

## 2. The quantum correction

Run the identical computation under the free BF measure:

| loop | free BF | squared (ledger) |
|---|---|---|
| p0 (encloses the mass) | **1.0000** | 0.4007 |
| p0 + p1 | **1.0000** | 0.1618 |
| 2×2 block with mass | **1.0000** | 0.0361 |

Same deficit phase in both. But under BF the magnitude is
**1.0000 exactly at every loop — the geometry is rigid**, with no
fluctuation whatsoever. Under the ledger's squared measure the
magnitude falls with the loop's **area**.

So the two theories agree on the topological content and differ on
whether geometry *jitters*. |⟨W⟩| < 1 is a purely quantum
observable with no classical counterpart: the zero-point
fluctuation of curvature. **The square is what makes geometry
fluctuate.**

## 3. The lattice graviton

In the flux basis, the plaquette price

```
V(F) = −log W(F) = log(N/gcd(F,N))
```

is the **on-site energy of a curvature quantum**, and the lattice
theory's electric term shifts a link — moving one quantum to a
neighbouring plaquette, i.e. **hopping**. Because Σ F = 0, quanta
exist only in **± pairs** (the budget again — a lone curvature
quantum is forbidden on a closed web, exactly as a lone mass is).

Diagonalizing the pair's centre-of-mass motion on a ring (N = 3,
L = 12, t = 1) — both ends hop, so the relative amplitude carries a
2cos(k/2) factor:

| k | 0.000 | 0.524 | 1.047 | 1.571 | 2.094 | 2.618 | 3.142 |
|---|---|---|---|---|---|---|---|
| E(k) | −1.666 | −1.535 | −1.149 | −0.535 | +0.265 | +1.197 | +2.197 |

**Bandwidth 3.86, maximum group velocity 1.91: a propagating
mode.** Under the free BF measure V = +∞, so no state of nonzero
curvature exists at any energy and the band is *empty*.

> The ledger's square is exactly what turns an infinitely costly
> frozen constraint into a finite-price, dispersing excitation.

0050 counted the release classically (0 → 2 degrees of freedom by
rank); 0053 found the mechanism in the measure (K(F) = N·gcd(F,N));
here it is a spectrum with a group velocity.

## Honest limits

- This is the **abelian Z_N truncation** — the sector where 0027's
  prototype lives. The excitation is the curvature quantum of that
  model, not a spin-2 graviton with two polarizations: the
  polarization content requires the nonabelian SO(3,1) links of
  0052, which are not quantized here.
- §3's hopping amplitude t is a free parameter (the electric
  coupling); the dispersion's *shape* (the 2cos(k/2) envelope) and
  the infinite-vs-finite contrast are the results, not the
  numerical bandwidth.
- The lattice is 3×3 and 2-dimensional; the deficit result is exact
  on it, but the classical continuum limit (deficit → 0 as N → ∞
  *and* lattice → continuum) is checked only in N.
- The curvature price V = log(N/gcd) is read off the measure of
  0053, whose own honest limits (uniform, independent frame factors
  per plaquette) carry over.

## Open

1. **Polarizations**: quantize the nonabelian links (0052) and ask
   whether the propagating sector carries the two TT polarizations
   the classical count (0050) predicts — the real spin-2 test.
2. **The area law's coefficient**: |⟨W⟩| falls with area; extract
   the coefficient and ask whether it is the ledger's log(N/gcd)
   per plaquette (a "string tension" of the geometry's jitter).
3. **Two masses**: with the machinery here, compute ⟨W⟩ for two
   sources and look for the *interaction* — the quantum ancestor of
   the bond (0040), whose classical form is tension = force.
4. Standing from 0048: the Lorentzian arena, P4 → Tsirelson, matter
   beyond scripted sources, the arithmetic bridges.
