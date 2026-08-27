"""0076 -- the quarter: confronting the horizon accounts with A/4G.

C4 of path C (0070), run with everything C1-C3 measured. Three
verdicts, each an assembly of measured numbers plus small exact
checks; 0070 said to treat a mismatch as a finding, and there is one.

  s1  THE 1/4 IS LOCATED, NOT DERIVED. Identifying the measured
      vacuum-cut entropy S/A with the Bekenstein-Hawking A/4G fixes
      the lattice spacing at the Planck scale with an O(1) measured
      coefficient: a = 0.440 l_P (NN stencil), a = 0.621 l_P
      (program's CD stencil), a = 0.378 l_P if the capacity account
      is charged instead. Regulator dependence moves a/l_P by O(1) --
      the Sakharov trade, exactly as 0082 s4 anticipated: the 1/4
      lives in the induced sector, and a bare match was never on
      offer.
  s2  THE FINDING: THE DEFICIT LEDGER CANNOT BE THE BH CHARGE. The
      program's deficit additivity (0012) makes the total deficit
      sourced by a mass M equal 8 pi G M, and on a Schwarzschild
      horizon A = 16 pi G^2 M^2 this is 2 sqrt(pi A): G drops out and
      it scales as sqrt(A) -- while the measured vacuum-cut deficit
      (0084) is area-extensive. Two accounts, two roles: the deficit
      is the SOURCE ledger (mass-extensive), the entropy/capacity is
      the RECORD account (area-extensive), and only the latter can be
      Bekenstein-Hawking. They cross at A* ~ 1.2e3 a^2 (R* ~ 4 l_P):
      above ~5 l_P every horizon's zero-point record dwarfs its
      sourced deficit. Consequence: the vacuum's area-extensive
      record must NOT source deficit (else a curvature catastrophe at
      every cut) -- which is exactly the zero-mode/budget deletion
      (0069/0080) doing its unimodular job. Path C and path Lambda
      protect each other.
  s3  THE SATURATED-CHANNEL PICTURE, SHARPENED. Per channel
      delta = 2 pi (1 - 1/(2 nu)) saturates at the full turn 2 pi;
      99% saturation at record I = ln 100 = 4.6 nats. A saturated
      channel in 3+1 is a string defect of extremal tension
      mu = 1/4G (delta = 8 pi G mu = 2 pi closes the cone), and a
      mass M's worth of extremal string has total length
      L = M/mu = 4 G M = 2 R_s: THE DIAMETER, G-independent. The
      horizon's source structure is one-dimensional (2 R_s of
      extremal string -- the string defects Ambrose-Singer left the
      finite sector, 0061 s4) while its record structure is
      two-dimensional (the area law). Conjecture shape, stated for
      falsification: horizon = ~R_s/l_P saturated source channels
      + A/l_P^2 of vacuum record.
"""

import numpy as np


# ----------------------------------------------------------------------
# re-measure the area coefficients (C1 machinery, self-contained)
# ----------------------------------------------------------------------

def chain_entropy_nus(m2, L, cut, stencil):
    if stencil == "nn":
        K = (m2 + 2.0) * np.eye(L)
        for i in range(L - 1):
            K[i, i + 1] = K[i + 1, i] = -1.0
    else:
        K = (m2 + 0.5) * np.eye(L)
        for i in range(L - 2):
            K[i, i + 2] = K[i + 2, i] = -0.25
    w, U = np.linalg.eigh(K)
    sq = U @ np.diag(np.sqrt(w)) @ U.T
    isq = U @ np.diag(1.0 / np.sqrt(w)) @ U.T
    X = isq[:cut, :cut] / 2.0
    P = sq[:cut, :cut] / 2.0
    nu = np.sqrt(np.clip(np.linalg.eigvals(X @ P).real, 0.25, None))
    a, b = nu + 0.5, np.clip(nu - 0.5, 1e-300, None)
    S = float(np.sum(a * np.log(a) - b * np.log(b)))
    D = float(2 * np.pi * np.sum(1 - 1 / (2 * nu)))
    W = float(np.sum(4 * nu ** 2 - 1))
    return S, W, D


