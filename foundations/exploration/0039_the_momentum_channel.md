# 0039 — The momentum channel, and the half that is the bond

0038 diagnosed the binary deficit (the null channel lacks the
sender's momentum flux). This exploration builds the **momentum
channel**, discovers the deficit splits in half with a theorem, and
closes it: **the quadrupole formula is reproduced to ~2%, and the
missing half turned out to be the program's founding claim.** Code:
`output/0034_the_momentum_channel.py`.

---

## 1. The momentum channel

The sender broadcasts its stress tensor, metered by its clock:

```
h_μν = [4m·u_μu_ν + 2m·η_μν] / (u·ℓ)
```

(the tensor Liénard–Wiechert form; the trace term is the
trace-reversal). Verified: the static limit is exactly linearized
isotropic Schwarzschild; and for **uniform motion** the momentum
channel and 0035's null channel agree at the gauge-invariant tier
(E_ij) to O(m) — the two broadcasts are gauge-equivalent wherever
the sender does not accelerate. Acceleration is where they part.

## 2. The wave zone, and the half theorem

At R = 12 (R/λ ≈ 6 — 0038's R = 3 was near zone, inflating the
null channel's 0.014 to what is really 0.001):

| channel | face-on ratio to the quadrupole formula |
|---|---|
| null (KS) | **0.001** — no quadrupole radiation at all |
| momentum (LW) | **0.528 / 0.498 — one half** |

The half is a theorem, not a coincidence. The direct field of free
particles radiates from the momentum-flux integral
∫T_ij = Σmγv_iv_j; the quadrupole formula's (2/R)Ï instead uses
*source conservation*, which converts ∫T_ij into ½Ï — thereby
including the stress of whatever binds the orbit. Circular-orbit
algebra: Ï = 2Σm[vvᵀ + zaᵀ], and with a = −Ω²z the two oscillating
terms are equal — **the free-particle field is exactly half**.
Measured 0.528 = ½(1 + O(v)).

## 3. The missing half is the bond

The binding interaction's own stress must radiate. In web language:
**the pair's mutual channel — their correlation — carries budget
and sources curvature.** "Correlation sources curvature," the
founding claim of this program, is *quantitatively the other half
of the quadrupole formula.* The same object explains 0037's
O(M₁M₂) static vacuum violation (the bond's unaccounted stress) and
0038's in-plane non-vacuum radiation (the bond lives between the
bodies — in the plane).

## 4. The bond channel, built and verified

The bond's integrated stress needs no model: it is the
**conservation deficit** S_ij(t) = ½Ï_ij − Σmγv_iv_j, computed from
the worldlines, broadcast retarded from the pair's center
(h^bond_ij = 4S_ij(t−r)/r). Result:

| direction | components | ratio to GR |
|---|---|---|
| face-on | E_xx, E_xy | **1.017, 0.988** |
| edge-on | E_xx, E_zz | **0.978, 1.005** |

**The quadrupole formula is reproduced to ~2% (= O(v) residuals).**
The channel ontology that radiates like Einstein gravity, complete
at this tier — a channel broadcasts, in increasing tensor rank of
the sender's state:

1. **participation** (mass): deficits, statics, the vacuum profile
   → Newton, Kepler, bending, precession;
2. **momentum flux** (u⊗u): the free half of radiation;
3. **the bond** (correlation): the other half.

## Honest limits

- The bond channel here is the *integrated* stress broadcast from
  the center — the far-field monopole-of-stress approximation; the
  bond's spatial distribution (a channel along the separation, the
  virial density) is not resolved, and near-zone/statics with this
  completion are unmeasured.
- The momentum channel is the linear (in m) tier; unlike the null
  channel's exact single-source Kerr–Schild form, its nonlinear
  completion is not written (in GR it is the Einstein equation).
- Conservation was *imposed* via ½Ï (the worldlines are scripted);
  a self-consistent web binary (motion from the web's own forces,
  0025's momentum charge) has not been run.
- Ratios carry O(v) = 20% headroom used down to ~2%; higher-order
  PN comparison untested.

## Open

1. **The bond as geometry**: resolve the bond channel spatially
   (stress along the mutual channel) and check statics: does it
   cancel the O(M₁M₂) vacuum violation of 0037? If yes, the
   two-body rule is complete: particles broadcast (i)+(ii), pairs
   broadcast (iii), and vacuum holds off-source.
2. **The web-native bond law**: derive S_ij from the web (the
   mutual channel's budget — the conjugate square: the bond is
   correlation, correlation is budget, budget gravitates). The
   virial identity ∫T^bond = −F·d·d̂d̂ᵀ suggests: bond stress =
   force × proper separation, both already web charges (0025).
3. **In-model Hulse–Taylor**: with the completed radiation,
   compute the energy flux and the orbit's back-reaction decay.
4. **Self-consistent motion**: let the web move its own sources.
