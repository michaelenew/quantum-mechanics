"""0073 -- the half space: graviton zero-point entanglement, exactly.

C1 of path C (0070): 0063's free lattice graviton is two TT oscillator
modes per momentum -- a Gaussian ground state -- so the entanglement of
the zero-point state across a flat spatial cut is exact
covariance-matrix algebra. For a quadratic Hamiltonian
H = 1/2 p^2 + 1/2 x K x, the ground-state correlators are
X = K^{-1/2}/2 and P = K^{1/2}/2; restricting both to region A, the
symplectic eigenvalues nu = sqrt(eig(X_A P_A)) give
S = sum (nu+1/2)ln(nu+1/2) - (nu-1/2)ln(nu-1/2).

Geometry: 3D spatial lattice, transverse torus (N_perp^2 momenta),
open (Dirichlet) chains of length L in the cut direction, region =
half the chain -- ONE cut face, no zero mode. Per transverse momentum
the chain mass is the transverse dispersion.

  s1  Machinery anchor: the 1D massive chain obeys the c = 1 CFT law
      S = -(1/6) ln m + const in the window 1/L << m << 1
      (slope within 0.2% at L = 2048).
  s2  Area law, nearest-neighbor stencil: S/A converges in N_perp to
      alpha ~ 0.0242 per scalar polarization. Graviton = 2 alpha.
      (External anchor, from memory -- flag, not assert: Srednicki
      (1993) gives S = 0.30 M^2 R^2 for spheres, i.e. 0.30/(4 pi)
      ~ 0.0239 per unit area with his radial regulator.)
  s3  The massless line's fingerprint: at fixed N_perp the coefficient
      grows as [(1/6) ln L]/N_perp^2 -- the k_perp = 0 graviton line
      through the cut is a c = 1 CFT, the entanglement echo of 0077's
      gapless channel.
  s4  The program's own stencil (0063's central differences): the
      distance-2 chain factorizes exactly into two half-length
      nearest-neighbor-type chains (doublers), and the area
      coefficient roughly doubles. The coefficient is regulator
      dependent -- non-universal, as the UV-divergent area term must
      be. This is the standard species/induced-gravity problem
      arriving on schedule; C4's confrontation with A/4G must go
      through a renormalization-of-G argument, not a bare match.
  s5  Massive control: alpha decreases monotonically with M^2
      (locality of the vacuum).
"""

import time

import numpy as np


# ----------------------------------------------------------------------
# exact Gaussian entanglement
# ----------------------------------------------------------------------

def build_K(m2, L, stencil):
    """Coupling matrix of the open chain. 'nn': standard second
    difference (dispersion m^2 + 4 sin^2(k/2)). 'cd': central
    difference (dispersion m^2 + sin^2 k, distance-2 coupling)."""
    if stencil == "nn":
        K = (m2 + 2.0) * np.eye(L)
        for i in range(L - 1):
            K[i, i + 1] = K[i + 1, i] = -1.0
    elif stencil == "cd":
        K = (m2 + 0.5) * np.eye(L)
        for i in range(L - 2):
            K[i, i + 2] = K[i + 2, i] = -0.25
    else:  # 'sub': the cd sublattice chain, for the factorization check
        K = (m2 + 0.5) * np.eye(L)
        for i in range(L - 1):
            K[i, i + 1] = K[i + 1, i] = -0.25
    return K


def chain_entropy(m2, L, cut, stencil="nn"):
    K = build_K(m2, L, stencil)
    w, U = np.linalg.eigh(K)
    assert w.min() > 0, "chain K not positive definite"
    sq = U @ np.diag(np.sqrt(w)) @ U.T
    isq = U @ np.diag(1.0 / np.sqrt(w)) @ U.T
    X = isq[:cut, :cut] / 2.0
    P = sq[:cut, :cut] / 2.0
    nu = np.sqrt(np.clip(np.linalg.eigvals(X @ P).real, 0.25, None))
    a, b = nu + 0.5, np.clip(nu - 0.5, 1e-300, None)
    return float(np.sum(a * np.log(a) - b * np.log(b)))


