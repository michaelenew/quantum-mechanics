"""0092 -- the coupling scan: the scale field along the flow.

0101 measured the dressed vacuum at one point: the bare stack
(J = 2.5) at L = 4, finding a Gaussian one-point marginal plus a
weak, short-ranged spatial scale field (s_P-excess ~ 0.012, d = 1
correlation +0.045). Its opens: (1) does the scale field grow toward
strong coupling, tracking the flow? (2) is "short-ranged" a finite-
size artifact of L = 4?

THE COUPLING AXIS IS THE FLOW ITSELF. The derived weight has no
knob; but the RG (0092/0093) acts on the plaquette weight by heat-
kernel smoothing on the group. So the one-parameter family this
program itself generates is

    W_tau = e^{tau Lap} W = sum_j c_j e^{-tau j(j+1)} chi_j ,

with c_j the (integer, fusion-counting) character coefficients of
the bare Born weight W = A^2, A = sum_{j<=2.5} chi_j. tau = 0 is the
bare stack; growing tau walks toward strong coupling (the IR of the
flow), ending at Haar. Positivity is automatic (heat kernel).

COMPILED KERNEL. The sweep is a C kernel embedded below (quaternion
links, sequential-scan Metropolis, lnW by table lookup, xoshiro256**
RNG whose state round-trips through checkpoints), compiled at import
into the checkpoint dir and driven from Python via ctypes. The
Python implementation (0091) stays the correctness reference; the
kernel is gated three ways before any physics:

  g1  bitwise determinism/resume: 20 sweeps in one call == 10 + 10
      with the state saved and restored between calls;
  g2  free theory (flat table) reproduces the Haar class
      distribution;
  g3  the L = 4, tau = 0 run reproduces 0091's Python-reference
      dressed statistics within errors.

SCAN. tau in {0, 0.15, 0.3, 0.6, 1.2} at L = 4 and L = 6 (the flow
question), plus L = 8 at tau in {0, 0.6} (the range question, with
distances out to L/2 = 4). Four chains per run, atomically
checkpointed and resumable in output/mc0092/ exactly as in 0091;
chains of a run execute in parallel threads (the C call releases
the GIL).

DISCOVERED BY g3 ON THE FIRST PASS: at tau = 0 the start matters.
The bare weight W = A^2 has exact zeros (roots of A), and a
hot-started chain lands in a broad branch ~13x wider than 0091's
ordered-start reference and stays there -- local Metropolis
effectively never crosses the zeros' barriers. Any tau > 0 lifts
the zeros. So tau = 0 is run from BOTH starts (plus a 40000-sweep
relaxation chain on the disordered branch), and tau = 0.05/0.15 are
run from both starts to locate where ergodicity is restored and
which branch the tau -> 0+ equilibrium selects.
"""

import ctypes
import hashlib
import json
import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "mc0092")

# ----------------------------------------------------------------------
# the C sweep kernel
# ----------------------------------------------------------------------

