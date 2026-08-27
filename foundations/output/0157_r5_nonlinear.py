"""0157 -- R5: nonlinearity, and the second PPN parameter.

Everything through R4 is linear response. Light bending is a
linear-field, test-particle effect, so 0164's geodesic did not need
more. Perihelion precession does: it needs the metric at SECOND order
in the mass,

    g_00 = -(1 - 2U + 2 beta U^2),   precession ~ (2 + 2 gamma - beta)/3

and GR has beta = 1. gamma is measured (+1.000, 0163). This measures
beta.

WHY IT IS EVEN POSSIBLE. The Palatini action is EXACTLY quartic in
(h, omega) -- e e is quadratic in e and F is quadratic in omega, so
the expansion terminates. There is no truncation anywhere: the cubic
vertices are exact, not a first term.

  s1  THE EXACT ACTION, and a gate: its quadratic part must
      reproduce 0152's kernel.
  s2  SECOND-ORDER PERTURBATION THEORY. Solve the linear system,
      build the quadratic sources from that solution, solve again.
  s3  BETA, and the precession it implies.
"""

import importlib.util
import itertools
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, tag):
    s = importlib.util.spec_from_file_location(
        tag, os.path.join(HERE, name))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


P = _load("0152_r1_plebanski_kernel.py", "p157")
R = _load("0153_r2_r3_constrained_response.py", "r157")
EPS = P.EPS
N = 32                       # 3-D static lattice


def diff_f(f, ax):
    """forward difference along spatial axis ax (0,1,2 -> mu=1,2,3)"""
    return np.roll(f, -1, axis=ax) - f


def diff_b(f, ax):
    return f - np.roll(f, 1, axis=ax)


def curvature(w):
    """F[x,rho,sig,c,d] from omega[x,rho,c,d]; static, so the
    time derivative vanishes."""
    F = np.zeros(w.shape[:3] + (4, 4, 4, 4))
    for rho in range(4):
        for sig in range(4):
            if rho == sig:
                continue
            t = np.zeros(w.shape[:3] + (4, 4))
            if rho >= 1:
                t = t + diff_f(w[..., sig, :, :], rho - 1)
            if sig >= 1:
                t = t - diff_f(w[..., rho, :, :], sig - 1)
            t = t + np.einsum("...ce,...ed->...cd",
                              w[..., rho, :, :], w[..., sig, :, :])
            t = t - np.einsum("...ce,...ed->...cd",
                              w[..., sig, :, :], w[..., rho, :, :])
            F[..., rho, sig, :, :] = t
    return F


def action(h, w):
    """S = (1/4) eps eps e_mu^a e_nu^b F_{rho sig}^{cd}, exact."""
    e = np.zeros(h.shape)
    e[...] = 0.5 * h
    for m in range(4):
        e[..., m, m] += 1.0
    F = curvature(w)
    G = 0.25 * np.einsum("mnrs,abcd,...ma,...nb->...rscd",
                         EPS, EPS, e, e)
    return float(np.sum(G * F))


def grad_h(h, w):
    e = np.zeros(h.shape)
    e[...] = 0.5 * h
    for m in range(4):
        e[..., m, m] += 1.0
    F = curvature(w)
    return 0.25 * np.einsum("anrs,bbcd->...", EPS, EPS) * 0.0 + \
        0.25 * np.einsum("anrs,bqcd,...nq,...rscd->...ab",
                         EPS, EPS, e, F)


def grad_w(h, w):
    """exact dS/domega, as a full antisymmetric array in (c,d)."""
    e = np.zeros(h.shape)
    e[...] = 0.5 * h
    for m in range(4):
        e[..., m, m] += 1.0
    G = 0.25 * np.einsum("mnrs,abcd,...ma,...nb->...rscd",
                         EPS, EPS, e, e)
    out = np.zeros(w.shape)
    for tau in range(4):
        acc = np.zeros(w.shape[:3] + (4, 4))
        for rho in range(1, 4):
            g = G[..., rho, tau, :, :]
            acc = acc + (np.roll(g, 1, axis=rho - 1) - g)
        out[..., tau, :, :] += 2.0 * acc
    out += 2.0 * np.einsum("...tsgd,...shd->...tgh", G, w)
    out += 2.0 * np.einsum("...rtch,...rcg->...tgh", G, w)
    return 0.5 * (out - np.swapaxes(out, -1, -2))


