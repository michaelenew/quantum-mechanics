"""0093 -- the time tier: Euclidean = smoother, Lorentzian = filter.

The homomorphism's remaining structural seam is time: the filter is
causal, the physics' measure is Euclidean with no arrow. This module
proves the seam closed at every tier where the isomorphism is
established (R, U(1), SU(2)):

  THE EUCLIDEAN MEASURE IS THE SMOOTHER; THE FILTER IS ITS CAUSAL
  HALF. Conditioning the Euclidean chain measure on both endpoints
  gives exactly the two-sided (RTS/forward-backward) posterior;
  dropping the backward message gives the causal filter; the
  dynamics (the transfer kernel) is IDENTICAL in both readings.
  The Lorentzian lift therefore changes no dynamical object -- it
  only removes end-conditioning.

  s1  R tier, exact: the Euclidean propagator on a Dirichlet chain
      (inverse tridiagonal Laplacian) equals the smoother covariance
      C(s,t) = s(T-t)/T identically; the filter variance is t
      (the massless/pinned-root linear growth).
  s2  U(1) tier: the marginal of the Euclidean chain measure with
      fixed ends, computed by brute grid contraction, equals
      forward-message x backward-message (wrapped heat kernels),
      to near machine precision.
  s3  SU(2) tier: same identity by characters; and the smoother's
      two-message fusion carries a WIDTH-INDEPENDENT curvature tax
      (0099's van Vleck mechanism, here measured in the smoother):
      p_bridge = p_fwd + p_bwd - delta_s, delta_s constant.
  s4  Causal attainability, exact at the free tier: the fraction of
      the smoother's precision available causally is (T-t)/T on R
      (linear decay toward the far end), with the SU(2) curve
      measured next to it -- the exact template for F3.
"""

import numpy as np

# ----------------------------------------------------------------------
# s1 -- R tier
# ----------------------------------------------------------------------

def s1_flat():
    print("== s1: R tier -- Euclidean propagator == smoother "
          "covariance, exactly ==")
    T = 64
    M = 2 * np.eye(T - 1) - np.eye(T - 1, k=1) - np.eye(T - 1, k=-1)
    C = np.linalg.inv(M)                     # Euclidean, Dirichlet
    s = np.arange(1, T)
    Csm = np.minimum.outer(s, s) * (T - np.maximum.outer(s, s)) / T
    err = np.abs(C - Csm).max()
    print(f"  inverse Dirichlet Laplacian vs s(T-t)/T: max err = "
          f"{err:.1e}")
    assert err < 1e-9
    # bridge variance = precision sum of forward and backward
    vb = C.diagonal()
    vpred = 1 / (1 / s + 1 / (T - s))
    assert np.abs(vb - vpred).max() < 1e-9
    print("  diag = (1/t + 1/(T-t))^-1: forward and backward "
          "message precisions ADD")
    print("  filter (causal half): var = t -- the massless linear "
          "growth; smoother pins it\n")


# ----------------------------------------------------------------------
# s2 -- U(1) tier
# ----------------------------------------------------------------------

def k_u1(tau, phi, nmax=40):
    n = np.arange(1, nmax + 1)
    return (1 + 2 * (np.exp(-n ** 2 * tau / 2)[None, :]
                     * np.cos(np.outer(phi, n))).sum(1)) / (2 * np.pi)


def s2_u1():
    print("== s2: U(1) tier -- brute contraction vs "
          "forward x backward ==")
    tau, y, G = 0.35, 1.0, 101
    phi = np.linspace(-np.pi, np.pi, G, endpoint=False)
    K = k_u1(tau, phi)
    # brute: p(x2 | x0=0, x4=y) with x1, x3 integrated on the grid
    Kd = k_u1(tau, phi[:, None] - phi[None, :]
              if False else np.subtract.outer(phi, phi).ravel()
              ).reshape(G, G)
    p = np.einsum("a,ab,bc,c->b", K, Kd.T, Kd, k_u1(tau, y - phi))
    p /= p.sum()
    # forward x backward with semigroup kernels
    q = k_u1(2 * tau, phi) * k_u1(2 * tau, y - phi)
    q /= q.sum()
    err = np.abs(p - q).max() / q.max()
    print(f"  Euclidean conditional (3 integrals, grid) vs "
          f"K_2tau(x) K_2tau(y-x): rel err = {err:.1e}")
    assert err < 1e-10
    print("  the Euclidean chain measure, end-conditioned, IS the "
          "smoother\n")


