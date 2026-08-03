"""
One object, three behaviours: split quaternions and the nilpotent photon.

0006 answered the photon problem by splitting a particle into TWO structures
(a 4-velocity plus an orthogonal spin bivector). That is standard relativistic
spinning-particle theory, it is descriptive rather than explanatory, and it
throws away the single-object framing. Retracted here.

This is the alternative: ONE element of ONE algebra, whose square decides
everything. Split quaternions, basis {1,i,j,k} with i^2 = -1, j^2 = k^2 = +1.

  PART 1  the master identity: for pure v = bi + cj + dk,  v^2 = -Q(v)*1
          with Q(v) = b^2 - c^2 - d^2. One equation, and the whole trichotomy
          of 0004 is the sign of Q.
  PART 2  all three behaviours out of the same exponential
  PART 3  THE POINT. A nilpotent has a NONZERO rotational component but zero
          invariant: spinning in space, nothing in time. That is the photon,
          and it is a boundary case of one object rather than a third
          structure bolted on.
  PART 4  the nilpotent IS the null-rotation generator, and the reason 0004
          found N^3 = 0 in the vector rep while here N^2 = 0
  PART 5  the level spacing 0005 got from a family of planes, recovered from
          the algebra: period 2pi/sqrt(Q) -> infinity as Q -> 0
  PART 6  honest scope -- split quaternions are 2+1 dimensional. The 4D
          version is sl(2,C), where the master identity still holds but a
          FOURTH class appears.

Pure stdlib. Run: python3 0007_split_quaternion_one_object.py
"""

import cmath
import math

PASS = []


def check(name, got, want, atol=1e-12):
    ok = abs(got - want) <= atol
    PASS.append((name, ok, got, want))
    return ok


# ---------------------------------------------------------------- algebra
# q = (a, b, c, d)  <->  a + b i + c j + d k
#   i^2 = -1,  j^2 = k^2 = +1
#   ij = k = -ji,   jk = -i = -kj,   ki = j = -ik

def mul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return (
        a1 * a2 - b1 * b2 + c1 * c2 + d1 * d2,
        a1 * b2 + b1 * a2 - c1 * d2 + d1 * c2,
        a1 * c2 + c1 * a2 + d1 * b2 - b1 * d2,
        a1 * d2 + d1 * a2 + b1 * c2 - c1 * b2,
    )


def add(p, q):
    return tuple(p[i] + q[i] for i in range(4))


def smul(s, q):
    return tuple(s * x for x in q)


def Q(v):
    """The invariant of the pure part: b^2 - c^2 - d^2."""
    return v[1] ** 2 - v[2] ** 2 - v[3] ** 2


def expq(v, theta, terms=200):
    """exp(theta v) by direct series -- no case analysis."""
    acc = (1.0, 0.0, 0.0, 0.0)
    term = (1.0, 0.0, 0.0, 0.0)
    tv = smul(theta, v)
    for n in range(1, terms):
        term = smul(1.0 / n, mul(term, tv))
        acc = add(acc, term)
    return acc


ONE = (1.0, 0.0, 0.0, 0.0)
I = (0.0, 1.0, 0.0, 0.0)
J = (0.0, 0.0, 1.0, 0.0)
K = (0.0, 0.0, 0.0, 1.0)