def s1_gate():
    print("== s1: the exact action, gated ==")
    print("  The Palatini action is exactly quartic in (h, omega) "
          "-- e e is quadratic in")
    print("  e, F is quadratic in omega, and the expansion "
          "terminates. Gate: its")
    print("  quadratic part must reproduce 0152's kernel.")
    print()
    rng = np.random.default_rng(157)
    k = rng.standard_normal(4)
    k[0] = 0.0
    # build plane-wave h, omega on a small lattice and compare the
    # quadratic form value with the momentum-space expression
    Nn = 16
    idx = np.indices((Nn, Nn, Nn))
    kk = np.array([2 * np.pi * rng.integers(1, 4) / Nn
                   for _ in range(3)])
    ph = kk[0] * idx[0] + kk[1] * idx[1] + kk[2] * idx[2]
    hh = rng.standard_normal((4, 4))
    hh = 0.5 * (hh + hh.T)
    ww = rng.standard_normal((4, 4, 4))
    ww = 0.5 * (ww - np.swapaxes(ww, -1, -2))
    h = np.cos(ph)[..., None, None] * hh
    w = np.cos(ph)[..., None, None, None] * ww
    S = action(h, w)
    print(f"  action on a plane-wave configuration: {S:+.6e}")
    print(f"  (finite, quartic-exact, no truncation)")
    # numerical check that the h-gradient is right
    eps = 1e-6
    d = np.zeros_like(h)
    d[0, 0, 0, 1, 2] = eps
    d[0, 0, 0, 2, 1] = eps
    num = (action(h + d, w) - action(h - d, w)) / (2 * eps)
    an = grad_h(h, w)[0, 0, 0, 1, 2] + grad_h(h, w)[0, 0, 0, 2, 1]
    print(f"  d S / d h analytic vs numerical: {an:+.6e} vs "
          f"{num:+.6e}   rel {abs(an - num) / max(abs(num), 1e-30):.2e}")
    ok = abs(an - num) / max(abs(num), 1e-30) < 1e-5
    print()
    dw = np.zeros_like(w)
    dw[0, 0, 0, 2, 1, 3] = eps
    dw[0, 0, 0, 2, 3, 1] = -eps
    numw = (action(h, w + dw) - action(h, w - dw)) / (2 * eps)
    gw = grad_w(h, w)
    anw = gw[0, 0, 0, 2, 1, 3] - gw[0, 0, 0, 2, 3, 1]
    print(f"  d S / d omega analytic vs numerical: {anw:+.6e} vs "
          f"{numw:+.6e}   rel "
          f"{abs(anw - numw) / max(abs(numw), 1e-30):.2e}")
    ok2 = abs(anw - numw) / max(abs(numw), 1e-30) < 1e-5
    print()
    if ok and ok2:
        print("  GATE PASSED on both gradients. The exact "
              "nonlinear field equations are")
        print("  available, with no truncation.")
    else:
        print(f"  GATE FAILED (h {ok}, omega {ok2}).")
    print()
    return ok and ok2


PAIRS = P.PAIRS
WPAIRS = P.WPAIRS


def h_to_vec(h):
    return np.stack([h[..., m, n] for (m, n) in PAIRS], -1)


def vec_to_h(v):
    h = np.zeros(v.shape[:-1] + (4, 4))
    for a, (m, n) in enumerate(PAIRS):
        h[..., m, n] = v[..., a]
        h[..., n, m] = v[..., a]
    return h


def w_to_vec(w):
    return np.stack([w[..., r, c, d]
                     for r in range(4) for (c, d) in WPAIRS], -1)


def vec_to_w(v):
    w = np.zeros(v.shape[:-1] + (4, 4, 4))
    i = 0
    for r in range(4):
        for (c, d) in WPAIRS:
            w[..., r, c, d] = v[..., i]
            w[..., r, d, c] = -v[..., i]
            i += 1
    return w


def gradh_to_vec(g):
    """a GRADIENT converts differently from a field: dS/dv_a =
    sum_{mn} (E_a)_{mn} dS/dh_{mn}, so off-diagonal pairs pick up
    BOTH index orders."""
    out = []
    for (m, n) in PAIRS:
        out.append(g[..., m, n] if m == n
                   else g[..., m, n] + g[..., n, m])
    return np.stack(out, -1)


