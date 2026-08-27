# 0001 — The gravitational which-branch experiment

The user's thought experiment, taken seriously, worked through, and resolved.
It turns out to be a sharp probe of **P2** (the actionable/correlational
firewall) and it forces a commitment the framework had so far avoided.

## The setup, restated

A closed sphere of mass `M` carries two guns at opposite ends and one hole
facing us. The guns fire back-to-back, so momentum conservation entangles the
pair. One particle may exit the hole; its partner is then necessarily on the
far side, inside, and is absorbed by the wall.

Momentum bookkeeping (worth doing, because it is what makes the two branches
gravitationally distinct at all):

| | apparatus mass | apparatus momentum | subsequent motion |
|---|---|---|---|
| **exit** | `M − m` | `−p` (wall absorbed the partner) | tuned to circular orbit at radius `R` |
| **no exit** | `M` | `0` (recoils cancel, both absorbed) | radial free fall toward us |

Both branches start at `R`. The exit branch stays at `R`; the no-exit branch
falls. So the branches separate *positionally*, and the position difference
swamps the mass difference `m` in the gravitational signal almost immediately.
That is a strengthening of the original argument, not a weakening: the user
motivated the effect via the mass difference, but the dominant discriminator is
the trajectory difference.

## Correction 1 — the deadline is 0.177 `T_orb`, not 1 `T_orb`

The protocol says *wait one orbital period, then read the gravimeters*. But the
no-exit branch is in radial free fall, which is the degenerate ellipse of
semi-major axis `R/2`. By Kepler III its period is `T_orb·(1/2)^{3/2}`, and
infall is half of that:

```
t_fall / T_orb = ½ · 2^{−3/2} = 1 / (4√2) ≈ 0.1768
```

Verified three independent ways (Kepler III, the closed form
`t_fall = (π/2)√(R³/2GM)`, and direct quadrature of `∫dr/v(r)`) to 11 digits
in `output/0001`. It is a **pure number, independent of `R` and of both
masses** — a small piece of elegance the setup didn't advertise.

So the no-exit branch has already collided with us at `0.177 T_orb`. Waiting a
full period is 5.7× too long; the experiment as specified self-destructs before
the measurement. The protocol has to run inside `t < T_orb/(4√2)`.

This also disposes of the user's "wait long enough and we learn by
non-collision" observation — correct, but it is not a subtle information-free
inference. Non-collision at `0.18 T_orb` is a *macroscopic dynamical fact about
our own laboratory*, which is about as coupled to us as anything can be.

## Correction 2 — "informationally isolated" and "gravitationally detectable"
## are contradictory premises

This is the resolution, and it is quantitative.

Two different times matter and the argument silently conflates them:

- **`t_ent`** — when the gravimeter's *quantum phase* becomes
  branch-distinguishable. Branch-dependent interaction energy
  `ΔU = GμM·δr/r²`, accumulated phase `Δφ = ΔU·t/ħ`; set `Δφ = 1`. This is the
  Bose / Marletto–Vedral gravitational-entanglement criterion. **This is when
  which-branch information has left the system.**
- **`t_read`** — when the branch-dependent acceleration `a = 2GM·δr/r³` produces
  a displacement above the free-mass standard quantum limit
  `√(ħt/μ)`, giving `t_read = (4ħ/μa²)^{1/3}`. **This is when we can act on it.**

The paradox needs `t_read < t_ent`: a window in which we can read the branch
while the superposition is still intact. Their ratio is startlingly clean:

```
        t_read              ⎛ G M μ² δr ⎞^(1/3)
  𝒩  =  ──────  =  ⎜ ───────── ⎟
        t_ent               ⎝    ħ²     ⎠
```

**The distance `r` cancels exactly.** Both times scale as `r²`, so backing the
gravimeter off buys precisely nothing — verified over three decades of `r` in
`output/0001` (𝒩 constant to 9 digits). There is no "far enough away to stay
isolated" configuration. That is the sharpest single statement here.