C_SRC = r"""
#include <stdint.h>
#include <math.h>

static inline uint64_t rotl(uint64_t x, int k){
    return (x << k) | (x >> (64 - k));
}
static uint64_t xnext(uint64_t* s){
    uint64_t r = rotl(s[1] * 5ULL, 7) * 9ULL;
    uint64_t t = s[1] << 17;
    s[2] ^= s[0]; s[3] ^= s[1]; s[1] ^= s[2]; s[0] ^= s[3];
    s[2] ^= t; s[3] = rotl(s[3], 45);
    return r;
}
static double u01(uint64_t* s){
    return (double)(xnext(s) >> 11) * (1.0 / 9007199254740992.0);
}
static double gauss(uint64_t* s){
    double u = 1.0 - u01(s);
    double v = u01(s);
    return sqrt(-2.0 * log(u)) * cos(6.283185307179586 * v);
}
static inline void qmul(const double* a, const double* b, double* o){
    o[0] = a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3];
    o[1] = a[0]*b[1] + a[1]*b[0] + a[2]*b[3] - a[3]*b[2];
    o[2] = a[0]*b[2] - a[1]*b[3] + a[2]*b[0] + a[3]*b[1];
    o[3] = a[0]*b[3] + a[1]*b[2] - a[2]*b[1] + a[3]*b[0];
}
static inline void qconj(const double* a, double* o){
    o[0] = a[0]; o[1] = -a[1]; o[2] = -a[2]; o[3] = -a[3];
}
static inline double lnw(const double* tab, int ntab, double w){
    if(w > 1.0) w = 1.0;
    if(w < -1.0) w = -1.0;
    double x = acos(w) * (ntab - 1) / 3.14159265358979323846;
    int i = (int)x;
    if(i > ntab - 2) i = ntab - 2;
    double f = x - i;
    return tab[i] * (1.0 - f) + tab[i + 1] * f;
}

/* links[((mu*V)+s)*4 + c]; up/dn[mu*V + s] neighbor tables */
void sweeps(double* links, const int32_t* up, const int32_t* dn,
            int V, int nsweeps, double sig,
            const double* tab, int ntab,
            uint64_t* rs, long* acc_out, long* tot_out)
{
    long acc = 0, tot = 0;
    for(int sw = 0; sw < nsweeps; sw++){
      for(int mu = 0; mu < 4; mu++){
        for(int s = 0; s < V; s++){
          double* U = links + ((long)(mu * V) + s) * 4;
          double ang = sig * gauss(rs);
          double a0 = gauss(rs), a1 = gauss(rs), a2 = gauss(rs);
          double n = sqrt(a0*a0 + a1*a1 + a2*a2);
          if(n < 1e-12){ a0 = 1; a1 = 0; a2 = 0; n = 1; }
          double c = cos(0.5 * ang), sn = sin(0.5 * ang) / n;
          double rot[4] = {c, sn*a0, sn*a1, sn*a2};
          double P[4]; qmul(rot, U, P);
          double dln = 0.0;
          double t1[4], t2[4], S[4], q[4];
          for(int nu = 0; nu < 4; nu++){
            if(nu == mu) continue;
            /* up plaquette at base s:
               theta = angle(U * S), S = U_nu(s+mu) U_mu(s+nu)^+ U_nu(s)^+ */
            const double* pa = links + ((long)(nu*V) + up[mu*V + s]) * 4;
            const double* pb = links + ((long)(mu*V) + up[nu*V + s]) * 4;
            const double* pc = links + ((long)(nu*V) + s) * 4;
            qconj(pb, t1); qmul(pa, t1, t2);
            qconj(pc, t1); qmul(t2, t1, S);
            qmul(U, S, q);
            double lo = lnw(tab, ntab, q[0]);
            qmul(P, S, q);
            dln += lnw(tab, ntab, q[0]) - lo;
            /* down plaquette at base b = s - nu; our link is the
               conjugated third factor; by cyclic invariance
               theta = angle(U^+ T), T = U_nu(b)^+ U_mu(b) U_nu(b+mu) */
            int b = dn[nu*V + s];
            const double* d1 = links + ((long)(nu*V) + b) * 4;
            const double* d2 = links + ((long)(mu*V) + b) * 4;
            const double* d3 = links + ((long)(nu*V) + up[mu*V + b]) * 4;
            qconj(d1, t1); qmul(t1, d2, t2);
            qmul(t2, d3, S);
            qconj(U, t1); qmul(t1, S, q);
            lo = lnw(tab, ntab, q[0]);
            qconj(P, t1); qmul(t1, S, q);
            dln += lnw(tab, ntab, q[0]) - lo;
          }
          tot++;
          if(log(u01(rs) + 1e-300) < dln){
            U[0] = P[0]; U[1] = P[1]; U[2] = P[2]; U[3] = P[3];
            acc++;
          }
        }
      }
    }
    *acc_out += acc; *tot_out += tot;
}
"""


def build():
    os.makedirs(DIR, exist_ok=True)
    h = hashlib.sha1(C_SRC.encode()).hexdigest()[:12]
    so = os.path.join(DIR, f"kernel_{h}.so")
    if not os.path.exists(so):
        cpath = os.path.join(DIR, f"kernel_{h}.c")
        with open(cpath, "w") as f:
            f.write(C_SRC)
        subprocess.run(["cc", "-O3", "-march=native", "-shared",
                        "-fPIC", "-o", so, cpath, "-lm"], check=True)
    lib = ctypes.CDLL(so)
    dp = np.ctypeslib.ndpointer(np.float64, flags="C_CONTIGUOUS")
    ip = np.ctypeslib.ndpointer(np.int32, flags="C_CONTIGUOUS")
    up = np.ctypeslib.ndpointer(np.uint64, flags="C_CONTIGUOUS")
    lib.sweeps.argtypes = [dp, ip, ip, ctypes.c_int, ctypes.c_int,
                           ctypes.c_double, dp, ctypes.c_int, up,
                           ctypes.POINTER(ctypes.c_long),
                           ctypes.POINTER(ctypes.c_long)]
    lib.sweeps.restype = None
    return lib


