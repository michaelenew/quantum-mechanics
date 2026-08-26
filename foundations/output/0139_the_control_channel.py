"""0139 -- is the spin-2 channel empty, or is the measurement blind?

0138's two-level run resolves d = 2,3,4 to ~1e-9 and finds the
connected spin-2 correlator consistent with ZERO at every one of
them. That is either

  (a) physics -- the 2++ channel is gapped so hard that it has
      decayed into the noise by d = 2, or
  (b) a broken measurement -- the operator, the ensemble, or the
      projection is not seeing anything at all.

The way to tell them apart is a CONTROL: run the identical pipeline
on the 0++ (scalar) channel, where every lattice gauge theory has a
large, easily resolved correlator. If the scalar shows a clean signal
on the same configurations and the tensor does not, (a). If neither
does, (b), and the finding is about my pipeline, not the theory.

  s1  BOTH CHANNELS, one-level, d = 0..4, same configurations.
  s2  THE EFFECTIVE MASSES, and the verdict between (a) and (b).

Checkpointed to mc0139/run.npz.
"""

import importlib.util
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CK = os.path.join(HERE, "mc0139")
os.makedirs(CK, exist_ok=True)


def _load(name, tag):
    s = importlib.util.spec_from_file_location(
        tag, os.path.join(HERE, name))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


K = _load("0134_the_spin4_kernel.py", "k139")
M = K.M132
L = 8
NCONF = 15000
CHUNK = 1000


def both_channels(Up, Um, lat):
    """returns (scalar[L], tensor[L,3,3]) -- zero-momentum slice
    operators in the 0++ and 2++ channels, one plaquette pass."""
    qp, qm = M.all_plaq(Up, lat), M.all_plaq(Um, lat)
    sc = (qp[..., 0] + qm[..., 0]).mean(1).reshape((L,) * 4)
    Bp, Bm = qp[..., 1:], qm[..., 1:]
    o = np.einsum("vpi,vpj->vpij", Bp, Bm)
    tr = np.einsum("vpii->vp", o)
    s0 = 0.5 * (o + np.swapaxes(o, -1, -2)) - (
        tr / 3)[..., None, None] * np.eye(3)
    s0 = s0.mean(1).reshape((L,) * 4 + (3, 3))
    return (sc.reshape(L, -1).mean(1),
            s0.reshape(L, -1, 3, 3).mean(1))


def run(nconf=NCONF):
    path = os.path.join(CK, "run.npz")
    lat, up, dn = K.lat_arrays(L)
    V = lat["V"]
    lp, lm = K.fresh(L)
    rs = K.seed(2139)
    sig = 0.08
    S, T = [], []
    if os.path.exists(path):
        z = np.load(path)
        S, T = list(z["S"]), list(z["T"])
        lp = np.ascontiguousarray(z["lp"])
        lm = np.ascontiguousarray(z["lm"])
        rs = np.ascontiguousarray(z["rs"])
        sig = float(z["sig"])
        print(f"  resuming from {len(S)} configurations")
    else:
        for s in range(700):
            a, t = K.csweeps(lp, lm, up, dn, V, 1, sig, rs)
            if s < 400:
                r = a / max(t, 1)
                sig *= 1.06 if r > 0.45 else (0.94 if r < 0.35 else 1)
                sig = float(np.clip(sig, 0.005, 1.0))
    t0 = time.time()
    while len(S) < nconf:
        for _ in range(CHUNK):
            if len(S) >= nconf:
                break
            K.csweeps(lp, lm, up, dn, V, 10, sig, rs)
            s_, t_ = both_channels(K.as_links(lp, V),
                                   K.as_links(lm, V), lat)
            S.append(s_)
            T.append(t_)
        np.savez(path, S=np.array(S), T=np.array(T), lp=lp, lm=lm,
                 rs=rs, sig=sig)
        el = time.time() - t0
        print(f"  {len(S)}/{nconf}, {el:.0f}s", flush=True)
    return np.array(S), np.array(T)


def conn(A, d, tensor):
    """connected slice-slice correlator at separation d, averaged
    over all t (translation average)."""
    n = A.shape[0]
    if tensor:
        Ac = A - A.mean(0)
        v = np.zeros(n)
        for t in range(L):
            v += np.einsum("nab,nab->n", Ac[:, t],
                           Ac[:, (t + d) % L])
        return v / L
    Ac = A - A.mean(0)
    return np.array([(Ac[:, t] * Ac[:, (t + d) % L])
                     for t in range(L)]).mean(0)