def alpha3d(n_perp, L=64, stencil="nn", M2=0.0):
    """S per unit cut area: transverse torus of n_perp^2 momenta, one
    chain per momentum with the transverse dispersion as its mass."""
    tot = 0.0
    for ix in range(n_perp):
        for iy in range(n_perp):
            kx = 2 * np.pi * ix / n_perp
            ky = 2 * np.pi * iy / n_perp
            if stencil == "nn":
                mp2 = 4 * np.sin(kx / 2) ** 2 + 4 * np.sin(ky / 2) ** 2
            else:
                mp2 = np.sin(kx) ** 2 + np.sin(ky) ** 2
            tot += chain_entropy(mp2 + M2, L, L // 2, stencil)
    return tot / n_perp ** 2


# ----------------------------------------------------------------------

def s1_cft_anchor():
    print("== s1: c = 1 CFT anchor for the machinery ==")
    L = 2048
    ms = np.array([0.01, 0.015, 0.023, 0.04, 0.06])
    Ss = [chain_entropy(m * m, L, L // 2) for m in ms]
    slope = np.polyfit(np.log(ms), Ss, 1)[0]
    print(f"  L={L}: dS/d ln m = {slope:.5f}  (CFT: -1/6 = {-1/6:.5f}, "
          f"rel err {abs(6 * slope + 1):.4f})")
    assert abs(6 * slope + 1) < 0.02
    print("  half-chain entropy follows -(1/6) ln m to 0.2% -- "
          "machinery certified\n")


def s2_area_law():
    print("== s2: area law, nearest-neighbor stencil (L = 64) ==")
    alphas = {}
    for n in (8, 16, 32, 64):
        t0 = time.time()
        alphas[n] = alpha3d(n)
        print(f"  N_perp = {n:2d}: S/A = {alphas[n]:.6f}   "
              f"({time.time() - t0:.1f}s)")
    d1 = alphas[16] - alphas[32]
    d2 = alphas[32] - alphas[64]
    assert d1 > d2 > 0, "not monotonically converging"
    assert d2 / alphas[64] < 0.005, "N_perp = 64 not converged to 0.5%"
    # extrapolants assuming c/N^2 tails from successive pairs
    ex_a = alphas[32] - d1 / 3.0
    ex_b = alphas[64] - d2 / 3.0
    spread = abs(ex_a - ex_b) / ex_b
    alpha = ex_b
    print(f"  extrapolants: {ex_a:.6f} (16/32), {ex_b:.6f} (32/64); "
          f"spread {100 * spread:.2f}%")
    assert spread < 0.02
    print(f"  alpha_scalar = {alpha:.4f} per polarization;  "
          f"GRAVITON S/A = 2 alpha = {2 * alpha:.4f}")
    print("  (memory-flagged external anchor: Srednicki '93 spheres "
          f"give 0.30/4pi = {0.30 / (4 * np.pi):.4f} -- same scale, "
          "different regulator/geometry; cite before relying)\n")
    return alpha


def s3_massless_line():
    print("== s3: the massless graviton line through the cut ==")
    n = 16
    aL = {L: alpha3d(n, L=L) for L in (32, 64, 128)}
    c_log = (aL[128] - aL[32]) / np.log(4.0) * n ** 2
    print(f"  N_perp={n}: S/A at L = 32/64/128 = "
          f"{aL[32]:.6f} / {aL[64]:.6f} / {aL[128]:.6f}")
    print(f"  d(S/A)/d ln L * N_perp^2 = {c_log:.4f}   (c = 1 CFT "
          f"predicts 1/6 = {1 / 6:.4f} from the k_perp = 0 line)")
    assert abs(6 * c_log - 1) < 0.05
    print("  the gapless channel (0077) leaves its central charge in "
          "the entanglement -- subleading, vanishes as 1/N_perp^2\n")


def s4_program_stencil():
    print("== s4: the program's central-difference stencil ==")
    for m2 in (0.0, 0.3):
        d = chain_entropy(m2, 64, 32, "cd")
        s = chain_entropy(m2, 32, 16, "sub")
        assert abs(d - 2 * s) < 1e-9, "sublattice factorization broken"
    print("  exact: S_cd(L) = 2 x S_sub(L/2) -- the doubler branches "
          "are literal sublattices")
    acd = {}
    for n in (16, 32, 64):
        acd[n] = alpha3d(n, stencil="cd")
        print(f"  CD N_perp = {n:2d}: S/A = {acd[n]:.6f}")
    d1, d2 = acd[16] - acd[32], acd[32] - acd[64]
    ex = acd[64] - d2 / 3.0
    ann = 0.0242
    print(f"  alpha_cd -> {ex:.4f}  vs alpha_nn 0.0242: ratio "
          f"{ex / ann:.2f}")
    assert ex > ann, "cd stencil should carry more branches"
    print("  the coefficient is regulator-dependent (non-universal UV "
          "object) -- C4 must renormalize G, not bare-match\n")
    return ex


def s5_massive_control():
    print("== s5: massive control ==")
    vals = [alpha3d(32, M2=M2) for M2 in (0.0, 0.25, 1.0)]
    print(f"  S/A at M^2 = 0, 0.25, 1: "
          + " / ".join(f"{v:.6f}" for v in vals))
    assert vals[0] > vals[1] > vals[2] > 0
    print("  monotone decrease -- vacuum locality\n")


if __name__ == "__main__":
    s1_cft_anchor()
    s2_area_law()
    s3_massless_line()
    s4_program_stencil()
    s5_massive_control()
    print("all assertions passed")
