"""The weight decomposition: coherence, tangle, and the Bloch budget.

0067 left the local-coherence/tangle split as its open 2, and weight
monogamy as its open 1.  Both close, and they close as one theorem.
For a qubit carrier at node A with pointer generator n.sigma/2 in an
arbitrary pure global state:

  s1  THE BLOCH BUDGET.  For pure two-qubit states, exactly:

        bias^2 + coherence^2 + tangle = 1
        (r.n)^2 + (|r|^2-(r.n)^2) + C^2 = 1

      -- the unit Bloch budget partitions into the DECIDED part (the
      component along the generator), the LOCAL COHERENCE (the
      transverse component), and the TANGLE (1 - |r|^2).  Verified
      to 1e-15 on 200 random states.

  s2  THE DECOMPOSITION THEOREM.  The channel weight is

        w = kappa^2 (1 - (r.n)^2) = kappa^2 (C^2 + coherence^2)

      exactly (8e-16 algebraic; QFI re-derived numerically from
      fidelity to 2e-7).  Equivalently w = kappa^2 Var(pointer): THE
      WEIGHT IS THE CARRIER'S UNDECIDEDNESS about its pointer.  The
      decided part is inert -- a definite record sources nothing.
      Covariance: the TANGLE part is encoding-independent (C^2 does
      not move as the generator direction n rotates) while the local
      part rotates with n and the bias is whatever n leaves decided.
      Poles: the relational family (pure tangle, 0067), |+>|0> (pure
      coherence, 0066), |0>|chi> (pure bias -- zero weight).

  s3  GEOMETRY IS BLIND TO PRIVACY.  Two states with the same w but
      opposite splits -- one all tangle, one all local coherence --
      produce IDENTICAL Bures configuration metrics (numeric
      Hessians equal to ~1e-7).  The deficit cannot distinguish
      private capacity from shared capacity; it charges
      undecidedness, wherever it lives.

  s4  THE LADDER, AND MASS MONOGAMY.  The identity holds verbatim
      for any pure GLOBAL state with tangle read as the node-vs-rest
      bipartite tangle 4 det rho_A = 1 - |r|^2.  For three qubits
      CKW then splits the tangle into pairwise + collective:

        w/kappa^2 = coherence^2 + C_AB^2 + C_AC^2 + tau_3

      with tau_3 >= 0 the three-tangle -- verified on 200 random
      states (0 violations) and at the poles: GHZ (all weight in the
      three-tangle, pairwise-invisible) and W (all pairwise, tau_3 =
      0, CKW saturated).  Consequences: MASS MONOGAMY -- the sum of
      a node's pairwise relational weights is bounded by its total
      weight, which is bounded by kappa^2 (the one-carrier cap); and
      a P1 refinement -- "pairwise" must mean node-vs-rest, because
      GHZ's weight has NO pairwise carrier: collective entanglement
      sources geometry that no pair accounts for.

Run directly for the verification suite.
"""

from __future__ import annotations

import cmath
import math
import random


def rand_state(n, rng):
    v = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(n)]
    nrm = math.sqrt(sum(abs(x) ** 2 for x in v))
    return [x / nrm for x in v]


def bloch_and_C(a):
    """(x, y, z, C) for a pure 2-qubit state a[2i+j] = <ij|psi>."""
    a00, a01, a10, a11 = a
    z = abs(a00) ** 2 + abs(a01) ** 2 - abs(a10) ** 2 - abs(a11) ** 2
    r01 = a00 * a10.conjugate() + a01 * a11.conjugate()
    x, y = 2 * r01.real, -2 * r01.imag
    C = 2 * abs(a00 * a11 - a01 * a10)
    return x, y, z, C


# =====================================================================
# 1. the Bloch budget
# =====================================================================

def verify_budget() -> None:
    rng = random.Random(11)
    worst = 0.0
    for _ in range(200):
        x, y, z, C = bloch_and_C(rand_state(4, rng))
        worst = max(worst, abs(z * z + (x * x + y * y) + C * C - 1))
    print(f"    bias^2 + coherence^2 + tangle = 1: max dev "
          f"{worst:.1e} over 200 random pure states")
    assert worst < 1e-12
    print()
    print("  THE UNIT BLOCH BUDGET PARTITIONS EXACTLY into the decided")
    print("  part, the local coherence, and the tangle.  One budget,")
    print("  three uses.")