Values: `𝒩 ≈ 1.8×10¹⁸` for a kg-scale apparatus with mm branch separation;
`𝒩 ≈ 9×10⁶` for C₆₀ in a double slit; `𝒩 > 1` in every case checked.

The physical content: **gravity imprints distinguishable phase on everything
massive nearby vastly sooner than it imprints a readable needle deflection.**
Phase leaks before position. The which-branch bit is out — spread thin across
every mass in the neighbourhood — long before any local subset can recover it.

That is verbatim the **dilution law of `mechanism/0002`**, arrived at from an
entirely independent direction. Encouraging: the repo's existing mechanism
predicts the right thing here without adjustment.

## Correction 3 — the paradox window is closed from both sides

`𝒩 < 1` requires `G M μ² δr < ħ²`, i.e. `M μ² δr < ħ²/G = 1.67×10⁻⁵⁸ kg³·m`.

With `M = μ` and `δr = 1 µm` that is `M < 5.5×10⁻¹⁸ kg` — a **real
nanoparticle**, not an absurdity. Levitated optomechanics operates near there.
So the coherence side of the paradox is genuinely satisfiable.

But at those parameters the differential acceleration is `~10⁻²⁶ m/s²` and
`t_read ≈ 9×10⁴ years` even at the SQL. The two failure modes are exactly
complementary:

- **heavy** → readable in principle, but decohered ~10¹⁸× sooner;
- **light** → coherent, but unreadable on any human or geological timescale.

No parameter choice opens a window. This is the honest form of the user's
option (4) — the limit is real, but it binds only in the light regime, and it
is the SQL rather than ruler-length uncertainty that does the binding.

## The double-slit objection, answered

The user's own strongest objection to "gravity is an information channel" was:
then we could always locate a particle gravitationally, and interference would
never work. The numbers say otherwise. For C₆₀ against a ~1 ms interferometer
transit, `t_ent/1ms ≈ 1.3×10⁷` and `t_read/1ms ≈ 1.2×10¹⁴`. Neither the leak
nor the readout has time to act.

So option (2) survives its own best counterargument. Gravity **is** a channel;
it is simply a channel of preposterously low capacity at laboratory scales.
That is a statement about the smallness of `G`, not about gravity being
exempt from information-theoretic accounting.

## Thermal shielding is *not* what saves us

Worth recording because it is the obvious cheap dismissal and it is wrong.
Self-emission of blackbody photons does carry which-path information, and at
300 K it decoheres a mm-separated branch pair in `~10⁻²²` s. But the
Joos–Zeh long-wavelength suppression `(δr/λ_th)²` is severe when cooled: at
1 mK, `λ_th ≈ 3.7 m ≫ δr`, and the decoherence time rises to ~22 s — *longer*
than `t_read`. Cooling genuinely defeats the thermal leak.

So the experiment cannot be waved away with "your apparatus is warm." The
binding constraint is gravitational coupling itself, which cooling cannot
touch. The user's option (5) is right that there is an unavoidable leak; it is
wrong that a *secondary* mechanism is needed. Gravity is the leak.

## Verdict on the five proposed resolutions

| | proposal | verdict |
|---|---|---|
| 1 | gravity is non-informational | **rejected** — then gravimeters could not work at all |
| 2 | gravity is itself the information leak | **correct**, and it survives its own double-slit objection quantitatively |
| 3 | collapse is a physical process; detectors sit at an average | **disfavoured** — this is semiclassical gravity; see below |
| 4 | detector-separation uncertainty | **right regime, wrong bound** — the SQL binds, and only in the light regime |
| 5 | a secondary leak is conspiratorially injected | **right instinct, no secondary needed** — (2) already supplies it |

Four of the five are facets of one answer, which is a good sign the user's
instincts were tracking something real rather than enumerating alternatives.

## What this forces on the framework

The experiment is a genuine stress test of **P2**. The paradox is manufactured
by treating the gravitational field as *correlational* knowledge — a passive
global bookkeeping quantity that merely reflects the state — while
simultaneously reading it off a needle, which is *actionable*. P2 forbids
having it both ways.