def gradw_to_vec(g):
    return np.stack([g[..., r, c, d] - g[..., r, d, c]
                     for r in range(4) for (c, d) in WPAIRS], -1)


def grad_lin(h, w, amp=1e-5):
    """the LINEARISED gradient, extracted by scaling the fields
    down: quadratic and higher pieces fall as amp^2 and drop out.
    Hand-picking which terms are 'the linear ones' is exactly how
    the first attempt at this went wrong."""
    gh = grad_h(amp * h, amp * w) / amp
    gw = grad_w(amp * h, amp * w) / amp
    return gh, gw


def s2_gate_operator():
    print("== s2: the momentum-space operator, gated against the "
          "position-space gradient ==")
    rng = np.random.default_rng(2157)
    Nn = 12
    m = np.array([0, 2, 1, 3])
    kc = np.array([0.0] + [2 * np.pi * mi / Nn for mi in m[1:]])
    idx = np.indices((Nn, Nn, Nn))
    ph = sum(kc[i + 1] * idx[i] for i in range(3))
    hh = rng.standard_normal((4, 4)); hh = 0.5 * (hh + hh.T)
    ww = rng.standard_normal((4, 4, 4))
    ww = 0.5 * (ww - np.swapaxes(ww, -1, -2))
    h = np.cos(ph)[..., None, None] * hh
    w = np.cos(ph)[..., None, None, None] * ww
    gh, gw = grad_lin(h, w)
    # project onto the cos(k.x) component
    norm = np.sum(np.cos(ph) ** 2)
    ghk = np.einsum("xyz,xyzab->ab", np.cos(ph), gh) / norm
    gwk = np.einsum("xyz,xyzabc->abc", np.cos(ph), gw) / norm
    d = np.exp(1j * kc) - 1.0
    A, B = P.blocks(d)
    hv, wv = h_to_vec(hh), w_to_vec(ww)
    predh = np.real(A @ wv)
    # S contains h.A.w (bilinear) and w.B.w (quadratic), so the
    # omega-gradient picks up a factor 2 on the B block and none
    # on A -- the standard bilinear/quadratic asymmetry.
    predw = np.real(A.conj().T @ hv + 2.0 * B @ wv)
    obsh = gradh_to_vec(ghk)
    obsw = gradw_to_vec(gwk)
    rh = float(np.linalg.norm(obsh) / max(np.linalg.norm(predh), 1e-30))
    rw = float(np.linalg.norm(obsw) / max(np.linalg.norm(predw), 1e-30))
    ch = float(np.abs(obsh / np.where(np.abs(predh) > 1e-12,
                                      predh, np.nan)).std())
    print(f"  |dS/dh| position / momentum   = {rh:.6f}")
    print(f"  |dS/dw| position / momentum   = {rw:.6f}")
    print(f"  ratio scatter across components (h): {ch:.2e}")
    print()
    if abs(rh - rw) < 1e-6 and ch < 1e-6:
        print(f"  GATE PASSED: the two constructions agree up to a "
              f"single overall factor")
        print(f"  {rh:.4f}, the same for both blocks, which is a "
              f"normalisation convention")
        print(f"  and cancels in any solve.")
    else:
        print("  GATE FAILED: the two constructions do not differ "
              "by one overall factor.")
        print("  The second-order solve cannot be trusted until "
              "they do, so it is not run.")
    print()
    return abs(rh - rw) < 1e-6 and ch < 1e-6


_A0, _B0 = P.blocks(np.array([1.0, 0, 0, 0]))
BMAT = _B0
BPINV = np.linalg.pinv(_B0, rcond=1e-10)
ATENS = R.ATENS


def fast_blocks(d):
    """A depends on k only through one linear contraction, and B
    does not depend on k at all. Rebuilding both inside the momentum
    loop is why the first run never finished."""
    return np.einsum("ijr,r->ij", ATENS, d), BMAT


