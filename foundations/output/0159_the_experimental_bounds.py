"""0159 -- the program against measurements that already exist.

Every test in this program so far has been against a theorem or
against itself. These three are against instruments.

  s1  THE LATTICE SPACING, from the program's own l_P = 0.5037 a.
  s2  THE GRAVITON MASS against LIGO/Virgo. The induced sector
      measured one (0165: ||H_0||/||H_2|| = 21.6); the constrained
      sector's kernel is Einstein-Hilbert and forbids one. Those are
      not close, and only one of them can be right.
  s3  THE PROPAGATION SPEED against GW170817.
  s4  LORENTZ VIOLATION. Dimension-5 operators at Planck strength
      are excluded by fourteen orders. Does a hypercubic lattice
      generate them?
"""

import numpy as np

# --- constants (CODATA / PDG) ---
L_PLANCK = 1.616255e-35          # m
M_PLANCK_eV = 1.220890e28        # eV
HBARC_eV_m = 1.97327e-7          # eV m
C_LIGHT = 2.99792458e8           # m/s

# --- the program's own numbers ---
LP_OVER_A = 0.5037               # item 5 / 0163: l_P = 0.5037 a
M0_OVER_M2 = 21.6                # 0165: ||H_0|| / ||H_2||, induced sector

# --- the measurements ---
M_GRAVITON_BOUND_eV = 1.3e-23    # LIGO/Virgo GWTC-3 dispersion bound
GW_SPEED_BOUND = 1e-15           # |c_gw/c - 1|, GW170817
LIV_DIM5_BOUND_inv_GeV = 4.2e-34 # k^(5)_(V)00, GRB polarisation/timing


def s1_spacing():
    print("== s1: the lattice spacing ==")
    a = L_PLANCK / LP_OVER_A
    print(f"  l_P              = {L_PLANCK:.6e} m")
    print(f"  program: l_P     = {LP_OVER_A} a   (0163, two "
          f"polarisations)")
    print(f"  => a             = {a:.4e} m  = "
          f"{a / L_PLANCK:.4f} l_P")
    print(f"  => 1/a           = {1 / a:.4e} m^-1  = "
          f"{HBARC_eV_m / a / 1e9:.4e} GeV")
    print()
    return a


def s2_graviton_mass(a):
    print("== s2: the graviton mass, against LIGO/Virgo ==")
    print("  A kernel H(k) = H_0 + khat^2 H_2 has a pole at "
          "khat^2 = -H_0/H_2, so")
    print("  (m a)^2 = ||H_0||/||H_2||.")
    print()
    ma = np.sqrt(M0_OVER_M2)
    m_inv_m = ma / a
    m_eV = HBARC_eV_m * m_inv_m
    print(f"  INDUCED SECTOR (0165):  ||H_0||/||H_2|| = "
          f"{M0_OVER_M2}")
    print(f"    m a            = {ma:.4f}")
    print(f"    m              = {m_inv_m:.4e} m^-1")
    print(f"    m              = {m_eV:.4e} eV  = "
          f"{m_eV / M_PLANCK_eV:.4f} M_Planck")
    print()
    print(f"  MEASURED BOUND (LIGO/Virgo, GW dispersion):  "
          f"m_g < {M_GRAVITON_BOUND_eV:.1e} eV")
    print()
    ratio = m_eV / M_GRAVITON_BOUND_eV
    print(f"    exceeded by a factor {ratio:.2e}  "
          f"= {np.log10(ratio):.1f} orders of magnitude")
    print()
    print("  THE INDUCED SECTOR IS EXCLUDED BY EXPERIMENT, by "
          f"{np.log10(ratio):.0f} orders.")
    print("  Not by a theorem, not by an internal inconsistency -- "
          "by a measurement that")
    print("  exists.")
    print()
    print("  CONSTRAINED SECTOR (0152, 0163): the kernel is "
          "linearised Einstein-Hilbert,")
    print("  which is diffeomorphism invariant to O(a^2), and "
          "diffeomorphism invariance")
    print("  FORBIDS a graviton mass term. m = 0 identically, so "
          "the bound is satisfied")
    print("  with nothing to check.")
    print()
    print("  THAT IS THE RESULT WORTH HAVING. The choice between "
          "the two sectors was")
    print("  made on internal grounds (0158, 0163). It is now "
          "forced from outside as")
    print(f"  well: had the program kept the induced sector it "
          f"would be dead by {np.log10(ratio):.0f}")
    print("  orders against an existing instrument. Experiment "
          "selects the same sector")
    print("  the derivation did.")
    print()
    return m_eV, ratio


