# 0038 — The binary test: superposed channels miss the quadrupole formula

0037 named the strongest correspondence test now in reach: orbit two
vacuum-profile sources and compare against GR's quadrupole formula,
coefficient included. Run here. **A sharp, quantified no for the
naive two-body rule — with a precise diagnosis.** Code:
`output/0033_the_binary_test.py`.

---

## 1. The setup

Equal masses M = 0.02 on a circular orbit (a₀ = 0.125, Newtonian Ω,
v = 0.2), each sourcing a covariant retarded null channel with the
vacuum profile w = 2M/(u·ℓ); the two-body metric is the
superposition — the web's natural ansatz, already known (0037) to
violate vacuum at O(M₁M₂) in statics. The GR side is the retarded
quadrupole formula computed *numerically from the same worldlines*
(h = (2/R)·TT[Ï(t−R)], E = −½ḧ — no hand factors), sanity-checked
against the standard pattern (face-on/edge-on = 2.000; circular
polarization on axis).

## 2. The measurement

| direction | web/GR amplitude ratio |
|---|---|
| face-on (orbit axis) | **0.014** — 70× too weak |
| edge-on (in plane) | **0.47** — half strength |

The radiation **pattern inverts**: GR's binary is loudest face-on;
the web's is nearly silent there. On axis the two particles'
direction-jitters cancel pairwise (the dipole cancellation works —
equal masses, opposite positions), but the surviving channel
quadrupole is far below GR's.

The vacuum structure splits the same way: the on-axis wave, tiny as
it is, is a *vacuum* wave (4D Ricci wave 1.9e−8); the orbital plane
carries a large non-vacuum oscillating stress (Ricci wave 4.8e−3,
larger than the Riemann wave there) — **the O(M₁M₂) interaction
zone, now seen radiating**.

## 3. The diagnosis

Linearized GR's moving-source solution is the tensor
Liénard–Wiechert potential h ~ 4m·u_μu_ν/(u·ℓ): the source's
**momentum flux** (u_μu_ν, i.e. m·v_iv_j at order v²) enters the
tensor structure directly. The channel form w·kkᵀ carries mass and
direction but not this sector at the needed order — and the
quadrupole wave *is* an order-v² effect. For a single uniformly
moving source the two agree exactly (both are boosted Schwarzschild
— 0035); acceleration is where they part.

This is the **third independent appearance of the
anisotropic-strength object**: 0024 built its kinematic form (mmᵀ),
0034 relocated its demand to velocity statics, and now the
radiative two-body tier measures its absence at 0.014/0.47. The
scoreboard is now clean:

- **single-source sector: fully Einstein** — statics exact
  (Schwarzschild from the vacuum principle), waves TT, bending,
  precession, Kepler;
- **two-body rule: the program's frontier** — superposition fails
  at O(M₁M₂) in statics and misses the quadrupole formula in
  radiation, pattern inverted.

## Honest limits

- v = 0.2 means O(v) post-quadrupole corrections of tens of
  percent are expected in GR's own pattern — they cannot account
  for 70×.
- The orbits are scripted (both sides identically), not
  self-consistent web dynamics; the comparison isolates the field
  rule, not the motion.
- One geometry (equal masses, circular, R = 3); the edge-on 0.47
  is not yet resolved into pattern-vs-coefficient contributions.

## Open

1. **The two-body fix rule** (now the program's single sharpest
   question): the candidate object is known — channels must carry
   the momentum-flux tensor m·u_μu_ν, not just mass along k. Test:
   replace w·kkᵀ with the tensor LW form 4m·u_μu_ν/(u·ℓ) + gauge
   completion as the *channel pair sector* and re-run this module —
   if face-on lands on 1.0, the missing structure is identified
   web-natively (what does u⊗u mean for a channel? the sender's
   clock ticking into the channel twice — the conjugate square
   again).
2. **The web-native derivation**: whether the fix rule follows
   from the ledger (momentum = mass × proper velocity was already
   a monodromy charge, 0025/0033) — the charge exists; the channel
   must broadcast it.
3. **Energy balance**: once the fix rule lands, the radiated power
   vs the orbit's energy loss (the Hulse–Taylor test, in-model).
