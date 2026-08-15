# 0025 — Noether on the web: the charges, and the choice that's not a choice

Before the composition experiment, the symmetry audit — as requested,
run through Noether's lens. The web has no action functional yet, so
Noether's theorem appears here in its operational form: for each
symmetry, find the conserved object and *measure* its conservation.
The results shore up the web's essence in exactly the way hoped —
the charges turn out not to be integrals of anything — and the
symmetry inventory does say the Lorentz/Galileo verdict plainly,
three independent ways. Code: `output/0020_noether_on_the_web.py`.

---

## 1. The symmetry inventory

| symmetry | status | conserved object / consequence |
|---|---|---|
| space translation | exact | momentum = the monodromy's drift rate (§2) |
| time translation | exact | energy = mass = the monodromy's rotation part (§2) |
| rotation | exact | (angular momentum needs spacetime loops — open) |
| **dilation, z = 1** | **exact, field-level** | scale-freeness; no-pair-force as its Ward identity; mass dimensionless |
| dilation, z = 2 | **broken by the cone** | (deviation 0.08 vs z = 1's 10⁻¹⁶) |
| time reversal | broken by retardation | the web's arrow (deviation 0.144 mid-transient; 0 in statics) |
| Galilean boost | static sector only | fails in the signal sector (§3) |
| Lorentz boost | exact at the Lorentz pole | passes both sectors (§3 + 0024) |

Three measured highlights:

- **Dilation is exact at field level** — g_λ(λx, λt) = g(x, t) to
  10⁻¹⁶ including the causal sector. The web has no length scale;
  the measured d-independence of atoms (0020's no-pair-force) is
  this symmetry's Ward identity, and mass (the deficit) is
  **dimensionless** — as it is in 2+1 gravity. Crucially the cone
  pins the scaling weight: x and t must scale *together* (z = 1);
  the Schrödinger scaling (t → λ²t, the symmetry of massive
  Galilean physics) breaks the field outright.
- **Time reversal is broken by the update rule** (retarded ≠
  advanced mid-transient, exactly equal in statics): the web
  carries an intrinsic arrow — the field-theory echo of the census
  chirality (0017).
- **The mass-broadcast test**: at the ether and Galileo poles the
  channel trace is exactly w everywhere — mass is a broadcast
  scalar, inert and universal: a **central charge**. At the Lorentz
  pole the trace is direction-dependent (0.469 vs 0.300 at w = 0.3,
  v = 0.6): mass mixes into the motion sector. This is Bargmann's
  dichotomy — Galilei needs mass as a central extension; Poincaré
  puts it inside energy-momentum — visible in the field components.

## 2. Charges are holonomies

The new instrument: full loop *development* — both the rotation and
translation parts of the ISO(2) monodromy. Calibrated:

- **Rotation part = the mass** (0.77240 vs δ = 0.77247, at every
  apex position).
- **Translation part = the mass moment**: |τ| = 2 sin(δ/2) × proper
  basepoint-to-apex distance, verified at three positions to <2%
  (exact at calibration: 0.85905 vs 0.85901).
- Under interior motion: the rotation part is conserved to 3×10⁻⁵
  (**energy conservation**), and the translation part drifts
  *perfectly linearly* (bend/step = 0.000) at rate
  2 sin(δ/2)·√(1+w)·|v| — matched to 0.02%: **momentum = mass ×
  proper velocity, read off the monodromy's drift.** (The moment is
  metered in the web's own distance — even the Noether charge uses
  the information metric as its ruler.)

The essence-shoring point, stated plainly: **the web's conservation
laws are not volume integrals of local densities. They are
quasi-local monodromies** — the 2+1 ADM structure — conserved
because of the causal cone: a loop's charge cannot change until
news crosses it (0020's jump law, now recognized as Noether
conservation). Energy = rotation part, momentum = translation
drift, mass moment = translation part. Holonomy is not just the
program's favorite observable; it is where the charges live.

## 3. Michelson–Morley in-model: the choice that's not a choice

The decisive structural fact: **signals ride the derived cone**
(0022) — speed c in the web frame, *independent of the update
rule*. So no choice of pole can change signal kinematics; the only
thing that can respond to motion is the **length standard** — the
metric that defines "equal arms." Round-trip anisotropy
T_∥/T_⊥ for a co-moving interferometer with arms held at fixed
proper length, over the baseline family I + (β−1)v̂v̂ᵀ at v = 0.6:

| β | T_∥/T_⊥ |
|---|---|
| 1 (ether *and* Galileo poles) | 1.250000 (= γ) |
| γ | 1.118034 |
| **γ²** (the Lorentz pole's baseline) | **1.000000** |
| γ³ | 0.894427 |

- The **Galileo pole fails**: its uniform-motion covariance (0024)
  was confined to the static sector. Its baseline is I, so its
  signal sector carries an O(v²) compass — a co-moving
  interferometer reads |v|. Extrapolated channels cannot fix this,
  because the cone is derived, not chosen.
- The **ether pole fails in both sectors** (0023).
- The **null occurs at β = γ² exactly and uniquely** — which is
  precisely the boosted baseline the Lorentz completion was forced
  to carry (0024's necessity result).

**The choice that's not a choice, three ways:**

1. *Operationally* (this section): relativity principle + derived
   cone ⇒ the length standard must contract ⇒ Lorentz, uniquely
   within the baseline family.
2. *Algebraically* (§1): massive Galilean physics is
   scale-invariant only at z = 2 (Schrödinger); the web's cone
   forces z = 1 and its dilation symmetry is exact — the Galilean
   option is algebraically incompatible with symmetries the web
   already has. Poincaré + z = 1 dilations coexist without strain.
3. *By the central charge* (§1): Galilei requires mass central —
   the trace identity is exactly that broadcast, and it is a
   feature of the poles that *fail*; the pole that passes is the
   one where mass mixes into motion, as Poincaré demands.

(One-way anisotropy is synchronization-convention dependent, here
as in physics: only round trips are invariant statements — the
model reproduces even that subtlety.)

## Honest limits

- No action functional exists yet, so "Noether" here is the
  operational correspondence symmetry ↔ measured conserved object,
  not a variational theorem; building the action that generates
  these charges (and makes the z = 1/Bargmann argument a strict
  no-go theorem) is the natural formalization step.
- The momentum law is measured for quasi-static interior motion;
  its retarded-sector version (charge flow during transients) is
  qualitative (the jump law) not quantitative here.
- The MM uniqueness is within the one-parameter baseline family
  β; the 0024 isometry argument makes β = γ² natural beyond the
  family, but a general uniqueness proof isn't given.
- Angular momentum and the boost charge proper (centroid law) need
  spacetime holonomy — the (2+1)-dimensional monodromy — not yet
  implemented.

## Open

1. **The composition experiment** (queued, now with sharpened
   stakes): two boosts at the Lorentz pole should produce the
   Thomas–Wigner rotation — landing the last Poincaré structure
   constant; the Galileo pole is already excluded, so this becomes
   a *confirmation* of the algebra rather than a discriminator.
2. **The action**: a variational principle whose Noether charges
   are the measured monodromies (Chern–Simons-like, where charges
   are naturally holonomies — the 2+1 gravity precedent says this
   is the right functional form).
3. **Spacetime monodromy**: implement development for loops in
   (x, t) to read the boost charge and angular momentum; check the
   full Poincaré algebra of charges.
4. **The arrow**: connect the retardation-broken T (measured here)
   to the census chirality (0017) — same arrow, two tiers?
