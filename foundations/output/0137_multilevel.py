"""0137 -- the granularity was wrong: multilevel, not multihit.

0136 ported lucid 0048's Rao-Blackwell fix at LINK granularity and
measured 0.98x. Unbiased, and worthless. The reason is in the
decomposition the fix rests on,

    Var(X) = Var(E[X|Z]) + E[Var(X|Z)] ,

and Rao-Blackwell removes only the SECOND term. Conditioning on every
link but one leaves Z containing almost the whole field, so
Var(E[X|Z]) is already nearly Var(X) and there is nothing to take.
The filter's law was right; a link is the wrong unit.

The right unit is a REGION. Freeze the spatial links on a set of time
slices; the sub-lattices between them then interact only through those
frozen links, so the site operators in different blocks are
CONDITIONALLY INDEPENDENT, and

    E[O(x)O(y) | boundary] = E[O(x)|bdry] . E[O(y)|bdry] ,

each factor estimated by its own sub-average. Now Z is only the
boundary, Var(E[X|Z]) is genuinely smaller, and the two sub-averages
multiply. This is Luescher-Weisz two-level; it is also exactly what
lucid 0048 s2 measured, at the granularity where the conditional
variance is actually large.

  s1  THE FROZEN KERNEL, and its gate: frozen links must not move,
      and unfrozen dynamics must match the unfrozen kernel.
  s2  THE VARIANCE BUDGET at both granularities -- what fraction of
      the operator's variance each choice of Z leaves on the table.
  s3  THE TWO-LEVEL CORRELATOR against the one-level one, matched on
      cost, with the bias check.
"""

import ctypes
import hashlib
import importlib.util
import os
import subprocess
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, tag):
    s = importlib.util.spec_from_file_location(
        tag, os.path.join(HERE, name))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


K = _load("0134_the_spin4_kernel.py", "k134")
M = K.M132
L = 8
NT = K.NTAB

# --- the frozen-boundary kernel: 0134's sweeps4 plus a link mask ---
SRC = K.C_SRC.replace(
    "void sweeps4(double* lp,double* lm,",
    "void sweeps4f(const unsigned char* frz,double* lp,double* lm,"
).replace(
    "        for(int s=0; s<V; s++){",
    "        for(int s=0; s<V; s++){\n"
    "          if(frz[(long)(mu*V)+s]) continue;"
)
assert "sweeps4f" in SRC and "if(frz[" in SRC


def build_f():
    h = hashlib.sha1(SRC.encode()).hexdigest()[:12]
    so = os.path.join(HERE, f".k137_{h}.so")
    c = so.replace(".so", ".c")
    if not os.path.exists(so):
        open(c, "w").write(SRC)
        subprocess.run(["cc", "-O3", "-march=native", "-ffast-math",
                        "-shared", "-fPIC", c, "-o", so, "-lm"],
                       check=True)
    lib = ctypes.CDLL(so)
    dp = np.ctypeslib.ndpointer(np.float64, flags="C_CONTIGUOUS")
    ip = np.ctypeslib.ndpointer(np.int32, flags="C_CONTIGUOUS")
    bp = np.ctypeslib.ndpointer(np.uint8, flags="C_CONTIGUOUS")
    up_ = np.ctypeslib.ndpointer(np.uint64, flags="C_CONTIGUOUS")
    lib.sweeps4f.argtypes = [bp, dp, dp, ip, ip, ctypes.c_int,
                             ctypes.c_int, ctypes.c_double, dp,
                             ctypes.c_int, up_,
                             ctypes.POINTER(ctypes.c_long),
                             ctypes.POINTER(ctypes.c_long)]
    lib.sweeps4f.restype = None
    return lib


LIBF = build_f()


def fsweeps(frz, lp, lm, up, dn, V, n, sig, rs):
    a, t = ctypes.c_long(0), ctypes.c_long(0)
    LIBF.sweeps4f(frz, lp, lm, up, dn, V, n, sig, K.TAB, NT, rs,
                  ctypes.byref(a), ctypes.byref(t))
    return a.value, t.value


def mask(L, tset):
    """freeze the SPATIAL links on the given time slices -- that is
    what makes the blocks between them conditionally independent."""
    V = L ** 4
    t = np.arange(V) // (L ** 3)
    f = np.zeros((4, V), np.uint8)
    on = np.isin(t, list(tset))
    for mu in (1, 2, 3):
        f[mu][on] = 1
    return np.ascontiguousarray(f.reshape(-1))