**Consequence: gravity must sit on the actionable side of the firewall.** It is
`c`-bounded, it is a real channel, and therefore it decoheres. The framework
does not get to quarantine gravity as bookkeeping.

Two further commitments follow, and both are non-trivial:

1. **The field must be an edge in the web, not a function of the state.** A
   classical field sourced by `⟨T_μν⟩` is an absolute, frame-independent object
   that every observer agrees on — which is exactly what **P1** denies. This is
   independent of, and converges with, the standard objections to semiclassical
   gravity (Eppley–Hannah 1977; Kibble 1980; Page–Geilker's 1981 experiment
   disfavouring the `⟨T_μν⟩` source). Option (3) is the semiclassical option and
   inherits all of that baggage. Gravitationally-induced-collapse models
   (Diósi–Penrose) are a live variant and are *not* covered by this objection —
   they modify the dynamics rather than keeping a classical field, and remain a
   standing alternative.
2. **Retardation is automatic and kills the FTL worry at the root.** The
   user's light-burst extension imagines seeing a photon and the gravimeter
   "immediately responding." It does not respond — it was already correlated,
   because the field at our location at time `t` reflects the source at
   retarded time `t − r/c`, the same `c` the photon travelled at. Gravitational
   news cannot outrun optical news. This is the `mechanism/0002` "sensor spike"
   reading applied unchanged, and it needs no new machinery.

## Where this lands relative to the literature

The user independently reconstructed a known and important class of argument.
Named honestly:

- **Mari, De Palma, Giovannetti (2016)**, *Sci. Rep.* **6**, 22777 — a distant
  test particle interacting via semiclassical forces permits superluminal
  signalling; consistency with causality forces a minimum time to distinguish
  superposition from mixture, proportional to the mass. Same skeleton as the
  user's argument.
- **Belenchia, Wald, Giacomini, Castro-Ruiz, Brukner, Aspelmeyer (2018)**,
  *Phys. Rev. D* **98**, 126009 — the definitive treatment. Their conclusion,
  quoted from the abstract: *both vacuum fluctuations of the gravitational
  field and the quantization of gravitational radiation are essential in order
  to avoid inconsistencies*, and *the quantum body must be viewed as entangled
  with its own Newtonian-like gravitational field*.

That last clause is the same commitment reached above from P1/P2, by a
different route. Their causality argument (Bob's minimum resolution time versus
Alice's recombination-induced graviton emission) is a genuine complementarity
that I have **not** reproduced here — I could not retrieve the paper's
inequalities (arXiv and the QUB mirror both returned 403), so the `t_ent`
vs `t_read` analysis above is an independent construction, not a restatement of
theirs. It reaches a compatible conclusion by a cruder route. Treat the
agreement as encouraging, not as verification.

**The strongest available reading of their result, which the user should
notice:** the thought experiment is not merely resolved by quantizing gravity —
it is *inconsistent unless* gravity is quantized. The user's instinct that
"if gravity is to fall out or be compatible, this is relevant" is exactly right,
and the direction of the argument is stronger than they proposed.

## Open threads

- **Reproduce the Belenchia complementarity.** Their `⟨N⟩ ~ G m²d⁴/(ħc⁵T⁴)`
  graviton-emission estimate is straightforward quadrupole bookkeeping and I
  can derive the scaling; the Bob-side vacuum-fluctuation bound is the part
  worth getting right. Needs the paper.
- **Is 𝒩's `r`-independence deeper than it looks?** Both timescales carrying
  identical `r²` is suspicious in a good way. Candidate reading: `𝒩` is a
  ratio of couplings, not of geometries — it should be expressible in terms of
  `M μ² δr` against `ħ²/G` alone, and `ħ²/G` has dimensions `kg³·m`. What is
  that combination? It is not obviously a Planck quantity. Worth a look.
- **Does "correlation sources curvature" (`foundations/0005`) survive this?**
  The commitment above — field is an edge, not a function of the state — is a
  constraint on any such Einstein-analog equation. It rules out sourcing
  curvature by an expectation value.
- **Diósi–Penrose as the live alternative** to option (2) deserves its own
  note; it is the one resolution on the user's list that is not disposed of.
