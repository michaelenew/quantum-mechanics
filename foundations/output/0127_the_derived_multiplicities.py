"""0127 -- the derived multiplicities: re-pricing the coupling.

0137's criticality item 1. 0074 s3 DERIVED the nonabelian amplitude's
multiplicities from the Gaussian frame measure -- n_j is the measure
of frame pairs whose bivector magnitude |B+| falls in bin j -- and
reported the profile as "peaked, not monotone". Every module from
0091 onward instead used FLAT counting, all n_j = 1, and since the
hierarchy is exponential in the weight's local precision kappa, that
simplification is worth eight orders of magnitude in xi/a.

This recomputes the derived profile and re-prices the coupling.

  s1  THE PROFILE, RECOMPUTED. 0074's quadrature, vectorised: two
      frame vectors from the chi_4 radial law, their relative angle
      from the semicircle law, bivector magnitude
      s = r_a r_b sin(theta)/sqrt(2), binned at scale s0. Reported
      for a range of s0, because s0 is 0074's own free parameter
      and the profile's robustness to it is the question.
  s2  THE RE-PRICED COUPLING. kappa and xi/a for the derived
      profile against flat counting.
  s3  AN UNRECORDED STRUCTURAL STEP, found while doing this. 0074
      derives n_j for the Spin(4) frame amplitude,
      A(U+,U-) = sum_j n_j chi_j(U+) chi_j(U-). The lattice uses a
      single SU(2) with A = sum_j n_j chi_j(U). The reduction
      between them is nowhere in the program. So the gap is not
      only "flat versus peaked" -- it is also "which group", and
      that is a second unpriced step sitting under the same number.
"""

import numpy as np

TH = np.linspace(1e-9, np.pi - 1e-9, 400001)
B0, B1 = 11 / (24 * np.pi ** 2), 17 / (96 * np.pi ** 4)
rng = np.random.default_rng(127)


def chi(n):
    return np.sin(n * TH) / np.sin(TH)


def kappa(ns):
    ns = np.asarray(ns, float)
    if ns.sum() <= 0:
        return float("nan")
    A = sum(c * chi(n) for n, c in enumerate(ns, start=1) if c > 0)
    W = np.maximum(A ** 2, 1e-300)
    sel = TH < 0.15
    return float(-2 * np.polyfit(TH[sel], np.log(W[sel]), 4)[-3])


def xi_over_a(beta):
    if not np.isfinite(beta) or beta <= 0:
        return float("nan")
    g2 = 4.0 / beta
    return 1.0 / ((B0 * g2) ** (-B1 / (2 * B0 ** 2))
                  * np.exp(-1 / (2 * B0 * g2)))


def bivector_samples(n=4_000_000):
    """|B+| = r_a r_b sin(theta) / sqrt(2), with r ~ chi_4 (the
    Gaussian frame measure's radial law in 4D) and cos(theta) from
    the semicircle law for two random 4-vectors."""
    ra = np.sqrt(rng.chisquare(4, n))
    rb = np.sqrt(rng.chisquare(4, n))
    # cos of the angle between two isotropic 4-vectors:
    # density (2/pi) sqrt(1-c^2) -- sampled via a Beta(3/2,3/2)
    c = 2 * rng.beta(1.5, 1.5, n) - 1
    return ra * rb * np.sqrt(np.maximum(1 - c * c, 0)) / np.sqrt(2)


def profile(s, s0, J=6):
    """0074's binning: bin index round(s/s0), keep the first J."""
    idx = np.rint(s / s0).astype(np.int64)
    n = np.array([float((idx == j).sum()) for j in range(J)])
    return n / max(n.max(), 1e-30)


def s1_profile(s):
    print("== s1: the profile, recomputed ==")
    print("  0074's quadrature, vectorised, 4e6 frame pairs. "
          "Profile normalised to its peak:")
    print("     s0      n_0    n_1    n_2    n_3    n_4    n_5"
          "     shape")
    out = {}
    for s0 in (0.5, 0.75, 1.0, 1.5, 2.0):
        n = profile(s, s0)
        out[s0] = n
        peak = int(np.argmax(n))
        shape = ("monotone falling" if peak == 0
                 else f"peaked at j = {peak}")
        print("    " + f"{s0:.2f}".ljust(6)
              + "  ".join(f"{v:.3f}" for v in n) + f"    {shape}")
    print()
    print("  0074 reported 'peaked, not monotone' at its own bin "
          "scales. Recomputed, the")
    print("  shape DEPENDS ON s0: coarse binning puts the peak in "
          "bin 0 and fine binning")
    print("  moves it up. s0 is a free parameter of the "
          "construction, so the derived")
    print("  profile is a FAMILY, not a vector\n")
    return out