LIB = build()


def c_sweeps(links, lat, nsweeps, sig, tab, rs):
    acc = ctypes.c_long(0)
    tot = ctypes.c_long(0)
    LIB.sweeps(links, lat["up"], lat["dn"], lat["V"], nsweeps, sig,
               tab, len(tab), rs, ctypes.byref(acc),
               ctypes.byref(tot))
    return acc.value, tot.value


# ----------------------------------------------------------------------
# lattice geometry (parametrized by L)
# ----------------------------------------------------------------------

_LATS = {}


def mklat(L):
    if L in _LATS:
        return _LATS[L]
    V = L ** 4
    coord = np.array([[t, x, y, z] for t in range(L) for x in range(L)
                      for y in range(L) for z in range(L)])
    sites = np.arange(V)

    def shift(s, mu, d=1):
        c = coord[s].copy()
        c[:, mu] = (c[:, mu] + d) % L
        return (c[:, 0] * L ** 3 + c[:, 1] * L ** 2 + c[:, 2] * L
                + c[:, 3])

    sh = {(mu, d): shift(sites, mu, d) for mu in range(4)
          for d in (1, -1)}
    lat = dict(L=L, V=V, sites=sites, shift=shift, sh=sh,
               up=np.ascontiguousarray(
                   np.stack([sh[(mu, 1)] for mu in range(4)])
                   .astype(np.int32)),
               dn=np.ascontiguousarray(
                   np.stack([sh[(mu, -1)] for mu in range(4)])
                   .astype(np.int32)))
    _LATS[L] = lat
    return lat


def qmul_np(a, b):
    w1, x1, y1, z1 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    w2, x2, y2, z2 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
                     w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
                     w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2], axis=-1)


def qinv_np(a):
    b = a.copy()
    b[..., 1:] *= -1
    return b


def all_plaq_thetas(links, lat):
    out = []
    for mu in range(4):
        for nu in range(mu + 1, 4):
            a = links[mu]
            bb = links[nu][lat["sh"][(mu, 1)]]
            c = qinv_np(links[mu][lat["sh"][(nu, 1)]])
            d = qinv_np(links[nu])
            q = qmul_np(qmul_np(a, bb), qmul_np(c, d))
            out.append(np.arccos(np.clip(q[..., 0], -1, 1)))
    return np.stack(out, axis=1)          # (V, 6)


# ----------------------------------------------------------------------
# the flowed weight family W_tau
# ----------------------------------------------------------------------

JS = np.arange(0, 2.6, 0.5)
JMAX = 5.0
NTAB = 16384
_GRID = np.linspace(1e-9, np.pi - 1e-9, 400001)


def chars(th):
    js = np.arange(0, JMAX + 0.1, 0.5)
    return js, np.stack([np.sin((2 * j + 1) * th) / np.sin(th)
                         for j in js])


def char_coeffs():
    js, X = chars(_GRID)
    A = sum(np.sin((2 * j + 1) * _GRID) / np.sin(_GRID) for j in JS)
    W = A ** 2
    haar = (2 / np.pi) * np.sin(_GRID) ** 2
    c = np.array([np.trapezoid(W * X[i] * haar, _GRID)
                  for i in range(len(js))])
    return js, c, W


CJS, CCOEF, WBARE = char_coeffs()


def w_tau(tau):
    """W_tau on _GRID (heat flow of the bare Born weight)."""
    if tau == 0.0:
        return WBARE
    _, X = chars(_GRID)
    lam = CJS * (CJS + 1)
    return np.maximum((CCOEF * np.exp(-tau * lam)) @ X, 1e-15)


def lnw_table(tau):
    th = np.linspace(0, np.pi, NTAB)
    thc = np.clip(th, 1e-9, np.pi - 1e-9)
    if tau == 0.0:
        A = sum(np.sin((2 * j + 1) * thc) / np.sin(thc) for j in JS)
        w = np.maximum(A ** 2, 1e-24)
    else:
        _, X = chars(thc)
        lam = CJS * (CJS + 1)
        w = np.maximum((CCOEF * np.exp(-tau * lam)) @ X, 1e-15)
    return np.ascontiguousarray(np.log(w))


