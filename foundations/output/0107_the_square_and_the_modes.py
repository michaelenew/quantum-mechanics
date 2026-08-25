"""0107 -- what the completion agrees with, what the modes count to,
and what the Born square actually buys.

Three standing obstructions, each moved.

  s1  THE SCALAR/TENSOR FACTOR IS A STRONG-FIELD DIFFERENCE, NOT A
      WEAK-FIELD ONE. The completion's transmission is
      psi = 1 - G M / r EXACTLY; GR's lapse is
      N = sqrt(1 - 2 G M / r). These agree to FIRST ORDER in
      G M / r -- same Newtonian potential AND same redshift -- and
      differ only in the nonlinear completion. So the 'named factor
      2' in r_h is not a discrepancy in the regime where the
      correspondence was built; it is a statement about how the two
      theories continue to strong field. Measured deviation vs
      field strength below.
  s2  THE MODE COUNT REACHES 2, WITH EVERY INGREDIENT NAMED. A
      symmetric spatial tensor has 6 components. Local frame
      rotation is gauge (their 0026, exact). Node relabelling --
      the filter has no preferred names for its nodes -- is the
      diffeomorphism analogue, 3 more. The Gauss law (0109: the
      boundary reads exactly the enclosed content) is one
      constraint. 6 - 3 - 1 = 2. Stated as a COUNTING argument
      whose ingredients are all objects this program already owns;
      the tensor dynamics itself is still not derived.
  s3  WHAT THE BORN SQUARE BUYS: BAND LIMITING. In the character
      basis the derived weight |A|^2 has NONNEGATIVE INTEGER
      coefficients that vanish EXACTLY above 2J -- a strictly
      band-limited weight. A heat kernel (what record noise can
      make, their 0027) has coefficients e^{-tau j(j+1)}: positive
      at EVERY j, never zero. The nodes in real space are the
      signature of finite support in the dual. So the Born square
      is what implements the LEVEL CUTOFF, and the standing
      question 'why squared' becomes 'why band-limited' -- a
      question in the program's own currency (the level N).
  s4  A CONSISTENCY CHECK ON THE INDUCED-GRAVITY IDENTIFICATION.
      That identification (0115) fixed the Planck length at 2.27 a
      from the measured area-law coefficient. Independently, the
      information and geometry mass bounds cross at sqrt(3) = 1.73
      a -- a number containing no alpha at all. Two Planck-scale
      estimates from unrelated inputs agreeing to ~30% is evidence
      for the identification, not proof; recorded as such.
"""

import numpy as np

TH = np.linspace(1e-9, np.pi - 1e-9, 400001)
HAAR = (2 / np.pi) * np.sin(TH) ** 2


def s1_linear_agreement():
    print("== s1: the factor 2 is a strong-field difference ==")
    print("   G M / r    psi = 1 - x    N = sqrt(1 - 2x)    "
          "(psi - N)/x^2")
    ratios = []
    for x in (0.001, 0.01, 0.05, 0.1, 0.3):
        psi = 1 - x
        N = np.sqrt(1 - 2 * x)
        ratios.append((psi - N) / x ** 2)
        print(f"   {x:.3f}      {psi:.5f}        {N:.5f}"
              f"          {ratios[-1]:.4f}")
    # the difference is second order with leading coefficient 1/2
    assert abs(ratios[0] - 0.5) < 0.01
    assert abs(ratios[1] - 0.5) < 0.02
    print("  psi - N = -(1/2)(GM/r)^2 + ...: the two agree at FIRST "
          "order (same Newtonian")
    print("  potential, same redshift) and part company only in the "
          "nonlinear completion.")
    print("  Horizons: psi = 0 at r = GM, N = 0 at r = 2GM -- the "
          "factor 2 lives entirely")
    print("  in the strong field, not in the regime where the "
          "correspondence was built\n")