# =====================================================================
# 2. the decomposition theorem
# =====================================================================

def verify_decomposition() -> None:
    rng = random.Random(13)
    KAP = 0.9
    w_alg = w_dec = w_num = 0.0
    for _ in range(200):
        a = rand_state(4, rng)
        x, y, z, C = bloch_and_C(a)

        def F(th):
            ph = cmath.exp(-1j * KAP * th / 2)
            b = [a[0] * ph, a[1] * ph,
                 a[2] * ph.conjugate(), a[3] * ph.conjugate()]
            return abs(sum(u.conjugate() * v
                           for u, v in zip(a, b))) ** 2

        h = 1e-4
        qfi = -2 * (F(h) - 2 * F(0) + F(-h)) / (h * h)
        w_num = max(w_num, abs(qfi - KAP ** 2 * (1 - z * z)))
        w_dec = max(w_dec, abs(KAP ** 2 * (1 - z * z)
                               - KAP ** 2 * (C * C + x * x + y * y)))
    print(f"    QFI(fidelity) = k^2(1 - z^2):        max dev "
          f"{w_num:.1e}")
    print(f"    k^2(1 - z^2) = k^2(C^2 + coh^2):     max dev "
          f"{w_dec:.1e}")
    assert w_num < 1e-5 and w_dec < 1e-12
    worst = 0.0
    for _ in range(100):
        a = rand_state(4, rng)
        x, y, z, C = bloch_and_C(a)
        tn = rng.uniform(0, math.pi)
        pn = rng.uniform(0, 2 * math.pi)
        nx, ny, nz = (math.sin(tn) * math.cos(pn),
                      math.sin(tn) * math.sin(pn), math.cos(tn))
        rn = x * nx + y * ny + z * nz
        r2 = x * x + y * y + z * z
        worst = max(worst, abs((1 - rn * rn)
                               - (C * C + (r2 - rn * rn))))
    print(f"    arbitrary generator n: 1-(r.n)^2 = C^2 + (|r|^2 -")
    print(f"    (r.n)^2): max dev {worst:.1e}")
    assert worst < 1e-12
    print("    poles: relational family -> pure tangle (0067);")
    print("    |+>|0> -> pure coherence (0066); |0>|chi> -> pure bias,")
    print("    ZERO weight: a decided record sources nothing")
    print()
    print("  w = kappa^2 (TANGLE + LOCAL COHERENCE), exactly -- and the")
    print("  tangle part is encoding-independent while the coherence")
    print("  part rotates with the generator.  Weight = kappa^2 x the")
    print("  carrier's UNDECIDEDNESS about its pointer.")


# =====================================================================
# 3. geometry is blind to privacy
# =====================================================================

def _bures_hessian(amps, KAP, P0):
    def sep(P):
        return math.hypot(P[1][0] - P[0][0], P[1][1] - P[0][1])

    def fid(dth):
        ph = cmath.exp(-1j * KAP * dth / 2)
        b = [amps[0] * ph, amps[1] * ph,
             amps[2] * ph.conjugate(), amps[3] * ph.conjugate()]
        return abs(sum(u.conjugate() * v
                       for u, v in zip(amps, b))) ** 2

    def d2(P):
        return 2 * (1 - math.sqrt(fid(sep(P) - sep(P0))))

    h = 1e-5
    v0 = [P0[0][0], P0[0][1], P0[1][0], P0[1][1]]
    H = [[0.0] * 4 for _ in range(4)]
    for a in range(4):
        for b in range(4):
            acc = 0.0
            for da, db, sg in ((h, h, 1), (h, -h, -1),
                               (-h, h, -1), (-h, -h, 1)):
                v = v0[:]
                v[a] += da
                v[b] += db
                acc += sg * d2([(v[0], v[1]), (v[2], v[3])])
            H[a][b] = acc / (4 * h * h)
    return H