def main():
    print("=" * 74)
    print("PART 1  --  The master identity")
    print("=" * 74)
    print()
    for lbl, x, want in (("i*i", mul(I, I), -1.0), ("j*j", mul(J, J), 1.0),
                         ("k*k", mul(K, K), 1.0)):
        print(f"    {lbl} = {x}")
        check(f"{lbl} scalar part", x[0], want)
    print(f"    i*j = {mul(I, J)}   (= k)")
    print(f"    j*k = {mul(J, K)}   (= -i)")
    check("ij = k", mul(I, J)[3], 1.0)
    check("jk = -i", mul(J, K)[1], -1.0)
    print()
    print("  Now square a GENERAL pure element v = b i + c j + d k:")
    print()
    hdr = f"{'(b,c,d)':<20}{'v*v':<32}{'-(b^2-c^2-d^2)':>18}"
    print(hdr)
    print("-" * len(hdr))
    for b, c, d in ((1, 0, 0), (0, 1, 0), (1, 1, 0), (2, 1, 1), (0.6, 0.8, 0)):
        v = (0.0, float(b), float(c), float(d))
        vv = mul(v, v)
        print(f"{str((b, c, d)):<20}{str(tuple(round(x, 6) for x in vv)):<32}"
              f"{-Q(v):>18.6f}")
        check(f"v^2 = -Q at {(b, c, d)}", vv[0], -Q(v))
        for comp in (1, 2, 3):
            check(f"v^2 pure part {comp} at {(b, c, d)}", vv[comp], 0.0)
    print()
    print("      v^2  =  -(b^2 - c^2 - d^2) * 1  =  -Q(v) * 1")
    print()
    print("  The square of any pure element is a SCALAR. So one number Q(v)")
    print("  controls everything that element can do. The trichotomy of 0004")
    print("  is not three structures -- it is the sign of Q on one object.")
    print()

    print("=" * 74)
    print("PART 2  --  Three behaviours, one exponential, no case analysis")
    print("=" * 74)
    print()
    print("  exp(theta v) computed by raw series in every row -- the code does")
    print("  not branch on the type. The behaviour comes from Q alone.")
    print()
    hdr = (f"{'(b,c,d)':<16}{'Q':>8}{'type':>12}"
           f"{'exp(1*v) scalar':>18}{'closed form':>18}")
    print(hdr)
    print("-" * len(hdr))
    cases = [
        ((1, 0, 0), "elliptic"),
        ((2, 0, 0), "elliptic"),
        ((0, 1, 0), "hyperbolic"),
        ((1, 2, 0), "hyperbolic"),
        ((1, 1, 0), "NILPOTENT"),
        ((5, 3, 4), "NILPOTENT"),
    ]
    for (b, c, d), lbl in cases:
        v = (0.0, float(b), float(c), float(d))
        q = Q(v)
        e = expq(v, 1.0)
        if q > 1e-12:
            closed = math.cos(math.sqrt(q))
        elif q < -1e-12:
            closed = math.cosh(math.sqrt(-q))
        else:
            closed = 1.0
        print(f"{str((b, c, d)):<16}{q:>8.1f}{lbl:>12}{e[0]:>18.10f}"
              f"{closed:>18.10f}")
        check(f"exp scalar matches closed form {(b, c, d)}", e[0], closed,
              atol=1e-9)
    print()
    print("    Q > 0:  v^2 = -Q  ->  exp = cos(t sqrt Q) + v sin(...)/sqrt Q")
    print("                          PERIODIC, closed orbit, period 2pi/sqrtQ")
    print("    Q < 0:  v^2 = +|Q| ->  exp = cosh + v sinh   OPEN, exponential")
    print("    Q = 0:  v^2 = 0    ->  exp = 1 + theta v EXACTLY, series stops")
    print("                          OPEN, but only LINEAR growth")
    print()
    v = (0.0, 1.0, 1.0, 0.0)
    for th in (1.0, 10.0, 100.0):
        e = expq(v, th)
        print(f"    nilpotent, theta={th:>6.0f}:  exp = "
              f"{tuple(round(x, 6) for x in e)}")
        check(f"nilpotent exp is 1+theta v at {th}", e[1], th, atol=1e-6)
    print()
    print("  The nilpotent is the knife edge: it does not oscillate and it")
    print("  does not blow up. That marginality is the whole resource.")
    print()

    print("=" * 74)
    print("PART 3  --  THE POINT: spinning in space, nothing in time")
    print("=" * 74)
    print()
    print("  Read the components physically. i squares to -1, so the i-part is")
    print("  the genuinely ROTATIONAL content. j and k square to +1, so they")
    print("  are BOOST content -- time-mixing. Then Q = b^2 - c^2 - d^2 is")
    print("  rotation-squared minus boost-squared.")
    print()
    hdr = (f"{'object':<22}{'b (rotation)':>14}{'boost |c,d|':>13}"
           f"{'Q ~ mass^2':>12}{'reading':>22}")
    print(hdr)
    print("-" * len(hdr))
    rows = [
        ("pure rotation  i", (0.0, 1.0, 0.0, 0.0), "massive, spinning"),
        ("pure boost     j", (0.0, 0.0, 1.0, 0.0), "no spin at all"),
        ("nilpotent  i+j", (0.0, 1.0, 1.0, 0.0), "SPIN, NO MASS"),
        ("nilpotent 5i+3j+4k", (0.0, 5.0, 3.0, 4.0), "SPIN, NO MASS"),
        ("near-null 1.01i+j", (0.0, 1.01, 1.0, 0.0), "spin, tiny mass"),
    ]
    for lbl, v, reading in rows:
        boost = math.hypot(v[2], v[3])
        print(f"{lbl:<22}{v[1]:>14.4f}{boost:>13.4f}{Q(v):>12.4f}"
              f"{reading:>22}")
    check("nilpotent has nonzero rotation", (0.0, 1.0, 1.0, 0.0)[1], 1.0)
    check("nilpotent has zero invariant", Q((0.0, 1.0, 1.0, 0.0)), 0.0)
    print()
    print("  Row 3 is the object asked for. The rotational component b is")
    print("  NONZERO -- there is genuine spin -- while Q = 0, so there is no")
    print("  mass and no rest frame. The rotation is exactly balanced against")
    print("  boost content, so it never shows up in the invariant.")
    print()
    print("  'No projected evidence of rotation in time but spinning in space'")
    print("  is precisely b != 0 with b^2 - c^2 - d^2 = 0.")
    print()
    print("  And this is NOT a third structure. It is one element of one")
    print("  algebra sitting on the cone Q = 0. Massive particles are off the")
    print("  cone; photons are on it. The nilpotents ARE the light cone of the")
    print("  algebra: b^2 = c^2 + d^2 is a cone in (b,c,d).")
    print()

    print("=" * 74)
    print("PART 4  --  The nilpotent is the null-rotation generator")
    print("=" * 74)
    print()
    print("  Split quaternions are the 2x2 real matrices. Send")
    print("    i -> [[0,1],[-1,0]]   j -> [[1,0],[0,-1]]   k -> [[0,-1],[-1,0]]")
    print()
    mi = [[0.0, 1.0], [-1.0, 0.0]]
    mj = [[1.0, 0.0], [0.0, -1.0]]

    def m2mul(A, B):
        return [[sum(A[r][t] * B[t][c] for t in range(2)) for c in range(2)]
                for r in range(2)]

    def m2add(A, B):
        return [[A[r][c] + B[r][c] for c in range(2)] for r in range(2)]

    N2 = m2add(mi, mj)
    N2sq = m2mul(N2, N2)
    print(f"    N = i + j  ->  {N2}")
    print(f"    N^2        ->  {N2sq}      (nilpotent, order 2)")
    check("2x2 nilpotent squares to zero",
          max(abs(N2sq[r][c]) for r in range(2) for c in range(2)), 0.0)
    det = N2[0][0] * N2[1][1] - N2[0][1] * N2[1][0]
    tr = N2[0][0] + N2[1][1]
    print(f"    det N = {det:.1f},  tr N = {tr:.1f}")
    check("nilpotent has zero determinant", det, 0.0)
    print()
    print("  0004 built the null-rotation generator in the 4x4 VECTOR rep and")
    print("  found N^3 = 0 (not N^2). Both are right, and the reason is that")
    print("  the vector rep is the symmetric square of this 2x2 one: squaring")
    print("  a rep sends nilpotency order 2 to order 3. Consistency check:")
    print()
    # symmetric square of a 2x2 nilpotent acting on sym^2 (3-dim)
    def sym2(A):
        """Induced DERIVATION of A on Sym^2, basis {e1e1, e1e2, e2e2}.

        With A: e1 -> a e1 + c e2, e2 -> b e1 + d e2, the Leibniz action is
            e1e1 -> 2a e1e1 + 2c e1e2
            e1e2 ->  b e1e1 + (a+d) e1e2 + c e2e2
            e2e2 ->            2b e1e2 + 2d e2e2
        Columns of the matrix are those images.
        """
        a, b = A[0]
        c, d = A[1]
        return [[2 * a, b, 0.0],
                [2 * c, a + d, 2 * b],
                [0.0, c, 2 * d]]

    S = sym2(N2)
    S2 = [[sum(S[r][t] * S[t][c] for t in range(3)) for c in range(3)]
          for r in range(3)]
    S3 = [[sum(S2[r][t] * S[t][c] for t in range(3)) for c in range(3)]
          for r in range(3)]
    m2 = max(abs(S2[r][c]) for r in range(3) for c in range(3))
    m3 = max(abs(S3[r][c]) for r in range(3) for c in range(3))
    print(f"    sym^2(N):  max|N^2| = {m2:.3f} (nonzero), "
          f"max|N^3| = {m3:.2e} (zero)")
    check("sym square has N^3 = 0", m3, 0.0)
    check("sym square has N^2 != 0", 1.0 if m2 > 0.5 else 0.0, 1.0)
    print()
    print("  So 0004's 4x4 result and this 2x2 one are the same object seen")
    print("  in two representations. The 2x2 is the primitive one.")
    print()

    print("=" * 74)
    print("PART 5  --  0005's level spacing, recovered from the algebra")
    print("=" * 74)
    print()
    print("  For Q > 0 the orbit closes with period 2pi/sqrt(Q), so the level")
    print("  spacing goes as sqrt(Q). 0005 got the same collapse by sweeping a")
    print("  family of PLANES; here it is one element approaching the cone.")
    print()
    hdr = f"{'(b,c,d)':<20}{'Q':>12}{'sqrt Q':>12}{'period':>14}"
    print(hdr)
    print("-" * len(hdr))
    for b in (2.0, 1.5, 1.1, 1.01, 1.0001, 1.0):
        v = (0.0, b, 1.0, 0.0)
        q = Q(v)
        if q > 1e-14:
            print(f"{f'({b}, 1, 0)':<20}{q:>12.3e}{math.sqrt(q):>12.3e}"
                  f"{2 * math.pi / math.sqrt(q):>14.4e}")
        else:
            print(f"{f'({b}, 1, 0)':<20}{q:>12.3e}{0.0:>12.3e}"
                  f"{'infinite':>14}")
    print()
    print("  Same result, better reason. Mass ~ sqrt(Q) is the DISTANCE FROM")
    print("  THE NILPOTENT CONE, and masslessness is sitting exactly on it.")
    print("  Apparent continuity near the cone and exact masslessness on it")
    print("  are one phenomenon, not two.")
    print()

    print("=" * 74)
    print("PART 6  --  Honest scope: 2+1 here, and what 4D adds")
    print("=" * 74)
    print()
    print("  Split quaternions have a 3-dimensional pure part with signature")
    print("  (+,-,-). That is 2+1 spacetime, NOT 3+1. So this is the right toy")
    print("  for the mechanism but not yet the real thing.")
    print()
    print("  The 3+1 version is sl(2,C): traceless 2x2 COMPLEX matrices. The")
    print("  master identity survives verbatim by Cayley-Hamilton:")
    print()
    print("      X traceless  =>  X^2 = -det(X) * 1")
    print()
    for lbl, X in (
        ("elliptic  (rotation)", [[1j, 0], [0, -1j]]),
        ("hyperbolic (boost)", [[1.0, 0], [0, -1.0]]),
        ("PARABOLIC (nilpotent)", [[0, 1.0], [0, 0]]),
        ("loxodromic (screw)", [[1 + 1j, 0], [0, -1 - 1j]]),
    ):
        d = X[0][0] * X[1][1] - X[0][1] * X[1][0]
        X2 = [[sum(X[r][t] * X[t][c] for t in range(2)) for c in range(2)]
              for r in range(2)]
        err = max(abs(X2[r][c] + d * (1.0 if r == c else 0.0))
                  for r in range(2) for c in range(2))
        print(f"    {lbl:<24} det = {d:>14.4f}   |X^2 + det*1| = {err:.1e}")
        check(f"Cayley-Hamilton {lbl}", err, 0.0)
    print()
    print("  det X is now COMPLEX, so there are four classes rather than")
    print("  three: det real positive (rotation), real negative (boost), zero")
    print("  (nilpotent -> massless), and genuinely complex (loxodromic -- a")
    print("  simultaneous rotation and boost about one axis, a screw).")
    print()
    print("  That fourth class is new and is worth noticing: it is the")
    print("  generic case, and 'rotating while boosting about the same axis'")
    print("  is what a massive particle WITH spin should look like. The 2+1")
    print("  toy cannot see it. Whether the loxodromic class is where mass and")
    print("  spin coexist in one object -- which is exactly what the")
    print("  two-structure hack in 0006 was avoiding -- is the open question")
    print("  this raises, and it is the right next calculation.")
    print()

    print("=" * 74)
    print("SELF-CHECKS")
    print("=" * 74)
    bad = [p for p in PASS if not p[1]]
    for name, ok, got, want in PASS:
        print(f"  [{'ok' if ok else 'FAIL'}] {name:<48} {got:+.6e}")
    print()
    print(f"  {len(PASS) - len(bad)}/{len(PASS)} checks passed.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
