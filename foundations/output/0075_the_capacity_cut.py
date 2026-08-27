"""0075 -- the capacity cut: the web-native count across the horizon.

C3 of path C (0070): cut the free graviton vacuum along C1/C2's flat
surface and count what the WEB says crosses it -- capacity (0067's
tangle tier, 0068's ladder) rather than entropy -- in ledger units.

The cut's exact structure (s1): for the pure Gaussian vacuum the
reduced states of the two sides share one symplectic spectrum {nu_k},
so the cut decomposes into COLLECTIVE two-mode-squeezed (TMS) channels,
one per nu_k > 1/2, with nu = (1/2) cosh 2r. For a TMS pair the
relational phase record |psi> = sum_n lambda^n e^{i n theta} |nn> has
QFI = 4 Var(n) = sinh^2(2r) -- the continuous-variable heir of 0067's
C^2 (both are 4x the generator variance). So the program's three
accounts of one cut are three charges on one spectrum:

    capacity  W  = sum_k (4 nu_k^2 - 1)         [ = sinh^2 2r_k ]
    record    I_k = (1/2) ln(1 + W_k) = ln 2nu_k     (0065's w-I map)
    deficit   delta = 2 pi sum_k (1 - e^{-I_k}) = 2 pi sum_k (1 - 1/(2 nu_k))
    entropy   S  = sum_k s(nu_k)                    (C1's account)

  s2  The pairwise account fails at field level: the two-site
      negativity across the cut is nonzero ONLY for the single
      adjacent pair (exactly zero at every other separation, chain
      and 3D alike), and that pair carries a small fraction of the
      cut capacity. 0068's P1 refinement -- capacity is node-vs-rest,
      not literal pairs -- is forced by the vacuum itself: the field
      is GHZ-like, not W-like.
  s3  All three accounts obey area laws; coefficients extracted
      (ledger units: delta/A in radians of deficit per plaquette).
  s4  The discriminator has teeth at field level: W/S and delta/S are
      NOT constants -- they run with mass -- so a geometry charged by
      capacity is distinguishable from one charged by entropy by the
      horizon charge's response to the field's mass/IR content.
  s5  Monogamy bookkeeping per site, in one currency (the Gaussian
      contangle = squared log-negativity, node-vs-rest contangle
      arccosh^2(2 nu) for the pure global state): the CKW-shaped
      inequality sum_pairs E_N^2 <= contangle(node|rest) holds with
      room, and the collective share at site level is ~2/3 -- a
      majority, not the ~99% first guessed; the cut-level collective
      share (s2) is the stronger statement.
"""

import numpy as np


# ----------------------------------------------------------------------
# Gaussian kit
# ----------------------------------------------------------------------

def ground_XP(m2, L):
    K = (m2 + 2.0) * np.eye(L)
    for i in range(L - 1):
        K[i, i + 1] = K[i + 1, i] = -1.0
    w, U = np.linalg.eigh(K)
    return (U @ np.diag(1 / np.sqrt(w)) @ U.T / 2,
            U @ np.diag(np.sqrt(w)) @ U.T / 2)


def spectrum(X, P, idx):
    XA = X[np.ix_(idx, idx)]
    PA = P[np.ix_(idx, idx)]
    v = np.sqrt(np.clip(np.linalg.eigvals(XA @ PA).real, 0.25, None))
    return np.sort(v)[::-1]


def accounts(nu):
    """entropy, capacity, deficit of one symplectic spectrum."""
    a, b = nu + 0.5, np.clip(nu - 0.5, 1e-300, None)
    S = float(np.sum(a * np.log(a) - b * np.log(b)))
    W = float(np.sum(4 * nu ** 2 - 1))
    D = float(2 * np.pi * np.sum(1 - 1 / (2 * nu)))
    return S, W, D


def pair_neg(x11, x22, x12, p11, p22, p12):
    """Log-negativity of a two-mode Gaussian state (no xp correls)."""
    detA, detB, detC = x11 * p11, x22 * p22, x12 * p12
    S4 = np.array([[x11, 0, x12, 0], [0, p11, 0, p12],
                   [x12, 0, x22, 0], [0, p12, 0, p22]])
    Dt = detA + detB - 2 * detC
    disc = max(Dt * Dt - 4 * np.linalg.det(S4), 0.0)
    nt = np.sqrt(max((Dt - np.sqrt(disc)) / 2, 1e-300))
    return max(0.0, -np.log(2 * nt))