def slice_op(Up, Um, lat, t):
    """the traceless-symmetric (spin-2) site operator, averaged over
    time slice t. 3x3."""
    qp, qm = M.all_plaq(Up, lat), M.all_plaq(Um, lat)
    Bp, Bm = qp[..., 1:], qm[..., 1:]
    o = np.einsum("vpi,vpj->vpij", Bp, Bm)
    tr = np.einsum("vpii->vp", o)
    s0 = 0.5 * (o + np.swapaxes(o, -1, -2)) - (
        tr / 3)[..., None, None] * np.eye(3)
    s0 = s0.mean(1).reshape((L,) * 4 + (3, 3))
    return s0[t].reshape(-1, 3, 3).mean(0)


def therm(seed=911):
    lat, up, dn = K.lat_arrays(L)
    V = lat["V"]
    lp, lm = K.fresh(L)
    rs = K.seed(seed)
    sig = 0.08
    for s in range(700):
        a, t = K.csweeps(lp, lm, up, dn, V, 1, sig, rs)
        if s < 400:
            r = a / max(t, 1)
            sig *= 1.06 if r > 0.45 else (0.94 if r < 0.35 else 1)
            sig = float(np.clip(sig, 0.005, 1.0))
    return lat, up, dn, V, lp, lm, rs, sig


def s1_gate(lat, up, dn, V, lp, lm, rs, sig):
    print("== s1: the frozen kernel, and its gate ==")
    frz = mask(L, {0, 2, 4, 6})
    a, b = lp.copy(), lm.copy()
    fsweeps(frz, a, b, up, dn, V, 8, sig, K.seed(5))
    f4 = frz.reshape(4, V).astype(bool)
    moved_f = np.abs(a.reshape(4, V, 4)[f4]
                     - lp.reshape(4, V, 4)[f4]).max()
    moved_u = np.abs(a.reshape(4, V, 4)[~f4]
                     - lp.reshape(4, V, 4)[~f4]).max()
    nfrz = int(frz.sum())
    print(f"  frozen links: {nfrz} of {4 * V} "
          f"({100 * nfrz / (4 * V):.1f}%) -- spatial links on "
          f"t = 0,2,4,6")
    print(f"  max motion of a FROZEN link over 8 sweeps: "
          f"{moved_f:.2e}   (must be 0)")
    print(f"  max motion of a free link over 8 sweeps:   "
          f"{moved_u:.2e}   (must not be 0)")
    assert moved_f == 0.0, "frozen links moved"
    assert moved_u > 0.1, "free links did not move"
    ar, tt = fsweeps(frz, a, b, up, dn, V, 20, sig, K.seed(7))
    print(f"  acceptance with the boundary frozen: "
          f"{ar / max(tt, 1):.3f}")
    print("  the blocks t=1,3,5,7 now touch only through the frozen")
    print("  slices, so their operators are conditionally "
          "independent")
    print()
    return frz


def s2_budget(lat, up, dn, V, lp, lm, rs, sig, frz, nb=60, nsub=20):
    print("== s2: the variance budget at two granularities ==")
    print("  Var(X) = Var(E[X|Z]) + E[Var(X|Z)].  Rao-Blackwell can")
    print("  only ever remove the second term. So: how big is it?")
    tsl = [1, 3, 5, 7]
    outer, inner = [], []
    for _ in range(nb):
        K.csweeps(lp, lm, up, dn, V, 10, sig, rs)
        sub = []
        a, b = lp.copy(), lm.copy()
        rs2 = K.seed(int(1000 + _ * 7))
        for _s in range(nsub):
            fsweeps(frz, a, b, up, dn, V, 4, sig, rs2)
            Up, Um = K.as_links(a, V), K.as_links(b, V)
            sub.append(np.array([slice_op(Up, Um, lat, t)
                                 for t in tsl]))
        sub = np.array(sub)
        outer.append(sub.mean(0))
        inner.append(sub.var(0))
    outer, inner = np.array(outer), np.array(inner)
    vb = outer.var(0).mean()
    vw = inner.mean(0).mean()
    print(f"  Z = the frozen boundary   "
          f"Var(E[X|Z]) = {vb:.3e}   E[Var(X|Z)] = {vw:.3e}")
    print(f"     removable fraction: {vw / (vb + vw):.3f}")
    print()
    print("  0136 measured the same fraction for Z = 'all links but")
    print("  one': effectively zero -- the reduction came out 0.98x.")
    print(f"  A boundary leaves {100 * vw / (vb + vw):.0f}% on the "
          f"table instead.")
    print()
    return vb, vw