def verify_blind_to_privacy() -> None:
    KAP = 0.9
    P0 = [(0.0, 0.0), (2.0, 0.5)]
    # state 1: pure tangle, C^2 = 1/2 -> 4pq = 1/2
    p = (1 - math.sqrt(0.5)) / 2
    s_tangle = [math.sqrt(p), 0.0, 0.0, math.sqrt(1 - p)]
    # state 2: pure coherence, product, Bloch (sin45, 0, cos45)
    al = math.pi / 4
    s_coh = [math.cos(al / 2), 0.0, math.sin(al / 2), 0.0]
    x1, y1, z1, C1 = bloch_and_C(s_tangle)
    x2, y2, z2, C2 = bloch_and_C(s_coh)
    w1 = 1 - z1 * z1
    w2 = 1 - z2 * z2
    assert abs(w1 - 0.5) < 1e-12 and abs(w2 - 0.5) < 1e-12
    assert C1 * C1 > 0.49 and C2 < 1e-12
    H1 = _bures_hessian(s_tangle, KAP, P0)
    H2 = _bures_hessian(s_coh, KAP, P0)
    worst = max(abs(H1[a][b] - H2[a][b])
                for a in range(4) for b in range(4))
    print(f"    state 1: w = k^2/2 ALL tangle (C^2 = {C1 * C1:.3f})")
    print(f"    state 2: w = k^2/2 ALL coherence (C = {C2:.1e})")
    print(f"    Bures configuration Hessians: max difference "
          f"{worst:.1e}  (finite-difference floor)")
    assert worst < 5e-6
    print()
    print("  IDENTICAL GEOMETRY.  The deficit cannot distinguish")
    print("  private capacity from shared capacity -- it charges")
    print("  undecidedness wherever it lives.  Only the budget's")
    print("  split (readable by whom?) differs.")


# =====================================================================
# 4. the ladder, and mass monogamy
# =====================================================================

def _matmul4(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4))
             for j in range(4)] for i in range(4)]


_SYY = [[0, 0, 0, -1], [0, 0, 1, 0], [0, 1, 0, 0], [-1, 0, 0, 0]]
_SYY = [[complex(v) for v in row] for row in _SYY]


def _eig4(M):
    """Eigenvalues of a complex 4x4 (char poly + deflation + DK)."""
    A1 = M
    c3 = -sum(A1[i][i] for i in range(4))
    B = [[A1[i][j] + (c3 if i == j else 0) for j in range(4)]
         for i in range(4)]
    A2 = _matmul4(M, B)
    c2 = -sum(A2[i][i] for i in range(4)) / 2
    B = [[A2[i][j] + (c2 if i == j else 0) for j in range(4)]
         for i in range(4)]
    A3 = _matmul4(M, B)
    c1 = -sum(A3[i][i] for i in range(4)) / 3
    B = [[A3[i][j] + (c1 if i == j else 0) for j in range(4)]
         for i in range(4)]
    A4 = _matmul4(M, B)
    c0 = -sum(A4[i][i] for i in range(4)) / 4
    coef = [complex(1), c3, c2, c1, c0]
    scale = max(abs(c) for c in coef)
    roots = []
    # deflate near-zero trailing coefficients (multiple roots at 0)
    while len(coef) > 1 and abs(coef[-1]) < 1e-14 * max(scale, 1.0):
        roots.append(0j)
        coef = coef[:-1]
    deg = len(coef) - 1
    if deg > 0:
        guess = [0.4 * cmath.exp(2j * math.pi * k / deg) + 0.3
                 for k in range(deg)]

        def pv(xv):
            r = 0j
            for c in coef:
                r = r * xv + c
            return r

        for _ in range(400):
            new = []
            for i, ri in enumerate(guess):
                d = 1 + 0j
                for j, rj in enumerate(guess):
                    if i != j:
                        d *= (ri - rj)
                new.append(ri - pv(ri) / d if abs(d) > 1e-300 else ri)
            if max(abs(u - v) for u, v in zip(new, guess)) < 1e-15:
                guess = new
                break
            guess = new
        roots.extend(guess)
    return roots


def conc_mixed(rho):
    rhoc = [[rho[i][j].conjugate() for j in range(4)]
            for i in range(4)]
    rt = _matmul4(_matmul4(_SYY, rhoc), _SYY)
    ev = _eig4(_matmul4(rho, rt))
    lams = sorted((math.sqrt(max(e.real, 0.0)) for e in ev),
                  reverse=True)
    return max(0.0, lams[0] - lams[1] - lams[2] - lams[3])


