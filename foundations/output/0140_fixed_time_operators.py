"""0140 -- the operator was not a fixed-time operator.

0139's control settles that the pipeline can see a signal: the 0++
correlator is resolved at 105 sigma at d = 0 and 13.6 sigma at d = 1
on the same configurations where the 2++ shows nothing past d = 0.
So the measurement is not blind. But before calling the tensor
channel empty, two things about the OPERATOR have to be fixed, and
both are standard:

  1. FIXED TIME. all_plaq returns plaquettes in the order
     (0,1),(0,2),(0,3),(1,2),(1,3),(2,3) -- the first three are
     TEMPORAL. An operator averaging all six straddles two time
     slices, so it is not an operator of the transfer matrix at all,
     and its correlator is contaminated by contact terms at d = 0
     and d = 1. That is exactly the pattern 0139 measured: enormous
     at d = 0, nothing after. Indices 3,4,5 are the spatial
     plaquettes; a fixed-time operator uses only those.

  2. OVERLAP. A correlator that vanishes past d = 0 does not prove
     there is no light state -- it bounds that state's OVERLAP with
     this operator. The standard cure is APE link smearing, which in
     the quaternion representation is exact and free: SU(2) matrices
     are unit quaternions, so "project the staple sum back onto the
     group" is just normalisation.

  s1  APE SMEARING, gated: smeared links stay in the group and
      smearing must raise the spatial plaquette (it is a local
      cooling).
  s2  BOTH CHANNELS, fixed-time, at four smearing levels.
  s3  THE MASS, OR THE BOUND -- whichever the data supports.

Checkpointed to mc0140/run.npz.
"""

import importlib.util
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CK = os.path.join(HERE, "mc0140")
os.makedirs(CK, exist_ok=True)


def _load(name, tag):
    s = importlib.util.spec_from_file_location(
        tag, os.path.join(HERE, name))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


K = _load("0134_the_spin4_kernel.py", "k140")
M = K.M132
qmul, qinv = M.qmul, M.qinv
L = 8
NSM = [0, 2, 4, 8]
ALPHA = 0.5
NCONF = 6000
CHUNK = 500
SPAT = [3, 4, 5]          # (1,2), (1,3), (2,3)


def sp_staple(U, lat, mu):
    up, dn = lat["up"], lat["dn"]
    tot = 0.0
    for nu in (1, 2, 3):
        if nu == mu:
            continue
        f = qmul(qmul(U[nu], U[mu][up[nu]]), qinv(U[nu][up[mu]]))
        y = dn[nu]
        b = qmul(qmul(qinv(U[nu][y]), U[mu][y]),
                 U[nu][up[mu][y]])
        tot = tot + f + b
    return tot


def ape(U, lat, n, alpha=ALPHA):
    """APE-smear the SPATIAL links n times. For SU(2) the group
    projection is exactly quaternion normalisation."""
    V = [u.copy() for u in U]
    for _ in range(n):
        W = [v.copy() for v in V]
        for mu in (1, 2, 3):
            q = V[mu] + alpha * sp_staple(V, lat, mu)
            nrm = np.linalg.norm(q, axis=-1, keepdims=True)
            W[mu] = q / np.maximum(nrm, 1e-300)
        V = W
    return V


def ops(Up, Um, lat, nsm):
    """fixed-time zero-momentum 0++ and 2++ slice operators from the
    SPATIAL plaquettes of nsm-times-smeared links."""
    A = ape(Up, lat, nsm) if nsm else Up
    B = ape(Um, lat, nsm) if nsm else Um
    qp = M.all_plaq(A, lat)[:, SPAT]
    qm = M.all_plaq(B, lat)[:, SPAT]
    sc = (qp[..., 0] + qm[..., 0]).mean(1).reshape((L,) * 4)
    Bp, Bm = qp[..., 1:], qm[..., 1:]
    o = np.einsum("vpi,vpj->vpij", Bp, Bm)
    tr = np.einsum("vpii->vp", o)
    s0 = 0.5 * (o + np.swapaxes(o, -1, -2)) - (
        tr / 3)[..., None, None] * np.eye(3)
    s0 = s0.mean(1).reshape((L,) * 4 + (3, 3))
    return (sc.reshape(L, -1).mean(1),
            s0.reshape(L, -1, 3, 3).mean(1))