def bare_stats(tau):
    p = w_tau(tau) * np.sin(_GRID) ** 2
    p /= np.trapezoid(p, _GRID)
    m2 = np.trapezoid(p * _GRID ** 2, _GRID)
    m4 = np.trapezoid(p * _GRID ** 4, _GRID)
    lt = np.trapezoid(p * np.log(_GRID), _GRID)
    l2 = np.trapezoid(p * np.log(_GRID) ** 2, _GRID)
    return float(m2), float(9 / 5 * m4 / m2 ** 2), \
        float(np.sqrt(l2 - lt ** 2))


def gauss_control(m2):
    q = np.exp(-_GRID ** 2 / (2 * (m2 / 3))) * _GRID ** 2
    q /= np.trapezoid(q, _GRID)
    lt = np.trapezoid(q * np.log(_GRID), _GRID)
    l2 = np.trapezoid(q * np.log(_GRID) ** 2, _GRID)
    return float(np.sqrt(l2 - lt ** 2))


# ----------------------------------------------------------------------
# gates
# ----------------------------------------------------------------------

def seed_state(seed):
    return np.ascontiguousarray(
        np.random.SeedSequence(seed).generate_state(4, np.uint64))


def gates():
    print("== gates ==")
    # weight machinery: integer fusion coefficients, exact
    # reconstruction at tau = 0, positivity along the flow
    assert np.abs(CCOEF - np.round(CCOEF)).max() < 1e-6
    assert abs(CCOEF[0] - 6) < 1e-6
    _, X = chars(_GRID)
    rec = np.abs(CCOEF @ X - WBARE).max()
    assert rec < 1e-5, rec
    for tau in (0.15, 0.3, 0.6, 1.2):
        assert w_tau(tau).min() > 0
    print(f"  weight: c_j integer fusion counts (c_0 = "
          f"{CCOEF[0]:.0f}), tau=0 reconstruction {rec:.1e}, "
          f"W_tau > 0 along the flow")
    lat = mklat(4)
    tab = lnw_table(0.0)
    # g1: bitwise determinism / checkpoint round-trip
    l1 = np.tile([1.0, 0, 0, 0], (4, lat["V"], 1))
    l1 = np.ascontiguousarray(l1)
    rs1 = seed_state(7)
    c_sweeps(l1, lat, 20, 0.5, tab, rs1)
    l2 = np.ascontiguousarray(np.tile([1.0, 0, 0, 0],
                                      (4, lat["V"], 1)))
    rs2 = seed_state(7)
    c_sweeps(l2, lat, 10, 0.5, tab, rs2)
    saved_links, saved_rs = l2.copy(), rs2.copy()
    l2, rs2 = saved_links.copy(), saved_rs.copy()
    c_sweeps(l2, lat, 10, 0.5, tab, rs2)
    assert np.array_equal(l1, l2) and np.array_equal(rs1, rs2)
    print("  g1: 20 sweeps == 10 + (save/restore) + 10, bitwise")
    # g2: free theory (flat table) -> Haar
    lf = np.ascontiguousarray(np.tile([1.0, 0, 0, 0],
                                      (4, lat["V"], 1)))
    rsf = seed_state(11)
    flat = np.zeros(NTAB)
    ths = []
    for it in range(120):
        c_sweeps(lf, lat, 1, 1.2, flat, rsf)
        if it > 40 and it % 4 == 0:
            ths.append(all_plaq_thetas(lf, lat).ravel())
    th = np.concatenate(ths)
    haar = np.sin(_GRID) ** 2
    haar /= np.trapezoid(haar, _GRID)
    m2h = np.trapezoid(haar * _GRID ** 2, _GRID)
    dev = abs(np.mean(th ** 2) / m2h - 1)
    print(f"  g2: free theory <th^2> = {np.mean(th ** 2):.4f} vs "
          f"Haar {m2h:.4f}  ({100 * dev:.1f}%)")
    assert dev < 0.02
    print("  gates passed (g3 = tau=0 match vs 0091 runs after the "
          "scan)\n")


# ----------------------------------------------------------------------
# map: runs and chains (durable, resumable, parallel)
# ----------------------------------------------------------------------

