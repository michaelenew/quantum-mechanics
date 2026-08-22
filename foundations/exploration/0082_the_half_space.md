# 0082 — The half space: the graviton's zero-point entanglement

Third stone down the queue: **C1** of path C (0070) — the entanglement
of the free graviton's vacuum across a flat spatial cut. 0063's
linearized theory is two TT oscillator modes per momentum, so the
ground state is Gaussian and the reduced state of a half space is
exact covariance-matrix algebra: X = K^(−1/2)/2, P = K^(1/2)/2,
symplectic spectrum ν = √eig(X_A P_A). Done-criteria (area law
measured, coefficient extracted): **met**. Code:
`output/0073_the_half_space.py`.

A framing note first. This stone deliberately computes the *standard*
side of the program's sharpest internal disagreement. 0067 found that
curvature couples to the **tangle** at pair level, where the
RT/Jacobson tradition couples it to **entropy**. C1 establishes what
the entropy side actually is in this theory's own vacuum, so that C3
(the web-native capacity count) and C4 (the 1/4) can be a real
confrontation instead of a shrug. Finding the standard structure
present and correct here is the *useful* outcome — the difference, if
the program earns one, must then live where 0067 says it lives.

---

## 1. The machinery, anchored on CFT

Geometry: transverse torus (N⊥² momenta), open chains of length L
along the cut normal, region = half chain — one cut face, no zero
mode. Anchor: the half-chain entropy of a massive 1D chain must obey
the c = 1 law S = −(1/6)ln m + const in the window 1/L ≪ m ≪ 1.
Measured at L = 2048: slope **−0.16639** against −1/6 = −0.16667 —
0.2%. The instrument is certified before it is pointed at anything.

## 2. The area law and its coefficient

Nearest-neighbor stencil, L = 64, N⊥ = 8 → 64:

| N⊥ | 8 | 16 | 32 | 64 |
|---|---|---|---|---|
| S/A | 0.029429 | 0.025106 | 0.024360 | 0.024258 |

converging monotonically; paired extrapolants agree to 0.46%:

```
α_scalar = 0.0242 per polarization      S_graviton/A = 2α = 0.0484
```

(natural units of the lattice spacing; two TT polarizations, exact in
the free theory). External anchor, **from memory and flagged as
such**: Srednicki (1993) found S = 0.30 M²R² for spheres, i.e.
0.30/4π ≈ 0.0239 per unit area under his radial regulator — the same
scale as our flat-cut 0.0242, consistent with weak scheme dependence
among nearest-neighbor-type regulators. The citation should be
checked directly before this comparison is relied on.

## 3. The gapless channel signs its work

At fixed N⊥ the coefficient grows with L:

```
d(S/A)/d ln L × N⊥²  =  0.1638      (c = 1 CFT: 1/6 = 0.1667)
```

The k⊥ = 0 graviton line through the cut is a massless 1D mode — a
c = 1 CFT — and it deposits exactly its central charge as a
(1/6)ln L / N⊥² subleading term. This is 0077's gapless graviton
channel showing up a third way: first as μ ∝ ε in the MK spectrum,
then as the heat-kernel fixed structure, now as a central charge in
the vacuum's entanglement. Three instruments, one massless thing.

## 4. The coefficient is not universal — and that is the finding

The program's own stencil (0063's central differences) factorizes
exactly — S_cd(L) = 2·S_sub(L/2), the doubler branches are literal
sublattices (verified to 1e−9) — and its area coefficient converges
to **0.0482**, ratio 1.99 against the nearest-neighbor 0.0242. The
z-doubling contributes exactly 2; the transverse rearrangement
(4 light points, shallower dispersion) empirically nets ≈ 1; the
total being exactly 2 is *not* proven, just measured at 1.99.

So the area-law coefficient depends on the regulator, as a
UV-divergent object must. This is the standard **species problem** of
semiclassical gravity arriving in this program right on schedule: you
cannot bare-match S/A to A/4G because the left side knows about the
cutoff and field content. The known resolution shape is Sakharov's —
the same UV modes that produce the entanglement also renormalize G,
and the *matched pair* is scheme-independent. Consequence recorded
for **C4**: the 1/4 confrontation must be run as a renormalized-G
statement, never as a bare coefficient match. A mismatch at bare
level is not a finding; agreement at bare level would be an accident.

Massive control: S/A = 0.0244 / 0.0196 / 0.0137 at M² = 0, ¼, 1 —
monotone, the vacuum localizes as the correlation length shrinks.

## Honest limits

- **Free theory only.** This is the entanglement of 0063's linearized
  graviton, not of the interacting ledger vacuum (0074+). The
  deconfined 4D measure's entanglement — where the topological-order
  alternative of path C's own footnote lives — is untouched.
- A flat cut on a lattice is not a horizon; no statement about
  thermality is made here (that is C2, via the modular Hamiltonian).
- The Srednicki number is quoted from memory, flagged in module and
  doc alike.
- The graviton = two massless scalars identification is exact for the
  free TT sector and only there.
- Dirichlet walls at the chain ends contribute O(1/L) edge effects;
  the L-stability scan bounds them but they are present.

## Open

1. **C2 — thermality**: modular structure of this same reduced state
   vs the lattice boost (Bisognano–Wichmann). Still Gaussian, next
   easiest in path C.
2. **C3 — the web-native count**: tangle + coherence capacity
   crossing the same cut (0068's decomposition), in ledger units —
   the other side of the discriminator, same geometry.
3. **C4 — the 1/4**, now explicitly as a renormalized-G confrontation
   (per §4).
4. The interacting version: entanglement of the deconfined ledger
   phase (ties to 0071's topological finding).
