# 0083 — The wedge temperature: Unruh for the free graviton, measured

Fourth stone: **C2** of path C (0070) — is the graviton vacuum
restricted to a half space *thermal*, and at what temperature?
Bisognano–Wichmann says the vacuum seen from a Rindler wedge is
e^(−2πK) with K the boost generator: thermal at inverse temperature
2π per unit rapidity — the Unruh effect. Done-criterion ("thermal form
confirmed/refuted with a temperature"): **confirmed, with the
temperature measured to 1e−4.** Code:
`output/0074_the_wedge_temperature.py`.

---

## 0. A methods note first: the inverse route fails, and why

The obvious attack — reconstruct the modular Hamiltonian matrix
H_mod = ½pM_Ep + ½xK_Ex from the reduced covariances — is **not
usable in double precision**: the deep modular modes carry
single-particle energies ε ≳ 30, their symplectic eigenvalues sit
within 1e−16 of the vacuum floor ν = ½, and the log divergence of
ε(ν) turns rounding into O(10) errors that contaminate the whole
matrix (measured: spurious off-diagonals at 58% of the diagonal).
The forward test needs no such resolution and is the physically
meaningful one anyway: build the lattice **boost operator**
explicitly (site j at distance d_j from the cut weighted d_j, links
weighted d_j − ½), compute its exact β-thermal Gaussian correlators,
and compare *states*, not matrices.

## 1. The reduced state is the boost-thermal state at 2π

Light mass (m² = 0.0025a⁻², region 128 sites, wall ≫ ξ from the cut):
at β = 2π the boost-thermal correlators reproduce the exact reduced
correlators near the cut to **4.3e−5 relative**; entanglement entropy
matches to 0.026%; the leading symplectic eigenvalue to 6e−5. The
half-space vacuum doesn't just resemble a thermal state — at the
measured precision it *is* one.

## 2. The temperature, fitted — and its lattice correction law

Freeing β and fitting it against the exact reduced state:

| m²a² | 0.0025 | 0.01 | 0.09 | 0.5 |
|---|---|---|---|---|
| β*/2π | **0.9999** | 0.9994 | 0.9944 | 0.9708 |
| deviation / m² | — | 0.062 | 0.062 | 0.058 |

The fit is sharp (the residual moves by orders of magnitude across
the minimum), and the deviation from 2π is **linear in m²a² with
coefficient ≈ 0.06** — a pure lattice artifact with a clean continuum
limit. β → 2π as a → 0: the Unruh temperature comes out of the
measurement rather than going in.

## 3. The horizon's location is measurable

Freeing the offset s in d_j = (n−1−j) + s and minimizing the residual:
**s* = 0.5000**. The horizon sits exactly half a lattice spacing
beyond the last site of the region — the natural midpoint between the
kept and traced sites, measured rather than assumed. (The
discretization ambiguities of the boost operator at the edge are
O(a); they are precisely what this fit absorbs, and it absorbs them
at the midpoint.)

## 4. One temperature for the whole graviton

In the free theory the wedge modular structure factorizes exactly
over transverse momenta (transverse translations commute with the
boost), so the 3+1 statement reduces to the per-mode tower — and
every mode sees the same temperature up to its own lattice
correction:

| k⊥ | 0 | 0.1 | 0.2 | 0.4 |
|---|---|---|---|---|
| β*/2π | 1.0002 | 0.9988 | 0.9951 | 0.9811 |

with both TT polarizations contributing identically. The wedge
temperature is **geometric** — set by the horizon, not by the mode —
which is exactly what makes it a temperature rather than a
mode-by-mode accident.

## 5. What path C now has in hand

- C1: the vacuum's entanglement obeys an **area law** with extracted
  coefficient (0082).
- C2: the same reduced state is **thermal at 2π** (here).

Those are the two inputs of the Clausius route (Jacobson's δQ = TdS
needs a horizon entropy proportional to area and an Unruh
temperature) — both now *measured inside the program's own free
graviton vacuum* rather than imported. What is missing for that route
is the coupling: a source term and the first law across the horizon,
which is C3/C4 territory. Also newly live: 0070's "then-do"
conjecture (*is a saturated channel a horizon?*) now has a
temperature to attach — a saturated channel (I → ∞, m → 1/4G) should
be checked for exactly this modular structure in the web-native
variables.

## Honest limits

- **Free theory.** This is the linearized graviton's vacuum; nothing
  here says the interacting ledger vacuum behaves this way.
- The comparison window is the sites nearest the cut (where BW is a
  local statement); the deep modular spectrum — the large-ε modes the
  inverse route couldn't resolve — is untested by construction, on
  both sides of the comparison.
- The k⊥ = 0 line carries an IR regulator mass (0.0025); its entry in
  §4 is really the lightest massive mode.
- The boost operator is one discretization choice; s and the m²a²
  correction law are statements about that choice. The *continuum*
  statements (β = 2π, geometric universality) are the invariant
  content.
- 1D reductions per transverse mode are exact for the free theory
  only; the factorization argument breaks at the first interaction
  vertex.

## Open

1. **C3** — the web-native count: capacity (tangle + coherence)
   crossing the same cut, ledger units, against C1's entropy — the
   discriminator at field level.
2. **C4** — the 1/4, as a renormalized-G confrontation (0082 §4).
3. The saturated-channel/horizon conjecture, now with a modular
   target (§5).
4. Thermality of the *interacting* deconfined phase — the heavy
   version of this stone.
