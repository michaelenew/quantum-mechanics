# 0086 — The two ledgers: the polar theorem, and the budget's real job

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

Seventh stone, and the **first pivot down the escalation ladder**:
0085's protection calculation, run in the Z_N toy because that is
where it is exact. It came back with a theorem, a leak, and a
correction to 0085's assumed mechanism — the toy did precisely what
it was recruited for: it did not confirm the story, it *fixed* it.
Code: `output/0077_the_two_ledgers.py` (exact dual-formula sums,
cross-checked against brute flux enumeration at 1e−12 throughout).

---

## 1. The polar theorem

On the open (unconstrained) lattice, with frustration n_p at each
plaquette and a Wilson loop enclosing area A:

```
⟨W⟩  =  exp( i·2π/N · Σ_enc n_p )  ×  f(N)^A          — exact
         └── source ledger ──┘        └ record ┘
```

The two ledgers 0085 discovered by their scalings are literally the
**polar decomposition of one complex number**. The phase carries only
the sources — additive, area-independent, the mass-extensive ledger.
The modulus carries only the record — the f(N)^A area law, blind to
every source. Verified exactly for arbitrary frustration patterns,
and the vacuum phase is 0 for every loop on both geometries (W even,
Ŵ real).

> **The vacuum record cannot twist, categorically.** 0085 §2 worried
> that the area-extensive record would curve every cut unless the
> budget protected it. No protection is needed: records are moduli.
> Confidence damps; content twists. (This is the program's seed —
> "a distribution cannot encode its own confidence" — materialized
> as the two factors of a Wilson loop: |⟨W⟩| is the confidence
> channel, arg⟨W⟩ the content channel.)

## 2. The budget does not delete uniform sources — it quantizes Λ

0085 credited the budget/zero-mode deletion with protecting the
vacuum. The toy says the budget's actual job is different, and
smaller, and it is exactly the job 0069/0080 described:

- **N = 3, P = 9 (N | P):** a uniform frustration n = 1 satisfies the
  budget outright (Pn ≡ 0 mod N), and every loop reads the full
  Λ phase 2πA/3 **exactly**. Uniform vacuum energy gravitates,
  quantized.
- **N = 5, P = 9 (coprime):** the budget must offset Pn ≡ 4, but
  fluxes are discrete — there is no way to smear −n/P over the
  lattice — so it subtracts **one quantum, localized**, and uniform
  curvature appears at essentially full strength (arg = 1.2584 vs
  naive 1.2566 at A = 1). The smeared trace-removal guess
  (1 − A/P), which 0085's unimodular intuition would predict, is
  **rejected by measurement** (deviations 0.14–0.49 rad vs 0.002–0.07
  for the naive reading).
- **The one true deletion:** the A = P loop reads phase 0 exactly for
  any uniform n. The budget constrains the *global* residual only:
  **Λ·Volume ∈ (2π/N)·Z** — 0069's quantized spectrum and 0080's
  residual distribution, now visible dynamically in loop phases.

So the corrected division of labor, recorded as a revision of
0085 §2:

| layer | what protects | mechanism | status |
|---|---|---|---|
| (i) the vacuum record | the polar theorem | records are moduli — cannot source | exact, constraint-free |
| (ii) the global Λ | the budget | one global mode: Λ·V quantized | exact, and *only* global |

The "mutual protection" of paths C and Λ survives with reassigned
roles: path C's vacuum is safe by (i) alone; path Λ's content is
(ii) — and (ii) is a *quantization*, not a deletion, consistent with
0080's finding that the measure does not prefer Λ = 0.

## 3. Small-universe corrections, measured

Two finite-closed-universe effects, quantified rather than guessed:

- **Vacuum complementarity:** on the torus Σ_enc F = −Σ_comp F, so
  |⟨W(A)⟩| = |⟨W(P−A)⟩| and the f^A modulus law bends back as
  A → P/2 (2% off at A/P = 1/3, large by A/P = 4/9).
- **Defect erosion:** a single enclosed defect keeps 99.9% of its
  open-lattice deficit at A/P = 1/9, eroding to 72% by A/P = 4/9 —
  the budget's compensating quantum sits somewhere in the complement
  and the loop increasingly averages over it. A finite-universe
  correction with the right limits (full deficit as P → ∞), not a
  trace removal.

## Honest limits

- Abelian 2D toy throughout — recruited deliberately (the escalation
  ladder's second rung); the polar factorization's exactness is
  special to the abelian product measure. In the 4D nonabelian
  theory the analogous split (class-function magnitude vs central
  phase) is a conjecture this stone motivates but does not prove.
- The Λ-leak statement is about *frustration* sources (preferred
  flux). A different microscopic model of vacuum energy could couple
  differently; within the toy's source model the conclusion is
  exact.
- The 2+1 continuum limit of the leak (does the quantized Λ survive
  the τ-theory's continuum scaling?) is 0069 step 2, still open.

## Open

1. **The nonabelian polar split**: does the SU(2) ledger's ⟨W⟩
   factorize into a central phase (source) × class-function modulus
   (record)? The vertex machinery (0078) has the pieces; this is the
   natural bridge stone back to the full theory.
2. Λ-leak phenomenology: on the physical reading, the universe's
   P mod N decides whether uniform vacuum energy is allowed to
   gravitate — fold into 0069 step 4's confrontation (a new, sharp
   input: Λ ∝ (Pn mod N)/P·2π/N).
3. The 2+1 continuum limit of layers (i)–(ii) (0069 step 2).
4. Decoherence as inter-ledger transfer (0068/0085), now precise:
   collapse should move an entry from modulus to phase.
