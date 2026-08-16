# 0058 — Position against the literature: what is rediscovery, what might be new

An orientation pass, not an exploration: no verification module, no new
computation. The question is where this program sits relative to
~100 years of quantum-gravity and ~30 years of information-geometry
work, and specifically whether the repo's "correlation sources
curvature" result is the shape the literature has been looking for.

**Method and its limit.** This is a *scan* — targeted searches and
abstracts, not a systematic survey, and arXiv full texts were not
reachable from the working environment. Statements below about what
the literature does *not* contain are therefore weak claims. Anything
marked "possibly new" means "I did not find precedent," which is a
much smaller claim than "there is none."

---

## 1. Rediscovered, with precedent

These are results the repo derived independently that are established
in the literature. That is not a criticism — independent rederivation
from different postulates is a real consistency check, and several of
these are load-bearing evidence that the machinery is sound. But they
are not new.

| Repo result | Precedent |
|---|---|
| Channel one-form A_μ = w·k_μ has exactly the Liénard–Wiechert field strength; the metric is its square (0040, 0047) | **Classical double copy / Kerr–Schild**: Monteiro, O'Connell & White (2014); Luna et al. Schwarzschild ↔ Coulomb is the standard example. Exact match. |
| Conical defects, δ = 8πGm, no force between masses in 2+1, no local dof (0012, 0020, 0055 §3) | Staruszkiewicz (1963); **Deser, Jackiw & 't Hooft (1984)**; Carlip's *Living Reviews* on 2+1 gravity. Textbook. |
| Curvature concentrated at vertices as deficit angles; flat elsewhere (0012) | **Regge calculus** (1961). |
| Σ deficits = 4π ⇒ Σm = 1/2G, per-defect m < 1/4G | Standard 2+1 mass bound / Gauss–Bonnet. |
| GR as BF theory plus a constraint forcing B = e∧e (0045, 0046, 0050) | **Plebański (1977)**; Freidel–Krasnov; the whole spin-foam program. |
| Simplicity is not a delta function — it is a suppression, imposed weakly (0055 §1) | **EPRL/FK models** impose simplicity weakly via master-constraint/Casimir techniques; Dupuis–Livine holomorphic coherent-state constraints. The *concept* is standard. |
| Continuum limit exists only at a critical point (0056, 0057) | Textbook lattice field theory; Hamber's lattice-gravity program; asymptotic safety. |
| **Graviton massive off criticality ⇒ Yukawa force; massless at t_c** (0056) | **Hamber & Williams, "Newtonian potential in quantum Regge gravity," Nucl. Phys. B435 (1995) 361**: the potential is Yukawa-like with a mass parameter that *decreases toward the critical point where the average curvature vanishes.* Direct match. |
| **Gravitational Wilson loop obeys an area law at strong coupling** (0055 §2) | **Hamber & Williams, Phys. Rev. D 81, 084048 (2010)**, "Gravitational Wilson loop in discrete quantum gravity" — area law for large loops in the strong-coupling region, argued generic. |
| **Newtonian 1/r recovered near the critical point** (0057) | Same Hamber–Williams (1995): potential attractive near the critical point, scaling like mass squared, "more or less the expected classical form in the vicinity of the critical point." |
| P = \|ψ\|² from Fisher-optimal inference (0008) | **Wootters (1981)** — already cited in the repo. |
| Fisher/Bures metric unique up to scale | **Chentsov / Petz** — already cited. |
| Local consistency without a global section = contextuality | **Abramsky & Brandenburger (2011)** sheaf framework; Fine's theorem. |
| Lossy channel = lossless + coarse-grain | **Stinespring dilation** — repo already calls this a theorem, correctly. |

**The Hamber overlap is the significant one.** The entire quantum
lattice arc 0054–0057 — area law at strong coupling, massive graviton
off criticality, Yukawa → massless as the critical point is
approached, Newtonian form recovered there — reproduces the
qualitative phase structure Hamber and Williams established in
simplicial Regge gravity between 1994 and 2010, in a different
discretization (Z_N gauge sector vs. simplicial edge lengths). The
agreement across two unrelated discretizations is genuine evidence
that the phenomenology is robust rather than an artefact of either.
It is also a hard ceiling on the novelty of that arc.