def jack(x, f, nb=50):
    n = len(x)
    b = n // nb
    full = f(x)
    dels = np.array([f(x[np.r_[0:k * b, (k + 1) * b:n]])
                     for k in range(nb)])
    return full, np.sqrt((nb - 1) * np.mean(
        (dels - dels.mean(0)) ** 2, axis=0))


def s1(S, T):
    print("== s1: both channels, same configurations ==")
    n = len(S)
    print(f"  L = {L}, {n} configurations, one-level estimator")
    print()
    print("     d     0++ (scalar)              2++ (tensor)")
    out = {}
    for d in range(5):
        cs, es = jack(S, lambda x, d=d: conn(x, d, False).mean())
        ct, et = jack(T, lambda x, d=d: conn(x, d, True).mean())
        out[d] = (float(cs), float(es), float(ct), float(et))
        print(f"    {d:2d}   {cs:+.4e} +- {es:.1e}"
              f"   ({abs(cs) / max(es, 1e-99):5.1f}s)   "
              f"{ct:+.4e} +- {et:.1e}   "
              f"({abs(ct) / max(et, 1e-99):5.1f}s)")
    print()
    return out


def s2(S, T, out):
    print("== s2: effective masses, and the verdict ==")
    print()
    print("     d -> d+1      0++ m_eff a           2++ m_eff a")

    def me(x, d, tensor):
        a = conn(x, d, tensor).mean()
        b = conn(x, d + 1, tensor).mean()
        return np.log(a / b) if (a > 0 and b > 0) else np.nan

    for d in range(3):
        ms, es = jack(S, lambda x, d=d: me(x, d, False))
        mt, et = jack(T, lambda x, d=d: me(x, d, True))
        fs = "nan" if not np.isfinite(ms) else f"{ms:+.4f} +- {es:.4f}"
        ft = "nan" if not np.isfinite(mt) else f"{mt:+.4f} +- {et:.4f}"
        print(f"    {d} -> {d + 1}      {fs:22s}{ft}")
    print()
    sig_s = max(abs(out[d][0]) / max(out[d][1], 1e-99)
                for d in (1, 2, 3))
    sig_t = max(abs(out[d][2]) / max(out[d][3], 1e-99)
                for d in (1, 2, 3))
    print(f"  best significance at d >= 1:  "
          f"0++ {sig_s:.1f} sigma,  2++ {sig_t:.1f} sigma")
    print()
    if sig_s > 5 and sig_t < 3:
        print("  (a) THE PIPELINE WORKS. The scalar correlator "
              "is resolved on the same")
        print("  configurations with the same code, so the "
              "tensor's silence is not the")
        print("  measurement failing.")
        print()
        print("  BUT NOT 'THE CHANNEL IS EMPTY'. 0141 shows why "
              "that reading would be")
        print("  wrong: the mean plaquette here is 0.957, so beta "
              "~ 16-17.5, so by")
        print("  asymptotic freedom xi/a ~ 1e18. Nothing bound can "
              "appear on an 8^4 box")
        print("  that is 1e-17 of one correlation length -- in "
              "EITHER channel. What the")
        print("  0++ column shows is therefore not a glueball "
              "mass; it is the")
        print("  ultraviolet slope of a local operator on a very "
              "fine lattice, and the")
        print("  2++ operator simply has less ultraviolet in it. "
              "Both channels are UV.")
    elif sig_s > 5 and sig_t > 3:
        print("  BOTH CHANNELS CARRY SIGNAL. The tensor is "
              "resolved after all at short")
        print("  distance; 0138's null at d >= 2 is then a "
              "statement about the tail, and")
        print("  the mass comes from the short-distance slopes "
              "above.")
    else:
        print("  (b) NEITHER CHANNEL IS RESOLVED. The finding is "
              "about the pipeline, not")
        print("  the theory: a zero-momentum slice correlator that "
              "cannot see the 0++")
        print("  channel is not measuring what it claims to. That "
              "is the next thing to")
        print("  fix, and it is a much better problem to have than "
              "an ambiguous null.")
    print()


if __name__ == "__main__":
    S, T = run()
    out = s1(S, T)
    s2(S, T, out)
    print("done")