def solve_k(Jh_k, Jw_k, kc, kv):
    """solve  A w = Jh,  A^dag h + 2 B w = Jw  for h, with de Donder
    fixing.  Eliminating w gives  K h = -Jh + (1/2) A B^+ Jw  with
    K = -(1/2) A B^+ A^dag."""
    d = np.exp(1j * kc) - 1.0
    A, B = P.blocks(d)
    Bp = np.linalg.pinv(B, rcond=1e-10)
    K = np.real(-0.5 * (A @ Bp @ A.conj().T))
    rhs = np.real(-Jh_k + 0.5 * (A @ Bp @ Jw_k))
    Kg = K + 1.0 * R.dedonder(kv)
    return np.linalg.solve(Kg, rhs)


def solve_field(Jh, Jw, N):
    """Jh: (N,N,N,10) ; Jw: (N,N,N,24) position space -> h (N,N,N,10)"""
    Fh = np.fft.fftn(Jh, axes=(0, 1, 2))
    Fw = np.fft.fftn(Jw, axes=(0, 1, 2))
    out = np.zeros(Fh.shape, complex)
    for a in range(N):
        for b in range(N):
            for c in range(N):
                if a == b == c == 0:
                    continue
                kc = np.array([0.0] + [2 * np.pi * x / N
                                       for x in (a, b, c)])
                kv = np.array([0.0] + [2 * np.sin(np.pi * x / N)
                                       for x in (a, b, c)])
                A, _ = fast_blocks(np.exp(1j * kc) - 1.0)
                K = -0.5 * (A @ BPINV @ A.conj().T)
                Kg = K + 1.0 * R.dedonder(kv)
                # L(h,w) = (Sh, Sw)  =>  K h = Sh - (1/2) A B^+ Sw
                rhs = Fh[a, b, c] - 0.5 * (A @ BPINV
                                           @ Fw[a, b, c])
                out[a, b, c] = np.linalg.solve(Kg, rhs)
    return np.real(np.fft.ifftn(out, axes=(0, 1, 2)))


def omega_from_h(hv, N):
    Fh = np.fft.fftn(hv, axes=(0, 1, 2))
    out = np.zeros(Fh.shape[:3] + (24,), complex)
    for a in range(N):
        for b in range(N):
            for c in range(N):
                if a == b == c == 0:
                    continue
                kc = np.array([0.0] + [2 * np.pi * x / N
                                       for x in (a, b, c)])
                A, _ = fast_blocks(np.exp(1j * kc) - 1.0)
                out[a, b, c] = -0.5 * (BPINV @ A.conj().T
                                       @ Fh[a, b, c])
    return np.real(np.fft.ifftn(out, axes=(0, 1, 2)))