## 2. Same territory, different route: "correlation sources curvature"

The repo's flagged row (0005) asked for **"correlation/entanglement
sources information-manifold curvature."** What 0019/0020 delivered is

```
K(x) = π s(x)     s = participation-strength density
```

proved at the linear tier, coefficient machine-checked (Richardson
1.0002), with superposition and a screening law. The question is
whether this is the shape the literature wants. **It is not — it is a
different and narrower statement**, for three reasons.

### 2.1 The literature's three shapes

- **Jacobson (1995)**: Einstein's equation as an equation of state,
  from the Clausius relation δQ = T dS on local Rindler horizons.
  Full nonlinear Einstein equations; requires a horizon and Unruh
  temperature.
- **The holographic first-law route**: Van Raamsdonk (2010);
  Lashkari–McDermott–Van Raamsdonk (2014);
  Faulkner–Guica–Hartman–Myers–Van Raamsdonk (2014). Linearized *bulk*
  Einstein equations from the first law of **entanglement entropy** of
  *boundary* regions, via Ryu–Takayanagi. This is a duality: the
  entanglement lives in a boundary QFT, the curvature in a bulk that
  is not where the entanglement is.
- **Jacobson (2016)**, entanglement equilibrium: maximal vacuum
  entanglement entropy in small geodesic balls ⇒ Einstein equation,
  directly in spacetime, no holography. Closest in spirit to what this
  repo wants.
- **Matsueda (2013)**, "Emergent General Relativity from Fisher
  Information Metric": Einstein tensor derived from the Fisher metric
  of a statistical-mechanical distribution. The nearest structural
  neighbour to 0019/0020.

### 2.2 Where ours differs — the crux

**(a) The source is participation strength, not a correlation
measure.** This is the decisive gap. `s` is a channel weight in the
metric — how strongly a node participates in the web. Nothing in
0019 or 0020 establishes that `s` is an entanglement entropy, a
mutual information, or any correlation functional. The honest name
for the result is **"participation density sources curvature."**
Calling it "correlation sources curvature" claims the row that was
flagged; what was delivered is a different row. **Closing this — an
explicit demonstration that `s` is (or is monotone in) a correlation
measure — is the single highest-value open item in the repo for
making contact with the RT / Van Raamsdonk / Jacobson literature.**
Until it is closed, comparison to that literature is by analogy.

**(b) G is registered, not derived.** ρ_mass = s/8G follows from
*imposing* δ = 8πGm. The content is K = πs with a derived π; the 8πG
is a units map. Newton's constant is not predicted, and no statement
here fixes it.

**(c) The manifold is the space of knowledge states, and its
identification with physical spacetime is assumed.** 0005 states the
GR analogy as "literal, not metaphor." That identification is doing
heavy load-bearing work throughout and is not independently derived.
This is precisely the step the holographic program *earns* as a
duality rather than assuming. It is the program's largest unpriced
assumption.

Scope, additionally: 2+1, static, linear tier.

### 2.3 What is genuinely attractive about it anyway

The result is **constructive and computable** rather than a
thermodynamic identity or a duality. Jacobson's route gives you the
equation but not a calculational handle; the holographic route needs
AdS and a boundary CFT. K = πs is a pointwise equation on an
explicitly constructed object, verified numerically and proved at the
linear tier, with no AdS, no horizon, and no temperature. If (a) were
closed, that combination would be worth attention on its own terms.

## 3. Possibly new

Ranked by my confidence that precedent is absent — which, per the
method caveat, is not high for any of them.

