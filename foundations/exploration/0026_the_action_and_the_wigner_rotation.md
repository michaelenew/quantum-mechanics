# 0026 — The action, and the Thomas–Wigner confirmation

The two queued items, delivered together because they are two halves
of one statement: the web's geometric sector now has an **action**
whose equations of motion are the measured laws and whose Noether
charges are the measured monodromies — and the symmetry group whose
charges those are is confirmed to act on web solutions with the
correct Poincaré structure constants, Thomas–Wigner rotation
included. Code: `output/0021_the_action_and_the_wigner_rotation.py`.

---

## 1. The action

The 2+1 precedent (Witten: gravity as Chern–Simons, charges as
holonomies) says the functional form; the web fills it. The
geometric sector is **discrete BF theory**:

```
S[θ, B] = Σ_faces B_f · (curl θ − src_f),      src_f = δᵢ on
                                               participant faces
```

with θ an SO(2) lattice connection and B the budget field. Verified
lattice-exactly — no numerics, every check to machine zero:

- **EOM from varying B**: curl θ = src — flat everywhere except
  participant faces, deficits prescribed. This is the measured local
  law (K = πs, 0019) as an equation of motion.
- **EOM from varying θ**: ∂S/∂θ_e = B_left − B_right, so
  stationarity forces **B constant**: the second EOM *is* the
  conservation law — the budget admits no interior gradients. The
  continuity structure (0020) is not an added axiom of the action;
  it is its other half.
- **Gauge invariance**: under random gauge transformations the
  fluxes, the boundary Wilson loop, and the action's value are
  invariant.
- **The Noether/boundary charge**: the boundary Wilson loop equals
  the enclosed deficit sum exactly (Stokes), and obeys the jump law
  exactly — a source moved within a loop changes nothing; a source
  leaving a subloop subtracts exactly its deficit. **Noether
  conservation on the lattice, with no numerics at all.**

## 2. The action's charges are the measured charges

Promoting the boundary charge to ISO(2) (rotation and translation
parts, composed with the exact iso algebra, expressed in the
developed-loop basepoint frame) and comparing against 0025's
developed-loop measurement on the honest Fisher web:

| w | rot (action / web) | mass moment (action / web) | gap |
|---|---|---|---|
| 0.05 | 0.30285 / 0.29321 | 0.31637 / 0.32019 | ~3% / ~1% |
| 0.20 | 1.09490 / 0.98182 | 1.10549 / 1.17035 | ~10% / ~6% |

At weak strength the action's monodromy **is** the measured charge;
the gap grows faster than linearly with w and is precisely the
mutual screening + halo — **the Fisher web's measured
non-topological dressing over the BF skeleton**. This cleanly
stratifies the theory: the action is the topological core (atoms,
charges, conservation, the exact lattice tier); the information
metric decorates it at finite strength — and the dressing, not the
core, is where 0019's open nonlinear law lives.

## 3. Thomas–Wigner, confirmed on solutions

The boost action on Lorentz-pole solutions is the 3×3 Minkowski
matrix M acting through the slice map S_M (the spatial block of
M⁻¹). Composing orthogonal boosts v₁ = 0.5, v₂ = 0.4:

- **Velocity addition**: |v₃|² = v₁² + v₂² − v₁²v₂² to 10⁻¹².
- **The factorization**: S_M = R(ω)·P with P equal to the *single*
  boost's slice map to v₃ (max deviation 8×10⁻¹⁷) and ω matching
  the Thomas–Wigner formula tan ω = γ₁γ₂v₁v₂/(γ₁+γ₂) to 10⁻¹²;
  reversing the boost order reverses the rotation exactly; the
  Galileo pole's slice maps are identities — abelian, no rotation.
- **The solution-level identity**: the twice-boosted two-defect web
  *equals* the once-boosted, Wigner-rotated web, pointwise
  (max deviation 4×10⁻¹⁶).

So the Lorentz pole realizes the Poincaré composition law on web
solutions with the correct structure constants — boosts close into
boost × rotation, exactly as the algebra whose charges §1's action
carries requires. With 0025's verdict (the symmetry was never a
choice) this closes the loop: **cone derived (0022) → symmetry
forced (0025) → algebra confirmed with its structure constants on
solutions (here) → action written whose charges are the conserved
monodromies (here)**. The geometric sector of the web is, end to
end, the information-theoretic realization of 2+1 defect gravity in
its Chern–Simons/BF form.

## Honest limits

- The lattice action is the abelian (rotation) sector made fully
  variational; the translation charge is verified through the exact
  ISO(2) composition rather than a full ISO(2) lattice BF — writing
  the latter (and its Lorentzian ISO(2,1) version, which would make
  the boost charge variational too) is the natural completion.
- The action governs the topological core only; the halo/screening
  dressing is measured, not yet derived from an extended functional
  (an obvious candidate: BF plus the Fisher-metric kinetic term as
  the dressing's generator).
- Thomas–Wigner is confirmed for the slice-map realization of
  boosts on uniform-motion solutions; transient (kicked) solutions
  compose through the full time-dependent maps, unverified.

## Open

1. **ISO(2,1) lattice BF/CS**: one action carrying mass, momentum,
   boost charge, and angular momentum variationally — the full
   Poincaré multiplet as lattice monodromy.
2. **Derive the dressing**: extend S by the information-metric term
   that generates the screening/halo (target curve: 0019's
   nonlinear measurements; success = the nonlinear law as EOM).
3. **The matter term**: participants as Wilson lines with dynamics
   (the movie coupled to the action) — this is where a force law
   would first become variational rather than scripted.
4. **The quantum tier**: BF/CS quantization is where the amplitude
   sector (the forced U(1) compensator, 0015–0016) should meet the
   action; the 2+1 precedent says the Hilbert space is spanned by
   the very holonomies the charges live on.
