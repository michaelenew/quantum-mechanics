"""0072 -- the Lorentzian congruence: signature as arithmetic mod 4.

The wall's "Lorentzian lift" open item, taken at its easiest layer: the
kinematic/arithmetic structures of 0061/0062 (star, curvature split,
Einstein criterion) redone with eta = diag(-1,1,1,1) over Z_p. Exact
modular arithmetic throughout; the only floats are the Gauss sums of s4.

  s1  The Lorentzian Hodge star on bivectors satisfies S^2 = -I mod p.
      Its eigenvalues are +-i, so the self-dual / anti-self-dual split
      exists over the BASE field iff -1 is a quadratic residue:
      p == 1 (mod 4). For p == 3 (mod 4) the split requires the
      quadratic extension F_{p^2} = F_p[i] -- the arithmetic form of
      the continuum fact that real Lorentzian 2-forms have no real SD
      split (why Ashtekar variables are complex) -- and the Galois
      (Frobenius) conjugation x -> x^p swaps the two eigenspaces:
      REALITY CONDITIONS ARE FROBENIUS INVARIANCE.
  s2  The Einstein criterion is signature-blind: on the 20-dim Bianchi
      space, ker(M -> [R_op, S]) = ker(M -> traceless Ricci), rank
      9 = 9 = 9 stacked (0062's Euclidean identity, now with eta), at
      p == 1 and p == 3 mod 4 alike. Vacuum (adding s = 0) is rank 10
      and its kernel is the 10-dim Weyl space.
  s3  (in-doc, no computation needed: the frame-integration price
      K(F) = N^4 |ker F| and Pf(F) contain no metric -- the ledger
      never saw the signature.)
  s4  The same congruence sets the PHASE of the amplitude: the
      quadratic Gauss sum is sqrt(p) for p == 1 (mod 4) and
      i*sqrt(p) for p == 3 (mod 4) (Gauss). At p == 1 (mod 4) the
      arithmetic amplitude is already real and positive -- the theory
      is self-Wick-rotated exactly when the SD split is real.

Constraint stack on the level: odd (Born structure, 0065/0074), >= 3
(deconfinement, 0071), and every prime factor == 1 mod 4 (real SD
split, here -- for composite N the congruence on N alone is not
enough: 9 == 1 mod 4 has no sqrt(-1)). Smallest survivor: N = 5.
"""

import cmath
import math
from itertools import permutations


# ----------------------------------------------------------------------
# modular linear algebra
# ----------------------------------------------------------------------

def inv(x, p):
    return pow(x % p, p - 2, p)


def rank_mod(rows, p):
    """Rank of a matrix (list of rows) over F_p by Gaussian elimination."""
    m = [[x % p for x in r] for r in rows]
    rank, col, nrows = 0, 0, len(m)
    ncols = len(m[0]) if m else 0
    while rank < nrows and col < ncols:
        piv = next((r for r in range(rank, nrows) if m[r][col]), None)
        if piv is None:
            col += 1
            continue
        m[rank], m[piv] = m[piv], m[rank]
        iv = inv(m[rank][col], p)
        m[rank] = [(x * iv) % p for x in m[rank]]
        for r in range(nrows):
            if r != rank and m[r][col]:
                f = m[r][col]
                m[r] = [(a - f * b) % p for a, b in zip(m[r], m[rank])]
        rank += 1
        col += 1
    return rank


# ----------------------------------------------------------------------
# bivector kit, Lorentzian signature eta = diag(-1, 1, 1, 1)
# ----------------------------------------------------------------------

PAIRS = [(0, 1), (0, 2), (0, 3), (2, 3), (3, 1), (1, 2)]
ETA = [-1, 1, 1, 1]

_EPS = {}
for perm in permutations(range(4)):
    sgn, lst = 1, list(perm)
    for i in range(4):
        for j in range(i + 1, 4):
            if lst[i] > lst[j]:
                sgn = -sgn
    _EPS[perm] = sgn


def eps(a, b, c, d):
    return _EPS.get((a, b, c, d), 0)


PIDX = {}
for I, (a, b) in enumerate(PAIRS):
    PIDX[(a, b)] = (I, 1)
    PIDX[(b, a)] = (I, -1)


def star_matrix(p):
    """(S v)_I = sum_J S[I][J] v_J with S[I][J] = eps(I,J) eta_c eta_d,
    J = (c,d): the Lorentzian Hodge star on bivector components."""
    S = [[0] * 6 for _ in range(6)]
    for I, (a, b) in enumerate(PAIRS):
        for J, (c, d) in enumerate(PAIRS):
            S[I][J] = (eps(a, b, c, d) * ETA[c] * ETA[d]) % p
    return S


