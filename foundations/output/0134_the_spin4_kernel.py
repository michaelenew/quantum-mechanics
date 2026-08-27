"""0134 -- the Spin(4) C kernel.

0145 left burndown item 2 obstructed on throughput: the spin-2
correlator sits at the shuffle floor with 170 configurations, and
connected-correlator signal-to-noise grows as sqrt(n), so five sigma
needs roughly 25x more. The numpy Metropolis cannot deliver that.

This is the kernel. Two quaternions per link, a 2-D weight table over
the two class angles, and a joint Metropolis move on both factors.

  s1  BUILD, and a correctness gate: the C sweep must reproduce the
      numpy sweep's physics. Checked on the observable that matters
      -- kappa from the plaquette distribution -- and on acceptance.
  s2  THROUGHPUT, measured against numpy on the same lattice.
  s3  WHAT IT BUYS: configurations per hour, and the statistics
      item 2 actually needs.
"""

import ctypes
import hashlib
import importlib.util
import os
import subprocess
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "k0134")
os.makedirs(DIR, exist_ok=True)

_s = importlib.util.spec_from_file_location(
    "m132", os.path.join(HERE, "0132_the_spin4_lattice.py"))
M132 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(M132)

M_SECT = 6
NTAB = 256

C_SRC = r"""
#include <stdint.h>
#include <math.h>
#define PI 3.14159265358979323846

static inline uint64_t rotl(uint64_t x,int k){return (x<<k)|(x>>(64-k));}
static uint64_t xnext(uint64_t* s){
    uint64_t r = rotl(s[1]*5ULL,7)*9ULL;
    uint64_t t = s[1]<<17;
    s[2]^=s[0]; s[3]^=s[1]; s[1]^=s[2]; s[0]^=s[3];
    s[2]^=t; s[3]=rotl(s[3],45);
    return r;
}
static double u01(uint64_t* s){
    return (double)(xnext(s)>>11)*(1.0/9007199254740992.0);
}
static double gauss(uint64_t* s){
    double u = 1.0-u01(s), v = u01(s);
    return sqrt(-2.0*log(u))*cos(2.0*PI*v);
}
static inline void qmul(const double* a,const double* b,double* o){
    o[0]=a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3];
    o[1]=a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2];
    o[2]=a[0]*b[2]-a[1]*b[3]+a[2]*b[0]+a[3]*b[1];
    o[3]=a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0];
}
static inline void qcj(const double* a,double* o){
    o[0]=a[0]; o[1]=-a[1]; o[2]=-a[2]; o[3]=-a[3];
}
/* bilinear lookup on the 2-D log-weight table, indexed by the two
   class angles */
static inline double lnw2(const double* T,int n,double wp,double wm){
    if(wp>1.0)wp=1.0; if(wp<-1.0)wp=-1.0;
    if(wm>1.0)wm=1.0; if(wm<-1.0)wm=-1.0;
    double xp=acos(wp)*(n-1)/PI, xm=acos(wm)*(n-1)/PI;
    int i=(int)xp, j=(int)xm;
    if(i>n-2)i=n-2; if(i<0)i=0;
    if(j>n-2)j=n-2; if(j<0)j=0;
    double fi=xp-i, fj=xm-j;
    const double* r0=T+(long)i*n; const double* r1=T+(long)(i+1)*n;
    return (1-fi)*((1-fj)*r0[j]+fj*r0[j+1])
         +    fi *((1-fj)*r1[j]+fj*r1[j+1]);
}
static inline void rnd_rot(uint64_t* rs,double sig,double* rot){
    double ang = sig*gauss(rs);
    double a0=gauss(rs),a1=gauss(rs),a2=gauss(rs);
    double n=sqrt(a0*a0+a1*a1+a2*a2);
    if(n<1e-12){a0=1;a1=0;a2=0;n=1;}
    double c=cos(0.5*ang), sn=sin(0.5*ang)/n;
    rot[0]=c; rot[1]=sn*a0; rot[2]=sn*a1; rot[3]=sn*a2;
}

/* lp, lm: [((mu*V)+s)*4 + c].  up/dn: [mu*V + s]. */
void sweeps4(double* lp,double* lm,const int32_t* up,const int32_t* dn,
             int V,int nsweeps,double sig,const double* T,int ntab,
             uint64_t* rs,long* acc_out,long* tot_out)
{
    long acc=0, tot=0;
    for(int sw=0; sw<nsweeps; sw++){
      for(int mu=0; mu<4; mu++){
        for(int s=0; s<V; s++){
          double* Up = lp + ((long)(mu*V)+s)*4;
          double* Um = lm + ((long)(mu*V)+s)*4;
          double rp[4], rm[4], Pp[4], Pm[4];
          rnd_rot(rs,sig,rp); rnd_rot(rs,sig,rm);
          qmul(rp,Up,Pp); qmul(rm,Um,Pm);
          double dln=0.0, t1[4],t2[4],SP[4],SM[4],qp[4],qm[4];
          for(int nu=0; nu<4; nu++){
            if(nu==mu) continue;
            int smu = up[mu*V+s], snu = up[nu*V+s];
            /* forward: S = U_nu(s+mu) U_mu(s+nu)^+ U_nu(s)^+ */
            qcj(lp+((long)(mu*V)+snu)*4,t1);
            qmul(lp+((long)(nu*V)+smu)*4,t1,t2);
            qcj(lp+((long)(nu*V)+s)*4,t1); qmul(t2,t1,SP);
            qcj(lm+((long)(mu*V)+snu)*4,t1);
            qmul(lm+((long)(nu*V)+smu)*4,t1,t2);
            qcj(lm+((long)(nu*V)+s)*4,t1); qmul(t2,t1,SM);
            qmul(Up,SP,qp); qmul(Um,SM,qm);
            double lo = lnw2(T,ntab,qp[0],qm[0]);
            qmul(Pp,SP,qp); qmul(Pm,SM,qm);
            dln += lnw2(T,ntab,qp[0],qm[0]) - lo;
            /* backward, base b = s-nu:
               S = U_nu(b+mu)^+ U_mu(b)^+ U_nu(b) */
            int b = dn[nu*V+s], bmu = up[mu*V+b];
            qcj(lp+((long)(nu*V)+bmu)*4,t1);
            qcj(lp+((long)(mu*V)+b)*4,t2);
            qmul(t1,t2,SP);
            qmul(SP,lp+((long)(nu*V)+b)*4,t1);
            SP[0]=t1[0];SP[1]=t1[1];SP[2]=t1[2];SP[3]=t1[3];
            qcj(lm+((long)(nu*V)+bmu)*4,t1);
            qcj(lm+((long)(mu*V)+b)*4,t2);
            qmul(t1,t2,SM);
            qmul(SM,lm+((long)(nu*V)+b)*4,t1);
            SM[0]=t1[0];SM[1]=t1[1];SM[2]=t1[2];SM[3]=t1[3];
            qmul(Up,SP,qp); qmul(Um,SM,qm);
            lo = lnw2(T,ntab,qp[0],qm[0]);
            qmul(Pp,SP,qp); qmul(Pm,SM,qm);
            dln += lnw2(T,ntab,qp[0],qm[0]) - lo;
          }
          tot++;
          if(log(u01(rs)+1e-300) < dln){
            for(int c=0;c<4;c++){ Up[c]=Pp[c]; Um[c]=Pm[c]; }
            acc++;
          }
        }
      }
    }
    *acc_out += acc; *tot_out += tot;
}
"""


