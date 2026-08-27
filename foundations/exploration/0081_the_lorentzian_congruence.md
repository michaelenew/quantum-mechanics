# 0081 — The Lorentzian congruence: signature is arithmetic mod 4

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Second stone down the queue. The wall's "Lorentzian lift" open item has
a heavy dynamical core (real-time measure, causal structure, the
interacting 4D theory) and a light kinematic shell — the structures
0061/0062 built in Euclidean signature, redone with η = diag(−1,1,1,1).
The shell is done here, exactly, and it turned out not to be routine:
**the arithmetic knows about signature, and it prices it as a
congruence on the level N.** Code:
`output/0072_the_lorentzian_congruence.py` — exact modular arithmetic
except the (classical) Gauss sums, which are floats.

---

## 1. The Lorentzian star splits only over N ≡ 1 (mod 4)

The Lorentzian Hodge star on bivectors satisfies **S² = −I** (verified
mod p at p = 5, 13, 7, 11), against S² = +I Euclidean. So its
eigenvalues are ±i, and the self-dual/anti-self-dual decomposition —
the working coordinates of the entire 4D program — exists over the base
ring **iff √−1 exists there**:

| level | √−1 | SD/ASD split |
|---|---|---|
| p ≡ 1 (mod 4): 5, 13 | i = 2, 5 ∈ F_p | **real: 3 + 3 over F_p** |
| p ≡ 3 (mod 4): 7, 11 | none | only over **F_p[i] = F_{p²}** |

For p ≡ 3 (mod 4) the split forces the quadratic extension — and this
is not a defect, it is **the continuum fact in arithmetic dress**: real
Lorentzian 2-forms have no real self-dual split either; the continuum
complexifies (this is exactly why Ashtekar's self-dual variables are
complex) and then imposes reality conditions. In the arithmetic theory
the complexification is the Galois extension F_{p²}/F_p, and:

> **Reality conditions are Frobenius invariance.** The Galois
> conjugation x ↦ x^p sends i ↦ −i (p ≡ 3 mod 4), and it maps the
> self-dual eigenspace onto the anti-self-dual one — verified 6/6 on
> constructed eigenvectors over F₄₉. "Real curvature" = a
> Frobenius-invariant SD ⊕ ASD pair, which is word for word the
> continuum prescription with Frobenius in place of complex
> conjugation.

For composite N the criterion sharpens: √−1 exists mod N iff **every
prime factor** of N is ≡ 1 (mod 4) — N ≡ 1 (mod 4) alone is not
enough (9 ≡ 1 mod 4 has no i). Verified by direct scan: the admissible
odd levels below 40 are 5, 13, 17, 25, 29, 37.

## 2. The Einstein predicate never depended on signature

0062's kernel identity, re-proved with η everywhere (operator raised
with the bivector metric G = η∧η, Ricci traced with η):

```
ker( M ↦ [R_op, ⋆_η] )  =  ker( M ↦ traceless Ricci_η )
rank 9 = 9 = 9 stacked, on the 20-dim Bianchi space
vacuum ([R,⋆] = 0 ∧ s = 0): rank 10, kernel = the 10-dim Weyl space
```

at p = 5, 13, 7, 11 alike — identical ranks to the Euclidean case.
Expected (it is an algebraic identity), but now checked rather than
assumed: **"this curvature is Einstein" is exactly sayable in the
Lorentzian arithmetic too, at every odd level, both congruence
classes.** Signature does not live in the field equations' predicate;
it lives in the star's square and nowhere else.

The measure side is even more indifferent: the frame-integration price
K(F) = N⁴·|ker F| (0061 §3) is built from ε alone — no metric appears
in it — and Pf(F) is likewise metric-free. The ledger never saw the
signature.

## 3. The same congruence sets the phase of the amplitude

The ledger's Born identity (0065/0074) writes the gcd weight as
|quadratic Gauss sum|²/N. The *amplitude* under that modulus obeys
Gauss's classical evaluation, re-verified here:

```
g_p = Σ_k ω^{k²}  =  √p        p ≡ 1 (mod 4)   — real, positive
                  =  i·√p      p ≡ 3 (mod 4)   — imaginary
```

(p = 5, 13, 17 vs 3, 7, 11, to 1e−9). So the two faces of the
congruence line up:

> On the class N ≡ 1 (mod 4) — where the Lorentzian SD split is real —
> the amplitude whose square is the ledger is *already real and
> positive*. On the other class the amplitude carries an explicit
> factor of i. The arithmetic theory does not need a Wick rotation to
> be told about signature: **the same quadratic-residue fact controls
> the geometry's split and the amplitude's phase.**

Stated as correlation, not mechanism: both facts reduce to "−1 is a
square mod p iff p ≡ 1 mod 4," which is one theorem wearing two hats.
Whether the physics makes the two hats one head — whether the real
amplitude class *is* the Lorentzian-consistent class of the dynamical
theory — is exactly the heavy part of the lift, untouched here.

## 4. The constraint stack on the level

The program keeps deriving conditions on its one regulator:

| constraint | source |
|---|---|
| N odd | Born structure / nondegenerate Gauss sums (0065, 0074) |
| N ≥ 3 | 4D deconfinement bound (0071) |
| every prime factor ≡ 1 (mod 4) | real Lorentzian SD split (here) |

**Smallest surviving level: N = 5.** (And by Fermat, the admissible
primes are exactly those expressible as a² + b² — the levels that split
as sums of two squares are the ones where spacetime signature is
representable. Flavor, not physics, but good flavor.)

## Honest limits

- This is the **kinematic shell only**. Nothing here constructs a
  Lorentzian path integral, a causal/transfer-matrix structure in real
  time, or the Lorentzian version of the interacting 4D nonabelian
  theory. The heavy stone is untouched; this settles what the
  arithmetic *arena* for it must look like.
- §2's signature-blindness was expected; its value is confirmation and
  the license to reuse 0061/0062 machinery verbatim in the Lorentzian
  program.
- §3 is a correlation between two consequences of one number-theoretic
  fact. I have not shown the dynamical theory *selects* the real
  class — the extension option (F_{p²} + Frobenius reality) remains
  open at p ≡ 3 (mod 4), exactly as complex variables + reality
  conditions remain workable in the continuum.
- The eigenspace and kernel computations are at specific small primes
  (5, 7, 11, 13). The statements are rank identities expected to hold
  for all admissible p; only these cases are certified.

## Open

1. The dynamical lift proper: a real-time/causal version of the 4D
   measure. The filter adoption plan's F3 (causal attainability of the
   batch posterior) is the doppelgänger formulation, and this stone
   now gives it a sharp arithmetic target: does the dynamical theory
   prefer the N ≡ 1 (mod 4) class where its amplitude is real?
2. Whether the SU(2) class-function ledger (0074+) has an analogous
   congruence story — its characters are real, so the question moves
   to the vertex/boundary phase.
3. Fold the constraint stack into the bar's knob-derivation demand
   (0069 (D)): three independent constraints on N now exist; a fourth
   that pins N against the strength of gravity would be a derivation.
