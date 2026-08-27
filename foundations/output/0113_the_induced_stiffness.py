"""0113 -- the induced stiffness: the gravity channel's record
precision, measured, against the number lucid 0032 demands.

lucid 0032 closed the matter coupling as a formula: the stress
tensor is the local record's Fisher information, and Newton's
constant is G = 1/(4 pi p) with p the RECORD PRECISION of the
channel that carries gravity. That converted "direct G" into a
single measurement with a target: this program's induced-gravity
value G = 5.165 a^2 (0105 s1b, from the vacuum entanglement area
density alpha = 0.0242 per polarization) requires

    p* = 1/(4 pi * 5.165) = 0.01541   (two polarizations)

i.e. a channel about 865x softer than the plaquette weight's own
local precision (13.34). "A collective mode is softer than a single
plaquette" was plausible; it was not a calculation. This module
does the calculation.

THE OBJECT. Gravity here is induced, so the trust field lambda has
no bare action -- its entire dynamics is what the matter's own
record generates. The filter fixes lambda's normalization: a node
transmits e^{-2I} of an incident influence (lucid 0010), which on
the lattice is the link weight w = e^{2 lambda}, exactly the
D = 4 conformally-flat matter coupling sqrt(g) g^{uv} = e^{2 lambda}
delta. Integrating out one massless lattice scalar in that
background gives Gamma[lambda] = (1/2) ln det' (D^T W D), and the
induced stiffness p is the coefficient of (1/2)|grad lambda|^2 in
its quadratic part.

  s1  THE INDUCED SCALE ACTION IS EXACTLY MASSLESS AND POSITIVE --
      a theorem, not a fit. With B = D M0^-1 D^T the orthogonal
      projector onto gradient link fields,

        Gamma''[lambda] = sum_{l,l'} B_{ll'}^2 (lambda_l - lambda_l')^2

      identically. Two consequences with no tuning: the form is
      POSITIVE SEMIDEFINITE, and its kernel is EXACTLY the
      constants -- there is no induced mass term in the scale
      channel, so the 1/r that lucid 0019 needs is not a tuned
      coincidence. (0112 measured the plaquette SCALE field
      screened within ~0.32 a; that is a different, composite
      observable -- the trust channel itself is exactly massless.)
      Verified against dense log-determinants at L = 6, 8.
  s2  THE NUMBER. p = 0.15493 per field (L -> infinity, 1/L^2
      extrapolation, six stable digits), against the target
      p* = 0.01541. THE PREDICTION IS WRONG BY 20x: the gravity
      channel is not 865x softer than the plaquette weight, it is
      about 43x softer. Recorded as measured, with the arithmetic
      in one place.
  s3  THE RESIDUE IS FIELD-COUNT INDEPENDENT. Both routes to G
      scale as 1/N in the number of fields carrying gravity, so
      their ratio does not:

        G_entanglement / G_induced = pi p / alpha = 20.1

      The gap cannot be blamed on how many polarizations gravitate.
      It is a pure number, and it is what "direct G" now is.
"""

import numpy as np

# ----------------------------------------------------------------
# the two published numbers this module is confronting
# ----------------------------------------------------------------
ALPHA_SCALAR = 0.0242          # 0082/0073: entanglement area density
G_INDUCED = 1 / (4 * 2 * ALPHA_SCALAR)      # 0105 s1b: 5.165 a^2
P_TARGET = 1 / (4 * np.pi * G_INDUCED)      # lucid 0032: 0.01541
KAPPA_PLAQ = 13.337            # Born weight's local precision, tau = 0


# ----------------------------------------------------------------
# brute force: the actual log-determinant
# ----------------------------------------------------------------
def gradient(L, d):
    V = L ** d
    idx = np.arange(V).reshape((L,) * d)
    D = np.zeros((d * V, V))
    for mu in range(d):
        sh = np.roll(idx, -1, axis=mu).reshape(-1)
        D[mu * V + np.arange(V), sh] += 1.0
        D[mu * V + np.arange(V), idx.reshape(-1)] -= 1.0
    return D


