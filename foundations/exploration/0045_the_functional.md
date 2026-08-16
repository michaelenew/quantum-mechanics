# 0045 — The functional: the channel is a gauge field, the metric its square

The task: write the action. **Half works cleanly — and resolves
0030's standing obstruction — while the other half fails in a way
worth recording, falling back to the prototype path.** Code:
`output/0040_the_functional.py`.

---

## 1. The channel is a Maxwell field

Take the web's own channel one-form **A_μ = w·k_μ** (0035's
covariant channel). Its field strength is *exactly* the
Liénard–Wiechert field:

| source | \|F_channel − F_LW\| / \|F\| |
|---|---|
| static | 1e−8 |
| boosted v = 0.5 | 2e−8 |

The two potentials differ by a pure gradient — the same gauge orbit.
**The web's metric building block is a linear gauge field.**

## 2. The metric is its square

g = η + w·k⊗k is quadratic in the channel data. This is the
Kerr–Schild double copy (A = φk solves Maxwell, g = η + φk⊗k solves
Einstein — imported from the GR literature, verified here for the
web's channel). One structural fact, four measurements explained:

- **0044's Kerr–Schild linearization is inherited**: gravity is
  linear per channel *because the gauge theory is linear*;
- **0041's "charges add, bonds multiply"**: addition happens in the
  single copy, multiplication in the square;
- **0042's bond quantum = (charge quantum)²**: same reason;
- **the square-root ledger, now at the top of the theory**: the
  channel is the amplitude, the metric is the probability. The
  ½-exponent that ran through trust = √information, amplitude =
  √probability, det^(−1/2) screening and the codim ladder is the
  same ½ that relates channel to geometry.

Measured here: the single copy's vacuum condition (w harmonic)
selects p = d − 2 for every d ≥ 3 — **the same ladder gravity's
vacuum principle selected in 0042**.

## 3. 0030's obstruction resolved

0030 stopped at: *"4D BF is topological, so no gravitons; the bridge
is Plebanski's simplicity constraint."* The resolution is that
**the 3+1 single copy is not BF but Maxwell** — it carries a genuine
field strength (Coulomb, Liénard–Wiechert, radiative), and its
double copy is gravity *with* gravitons.

| dim | single copy | gravity |
|---|---|---|
| 2+1 | degenerate — d = 2 gravity takes constant w (the conical defect, no force, 0043) where Maxwell would give a logarithm *with* a force | topological; **no radiation** (measured, 0023) |
| 3+1 | Maxwell: Coulomb, LW, radiative | gravitons; **1/R TT waves at the quadrupole luminosity** (measured, 0031–0035) |

Both rows were measured on both sides before this module; the double
copy is what ties them together. The obstruction was an artefact of
taking BF as the 3+1 single copy — natural from the 2+1 prototype,
where the degeneracy makes gravity topological, and wrong one
dimension up.

## 4. The honest negative, and the fallback

**Does the double copy work off shell?** If the metric is a square,
adding the square's cross term to the two-body metric should fix
0037's O(M₁M₂) violation. Measured: **no.**

| c (cross-term coefficient) | −1.0 | −0.5 | **0.0** | +0.5 | +1.0 |
|---|---|---|---|---|---|
| max\|R_μν\| | 4.3e−2 | 2.0e−2 | **5.2e−3** | 2.6e−2 | 5.0e−2 |

The minimum is at c = 0 — the plain sum of squares. **The double
copy is a solution-level correspondence, not an off-shell squaring
map.** The bond therefore enters where it was already verified to
work: as *source stress* (0039/0040 — the quadrupole formula to
0.01%, the ADM binding energy to 0.03%).

### The state of the action

**Single copy — written:**

```
S = −(1/4) ∫ F_μν F^μν d⁴x  +  Σ_a q_a ∫ A_μ dx^μ_a
with   g_μν = η_μν + φ k_μ k_ν ,  A_μ = φ k_μ ,  k null geodesic
```

linear per channel, and degenerating in 2+1 to the topological form
0026 built (S = Σ B(curl θ − src)).

**Gravitational functional — prototype path.** As in 0026, it is
fixed by its charges and conservation laws (0044: ten Poincaré
charges as surface integrals, dE/dt = −L, dJ/dt = −L/Ω) rather than
derived by squaring. What remains unwritten is the off-shell map,
and the measured obstruction to the naive one is now on record.

## Honest limits

- The Kerr–Schild double copy is imported from the GR literature
  (Monteiro–O'Connell–White and the KS-double-copy line); what is
  measured here is that the *web's* channel is that gauge field.
- §1 tests two configurations (static, uniformly boosted). The
  correspondence for accelerated sources and for the wiggling
  string is not verified here, and is where such maps are known to
  need care.
- §2's "same ladder" is measured for d ≥ 3; at d = 2 the two sides
  genuinely differ (constant vs logarithm), which is the
  degeneracy §3 uses — consistent, but it means the dictionary is
  not uniform in dimension.
- §4 rules out *one* natural off-shell ansatz (a symmetric cross
  term with √(w₁w₂) weight); it does not rule out off-shell double
  copies generally.

## Open

1. **The off-shell map**: a squaring prescription that survives
   superposition. The measured constraint is now sharp — it must
   vanish for the naive symmetric cross term and reproduce the
   bond's source stress instead.
2. **The accelerated single copy**: verify A = wk remains Maxwell
   for the wiggling string and the orbiting binary (where the
   radiative sector lives) — this is the assumption the whole
   §2 reading rests on.
3. **Why the channel is null**: k null geodesic is what makes both
   copies work. The web derived it (0037: each channel rides the
   cone it creates) — worth stating as the one axiom the double
   copy needs and the web supplies.
4. **The 2+1 degeneracy**: sharpen §3's table into a statement
   about which gauge theories double-copy to topological gravity,
   which would make the dimensional trade (0043) a statement about
   the single copy.