def spec(L, tau, sweeps, burn, start="dis", chains=4, meas_every=5,
         ckpt=200):
    return dict(name=f"L{L}_t{tau:.2f}_{start}", L=L, tau=tau,
                sweeps=sweeps, burn=burn, start=start, chains=chains,
                sig=0.5 + 0.5 * tau, meas_every=meas_every, ckpt=ckpt)


# tau = 0: the bare weight's exact zeros (A has roots) put effectively
# impassable barriers under local Metropolis -- ordered and disordered
# starts do NOT mix (discovered by the g3 gate: the hot-started kernel
# landed in a branch 13x broader than 0091's ordered-start reference).
# So tau = 0 runs both branches (ord = 0091's protocol, dis = hot
# start, with a long relaxation chain), and small tau probes whether
# the flow's smoothing restores ergodicity and which branch the
# tau -> 0+ equilibrium selects.
RUNS = (
    [spec(4, 0.0, 4000, 800, "ord"),
     spec(4, 0.0, 40000, 800, "dis", chains=2, meas_every=20,
          ckpt=1000),
     spec(4, 0.05, 6000, 1500, "ord"), spec(4, 0.05, 6000, 1500),
     spec(4, 0.15, 4000, 800, "ord")]
    + [spec(4, t, 4000, 800) for t in (0.15, 0.3, 0.6, 1.2)]
    + [spec(6, 0.0, 4000, 800, "ord")]
    + [spec(6, t, 4000, 800) for t in (0.15, 0.3, 0.6, 1.2)]
    + [spec(8, 0.0, 3000, 600, "ord"), spec(8, 0.6, 3000, 600)])


def ckpt_path(sp, k):
    return os.path.join(DIR, f"{sp['name']}_c{k}.npz")


def save_chain(sp, k, links, rs, done, thetas):
    tmp = ckpt_path(sp, k) + ".tmp.npz"
    np.savez_compressed(
        tmp, links=links, rs=rs, done=done,
        thetas=np.array(thetas, dtype=np.float16))
    os.replace(tmp, ckpt_path(sp, k))


def load_chain(sp, k):
    d = np.load(ckpt_path(sp, k), allow_pickle=False)
    links = np.ascontiguousarray(d["links"].astype(np.float64))
    rs = np.ascontiguousarray(d["rs"].astype(np.uint64))
    return links, rs, int(d["done"]), list(d["thetas"])


def run_chain(sp, k):
    lat = mklat(sp["L"])
    tab = lnw_table(sp["tau"])
    if os.path.exists(ckpt_path(sp, k)):
        links, rs, done, thetas = load_chain(sp, k)
        if done >= sp["sweeps"]:
            return
    else:
        rs = seed_state(10000 + 100 * RUNS.index(sp) + k)
        links = np.ascontiguousarray(
            np.tile([1.0, 0, 0, 0], (4, lat["V"], 1)))
        if sp["start"] == "dis":
            c_sweeps(links, lat, 20, 1.5, np.zeros(NTAB), rs)
        else:  # ordered start, 0091's protocol
            c_sweeps(links, lat, 5, 1.5, tab, rs)
        done, thetas = 0, []
    while done < sp["sweeps"]:
        acc, tot = c_sweeps(links, lat, sp["meas_every"], sp["sig"],
                            tab, rs)
        done += sp["meas_every"]
        if done > sp["burn"]:
            thetas.append(all_plaq_thetas(links, lat)
                          .astype(np.float16))
        if done % sp["ckpt"] == 0:
            links /= np.linalg.norm(links, axis=-1, keepdims=True)
            save_chain(sp, k, links, rs, done, thetas)
    save_chain(sp, k, links, rs, done, thetas)
    return acc / tot


def run_all():
    print("== map: runs ==")
    for sp in RUNS:
        t0 = time.time()
        with ThreadPoolExecutor(max_workers=4) as ex:
            accs = list(ex.map(lambda k: run_chain(sp, k),
                               range(sp["chains"])))
        accs = [a for a in accs if a is not None]
        word = (f"acc {np.mean(accs):.2f}" if accs
                else "all chains already complete")
        print(f"  {sp['name']}: {sp['chains']} chains x "
              f"{sp['sweeps']} sweeps, {time.time() - t0:.0f}s, "
              f"{word}")
    print()


# ----------------------------------------------------------------------
# reduce
# ----------------------------------------------------------------------

