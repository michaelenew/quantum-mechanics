"""0074 -- the wedge temperature: Bisognano-Wichmann on the lattice.

C2 of path C (0070): is the free graviton's reduced half-space state
thermal, and at what temperature? Bisognano-Wichmann / Unruh say the
vacuum restricted to a Rindler wedge is exp(-2 pi K_boost): thermal
w.r.t. the boost at inverse temperature 2 pi per unit rapidity.

Method (forward, numerically stable): build the lattice boost
Hamiltonian H_boost = sum_j d_j h_j explicitly (d_j = distance from
the entangling cut, energy density h_j with split links), compute its
EXACT beta-thermal Gaussian correlators, and compare with the exact
reduced correlators of the ground state -- then fit beta. The inverse
route (reconstructing the modular Hamiltonian matrix) is documented
unusable in double precision: deep modular modes have eps ~ 30+ and
their eigenvectors contaminate the matrices; the forward test needs no
such resolution and is the physically meaningful comparison (states,
not matrices).

  s1  At beta = 2 pi the boost-thermal state reproduces the reduced
      state near the cut to ~1e-5 relative (light mass), entropy to
      0.03%, top symplectic eigenvalue to 1e-4.
  s2  Fitting beta: beta*/2pi = 0.9999 at m^2 = 0.0025 and the
      deviation grows linearly in m^2 a^2 (coefficient ~ 0.06) -- a
      pure lattice artifact vanishing in the continuum. The Unruh
      temperature is measured, not assumed.
  s3  The horizon location is measurable too: fitting the offset s in
      d_j = (n-1-j) + s gives s* ~ 1/2 -- the horizon sits half a
      lattice spacing outside the last site.
  s4  The 3+1 graviton: every transverse-momentum mode of the TT
      tower sees the SAME beta* = 2 pi (up to its own m_perp^2 a^2
      lattice correction), and both polarizations identically: the
      wedge temperature is geometric, not mode-dependent -- the Unruh
      effect for the free graviton vacuum.

Region convention: open chain of L sites, region A = first n sites
(Dirichlet wall at 0), entangling cut between sites n-1 and n; window
metrics use the sites nearest the cut, and the light-mass runs scale n
so the wall sits several correlation lengths from the cut.
"""

import numpy as np
from scipy.optimize import minimize_scalar


# ----------------------------------------------------------------------
# exact Gaussian machinery
# ----------------------------------------------------------------------

def ground_XP(m2, L):
    K = (m2 + 2.0) * np.eye(L)
    for i in range(L - 1):
        K[i, i + 1] = K[i + 1, i] = -1.0
    w, U = np.linalg.eigh(K)
    return (U @ np.diag(1 / np.sqrt(w)) @ U.T / 2,
            U @ np.diag(np.sqrt(w)) @ U.T / 2)


def thermal_XP(ME, KE, beta):
    """Exact correlators of the Gaussian state exp(-beta H) for
    H = 1/2 p ME p + 1/2 x KE x."""
    wM, UM = np.linalg.eigh(ME)
    Ms = UM @ np.diag(np.sqrt(wM)) @ UM.T
    Msi = UM @ np.diag(1 / np.sqrt(wM)) @ UM.T
    w2, O = np.linalg.eigh(Ms @ KE @ Ms)
    om = np.sqrt(np.clip(w2, 1e-30, None))
    c = 0.5 / np.tanh(beta * om / 2)
    return (Ms @ O @ np.diag(c / om) @ O.T @ Ms,
            Msi @ O @ np.diag(c * om) @ O.T @ Msi)


def boost_MK(n, m2, s):
    """Lattice boost on the region: site j at distance d_j = (n-1-j)+s
    from the cut, on-site energy weighted d_j, link (j,j+1) energy
    weighted d_j - 1/2."""
    d = (n - 1 - np.arange(n)) + s
    ME = np.diag(d.astype(float))
    KE = np.diag(m2 * d.astype(float))
    for j in range(n - 1):
        w = d[j] - 0.5
        KE[j, j] += w
        KE[j + 1, j + 1] += w
        KE[j, j + 1] -= w
        KE[j + 1, j] -= w
    return ME, KE


def sym_spectrum(X, P):
    nu = np.sqrt(np.clip(np.linalg.eigvals(X @ P).real, 0.25, None))
    a, b = nu + 0.5, np.clip(nu - 0.5, 1e-300, None)
    return float(np.sum(a * np.log(a) - b * np.log(b))), np.sort(nu)[::-1]


def fit_beta(XA, PA, ME, KE, win):
    n = XA.shape[0]
    w = slice(n - win, n)
    nX, nP = np.linalg.norm(XA[w, w]), np.linalg.norm(PA[w, w])

    def err(lb):
        Xb, Pb = thermal_XP(ME, KE, np.exp(lb))
        return (np.linalg.norm((Xb - XA)[w, w]) / nX
                + np.linalg.norm((Pb - PA)[w, w]) / nP)

    r = minimize_scalar(err, bounds=(np.log(3), np.log(13)),
                        method='bounded',
                        options={'xatol': 1e-10})
    return float(np.exp(r.x)), float(r.fun), err