def s2_mode_count():
    print("== s2: the mode count ==")
    d = 3
    frame = d * d                      # local frame e_i^a
    rot = d * (d - 1) // 2             # local rotations of the frame
    comps = frame - rot                # = symmetric metric/precision
    relabel = d                        # node relabelling
    gauss = 1                          # boundary reads enclosed
    print(f"   local frame components e_i^a             : {frame}")
    print(f"   local frame rotation (their 0026, exact) : -{rot}"
          f"  [frame <-> metric redundancy]")
    print(f"   => symmetric precision/metric field      :  {comps}")
    print(f"   node relabelling (no preferred names)    : -{relabel}"
          f"  [the diffeomorphism analogue]")
    print(f"   Gauss law (0109: boundary = enclosed)    : -{gauss}"
          f"  [constraint]")
    left = comps - relabel - gauss
    print(f"   propagating                              :  {left}")
    assert comps == 6 and left == 2
    print("  every ingredient is an object this program already "
          "owns, and the count lands")
    print("  on 2. Reconciling with 0026: that stone quotiented a "
          "SINGLE node's precision by")
    print("  local rotation and was left with its eigenvalues -- "
          "the frame<->metric")
    print("  redundancy. In the field theory that quotient is spent "
          "identifying P with the")
    print("  metric; it must not be subtracted a second time. This "
          "is a COUNTING argument:")
    print("  the tensor field equations are still not derived, and "
          "the count must survive")
    print("  them\n")


def coeffs_of(weight, jmax=8.0):
    js = np.arange(0, jmax + 0.1, 0.5)
    out = []
    for j in js:
        chi = np.sin((2 * j + 1) * TH) / np.sin(TH)
        out.append(float(np.trapezoid(weight * chi * HAAR, TH)))
    return js, np.array(out)


def s3_band_limited():
    print("== s3: what the Born square buys ==")
    J = 2.5
    A = sum(np.sin((2 * j + 1) * TH) / np.sin(TH)
            for j in np.arange(0, J + 0.1, 0.5))
    W = A ** 2
    js, c = coeffs_of(W)
    cut = 2 * J
    below = c[js <= cut]
    above = c[js > cut]
    print(f"  |A|^2 with J = {J}: character coefficients up to "
          f"2J = {cut}:")
    print("   " + "  ".join(f"{v:.2f}" for v in below))
    print(f"  max |coefficient| ABOVE 2J: {np.abs(above).max():.2e} "
          f"-> EXACTLY band-limited")
    assert np.abs(above).max() < 1e-6
    assert np.abs(below - np.round(below)).max() < 1e-5
    print("  (and every coefficient below the cut is a nonnegative "
          "INTEGER: fusion counts)")
    # a heat kernel: positive at every j, never zero
    tau = 0.2
    kc = np.array([(2 * j + 1) * np.exp(-tau * j * (j + 1))
                   for j in js])
    print(f"  heat kernel K_{tau}: coefficient at j = 8 is "
          f"{kc[-1]:.2e} > 0 -- positive at EVERY j")
    assert kc.min() > 0
    print("  the real-space NODES are the dual-space CUTOFF. Record "
          "noise makes heat")
    print("  kernels (their 0027) and can never be band-limited; "
          "the Born square is what")
    print("  implements the level cutoff. 'Why squared' becomes "
          "'why band-limited' --")
    print("  a question in the program's own currency, the level N\n")


def s4_planck_consistency():
    print("== s4: a consistency check on induced gravity ==")
    alpha_scalar, pol = 0.0242, 2
    G = 1 / (4 * pol * alpha_scalar)
    lp = np.sqrt(G)
    cross = np.sqrt(3.0)
    print(f"  induced-gravity Planck length (from the measured "
          f"area law): {lp:.3f} a")
    print(f"  information/geometry bound crossover (contains no "
          f"alpha):        {cross:.3f} a")
    print(f"  agreement: {100 * abs(lp / cross - 1):.0f}%")
    assert abs(lp / cross - 1) < 0.4
    print(f"  two Planck-scale estimates from unrelated inputs "
          f"landing within "
          f"{100 * abs(lp / cross - 1):.0f}% is")
    print("  EVIDENCE for the identification, not proof -- a factor "
          "that could have been")
    print("  astronomically off is not. Recorded as such\n")


if __name__ == "__main__":
    s1_linear_agreement()
    s2_mode_count()
    s3_band_limited()
    s4_planck_consistency()
    print("all assertions passed")
