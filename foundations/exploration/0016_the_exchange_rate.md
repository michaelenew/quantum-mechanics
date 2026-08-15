# 0016 — The exchange rate: the compensator is an information functional

0015's three opens, executed. The headline: the amplitude-phase
compensator is now priced in information units, the binary-trust
premise is discharged as a theorem of genericity, and time-reversal
staging finds chirality exactly where the census is most braided.
Code: `output/0011_the_exchange_rate.py`.

---

## 1. The exchange-rate law

The cone-angle integrand factors into estimation-theoretic pieces:

```
Θ = ∮ √( J_ang|rad / J_rad ) dφ = ∮ √(C/E) · e^(−I(φ)) dφ
```

J_rad = E is the total radial information; J_ang|rad = C − B²/E is
the Schur complement (conditional angular information); and
I = −½ln(1−ρ²) is the **Gaussian mutual information between the
radial and angular score errors**. So the deficit — and the
compensator φ = π − δ — splits exactly into an **anisotropy part**
(2π − ∮√(C/E)) and a **correlation part** (∮√(C/E)(1 − e^(−I))):

| k | δ | anisotropy | correlation | mean I |
|---|---|---|---|---|
| 2 | π | 2.7577 | 0.3839 | 0.188 |
| 3 | 1.9351 | 1.7883 | 0.1468 | 0.035 |
| 6 | 0.9851 | 0.9466 | 0.0384 | 0.007 |
| 12 | 0.5051 | 0.4950 | 0.0101 | 0.002 |

Two anchors make the reading exact rather than suggestive:

- **Any constant SPD information matrix is flat**: ∮√(det A)/A_rr dφ
  = 2π exactly (verified over random A, correlations included).
  Ambient anisotropy alone curves nothing.
- **Participation curves; spectating does not.** Remove the beacon's
  *own* channel and transport around its site drops to 0.00000: the
  conical atom at an interaction is created by that interaction's
  own information channel — the apex exists only for participants.

So the user's conjecture lands in a sharpened form: the compensator
is not "the information the others hold about the interior" but
**the anisotropy-plus-score-correlation of the information field the
other channels leave you, activated by your own participation**. The
amplitude phase is priced in the web's own currency.

## 2. Binary trust, derived

0015's conditional ("*if* round-trip trust is binary") is discharged
inside the synthesis: at a generic double point the fiber has
exactly two preimages (Whitney genericity), so loop monodromy acts
through Sym(2) = Z₂ — winding reduces mod 2 through the sheet swap,
verified on the model cover w² = z (n windings flip the sheet iff n
odd, n = 1..6). Triple points are isolated events no loop can link,
so no loop ever probes an S₃ fiber. **Round-trip trust is binary by
genericity**, the forced-U(1) conclusion of 0015 is now
unconditional within the synthesis, and the compensator's value is
pinned to π − δ by continuity along web families (max step 0.049
over the θ-sweep — no branch ambiguity).

## 3. Time reversal: chirality lives on the deepest braiding

A movie run backwards applies inverse events in reverse order, so a
surviving weight must satisfy the tetrahedron identity for R *and*
R⁻¹. Solving the joint system for all 21 orbits (p = 2, 3):
**19 of 21 orbits retain nonconstant bidirectional weights — and the
two casualties are exactly the (4,4) orbits**, the census's most
braided solutions (placement group order 384). Their weights exist
only forward: **time-reversal-asymmetric (chiral) weights live
precisely on the deepest braiding**, echoing the physical pairing of
chirality with braided statistics. A bidirectional nonconstant
witness on a nonabelian orbit is verified in both directions on all
64 states.

## Honest limits

- §1's decomposition is exact algebra on the validated cone formula;
  the "currency" reading (Gaussian mutual information of score
  errors) is the standard Gaussian-local interpretation of Fisher
  quantities, not a new theorem beyond the identity.
- §2's derivation rests on Whitney genericity (standard, cited) and
  on loops-in-the-complement as the probe class; non-generic
  (fine-tuned) projections evade it exactly as degenerate cases
  should.
- §3 stages time reversal only; the cup/cap algebra (births, deaths,
  saddles) remains the last unstaged move family before a full
  surface invariant.

## Open

1. **The correlation part's decay law.** The table suggests the
   correlation share of the deficit falls faster (~1/k²?) than the
   anisotropy share (~1/k): if so, dense webs are anisotropy-priced
   only, and the mutual-information term is a genuinely two-party
   effect — worth a closed form.
2. **Chirality as an invariant.** The (4,4) forward-only weights:
   do they detect orientation of a movie (a set-theoretic arrow of
   time), and is their loss under reversal the census shadow of the
   framing anomaly?
3. **Cup/cap.** The one move family left.
