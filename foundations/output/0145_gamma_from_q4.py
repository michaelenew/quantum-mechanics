"""0145 -- item 6: the classical tests, from Q4.

The classical tests all hang off ONE number in the PPN scheme:

    g_00 = -(1 - 2U),  g_ij = (1 + 2 gamma U) delta_ij
    light deflection  ~ (1 + gamma)/2
    perihelion shift  ~ (2 + 2 gamma - beta_ppn)/3

GR has gamma = +1. A theory whose metric is conformally flat has
gamma = -1 and predicts ZERO light bending -- null geodesics are
conformally invariant. That is exactly what killed Nordstrom gravity,
and 0125's matter coupling is written conformally flat, so this is the
sharpest available test of the program and it can go either way.

THE MEASUREMENT. 0142's identity holds for an ARBITRARY per-link
weight, so nothing new is needed: let the weight depend on direction,
w_{x,mu}, which is a DIAGONAL metric,

    w_mu = sqrt(g) g^{mu mu}   =>   ln w = (J - 2I) a,
    g_{mu mu} = e^{2 a_mu},  J = all-ones.

A static mass couples to the time-time stress alone, so the source
sits in direction 0. The response is delta a = -[Gamma''_a]^{-1} J_a,
and

    gamma = - a_s / a_0 ,   a_s = (a_1 + a_2 + a_3)/3.

  s1  THE CONFORMAL GATE. Restrict the coupling to the trace mode and
      the answer must come back exactly -1. If it does not, the
      machinery is wrong and nothing after it counts.
  s2  GAMMA, flat background, as a function of distance.
  s3  GAMMA in the quantum background.
  s4  THE CLASSICAL TESTS, and the caveat that bounds them.
"""

import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, tag):
    s = importlib.util.spec_from_file_location(
        tag, os.path.join(HERE, name))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


F = _load("0142_matter_on_spin4.py", "f145")
Mmap = np.ones((4, 4)) - 2 * np.eye(4)          # ln w = (J - 2I) a


def gamma2_dir(L):
    """direction-resolved Gamma''(k) in ln w space, flat
    background: Gamma''_{mu nu}(k) = 2[delta_{mu nu} S - Chat]."""
    ax = 2 * np.pi * np.fft.fftfreq(L)
    g = np.meshgrid(*([ax] * 4), indexing="ij")
    e = [np.exp(1j * gi) - 1.0 for gi in g]
    k2 = sum(np.abs(ei) ** 2 for ei in e)
    k2s = k2.copy()
    k2s[(0,) * 4] = np.inf
    Chat = np.zeros((4, 4) + (L,) * 4)
    S = 0.0
    for mu in range(4):
        for nu in range(4):
            bz = np.fft.ifftn(e[mu] * np.conj(e[nu]) / k2s)
            C = 4.0 * np.abs(bz) ** 2
            Chat[mu, nu] = np.real(np.fft.fftn(C))
            if mu == 0:
                S += C.sum()
    G = -2.0 * Chat
    for mu in range(4):
        G[mu, mu] += 2.0 * S
    return G


def response(G, conformal=False):
    """delta a(k) for a static unit mass: source in ln w direction 0,
    at k_0 = 0. Returns the four a_mu(k) fields."""
    L = G.shape[-1]
    Ga = np.einsum("mi,mnabcd,nj->ijabcd", Mmap, G, Mmap)
    Jl = np.zeros(4)
    Jl[0] = 1.0
    Ja = Mmap.T @ Jl
    if conformal:
        # project everything onto the trace mode: the coupling is
        # forced to be a single conformal factor
        u = np.ones(4) / 2.0
        s = float(u @ Ja)
        gg = np.einsum("i,ijabcd,j->abcd", u, Ga, u)
        out = np.zeros((4,) + (L,) * 4)
        m = np.abs(gg) > np.abs(gg).max() * 1e-12
        f = np.zeros_like(gg)
        f[m] = -s / gg[m]
        f.reshape(-1)[0] = 0.0          # same zero-mode removal
        for mu in range(4):
            out[mu] = f * u[mu] * 2.0
        return out
    A = np.moveaxis(Ga.reshape(4, 4, -1), -1, 0)
    b = np.tile(Ja, (A.shape[0], 1))
    sol = np.zeros_like(b)
    # Gamma'' is a graph Laplacian on link space, so it is SINGULAR
    # at k = 0. Leaving that mode in makes the response ~1e11 and
    # identical in every direction, which fakes gamma = -1 exactly.
    # Drop it, as 0143 drops it in the scalar channel.
    for i in range(A.shape[0]):
        if i == 0:
            continue
        w = np.linalg.eigvalsh(A[i])
        if w.min() < w.max() * 1e-10:
            sol[i] = np.linalg.lstsq(A[i], -b[i], rcond=None)[0]
        else:
            sol[i] = -np.linalg.solve(A[i], b[i])
    return np.moveaxis(sol, 0, -1).reshape((4,) + (L,) * 4)


def profile(a, L):
    assert np.abs(a).max() < 1e6, (
        "response is diverging -- a singular mode was left in")
    """static projection: k_0 = 0 is the sum over the time
    separation, then read along a spatial axis."""
    out = []
    for mu in range(4):
        f = np.real(np.fft.ifftn(a[mu]))
        out.append(f.sum(0))
    return np.array(out)