def matmul(A, B, p):
    return [[sum(A[i][k] * B[k][j] for k in range(6)) % p
             for j in range(6)] for i in range(6)]


G = [ETA[a] * ETA[b] for (a, b) in PAIRS]     # bivector metric, diagonal


def bianchi_basis():
    """Basis of the 20-dim Bianchi subspace of symmetric 6x6 M:
    constraint M[0][3] + M[1][4] + M[2][5] = 0 (the eps-pairing traces
    couple exactly the three complementary pairs)."""
    basis = []
    for i in range(6):
        for j in range(i, 6):
            if (i, j) in ((0, 3), (1, 4), (2, 5)):
                continue
            M = [[0] * 6 for _ in range(6)]
            M[i][j] = M[j][i] = 1
            basis.append(M)
    for (i, j), (k, l) in (((0, 3), (1, 4)), ((1, 4), (2, 5))):
        M = [[0] * 6 for _ in range(6)]
        M[i][j] = M[j][i] = 1
        M[k][l] = M[l][k] = -1
        basis.append(M)
    return basis


def riemann4(M, a, b, c, d, p):
    if a == b or c == d:
        return 0
    I, s1 = PIDX[(a, b)]
    J, s2 = PIDX[(c, d)]
    return (s1 * s2 * M[I][J]) % p


def ricci(M, p):
    Ric = [[0] * 4 for _ in range(4)]
    for b in range(4):
        for d in range(4):
            Ric[b][d] = sum(ETA[a] * riemann4(M, a, b, a, d, p)
                            for a in range(4)) % p
    return Ric


def traceless_ricci_flat(M, p):
    Ric = ricci(M, p)
    s = sum(ETA[b] * Ric[b][b] for b in range(4)) % p
    q = (s * inv(4, p)) % p
    out = []
    for b in range(4):
        for d in range(b, 4):
            out.append((Ric[b][d] - (q * ETA[b] if b == d else 0)) % p)
    return out          # 10 entries


def scalar_flat(M, p):
    Ric = ricci(M, p)
    return [sum(ETA[b] * Ric[b][b] for b in range(4)) % p]


def commutator_flat(M, p):
    """[R_op, S] flattened, R_op = G^{-1} M (G diagonal +-1)."""
    S = star_matrix(p)
    R = [[(G[i] * M[i][j]) % p for j in range(6)] for i in range(6)]
    C = [[(x - y) % p for x, y in zip(r1, r2)]
         for r1, r2 in zip(matmul(R, S, p), matmul(S, R, p))]
    return [C[i][j] for i in range(6) for j in range(6)]


# ----------------------------------------------------------------------
# s1 -- the star squares to -1; the split is a congruence
# ----------------------------------------------------------------------

def sqrt_minus_one(p):
    for x in range(1, p):
        if (x * x + 1) % p == 0:
            return x
    return None


def s1_split():
    print("== s1: Lorentzian star and the mod-4 split ==")
    for p in (5, 13, 7, 11):
        S = star_matrix(p)
        S2 = matmul(S, S, p)
        assert all(S2[i][j] == (p - 1 if i == j else 0)
                   for i in range(6) for j in range(6)), "S^2 != -I"
        i_p = sqrt_minus_one(p)
        if p % 4 == 1:
            assert i_p is not None
            # eigenvectors u -+ i S u; count independent ones per sign
            rows_p, rows_m = [], []
            for k in range(6):
                u = [1 if j == k else 0 for j in range(6)]
                Su = [sum(S[i][j] * u[j] for j in range(6)) % p
                      for i in range(6)]
                rows_p.append([(u[i] - i_p * Su[i]) % p for i in range(6)])
                rows_m.append([(u[i] + i_p * Su[i]) % p for i in range(6)])
            rp, rm = rank_mod(rows_p, p), rank_mod(rows_m, p)
            print(f"  p={p:2d} (1 mod 4): i = {i_p} in F_p; "
                  f"SD/ASD split over the base field, dims {rp}+{rm}")
            assert (rp, rm) == (3, 3)
        else:
            assert i_p is None
            print(f"  p={p:2d} (3 mod 4): no sqrt(-1) in F_p -- "
                  f"no real SD split; extend to F_p[i]")

    # Frobenius swaps the eigenspaces over F_{p^2}, p == 3 (mod 4)
    p = 7
    S = star_matrix(p)

    def cmulf(x, y):        # F_{p^2} as pairs (a, b) = a + b i, i^2 = -1
        a, b = x
        c, d = y
        return ((a * c - b * d) % p, (a * d + b * c) % p)

    def frob(x):
        return (x[0], (-x[1]) % p)

    swapped = 0
    for k in range(6):
        u = [(1, 0) if j == k else (0, 0) for j in range(6)]
        Su = [(sum(S[i][j] * u[j][0] for j in range(6)) % p,
               sum(S[i][j] * u[j][1] for j in range(6)) % p)
              for i in range(6)]
        v = [((u[i][0] - (-Su[i][1])) % p, (u[i][1] - Su[i][0]) % p)
             for i in range(6)]                     # u - i S u
        Sv = [(sum(S[i][j] * v[j][0] for j in range(6)) % p,
               sum(S[i][j] * v[j][1] for j in range(6)) % p)
              for i in range(6)]
        assert all(Sv[i] == cmulf((0, 1), v[i]) for i in range(6)), \
            "not an SD eigenvector"
        w = [frob(x) for x in v]
        Sw = [(sum(S[i][j] * w[j][0] for j in range(6)) % p,
               sum(S[i][j] * w[j][1] for j in range(6)) % p)
              for i in range(6)]
        assert all(Sw[i] == cmulf((0, p - 1), w[i]) for i in range(6)), \
            "Frobenius image not ASD"
        swapped += 1
    print(f"  p=7 over F_49: S v = i v  ==>  S v^Frob = -i v^Frob for "
          f"{swapped}/6 constructions -- reality conditions are "
          f"Frobenius invariance\n")


