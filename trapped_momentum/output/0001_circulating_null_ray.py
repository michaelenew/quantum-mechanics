"""
The circulating null ray: what actually drops out, and what does not.

Model. A massless excitation constrained to a closed circular path of radius r,
always moving at c. Rest energy m c^2 = the trapped energy; net translation
zero. "A photon chasing its own tail."

This script checks, numerically and to machine precision where exact:

  PART 1  spin           -- L = hbar/2 falls out with no free parameter
  PART 2  the factor 2   -- and you cannot also get E = hbar omega. Sharp.
  PART 3  de Broglie     -- BOTH E = hbar w and p = hbar k drop out of the
                            internal clock plus Lorentz. This is exact and is
                            the strongest result here.
  PART 4  time dilation  -- from one line of trigonometry on the helix
  PART 5  spin is a boost invariant, NOT reduced by acceleration (correction)
  PART 6  sqrt(pitch * lambda_dB) = lambda_Compton  (a clean three-length tie)
  PART 7  mass as trapped momentum -- the QCD ledger, which is the empirical
                            core of the whole idea

Pure stdlib. Run: python3 0001_circulating_null_ray.py
"""

import math

# ---------------------------------------------------------------- constants
H    = 6.62607015e-34            # J s (exact, SI definition)
HBAR = H / (2.0 * math.pi)       # derived, NOT a rounded literal -- Part 6
                                 # compares h- and hbar-based lengths and is
                                 # exact only if the two agree to full float
C    = 2.99792458e8      # m/s
M_E  = 9.1093837015e-31  # kg  electron
EV   = 1.602176634e-19   # J

PASS = []


def check(name, got, want, rtol=1e-12):
    ok = abs(got - want) <= rtol * max(abs(want), 1e-300)
    PASS.append((name, ok, got, want))
    return ok


def gamma(v):
    return 1.0 / math.sqrt(1.0 - (v / C) ** 2)


# ================================================================= PART 1
# Radius fixed to half the reduced Compton wavelength; everything else follows.

def zitter(m):
    """Return (radius, angular frequency, angular momentum) for r = hbar/2mc."""
    r = HBAR / (2.0 * m * C)      # half the reduced Compton wavelength
    omega = C / r                 # null constraint: tangential speed is c
    L = m * C * r                 # trapped angular momentum
    return r, omega, L


# ================================================================= PART 3
# de Broglie from an internal clock, exactly.
#
# Rest frame: internal phase  phi = omega0 * tau,  omega0 = m c^2 / hbar.
# Lab frame:  tau = gamma (t - v x / c^2), so
#             phi = (gamma omega0) t  -  (gamma omega0 v / c^2) x
#                 =        w      t   -         k             x
# Claim: w = E/hbar and k = p/hbar identically, for every v.

def de_broglie_from_clock(m, v):
    """(w, k) read off the Lorentz-transformed internal phase."""
    omega0 = m * C ** 2 / HBAR
    g = gamma(v)
    w = g * omega0
    k = g * omega0 * v / C ** 2
    return w, k


def de_broglie_standard(m, v):
    """(E/hbar, p/hbar) from the relativistic energy-momentum of a mass m."""
    g = gamma(v)
    return g * m * C ** 2 / HBAR, g * m * v / HBAR


# ================================================================= PART 4/5
# Boost along the spin axis. Transverse dimensions do not contract, so the
# circle stays a circle and the null ray traces a helix of the same radius.
#
#   pitch angle theta:  sin(theta) = v/c   (fraction of c spent translating)
#   tangential speed:   c cos(theta) = c/gamma
#   circulation rate:   omega = c cos(theta) / r = omega0 / gamma

def helix(v, r, omega0):
    theta = math.asin(v / C)
    v_tangential = C * math.cos(theta)
    omega = v_tangential / r
    return theta, v_tangential, omega


# ================================================================= PART 7
# The QCD ledger: how much of the proton is trapped momentum rather than Higgs.
QUARK_MASSES_MEV = {"up": 2.16, "down": 4.67}   # PDG current-quark masses
PROTON_MEV = 938.27208816