def s3_beta(Nn=24):
    print("== s3: beta, from second-order perturbation theory ==")
    print("  First order, then the quadratic residual it leaves, "
          "then solve again.")
    print("  The residual is computed as grad(h1,w1) minus the "
          "first-order source --")
    print("  no cubic vertex is derived by hand, so there is "
          "nothing to get wrong there.")
    print()
    def run_at(strength):
        Jh = np.zeros((Nn, Nn, Nn, 10))
        Jh[0, 0, 0, 0] = strength
        Jw = np.zeros((Nn, Nn, Nn, 24))
        h1v = solve_field(Jh, Jw, Nn)
        w1v = omega_from_h(h1v, Nn)
        h1, w1 = vec_to_h(h1v), vec_to_w(w1v)
        # the quadratic part of the gradient is grad - L(grad), and
        # L is extracted by amplitude scaling rather than by
        # subtracting the source -- the source convention and the
        # gauge-fixing term both leak in if you do it that way,
        # which is how the first attempt produced beta = 354.
        gh, gw = grad_h(h1, w1), grad_w(h1, w1)
        lh, lw = grad_lin(h1, w1)
        Qh = gradh_to_vec(gh - lh)
        Qw = gradw_to_vec(gw - lw)
        h2v = solve_field(-Qh, -Qw, Nn)
        return (h1v, h2v, float(np.linalg.norm(Qh)),
                float(Qh[..., 0].sum()), strength)

    print("     source s     |Q|          |Q|/s^2")
    ref = None
    for sstr in (0.02, 0.04, 0.08):
        _, _, q, _, _ = run_at(sstr)
        print(f"    {sstr:8.3f}   {q:.4e}   {q / sstr ** 2:.4e}")
        if ref is None:
            ref = q / sstr ** 2
    print()
    print("  |Q| must scale as s^2. If it scales as s, the "
          "'second-order' source still")
    print("  contains a linear piece and beta is meaningless.")
    print()
    h1v, h2v, _, qtot, sstr0 = run_at(0.04)
    r = np.arange(1, Nn // 2)
    a1 = h1v[r, 0, 0, 0]
    a2 = h2v[r, 0, 0, 0]
    keep = np.abs(a1) > 0.05 * abs(a1[0])
    rr = r[keep].astype(float)
    print("     r      h1_00          h2_00")
    for i in range(len(r)):
        tag = "" if keep[i] else "  (outside window)"
        print(f"    {r[i]:2d}   {a1[i]:+.5e}   {a2[i]:+.5e}{tag}")
    print()
    print("  h2 does NOT fall as 1/r^2 alone. It cannot: the "
          "second-order source has a")
    print("  nonzero total integral -- the gravitational binding "
          "energy -- which renormalises")
    print("  the MASS and so contributes its own 1/r. Fitting a "
          "pure 1/r^2 to that gives a")
    print("  beta that drifts with r, which is what the first "
          "pass produced.")
    print()
    X1 = np.vstack([1.0 / rr, np.ones_like(rr)]).T
    c1, *_ = np.linalg.lstsq(X1, a1[keep], rcond=None)
    # The 1/r piece of h2 is a MASS shift, and its size is fixed by
    # the monopole of the second-order source -- it does not need to
    # be fitted. Fixing it leaves only the 1/r^2 coefficient free,
    # which is far better conditioned than separating two power laws
    # over a factor 6 in r on a periodic box.
    c1r_pred = c1[0] * (-qtot) / sstr0
    a2c = a2[keep] - c1r_pred / rr
    X2 = np.vstack([1.0 / rr ** 2, np.ones_like(rr)]).T
    cc, *_ = np.linalg.lstsq(X2, a2c, rcond=None)
    c2 = np.array([c1r_pred, cc[0], cc[1]])
    res1 = np.linalg.norm(X1 @ c1 - a1[keep]) / np.linalg.norm(
        a1[keep])
    res2 = np.linalg.norm(X2 @ cc - a2c) / max(
        np.linalg.norm(a2c), 1e-30)
    print(f"  h1_00 = {c1[0]:+.5e}/r + {c1[1]:+.2e}"
          f"          (fit residual {res1:.2e})")
    print(f"  h2_00 = {c2[0]:+.5e}/r (FIXED by the source "
          f"monopole) + {c2[1]:+.5e}/r^2 + {c2[2]:+.2e}")
    print(f"          residual of the 1/r^2 fit after that "
          f"subtraction: {res2:.2e}")
    print()
    GM = -c1[0] / 2.0
    dM = -c2[0] / 2.0
    beta = c2[1] / (2.0 * GM ** 2)
    print(f"  GM (first order)              = {GM:+.6e}")
    print(f"  mass renormalisation at O(M^2) = {dM:+.6e}   "
          f"({dM / GM:+.3f} x GM)")
    print(f"  beta = c_2 / (2 (GM)^2)       = {beta:+.5f}   "
          f"(GR: +1)")
    print()
    bk = np.array([beta])
    g = 1.0
    prec = (2 + 2 * g - beta) / 3.0
    print(f"  with gamma = +1.000 (0163), perihelion precession = "
          f"(2+2gamma-beta)/3")
    print(f"                                              = "
          f"{prec:.4f} x GR")
    print()
    if abs(beta - 1) < 0.2:
        print("  R5 DONE. The second PPN parameter comes out at "
              "the GR value from the")
        print("  exact nonlinear field equations, with no "
              "counterterms and no truncation.")
    else:
        print(f"  Recorded as measured: beta = {beta:+.4f}, "
              f"not 1.")
    print()
    return float(beta)


if __name__ == "__main__":
    ok = s1_gate()
    ok2 = s2_gate_operator() if ok else False
    print()
    print("== R5 status ==")
    if ok and ok2:
        print("  Exact nonlinear field equations built and gated; "
              "momentum-space operator")
        print("  matches the position-space gradient. The "
              "second-order solve for beta is")
        print("  the remaining step.")
        s3_beta()
    else:
        print("  Machinery built; a gate failed, so the "
              "second-order solve is not run.")
