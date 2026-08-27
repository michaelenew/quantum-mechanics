# 0047 — The derived channel: the rule is the functional's Green function

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0046's four fronts, three moved. The matter-variation front closes
with a derivation; the closing turns up the principle that unifies
the bond and the string's tension; and one measured surprise plus
one honest artefact are recorded on the way. Code:
`output/0042_the_derived_channel.py`.

---

## 1. The channel rule, derived

Vary the functional (0046's tetrad action + matter terms):

- **A-sector**: □A = j, whose retarded Green-function solution is
  A = q·u/(u·ℓ) — the Liénard–Wiechert potential, which *is* the
  web's channel (0045's 1e−8 identity, re-verified);
- **e-sector at linear order**: □h̄ = −16πT, whose solution is the
  tensor Liénard–Wiechert — which *is* the momentum channel
  (0039's ansatz, now δS).

**The sender-clock normalization u·ℓ is the Jacobian of the
retarded projection — derived, not chosen.** Two standing opens
close at once: 0035's "clock principle" (which clock meters a
channel) was never a choice; and the element-vs-system clock fork
dissolves — the functional says *integrate the Green function over
the conserved source*, and there is no per-element decision left to
make.

## 2. Conservation is the operative principle (measured)

Wave-zone (R = 12) Ricci-wave / Riemann-wave ratios:

| source | face-on | 45° |
|---|---|---|
| **conserved** (LW + bond) | **0.014** | **0.042** |
| non-conserved (LW only) | 0.067 | **0.909** |

**The Green-function field is vacuum off-source iff the source is
conserved** — and the 45° direction, where the bond radiates
(0038's in-plane finding), is exactly where the unconserved field
fails hardest. This is the unification: **the bond (for the binary)
and the internal tension (for the string) are the same
conservation-completing term**, read at two source types. It also
retro-diagnoses 0035's ~20% radiative admixture: measured with the
nearest-point rule, i.e. with a non-conserved effective source; the
conserved compact source is clean to 1–4%.

## 3. The string's tension (partial, with a named artefact)

Integrating tensor-LW elements over the wiggling string *with* the
Nambu–Goto tension term (T ~ ẋẋᵀ − x′x′ᵀ):

| shape | u⊗u only | with tension |
|---|---|---|
| traveling | 1.14 | **0.46** |
| standing | 1.13 | **0.53** |

The tension term **halves the admixture** — conservation acting.
But a truncated open string breaks conservation at its *ends* (the
ratio does not converge with window size: 1.14 at L = 8, 1.18 at
L = 12 for the u⊗u case; the sliding-window variant was worse
still, 1.82 — both artefacts identified during the session), so
the **Vachaspati test — exact traveling-wave silence — stays open
pending a closed-loop source.** Recorded, not claimed. The
prediction is sharp: a closed loop is compact and exactly
conserved, so its traveling modes should go silent and its standing
modes radiate.

## 4. The operator square

B = e∧e read on the charge lattice: the budget operator is the
symmetrized square of the frame operator, and its holonomy spectrum
ω^(n_a n_b) is exactly 0042's measured bond table (N = 5, all 25
states); in 2+1, B = e is linear and the spectrum is the additive
n. **"Budget = frame squared" now holds at every tier the program
has**: metric (0046's exact tetrad), charges (0041/0042's
add-vs-multiply), action (0046's B = e∧e), operators (here).

## Honest limits

- §1's derivation imports the standard retarded Green functions of
  the wave equation; the web-side content is the identification
  (channel ≡ LW, momentum channel ≡ tensor LW) — measured, and the
  Jacobian reading of u·ℓ.
- §2's "iff" is two points each way, at one binary configuration;
  the conserved side's residual 1–4% contains O(v) and O(h²)
  pieces not separated.
- §3's string source uses the leading-order Nambu–Goto stress in a
  non-conformal parametrization; O(A²) gauge terms enter at the
  second harmonic and are not isolated. The end-effect diagnosis
  is by non-convergence in L, not by an explicit end-field
  computation.
- §4 is definitional given 0042's operator; its content is the
  cross-tier consistency, not a new measurement.

## Open

1. **The closed loop**: a compact, exactly conserved string — the
   clean Vachaspati test (traveling silence, standing radiation)
   and the honest replacement for truncated strings. The machinery
   exists (element integration + tension term); the geometry is a
   circle.
2. **The lattice Palatini** (carried from 0046): e on 0030's
   lattice, B = e∧e imposed, torsion equation verified.
3. **The 1–4% residual**: separate O(v) from O(h²) in the
   conserved binary's vacuum residual — the first would be
   post-quadrupole source structure, the second the genuine
   next-order iteration.
4. **The loop of derivations is nearly closed**: postulates →
   metric (Chentsov) → cone → Lorentz → functional (0046) →
   channel rule (here, from the functional) → everything measured
   since 0035. The remaining underived steps are the functional's
   own normalization (κ) and the lattice construction — worth a
   consolidation pass that states the full chain end to end with
   each link's evidence.