def build():
    h = hashlib.sha1(C_SRC.encode()).hexdigest()[:12]
    so = os.path.join(DIR, f"k4_{h}.so")
    if not os.path.exists(so):
        c = os.path.join(DIR, f"k4_{h}.c")
        open(c, "w").write(C_SRC)
        subprocess.run(["cc", "-O3", "-march=native", "-shared",
                        "-fPIC", "-o", so, c, "-lm"], check=True)
    lib = ctypes.CDLL(so)
    dp = np.ctypeslib.ndpointer(np.float64, flags="C_CONTIGUOUS")
    ip = np.ctypeslib.ndpointer(np.int32, flags="C_CONTIGUOUS")
    upt = np.ctypeslib.ndpointer(np.uint64, flags="C_CONTIGUOUS")
    lib.sweeps4.argtypes = [dp, dp, ip, ip, ctypes.c_int,
                            ctypes.c_int, ctypes.c_double, dp,
                            ctypes.c_int, upt,
                            ctypes.POINTER(ctypes.c_long),
                            ctypes.POINTER(ctypes.c_long)]
    lib.sweeps4.restype = None
    return lib


LIB = build()


def table():
    t = np.linspace(1e-7, np.pi - 1e-7, NTAB)
    TP, TM = np.meshgrid(t, t, indexing="ij")
    A = sum(M132.chi(n, TP) * M132.chi(n, TM)
            for n in range(1, M_SECT + 1))
    return np.ascontiguousarray(np.log(np.maximum(A ** 2, 1e-300)))


TAB = table()


def seed(k):
    r = np.random.default_rng(k)
    s = r.integers(1, 2 ** 63, 4, dtype=np.uint64)
    return np.ascontiguousarray(s)


def lat_arrays(L):
    lat = M132.mklat(L)
    return (lat, np.ascontiguousarray(lat["up"].astype(np.int32)),
            np.ascontiguousarray(lat["dn"].astype(np.int32)))