def reduce_run(sp):
    lat = mklat(sp["L"])
    V, L = lat["V"], sp["L"]
    dmax = L // 2
    per = []
    for k in range(sp["chains"]):
        _, _, done, thetas = load_chain(sp, k)
        assert done >= sp["sweeps"], f"{sp['name']} chain {k} " \
            f"incomplete ({done})"
        T = np.array(thetas, dtype=np.float64)      # (nmeas, V, 6)
        th = T.ravel()
        m2 = np.mean(th ** 2)
        kurt = 9 / 5 * np.mean(th ** 4) / m2 ** 2
        sd = np.log(np.clip(th, 1e-6, None)).std()
        lnr = np.log(np.sqrt((T ** 2).mean(axis=2)))
        sP = lnr.std(axis=1).mean()
        rngs = np.random.default_rng(50 + k)
        Ts = T.copy()
        for i in range(len(Ts)):
            flat = Ts[i].ravel()
            rngs.shuffle(flat)
            Ts[i] = flat.reshape(V, 6)
        sPs = np.log(np.sqrt((Ts ** 2).mean(axis=2))) \
            .std(axis=1).mean()
        x = lnr - lnr.mean(axis=1, keepdims=True)
        var = (x ** 2).mean()
        cors = []
        for d in range(1, dmax + 1):
            num = 0.0
            for mu in range(4):
                sh = lat["shift"](lat["sites"], mu, d)
                num += (x * x[:, sh]).mean()
            cors.append(num / 4 / var)
        per.append([m2, kurt, sd, sP, sPs] + cors)
    P = np.array(per)
    mean, se = P.mean(axis=0), P.std(axis=0) / np.sqrt(len(P))
    m2b, kurtb, sdb = bare_stats(sp["tau"])
    return dict(name=sp["name"], L=L, tau=sp["tau"],
                m2b=m2b, kurtb=kurtb, sdb=sdb,
                m2=mean[0], m2_se=se[0], kurt=mean[1],
                kurt_se=se[1], sd=mean[2], sd_se=se[2],
                sdg=gauss_control(mean[0]),
                sP=mean[3], sP_se=se[3], sPsh=mean[4],
                exc=mean[3] - mean[4],
                exc_se=float(np.sqrt(se[3] ** 2 + se[4] ** 2)),
                cors=list(mean[5:]), cors_se=list(se[5:]))