def s1_gate():
    print("== s1: APE smearing, gated ==")
    lat, up, dn = K.lat_arrays(L)
    V = lat["V"]
    lp, lm = K.fresh(L)
    rs = K.seed(51)
    sig = 0.08
    for s in range(400):
        a, t = K.csweeps(lp, lm, up, dn, V, 1, sig, rs)
        r = a / max(t, 1)
        sig *= 1.06 if r > 0.45 else (0.94 if r < 0.35 else 1)
        sig = float(np.clip(sig, 0.005, 1.0))
    U = K.as_links(lp, V)
    prev = None
    print("     smearings   |q| max deviation from 1   mean "
          "spatial plaquette")
    for n in NSM:
        S = ape(U, lat, n)
        dev = max(float(np.abs(np.linalg.norm(S[mu], axis=-1)
                               - 1).max()) for mu in (1, 2, 3))
        pl = float(M.all_plaq(S, lat)[:, SPAT, 0].mean())
        print(f"        {n:2d}          {dev:.2e}                  "
              f"{pl:+.6f}")
        assert dev < 1e-12, "smeared link left the group"
        if prev is not None:
            assert pl > prev - 1e-9, "smearing lowered the plaquette"
        prev = pl
    print("  smeared links stay exactly in SU(2) and the plaquette "
          "rises monotonically")
    print("  -- smearing is cooling, as it must be")
    print()
    return lat, up, dn, V, lp, lm, rs, sig


def run(st, nconf=NCONF):
    lat, up, dn, V, lp, lm, rs, sig = st
    path = os.path.join(CK, "run.npz")
    S = {n: [] for n in NSM}
    T = {n: [] for n in NSM}
    if os.path.exists(path):
        z = np.load(path)
        for n in NSM:
            S[n] = list(z[f"S{n}"])
            T[n] = list(z[f"T{n}"])
        lp = np.ascontiguousarray(z["lp"])
        lm = np.ascontiguousarray(z["lm"])
        rs = np.ascontiguousarray(z["rs"])
        sig = float(z["sig"])
        print(f"  resuming from {len(S[NSM[0]])} configurations")
    t0 = time.time()
    while len(S[NSM[0]]) < nconf:
        for _ in range(CHUNK):
            if len(S[NSM[0]]) >= nconf:
                break
            K.csweeps(lp, lm, up, dn, V, 10, sig, rs)
            Up, Um = K.as_links(lp, V), K.as_links(lm, V)
            for n in NSM:
                s_, t_ = ops(Up, Um, lat, n)
                S[n].append(s_)
                T[n].append(t_)
        d = {f"S{n}": np.array(S[n]) for n in NSM}
        d.update({f"T{n}": np.array(T[n]) for n in NSM})
        np.savez(path, lp=lp, lm=lm, rs=rs, sig=sig, **d)
        el = time.time() - t0
        print(f"  {len(S[NSM[0]])}/{nconf}, {el:.0f}s", flush=True)
    return ({n: np.array(S[n]) for n in NSM},
            {n: np.array(T[n]) for n in NSM})


def conn(A, d, tensor):
    Ac = A - A.mean(0)
    if tensor:
        return sum(np.einsum("nab,nab->n", Ac[:, t],
                             Ac[:, (t + d) % L])
                   for t in range(L)) / L
    return np.mean([Ac[:, t] * Ac[:, (t + d) % L]
                    for t in range(L)], axis=0)


def jack(x, f, nb=50):
    n = len(x)
    b = n // nb
    full = f(x)
    dl = np.array([f(x[np.r_[0:k * b, (k + 1) * b:n]])
                   for k in range(nb)])
    return full, np.sqrt((nb - 1) * np.mean(
        (dl - dl.mean(0)) ** 2, axis=0))