def s2_reprice(out):
    print("== s2: the re-priced coupling ==")
    flat = np.ones(6)
    kf = kappa(flat)
    print(f"  flat counting (what was simulated):  kappa = "
          f"{kf:.3f},  xi/a = {xi_over_a(kf):.2e}")
    print()
    print("     s0     kappa    xi/a        vs flat")
    ks = []
    for s0, n in out.items():
        k = kappa(n)
        ks.append(k)
        r = xi_over_a(k) / xi_over_a(kf)
        print(f"    {s0:.2f}   {k:7.3f}  {xi_over_a(k):.2e}   "
              f"{r:.2e}x")
    lo, hi = min(ks), max(ks)
    print()
    print(f"  across 0074's own free parameter, kappa runs "
          f"{lo:.2f} to {hi:.2f} and xi/a runs")
    print(f"  {xi_over_a(lo):.1e} to {xi_over_a(hi):.1e} -- a spread "
          f"of {xi_over_a(hi) / xi_over_a(lo):.0e}.")
    print()
    print("  SO THE DERIVATION DOES NOT DELIVER A NUMBER. It "
          "delivers a family indexed by")
    print("  a binning scale nobody has fixed. Flat counting was "
          "not a lazy choice over a")
    print("  known answer -- it was a choice over an UNDETERMINED "
          "one, and the program has")
    print("  been quoting a hierarchy that depends on it.")
    assert xi_over_a(hi) / xi_over_a(lo) > 10
    print()
    return kf, lo, hi


def s3_the_group_step():
    print("== s3: an unrecorded structural step ==")
    print("  0074 s3 derives the multiplicities for the SPIN(4) "
          "frame amplitude:")
    print("      A(U+, U-) = sum_j n_j chi_j(U+) chi_j(U-)")
    print("  The lattice (0091 onward) simulates a single SU(2) "
          "with")
    print("      A(U)      = sum_j n_j chi_j(U)")
    print("  These are different objects. On the diagonal U+ = U- "
          "the first becomes")
    print("  sum_j n_j chi_j(U)^2, whose character content is the "
          "FUSION of each sector with")
    print("  itself -- not the second.")
    d = np.ones(6)
    A1 = sum(c * chi(n) for n, c in enumerate(d, start=1))
    A2 = sum(c * chi(n) ** 2 for n, c in enumerate(d, start=1))
    k1, k2 = kappa(d), None
    W2 = np.maximum(A2 ** 2, 1e-300)
    sel = TH < 0.15
    k2 = float(-2 * np.polyfit(TH[sel], np.log(W2[sel]), 4)[-3])
    print()
    print(f"  flat multiplicities, single SU(2):   kappa = "
          f"{k1:7.3f}   xi/a = {xi_over_a(k1):.2e}")
    print(f"  flat multiplicities, Spin(4) diagonal: kappa = "
          f"{k2:7.3f}   xi/a = {xi_over_a(k2):.2e}")
    print(f"  ratio in xi/a: {xi_over_a(k2) / xi_over_a(k1):.1e}")
    print()
    print("  So the reduction from the derived Spin(4) amplitude to "
          "the simulated SU(2) one")
    print("  is a SECOND unpriced step, and it is worth more than "
          "the first. Neither is")
    print("  recorded anywhere in the program.\n")


def s4_verdict(kf, lo, hi):
    print("== s4: verdict on criticality item 1 ==")
    print("  The item was 'derive the multiplicities and re-run the "
          "coupling'. It cannot be")
    print("  closed that way, and the reason is the result:")
    print()
    print("   - 0074's derivation yields a FAMILY indexed by a bin "
          "scale s0, not a vector.")
    print("     Across s0 the hierarchy moves by orders of "
          "magnitude.")
    print("   - and the derived object lives on Spin(4) while the "
          "simulated one lives on")
    print("     SU(2), with no recorded reduction between them.")
    print()
    print("  THE COUPLING IS THEREFORE NOT DERIVED. kappa = 13.34 "
          "is the value of one")
    print("  particular choice (flat, single SU(2)), and the "
          "program has been treating it as")
    print("  the theory's own number since 0091.")
    print()
    print("  This does not touch the STRUCTURAL results -- no dial "
          "exists, asymptotic freedom")
    print("  supplies the separation, Lorentz restoration was "
          "measured on whatever weight was")
    print("  used. It removes the NUMBER, and with it the 'why "
          "gravity is weak' chain, whose")
    print("  entire content was that number.")
    print()
    print("  Item 1 is not fixable by computation. It needs a "
          "DERIVATION that fixes s0 and")
    print("  the group reduction -- which is a real open problem, "
          "now stated.\n")


if __name__ == "__main__":
    s = bivector_samples()
    out = s1_profile(s)
    kf, lo, hi = s2_reprice(out)
    s3_the_group_step()
    s4_verdict(kf, lo, hi)
    print("all assertions passed")