def corr_from(ops, tsl):
    """connected 3x3:3x3 correlator between slice operators."""
    n = len(tsl)
    out = {}
    for i in range(n):
        for j in range(n):
            d = min(abs(tsl[i] - tsl[j]),
                    L - abs(tsl[i] - tsl[j]))
            if d == 0:
                continue
            out.setdefault(d, []).append((i, j))
    return out


def s3_two_level(lat, up, dn, V, lp, lm, rs, sig, frz,
                 nb=120, nsub=16):
    print("== s3: two-level against one-level, matched on cost ==")
    tsl = [1, 3, 5, 7]
    pairs = corr_from(None, tsl)
    two, one = [], []
    t0 = time.time()
    for _ in range(nb):
        K.csweeps(lp, lm, up, dn, V, 10, sig, rs)
        Up, Um = K.as_links(lp, V), K.as_links(lm, V)
        o1 = np.array([slice_op(Up, Um, lat, t) for t in tsl])
        one.append(o1)
        a, b = lp.copy(), lm.copy()
        rs2 = K.seed(int(31 + _ * 13))
        acc = np.zeros((len(tsl), 3, 3))
        for _s in range(nsub):
            fsweeps(frz, a, b, up, dn, V, 4, sig, rs2)
            Ua, Ub = K.as_links(a, V), K.as_links(b, V)
            acc += np.array([slice_op(Ua, Ub, lat, t) for t in tsl])
        two.append(acc / nsub)
    one, two = np.array(one), np.array(two)
    secs = time.time() - t0
    print(f"  L = {L}, {nb} boundary configurations, {nsub} "
          f"sub-averages of 4 sweeps, {secs:.0f}s")
    print()
    print("     d      one-level: mean +- se      two-level: mean "
          "+- se     var ratio   bias")
    ratios = []
    worst = 0.0
    for d in sorted(pairs):
        def series(arr):
            v = []
            for (i, j) in pairs[d]:
                v.append(np.einsum(
                    "nab,nab->n",
                    arr[:, i] - arr[:, i].mean(0),
                    arr[:, j] - arr[:, j].mean(0)))
            return np.mean(v, axis=0)
        p, q = series(one), series(two)
        sp, sq = p.std() / np.sqrt(nb), q.std() / np.sqrt(nb)
        rt = (p.std() / max(q.std(), 1e-300)) ** 2
        ratios.append(rt)
        z = abs(p.mean() - q.mean()) / max(
            np.sqrt(sp ** 2 + sq ** 2), 1e-300)
        worst = max(worst, z)
        print(f"    {d:2d}   {p.mean():+.3e} +- {sp:.1e}    "
              f"{q.mean():+.3e} +- {sq:.1e}   {rt:7.2f}x   "
              f"{z:.1f}s")
    print()
    g = float(np.mean(ratios))
    print(f"  variance reduction: {g:.2f}x on average "
          f"(0136's link-level fix: 0.98x)")
    print(f"  worst bias: {worst:.1f} sigma")
    print()
    cost = 1 + nsub * 4 / 10.0
    print(f"  cost per boundary configuration is ~{cost:.1f}x a "
          f"plain measurement, so the")
    print(f"  cost-matched gain is {g / cost:.2f}x.")
    print()
    if g / cost > 1.5 and worst < 3:
        print("  THE GRANULARITY WAS THE BUG. lucid 0048's fix "
              "works on this operator")
        print("  once Z is a boundary rather than a neighbourhood. "
              "Item 2 re-runs with it.")
    elif g > 1.5:
        print("  Gain before cost, none after. Recorded as "
              "measured: the sub-averaging")
        print("  buys variance but not faster than simply taking "
              "more configurations.")
    else:
        print("  NO GAIN AT EITHER GRANULARITY. Recorded as "
              "measured: the operator's")
        print("  variance is not conditional variance at any Z "
              "tried, and the estimator")
        print("  route to item 2 is closed -- which is itself the "
              "finding.")
    print()
    return g, g / cost, worst


if __name__ == "__main__":
    st = therm()
    frz = s1_gate(*st)
    s2_budget(*st, frz)
    s3_two_level(*st, frz)
    print("all assertions passed")
