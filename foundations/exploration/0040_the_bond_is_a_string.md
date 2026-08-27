# 0040 — The bond is a string, and it is the anti-string

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

0039 found the quadrupole formula's missing half: the **bond** —
the pair's correlation, broadcast as a source — supplied there as a
numerical conservation deficit. This exploration asks what the bond
*is*. The answer is a closed form, confirmed twice by independent
routes, with a surprise in its equation of state. Code:
`output/0035_the_bond_is_a_string.py`.

---

## 1. The virial law: tension = force

The conservation deficit closes exactly:

```
S_ij = −(m₁m₂/d)·n̂ᵢn̂ⱼ = −(F·d)·n̂ᵢn̂ⱼ
```

verified to 1e−8 against the numerical deficit at three phases.
**The bond's integrated stress is a pure tension along the line
joining the participants, of magnitude force × separation.**
(0039's 2% residual is identified: the γ in the kinetic tensor,
γ − 1 = 0.021 at v = 0.2.)

## 2. The same object, measured from the field

The virial route uses the *particles' motion*. The independent
route uses the *field's own stress*
t_ij = (1/4πG)[∂_iΦ∂_jΦ − ½δ_ij|∇Φ|²]. In prolate spheroidal
coordinates with the two masses at the foci, the cross-term
integrals collapse to two universal numbers:

| integral | measured (N = 200/400/800) | meaning |
|---|---|---|
| ∫(ξ²+η²−2)/(ξ²−η²)² | **1.000000** | trace — the exact calibration |
| ∫(ξ²η²−1)/(ξ²−η²)² | **0.000000** | longitudinal — the result |

The vanishing longitudinal integral is exactly the statement

```
∫ t_ij d³x = −(m₁m₂/d)·n̂ᵢn̂ⱼ
```

— *identically* the virial bond. **The bond is not an add-on to the
theory: it is the field between the participants**, and that
field's integrated stress is a stretched string. (The trace
identity ∫∇Φ₁·∇Φ₂ = 4πG²m₁m₂/d is classical; the tensor structure
is what the geometry needed.)

## 3. The anti-string

Two numbers now characterize the bond as a string of length d:

- **tension** T = m₁m₂/d² — *exactly the gravitational force*;
- **energy density** μ = ∫t₀₀/d = −m₁m₂/d² — *the binding energy*.

So **μ = −T exactly**. Since a straight string's deficit angle is
4πG(μ+T) — verified here on four string types with the 0033 charge
reader:

| string | μ, T | deficit measured | predicted |
|---|---|---|---|
| cosmic string | μ = +T | 0.25129 | 0.25133 |
| mass line | T = 0 | 0.12564 | 0.12566 |
| strut | μ = 0 | 0.12564 | 0.12566 |
| **bond** | **μ = −T** | **0.00000** | **0.00000** |

— the bond has **zero conical deficit while carrying the entire
binding energy**. The theory's two string species are the two
extremes of one equation of state:

> **cosmic string (μ = +T): all deficit, no attraction.**
> **bond (μ = −T): all attraction, no deficit.**

And the web reading is exact: **the bond carries budget but no
holonomy charge** — invisible to the charge reader, precisely as
*correlation* (rather than participation) must be. Participation
curves the web and is read by loops; correlation binds and
radiates but leaves no monodromy. The two-tier structure of P2,
appearing here as two string equations of state.

## 4. In-model Hulse–Taylor

Radiated power of the completed binary (momentum channels + the
closed-form bond), from the Isaacson flux of the measured wave
integrated over a sphere:

| | luminosity |
|---|---|
| GR quadrupole formula | 4.1943e−5 |
| **web (virial bond)** | **4.1947e−5 — ratio 1.0001** |
| web (γ-corrected bond) | 4.1091e−5 — ratio 0.980 |

**The luminosity is Einstein's to 0.01%** at the order the
quadrupole formula is defined; the 2% spread between the two bond
definitions is γ − 1 = v²/2, the first post-Newtonian correction
the formula does not itself capture — the honest accuracy floor of
this comparison. The implied inspiral for the model binary
(tight: v = 0.2): Ḋ = −1.3e−2, Ṗ/P = −0.31 per orbit.

## Honest limits

- The field-stress integral and the virial identity are classical
  computations (the trace identity certainly is; the tensor
  structure may be too — I cannot check the literature from here).
  What this exploration contributes is the *identification*: this
  object is the web's mutual channel, and it is quantitatively the
  radiation's missing half.
- The bond is characterized by its **integrated** stress; its
  spatial profile is the field's, not a literal line source. The
  string picture is exact for the integrated quantities (which is
  what the far field and the deficit see), not a claim that the
  stress is delta-localized on the segment.
- μ = −T uses the Newtonian field energy; at higher order the
  energy is not a tensor and the statement is gauge-dependent.
- The deficit test is on the linearized (μ, T) string metric, an
  independent model check, not a measurement of the actual
  two-body field's holonomy.

## Open

1. **The static two-body**: does the bond's field cancel 0037's
   O(M₁M₂) vacuum violation? The bond is the interaction stress the
   superposition omits, so this should now be a computation, not a
   question — and it would complete the two-body rule
   (participants broadcast (i)+(ii), pairs broadcast (iii),
   vacuum holds).
2. **The web-native bond law**: derive T = F from the web instead
   of importing it — the bond's tension is the mutual channel's
   own budget, and *force = tension* is the statement that a
   channel pulls with what it carries. The conjugate square
   suggests the check: bond tension ↔ trust, participation
   deficit ↔ distribution.
3. **N bodies**: bonds are pairwise, so the ledger is Σ over pairs
   — check that N-body radiation is the pair sum (it should be,
   by linearity of the virial identity).
4. **The quantum tier of the bond**: a string with μ = −T carries
   no deficit, hence no quantized 2πn/N charge (0027) — so the
   bond is *not* quantized like participation. What, then, is its
   quantum? (Candidate: it is entanglement, and its quantum is the
   ledger's ½ — the correlation tier, not the charge tier.)