# ----------------------------------------------------------------------

L, NCUT = 64, 32
M2_LIGHT = 0.0025


def s1_schmidt():
    print("== s1: the cut is a stack of collective TMS channels ==")
    for m2 in (M2_LIGHT, 0.09):
        X, P = ground_XP(m2, L)
        vA = spectrum(X, P, list(range(NCUT)))
        vB = spectrum(X, P, list(range(NCUT, L)))
        gap = np.abs(vA - vB).max()
        print(f"  m^2={m2}: A and B spectra identical to {gap:.1e}")
        assert gap < 1e-12
        # capacity = sinh^2(2r) with nu = cosh(2r)/2, identically
        r = 0.5 * np.arccosh(np.clip(2 * vA, 1.0, None))
        assert np.abs((4 * vA ** 2 - 1) - np.sinh(2 * r) ** 2).max() < 1e-10
    print("  pure global state => two-sided Schmidt pairing: each "
          "nu_k > 1/2 is one collective")
    print("  two-mode-squeezed channel; capacity per channel = "
          "sinh^2(2r_k) = 4nu_k^2 - 1\n")


def s2_pairwise_fails():
    print("== s2: the pairwise account across the cut ==")
    X, P = ground_XP(M2_LIGHT, L)
    pairs = [(31, 32), (30, 32), (31, 33), (30, 33), (28, 35)]
    ens = {}
    for i, j in pairs:
        ens[(i, j)] = pair_neg(X[i, i], X[j, j], X[i, j],
                               P[i, i], P[j, j], P[i, j])
        print(f"  chain E_N({i},{j}) = {ens[(i, j)]:.6f}")
    assert ens[(31, 32)] > 0.1
    assert all(v == 0.0 for k, v in ens.items() if k != (31, 32))
    nu = spectrum(X, P, list(range(NCUT)))
    _, W, _ = accounts(nu)
    share = ens[(31, 32)] ** 2 / W
    ctg = float(np.sum(np.arccosh(np.clip(2 * nu, 1, None)) ** 2))
    share_ctg = ens[(31, 32)] ** 2 / ctg
    print(f"  only the ADJACENT pair is entangled -- all other "
          f"separations exactly separable;")
    print(f"  its share of the cut: {100 * share:.1f}% in capacity "
          f"units, {100 * share_ctg:.1f}% in contangle units")
    assert share < 0.15 and share_ctg < 0.2
    print("  field-level GHZ lesson: the cut's capacity is collective; "
          "P1 must be read node-vs-rest\n")


def _column_XP(Nt, L, M2=0.0, phase=None):
    """3D covariances between sites in one transverse column
    (phase=None) or with a transverse-neighbor phase factor."""
    Xp = np.zeros((L, L))
    Pp = np.zeros((L, L))
    for ix in range(Nt):
        for iy in range(Nt):
            kx = 2 * np.pi * ix / Nt
            ky = 2 * np.pi * iy / Nt
            mp2 = 4 * np.sin(kx / 2) ** 2 + 4 * np.sin(ky / 2) ** 2 \
                + M2 + 1e-6
            Xk, Pk = ground_XP(mp2, L)
            f = 1.0 if phase is None else np.cos(kx)
            Xp += f * Xk
            Pp += f * Pk
    return Xp / Nt ** 2, Pp / Nt ** 2


def s3_three_area_laws():
    print("== s3: three area laws, one spectrum ==")
    coeffs = {}
    for Nt in (16, 32):
        tot = np.zeros(3)
        for ix in range(Nt):
            for iy in range(Nt):
                kx = 2 * np.pi * ix / Nt
                ky = 2 * np.pi * iy / Nt
                mp2 = 4 * np.sin(kx / 2) ** 2 + 4 * np.sin(ky / 2) ** 2 \
                    + 1e-6
                X, P = ground_XP(mp2, L)
                nu = spectrum(X, P, list(range(NCUT)))
                tot += accounts(nu)
        coeffs[Nt] = tot / Nt ** 2
        S, W, D = coeffs[Nt]
        print(f"  N_perp={Nt}: S/A = {S:.5f}  W/A = {W:.5f}  "
              f"delta/A = {D:.5f} rad/plaquette")
    drift = np.abs(coeffs[32] - coeffs[16]) / coeffs[32]
    print(f"  N_perp drift: {100 * drift[0]:.1f}% / {100 * drift[1]:.1f}%"
          f" / {100 * drift[2]:.1f}% -- all three converge (area laws)")
    assert np.all(drift < 0.12)
    S, W, D = coeffs[32]
    print(f"  ledger-unit coefficient: the graviton (2 polarizations) "
          f"deficit density = {2 * D:.4f} rad per plaquette of "
          f"horizon\n")
    return coeffs[32]


