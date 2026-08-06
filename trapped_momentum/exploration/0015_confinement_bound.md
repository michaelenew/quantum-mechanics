# 0015 — The confinement bound: Kerr's quadrupole is not reachable by material tension

Next rung after `0014`. Pressing on the strong-field endpoint turned up a
sharper and fully rigorous question in the same bookkeeping, and it has an
exact answer. `output/0014_confinement_bound.py`, 17/17 checks, 5/5
pre-registered predictions confirmed.

**This upgrades `0013`'s "achievable, not automatic" to a theorem with a sharp,
attained bound — and it retires that phrasing as too weak.**

## The reduction

Axisymmetric static equilibrium of the *whole* system (ring + confinement),
thin in `z`. Define the **transmitted radial force**

```
u(ρ) = 2πρ·S^{ρρ}(ρ)      (negative = net inward pull crossing radius ρ)
```

Total-system equilibrium gives `S^{φφ} = ∂_ρ(ρS^{ρρ})`, i.e. `u' = 2πS^{φφ}`,
and the entire stress second moment collapses to one quadrature:

```
Y_tot = −2∫₀^a u(ρ)ρ² dρ
```

with no boundary term (`u = 0` outside). Verified against all three known
architectures to 1e-8 — hoop `0`, membrane `Ea²/2`, spokes `2Ea²/3`. **The
`0013` ladder was three choices of one function.**

## The theorem

If every stress is a **tension** (`S^{ρρ} ≤ 0` and `S^{φφ} ≤ 0`), then `u ≤ 0`
and `u' ≤ 0`, so `u` decreases monotonically from `u(0) = 0`, and the ring's
own force balance caps it at `|u(a)| ≤ E/a`. Hence
`|∫uρ²| ≤ (E/a)(a³/3)` and

> ```
> 0 ≤ Y_tot ≤ 2Ea²/3        ⟺        M₂ fraction ∈ [1/2, 5/6]
> ```
>
> **No all-tension material confinement can produce more than 5/6 of the Kerr
> quadrupole. Kerr is outside the reachable set.**

The bound is **tight at both ends**, shown by the power-law family
`u = −(E/a)(ρ/a)^n`, which has the exact closed form
`fraction = (1 + 2/(n+3))/2` (verified numerically) and sweeps the whole
interval: `n = 0` gives the supremum 5/6 (spokes — all force transmitted from
the very centre), `n → ∞` gives the infimum 1/2 (hoop — nothing transmitted
radially at all).

Honesty note on the numerics: 4000 random monotone tension profiles violate
nothing, but they only span `[0.72, 0.78]` and never approach either edge — on
their own that is weak evidence of tightness. The power-law family is what
establishes it. The random sample is reported anyway because it is what I ran
first and it would have been easy to present it as stronger than it is.

## What Kerr costs

Reaching `Y_tot = Ea²` requires `∫uρ²dρ = −Ea²/2`. Writing `u = −(E/a)g(ρ/a)`,
the condition is `∫₀¹gx²dx = 1/2` — while all-tension gives `g ≤ 1` hence
`≤ 1/3`. Minimising the peak of `g` subject to the constraint (put weight where
`x²` is largest) gives `G = 3/(2(1−x₀³))`, minimised at **`G = 3/2`**.

Verified: box profiles at several `x₀` all hit fraction `1.000000` exactly, the
cheapest needing peak `|u| = 1.5 E/a`.

> The structure must carry **50% more internal tension than the load it
> transmits**. That excess can only be closed by `u' > 0` somewhere — which is
> **hoop compression**.

So Kerr is not a fine-tuning of a tension profile. It requires a qualitatively
different object: a **pre-stressed structure with compression members** — a
tensegrity, not a web.

## The energy price (lower bound only)

DEC bounds a member's linear energy density by its stress, so a compression
ring of radius `r` carrying `C` costs at least `C·2πr`. With `C = 0.5 E/a`:

| ring radius | minimum energy |
|---|---|
| `a` | ≥ 3.14 E |
| `a/2` | ≥ 1.57 E |
| `a/4` | ≥ 0.79 E |

Order of magnitude: **the confinement is comparable to or heavier than the ring
it confines.** Moving the compression ring inward reduces the cost but also its
lever arm, and the profile then fails to reach Kerr.

Registered honestly as an obstruction of unknown severity, **not** a
refutation: the confinement's own energy adds to `E`, shifts `a = S/E`, and
changes the target. That self-consistency problem is not solved here.

## Why gravity is not bounded by any of this

The bound constrains **matter** stresses — `u` is the force carried by
`T^{ρρ}`. Gravitational binding transmits force with no matter stress at all;
in `0014` the self-force came from the field, and the hoop tension it replaced
scaled away as `(1−f)`.

That dissolves what looked like a tension between `0013` and `0014`:

- `0013`'s ladder tops out at 5/6 — now known to be a **hard ceiling** for
  material confinement, not a sampling artefact.
- `0014`'s self-gravitating case reaches exactly 1 — possible *precisely
  because* it removes matter stress rather than rearranging it.

> **Kerr's quadrupole is a signature of non-material confinement.**

## What this means for the electron — **WITHDRAWN, see `0016`**

> **This entire section is retracted.** Link (1) was verified in `0016` and
> carries a qualifier that voids the inference: minimal coupling reproduces
> Kerr's multipoles **in the infinite-spin limit**, and a spin-`s` state carries
> multipoles only to rank `2s`. For `s = ½` the spin-induced quadrupole
> operator vanishes *identically as a matrix* — **the electron has no
> quadrupole moment at all**, so there is nothing to sit at fraction 1 of.
> The theorem above is untouched (it never needed the electron); only this
> application dies. Kept below as the record of the wrong inference.

Assembling the chain, with its one unverified link flagged:

1. If minimal coupling = Kerr multipoles **[K, unverified — search quota
   exhausted]**, the electron sits at fraction 1.
2. `0015` (here): no all-tension material structure exceeds 5/6.
3. `0014`: gravity supplies `~10⁻⁴⁴` of the electron's confinement.

So *if* (1) holds, whatever confines the electron's circulating null momentum
is **neither ordinary material tension nor gravity** — it must be either
pre-stressed structure at an energy cost comparable to the electron itself, or
a field binding that is not gravitational.

The natural candidate the workstream has been circling since `0001` is the
electromagnetic/quantum vacuum — and `0013`'s Israel-disk result (exact Kerr
needs a *negative*-energy interior sheet) points the same way, since negative
energy density is a vacuum phenomenon, not a material one. Registered as a
direction with two independent arrows pointing at it, not as a claim.

**Link (1) is now load-bearing for a lot.** Verifying the minimal-coupling =
Kerr-multipoles statement is promoted to the top of the reading list, alongside
Souriau.

## Method

Five predictions registered before running, five confirmed — the first clean
sweep in this workstream. Worth noting *why*, since the previous three rungs
each falsified something: this rung was derived analytically first (the
`u`-reduction is exact algebra) and the numerics only checked it. The rungs
that produced falsifications were the ones where I guessed a physical result
and then computed. That is a usable distinction going forward: **derive, then
check — and register the guess separately when there is one.**

## Next

1. **Verify the minimal-coupling = Kerr multipoles claim [K]** — now
   load-bearing for the electron conclusion above.
2. **Strong-field endpoint** — still open from `0014`: does `f → 1` stay at
   Kerr beyond leading order? The Neugebauer–Meinel disc → extreme Kerr result
   [K] is the anchor.
3. **Souriau** — still gates the interaction formalism.
4. The self-consistency problem in P4: solve the fixed point where the
   confinement's energy is included in `E` and `a = S/E`.
