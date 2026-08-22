"""The continuous twist: the graviton counted.

0061/0062 named the move -- the quantum sector must lift from the
finite alphabet Z_N to a CONTINUOUS twist group (continuity, not
non-commutativity, is the operative property).  This module takes the
first exact step: the linearized continuous theory on the lattice,
where everything is rational linear algebra and the four standing
polarization opens (0054/1, 0055/3, 0056/2, 0057/1) close at the
linearized level.  THE COUNT IS 2, AND WHAT THE TWO MODES CARRY IS
PURE WEYL.

  s1  THE MODE COUNT.  Central differences turn every derivative into
      the symbol s_mu = sin k_mu, and the linearized field equations
      become a 10x10 matrix E(s) over the rationals.  Exactly:

        off the shell (eta.s^2 != 0):  ker E = 4   (all pure gauge)
        on  the shell (eta.s^2  = 0):  ker E = 6   -> quotient = 2

      at exact rational shell points (5,3,4,0) and (13,3,4,12).  In
      n = 3 the on-shell kernel is 3 = the gauge subspace: quotient
      0.  Two propagating modes in 3+1, zero in 2+1 -- the
      dimensional trade at the propagating level, in exact
      arithmetic.

  s2  WHAT THE MODES CARRY.  Gauge modes have Riemann == 0
      IDENTICALLY (all components, any s) -- they carry no geometry
      at all.  The two physical modes (TT polarizations h+, hx):
      linearized Ricci = 0 exactly while Riemann has 72 nonzero
      components -- so their curvature is PURE WEYL.  The target
      0061 set ("produce a curvature operator whose Weyl block is
      nonzero") is delivered by the graviton itself.  And the
      curvature operator of each mode commutes with the LORENTZIAN
      Hodge star -- the Einstein criterion, satisfied by the
      graviton in the physical signature.  In n = 3, every on-shell
      solution has Riemann == 0: nothing propagates, exactly.

  s3  THE LORENTZIAN CRITERION, PROVEN.  0061 proved
      [R, star] = 0 <=> traceless Ricci = 0 in Euclidean signature
      (star^2 = +1) over Z_N; its open 3 asked for the Lorentzian
      version.  Here: star^2 = -1 (verified), and over Q on the
      20-dimensional Riemann space the maps M -> [M, star] and
      M -> traceless Ricci have identical kernels (rank 9 = 9 =
      stacked 9), with the vacuum pair (commute AND s = 0) matching
      the full Ricci map (rank 10 = 10 = 10).  0061 open 3 CLOSED.

  s4  THE LATTICE GROUNDING.  The symbol algebra is not an idealized
      continuum statement: applying the literal central-difference
      stencil to a discrete TT wave at a real lattice momentum ON
      the lattice shell sin^2(omega) = sum_i sin^2(k_i) gives
      max|E| = 0.0 to machine precision, and 1.1e-1 off the shell.
      The lattice dispersion is massless (omega -> |k| at small k);
      central differences carry doublers, counted honestly as a
      known artifact.

  s5  THE QUANTUM TIER.  The theory is quadratic, so quantization is
      exact (Gaussian): each of the TWO modes per momentum is a
      harmonic oscillator.  The equal-time zero-point variance on an
      Nt-site time lattice sums to 1/(2 omega sqrt(1 + omega^2/4))
      -- matched to 6 digits -- approaching the continuum 1/(2 omega):
      the graviton's zero-point jitter, the continuous heir of
      0054's |<W>| < 1.  And the compact-U(1) plaquette with the
      heat-kernel weight shows the shape of the continuous-alphabet
      quantum theory: <W> = e^(-1/(2 beta)) exactly -- a jitter
      tension 1/(2 beta) CONTINUOUS in the coupling, where Z_N's was
      the arithmetic sequence f(N) -- while the dual variables in
      the character expansion are INTEGERS: the alphabet is
      continuous, the labels are whole numbers.  Discreteness as
      output, not ingredient.

Run directly for the verification suite.
"""

from __future__ import annotations

import math
from fractions import Fraction as Fr

PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
IDX = {p: i for i, p in enumerate(PAIRS)}
ETA4 = [-1, 1, 1, 1]


def eta(n):
    return [-1] + [1] * (n - 1)


def spairs(n):
    return [(a, b) for a in range(n) for b in range(a, n)]


