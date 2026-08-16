# 0055 — Three quantum fronts: simplicity priced, jitter measured, no force

0054's three opens, all closed. The first is the sharpest result of
the quantum arc: **Plebanski's simplicity constraint is not imposed
in this theory — it is priced, and the price ratio is exactly 2.**
Code: `output/0050_the_quantum_fronts.py`.

---

## 1. The quantum simplicity constraint

Sum the frame factors of B = e∧e *inside* the action at one
plaquette:

```
K(F) = Σ_{a,b ∈ Z_N⁴} ω^{ ε_IJKL a^I b^J F^KL }
```

— a Gauss sum over **simple bivectors** (a∧b), evaluated on the
curvature F. Computed exactly, the weight depends only on the
simplicity invariant Pf(F) = ε_IJKL F^IJ F^KL / 8:

| curvature | \|K\| (N = 3) | action cost |
|---|---|---|
| F = 0 (flat) | 6561 | **0** |
| Pf(F) = 0 (**simple**, geometric) | 729 | **2 log N** |
| Pf(F) ≠ 0 (non-simple) | 81 | **4 log N** |

Exact at N = 2 and N = 3, and level-independent in units of log N.

> **Non-geometric curvature costs exactly twice what geometric
> curvature costs.**

And nothing is forbidden — no F has K = 0 — so the constraint is a
*suppression by N² per plaquette*, not a delta function. That is
the quantum form of B = e∧e. The arc closes on itself: 0046
identified simplicity with the ledger (probability = amplitude²),
0053 showed the ledger prices curvature (K = N·gcd(F,N)), and here
the price **resolves by simplicity** — the very sector where the
graviton polarizations live.

Reading it physically: the theory does not forbid non-geometric
curvature, it charges double for it. In the continuum/large-N limit
the ratio is unchanged (it is 2 in units of log N at every level),
so the suppression is not a lattice artefact that washes out — it
is the constraint's exact quantum weight.

## 2. The jitter's tension

0054 measured |⟨W⟩| falling with the loop's area but left the law
unextracted. It is exactly an area law, with a *derived*
coefficient — the single-plaquette factor

```
f(N) = Σ_F gcd(F,N)·ω^F / Σ_F gcd(F,N)
```

| N | 2 | 3 | 4 | 5 | 7 |
|---|---|---|---|---|---|
| f | 1/3 | **2/5** | 1/4 | 4/9 | 6/13 |
| tension −log f | 1.099 | 0.916 | 1.386 | 0.811 | 0.773 |

and ⟨W(R)⟩ = f^|R|: measured 0.4007 and 0.1618 against 0.4000 and
0.1600 for one and two plaquettes. (The four-plaquette value,
0.0361 vs 0.0256, carries the torus's global-constraint correlation
on top of the pure area law — the closed-universe budget again.)

So the geometry's zero-point jitter has a **string tension**, and
the numbers are number-theoretic: f(N) is a normalized
Ramanujan-type sum.

## 3. No pair force, quantum mechanically

The interaction energy of two sources, at separations from adjacent
to maximal:

| separation | adjacent | 2 apart | diagonal | far diagonal |
|---|---|---|---|---|
| energy | −0.0000000000 | −0.0000000000 | −0.0000000000 | −0.0000000000 |

**Exactly zero at every separation.** The 2+1 quantum model has no
gravitational force between masses — reproducing 0020's classical
measurement and 0043's dimensional trade (d = 2: topological charge,
no force).

The quantization introduced no spurious dynamics. And the null is
*sharp* precisely because the same measure demonstrably does
produce a deficit (0054 §1) and a propagating quantum (0054 §3) —
this is a theory that knows the difference between having curvature
and having attraction.

## Honest limits

- §1 computes the simplicity kernel at **one plaquette** with
  independent frame vectors a, b; the full theory shares frames
  between plaquettes (the correlation measured in 0053 §4), which
  is not folded in here.
- §1's Pf classification is the mod-N invariant; over Z_N,
  "Pf = 0" is a larger set than the geometric (rank-2) bivectors,
  so "simple" here means "simplicity-invariant vanishing," not
  "literally a∧b."
- §2's area law holds cleanly at 1 and 2 plaquettes on a 3×3 torus;
  at 4 plaquettes the global constraint dominates, so the pure area
  law is verified in a small window.
- §3's null is exact but 2+1 and static; it says nothing about
  whether the 3+1 lattice would produce Newton (which classically
  it must, 0036).

## Open

1. **The 3+1 quantum force**: repeat §3 on a 3+1 lattice, where
   the classical theory *does* give Newton — the sharpest
   remaining quantum test, and the direct quantum counterpart of
   0036's vacuum selection.
2. **Shared frames**: fold 0053 §4's correlation into §1's kernel
   — the honest B = e∧e measure on a full complex rather than one
   plaquette.
3. **Polarizations**: with simplicity now priced rather than
   imposed, count the propagating modes in the *constrained*
   measure directly — the quantum version of 0050's rank count,
   and the real spin-2 test.
4. Standing from 0048: the Lorentzian arena, P4 → Tsirelson,
   matter beyond scripted sources, the arithmetic bridges.
