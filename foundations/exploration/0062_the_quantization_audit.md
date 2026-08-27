# 0062 — The quantization audit

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

A model-switch audit of the quantized-curvature arc — 0061 and its
revision, with spot-rechecks of 0057 — requested on the ground that
the work was done under a different model and its consistency was in
question. Verdict: **everything substantive held; one verification was
much weaker than its headline claimed and is now exact; one wording
and one citation were wrong; and the audit produced a small theorem**
that resolves 0061's open sub-question about the exactly-2 price
ratio. Code: `output/0056_the_quantization_audit.py` (14 s).

Scope note: 0059 and 0060 were adversarially audited in-session when
written (0060 §4 records the gauge-dependence correction that audit
produced), so this pass concentrates on 0061 and its revision.

---

## 1. What held, upgraded from sampled to exact

0061's projector checks were spot-samples. Now, on **every** one of
the 20 basis elements at N = 5 and 7: the Weyl projector's output is
symmetric, satisfies the first Bianchi identity, is annihilated by the
Ricci contraction, and is idempotent; its image has rank 10 — exactly
the kernel of the rank-10 Ricci map. Identities, not statistics.

The dimension counts (20/10/10 and 6/6/0), the price-changed tests,
the Gauss-sum mechanism with its rejected misreading (2673 vs 729),
and the three holonomy corrections (strings radiate; quantum ≠ finite;
continuity not non-commutativity) all survived scrutiny unchanged.

## 2. The verification gap: a headline number with no evidential force

0061 §2 reported "[R, ⋆] = 0 ⟺ traceless Ricci = 0, verified
3000/3000." **Those 3000 samples contained zero positive cases** — a
random curvature is Einstein with probability ~N⁻⁹ — so the check, as
shipped, confirmed only "generic curvature fails both conditions." The
pure-Weyl check covered one direction of the equivalence; the converse
(commuting ⇒ Einstein) was untested entirely. The assertion would have
passed even if the equivalence failed everywhere on the commuting set.

This is exactly the consistency failure the audit was looking for: a
true statement verified by a procedure that could not have caught its
falsity.

The repair is exact linear algebra, no sampling. On the 20-dimensional
Riemann space, the linear maps M ↦ [M, ⋆] and M ↦ traceless Ricci(M)
have **identical kernels**: each has rank 9, and their stacked map
also has rank 9 (N = 5 and 7). Equal ranks with equal stacked rank
forces equal kernels, so the equivalence is proven over Z_N, both
directions, all curvatures.

**Sharpened while repairing**: [R, ⋆] = 0 is **Einstein-with-Λ**
(R_ab ∝ g_ab), not vacuum. Witness: Weyl + 2·Id commutes with ⋆ while
Ricci = (s/4)δ ≠ 0. Vacuum is the pair [R, ⋆] = 0 ∧ s = 0, equally
arithmetic — its kernel equals the full Ricci map's kernel (rank
10 = 10 = stacked 10). 0061 §2's title said "vacuum"; the criterion it
stated was Einstein. Both are decidable predicates; they are different
predicates.

## 3. The theorem: the price is the rank

Chasing the price mechanism one step past 0061 closes an open. The
kernel map b ↦ ε_IJKL b^J F^KL **is** the alternating matrix ⋆F
acting on frame vectors — verified against the shipped `m_of` on 400
random pairs, then used exhaustively. Hence |ker F| = N^(4−rank ⋆F)
and

```
price(F) = rank(F) × log N
```

**Alternating forms have even rank in every characteristic.** So the
only possible tiers are 0, 2, 4 — and the "exactly 2" cost ratio that
0061 flagged as suspiciously clean is the parity theorem for
alternating forms, not a coincidence and not a physics input.

Verified exhaustively: every configuration at N = 3 (729, with
literal kernel counts confirming |ker| = N^(4−r)), N = 5 (15 625) and
N = 7 (117 649); rank even in every single case; tier ⟺ Pfaffian
exact throughout (rank 4 ⟺ Pf ≠ 0; rank 2 ⟺ Pf = 0 with F ≠ 0;
rank 0 ⟺ flat).

This ties the arc's three descriptions of the price into one
statement: 0055's Pfaffian table, 0056's kernel codimension, and
0057's self-dual imbalance are all shadows of *rank of the curvature
bivector as an alternating form* — and "how many planes the curvature
rotates" (0061) is rank/2, literally.

## 4. The two errors found

- **Citation**: 0061 attributed the loop-decay measurement
  Γ = P/(Gμ²) = 45.8 to exploration 0049. 0049 *built* the
  Kibble–Turok loop and listed decay power as its open 4; the
  measurement is 0050's (`output/0045`, `loop_power`: 45.8 at R = 20,
  45.4 at R = 30). Fixed in 0061, in `output/0055`'s docstring and
  prints, and in the SUMMARY entry.
- **Wording**: "vacuum Einstein equation" for the commutator
  criterion (§2 above). Fixed with the witness recorded.

## 5. What remains Monte Carlo, knowingly

0061 §3's sector comparison (cheapest-tier fractions for pure Weyl /
generic / pure Ricci) is a sampled statement and stays one, but the
ordering **pure Ricci > pure Weyl ≫ generic** reproduces at three
fresh seeds (0.0640/0.0620/0.0677 vs 0.0117/0.0100/0.0117 vs
0.0003/0.0007/0.0000). The honest negative — the measure does not
select the Einstein sector — stands. 0057's self-dual reading and
critical-dispersion arithmetic also reproduce exactly.

## Honest limits

- The audit proves statements about the *formal* Z_N curvature
  operator — 0061's own honest limits (symmetries imposed by hand,
  Euclidean signature, the six-columns lift as a modelling choice)
  are inherited, not discharged.
- Section 3's theorem is for prime N (rank over a field). Composite N
  (0053's divisor structure) needs the alternating-form theory over
  Z_N as a ring — even rank still holds for alternating forms over
  any commutative ring in the appropriate Smith-form sense, but that
  was not verified here.
- The seed-stability check is three seeds of 3000, adequate for an
  ordering that differs by factors of 5–100, not for fine structure.

## Open

1. **The price is pure symplectic linear algebra** — rank
   stratification of the alternating form ⋆F. Does the whole measure,
   frame correlations included (0056 §3), reduce to symplectic
   invariants of the curvature data? If so, the geometric/
   non-geometric distinction (0061 open 1) is the rank-2 stratum of
   the bivector variety, and the question "what does the tier
   structure correspond to tensorially" has a candidate answer:
   nothing tensorial — it is the symplectic stratification, which is
   *finer* than any curvature decomposition.
2. Composite N inside the rank picture (carries 0056's open 3
   forward, now sharper: Smith normal form of ⋆F over Z_{2^k}).
3. Standing: the continuous-twist lift (0061 open 2), Lorentzian
   ⋆² = −1 (0061 open 3), the correlation gap (0058), the bond's h²
   (0060).