def riem_sym(s, h, n):
    """Linearized Riemann symbol (central differences, d_mu -> i s_mu):
    R_mnrs = -1/2 (s_n s_r h_ms + s_m s_s h_nr - s_n s_s h_mr
                   - s_m s_r h_ns)."""
    R = [[[[Fr(0)] * n for _ in range(n)] for _ in range(n)]
         for _ in range(n)]
    for m in range(n):
        for nu in range(n):
            for r in range(n):
                for sg in range(n):
                    R[m][nu][r][sg] = -Fr(1, 2) * (
                        s[nu] * s[r] * h[m][sg] + s[m] * s[sg] * h[nu][r]
                        - s[nu] * s[sg] * h[m][r] - s[m] * s[r] * h[nu][sg])
    return R


def ricci_of(R, n):
    E = eta(n)
    return [[sum(Fr(E[m]) * R[m][nu][m][sg] for m in range(n))
             for sg in range(n)] for nu in range(n)]


def einstein_of(h, s, n):
    R = riem_sym(s, h, n)
    Ric = ricci_of(R, n)
    E = eta(n)
    scal = sum(Fr(E[a]) * Ric[a][a] for a in range(n))
    return [[Ric[a][b] - Fr(1, 2) * Fr(E[a] if a == b else 0) * scal
             for b in range(n)] for a in range(n)]


def basis_h(n):
    out = []
    for (a, b) in spairs(n):
        h = [[Fr(0)] * n for _ in range(n)]
        h[a][b] = Fr(1)
        h[b][a] = Fr(1)
        out.append(h)
    return out


def rankQ(rows):
    A = [r[:] for r in rows]
    rk = 0
    cols = len(A[0]) if A else 0
    for c in range(cols):
        piv = None
        for i in range(rk, len(A)):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[rk], A[piv] = A[piv], A[rk]
        inv = 1 / A[rk][c]
        A[rk] = [x * inv for x in A[rk]]
        for i in range(len(A)):
            if i != rk and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][k] - f * A[rk][k] for k in range(cols)]
        rk += 1
    return rk


def Ematrix(s, n):
    P = spairs(n)
    return [[einstein_of(h, s, n)[a][b] for (a, b) in P]
            for h in basis_h(n)]


def kernel_dim(s, n):
    return len(spairs(n)) - rankQ(Ematrix(s, n))


def gauge_basis(s, n):
    out = []
    for mu in range(n):
        h = [[Fr(0)] * n for _ in range(n)]
        for a in range(n):
            h[a][mu] += s[a]
            h[mu][a] += s[a]
        out.append(h)
    return out


def null_space(rows):
    """Kernel of the map c -> sum_i c_i row_i (coefficients over Q)."""
    m = len(rows)
    cols = len(rows[0])
    AT = [[rows[i][j] for i in range(m)] for j in range(cols)]
    piv_cols = []
    rk = 0
    for c in range(m):
        piv = None
        for i in range(rk, len(AT)):
            if AT[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        AT[rk], AT[piv] = AT[piv], AT[rk]
        inv = 1 / AT[rk][c]
        AT[rk] = [x * inv for x in AT[rk]]
        for i in range(len(AT)):
            if i != rk and AT[i][c] != 0:
                f = AT[i][c]
                AT[i] = [AT[i][k] - f * AT[rk][k] for k in range(m)]
        piv_cols.append(c)
        rk += 1
    free = [c for c in range(m) if c not in piv_cols]
    out = []
    for fc in free:
        vec = [Fr(0)] * m
        vec[fc] = Fr(1)
        for r, pc in enumerate(piv_cols):
            vec[pc] = -AT[r][fc]
        out.append(vec)
    return out


# =====================================================================
# 1. the mode count
# =====================================================================

def verify_mode_count() -> None:
    print("    off the shell (eta.s^2 != 0):")
    for s in ([Fr(1), Fr(2), Fr(3), Fr(5)], [Fr(1), Fr(1), Fr(1), Fr(1)],
              [Fr(2), Fr(1), Fr(0), Fr(0)]):
        k = kernel_dim(s, 4)
        s2 = -s[0] ** 2 + sum(x * x for x in s[1:])
        print(f"      s = {tuple(map(str, s))}, s^2 = {s2}: ker = {k}")
        assert k == 4, k
    print("    on the shell (eta.s^2 = 0):")
    for s in ([Fr(5), Fr(3), Fr(4), Fr(0)],
              [Fr(13), Fr(3), Fr(4), Fr(12)]):
        k = kernel_dim(s, 4)
        g = rankQ([[gb[a][b] for (a, b) in spairs(4)]
                   for gb in gauge_basis(s, 4)])
        print(f"      s = {tuple(map(str, s))}: ker = {k}, gauge = {g},"
              f" physical = {k - g}")
        assert k == 6 and g == 4
    s3 = [Fr(5), Fr(3), Fr(4)]
    k3 = kernel_dim(s3, 3)
    g3 = rankQ([[gb[a][b] for (a, b) in spairs(3)]
                for gb in gauge_basis(s3, 3)])
    print(f"    n = 3 on-shell: ker = {k3}, gauge = {g3}, "
          f"physical = {k3 - g3}")
    assert k3 == 3 and g3 == 3
    print()
    print("  TWO PROPAGATING MODES IN 3+1, ZERO IN 2+1 -- exact")
    print("  rational arithmetic, no sampling, no limits.  The")
    print("  dimensional trade (0043) at the propagating level.")


# =====================================================================
# 2. what the modes carry
# =====================================================================

def eps4(i, j, k, l):
    p = [i, j, k, l]
    if len(set(p)) < 4:
        return 0
    sg = 1
    for x in range(4):
        for y in range(x + 1, 4):
            if p[x] > p[y]:
                sg = -sg
    return sg


def star6():
    S = [[Fr(0)] * 6 for _ in range(6)]
    for (a, b) in PAIRS:
        for (c, d) in PAIRS:
            S[IDX[(a, b)]][IDX[(c, d)]] = Fr(
                eps4(a, b, c, d) * ETA4[c] * ETA4[d])
    return S


def mat6(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(6)) for j in range(6)]
            for i in range(6)]


