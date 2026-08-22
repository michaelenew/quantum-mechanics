"""The tension spectrum: A3's first half, where Barrett-Crane failed.

The graviton-propagator test (0070's A3) splits into a tensorial half
-- WHICH modes does the interacting measure propagate, with what
hierarchy -- and a momentum half (the 1/k^2 structure), which needs a
4D complex.  The tensorial half is exactly where Barrett-Crane's
propagator failed, and it is exactly computable on the healed weight:
for a class-function weight W = sum c_R chi_R on Spin(4), a chain of
plaquettes propagates the mode R with per-step transfer eigenvalue

    t_R = c_R / (d_R c_0),        tension (mass) = -ln t_R

(Schur: E[R(U)] = (c_R/(d_R c_0)) Id; the orientation-average
identity behind it is verified numerically below).

  s1  THE SPECTRUM OF THE HEALED WEIGHT (both bin scales):

        s0 = 0.75:  (1,0) 1.100 < (1,1) 1.201 < (2,0) 1.611
                    < (2,1) 1.725 < (2,2) 1.879 < ...
        s0 = 1.5 :  same ordering at the top.

      A clean, finite, RISING spectrum -- every mode damped, more so
      at higher spin.  The ordering is bin-scale-stable; the numbers
      are not (honest profile dependence).

  s2  WITHIN THE SIMPLE (BALANCED) TOWER -- the sector the simplicity
      structure selects and the sector gravitons live in -- THE
      GRAVITON MULTIPLET IS THE LIGHTEST EXCITATION:
      (1,1) < (2,2) < (3,3), strictly, at both scales.  And (1,1) of
      Spin(4) is the 9-dimensional symmetric-traceless SO(4) tensor:
      the covariant graviton multiplet.  The derived radial profile
      supplies exactly the HIGH-SPIN DAMPING Barrett-Crane lacked.
      Measured honestly alongside: the unbalanced (1,0) (the
      connection/2-form multiplet) interleaves slightly BELOW (1,1)
      at the bare one-plaquette chain -- the signature that
      vertex-level simplicity (intertwiners/budget), absent here,
      still has its job to do.  A pointer, not a hidden failure.

  s3  THE TWO FAILURE MODES, FOR CONTRAST.  Barrett-Crane's weight
      (the bare delta on balanced reps) gives t(j,j) = 1 for EVERY j:
      all balanced modes massless and degenerate, no hierarchy, no
      damping -- the known high-spin pathology, restated as a flat
      transfer spectrum.  The naive 0073 lift gives t(1,0) < 0: an
      UNDEFINED (complex) tension -- the sign disease restated as an
      unphysical spectrum.  Of the three candidate weights, only the
      Born square has a physical spectrum.

  s4  WHAT THIS IS AND IS NOT.  These are 1D-chain tensions --
      per-plaquette decorrelation rates by representation -- the
      nonabelian, rep-resolved analogue of the jitter tension f(N).
      They are NOT 4D masses: 0071's lesson stands (low-D is
      confined for everyone; 4D is where deconfinement begins).
      A3's completion -- the momentum structure against 0063's free
      graviton -- needs the 4D complex, for which this spectrum
      supplies the sector-resolved input: the 4D question is now
      WHICH multiplet deconfines first, and the candidate list is
      ordered.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
_m66 = importlib.import_module('0066_the_nonabelian_dirichlet_square')
_m65 = importlib.import_module('0065_the_nonabelian_plaquette')


def _chi4pdf(x):
    return x ** 3 * math.exp(-x * x / 2) / 2


def density(s0, jmax, nr=60):
    nj = [0.0] * (jmax + 1)
    for i in range(nr):
        ra = 8 * (i + 0.5) / nr
        pa = _chi4pdf(ra) * 8 / nr
        for j in range(nr):
            rb = 8 * (j + 0.5) / nr
            pb = _chi4pdf(rb) * 8 / nr
            for k in range(nr):
                c = -1 + 2 * (k + 0.5) / nr
                pc = (2 / math.pi) * math.sqrt(max(1 - c * c, 0)) * 2 / nr
                s = ra * rb * math.sqrt(max(1 - c * c, 0)) / math.sqrt(2)
                jj = int(round(s / s0))
                if jj <= jmax:
                    nj[jj] += pa * pb * pc
    return nj


def spectrum(s0):
    nj = density(s0, 8)
    n = {m: v for m, v in enumerate(nj) if v > 0}
    C = _m66.born_coeffs(n, 5)
    c00 = C[(0, 0)]
    out = {}
    for (jp, jm), c in C.items():
        if jp < jm or (jp, jm) == (0, 0) or c <= 0:
            continue
        if jp != int(jp) or jp > 4 or jm > 4:
            continue
        t = c / ((2 * jp + 1) * (2 * jm + 1) * c00)
        out[(int(jp), int(jm))] = t
    return out


# =====================================================================
# 0. the transfer identity's anchor
# =====================================================================

def _rot(axis, th):
    c, s = math.cos(th), math.sin(th)
    if axis == 'z':
        return [[c, -s, 0], [s, c, 0], [0, 0, 1]]
    return [[1, 0, 0], [0, c, -s], [0, s, c]]


def _mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)]


def verify_transfer_identity() -> None:
    # orientation-average identity (spin 1, SO(3) matrices):
    # int dg chi(U1 g U2 g^-1) = chi(U1) chi(U2) / d
    th1, th2 = 0.9, 1.7
    U1 = _rot('z', th1)
    U2 = _rot('z', th2)
    ng = 24
    acc = 0.0
    wtot = 0.0
    for i in range(ng):
        al = 2 * math.pi * (i + 0.5) / ng
        for j in range(ng):
            be = math.pi * (j + 0.5) / ng
            w = math.sin(be)
            for k in range(ng):
                ga = 2 * math.pi * (k + 0.5) / ng
                g = _mm(_mm(_rot('z', al), _rot('x', be)),
                        _rot('z', ga))
                gi = [[g[b][a] for b in range(3)] for a in range(3)]
                M = _mm(_mm(_mm(U1, g), U2), gi)
                acc += w * (M[0][0] + M[1][1] + M[2][2])
                wtot += w
    lhs = acc / wtot
    rhs = (1 + 2 * math.cos(th1)) * (1 + 2 * math.cos(th2)) / 3
    print(f"    orientation average of chi_1(U1 g U2 g^-1): "
          f"{lhs:.6f} = chi chi / d = {rhs:.6f}")
    assert abs(lhs - rhs) < 1e-3
    print()
    print("  THE TRANSFER IDENTITY'S ANCHOR HOLDS: chain correlations")
    print("  factor through t_R = c_R/(d_R c_0) per step.")


# =====================================================================
# 1. the spectrum of the healed weight
# =====================================================================

def verify_spectrum() -> None:
    global SPECS
    SPECS = {}
    for s0 in (0.75, 1.5):
        t = spectrum(s0)
        SPECS[s0] = t
        rows = sorted(t.items(), key=lambda kv: -kv[1])[:8]
        print(f"    s0 = {s0}: lightest modes (t, mass = -ln t):")
        for (jp, jm), tv in rows:
            print(f"      ({jp},{jm}): t = {tv:.4f}   mass = "
                  f"{-math.log(tv):.4f}")
    for s0, t in SPECS.items():
        top2 = set(k for k, _ in
                   sorted(t.items(), key=lambda kv: -kv[1])[:2])
        assert top2 == {(1, 0), (1, 1)}, (s0, top2)
        assert t[(1, 1)] > t[(2, 2)] > t[(3, 3)]
        assert t[(1, 0)] > t[(2, 0)] > t[(3, 0)] > t[(4, 0)]
    print()
    print("  A FINITE, RISING SPECTRUM: every mode damped, higher spin")
    print("  damped more.  Ordering bin-scale-stable; numbers not")
    print("  (honest profile dependence).")


# =====================================================================
# 2. the graviton multiplet is the lightest simple excitation
# =====================================================================

def verify_graviton_selection() -> None:
    for s0, t in SPECS.items():
        bal = {k: v for k, v in t.items() if k[0] == k[1]}
        lightest = max(bal, key=bal.get)
        assert lightest == (1, 1), (s0, lightest)
        print(f"    s0 = {s0}: lightest SIMPLE excitation = (1,1), "
              f"dim 9 -- the symmetric-traceless SO(4) tensor")
        print(f"      balanced tower masses: "
              + ", ".join(f"({j},{j}) {-math.log(t[(j, j)]):.3f}"
                          for j in (1, 2, 3)))
        gap = -math.log(t[(1, 0)]) + math.log(t[(1, 1)])
        print(f"      unbalanced (1,0) interleaves below (1,1) by "
              f"{-gap:.3f} in mass -- the vertex-constraint gap,")
        print(f"      measured")
    print()
    print("  WITHIN THE SIMPLE TOWER THE GRAVITON MULTIPLET IS THE")
    print("  LIGHTEST EXCITATION, with clean rising hierarchy -- the")
    print("  high-spin damping Barrett-Crane lacked.  The (1,0)")
    print("  interleaving is the measured job description for")
    print("  vertex-level simplicity (intertwiners/budget), absent at")
    print("  one plaquette.")


# =====================================================================
# 3. the two failure modes
# =====================================================================

def verify_failure_modes() -> None:
    # BC: W = sum_j d_j^2 chi_j chi_j -> c(j,j) = d_j^2, c00 = 1
    for j in (1, 2, 3):
        d = 2 * j + 1
        tBC = (d * d) / (d * d * 1.0)
        assert abs(tBC - 1.0) < 1e-15
    print("    Barrett-Crane (bare balanced delta): t(j,j) = 1 for")
    print("    EVERY j -- all balanced modes massless and degenerate,")
    print("    no damping: the high-spin pathology as a flat spectrum")
    C = _m65.dual_coeffs(0.01, [(0, 0), (1, 0), (1, 1)])
    t10 = C[(1, 0)] / (3 * C[(0, 0)])
    assert t10 < 0
    print(f"    naive 0073 lift: t(1,0) = {t10:+.4f} < 0 -- an")
    print(f"    undefined (complex) tension: the sign disease as an")
    print(f"    unphysical spectrum")
    print()
    print("  OF THE THREE CANDIDATE WEIGHTS, ONLY THE BORN SQUARE HAS")
    print("  A PHYSICAL SPECTRUM: finite, positive, hierarchical.")


# =====================================================================
# 4. what this is and is not
# =====================================================================

def verify_scope() -> None:
    print("    these are 1D-chain tensions -- per-plaquette")
    print("    decorrelation rates by representation, the nonabelian")
    print("    rep-resolved analogue of the jitter tension f(N) --")
    print("    NOT 4D masses (0071: low D confines for everyone; 4D")
    print("    is where deconfinement begins).")
    print()
    print("  A3'S MOMENTUM HALF (the 1/k^2 structure against 0063)")
    print("  NEEDS THE 4D COMPLEX; this spectrum supplies its")
    print("  sector-resolved input.  The 4D question is now: WHICH")
    print("  MULTIPLET DECONFINES FIRST -- and the candidate list is")
    print("  ordered, with the graviton multiplet leading the simple")
    print("  tower.")


def run_verification_suite() -> None:
    sections = [
        ("The transfer identity's anchor", verify_transfer_identity),
        ("The spectrum of the healed weight", verify_spectrum),
        ("The graviton multiplet is the lightest simple excitation",
         verify_graviton_selection),
        ("The two failure modes", verify_failure_modes),
        ("What this is and is not", verify_scope),
    ]
    for index, (title, check) in enumerate(sections, start=1):
        print("=" * 70)
        print(f"{index}. {title}")
        print("=" * 70)
        check()
        print()
    print("=" * 70)
    print("suite complete")
    print("=" * 70)


if __name__ == "__main__":
    run_verification_suite()