def s4_discriminator():
    print("== s4: the discriminator runs -- capacity is not entropy ==")
    Nt = 16
    rows = {}
    for M2 in (0.0, 0.09, 0.5):
        tot = np.zeros(3)
        for ix in range(Nt):
            for iy in range(Nt):
                kx = 2 * np.pi * ix / Nt
                ky = 2 * np.pi * iy / Nt
                mp2 = 4 * np.sin(kx / 2) ** 2 + 4 * np.sin(ky / 2) ** 2 \
                    + M2 + 1e-6
                X, P = ground_XP(mp2, L)
                nu = spectrum(X, P, list(range(NCUT)))
                tot += accounts(nu)
        S, W, D = tot / Nt ** 2
        rows[M2] = (W / S, D / S)
        print(f"  M^2={M2:4}: W/S = {W / S:.3f}   delta/S = {D / S:.3f}")
    spread = rows[0.0][0] / rows[0.5][0]
    print(f"  W/S varies by {spread:.2f}x across the mass scan: the "
          f"accounts are NOT proportional --")
    print("  a horizon charge coupled to capacity responds differently "
          "to the field's mass/IR")
    print("  content than one coupled to entropy: 0067's discriminator, "
          "now at field level\n")
    assert spread > 1.2


def s5_site_budget():
    print("== s5: per-site budget -- collective dominance ==")
    Nt = 16
    Xc, Pc = _column_XP(Nt, L)
    Xn, Pn = _column_XP(Nt, L, phase='t')
    j = NCUT - 1                       # bulk site (cut-adjacent in A)
    nu_site = np.sqrt(Xc[j, j] * Pc[j, j])
    # one currency: Gaussian contangle. Node-vs-rest for a pure global
    # state is a TMS split with cosh(2r) = 2 nu -> contangle (2r)^2.
    tau_node = float(np.arccosh(2 * nu_site)) ** 2
    # pairwise: longitudinal neighbors (j-1, j+1), transverse (4x);
    # bulk cubic symmetry makes all six nearest pairs equivalent
    en_long_m = pair_neg(Xc[j, j], Xc[j - 1, j - 1], Xc[j, j - 1],
                         Pc[j, j], Pc[j - 1, j - 1], Pc[j, j - 1])
    en_long_p = pair_neg(Xc[j, j], Xc[j + 1, j + 1], Xc[j, j + 1],
                         Pc[j, j], Pc[j + 1, j + 1], Pc[j, j + 1])
    en_trans = pair_neg(Xc[j, j], Xc[j, j], Xn[j, j],
                        Pc[j, j], Pc[j, j], Pn[j, j])
    pair_sum = en_long_m ** 2 + en_long_p ** 2 + 4 * en_trans ** 2
    share = 1 - pair_sum / tau_node
    print(f"  site: node-vs-rest contangle = {tau_node:.4f}")
    print(f"  pairwise E_N: longitudinal {en_long_m:.4f}/{en_long_p:.4f}"
          f", transverse {en_trans:.4f} (bulk symmetry: all equal)")
    print(f"  CKW-shaped check: sum of pairwise contangles "
          f"{pair_sum:.4f} <= {tau_node:.4f}  (monogamy holds)")
    print(f"  collective share at site level = {100 * share:.1f}%")
    assert pair_sum <= tau_node
    assert share > 0.5
    print("  a majority of each site's capacity is collective "
          "(consistent with Gaussian contangle")
    print("  monogamy, Adesso-Illuminati); the literal-pairs picture "
          "undercounts the vacuum\n")


if __name__ == "__main__":
    s1_schmidt()
    s2_pairwise_fails()
    s3_three_area_laws()
    s4_discriminator()
    s5_site_budget()
    print("all assertions passed")