def link_lambda(L, d, k, eps):
    """lambda_{x,mu} = (lam_x + lam_{x+mu})/2 with lam = eps cos(k.x)"""
    g = np.indices((L,) * d).reshape(d, -1)
    lam = eps * np.cos(np.tensordot(np.asarray(k, float), g, (0, 0)))
    idx = np.arange(L ** d).reshape((L,) * d)
    out = np.empty(d * L ** d)
    for mu in range(d):
        sh = np.roll(idx, -1, axis=mu).reshape(-1)
        out[mu * L ** d:(mu + 1) * L ** d] = 0.5 * (lam + lam[sh])
    return out


def gamma_dense(L, d, D, k, eps):
    W = np.exp(2.0 * link_lambda(L, d, k, eps))
    ev = np.sort(np.linalg.eigvalsh(D.T @ (W[:, None] * D)))[1:]
    return 0.5 * np.log(ev).sum()


def khat2(k):
    return float(sum(2 * (1 - np.cos(kk)) for kk in k))


# ----------------------------------------------------------------
# exact fast evaluator: F(k) = 2 Gamma''(k) / V
# ----------------------------------------------------------------
def F_rows(L, d=4, nmax=3):
    ax = 2 * np.pi * np.fft.fftfreq(L)
    grids = np.meshgrid(*([ax] * d), indexing="ij")
    e = [np.exp(1j * g) - 1.0 for g in grids]
    p2 = sum(np.abs(ei) ** 2 for ei in e)
    p2[(0,) * d] = 1.0
    ns = [n for n in range(1, nmax + 1)
          if abs(2 * np.pi * n / L - np.pi) > 1e-12]   # 2k = 0 excluded
    mk = {n: tuple([(-n) % L] + [0] * (d - 1)) for n in ns}
    S0 = np.zeros((d, d))
    Sk = {n: np.zeros((d, d), complex) for n in ns}
    for mu in range(d):
        for nu in range(d):
            Bh = e[mu] * np.conj(e[nu]) / p2
            Bh[(0,) * d] = 0.0
            St = np.fft.fftn(np.real(np.fft.ifftn(Bh)) ** 2)
            S0[mu, nu] = St[(0,) * d].real
            for n in ns:
                Sk[n][mu, nu] = St[mk[n]]
    rows = []
    for n in ns:
        k = np.array([2 * np.pi * n / L] + [0.0] * (d - 1))
        a = (1 + np.exp(1j * k)) / 2
        tot = sum(abs(a[mu]) ** 2 * S0[mu, nu]
                  - (a[mu] * np.conj(a[nu]) * Sk[n][mu, nu]).real
                  for mu in range(d) for nu in range(d))
        rows.append((khat2(k), 2.0 * tot))
    return rows


def stiffness(rows):
    """F = P khat2 + Q khat2^2: two smallest momenta."""
    (a1, f1), (a2, f2) = rows[0], rows[1]
    Q = (f2 / a2 - f1 / a1) / (a2 - a1)
    return f1 / a1 - Q * a1


# ----------------------------------------------------------------
def s1_massless_and_positive():
    print("== s1: the induced scale action is massless and positive"
          " ==")
    d = 4
    print("  theorem: Gamma'' = sum_{ll'} B_{ll'}^2 (lam_l-lam_l')^2,"
          "  B = D M0^-1 D^T")
    print("  (B is the orthogonal projector onto gradient link "
          "fields, so B_ll = sum_l' B_ll'^2)")
    print("  => PSD, and zero exactly on constant lambda: no induced"
          " mass term.\n")
    for L in (6, 8):
        D = gradient(L, d)
        V = L ** d
        g0 = gamma_dense(L, d, D, [0.0] * d, 0.0)
        # a uniform lambda shifts ln det' by exactly 2 lam (V-1)
        lin = gamma_dense(L, d, D, [0.0] * d, 0.0)
        for c in (0.1, 0.3):
            W = np.exp(2.0 * c) * np.ones(d * V)
            ev = np.sort(np.linalg.eigvalsh(D.T @ (W[:, None] * D)))[1:]
            gc = 0.5 * np.log(ev).sum()
            pred = lin + (V - 1) * c
            assert abs(gc - pred) < 1e-6 * max(1.0, abs(pred))
        print(f"  L = {L}: uniform lambda -> Gamma is EXACTLY linear "
              f"(residual < 1e-6): the k = 0")
        print("           quadratic response vanishes identically")
        rows = F_rows(L, d, nmax=3)
        print("           k^2      F (fast, exact)    F (dense "
              "log-det)     rel")
        for n, (k2, f) in zip(range(1, 9), rows):
            k = [2 * np.pi * n / L] + [0.0] * (d - 1)
            eps = 0.02
            fb = 2 * (gamma_dense(L, d, D, k, eps)
                      + gamma_dense(L, d, D, k, -eps)
                      - 2 * g0) / eps ** 2 / V
            print(f"          {k2:7.4f}   {f:14.6f}   {fb:16.6f}"
                  f"   {abs(f / fb - 1):.1e}")
            assert abs(f / fb - 1) < 1e-4
            assert f > 0
    print("  positive at every momentum, zero only at k = 0: the "
          "trust channel is exactly")
    print("  massless with no tuning -- lucid 0019's massless mode, "
          "proved on this side\n")


