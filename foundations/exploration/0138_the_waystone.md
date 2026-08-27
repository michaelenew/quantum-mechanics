# 0138 — The waystone: every material result, by tier, by criticality

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

**Scope: stones 0001–0137.** This is a snapshot, not a live board.
Anything numbered above 0138 supersedes it; `SUMMARY.md` holds the
current state. Read this to find out where a result *sat* as of
0137, not whether it still sits there.

Two axes: **(classical, quantum) × (discrete, continuous)**. Discrete
means a finite ring — Z_N, the exactly-solvable toy. Continuous means
a Lie group or a field: SU(2), a scalar, a metric.

**Status key** — `LIVE` in the continuous theory · `LIFTED` proved on
the toy and carried across · `TOY` proved and *not* carried across ·
`OPEN` not established anywhere.

---

## Q4 · QUANTUM × CONTINUOUS — the theory itself

Everything the program is actually claiming lives here.

| result | status | note |
|---|---|---|
| **the derived measure** — 4D SU(2), Born weight W = A² | `LIVE` **⚠** | **the multiplicities are flat, not the derived profile (0074 §3 vs 0091). ξ/a spans 8 orders across plausible profiles.** |
| transfer operator, spectrum w_j/d_j | `LIVE` | verified 1e−6; convolution by W on class functions |
| RP ⟺ nonneg character coefficients ⟹ OS | `LIFTED` | 0111/0123 — Hilbert space + unitary time |
| positivity from counting | `LIFTED` | 0074 §2, 200 SU(2) countings |
| band-as-budget (sector cost ln N) | `LIVE` | 0108, SU(2) characters |
| why squared | `LIVE` on U(1); **refuted on SU(2)** | 0119/0120, with an exact criterion |
| free graviton; area law α = 0.0242 | `LIVE` | 0073, continuum field |
| induced stiffness p = 0.1549; G = 1/4πp | `LIVE` | 0113 — **factor 20 vs the entanglement route** |
| continuity: no dial, branch decided, ξ/a | `LIVE` **⚠** | structural results stand; the *number* inherits the ⚠ above |
| Lorentz restoration, 2-point and all orders | `LIVE` | 0123/0124, injection-calibrated |

## Q2 · CLASSICAL × CONTINUOUS — GR

| result | status | note |
|---|---|---|
| Newtonian limit, Kepler | `LIVE` | 0031 |
| light bending 4M/b (0.3–0.6%), perihelion 6πM/p | `LIVE` | 0032 — **passes by construction**: the Kerr–Schild channel *is* Schwarzschild |
| PPN β = γ = 1 | `LIVE` | 0059 |
| filter gravity chain: mass = absorption, Newton 1/r, force = code gradient | `LIVE` | lucid 0010–0019 |
| nonlinear completion → Schwarzschild form, hoop bound, T = 2/M | `LIVE` | lucid 0022, 0104 |
| S = A/4G with the ¼; ℓ_P = 2.27a | `LIVE` | 0105 — conditional on the induced identification |
| two-body h² residual | `OPEN` | 0048 residue #5 |
| ambient screening (the one deviation) | **DEAD** | 0059 — killed by LLR 127×, PPN 12500× |

## Q3 · QUANTUM × DISCRETE — the exactly-solvable toy

| result | status | note |
|---|---|---|
| ledger = Born square, gcd(F,N) = \|Σω^{e²F}\|²/N | `LIFTED` | 0074 — the lift is §2's positivity theorem |
| two-ledger theorem | `TOY` (partial lift) | 0077 "run in the Z_N toy"; lucid 0027 gives the SU(2) form via exact zeros |
| action = prequential code length | `LIFTED` (trivially) | 0095 demos on 2D Z_N; the identity is the chain rule |
| innovation capacity = ln N *as a number* | `TOY` | 0095, the 2D Z_N boundary |
| bridge floor n\* = 58 | `TOY` | 0096 — priced *over the ladder* |
| quantized curvature, divisor ensemble | `TOY` | 0055, 0058 |

## Q1 · CLASSICAL × DISCRETE — the Z_N geometry

| result | status | note |
|---|---|---|
| **Λ·V ∈ (2π/N)·ℤ** | `TOY` | 0071/0086 — **the program's only observational route** |
| budget = Stokes: ΣF ≡ hol(∂) mod N | `TOY` | 0071 |
| the even wall (frames indivisible) | `TOY` | 0090 — no continuum shadow (0136) |
| the Lorentzian congruence x² ≡ −1 mod N | `TOY` | 0081 — its own text calls it "the continuum fact in arithmetic dress" |
| the admissible ladder 5, 13, 17, 25, 29, 37 | `TOY` | 0136 — every level passes at the SU(2) tier |
| t_c = log N | `TOY` | 0051 |

---

## Ordered by criticality

**1 · The derived measure's multiplicities** `Q4` — *everything*
downstream of the coupling. Flat counting was a simplification;
0074 §3 derived a peaked profile and nothing since uses it. ξ/a runs
6e9 → 8e17. **Fix first: cheap, self-contained, and it re-prices the
hierarchy.**

**2 · Λ quantisation** `Q1 → Q4` — the only observational route the
program has ever had, and its mechanism is mod-N. On SU(2) the
analogue is a π₁/centre statement. **Until ported, no falsifiable
prediction exists.**

**3 · The Born chain** `Q4` — band-as-budget is SU(2)-native and the
sum rule is derived, but *why squared* is exact only on U(1) and
**refuted on SU(2)**. The quantum tier's central claim is
tier-incomplete.

**4 · Induced G, the factor 20** `Q4` — the only bridge to G, and the
two routes disagree by a field-count-independent 20.1.

**5 · The level's candidate set** `Q1/Q3` — requirement (D). Ladder
is toy-only, so the candidate set is currently *all integers* and
n\* = 58 must be re-priced.

**6 · Two-ledger theorem** `Q3` — the foundation the whole source
ledger rests on, with only a partial lift.

**7 · Classical tests** `Q2` — pass, but by construction; no
discriminating power.

**8 · Two-body residual** `Q2` — the only place the classical sector
could still surprise.

---

## The north star (set 2026-08-26)

Three targets, in order, and everything above is scored against them:

1. **A GR simulation built from this theory.** Q2 largely has it —
   0031/0032 run orbits, bending, precession. What is missing is that
   it be built *from the quantum-continuous theory* rather than from
   the Kerr–Schild channel.
2. **A quantum experiment — start with a double slit.** Q4 has the
   machinery: derived measure, transfer operator with explicit
   spectrum, OS reconstruction, complex composition, the sum rule.
   Nobody has assembled them into a process amplitude.
3. **A falsifiable prediction, preferably vacuum energy.** Blocked on
   criticality item 2.

Method: **filter homo/isomorphisms first.** The filter is ours to
modify; it converts hard physical questions into tractable
engineering ones, and it has done so four times running (the
observation kernel, the code-length reframing, the directional test,
Z_N itself).