# ================================================================= RUN
def main():
    print("=" * 74)
    print("PART 1  --  Spin falls out with no free parameter")
    print("=" * 74)
    r, omega, L = zitter(M_E)
    print(f"  electron, r = hbar/(2 m c)")
    print(f"    radius r          = {r:.6e} m")
    print(f"    angular freq w    = {omega:.6e} rad/s")
    print(f"    L = m c r         = {L:.6e} J s")
    print(f"    hbar/2            = {HBAR / 2:.6e} J s")
    check("L = hbar/2", L, HBAR / 2.0)
    check("w = 2 m c^2 / hbar", omega, 2.0 * M_E * C ** 2 / HBAR)
    print()
    print("  L = m c r = m c (hbar / 2 m c) = hbar/2  -- the mass cancels.")
    print("  Every massive spin-1/2 particle, same answer. That is the")
    print("  single most persuasive thing about this picture: spin is not")
    print("  fitted, it is forced by 'null ray on a Compton-scale loop'.")
    print(f"  w is exactly the Dirac zitterbewegung frequency 2mc^2/hbar.")
    print()

    print("=" * 74)
    print("PART 2  --  The factor 2 you cannot get rid of")
    print("=" * 74)
    print()
    hdr = f"{'radius choice':<26}{'L / hbar':>12}{'hbar w / mc^2':>16}"
    print(hdr)
    print("-" * len(hdr))
    for label, rr in (("hbar/(2mc)  [Compton/2]", HBAR / (2 * M_E * C)),
                      ("hbar/(mc)   [Compton]", HBAR / (M_E * C))):
        ww = C / rr
        LL = M_E * C * rr
        print(f"{label:<26}{LL / HBAR:>12.4f}{HBAR * ww / (M_E * C ** 2):>16.4f}")
    check("Compton/2 gives L=hbar/2", M_E * C * (HBAR / (2 * M_E * C)) / HBAR, 0.5)
    check("Compton gives L=hbar", M_E * C * (HBAR / (M_E * C)) / HBAR, 1.0)
    print()
    print("  Right spin (hbar/2) => the loop 'photon' carries 2 mc^2.")
    print("  Right energy (mc^2) => the spin comes out hbar, i.e. spin 1.")
    print("  You may have either, not both. This is a real defect of the")
    print("  naive model and should not be papered over.")
    print()
    print("  It is also exactly where the spinor double cover lives: the")
    print("  720-degree periodicity of a spin-1/2 state is the same factor 2.")
    print("  Suggestive, not a resolution -- nothing here derives it.")
    print()

    print("=" * 74)
    print("PART 3  --  Both de Broglie relations, exactly, for free")
    print("=" * 74)
    print()
    hdr = (f"{'v/c':>8}{'w (clock)':>16}{'E/hbar':>16}"
           f"{'k (clock)':>16}{'p/hbar':>16}")
    print(hdr)
    print("-" * len(hdr))
    for beta in (0.001, 0.01, 0.1, 0.5, 0.9, 0.99, 0.999):
        v = beta * C
        w_c, k_c = de_broglie_from_clock(M_E, v)
        w_s, k_s = de_broglie_standard(M_E, v)
        print(f"{beta:>8.3f}{w_c:>16.6e}{w_s:>16.6e}{k_c:>16.6e}{k_s:>16.6e}")
        check(f"E = hbar w  at b={beta}", w_c, w_s)
        check(f"p = hbar k  at b={beta}", k_c, k_s)
    print()
    print("  Exact at every speed, to machine precision. The derivation is")
    print("  three lines: an internal clock ticking at omega0 = mc^2/hbar,")
    print("  Lorentz-transformed, IS a plane wave with w = E/hbar, k = p/hbar.")
    print("  Nothing quantum was assumed beyond 'there is an internal clock")
    print("  at the Compton frequency'. This is de Broglie's own 1924")
    print("  'harmony of phases' argument and it is the strongest support")
    print("  the circulating-null-ray picture has.")
    print()
    print("  Note also what this explains: the superluminal de Broglie PHASE")
    print("  velocity w/k = c^2/v is just the relativity of simultaneity")
    print("  applied to a clock that is synchronous in its own rest frame.")
    print("  No signal moves; the loop's phase merely desynchronises.")
    print()

    print("=" * 74)
    print("PART 4  --  Time dilation from the helix pitch angle")
    print("=" * 74)
    print()
    r0, omega0, _ = zitter(M_E)
    hdr = f"{'v/c':>8}{'theta (deg)':>14}{'v_tan/c':>12}{'w0/w':>12}{'gamma':>12}"
    print(hdr)
    print("-" * len(hdr))
    for beta in (0.0, 0.1, 0.5, 0.9, 0.99):
        v = beta * C
        th, vt, w = helix(v, r0, omega0)
        print(f"{beta:>8.2f}{math.degrees(th):>14.4f}{vt / C:>12.6f}"
              f"{omega0 / w:>12.6f}{gamma(v):>12.6f}")
        check(f"w = w0/gamma at b={beta}", w, omega0 / gamma(v))
        check(f"v_tan = c/gamma at b={beta}", vt, C / gamma(v))
    print()
    print("  sin(theta) = v/c exactly, and the transverse (circulating)")
    print("  component is c cos(theta) = c/gamma. So the loop's tick rate")
    print("  slows by exactly gamma. Time dilation is one line of")
    print("  trigonometry once you accept the speed is always c.")
    print("  Stationary = orthogonal (theta = 0), as the user described.")
    print()

    print("=" * 74)
    print("PART 5  --  CORRECTION: spin is boost-invariant, not reduced")
    print("=" * 74)
    print()
    print("  The claim was that accelerating REDUCES the trapped angular")
    print("  momentum, because the procession rate drops. Half right: the")
    print("  rate does drop by gamma. But the inertia rises by gamma too.")
    print()
    hdr = f"{'v/c':>8}{'gamma m':>14}{'v_tan':>14}{'L = gm*vtan*r':>18}{'L/hbar':>10}"
    print(hdr)
    print("-" * len(hdr))
    for beta in (0.0, 0.1, 0.5, 0.9, 0.99, 0.999):
        v = beta * C
        g = gamma(v)
        _, vt, _ = helix(v, r0, omega0)
        L = g * M_E * vt * r0
        print(f"{beta:>8.3f}{g * M_E:>14.4e}{vt:>14.4e}{L:>18.8e}{L / HBAR:>10.4f}")
        check(f"L invariant at b={beta}", L, HBAR / 2.0)
    print()
    print("  gamma * m * (c/gamma) * r = m c r. The gammas cancel exactly.")
    print("  This is a repair, not a problem: spin magnitude IS a Poincare")
    print("  Casimir invariant, so a model in which it changed under boost")
    print("  would be wrong. The model gets this right automatically.")
    print()

    print("=" * 74)
    print("PART 6  --  The three lengths close: sqrt(pitch * lambda_dB) = l_C")
    print("=" * 74)
    print()
    lam_C = H / (M_E * C)
    hdr = (f"{'v/c':>8}{'pitch (m)':>15}{'lambda_dB (m)':>15}"
           f"{'sqrt(prod)':>15}{'lambda_C':>15}")
    print(hdr)
    print("-" * len(hdr))
    for beta in (0.01, 0.1, 0.5, 0.9):
        v = beta * C
        g = gamma(v)
        omega_lab = omega0_c = M_E * C ** 2 / HBAR   # internal clock, rest frame
        pitch = v * g * (2.0 * math.pi / omega0_c)   # advance per lab-frame tick
        lam_dB = H / (g * M_E * v)
        print(f"{beta:>8.3f}{pitch:>15.6e}{lam_dB:>15.6e}"
              f"{math.sqrt(pitch * lam_dB):>15.6e}{lam_C:>15.6e}")
        check(f"geometric mean = lambda_C at b={beta}",
              math.sqrt(pitch * lam_dB), lam_C)
    print()
    print("  pitch ~ v, lambda_dB ~ 1/v, and their product is v-independent:")
    print("    pitch * lambda_dB = (2 pi c / omega0)^2 = (h/mc)^2")
    print("  The Compton wavelength is the geometric mean of the helix pitch")
    print("  and the de Broglie wavelength, at every speed.")
    print()
    print("  Worth flagging as a TRAP: the de Broglie wavelength is NOT the")
    print("  helix pitch. They scale oppositely in v. lambda_dB belongs to")
    print("  the phase wave (Part 3), not to the visible winding.")
    print()

    print("=" * 74)
    print("PART 7  --  'Mass is trapped momentum' is already true for hadrons")
    print("=" * 74)
    print()
    quark_sum = 2 * QUARK_MASSES_MEV["up"] + QUARK_MASSES_MEV["down"]
    frac_higgs = quark_sum / PROTON_MEV
    print(f"  proton mass                 = {PROTON_MEV:.4f} MeV/c^2")
    print(f"  sum of current quark masses = {quark_sum:.4f} MeV/c^2  (uud)")
    print(f"  from the Higgs mechanism    = {100 * frac_higgs:.3f} %")
    print(f"  from confined energy-momentum "
          f"= {100 * (1 - frac_higgs):.3f} %")
    check("higgs fraction ~1%", round(100 * frac_higgs, 3), 0.958, rtol=1e-3)
    print()
    print("  ~99% of the mass of ordinary matter already IS trapped momentum:")
    print("  kinetic and binding energy of near-massless quarks and strictly")
    print("  massless gluons, confined. The reframing is not speculative for")
    print("  hadrons -- it is the Standard Model's own accounting.")
    print()
    print("  And the equivalence principle comes along for free: confined")
    print("  energy-momentum sources gravity as E/c^2 in GR, so inertial and")
    print("  gravitational mass agree for trapped momentum as a theorem, not")
    print("  an assumption. That is the user's point (3), and it holds.")
    print()

    print("=" * 74)
    print("SELF-CHECKS")
    print("=" * 74)
    bad = [p for p in PASS if not p[1]]
    for name, ok, got, want in PASS:
        flag = "ok" if ok else "FAIL"
        print(f"  [{flag}] {name:<40} {got:.10e}")
    print()
    print(f"  {len(PASS) - len(bad)}/{len(PASS)} checks passed.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