def riem_to_op(R):
    O = [[Fr(0)] * 6 for _ in range(6)]
    for (a, b) in PAIRS:
        for (c, d) in PAIRS:
            O[IDX[(a, b)]][IDX[(c, d)]] = R[a][b][c][d] * ETA4[c] * ETA4[d]
    return O


def verify_mode_content() -> None:
    s = [Fr(1), Fr(2), Fr(3), Fr(5)]
    for g in gauge_basis(s, 4):
        Rg = riem_sym(s, g, 4)
        assert all(Rg[a][b][c][d] == 0 for a in range(4) for b in range(4)
                   for c in range(4) for d in range(4))
    print("    gauge modes: Riemann == 0 IDENTICALLY (any s) -- they")
    print("    carry no geometry")
    s = [Fr(5), Fr(3), Fr(4), Fr(0)]
    e1 = [Fr(0), Fr(4, 5), Fr(-3, 5), Fr(0)]
    e2 = [Fr(0), Fr(0), Fr(0), Fr(1)]
    hplus = [[e1[a] * e1[b] - e2[a] * e2[b] for b in range(4)]
             for a in range(4)]
    hcross = [[e1[a] * e2[b] + e2[a] * e1[b] for b in range(4)]
              for a in range(4)]
    S = star6()
    for name, h in (("h+", hplus), ("hx", hcross)):
        tr = sum(Fr(ETA4[a]) * h[a][a] for a in range(4))
        trans = [sum(Fr(ETA4[a]) * s[a] * h[a][b] for a in range(4))
                 for b in range(4)]
        assert tr == 0 and all(v == 0 for v in trans)
        Eh = einstein_of(h, s, 4)
        assert all(v == 0 for row in Eh for v in row)
        R = riem_sym(s, h, 4)
        Ric = ricci_of(R, 4)
        assert all(v == 0 for row in Ric for v in row)
        nR = sum(1 for a in range(4) for b in range(4) for c in range(4)
                 for d in range(4) if R[a][b][c][d] != 0)
        assert nR > 0
        O = riem_to_op(R)
        C1, C2 = mat6(O, S), mat6(S, O)
        assert all(C1[i][j] == C2[i][j]
                   for i in range(6) for j in range(6))
        print(f"    {name}: E = 0, Ricci = 0, Riemann has {nR} nonzero")
        print(f"        components -> curvature PURE WEYL; and")
        print(f"        [R, star] = 0 in LORENTZIAN signature")
    s3 = [Fr(5), Fr(3), Fr(4)]
    B3 = basis_h(3)
    for vec in null_space(Ematrix(s3, 3)):
        h = [[sum(vec[i] * B3[i][a][b] for i in range(len(B3)))
              for b in range(3)] for a in range(3)]
        R = riem_sym(s3, h, 3)
        assert all(R[a][b][c][d] == 0 for a in range(3) for b in range(3)
                   for c in range(3) for d in range(3))
    print("    n = 3: EVERY on-shell solution has Riemann == 0 --")
    print("    nothing propagates, exactly")
    print()
    print("  THE TWO MODES CARRY PURE WEYL -- 0061's target ('a")
    print("  curvature operator whose Weyl block is nonzero') is")
    print("  delivered by the graviton itself, and its curvature")
    print("  satisfies the Einstein criterion in physical signature.")


