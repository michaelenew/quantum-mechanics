# gravitation — SUMMARY

Where gravity sits relative to the two-tier structure, and what the
gravitational which-branch thought experiment forces on the framework.

## Current state

Driven by the thought experiment in `exploration/0001`: a sphere in a
superposition of "fired a particle out the hole" (lighter, orbiting) and "did
not" (heavier, free-falling), read by two sensitive gravimeters. The apparent
paradox is that reading the gravimeter yields which-branch information from a
system stipulated to be informationally isolated.

**Resolution: the premises are contradictory. Gravitational detectability *is*
non-isolation.** Made quantitative by two timescales:

- `t_ent = ħr²/(GμM·δr)` — when the gravimeter's phase becomes
  branch-distinguishable (Bose / Marletto–Vedral criterion). The bit has left.
- `t_read = (4ħ/μa²)^{1/3}`, `a = 2GM·δr/r³` — when the branch-dependent
  acceleration clears the free-mass SQL. The bit becomes actionable.

```
        t_read     ⎛ G M μ² δr ⎞^(1/3)
  𝒩  =  ──────  =  ⎜ ───────── ⎟          — and r cancels exactly
        t_ent      ⎝    ħ²     ⎠
```

`𝒩 ≈ 1.8×10¹⁸` for a kg apparatus; `𝒩 > 1` in every case checked. The
which-branch information is diluted across every nearby mass long before it is
readable anywhere. **Phase leaks before position.** This reproduces
`mechanism/0002`'s dilution law from an independent direction.

The `r`-independence is the sharp result: **there is no "far enough away"
configuration.** Both timescales carry `r²` identically.

The paradox window `𝒩 < 1` requires `G M μ² δr < ħ²`, satisfiable at real
nanoparticle masses (`~10⁻¹⁸ kg`) — but there `t_read ≈ 10⁵ years`. Heavy →
decohered first; light → unreadable. No window.

All of the above computed and self-checked in
`output/0001_which_branch_timescales.py` (9/9 checks, pure stdlib).

## Two corrections to the experiment as posed

1. **The deadline is `T_orb/(4√2) ≈ 0.177 T_orb`, not one period.** Radial
   infall is the degenerate ellipse of semi-major axis `R/2`; by Kepler III the
   fraction is a pure number independent of `R` and both masses. Verified three
   ways to 11 digits. The protocol as specified runs 5.7× past the point where
   the no-exit branch has collided with the laboratory.
2. **The dominant discriminator is the trajectory difference, not the mass
   difference `m`.** The branches separate positionally far faster than the
   `m/M` fractional mass change matters. This strengthens the argument.

## What it forces on the framework

- **Gravity is actionable knowledge, not correlational.** It is `c`-bounded, it
  is a real channel, and therefore it decoheres. The framework does not get to
  quarantine gravity as passive bookkeeping. This is a genuine constraint that
  P2 generates rather than absorbs.
- **The field must be an edge in the web, not a function of the state.** A
  classical field sourced by `⟨T_μν⟩` is an absolute frame-independent object —
  exactly what **P1** denies. Converges with the standard objections to
  semiclassical gravity (Eppley–Hannah 1977; Kibble 1980; Page–Geilker 1981)
  and with Belenchia et al.'s "the body is entangled with its own Newtonian
  field," reached here by a different route.
- **Constrains `foundations/0005`.** Any "correlation sources curvature"
  Einstein-analog cannot source curvature from an expectation value.
- **Retardation kills the FTL worry at the root.** Gravitational news
  propagates at `c`, so it cannot outrun the light-burst variant of the
  experiment. `mechanism/0002`'s "sensor spike" reading applies unchanged.

## Verdict on the five proposed resolutions

| | proposal | verdict |
|---|---|---|
| 1 | gravity is non-informational | rejected — gravimeters would not work |
| 2 | gravity is itself the leak | **correct**; survives its own double-slit objection |
| 3 | collapse is physical, detectors average | disfavoured (= semiclassical gravity) |
| 4 | detector-separation uncertainty | right regime, wrong bound — the SQL binds, light regime only |
| 5 | a secondary leak is injected | right instinct, but (2) already supplies it |

The double-slit objection to (2) fails quantitatively: for C₆₀ against a 1 ms
transit, `t_ent/1ms ≈ 1.3×10⁷` and `t_read/1ms ≈ 1.2×10¹⁴`. Gravity is a
channel of preposterously low capacity, not an exempt one.

Thermal shielding is **not** the resolution: cooling to 1 mK pushes
self-emission decoherence to ~22 s via Joos–Zeh long-wavelength suppression,
*longer* than `t_read`. The cheap dismissal does not work; gravitational
coupling is the binding constraint and cooling cannot touch it.

## Positioning

The user independently reconstructed a known argument class:
**Mari–De Palma–Giovannetti (2016)**, *Sci. Rep.* **6**, 22777, and
**Belenchia–Wald–Giacomini–Castro-Ruiz–Brukner–Aspelmeyer (2018)**,
*Phys. Rev. D* **98**, 126009. The strongest reading of the latter, which
sharpens the user's motivation: the thought experiment is not merely *resolved
by* quantizing gravity — it is **inconsistent unless** gravity is quantized.

## Known gaps

- The `t_ent`/`t_read` analysis is an **independent construction**, not a
  restatement of Belenchia et al. (arXiv and the QUB mirror both 403'd). The
  agreement in conclusion is encouraging, not verification. Reproducing their
  vacuum-fluctuation bound on Bob's side is the concrete next target.
- `ħ²/G` has dimensions kg³·m and is not obviously a Planck combination. Why
  does the paradox condition land on it? Unexplained.
- **Diósi–Penrose gravitationally-induced collapse** is the one item on the
  user's list not disposed of — it modifies dynamics rather than retaining a
  classical field. Standing alternative; deserves its own note.
- Graviton-emission complementarity (`⟨N⟩ ~ Gm²d⁴/ħc⁵T⁴`) derivable by
  quadrupole bookkeeping; not yet done here.
