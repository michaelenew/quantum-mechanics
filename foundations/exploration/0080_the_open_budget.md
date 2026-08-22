# 0080 — The open budget: Λ off the closed surface

First stone of the post-wall queue, easiest first. 0069 §2 laid out the
falsifiability path for vacuum energy and named its step 1: *reformulate
the budget off the compact torus — the constraint Σ F ≡ 0 was derived on
closed lattices, and the compactness assumption currently does work.*
That step is delivered here, by exact enumeration — every statement
below is a complete count over lattice configurations or an exact
integer identity, no sampling. Code: `output/0071_the_open_budget.py`.

---

## 1. A disk has no budget

Enumerate all N¹² link configurations of a 2×2-plaquette open lattice
(3×3 vertices) at N = 3 and tally the four plaquette fluxes:

| | count |
|---|---|
| attained flux combinations | **81 = N⁴, all of them** |
| multiplicity of each | **6561 = N⁸ = N^(V−1), identical** |

Every flux configuration is attained, each with exactly the gauge
volume as multiplicity. **The measure on fluxes is unconstrained**:
Π W(F_p) with no delta function. The closed-universe budget was never
dynamics — it was the closure of the surface. Off the closed surface it
is simply absent, and Σ F becomes an *observable*.

## 2. Freezing the boundary restores it — as Stokes' theorem mod N

Same lattice, boundary links frozen to arbitrary values, interior links
enumerated. For every random boundary assignment tried:

```
attained Σ F  =  { hol(∂) }        exactly, uniform multiplicity
```

where hol(∂) is the sum of the frozen links around the outer loop. The
generalization conjectured in passing during the wall arc is now exact:

> **The open-universe budget is Σ F ≡ hol(∂) (mod N)** — total
> curvature equals boundary holonomy, the discrete Stokes theorem. The
> closed budget Σ F ≡ 0 is its special case hol(∂) = 0 (no boundary).
> Control: the 2×2 torus enumerated the same way recovers Σ F ≡ 0 with
> multiplicity N^(V−1)·N² (gauge volume × the two Wilson-line moduli —
> the count that confirms H¹(T²) = Z² inside the tally).

So the budget is a **topological ledger**: one linear condition per
closed surface, none per disk, boundary data in between. Three
ensembles, three fates for the total curvature:

| arena | Σ F is | Λ-residual |
|---|---|---|
| closed | constrained to 0 | exactly zero, topologically |
| Dirichlet boundary | fixed to hol(∂) | a boundary *datum* |
| free boundary | a random variable | quantized, distribution below |

## 3. The toy Λ: quantized, and uniformly distributed at large area

On the free disk the total curvature has an exact distribution. Using
the divisor identity gcd(F, N) = Σ_{d|N} φ(d)[d|F], the dual ledger
weight is the *integer*

```
Ŵ(n) = Σ_{d|N, (N/d)|n} φ(d)·(N/d),      Ŵ(0) = P(N)
```

and for a disk of P plaquettes

```
Prob(Σ F = h) = (1/N) Σ_n (Ŵ(n)/Ŵ(0))^P ω^{nh}
```

— verified against the direct weighted enumeration at N = 3, P = 4 to
1e−12. Two exact consequences:

**(a) The residual is quantized and asymptotically uniform.** The
values are 2πh/N, and the deviation from the uniform distribution dies
as **r_max^P** — an *area law* with

```
r_max = max_{n≠0} Ŵ(n)/Ŵ(0)  =  φ(N)/P(N)  =  f(N)     (N prime)
```

**the same base as the confinement tension** (0064's
log(P(N)/φ(N)) per plaquette). Verified: at N = 3 the decay tracks
(2/5)^P to 1e−9 relative across P = 4 → 64. The rate at which a large
universe forgets its total curvature *is* the string tension.

**(b) At composite N the fine structure of the budget dies first.** At
N = 15 the dual weights sort by gcd(n, 15): r = 8/45 (gcd 1), 2/5
(gcd 5), **4/9 (gcd 3, the maximum)**. The surviving deviation at large
P is exactly (5[5|h] − 1)/15 · (4/9)^P (verified to 1e−6 relative at
P = 256): the distribution equilibrates over Z₁₅ quickly but the
residue of Σ F **mod 5 = mod (N/3)** lingers longest. The coarsest
subgroup of the budget is the most robust observable — the mod-p
shadow of Λ outlives its fine value.

## 4. What this does to the falsifiability path

0069's four steps, updated:

1. ~~Budget off the compact torus~~ — **done, exactly.** The
   compactness assumption is now priced: closure is *why* Λ = 0, not a
   technicality. An open or bounded universe carries Λ as a boundary
   datum or a quantized random variable instead.
2. Zero mode in the continuum τ-theory — clarified but not done. On
   the open arena the "divergent" mode Ŵ(0)^P is just the partition
   function Z_disk = P(N)^P (nothing diverges; there is no constraint
   to fight). The identity Prob(Σ F = h) = Z_torus-twisted-by-h /
   Z_disk says 0064's divergence was always the closed budget eating
   the zero mode, never a pathology of the weight.
3. Residual spectrum ∝ 2πn/N — **delivered for this toy**, with its
   distribution, not just its support.
4. Confrontation with Λ_obs — still blocked on the arena step (what is
   the physical universe's topology/boundary in this program), and
   §3 sharpens what's at stake: on a *free* arena the measure does
   **not** prefer Λ = 0 — the distribution is asymptotically uniform
   over the quantized values. Smallness of Λ is not dynamical in this
   toy; it must come from closure (topology) or boundary data. That
   is a real, honest constraint on what step 4 can claim: the program
   predicts *quantization* of the residual, and predicts *zero* only
   for closed universes.

## Honest limits

- All of this is the **abelian 2D toy** (the arena where the budget was
  originally derived). The 4D nonabelian analogue — what replaces
  Σ F ≡ 0 when fluxes are SU(2) classes on a boundary-carrying complex
  — is untouched, and is where the physical claim would live.
- "Uniform at large area" is a statement about the *free-boundary
  ensemble* of this measure; a physical universe is not obviously any
  of the three ensembles. The table in §2 is the menu, not the choice.
- The N = 3 disk is small (P = 4). The multiplicity and constraint
  statements are exact and size-independent by the gauge-counting
  argument they verify (L = P + V − 1 on a disk), but only the small
  case was enumerated.

## Open

1. The 4D/nonabelian budget: does the class-function measure on an
   open 4D complex carry the analogous statement (total flux =
   boundary state)? This connects directly to the boundary-state
   vertex work (the heavy stone).
2. Step 2 proper: the zero mode in the continuum τ-theory.
3. Step 4's arena question, now sharpened by §4.
