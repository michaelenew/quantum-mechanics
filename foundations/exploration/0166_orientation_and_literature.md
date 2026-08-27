# 0166 — Orientation: where this sits in the literature

> **AI-generated, not peer-reviewed.** Orientation pass, no module.
> Sources checked against the literature rather than recalled.
> Prior art credited in [`ATTRIBUTION.md`](../ATTRIBUTION.md).
>
> **Prior art.** Barrett & Crane (1998); Alesci & Rovelli (2007); Engle, Pereira, Rovelli & Livine (2008); Freidel & Krasnov (2008); Sakharov (1967); Plebanski (1977).

The working hypothesis going in was that the gravity sector had moved
"plausibly out of known territory." **It has not.** Checking it
against the literature puts almost all of it inside well-mapped
ground, and turns up one finding serious enough that it changes how
item 2 should be read.

## 1. The derived weight is a Barrett–Crane amplitude

The weight is `A(U⁺,U⁻) = Σ_j n_j χ_j(U⁺) χ_j(U⁻)` — a sum over the
**diagonal** j⁺ = j⁻. Those are the **balanced representations**, and
restricting to them is exactly how [Barrett and Crane
(1998)](https://arxiv.org/abs/gr-qc/9709028) impose simplicity in
their Euclidean spin foam model. 0160 s3 presented this as the
program's own discovery of the simplicity constraint. It is that — but
it is also a 1998 model, re-derived.

## 2. And Barrett–Crane is known to fail the graviton propagator

This is the finding that matters. [Alesci and Rovelli
(2007)](https://arxiv.org/abs/0708.0883) computed the graviton
two-point function from the BC vertex and found **it does not give the
correct long-distance limit**. They traced the failure to the
**intertwiner-independence** of the BC vertex — the amplitude depends
only on the representation labels, not on the intertwiners at the
nodes. That result is why the field moved to the EPRL and FK vertices
in 2007–8, which retain intertwiner dependence.

**The derived weight is a pure character sum. It has no intertwiner
structure at all.** So it sits on the wrong side of exactly the
distinction that killed BC.

> **This reopens item 2.** 0149/0150 attributed the spin-2 null to
> ξ/a ~ 10²⁰ — a scale argument. There is a competing and better-
> established explanation: the amplitude is of a type independently
> known to give the wrong long-distance two-point function. The scale
> argument is not wrong, but it was never tested against this
> alternative, and it should have been.

That is a third mis-diagnosis of item 2, and unlike the first two it
was not found by measurement — it was found by reading.

## 3. The induced sector is Sakharov, with Sakharov's problems

Gravity from a one-loop matter determinant is [Sakharov
(1967)](https://arxiv.org/abs/gr-qc/0204062). The problems 0159 hit
are the classic ones, and the literature is blunt about their size: a
finite cosmological constant requires not only boson/fermion
compensation but "an incredible fine-tuning between their respective
masses," with the induced Λ coming out **~100 orders of magnitude too
large**. 0159's rank(B) = 4(V−1) cutoff-scale Λ, cancelled by a forced
counterterm, is that problem in miniature. The wrong-sign conformal
mode (0147/0150) is likewise standard: in Euclidean signature it makes
the path integral undefined, and that has been discussed since
[Gibbons–Hawking–Perry
(1978)](https://ui.adsabs.harvard.edu/abs/1990IJMPA...5.3811G/abstract).

## 4. The constrained sector is Plebanski, and R1–R3 are theorems

BF + simplicity = GR is [Plebanski
(1977)](https://arxiv.org/abs/2005.12004). That linearised Palatini
with the connection integrated out equals linearised Einstein-Hilbert
is a textbook result. **R1's (1, −1, −2, 2) at 1e−15 verified my
implementation, not a new physical fact**, and R3's γ = +1 follows
from it rather than testing it. The geodesic in 0164 is a correct
end-to-end demonstration and is *not* a new result about gravity.

γ = −1 as Nordström with zero bending, and γ = 1/2 with 3/4 bending as
the vDVZ discontinuity, are 1913 and 1970 respectively.

## 5. Even the route has company

"Derive the simplicity constraint from an information principle rather
than imposing it" is [being actively
pursued](https://www.researchsquare.com/article/rs-10440199/v1), via
relative-entropy monotonicity under spin-network coarse-graining. The
program's synergy argument is a different mechanism, but the
programmatic slot is occupied.

## What may actually be new

Stated as candidates, not claims, and each needs a literature check
deeper than one pass:

1. **A derived coupling.** Spin foam models carry a free
   Barbero–Immirzi parameter. This program's κ = 16.0001 is fixed by
   the band limit (M = 6) and the double copy, with the capacity
   argument forcing flat multiplicities. If that survives scrutiny it
   is a parameter the standard models do not have.
2. **Simplicity as information synergy.** The measured statement —
   weight-table rank 6 not 1, residual spread 1.0000 given either
   chiral stream alone and 0.0000 given both — is a sharper and more
   operational form than "impose j⁺ = j⁻."
3. **The derived hierarchy.** Evaluating two-loop asymptotic freedom
   at the derived coupling gives ξ/a = 6e19…4e20 with nothing tuned.
   Spin foams do not normally produce a scale ratio at all.

## What this orientation costs the program

Item 2 must be re-opened with the BC/intertwiner explanation as the
leading hypothesis. If it holds, the honest summary changes from "the
graviton propagator is unmeasurable at this coupling" to **"the
derived amplitude is of a class known to give the wrong graviton
propagator"** — which is a defect in the theory, not the instrument.

The concrete test is available and standard: BC's failure is
diagnosed by intertwiner-independence, so the question is whether the
derived weight can be extended to carry intertwiner dependence
without giving up the derivation of κ. If it can, the program moves
from BC to the EPRL/FK class. If it cannot — if the capacity argument
*forces* a character sum — that is a sharp negative result and worth
far more than another lattice run.

## 6. The founding constructions, checked

The orientation above covered the gravity sector. A later pass checked
the four ideas the program was *started* on. All four have established
lineages, and none of them carried a citation in `ATTRIBUTION.md`
before that check.

**"A distribution cannot encode its own confidence."** The motivating
puzzle is **inverted by a 1981 theorem**:
[Wootters](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.23.357)
showed the angle between rays in Hilbert space *is* the statistical
distance — not analogous to it, equal to it. Braunstein & Caves (1994)
completed it: the Fubini–Study metric is ¼ the quantum Fisher
information. The program's 0065 — the web's metric as the Fisher
metric of an inference network with w = e^{2I} − 1 — is the classical
shadow of exactly that.

**Knots as a topological basis for pairwise interactions.** This is
the construction that felt least occupied, and it is the most
precisely occupied. 0011's crossing rule
`2·over = under_in + under_out (mod p)` is verbatim the **Fox
n-colouring** condition, and Fox colourings are **quandle**
homomorphisms into the dihedral quandle. Quandles are due to Joyce
(1982) and Matveev (1982) independently, with Takasaki (1943) for the
involutory case, and their axioms *are* the Reidemeister moves.
0011 registered this honestly at the time — "it is an isomorphism of
formalisms" — and cited Deser–Jackiw–'t Hooft, Witten and
Kronheimer–Mrowka. Beyond what it cited: Rovelli & Smolin's (1988)
loop states are knot classes, and anyon braiding is
interactions-as-crossings in 2+1D.

**"Correlation sources curvature" — the holography hope.**
[Matsueda (2013)](https://arxiv.org/abs/1310.1831) derives the
Einstein tensor from the Fisher information metric and is the nearest
structural neighbour; Jacobson (1995, 2015), Ryu–Takayanagi (2006),
Van Raamsdonk (2010) and Maldacena–Susskind (2013) surround it. 0058
had already reached the honest verdict: what was delivered is
**"participation density sources curvature"**, not correlation, and
the identification of the knowledge manifold with spacetime is
*assumed* here where holography *earns* it as a duality — 0058's own
words, "the program's largest unpriced assumption". Cousin of
holography, correctly identified, and identified early.

**The two-tier split.** Relational QM (Rovelli 1996), QBism, and
Spekkens' epistemic restriction — all three named as inherited in
0002's own novelty assessment.

> **So no founding construction is new, and in three of the four the
> repository said so at the time it wrote them down.** What remains
> as a candidate is not an ingredient but a *closure*: that one
> derived measure lands on all of these in sequence with the coupling
> **fixed rather than chosen** (κ = 16.0001 where spin foams carry a
> free Barbero–Immirzi parameter), and the hierarchy that falls out of
> it.

And the caution that applies to that candidate more than to any
other: a chain of known links reaching a known destination is exactly
what a system with the whole literature in training would produce
whether or not the reasoning was sound. The convergence is evidence
about the generating process at least as much as about physics.

## Honest scoreboard

- **Not novel:** the constrained-sector construction, the induced
  sector and its pathologies, γ, β_PPN, vDVZ, the conformal-mode sign,
  the double copy, the lattice methodology.
- **Novel-adjacent, needs checking:** the derived coupling, synergy as
  simplicity, the derived hierarchy.
- **Newly serious:** the program has converged onto a spin foam model
  the field left behind in 2008, for a reason that bears directly on
  the one measurement it could not make.
