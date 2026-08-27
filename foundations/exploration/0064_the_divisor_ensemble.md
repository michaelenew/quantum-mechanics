# 0064 — The divisor ensemble: what the ledger measure actually is

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Pursuing the novelty thread. The quantum arc's weight gcd(F,N)/N has
been a number-theoretic black box since 0053 — its values measured,
its structure unexplained. A classical identity opens it, and what is
inside answers 0063's sharpest open — the continuum ledger — by
**derivation rather than choice**. Everything below is exact; the
suite runs in 0.24 s. Code: `output/0058_the_divisor_ensemble.py`.

---

## 1. The ledger is an ensemble of topological theories

Cesàro's identity (verified exactly for every F at every N ≤ 60):

```
gcd(F, N) = Σ_{d|N} φ(d) · [d | F]
```

Each [d|F] is a **flatness constraint at level d** — the
BF/Dijkgraaf–Witten weight of the level-d subtheory. So the
per-plaquette ledger weight is a φ-weighted mixture of topological
theories, and expanding the product over plaquettes, the partition
function is a sum over **divisor fields** {d_p}:

> **The quantization level is a local, dynamical variable,**
> distributed by Euler's φ. The ledger does not have *a* level N — it
> has a level *field*, fluctuating plaquette by plaquette over the
> divisors of N.

On a closed 2-plaquette universe the budget F₁ + F₂ = 0 couples the
two levels through their **lcm**:

```
Z = Σ_{d₁,d₂|N} φ(d₁) φ(d₂) · N/lcm(d₁,d₂)
```

verified exactly against the direct gcd sum at N = 6 and 12. 0053
§4's mysterious inter-plaquette correlation — measured as mutual
information, traced by 0056 §3 to shared frames — is here an exact
formula: **neighbouring levels are correlated because the budget can
only be satisfied inside their common refinement.**

## 2. Closed forms for everything the arc measured

**The jitter base.** 0055 measured the single-plaquette factor
f(N) = 1/3, 2/5, 1/4, 4/9, 6/13 at N = 2, 3, 4, 5, 7 and called it "a
normalized Ramanujan-type sum." It is exactly

```
f(N) = φ(N) / P(N)        (P = Pillai's function, Σₖ gcd(k,N))
```

verified against every measured value and at N = 6, 8, 9, 12. The
tension is log(P(N)/φ(N)).

**What the jitter *is*.** f(N) = φ(N)/P(N) is precisely the
probability that the plaquette's local level is **maximal** (d = N).
So: classical rigid geometry is the maximal-level sector; **the
quantum jitter is the φ-probability of sub-maximal local levels**;
and the Wilson magnitude falls with area because each enclosed
plaquette independently risks being sub-maximal.

**Prime N.** The ensemble is two-level — full BF plus the free
theory — with weights → (½, ½): the prime-N continuum tension is
**log 2 exactly**. Half rigid geometry, half no geometry at all.

**Dyadic N = 2^k.** The level distribution is asymptotically
**uniform over the dyadic tower** (weight 1/(k+2) per level, exact).
0053's 2-adic grading was the divisor lattice all along, uniformly
populated — the composite-N open (0056/0062) resolved in structure.

## 3. The continuum ledger, derived

The Fourier dual of the ledger weight is

```
Ŵ_N(n) = Σ_{e | gcd(n,N)} e · φ(N/e)
```

and for divisibility-saturated N (N = lcm(1..K)²), **exactly, not
asymptotically**:

```
Ŵ(n)/Ŵ(1) = τ(n)     for all n ≤ K
```

— the **number-of-divisors function**. Verified at K = 6, 10, 14
(N up to ~10¹¹).

Two readings, both sharp:

- **τ = 1 ∗ 1** — the Dirichlet convolution of the flat (BF) weight
  with itself. The ledger's "probability = amplitude²," which 0046
  located in B = e∧e and 0055 in the squared measure, appears in the
  charge basis as **Dirichlet convolution: the continuum ledger is
  the Dirichlet square of the topological theory.** (Checked
  n ≤ 2000.)
- The derived continuum U(1) weight is **arithmetic and
  heavy-tailed** — emphatically not the heat kernel 0063 had to
  choose. 0063's open 1 ("the continuous ledger weight is unknown")
  is **answered at the abelian tier**: it is τ.

The zero mode Ŵ(0)/Ŵ(1) = P(N)/φ(N) diverges (68 → 453 → 4328 along
K = 6, 10, 14) — and this is exactly the mode the closed-universe
budget removes (0029; the k = 0 exclusion that *was* the Newtonian
Green function's regularization in 0057). The measure's one
divergence and the budget's one deletion are the same object.

## 4. First observable, and its delicacy

The closed 2-plaquette universe's Wilson expectation falls slowly
with N: 0.350 (N = 144) → 0.282 (3600) → 0.239 (705600). The τ
weights' heavy tail (Σ τ(n)² diverges logarithmically) makes the
strict continuum value delicate — the same zero-mode/budget care the
Green function needed. Recorded as a trend, not a limit.

## Honest limits

- Abelian tier only. The derivation lives in U(1)/Z_N; the SO(3,1)
  ledger weight — what τ becomes when charges are representations of
  a nonabelian group — is untouched, though the Dirichlet-square
  reading suggests the form: the convolution square of the trivial
  weight in the representation ring.
- §3's exactness is along the divisibility-saturated sequence; other
  N → ∞ routes (primes: two-level; general N) approach different
  local structures. The τ statement is the *saturated* limit — the
  natural one if all levels are to be available, but a choice of
  sequence nonetheless.
- §4's observable has no established limit; the divergence structure
  is diagnosed, not resolved.
- Novelty per 0058's method caveat: I did not find gcd-as-ensemble /
  τ-as-ledger in the physics literature, but the search was shallow;
  Cesàro's identity itself is 19th-century number theory, and
  τ-weighted charge sums appear in Eisenstein-series q-expansions —
  the arithmetic-bridge thread (0010, standing open 0048) may be
  knocking.

## Open

1. **The nonabelian Dirichlet square**: define the convolution square
   of the trivial weight on the representation ring of SU(2)/SL(2,C)
   — candidate for the full continuum ledger, and the bridge to the
   EPRL-shaped machinery 0058 mapped.
2. **The τ-theory's observables**: redo 0057's quantum Newton and
   0063's mode count under the *derived* weight — does the heavy
   tail change the critical structure? (The heat-kernel comparison
   is now a controlled A/B test.)
3. **The Eisenstein connection**: Σ τ(n)qⁿ is (up to the constant
   term) the E₂ q-expansion — if the ledger's continuum partition
   sums are modular objects, the arithmetic bridge (0048 standing)
   opens for real.
4. Standing: the correlation/trust tier (the Gaussian derivation of
   w = precision ↔ mutual information — queued next); t and N
   derivations; the bond's h².