def area_coeffs(n_perp, L, stencil):
    tot = np.zeros(3)
    for ix in range(n_perp):
        for iy in range(n_perp):
            kx = 2 * np.pi * ix / n_perp
            ky = 2 * np.pi * iy / n_perp
            if stencil == "nn":
                mp2 = 4 * np.sin(kx / 2) ** 2 + 4 * np.sin(ky / 2) ** 2
            else:
                mp2 = np.sin(kx) ** 2 + np.sin(ky) ** 2
            tot += chain_entropy_nus(mp2 + 1e-6, L, L // 2, stencil)
    return tot / n_perp ** 2


def s1_locate_the_quarter():
    print("== s1: locating the 1/4 ==")
    rows = {}
    for stencil in ("nn", "cd"):
        S, W, D = area_coeffs(32, 64, stencil)
        rows[stencil] = (S, W, D)
        for name, coef in (("entropy", 2 * S), ("capacity", 2 * W)):
            G = 1 / (4 * coef)              # units of a^2
            a_over_lp = 1 / np.sqrt(G)
            print(f"  {stencil.upper()} {name:8s}: graviton coeff "
                  f"{coef:.4f}/a^2 -> G = {G:.3f} a^2 -> a = "
                  f"{a_over_lp:.3f} l_P")
    a_nn = 1 / np.sqrt(1 / (4 * 2 * rows['nn'][0]))
    assert 0.3 < a_nn < 0.6, "identification not at the Planck scale"
    print("  the identification works ONLY as a cutoff-fixing "
          "(Sakharov/induced) statement:")
    print("  the 1/4 is located in the renormalized sector, with a "
          "measured O(1) coefficient;")
    print("  regulator choice moves a/l_P by O(1) -- no bare match "
          "exists, as 0082 s4 said\n")
    return rows


def s2_the_finding(rows):
    print("== s2: the deficit ledger cannot be the BH charge ==")
    # program theorem (additivity, 0012): delta_tot(M) = 8 pi G M.
    # Schwarzschild: A = 16 pi G^2 M^2 => delta_tot = 2 sqrt(pi A).
    for G in (1.0, 0.1, 25.0):
        for M in (1.0, 7.0):
            A = 16 * np.pi * G * G * M * M
            assert abs(8 * np.pi * G * M - 2 * np.sqrt(np.pi * A)) \
                < 1e-12 * 8 * np.pi * G * M
    print("  source ledger: delta_tot = 8 pi G M = 2 sqrt(pi A) -- "
          "G-independent, ~ sqrt(A)")
    # measured record ledger: area-extensive (0084; re-verify drift)
    d16 = area_coeffs(16, 64, "nn")[2]
    d32 = rows['nn'][2]
    drift = abs(d16 - d32) / d32
    print(f"  record ledger: vacuum-cut delta/A = {d32:.4f} "
          f"rad/plaquette (N_perp 16->32 drift {100 * drift:.1f}%: "
          f"area law)")
    assert drift < 0.10
    dA = 2 * d32                              # graviton, 2 polarizations
    Astar = 4 * np.pi / dA ** 2
    Rstar = np.sqrt(Astar / (4 * np.pi))
    print(f"  the accounts cross at A* = {Astar:.0f} a^2, R* = "
          f"{Rstar:.1f} a ~ {Rstar * 0.44:.1f} l_P (NN):")
    print("  above ~5 l_P the zero-point record dwarfs the sourced "
          "deficit -- so the vacuum's")
    print("  record must NOT source (else curvature catastrophe at "
          "every cut): the budget/zero-mode")
    print("  deletion (0069/0080) is what protects it. Verdict: "
          "deficit = source ledger (~M),")
    print("  entropy/capacity = record account (~A); only the record "
          "account can be Bekenstein-Hawking\n")


def s3_saturated_channels():
    print("== s3: the saturated-channel picture, sharpened ==")
    nus = np.array([0.5, 0.6, 1.0, 5.0, 50.0, 5000.0])
    delta = 2 * np.pi * (1 - 1 / (2 * nus))
    assert np.all(np.diff(delta) > 0) and delta[-1] < 2 * np.pi
    print("  per-channel deficit 2pi(1 - 1/2nu): monotone, capped at "
          "the full turn 2 pi")
    nu99 = 50.0
    I99 = np.log(2 * nu99)
    assert abs(2 * np.pi * (1 - 1 / (2 * nu99)) / (2 * np.pi) - 0.99) \
        < 1e-12
    print(f"  99% saturation at record I = ln(2 nu) = {I99:.3f} nats")
    # extremal string: mu = 1/4G closes the cone; M/mu = 4GM = 2 R_s
    for G in (1.0, 2.0, 0.3):
        M = 3.0
        assert abs(M / (1 / (4 * G)) - 2 * (2 * G * M)) < 1e-12
    print("  extremal tension mu = 1/4G (delta = 8 pi G mu = 2 pi); a "
          "mass M's worth of extremal")
    print("  string has length L = M/mu = 4GM = 2 R_s: the DIAMETER, "
          "G-independent --")
    print("  the horizon's source structure is one-dimensional "
          "(0061 s4's string defects),")
    print("  its record structure two-dimensional (the area law). "
          "Falsifiable shape:")
    print("  horizon = ~R_s/l_P saturated source channels + A/l_P^2 "
          "of vacuum record\n")


if __name__ == "__main__":
    rows = s1_locate_the_quarter()
    s2_the_finding(rows)
    s3_saturated_channels()
    print("all assertions passed")
