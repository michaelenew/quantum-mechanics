# 0074 — The nonabelian Dirichlet square: the ledger was a Born rule all along

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0073's sign problem demanded the dual-square structure. Chasing where
the abelian ledger's positivity actually comes from turned up
something sharper than the demand. Code:
`output/0066_the_nonabelian_dirichlet_square.py` (0.6 s).

---

## 1. The ledger is a Born square — exact

For **every odd N tested** (3, 5, 7, 9, 11, 15, 21, 25, 33, 45, 61 —
all fluxes):

> **gcd(F, N) = | Σ_e ω^(e²F) |² / N**

The Z_N ledger weight — the black box 0053 measured, 0064 opened into
the divisor ensemble, and 0064 §3 dualized into τ — is the **squared
magnitude of a quadratic Gauss sum**: the Born rule applied to a
single-frame amplitude, with B = e² the abelian shadow of B = e∧e.
The measure was never a postulate; it was |amplitude|² from the start.

Two corollaries with reach:

- **Even N fails** (at most fluxes) — N = 2's degeneracy family
  (Kulkarni–Nomizu, SD/ASD, 4D confinement, and now this) traced to
  the root: no odd quadratic Gauss structure.
- **The positivity mechanism is visible**: the amplitude's dual
  expansion *counts frames* — r(m) = #{e : e² = m} ≥ 0 — so the
  weight's dual is the **autocorrelation of a nonnegative function**,
  automatically ≥ 0. Verified exactly (dual(gcd) = r⋆r at every mode,
  N = 15 and 21). τ = 1∗1 was the arithmetic face of this; the Born
  structure is its cause.

## 2. The positivity theorem, fusion form

If W = A² with A = Σ_j n_j χ_j a **counting amplitude** (n_j ≥ 0),
then every character coefficient of W is a sum of nonnegative fusion
terms: c_j(W) = Σ n_m n_m′ N^j_{mm′} ≥ 0. Checked over 200 random
nonnegative countings on SU(2) (multiplicity-free fusion): min
coefficient exactly 0. And the counting condition is what does the
work: the *virtual* amplitude χ₁ − χ₀ — an Adams-operation image, the
natural "nonabelian divisor" candidate — has c₁(A²) = −1 < 0. The
Dirichlet structure's nonabelian lift is virtual (Adams operations
carry signs); the Born structure's lift is not. **The right square is
the Born square.**

## 3. The derived nonabelian amplitude is diagonal

A frame pair spans a simple bivector, and **simple = balanced**
(||B⁺|² − |B⁻|²| < 10⁻¹⁴, random frames) — so the frame-counting
amplitude on Spin(4) lives on the diagonal:

```
A(U⁺, U⁻) = Σ_j n_j χ_j(U⁺) χ_j(U⁻)
```

with n_j the Gaussian frame measure's counting of |B⁺| (deterministic
quadrature, binned at scale s₀; two scales reported). The Born weight
W = A²:

- **every coefficient ≥ 0** (asserted; by construction),
- diagonal-dominant with positive-small off-diagonal — nothing
  forbidden, the ledger's signature, now with healed signs
  (c(1,1) = 2.71 vs c(1,0) = 1.00 at s₀ = 0.75),
- the diagonal profile follows the derived radial counting (peaked,
  not monotone — an honest difference from the ε-form kernel, set by
  the binning scale),
- and **pointwise the weight still ridges on the balanced classes**:
  ridge/off-ridge = 240× — the kernel's Cauchy concentration,
  preserved.

## 4. The wall status

0073 lifted the *weight* and met the sign problem. 0074 lifts the
*amplitude* and squares on the group: coefficient-positive by fusion,
ridge preserved. **The cure is the program's own rule — probability =
amplitude², applied at the right tier.** The healed object is
Barrett–Crane *as an amplitude* — "BC squared" — with a derived
radial profile. A3, the graviton-propagator test, now has a positive
object to run on.

And the toy-problem point stands sharpened: the abelian tier of this
entire structure — amplitude, Born square, dual counts, sign problem
and its cure — is *exactly solvable*. Most programs meet the sign
problem in Monte Carlo fog; this one owns a closed-form toy of it
(and the sibling arithmetic branch's "sign problem" probe suggests
the toy has already been hit from the other side).

## Honest limits

- The Born identity is verified for odd N ≤ 61, not proven for all
  odd N (it is a classical Gauss-sum theorem shape; a proof pass
  should cite or derive it properly).
- The nonabelian amplitude's radial counting n_j depends on the bin
  scale s₀ (two scales shown); the *positivity* and *diagonality* do
  not, but the profile numbers do. The continuum (unbinned) version
  — a coherent-state rather than character bin — is the right next
  refinement and touches the EPRL machinery.
- One plaquette; no intertwiners or vertex assembly; Euclidean
  Spin(4); integer bins (vector frames — consistent with 0073's
  center-blindness, but a choice here).
- W = A² pointwise-squares the amplitude; the relation of THIS
  square to the |K_L|²-vs-K_L convention at the algebra tier (a
  price-doubling bookkeeping) is noted, not resolved.

## Open

1. **A3 on the healed weight**: the graviton-propagator test against
   0063 — the wall's decisive stone, now unblocked.
2. The Born identity's proof (classical Gauss-sum literature) and
   its even-N obstruction stated precisely.
3. The coherent-state (unbinned) amplitude — the EPRL-shaped
   refinement of n_j.
4. The 2+1 abelian toy of the sign problem, packaged as such (the
   user's point: a toy other programs lack); cross-reference the
   arithmetic branch's probe on the next pass.