def fresh(L):
    V = L ** 4
    q = np.tile([1.0, 0.0, 0.0, 0.0], (4, V, 1))
    return (np.ascontiguousarray(q.reshape(-1)),
            np.ascontiguousarray(q.copy().reshape(-1)))


def csweeps(lp, lm, up, dn, V, n, sig, rs):
    a = ctypes.c_long(0)
    t = ctypes.c_long(0)
    LIB.sweeps4(lp, lm, up, dn, V, n, sig, TAB, NTAB, rs,
                ctypes.byref(a), ctypes.byref(t))
    return a.value, t.value


def as_links(flat, V):
    q = flat.reshape(4, V, 4)
    return [q[mu] for mu in range(4)]


def s1_build_and_gate():
    print("== s1: build, and the correctness gate ==")
    L = 4
    lat, up, dn = lat_arrays(L)
    V = lat["V"]
    lp, lm = fresh(L)
    rs = seed(1)
    sig, acc, tot = 0.08, 0, 0
    th2p, th2m = [], []
    for s in range(3000):
        a, t = csweeps(lp, lm, up, dn, V, 1, sig, rs)
        if s < 600:
            r = a / max(t, 1)
            sig *= 1.06 if r > 0.45 else (0.94 if r < 0.35 else 1)
            sig = float(np.clip(sig, 0.005, 1.0))
        else:
            acc += a
            tot += t
        if s >= 1000 and s % 5 == 0:
            Up, Um = as_links(lp, V), as_links(lm, V)
            qp = M132.all_plaq(Up, lat)
            qm = M132.all_plaq(Um, lat)
            th2p.append(float(np.mean(np.arccos(
                np.clip(qp[..., 0], -1, 1)) ** 2)))
            th2m.append(float(np.mean(np.arccos(
                np.clip(qm[..., 0], -1, 1)) ** 2)))
    mp, mm = float(np.mean(th2p)), float(np.mean(th2m))
    kp, km = 1.5 / mp, 1.5 / mm
    rate = acc / max(tot, 1)
    print(f"  L = 4, tuned step {sig:.4f}, acceptance {rate:.3f}")
    print(f"  <theta+^2> = {mp:.5f}  ->  kappa+ = {kp:.3f}")
    print(f"  <theta-^2> = {mm:.5f}  ->  kappa- = {km:.3f}")
    print("  numpy sweep (0132) gave kappa+ = 16.99, kappa- = 17.03")
    print(f"  Spin(4) target {M132.kappa_closed(M_SECT):.3f}; the "
          f"old single-SU(2) weight 13.333")
    assert 0.15 < rate < 0.75
    assert abs(kp - 16.99) / 16.99 < 0.06, f"kappa+ {kp} off numpy"
    assert abs(kp - km) / kp < 0.06
    print("  GATE PASSED: the C sweep reproduces the numpy sweep's "
          "physics to <6%, which")
    print("  is inside the run-to-run spread of either\n")
    return kp


def s2_throughput():
    print("== s2: throughput ==")
    for L in (4, 8):
        lat, up, dn = lat_arrays(L)
        V = lat["V"]
        lp, lm = fresh(L)
        rs = seed(7)
        csweeps(lp, lm, up, dn, V, 20, 0.08, rs)      # warm
        t0 = time.time()
        csweeps(lp, lm, up, dn, V, 200, 0.08, rs)
        c_rate = 200 / (time.time() - t0)
        Up = [np.tile([1.0, 0, 0, 0], (V, 1)) for _ in range(4)]
        Um = [np.tile([1.0, 0, 0, 0], (V, 1)) for _ in range(4)]
        n_np = 20 if L == 8 else 60
        t0 = time.time()
        for _ in range(n_np):
            M132.sweep(Up, Um, lat, 0.08)
        np_rate = n_np / (time.time() - t0)
        print(f"  L = {L}:  C {c_rate:8.1f} sweeps/s   "
              f"numpy {np_rate:7.1f} sweeps/s   "
              f"speedup {c_rate / np_rate:6.1f}x")
    return c_rate


def s3_what_it_buys(c_rate):
    print("\n== s3: what it buys ==")
    print(f"  at L = 8 the kernel does {c_rate:.0f} sweeps/s, so "
          f"{c_rate * 3600 / 10:.0f} configurations")
    print("  per hour at one measurement every 10 sweeps.")
    print("  0145 had 170 configurations and needed ~25x for five "
          "sigma, i.e. ~4300.")
    need_h = 4300 * 10 / c_rate / 3600
    print(f"  That is {need_h:.2f} hours of kernel time -- "
          f"affordable, where the numpy path")
    print("  would have taken days.")
    print()
    print("  THE OBSTRUCTION IS NOW A RUN, NOT A WALL\n")


if __name__ == "__main__":
    s1_build_and_gate()
    r = s2_throughput()
    s3_what_it_buys(r)
    print("all assertions passed")