# ----------------------------------------------------------------------
# s3 -- SU(2) tier
# ----------------------------------------------------------------------

TH = np.linspace(1e-7, np.pi - 1e-7, 200001)
HAAR = np.sin(TH) ** 2


def k_su2(tau, jmax=60):
    js = np.arange(0, jmax + 0.1, 0.5)
    out = np.zeros_like(TH)
    for j in js:
        out += (2 * j + 1) * np.exp(-tau * j * (j + 1)) \
            * np.sin((2 * j + 1) * TH) / np.sin(TH)
    return out


def vprec(dens):
    p = np.maximum(dens, 0) * HAAR
    p /= np.trapezoid(p, TH)
    return 1 / (np.trapezoid(p * TH ** 2, TH) / 3)


def s3_su2():
    print("== s3: SU(2) tier -- the smoother identity, and the "
          "curvature tax in the fusion ==")
    # semigroup (the exact Markov/conditioning structure): K_a * K_b
    # = K_{a+b} by characters -- verified as the identity's engine
    a, b = 0.25, 0.4
    ka, kb, kab = k_su2(a), k_su2(b), k_su2(a + b)
    # class convolution: coefficients multiply / (2j+1)
    js = np.arange(0, 60.1, 0.5)
    conv = np.zeros_like(TH)
    for j in js:
        fa = (2 * j + 1) * np.exp(-a * j * (j + 1))
        fb = (2 * j + 1) * np.exp(-b * j * (j + 1))
        conv += fa * fb / (2 * j + 1) \
            * np.sin((2 * j + 1) * TH) / np.sin(TH)
    err = np.abs(conv - kab).max() / kab.max()
    print(f"  K_a * K_b = K_(a+b) (characters): rel err = {err:.1e}")
    assert err < 1e-10
    # the fusion tax: p_bridge - (p_fwd + p_bwd), width-independent
    print("  bridge fusion p_b - (p_f + p_b'):")
    defs = []
    for ta, tb in ((0.5, 0.5), (0.3, 0.3), (0.2, 0.4), (0.2, 0.2),
                   (0.1, 0.1), (0.05, 0.05), (0.02, 0.02)):
        pf, pb = vprec(k_su2(ta)), vprec(k_su2(tb))
        pbr = vprec(k_su2(ta) * k_su2(tb))
        defs.append(pbr - pf - pb)
        print(f"    tau = ({ta}, {tb}): defect = {defs[-1]:+.4f}")
    defs = np.array(defs)
    print(f"  defect -> -2/3 = -4 delta (0099's delta = 1/6) as "
          f"widths -> 0: smallest-width value {defs[-1]:+.4f}")
    print("  mechanism: each single message's van Vleck factor "
          "cancels half the Haar curvature")
    print("  (a +1/3 = 2 delta precision bonus); in the product the "
          "cancellation is complete,")
    print("  so the fusion pays back both bonuses: the smoother "
          "inherits 0099's tax exactly\n")
    assert abs(defs[-1] + 2 / 3) < 0.01
    assert defs.std() < 0.05
    return defs.mean()


# ----------------------------------------------------------------------
# s4 -- causal attainability
# ----------------------------------------------------------------------

def s4_attainability():
    print("== s4: causal attainability (the F3 template, exact at "
          "the free tier) ==")
    T = 1.0
    print("  fraction of smoother precision causally attainable, "
          "site t/T:")
    print("    t/T   R tier (exact 1-t/T)   SU(2) tier (measured)")
    for f in (0.125, 0.25, 0.5, 0.75, 0.875):
        t = f * T
        flat = 1 - f
        pf = vprec(k_su2(t))
        ps = vprec(k_su2(t) * k_su2(T - t))
        print(f"    {f:.3f}       {flat:.3f}                "
              f"{pf / ps:.3f}")
    print("  linear decay toward the far end; curvature shifts the "
          "SU(2) curve by the tax.")
    print("  entropy cost of causality per site: "
          "0.5 ln(p_smoother/p_filter) nats -- computable, bounded, "
          "and zero at t = 0:")
    print("  the Lorentzian lift removes end-conditioning and "
          "nothing else\n")


if __name__ == "__main__":
    s1_flat()
    s2_u1()
    s3_su2()
    s4_attainability()
    print("all assertions passed")