def s2(S, T):
    print("== s2: fixed-time correlators, four smearing levels ==")
    n = len(S[NSM[0]])
    print(f"  L = {L}, {n} configurations, spatial plaquettes only")
    res = {}
    for nsm in NSM:
        print(f"\n  --- {nsm} smearings ---")
        print("     d     0++                        2++")
        for d in range(5):
            cs, es = jack(S[nsm],
                          lambda x, d=d: conn(x, d, False).mean())
            ct, et = jack(T[nsm],
                          lambda x, d=d: conn(x, d, True).mean())
            res[(nsm, d)] = (float(cs), float(es), float(ct),
                             float(et))
            print(f"    {d:2d}   {cs:+.4e} +- {es:.1e} "
                  f"({abs(cs) / max(es, 1e-99):5.1f}s)   "
                  f"{ct:+.4e} +- {et:.1e} "
                  f"({abs(ct) / max(et, 1e-99):5.1f}s)")
    print()
    return res


def s3(S, T, res):
    print("== s3: the mass, or the bound ==")
    print()
    print("     smear    0++ m_eff(0->1)        2++ m_eff(0->1)")

    def me(x, d, tensor):
        a = conn(x, d, tensor).mean()
        b = conn(x, d + 1, tensor).mean()
        return np.log(a / b) if (a > 0 and b > 0) else np.nan

    best_t = (None, 0.0)
    for nsm in NSM:
        ms, es = jack(S[nsm], lambda x: me(x, 0, False))
        mt, et = jack(T[nsm], lambda x: me(x, 0, True))
        fs = "nan" if not np.isfinite(ms) else f"{ms:.4f} +- {es:.4f}"
        ft = "nan" if not np.isfinite(mt) else f"{mt:.4f} +- {et:.4f}"
        print(f"      {nsm:2d}     {fs:22s} {ft}")
        c1, e1 = res[(nsm, 1)][2], res[(nsm, 1)][3]
        if abs(c1) / max(e1, 1e-99) > best_t[1]:
            best_t = (nsm, abs(c1) / max(e1, 1e-99))
    print()
    print(f"  best 2++ significance at d = 1 over all smearings: "
          f"{best_t[1]:.1f} sigma (at {best_t[0]} smearings)")
    print()
    if best_t[1] > 4:
        nsm = best_t[0]
        mt, et = jack(T[nsm], lambda x: me(x, 0, True))
        print(f"  THE TENSOR CHANNEL IS RESOLVED once the operator "
              f"is fixed-time and smeared.")
        print(f"  m(2++) a = {mt:.4f} +- {et:.4f}, "
              f"xi/a = {1 / mt:.3f}")
    else:
        c0 = res[(best_t[0], 0)][2]
        c1e = res[(best_t[0], 1)][3]
        bound = np.log(c0 / (3 * c1e))
        print("  STILL NOTHING AT d >= 1, with a fixed-time, "
              "smeared operator.")
        print(f"  That is now a BOUND, not a blind spot: any state "
              f"in this channel has")
        print(f"  either m a > {bound:.2f} (xi < {1 / bound:.3f} a) "
              f"or overlap below")
        print(f"  {100 * 3 * c1e / c0:.2f}% of the operator's norm.")
        print()
        print("  CORRECTION, from 0141. An earlier draft of this "
              "line read the bound as")
        print("  'everything in this theory is "
              "sub-lattice-spacing'. That is backwards. The")
        print("  plaquette is 0.957 -- an almost frozen lattice -- "
              "so beta ~ 16-17.5 and")
        print("  xi/a ~ 1e18. The correlation length is enormous, "
              "not tiny. A local")
        print("  operator on an 8^4 box at this spacing cannot "
              "overlap a state of size")
        print("  1e18 a, which is exactly why the overlap bound "
              "above is the binding one")
        print("  and the mass bound is not. Note too that smearing "
              "REDUCES the 2++ signal")
        print("  (1.7e-9 at 4 smearings, 2.1e-10 at 8): it is "
              "removing ultraviolet")
        print("  fluctuation, and ultraviolet fluctuation is all "
              "this operator has here.")
    print()


if __name__ == "__main__":
    st = s1_gate()
    S, T = run(st)
    res = s2(S, T)
    s3(S, T, res)
    print("all assertions passed")