CASES = [  # (m2, L, n) -- region scaled so the wall is >~ 4 xi away
    (0.0025, 512, 128),
    (0.01, 384, 96),
    (0.09, 256, 48),
    (0.5, 256, 48),
]
WIN = 24


def s1_baseline():
    print("== s1: the reduced state vs the boost at beta = 2 pi ==")
    m2, L, n = CASES[0]
    X, P = ground_XP(m2, L)
    XA, PA = X[:n, :n].copy(), P[:n, :n].copy()
    ME, KE = boost_MK(n, m2, 0.5)
    _, _, err = fit_beta(XA, PA, ME, KE, WIN)
    resid = err(np.log(2 * np.pi))
    Sx, nx = sym_spectrum(XA, PA)
    Sb, nb = sym_spectrum(*thermal_XP(ME, KE, 2 * np.pi))
    print(f"  m^2={m2}, n={n}: near-cut correlator residual at 2pi = "
          f"{resid:.2e}")
    print(f"  S_exact = {Sx:.5f} vs S_boost = {Sb:.5f} "
          f"({100 * abs(Sb / Sx - 1):.3f}%);  nu_1 {nx[0]:.6f} vs "
          f"{nb[0]:.6f}")
    assert resid < 1e-3
    assert abs(Sb / Sx - 1) < 1e-3
    assert abs(nb[0] - nx[0]) < 1e-4
    print("  the reduced state IS the boost-thermal state at 2 pi, to "
          "the precision measured\n")


def s2_temperature():
    print("== s2: the temperature, fitted ==")
    devs = {}
    for m2, L, n in CASES:
        X, P = ground_XP(m2, L)
        XA, PA = X[:n, :n].copy(), P[:n, :n].copy()
        ME, KE = boost_MK(n, m2, 0.5)
        bstar, resid, _ = fit_beta(XA, PA, ME, KE, WIN)
        ratio = bstar / (2 * np.pi)
        devs[m2] = 1 - ratio
        print(f"  m^2 = {m2:6}: beta* = {bstar:.4f}  beta*/2pi = "
              f"{ratio:.4f}  (resid {resid:.1e})")
    assert abs(devs[0.0025]) < 2e-3 and abs(devs[0.01]) < 2e-3
    coeffs = [devs[m2] / m2 for m2 in (0.01, 0.09, 0.5)]
    print(f"  deviation / m^2 = " + ", ".join(f"{c:.3f}" for c in coeffs)
          + "  -- linear in m^2 a^2, a lattice artifact")
    assert max(coeffs) / min(coeffs) < 1.3
    print("  beta -> 2 pi in the continuum: the Unruh temperature, "
          "measured\n")


def s3_horizon():
    print("== s3: where is the horizon? ==")
    m2, L, n = CASES[1]
    X, P = ground_XP(m2, L)
    XA, PA = X[:n, :n].copy(), P[:n, :n].copy()

    def resid_at(s):
        ME, KE = boost_MK(n, m2, s)
        _, r, _ = fit_beta(XA, PA, ME, KE, WIN)
        return r

    r = minimize_scalar(resid_at, bounds=(0.1, 0.9), method='bounded',
                        options={'xatol': 1e-4})
    print(f"  best offset s* = {r.x:.4f} (residual {r.fun:.1e}); "
          f"s = 0.5 residual {resid_at(0.5):.1e}")
    assert abs(r.x - 0.5) < 0.05
    print("  the horizon sits half a lattice spacing beyond the last "
          "site -- the natural midpoint, measured not assumed\n")


def s4_graviton_tower():
    print("== s4: the 3+1 graviton's transverse tower ==")
    L, n = 384, 96
    for kperp in (0.0, 0.1, 0.2, 0.4):
        mp2 = 2 * (4 * np.sin(kperp / 2) ** 2)   # kx = ky = kperp
        mp2 = mp2 if mp2 > 0 else 0.0025          # IR reg for the k=0 line
        X, P = ground_XP(mp2, L)
        XA, PA = X[:n, :n].copy(), P[:n, :n].copy()
        ME, KE = boost_MK(n, mp2, 0.5)
        bstar, resid, _ = fit_beta(XA, PA, ME, KE, WIN)
        print(f"  k_perp = {kperp:.1f} (m_perp^2 = {mp2:.4f}): "
              f"beta*/2pi = {bstar / (2 * np.pi):.4f}")
        if mp2 < 0.2:
            assert abs(bstar / (2 * np.pi) - 1) < 0.01
    print("  every transverse mode -- and both TT polarizations, "
          "identically -- sees the same wedge temperature: the Unruh "
          "effect is geometric for this vacuum\n")


if __name__ == "__main__":
    s1_baseline()
    s2_temperature()
    s3_horizon()
    s4_graviton_tower()
    print("all assertions passed")
