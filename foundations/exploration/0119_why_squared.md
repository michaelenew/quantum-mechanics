# 0119 — Why squared: the canonical form of a nonnegative band-limited weight

0118 reduced the Born question to "why is the weight band-limited?"
and answered it as a budget. This stone closes the other half — why
a band-limited weight is a **square** — and the answer is that it
was never a postulate. Code: `output/0109_why_squared.py`.

## 1. On the abelian tier, exactly

A nonnegative trigonometric polynomial of degree n **is** |A|² for
some A of degree n — the Fejér–Riesz theorem. Verified to machine
precision (3e−15 across five trials) on weights whose coefficients
were *not* built as squares: each is a random polynomial lifted
until nonnegative, then factored blind.

> **Nonnegativity + band-limiting ⟹ squared.**

On the tier where this program's ledger theorems were first proven,
the Born square requires nothing else.

## 2. The factorisation's non-uniqueness *is* the source ledger

Fejér–Riesz fixes |A| but not A: each conjugate root pair may be
assigned inside or outside the unit disc, giving 2ⁿ amplitudes with
**identical** |A|². Verified: flipping a single root leaves the
weight unchanged to 3.9e−15 while changing the amplitude by 0.72 —
32 distinct amplitudes for one weight.

**That freedom is exactly the phase/source ledger.** It is
structurally invisible in the record — which is what 0086 proved as
the two-ledger theorem and lucid 0005 measured operationally (phase
never pays on a classical stream). The program's most distinctive
structure turns out to be the gauge freedom of a factorisation.

## 3. The nonabelian case — **REFUTED** (see 0120)

> **Statement, as conjectured here.** Every class function W on
> SU(2) with W ≥ 0 and character support ≤ 2J equals |A|² for some
> class function A with character support ≤ J.

**This is false.** The 1e−4 fits reported in this stone's first
draft were partially-converged optimisations, not solutions;
0120 settles it with 200-restart solves and an exact criterion.
Generic nonnegative band-limited class functions do **not** factor.
The correction matters for the chain below: §4's second link holds
on U(1) and **fails on SU(2)**, so on the tier where this program's
physics lives, squaring is *extra structure* rather than a
consequence of band-limiting. See `0120`.

## 4. The chain, and what is left

```
  finite information budget   ⟹  band-limited weight    (0118, measured)
  band-limited + nonnegative  ⟹  squared weight         (here, exact on U(1))
  squared weight              ⟹  amplitude with an
                                  unobservable phase    (here + 0086)
```

**"Why the Born rule" is a chain of three statements** — all three
exact on the abelian tier. On the **nonabelian** tier the middle
link fails (0120): band-limiting does not imply squaring there, so
the square carries genuine content. The postulate is dissolved
where the program's ledger theorems were proven, and *sharpened*
where its physics lives.

## Honest limits
- §1 and §2 are exact on U(1); the SU(2) extension is §3's open
  statement, and the program's own weight lives there.
- The chain explains the *form* of the weight given a finite budget
  and nonnegativity; it does not explain why the level takes the
  particular admissible value it does (still open — see below).
