# 0075 — The tension spectrum: A3's first half, where Barrett–Crane failed

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.

The graviton-propagator test (0070's A3) splits in two: a **tensorial
half** — which modes does the interacting measure propagate, with what
hierarchy — and a **momentum half** (the 1/k² structure), which needs
a 4D complex. The tensorial half is exactly where Barrett–Crane's
propagator failed, and it is exactly computable on the healed weight.
Code: `output/0067_the_tension_spectrum.py` (0.9 s).

---

## 1. The instrument

For a class-function weight W = Σ c_R χ_R on Spin(4), a chain of
plaquettes propagates the mode R with per-step transfer eigenvalue

```
t_R = c_R / (d_R c₀),      tension = −ln t_R
```

by Schur's lemma (E[R(U)] = (c_R/d_R c₀)·Id). The orientation-average
identity behind it — ∫dg χ(U₁gU₂g⁻¹) = χ(U₁)χ(U₂)/d — is verified
numerically (spin 1, 10⁻³ by quadrature over SO(3)).

## 2. The spectrum of the healed weight

| mode | dim | mass (s₀ = 0.75) | mass (s₀ = 1.5) |
|---|---|---|---|
| (1,0) | 3 | **1.100** | **1.122** |
| **(1,1)** | **9** | **1.201** | **1.423** |
| (2,0) | 5 | 1.611 | 1.632 |
| (2,1) | 15 | 1.725 | 2.062 |
| (2,2) | 25 | 1.879 | 2.384 |
| (3,3) | 49 | 2.452 | 3.476 |

A finite, positive, **rising** spectrum — every mode damped, higher
spin damped more. The ordering is bin-scale-stable; the numbers are
not (honest profile dependence).

## 3. The graviton multiplet leads the simple tower

Within the **balanced (simple) tower** — the sector the simplicity
structure selects, and the sector gravitons live in —

> **(1,1) is the lightest excitation, strictly, at both scales**
> ((1,1) < (2,2) < (3,3)) — and (1,1) of Spin(4) is the
> 9-dimensional symmetric-traceless SO(4) tensor: the covariant
> graviton multiplet.

The derived radial profile supplies exactly the **high-spin damping
Barrett–Crane lacked**. Measured honestly alongside: the unbalanced
(1,0) — the connection/2-form multiplet — interleaves *below* (1,1)
by 0.10–0.30 in mass at the bare one-plaquette chain. That is the
measured job description for vertex-level simplicity (intertwiners,
the budget), which one plaquette does not have. A pointer, not a
hidden failure.

## 4. The two failure modes, for contrast

- **Barrett–Crane** (bare balanced delta): t(j,j) = 1 for *every* j —
  all balanced modes massless and degenerate, no hierarchy, no
  damping. The known high-spin pathology, restated as a flat
  transfer spectrum.
- **The naive 0073 lift**: t(1,0) = −0.055 — an undefined (complex)
  tension. The sign disease, restated as an unphysical spectrum.

Of the three candidate weights, **only the Born square has a physical
spectrum**: finite, positive, hierarchical.

## 5. What this is and is not

These are 1D-chain tensions — per-plaquette decorrelation rates by
representation, the nonabelian rep-resolved analogue of the jitter
tension f(N) = φ/P. They are **not** 4D masses: 0071's lesson stands
(low dimensions confine for everyone; four is where deconfinement
begins). A3's momentum half needs the 4D complex, and this spectrum
supplies its sector-resolved input: the 4D question is now **which
multiplet deconfines first**, and the candidate list is ordered with
the graviton multiplet leading the simple tower.

## Honest limits

- One plaquette, one chain: no intertwiners, no vertex assembly, no
  spatial momentum. Euclidean Spin(4), integer bins.
- The bin scale s₀ moves the numbers (not the ordering); the
  coherent-state unbinned amplitude (0074 open 3) is the refinement.
- The (1,0)-below-(1,1) interleaving is a bare-chain fact; whether
  vertex constraints lift it is the next computation, not an
  assumption.
- BC here means the bare balanced delta with d² weights — the
  simplest representative of its class, not the full BC vertex.

## Open

1. **The 4D sector-resolved deconfinement** (A3's completion / A4):
   which multiplet deconfines first under the healed weight — the
   nonabelian version of 0071's self-duality argument, now with an
   ordered candidate list.
2. **The vertex**: intertwiners/budget at a true 4-valent vertex —
   does the (1,0) interleaving lift?
3. The coherent-state amplitude (unbinned n_j).
4. Standing: Λ1, C1, the arithmetic-branch pass, the sign-problem
   toy packaging.
