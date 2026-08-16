# 0057 — Quantum Newton, and what stays massless at the critical point

0056 found the critical point where the lattice graviton goes
massless and named the consequence as the arc's sharpest open: *the
critical point exists, and the question is what force lives there.*
This closes it. **The critical lattice theory mediates a 1/r force
with the Newtonian coefficient**, and the mode that mediates it is
the geometric one — the non-geometric sector stays gapped by exactly
the geometric price. Code: `output/0052_quantum_newton.py`.

---

## 1. The critical dispersion is quadratic

On a 3D spatial lattice the curvature quantum carries the on-site
price V and hops to six neighbours with amplitude t, so

```
E(k) = V − 2t Σ_i cos k_i,     gap closes at t_c = V/6
```

and at t_c the dispersion is E(k) = 2t Σ_i (1 − cos k_i) → t k².

| k | 0.4 | 0.2 | 0.1 | 0.05 |
|---|---|---|---|---|
| E/(t k²) | 0.9867 | 0.9967 | 0.9992 | 0.9998 |

A quadratic dispersion is a **1/k² propagator**, and in three
spatial dimensions a 1/k² propagator is Newton. That is the whole
argument in one line — but the coefficient is the part worth
measuring, because getting 1/r is cheap and getting 1/(4πt) is not.

## 2. Quantum Newton

The static potential is the lattice Green function

```
G(r) = (1/L³) Σ_{k ≠ 0} cos(k·r) / E(k)
```

with the k = 0 mode removed — and **that removal is not a
regularization choice, it is the closed-universe budget** Σ F = 0
that 0029 imposed classically and 0054 found in the quantum measure.
The theory has no zero mode to propagate, so the sum has none to
drop.

Fitting G = A/r + B on L = 56 as the window moves outward:

| window | r = 2..8 | 4..10 | 6..14 |
|---|---|---|---|
| A/(1/4πt) | 1.0996 | 1.0237 | **0.9907** |

Short r is inflated by lattice structure, long r deflated by
periodic images. Holding the window fixed at r = 6..14 and growing
the box separates the two:

| L | 32 | 40 | 56 | 72 |
|---|---|---|---|---|
| A/(1/4πt) | 0.8744 | 0.9482 | 0.9907 | **1.0023** |
| offset B | −0.0145 | −0.0133 | −0.0104 | **−0.0084** |

Monotone convergence to the Newtonian coefficient **1/(4πt) to
0.2%**, with the offset heading to zero as the box grows. And the
coupling dependence is exact, not fitted: doubling t halves A, ratio
**2.0000** to four digits.

> **The critical quantum lattice theory mediates a 1/r force with
> the right coefficient.** 0036's classical Newton, obtained from
> the quantized model.

This is the step 0056 §1 explicitly did not take. The chain is now:
the measure prices curvature (0053), the price resolves by
simplicity (0055) and equals the kernel codimension (0056), the
quantum is massive off criticality (0056), and *at* criticality it
propagates a 1/r potential with the Newtonian normalization.

## 3. What stays massless: the geometric sector only

The price has two tiers (0055/0056): geometric (simple) curvature
costs 2 log N, non-geometric costs 4 log N. Two tiers means **two
critical couplings**, and they cannot both be reached. Tuning to the
geometric one, t_c = 2 log N/6:

| | geometric price | non-geometric | gap at t_c (simple) | gap at t_c (non-simple) |
|---|---|---|---|---|
| N = 3 | 2.1972 | 4.3944 | **0.000000** | **+2.197225** |
| N = 5 | 3.2189 | 6.4378 | **−0.000000** | **+3.218876** |

The surviving gap is exactly **2 log N — the geometric price
itself**. So the critical point is selective: it lets the geometric
sector through massless and leaves the non-geometric sector massive,
with a gap set by the same number that made the tier.

That is the job Plebanski's simplicity constraint is supposed to do
— project the BF theory onto the gravitational sector — **obtained
here as a gap rather than an imposition.** 0055 found the constraint
is priced rather than forbidden; this says what the pricing buys:
tune to the cheap tier and only the cheap tier is light.

## 4. And the priced direction is the self-dual imbalance

Decomposing the curvature bivector into self-dual and anti-self-dual
parts over Z_N, the simplicity invariant turns out to be a function
of the **imbalance alone**:

```
Pf(F) = function of ( |F⁺|² − |F⁻|² )   only
```

verified over all N⁶ curvatures at N = 3 and N = 5. At N = 3 the map
is imbalance 0 → Pf 0, 1 → Pf 2, 2 → Pf 1.

Since the price depends only on Pf (0055), **exactly one of the six
internal directions is priced** — the SD/ASD imbalance — and the
balanced cone is cheap. Plebanski's constraint |F⁺| = |F⁻| is not
imposed anywhere in this construction: it is the statement that the
theory charges for imbalance, and the balanced configurations are
the free ones.

That is a considerably tighter reading than 0055's Pfaffian table.
The price is not a generic function on a six-dimensional space of
curvatures; it is a function on a *one-dimensional* quotient, and
that quotient is the self-dual/anti-self-dual asymmetry that
distinguishes gravity from BF theory in the continuum.

## Honest limits

- §1–2 use the **single-quantum** dispersion on a 3D lattice with
  six neighbours, giving t_c = V/6. 0056's t_c = V/2 came from the
  **pair** gap Δ = 2V − 4t in one relative dimension. Both are
  correct for their model; they are not the same critical coupling,
  and neither is the critical coupling of a full interacting 3+1
  lattice, which would renormalize it. What survives model change is
  the *structure*: a gapped phase, a critical point, and a quadratic
  dispersion at it.
- §2's coefficient is measured, not derived. The 1/(4πt) is the
  continuum Green function of the quadratic dispersion, so §2 is
  properly a *verification that the lattice sum converges to its own
  continuum limit* with the zero mode removed — a real check, since
  the removal is physically forced rather than chosen, but not an
  independent derivation of 4π.
- §2 uses a free propagator: two static sources coupled to a
  non-interacting critical quantum. Interactions at criticality are
  exactly where a lattice theory is hardest, and nothing here
  probes them.
- §3's gaps are read off the tiered price of 0055/0056 plugged into
  §1's dispersion, not from a spectrum computed on the constrained
  measure. The claim "only the geometric sector is massless" is
  therefore as strong as the tier structure, which is exact, and as
  weak as the single-quantum dispersion, which is a model.
- §4 is exact over Z_N for prime N. The SD/ASD split uses the
  inverse of 2 mod N, so N even is excluded; the composite-N divisor
  structure of 0053 is still unexamined here (0056's standing open).

## Open

1. **The polarization count at t_c**: with a critical point, a
   massless geometric sector, and a 1/r potential in hand, count the
   propagating modes there — the spin-2 test, now with a specific
   coupling and a specific surviving sector to count in.
2. **Interactions**: §2 is a free propagator. The first
   post-Newtonian correction from the lattice would be the sharpest
   possible contact with 0037's classical tests.
3. **Composite N**: the 2-adic grading of 0053 inside §4's self-dual
   reading — the split needs 2 invertible, which is exactly where
   the divisor structure lives.
4. Standing from 0048: the Lorentzian arena, P4 → Tsirelson, matter
   beyond scripted sources, the arithmetic bridges.