def relax_traj(sp):
    """Windowed <th^2>(sweep) for the long disordered-branch chain."""
    rows = []
    for k in range(sp["chains"]):
        _, _, _, thetas = load_chain(sp, k)
        T = np.array(thetas, dtype=np.float64)
        m2t = (T ** 2).mean(axis=(1, 2))
        n = len(m2t)
        edges = [0, n // 8, n // 4, n // 2, n]
        rows.append([m2t[a:b].mean() for a, b in
                     zip(edges, edges[1:])])
    return np.array(rows).mean(axis=0), \
        [sp["burn"] + e * sp["meas_every"] for e in
         [0, n // 8, n // 4, n // 2, n]]


def reduce_all():
    print("== reduce ==")
    res = {sp["name"]: reduce_run(sp) for sp in RUNS}

    def get(L, tau, start):
        return res[f"L{L}_t{tau:.2f}_{start}"]

    # -- ergodicity at tau = 0 and along the flow --
    print("  -- tau = 0: the two branches (ergodicity broken by the "
          "weight's zeros) --")
    o, d = get(4, 0.0, "ord"), get(4, 0.0, "dis")
    print(f"  ordered start  : <th^2> = {o['m2']:.4f} +- "
          f"{o['m2_se']:.4f}   (0091 Python ref: 0.0968)")
    print(f"  disordered start: <th^2> = {d['m2']:.4f} +- "
          f"{d['m2_se']:.4f}   ({d['m2'] / o['m2']:.0f}x broader, "
          f"stable)")
    tr, edges = relax_traj(next(s for s in RUNS
                                if s["name"] == "L4_t0.00_dis"))
    seg = ", ".join(f"[{a}-{b}]: {v:.3f}" for v, a, b in
                    zip(tr, edges, edges[1:]))
    print(f"  disordered-branch relaxation <th^2> by sweep window: "
          f"{seg}")
    drift = abs(tr[-1] / tr[0] - 1)
    print(f"  drift over 40000 sweeps: {100 * drift:.1f}% -- "
          f"{'METASTABLE (no decay)' if drift < 0.05 else 'decaying'}")
    print("  -- small tau: does the flow's smoothing restore "
          "ergodicity? --")
    for t in (0.05, 0.15):
        a, b = get(4, t, "ord"), get(4, t, "dis")
        gap = abs(a["m2"] - b["m2"])
        agree = gap < 0.05
        print(f"  tau = {t:.2f}: ord {a['m2']:.4f} vs dis "
              f"{b['m2']:.4f}  ({'AGREE' if agree else 'SPLIT'})")
    print()

    # -- the flow scan. Primary branch: ordered start in the
    # hysteresis window (tau <= 0.05, where the disordered branch is
    # stuck), disordered start above it (unique equilibrium) --
    def primary(L, tau):
        return get(L, tau, "ord" if tau <= 0.05 else "dis")

    for L, taus in ((4, (0.0, 0.05, 0.15, 0.3, 0.6, 1.2)),
                    (6, (0.0, 0.15, 0.3, 0.6, 1.2))):
        print(f"  -- the flow scan, L = {L} "
              f"(tau: bare stack -> strong coupling) --")
        print("  tau   bare<th2> dress<th2>  kurt  SD(lnth)/ctl  "
              "sP_exc      c(1)      c(2)")
        for t in taus:
            r = primary(L, t)
            print(f"  {r['tau']:.2f}   {r['m2b']:.3f}     "
                  f"{r['m2']:.4f}   {r['kurt']:5.2f}  "
                  f"{r['sd']:.3f}/{r['sdg']:.3f}  "
                  f"{r['exc']:+.4f}  {r['cors'][0]:+.4f}  "
                  f"{r['cors'][1]:+.4f}")
        print()
    print("  -- the range question, L = 8 --")
    for r in [r for r in res.values() if r["L"] == 8]:
        cs = "  ".join(f"c({dd + 1}) {c:+.4f}+-{s:.4f}"
                       for dd, (c, s) in
                       enumerate(zip(r["cors"], r["cors_se"])))
        print(f"  tau {r['tau']:.2f} ({r['name'][-3:]}): sP_exc "
              f"{r['exc']:+.4f} +- {r['exc_se']:.4f}   {cs}")
    print()

    # g3: the ordered-start tau = 0 run must reproduce 0091's
    # Python-reference dressed statistics (same protocol)
    ref = get(4, 0.0, "ord")
    print(f"  g3: L4 tau=0 ord vs 0091 Python reference: "
          f"<th^2> {ref['m2']:.4f} (ref 0.0968), "
          f"SD(lnth) {ref['sd']:.3f} (ref 0.475), "
          f"c(1) {ref['cors'][0]:+.4f} (ref +0.0453)")
    assert abs(ref["m2"] - 0.0968) < 0.004
    assert abs(ref["sd"] - 0.475) < 0.010
    assert abs(ref["cors"][0] - 0.0453) < 0.010
    # ergodicity restored by tau = 0.15 (both starts agree); still
    # hysteretic at tau = 0.05
    assert abs(get(4, 0.15, "ord")["m2"]
               - get(4, 0.15, "dis")["m2"]) < 0.05
    assert abs(get(4, 0.05, "ord")["m2"]
               - get(4, 0.05, "dis")["m2"]) > 0.1
    # the ordered branch is the one continuous with the unique
    # tau > 0 equilibrium: dressed <th^2> monotone along the primary
    # curve (the flow selects 0091's branch)
    m2s = [primary(4, t)["m2"] for t in
           (0.0, 0.05, 0.15, 0.3, 0.6, 1.2)]
    assert all(x < y for x, y in zip(m2s, m2s[1:]))
    # the flow broadens the bare weight monotonically
    for L, taus in ((4, (0.0, 0.05, 0.15, 0.3, 0.6, 1.2)),
                    (6, (0.0, 0.15, 0.3, 0.6, 1.2))):
        m2bs = [primary(L, t)["m2b"] for t in taus]
        assert all(x < y for x, y in zip(m2bs, m2bs[1:]))
    with open(os.path.join(DIR, "results.json"), "w") as f:
        json.dump(list(res.values()), f, indent=1)
    return res


if __name__ == "__main__":
    gates()
    run_all()
    res = reduce_all()
    print("all gates and assertions passed")