def _ptrace_C(psi):
    rho = [[0j] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for c in range(2):
                rho[i][j] += psi[2 * i + c] * psi[2 * j + c].conjugate()
    return rho


def _ptrace_B(psi):
    rho = [[0j] * 4 for _ in range(4)]
    for a_ in range(2):
        for c_ in range(2):
            for a2 in range(2):
                for c2 in range(2):
                    v = 0j
                    for b in range(2):
                        v += (psi[4 * a_ + 2 * b + c_]
                              * psi[4 * a2 + 2 * b + c2].conjugate())
                    rho[2 * a_ + c_][2 * a2 + c2] = v
    return rho


def _rhoA(psi):
    r = [[0j] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(4):
                r[i][j] += psi[4 * i + k] * psi[4 * j + k].conjugate()
    return r


def verify_ladder_and_monogamy() -> None:
    rng = random.Random(17)
    a = rand_state(4, rng)
    rho = [[a[i] * a[j].conjugate() for j in range(4)]
           for i in range(4)]
    Cp = 2 * abs(a[0] * a[3] - a[1] * a[2])
    dev = abs(conc_mixed(rho) - Cp)
    print(f"    mixed-Wootters vs pure formula (embedded): dev "
          f"{dev:.1e}")
    assert dev < 1e-6, dev
    s3 = 1 / math.sqrt(3)
    W = [0.0] * 8
    W[1] = W[2] = W[4] = s3
    G = [0.0] * 8
    G[0] = G[7] = 1 / math.sqrt(2)
    assert abs(conc_mixed(_ptrace_C(W)) - 2 / 3) < 1e-6
    assert conc_mixed(_ptrace_C(G)) < 1e-6
    print("    W-state C_AB = 2/3, GHZ C_AB = 0: reproduced")
    viol = 0
    min_tau = 1.0
    for _ in range(200):
        psi = rand_state(8, rng)
        CAB = conc_mixed(_ptrace_C(psi))
        CAC = conc_mixed(_ptrace_B(psi))
        rA = _rhoA(psi)
        detA = (rA[0][0] * rA[1][1] - rA[0][1] * rA[1][0]).real
        z = (rA[0][0] - rA[1][1]).real
        coh2 = 4 * abs(rA[0][1]) ** 2
        w = 1 - z * z
        tau3 = 4 * detA - CAB ** 2 - CAC ** 2
        min_tau = min(min_tau, tau3)
        if (CAB ** 2 + CAC ** 2 > 4 * detA + 1e-7
                or abs(w - (coh2 + 4 * detA)) > 1e-9
                or w > 1 + 1e-12):
            viol += 1
    print(f"    200 random 3-qubit states:")
    print(f"      w/k^2 = coh^2 + 4 det rho_A  (node-vs-rest tangle):")
    print(f"      exact; CKW C_AB^2 + C_AC^2 <= 4 det rho_A:"
          f" {200 - viol}/200; min three-tangle {min_tau:.4f} >= 0")
    assert viol == 0 and min_tau > -1e-7
    for name, psi in (("GHZ", G), ("W  ", W)):
        CAB = conc_mixed(_ptrace_C(psi))
        CAC = conc_mixed(_ptrace_B(psi))
        rA = _rhoA(psi)
        detA = (rA[0][0] * rA[1][1] - rA[0][1] * rA[1][0]).real
        z = (rA[0][0] - rA[1][1]).real
        print(f"      {name}: w/k^2 = {1 - z * z:.4f} = pairwise "
              f"{CAB ** 2 + CAC ** 2:.4f} + three-tangle "
              f"{4 * detA - CAB ** 2 - CAC ** 2:.4f} + coh 0")
    print()
    print("  THE LADDER: w = k^2 (coherence^2 + sum of pairwise")
    print("  tangles + collective tangle), each rung charged equally.")
    print("  MASS MONOGAMY: a node's pairwise relational weights sum")
    print("  to at most its total weight, capped at k^2 -- the")
    print("  per-node sourcing bound.  And GHZ shows collective")
    print("  entanglement sources geometry NO PAIR accounts for: P1's")
    print("  'pairwise' must be read as node-vs-rest.")


def run_verification_suite() -> None:
    sections = [
        ("The Bloch budget", verify_budget),
        ("The decomposition theorem", verify_decomposition),
        ("Geometry is blind to privacy", verify_blind_to_privacy),
        ("The ladder, and mass monogamy",
         verify_ladder_and_monogamy),
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