# =====================================================================
# 3. the Lorentzian criterion, proven
# =====================================================================

def basis20():
    out = []
    for a in range(6):
        for b in range(a, 6):
            M = [[Fr(0)] * 6 for _ in range(6)]
            M[a][b] = Fr(1)
            M[b][a] = Fr(1)
            out.append(M)
    bia = lambda M: M[0][5] - M[1][4] + M[2][3]
    keep = [M for M in out if bia(M) == 0]
    viol = [M for M in out if bia(M) != 0]
    base = viol[0]
    for M in viol[1:]:
        c = bia(M) / bia(base)
        keep.append([[M[i][j] - c * base[i][j] for j in range(6)]
                     for i in range(6)])
    return keep


def comp20(M, I, J, K, L):
    if I == J or K == L:
        return Fr(0)
    sg = 1
    if I > J:
        I, J, sg = J, I, -sg
    if K > L:
        K, L, sg = L, K, -sg
    return sg * M[IDX[(I, J)]][IDX[(K, L)]]


def ric_eta(M):
    return [[sum(Fr(ETA4[I]) * comp20(M, I, J, I, L) for I in range(4))
             for L in range(4)] for J in range(4)]


def verify_lorentzian_criterion() -> None:
    S = star6()
    S2 = mat6(S, S)
    assert all(S2[i][j] == (-1 if i == j else 0)
               for i in range(6) for j in range(6))
    print("    Lorentzian star: star^2 = -Id  (verified)")
    B = basis20()
    assert rankQ([[M[i][j] for i in range(6) for j in range(6)]
                  for M in B]) == 20
    rows_c, rows_t, rows_r, rows_s = [], [], [], []
    for M in B:
        O = [[M[i][j] * ETA4[PAIRS[j][0]] * ETA4[PAIRS[j][1]]
              for j in range(6)] for i in range(6)]
        C1, C2 = mat6(O, S), mat6(S, O)
        rows_c.append([C1[i][j] - C2[i][j]
                       for i in range(6) for j in range(6)])
        R = ric_eta(M)
        sc = sum(Fr(ETA4[J]) * R[J][J] for J in range(4))
        rows_t.append([4 * R[a][b] - sc * Fr(ETA4[a] if a == b else 0)
                       for a in range(4) for b in range(4)])
        rows_r.append([R[a][b] for a in range(4) for b in range(4)])
        rows_s.append([sc])
    r1, r2 = rankQ(rows_c), rankQ(rows_t)
    rs = rankQ([rows_c[k] + rows_t[k] for k in range(20)])
    assert r1 == r2 == rs == 9, (r1, r2, rs)
    v1 = rankQ([rows_c[k] + rows_s[k] for k in range(20)])
    v2 = rankQ(rows_r)
    v3 = rankQ([rows_c[k] + rows_s[k] + rows_r[k] for k in range(20)])
    assert v1 == v2 == v3 == 10, (v1, v2, v3)
    print(f"    over Q, 20-dim space: rank[.,star] = {r1} = "
          f"rank(tlRic) = {r2} = stacked {rs}")
    print(f"    vacuum pair: rank {v1} = rank(Ricci) {v2} = stacked {v3}")
    print()
    print("  [R, star] = 0 <=> traceless Ricci = 0 PROVEN over Q in")
    print("  LORENTZIAN signature (star^2 = -1), and the vacuum pair")
    print("  matches the full Ricci map.  0061 open 3 CLOSED.")


# =====================================================================
# 4. the lattice grounding
# =====================================================================

def _stencil_einstein(eps, w, kx, x):
    def f(y):
        return math.cos(w * y[0] - kx * y[1])

    def D2(mu, nu, a, b):
        c = eps[a][b]
        if c == 0.0:
            return 0.0
        if mu == nu:
            xp, xm = list(x), list(x)
            xp[mu] += 2
            xm[mu] -= 2
            return c * (f(xp) - 2 * f(x) + f(xm)) / 4.0
        xpp, xpm, xmp, xmm = list(x), list(x), list(x), list(x)
        xpp[mu] += 1; xpp[nu] += 1
        xpm[mu] += 1; xpm[nu] -= 1
        xmp[mu] -= 1; xmp[nu] += 1
        xmm[mu] -= 1; xmm[nu] -= 1
        return c * (f(xpp) - f(xpm) - f(xmp) + f(xmm)) / 4.0

    R4 = [[[[0.0] * 4 for _ in range(4)] for _ in range(4)]
          for _ in range(4)]
    for m in range(4):
        for nu in range(4):
            for r in range(4):
                for sg in range(4):
                    R4[m][nu][r][sg] = 0.5 * (
                        D2(nu, r, m, sg) + D2(m, sg, nu, r)
                        - D2(nu, sg, m, r) - D2(m, r, nu, sg))
    Ric = [[sum(ETA4[m] * R4[m][a][m][b] for m in range(4))
            for b in range(4)] for a in range(4)]
    sc = sum(ETA4[a] * Ric[a][a] for a in range(4))
    return [[Ric[a][b] - 0.5 * (ETA4[a] if a == b else 0) * sc
             for b in range(4)] for a in range(4)]