1. **The screening law δ = πw/√(det A₀)** — a weak channel's deficit
   inside ambient information A₀ is reduced by 1/√(information
   volume) (0019, 0020; uniaxial case derived, general case measured
   to <2e−3). I found nothing resembling this.

   > **CORRECTED BY 0059.** This entry originally claimed the law
   > "predicts a deviation from standard gravity" and called it the
   > best falsification target. That was wrong. 0059 shows the
   > one-body sector is *exactly* Schwarzschild (0037's perihelion
   > excess is GR's own second-order term, 1.0532/1.0205 confirmed
   > against the exact orbit equation), so β = γ = 1 and there is no
   > room for a coupling that runs; and the naive varying-G reading
   > G_eff = G(1−U) is independently excluded by lunar laser ranging
   > by ~127×. The screening is **bookkeeping in the
   > w-parameterization**, not new gravity — consistent with 0020's
   > own note that a constant ambient is flat, and with 0012's exact
   > deficit additivity. It may still be novel as a statement about
   > the parameterization; it is not an observational claim. The
   > real falsification target is the **two-body rule vs
   > Einstein–Infeld–Hoffmann** (0059 §3).
2. **The trace identity tr h(x) = S_total everywhere** (0020, machine
   precision) — the web stores its total strength locally at every
   point; only the traceless anisotropy sector curves. Found no
   precedent.
3. **K(F) = N⁴·|ker F|: the simplicity price as kernel codimension**,
   with the exact 2:1 cost ratio between non-geometric and geometric
   curvature (0055 §1, 0056 §2). The concept of weak imposition is
   standard (EPRL/FK); this exact Gauss-sum evaluation and the
   "geometric = acts in a plane" reading I did not find. **Caveat: the
   abelian BF / Dijkgraaf–Witten literature is large and I searched it
   shallowly — this is the claim most likely to have precedent I
   missed.**
4. **Pf(F) is a function of |F⁺|² − |F⁻|² alone over Z_N** (0057 §4).
   Probably a known finite-field fact in unfamiliar dress. Low
   confidence of novelty.
5. **The bond/virial law, "charges add, bonds multiply," the braiding
   phase ω^(n_a n_b)** (0040–0042). Not searched. Unassessed — flagged
   so it is not mistaken for a cleared item.

## 4. On the speed of the graviton thread

The program's internal evidence for novelty has been that the arc
resolved fast and without a fatal flaw. That reasoning should be
discounted, for a specific reason: **the results that fell into place
fastest are precisely the ones with the strongest precedent.** The
Yukawa-to-massless transition, the Wilson-loop area law, and the
Newtonian potential near criticality are the three headline results
of Hamber's Regge program. A thread moves quickly and cleanly when it
is landing on correct, well-mapped terrain. That is strong evidence
the machinery is sound and weak evidence that it is new.

The "few knobs" property cuts both ways as well. A theory with no free
parameters that reproduces known results is a real achievement of
internal consistency. But **every quantitative success in this repo is
a recovery of a number already known** — π, 1/(4πt), 8πGm, TT
polarization at 0.977, light bending, perihelion advance. None is a
number the program produced *before* the answer was available to
check against. A framework that has only ever been asked to reproduce
can feel inevitable without having been tested.

## 5. What would move this from rediscovery to result

Three concrete targets, in the repo's own terms:

1. **Close the correlation gap** (§2.2a): show `s` is a correlation
   measure. This converts an analogy into the equation the literature
   has been after, and it is the difference between "an
   information-geometry model of gravity" and "correlation sources
   curvature."
2. **Make the screening law quantitative and falsifiable** (§3.1). If
   the local coupling really goes as 1/√det A₀, G varies with ambient
   information density — a modified-gravity claim with observational
   targets. It can fail, which is what makes it worth having.
3. **Derive t, or N.** The graviton is massless only because t is
   tuned to t_c by hand. Anything that *fixes* t predicts a nonzero
   graviton mass, which is directly bounded by LVK observations. Same
   for the level N, currently free.

## Honest limits of this document

- Scan, not survey; abstracts and search summaries, not full texts
  (arXiv was not reachable from the environment). The Hamber claims
  rest on two independent search summaries of the same abstract plus
  the PRD listing, not on the papers themselves — **they should be
  read directly before this document is relied on.**
- Absence-of-precedent claims in §3 are weak by construction.
- §5's targets are judgements about research direction, not results.
