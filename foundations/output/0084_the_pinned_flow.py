"""0084 -- the pinned flow: a hierarchy with no continuous knob.

0093 ended with the knob-derivation open: pin tau0 and the
transmutation formula predicts a hierarchy. This stone assembles the
program's first NO-CONTINUOUS-KNOB chain:

  constraint stack (odd + >=3 + 1-mod-4 primes)  ->  admissible N
  level cutoff (quantum-group admissibility)     ->  J(N)
  the DERIVED Born counting weight at cutoff J   ->  bare W (no dial)
  one MK blocking (0092's localization)          ->  tau1(N), exact
  the one-loop flow (0093)                       ->  ln(L*/a) = ln 2 / (c tau1)

Every link is derived or measured except ONE: the identification of
the ledger's level N with the representation cutoff. Quantum-group
conventions offer two natural forms, both carried:
    k = N     : j <= N/2
    k = N - 2 : j <= (N-2)/2

  s1  tau1 per admissible level, both conventions, with heat-kernel
      flatness verified (< 0.01 after the single blocking).
  s2  The hierarchy table. Headline classes:
        N =  5 : L*/a ~ 10^8  - 10^17
        N = 13 : L*/a ~ 10^65 - 10^88
        N = 17 : L*/a ~ 10^114 - 10^143
  s3  The scaling law: tau1 ~ 1.2/J^2, so the hierarchy exponent is
      QUADRATIC in the level: ln(L*/a) ~ (ln 2 / 1.2 c) J^2. Small
      admissible levels give particle-physics-sized hierarchies;
      the second admissible level gives cosmological-sized ones.
  s4  The error budget, stated before anyone gets excited: the MK
      coefficient c is scheme-dependent (+-30% -> exponent +-30%),
      the cutoff convention moves the exponent by up to 2x at small
      N, and the level-cutoff identification itself is a MODELING
      BRIDGE, not a derivation. The claim is the chain and the
      exponent class -- numerical near-misses with known ratios
      (10^17 ~ Planck/EW at N = 5; 10^65 ~ horizon/Planck at N = 13,
      k = N-2) are recorded as suggestive shapes only.
"""

import numpy as np

TH = np.linspace(1e-7, np.pi - 1e-7, 600001)
C_B2 = 0.127                      # 0093's b=2 coefficient


def chi(j, th):
    return np.sin((2 * j + 1) * th) / np.sin(th)


def C2(j):
    return j * (j + 1)


def r_of(W, j):
    p = W * np.sin(TH) ** 2
    return float(np.trapezoid(p * chi(j, TH), TH)
                 / ((2 * j + 1) * np.trapezoid(p, TH)))


def tau_after_one_blocking(J):
    W = sum(chi(j, TH) for j in np.arange(0, J + 0.01, 0.5)) ** 2
    W1 = (W / W.max()) ** 4
    js = (0.5, 1, 1.5, 2) if J >= 2 else (0.5, 1)
    vals = [-np.log(r_of(W1, j)) * 4 / C2(j) for j in js]
    flat = max(abs(v / vals[0] - 1) for v in vals)
    return float(np.mean(vals)), flat


STACK = (5, 13, 17, 25, 29)
CONVENTIONS = (("k=N", lambda N: N / 2),
               ("k=N-2", lambda N: (N - 2) / 2))


def s1_s2_table():
    print("== s1/s2: the pinned hierarchy table ==")
    out = {}
    for N in STACK:
        for name, Jf in CONVENTIONS:
            J = Jf(N)
            tau1, flat = tau_after_one_blocking(J)
            assert flat < 0.01, (N, name, flat)
            lnL = np.log(2) / (C_B2 * tau1)
            out[(N, name)] = (tau1, lnL)
            print(f"  N={N:2d} {name:6s} (J={J:4.1f}): tau1 = "
                  f"{tau1:.5f} (flat {flat:.4f})  ln(L*/a) = "
                  f"{lnL:5.0f}  ~ 10^{lnL / np.log(10):.0f}")
    # ordering sanity
    for name, _ in CONVENTIONS:
        lnLs = [out[(N, name)][1] for N in STACK]
        assert all(b > a for a, b in zip(lnLs, lnLs[1:]))
    for N in STACK:
        assert out[(N, "k=N-2")][1] < out[(N, "k=N")][1]
    print("  hierarchy strictly increasing in the level; k=N-2 "
          "convention always smaller\n")
    return out


def s3_scaling(out):
    print("== s3: the scaling law ==")
    for N in STACK:
        J = N / 2
        tau1 = out[(N, "k=N")][0]
        print(f"  N={N:2d}: tau1 * J^2 = {tau1 * J * J:.3f}")
    prods = [out[(N, "k=N")][0] * (N / 2) ** 2 for N in STACK[1:]]
    assert max(prods) / min(prods) < 1.15
    print("  tau1 ~ 1.2/J^2 (stable to 15% for N >= 13; the smallest "
          "level runs ~30% low),")
    print("  so ln(L*/a) ~ (ln 2 / 1.2 c) J^2: the hierarchy exponent "
          "is QUADRATIC in the level\n")


def s4_error_budget():
    print("== s4: the error budget, stated plainly ==")
    print("  - c is MK-scheme-dependent: +-30% on the exponent")
    print("  - cutoff convention (k=N vs k=N-2): up to 2x on the "
          "exponent at small N")
    print("  - the level<->cutoff identification is a modeling "
          "bridge, NOT derived in-program:")
    print("    it is now the chain's single unproven link and the "
          "sharpest open in the arc")
    print("  - near-misses (10^17 ~ M_P/M_EW at N=5; 10^65 ~ "
          "horizon/Planck at N=13, k=N-2)")
    print("    are recorded as suggestive shapes only -- the CLAIM is "
          "the existence of a")
    print("    no-continuous-knob chain from the constraint stack to "
          "a hierarchy class\n")


if __name__ == "__main__":
    out = s1_s2_table()
    s3_scaling(out)
    s4_error_budget()
    print("all assertions passed")