def gammas(G, L, conformal=False):
    a = response(G, conformal)
    pr = profile(a, L)
    r = np.arange(1, L // 2)
    a0 = pr[0][r, 0, 0]
    asp = (pr[1] + pr[2] + pr[3])[r, 0, 0] / 3.0
    return r, -asp / a0


def s1_gate(L=32):
    print("== s1: the conformal gate ==")
    print("  Force the coupling onto the trace mode -- a single "
          "conformal factor. Then")
    print("  the metric is conformally flat by construction and "
          "gamma MUST be exactly")
    print("  -1. This tests the machinery, not the physics.")
    G = gamma2_dir(L)
    r, g = gammas(G, L, conformal=True)
    print()
    print("     r      gamma (conformal coupling)")
    for i in range(len(r)):
        print(f"    {r[i]:2d}      {g[i]:+.6f}")
    worst = float(np.abs(g + 1).max())
    print()
    print(f"  max deviation from -1: {worst:.2e}")
    assert worst < 1e-6, "conformal gate failed"
    print("  GATE PASSED. The map ln w = (J - 2I) a, the source, "
          "and the response")
    print("  reproduce Nordstrom exactly when the coupling is "
          "conformal.")
    print()
    return G


def s2_gamma(G, L=32):
    print("== s2: gamma, flat background ==")
    a = response(G)
    pr = profile(a, L)
    rr = np.arange(1, L // 2)
    a0 = pr[0][rr, 0, 0]
    asp = (pr[1] + pr[2] + pr[3])[rr, 0, 0] / 3.0
    g = -asp / a0
    # 0143's window rule: removing the zero mode forces a zero
    # crossing, and a ratio near it is undefined. Keep r where the
    # temporal response is still 2% of its r = 1 value.
    keep = np.abs(a0) > 0.02 * abs(a0[0])
    print("     r      a_0            a_s            gamma")
    for i in range(len(rr)):
        tag = "" if keep[i] else "   (outside window)"
        print(f"    {rr[i]:2d}   {a0[i]:+.5e}   {asp[i]:+.5e}   "
              f"{g[i]:+.5f}{tag}")
    gk = g[keep]
    far = float(gk.mean())
    sp = float(gk.max() - gk.min())
    print()
    print(f"  window r = {rr[keep].min()}..{rr[keep].max()}:  "
          f"gamma = {far:+.4f}, spread {sp:.4f}")
    print(f"  GR: +1.   conformally flat (Nordstrom): -1.")
    print()
    return far


def s3_quantum():
    print("== s3: does the quantum background move it? ==")
    print("  0143 measured the background to be flat in k (0.42% "
          "spread), so it should")
    print("  rescale without distorting -- and gamma is a RATIO, "
          "so a rescaling cancels")
    print("  exactly. Stated as a prediction rather than a "
          "measurement: gamma is")
    print("  protected against the background renormalisation "
          "that moved p by 1.4%.")
    print()


def s4_tests(gam):
    print("== s4: the classical tests ==")
    b = (1 + gam) / 2
    print(f"  light deflection  (1+gamma)/2 = {b:+.4f}"
          f"   x GR   ({1.75 * b:+.4f} arcsec at the solar limb)")
    print(f"  Shapiro delay     (1+gamma)/2 = {b:+.4f}   x GR")
    pp = (2 + 2 * gam - 1) / 3
    print(f"  perihelion shift  (2+2gamma-beta)/3 = {pp:+.4f}"
          f"   x GR  (beta_ppn = 1 assumed)")
    print()
    print("  Measured bounds, for scale: Cassini gives "
          "gamma - 1 = (2.1 +- 2.3)e-5.")
    print()
    if abs(gam - 1) < 0.05:
        print("  THE PROGRAM PASSES THE CLASSICAL TESTS. gamma "
              "comes out at the GR value")
        print("  from a lattice weight that was derived, not "
              "fitted.")
    elif abs(gam + 1) < 0.05:
        print("  THE PROGRAM FAILS. gamma = -1 is Nordstrom: ZERO "
              "light bending. This is")
        print("  the classical result that ruled out "
              "scalar gravity in 1919, and it")
        print("  would rule out this program in the same way.")
    else:
        print(f"  gamma = {gam:+.4f}, neither GR nor Nordstrom. "
              f"Recorded as measured; the")
        print("  deviation from 1 is far outside Cassini, so as it "
              "stands this is excluded")
        print("  by experiment unless the caveat below is the "
              "explanation.")
    print()
    print("  THE CAVEAT THAT BOUNDS ALL OF THIS. The link weight "
          "w_{x,mu} can only carry")
    print("  a DIAGONAL metric. So this probes the conformal mode "
          "and the diagonal")
    print("  traceless modes, and is blind to the off-diagonal "
          "components of h_{mu nu}.")
    print("  A theory whose bending lives in the off-diagonal "
          "sector would read wrong")
    print("  here. Extending the weight to off-diagonal links is "
          "the follow-on, and")
    print("  until it is done this number is a strong indication "
          "and not a verdict.")
    print()


if __name__ == "__main__":
    G = s1_gate()
    gam = s2_gamma(G)
    s3_quantum()
    s4_tests(gam)
    print("all assertions passed")
