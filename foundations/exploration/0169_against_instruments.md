# 0169 — The program against measurements that already exist

> **AI-generated, not peer-reviewed.** Code: `output/0159_the_experimental_bounds.py`.
> Prior art credited in [`ATTRIBUTION.md`](../ATTRIBUTION.md).
>
> **Prior art.** LIGO/Virgo Collaboration (GWTC-3) for the graviton
> dispersion bound; Abbott et al. (2017), GW170817/GRB 170817A, for the
> propagation-speed bound; the gamma-ray-burst polarisation and
> spectral-lag programme for the dimension-5 Lorentz bound; Colladay &
> Kostelecký for the Standard Model Extension the coefficients are
> quoted in.

Every test in this program so far has been against a theorem or
against itself. **These are against instruments.**

## The scale

`ℓ_P = 0.5037 a` (0163, two polarisations) ⟹ **a = 3.2088e−35 m =
1.9853 ℓ_P**, so 1/a = 6.15e+18 GeV.

## The graviton mass — and this one bites

A kernel `H(k) = H₀ + k̂²H₂` has a pole at `k̂² = −H₀/H₂`, so
`(ma)² = ‖H₀‖/‖H₂‖`.

**Induced sector** (0165 measured ‖H₀‖/‖H₂‖ = 21.6):

| | |
|---|---|
| m·a | 4.6476 |
| m | 2.8581e+28 eV = **2.34 M_Planck** |
| LIGO/Virgo bound | m_g < 1.3e−23 eV |
| **exceeded by** | **2.20e+51 — 51.3 orders of magnitude** |

> **The induced sector is excluded by experiment, by 51 orders.** Not
> by a theorem, not by an internal inconsistency — by a measurement
> that exists.

**Constrained sector** (0152, 0163): the kernel is linearised
Einstein-Hilbert, diffeomorphism invariant to O(a²), and
diffeomorphism invariance **forbids** a mass term. m = 0 identically;
the bound is satisfied with nothing to check.

**That is the result worth having.** The choice between the two
sectors was made on internal grounds — 0158 (wrong sector), 0159
(wrong expansion point), 0163 (γ = +1.000). It is now forced from
outside as well. Had the program kept the induced sector it would be
**dead by 51 orders against an existing instrument**. Experiment
selects the same sector the derivation did, and it did not have to.

## Propagation speed — a pass that discriminates nothing

Lattice dispersion `E = 2 arcsinh(k̂/2)`, verified to 6.66e−16 in 0165.

| f (Hz) | k a | \|c_g/c − 1\| |
|---|---|---|
| 10 | 6.73e−42 | 3.77e−84 |
| 100 | 6.73e−41 | 3.77e−82 |
| 1000 | 6.73e−40 | 3.77e−80 |

Against GW170817's |c_gw/c − 1| < 1e−15: **passes by ~64 orders.**
Worth recording precisely because it is the boring outcome — a
Planck-spacing lattice cannot be caught this way.

## Lorentz violation — a structural pass

Dimension-5 operators at Planck strength would give ~1/M_Pl =
8.19e−20 GeV⁻¹. The measured bound is **4.2e−34 GeV⁻¹** — naive
Planck-strength dimension-5 LIV is **excluded by 14.3 orders**. This
is real data that has already killed real models.

Does this lattice generate one? Test the symmetry directly rather
than fitting:

| x = k a | E(x)/x + E(−x)/x |
|---|---|
| 0.001 … 0.5 | **+0.000e+00** |

**Exactly zero.** The dispersion is even in a, so odd powers cannot
appear at all, and the leading coefficient is −0.08333332 against the
exact −1/12 (E = 2 arcsinh(sin(x/2)) = x − x³/12 + O(x⁵)).

> **Dimension-5 Lorentz violation is forbidden by the lattice's own
> reflection symmetry**, not suppressed by accident.

The leading violation is dimension-6, suppressed by 1/M_Pl². Quadratic
LIV bounds require a suppression scale above roughly 1e11 GeV; Planck
is 1.22e19, so this passes with ~8 orders in the scale to spare.

*(A first pass fitted a power series and reported an a³ coefficient of
1.8e−05 as "numerically zero". It is not — that was ill-conditioning
in the fit. Testing the symmetry directly is unambiguous.)*

## Scoreboard

| benchmark | result |
|---|---|
| graviton mass (LIGO/Virgo) | **induced sector EXCLUDED by 51 orders**; constrained sector massless by symmetry — passes |
| GW speed (GW170817) | passes by ~64 orders — does not discriminate |
| dim-5 LIV (GRB) | forbidden by reflection symmetry — passes structurally |
| dim-6 LIV (GRB) | Planck-suppressed — passes by ~8 orders in scale |

**One of these is a real result and it is the first one.** Everything
this program had decided until now was decided by a theorem or by its
own measurements. The sector question is now decided from outside too,
and it agrees.

The other three are passes, two of them structural rather than lucky.
None discriminates this program against any other — a Planck-spacing
lattice is simply hard to catch this way, which is the field's problem
and not this program's alone.