def s2_the_number():
    print("== s2: the number ==")
    print("   L     P(L)        (F = P khat^2 + Q khat^4, two "
          "smallest momenta)")
    Ls = (12, 16, 20, 24, 28, 32)
    Ps = []
    for L in Ls:
        P = stiffness(F_rows(L, 4, nmax=3))
        Ps.append(P)
        print(f"  {L:3d}   {P:.6f}")
    # 1/L^2 extrapolation from the two largest
    x = np.array([1.0 / L ** 2 for L in Ls[-2:]])
    y = np.array(Ps[-2:])
    c = (y[0] - y[1]) / (x[0] - x[1])
    p_inf = float(y[1] - c * x[1])
    # consistency: the same extrapolation one size down
    x2 = np.array([1.0 / L ** 2 for L in Ls[-3:-1]])
    y2 = np.array(Ps[-3:-1])
    p_inf2 = float(y2[1] - (y2[0] - y2[1]) / (x2[0] - x2[1]) * x2[1])
    print(f"  1/L^2 extrapolation: p = {p_inf:.6f}  (one size down: "
          f"{p_inf2:.6f})")
    assert abs(p_inf - p_inf2) < 1e-5
    print()
    print(f"  measured, one field                  p  = {p_inf:.5f}")
    print(f"  measured, graviton (2 polarizations) p  = "
          f"{2 * p_inf:.5f}")
    print(f"  target (lucid 0032, G = {G_INDUCED:.3f} a^2)     p* = "
          f"{P_TARGET:.5f}")
    print(f"  THE PREDICTION IS WRONG BY {2 * p_inf / P_TARGET:.1f}x"
          " -- measured too STIFF, not too soft")
    print()
    print(f"  plaquette weight's local precision      "
          f"{KAPPA_PLAQ:.3f}")
    print(f"  predicted softness ratio                "
          f"{KAPPA_PLAQ / P_TARGET:.0f}x")
    print(f"  MEASURED softness ratio                 "
          f"{KAPPA_PLAQ / (2 * p_inf):.0f}x")
    print("  the gravity channel IS much softer than a single "
          "plaquette -- by 43, not 865\n")
    return p_inf


def s3_the_residue(p_inf):
    print("== s3: the residue is field-count independent ==")
    print("  entanglement route: G = 1/(4 N alpha)   (N "
          "polarizations, 0105 s1b)")
    print("  matter-coupling route: G = 1/(4 pi N p)  (lucid 0032)")
    print("  ratio = pi p / alpha -- N cancels")
    ratio = np.pi * p_inf / ALPHA_SCALAR
    print(f"  G_entanglement / G_induced = {ratio:.2f}")
    for N in (1, 2, 6):
        ge = 1 / (4 * N * ALPHA_SCALAR)
        gi = 1 / (4 * np.pi * N * p_inf)
        print(f"    N = {N}:  G_ent = {ge:8.3f} a^2   G_ind = "
              f"{gi:7.4f} a^2   ratio {ge / gi:.2f}")
        assert abs(ge / gi - ratio) < 1e-9
    print("  the gap survives any count of gravitating "
          "polarizations. It is a pure number,")
    print("  and it is the entire remaining content of direct G.")
    print(f"  (2 pi^2 = {2 * np.pi ** 2:.3f} sits "
          f"{100 * abs(ratio / (2 * np.pi ** 2) - 1):.1f}% away. "
          "Priced, not claimed: alpha itself is")
    print("  only converged to about a percent, and one near-miss "
          "at n = 1 is not evidence.)\n")


if __name__ == "__main__":
    s1_massless_and_positive()
    p = s2_the_number()
    s3_the_residue(p)
    print("all assertions passed")