# ----------------------------------------------------------------------
# s2 -- the Einstein criterion is signature-blind
# ----------------------------------------------------------------------

def s2_einstein():
    print("== s2: Einstein criterion with eta, kernel identity ==")
    basis = bianchi_basis()
    assert len(basis) == 20
    for p in (5, 13, 7, 11):
        comm = [commutator_flat(M, p) for M in basis]
        tric = [traceless_ricci_flat(M, p) for M in basis]
        scal = [scalar_flat(M, p) for M in basis]
        rc = rank_mod([list(c) for c in zip(*comm)], p)   # rank via cols
        rt = rank_mod([list(c) for c in zip(*tric)], p)
        rs = rank_mod([list(c) for c in zip(*[c + t for c, t in
                                              zip(comm, tric)])], p)
        rv = rank_mod([list(c) for c in zip(*[c + s for c, s in
                                              zip(comm, scal)])], p)
        print(f"  p={p:2d}: rank[R,*] = {rc}, rank tracelessRic = {rt}, "
              f"stacked = {rs}; vacuum ([R,*]=0 and s=0) rank = {rv}, "
              f"kernel dim = {20 - rv} (Weyl)")
        assert rc == rt == rs == 9, "kernel identity broken"
        assert rv == 10 and 20 - rv == 10, "vacuum kernel is not Weyl"
    print("  identical to the Euclidean ranks of 0062 -- the Einstein "
          "predicate never depended on signature\n")


# ----------------------------------------------------------------------
# s4 -- the Gauss-sum phase obeys the same congruence
# ----------------------------------------------------------------------

def s4_gauss():
    print("== s4: quadratic Gauss sums ==")
    for p in (5, 13, 17, 3, 7, 11):
        g = sum(cmath.exp(2j * math.pi * (k * k % p) / p)
                for k in range(p))
        want = math.sqrt(p) if p % 4 == 1 else 1j * math.sqrt(p)
        assert abs(g - want) < 1e-9, (p, g)
        tag = "sqrt(p)      -- real amplitude" if p % 4 == 1 \
            else "i*sqrt(p)   -- imaginary"
        print(f"  p={p:2d}: g = {g.real:+7.4f}{g.imag:+7.4f}i  =  {tag}")
    print("  the amplitude is real positive exactly on the congruence "
          "class where the SD split is real\n")


if __name__ == "__main__":
    s1_split()
    s2_einstein()
    s4_gauss()
    # for composite N the criterion is NOT "N == 1 mod 4" -- sqrt(-1)
    # exists mod N iff every prime factor is 1 mod 4 (9 == 1 mod 4 yet
    # has no i). Test existence directly:
    ok = [N for N in range(3, 40, 2) if sqrt_minus_one(N) is not None]
    print(f"levels passing odd + >=3 + real-SD (sqrt(-1) exists): "
          f"{ok} ... smallest N = {ok[0]}")
    assert ok == [5, 13, 17, 25, 29, 37] and 9 not in ok and 21 not in ok
    print("all assertions passed")