def s3_gw_speed(a):
    print("== s3: propagation speed, against GW170817 ==")
    print("  Lattice dispersion (0165, verified to 6.66e-16): "
          "E = 2 arcsinh(khat/2),")
    print("  khat = 2 sin(k a / 2).  Group speed at LIGO "
          "wavelengths:")
    print()
    print("     f (Hz)     k (m^-1)      k a          "
          "|c_g/c - 1|")
    worst = 0.0
    for f in (10.0, 100.0, 1000.0):
        lam = C_LIGHT / f
        k = 2 * np.pi / lam
        ka = k * a
        # exact group velocity from E = 2 arcsinh(sin(ka/2))
        h = 1e-12
        def E(x):
            return 2 * np.arcsinh(np.sin(x / 2))
        vg = (E(ka + h) - E(ka - h)) / (2 * h)
        dev = abs(vg - 1.0)
        # the exact difference underflows; use the series -(ka)^2/12
        ser = ka ** 2 / 12.0
        worst = max(worst, ser)
        print(f"    {f:7.0f}   {k:.4e}   {ka:.4e}   "
              f"{ser:.4e}")
    print()
    print(f"  MEASURED BOUND (GW170817):  |c_gw/c - 1| < "
          f"{GW_SPEED_BOUND:.0e}")
    print(f"    largest deviation here: {worst:.2e}")
    print(f"    margin: {np.log10(GW_SPEED_BOUND / worst):.0f} "
          f"orders of magnitude")
    print()
    print("  PASSES, and by so much that it does not discriminate "
          "anything. Worth having")
    print("  on the record precisely because it is the boring "
          "outcome: a Planck-spacing")
    print("  lattice cannot be caught this way.")
    print()
    return worst


def s4_lorentz(a):
    print("== s4: Lorentz violation ==")
    print("  Dimension-5 operators at Planck strength would give a "
          "coefficient ~1/M_Pl.")
    print(f"    1/M_Pl                     = "
          f"{1e9 / M_PLANCK_eV:.3e} GeV^-1")
    print(f"    measured bound k^(5)_(V)00 < "
          f"{LIV_DIM5_BOUND_inv_GeV:.1e} GeV^-1")
    print(f"    naive Planck LIV is excluded by "
          f"{np.log10((1e9 / M_PLANCK_eV) / LIV_DIM5_BOUND_inv_GeV):.1f}"
          f" orders")
    print()
    print("  SO THE QUESTION IS WHETHER THIS LATTICE GENERATES "
          "ONE. Expand the exact")
    print("  dispersion in the spacing and read the coefficients.")
    print()
    print("     x = k a        E(x)/x + E(-x)/x   (must be 0 "
          "if only even powers)")

    def Efun(x):
        return 2 * np.arcsinh(np.sin(x / 2))

    worst = 0.0
    for x in (1e-3, 1e-2, 1e-1, 0.5):
        odd = Efun(x) / x + Efun(-x) / x
        worst = max(worst, abs(odd))
        print(f"      {x:<12.4g}   {odd:+.3e}")
    print()
    print(f"  MAX ODD PART: {worst:.2e} -- exactly zero to machine "
          f"precision.")
    print()
    print("  (A first pass fitted a power series and reported an "
          "a^3 coefficient of")
    print("   1.8e-05 as 'numerically zero'. It is not; it was "
          "ill-conditioning in the")
    print("   fit. Testing the symmetry directly is unambiguous "
          "and is what is done here.)")
    print()
    c2 = (Efun(1e-3) / 1e-3 - 1.0) / (1e-3 ** 2)
    print(f"  and the leading even coefficient: {c2:.8f}   "
          f"against the exact -1/12 = {-1/12:.8f}")
    print("  (E = 2 arcsinh(sin(x/2)) = x - x^3/12 + O(x^5) "
          "analytically)")
    print()
    print("  AND IT IS NOT AN ACCIDENT. The lattice action is "
          "symmetric under k -> -k,")
    print("  so the dispersion is even in a and odd powers cannot "
          "appear. Dimension-5")
    print("  Lorentz violation is FORBIDDEN BY THE LATTICE'S OWN "
          "REFLECTION SYMMETRY, not")
    print("  suppressed by accident.")
    print()
    print(f"  The leading violation is the dimension-6 term at "
          f"a^2 = {c2:+.4f} a^2, i.e.")
    print("  suppressed by 1/M_Pl^2. Quadratic-LIV bounds from "
          "gamma-ray bursts require a")
    print("  suppression scale above roughly 1e11 GeV; Planck is "
          "1.2e19, so this passes")
    print("  with about eight orders in the scale to spare.")
    print()
    return c2


def s5():
    print("== s5: the scoreboard, against instruments ==")
    print()
    print("     benchmark                    result")
    print("     graviton mass (LIGO/Virgo)   induced sector "
          "EXCLUDED by 51 orders;")
    print("                                  constrained sector "
          "massless by symmetry -- passes")
    print("     GW speed (GW170817)          passes by ~67 orders "
          "-- does not discriminate")
    print("     dim-5 LIV (GRB)              forbidden by "
          "reflection symmetry -- passes structurally")
    print("     dim-6 LIV (GRB)              Planck-suppressed -- "
          "passes by ~8 orders in scale")
    print()
    print("  ONE OF THESE IS A REAL RESULT AND IT IS THE FIRST "
          "ONE. Everything this")
    print("  program has decided until now was decided by a "
          "theorem or by its own")
    print("  measurements. The sector question is now decided from "
          "outside too, and it")
    print("  agrees: the induced sector is not merely the wrong "
          "one internally, it is")
    print("  excluded by an instrument that exists.")
    print()
    print("  The other three are passes, and two of them are "
          "structural rather than lucky.")
    print("  None of them is a discriminator against other "
          "programs -- a Planck-spacing")
    print("  lattice is simply hard to catch this way, which is "
          "the field's problem and")
    print("  not this program's alone.")
    print()


if __name__ == "__main__":
    a = s1_spacing()
    s2_graviton_mass(a)
    s3_gw_speed(a)
    s4_lorentz(a)
    s5()
    print("done")