def verify_lattice_grounding() -> None:
    kx = math.asin(0.6)
    eps = [[0.0] * 4 for _ in range(4)]
    eps[2][2] = 1.0
    eps[3][3] = -1.0
    x0 = (3, 5, 2, 7)
    on = _stencil_einstein(eps, math.asin(0.6), kx, x0)
    off = _stencil_einstein(eps, 0.9, kx, x0)
    won = max(abs(on[a][b]) for a in range(4) for b in range(4))
    woff = max(abs(off[a][b]) for a in range(4) for b in range(4))
    print(f"    literal central-difference stencil, TT wave, real")
    print(f"    lattice momentum:")
    print(f"      ON the lattice shell sin^2 w = sum sin^2 k:  "
          f"max|E| = {won:.1e}")
    print(f"      OFF the shell (w = 0.9):                     "
          f"max|E| = {woff:.1e}")
    assert won < 1e-12 and woff > 1e-3
    print()
    print("  The symbol algebra IS the lattice operator: the discrete")
    print("  TT wave solves the discrete equations to machine zero on")
    print("  the lattice shell -- whose small-k limit is omega = |k|,")
    print("  a massless graviton.  (Central differences carry doublers")
    print("  at the zone edge -- a known artifact, counted per branch.)")


# =====================================================================
# 5. the quantum tier
# =====================================================================

def verify_quantum_tier() -> None:
    print("    zero-point variance per mode (Nt = 65536):")
    for om in (0.1, 0.5, 1.0):
        Nt = 1 << 16
        g = sum(1.0 / (4 * math.sin(math.pi * m / Nt) ** 2 + om * om)
                for m in range(Nt)) / Nt
        pred = 1.0 / (2 * om * math.sqrt(1 + om * om / 4))
        assert abs(g - pred) < 1e-6, (om, g, pred)
        print(f"      omega = {om}: sum {g:.6f} = "
              f"1/(2w sqrt(1+w^2/4)) {pred:.6f}  [-> 1/(2w) = "
              f"{1 / (2 * om):.4f}]")
    print("    compact U(1) plaquette, heat-kernel weight")
    print("    W(theta) = sum_n exp(-n^2/(2 beta)) e^(i n theta):")
    for beta in (0.5, 1.0, 2.0):
        steps, nmax = 4000, 40
        num = den = 0.0
        for i in range(steps):
            th = 2 * math.pi * (i + 0.5) / steps - math.pi
            W = sum(math.exp(-n * n / (2 * beta)) * math.cos(n * th)
                    for n in range(-nmax, nmax + 1))
            num += W * math.cos(th)
            den += W
        wv = num / den
        pred = math.exp(-1 / (2 * beta))
        assert abs(wv - pred) < 1e-9, (beta, wv, pred)
        print(f"      beta = {beta}: <W> = {wv:.6f} = e^(-1/2beta), "
              f"tension {1 / (2 * beta):.4f}")
    print()
    print("  Quantization is exact (Gaussian): TWO oscillators per")
    print("  momentum, each with zero-point variance -> 1/(2 omega) --")
    print("  the graviton's jitter, the continuous heir of 0054's")
    print("  |<W>| < 1.  And the U(1) plaquette shows the continuous")
    print("  alphabet with INTEGER dual labels: tension continuous in")
    print("  the coupling (1/(2 beta)) where Z_N's was the arithmetic")
    print("  f(N); discreteness as OUTPUT, not ingredient.")


def run_verification_suite() -> None:
    sections = [
        ("The mode count", verify_mode_count),
        ("What the modes carry", verify_mode_content),
        ("The Lorentzian criterion, proven",
         verify_lorentzian_criterion),
        ("The lattice grounding", verify_lattice_grounding),
        ("The quantum tier", verify_quantum_tier),
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
