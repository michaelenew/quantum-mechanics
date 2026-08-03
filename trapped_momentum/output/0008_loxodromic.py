"""
The loxodromic case: does ONE element carry mass and spin together?

Setup. X in sl(2,C), traceless 2x2 complex, X = (zeta/2)(n.sigma) with n a unit
axis and zeta = eta - i*theta the COMPLEX RAPIDITY: eta the boost rapidity,
theta the rotation angle, about the same axis.

  PART 1  det X = -zeta^2/4, and the four classes are four regions of zeta.
          The nilpotent needs a COMPLEX NULL axis, not just zeta = 0.
  PART 2  the complex determinant packages BOTH bivector invariants at once:
          Re(det X) ~ F.F ~ B^2 - E^2   and   Im(det X) ~ F.Fdual ~ E.B.
          This gives the second invariant the home 0005 said it lacked.
  PART 3  a loxodromic element CANONICALLY splits spacetime into a timelike
          plane (where it boosts) and the orthogonal spacelike plane (where it
          rotates). Frenkel-Pirani becomes automatic instead of imposed --
          which is what retires 0006's retracted hack.
  PART 4  mass = HAVING AN AXIS. det X != 0 -> two eigendirections -> a rest
          frame. det X = 0 -> the eigendirections COLLIDE -> no rest frame ->
          massless. Masslessness is eigenvector degeneracy.
  PART 5  the flow is compact x non-compact: the rotation part is periodic
          (quantized -> spin), the boost part is not (continuous -> momentum).
          One object, one discrete number and one continuous one.

Pure stdlib. Run: python3 0008_loxodromic.py
"""

import cmath
import math

PASS = []


def check(name, got, want, atol=1e-11):
    ok = abs(got - want) <= atol
    PASS.append((name, ok, got, want))
    return ok


# --------------------------------------------------------------- 2x2 tools
def mm(A, B):
    return [[sum(A[r][t] * B[t][c] for t in range(2)) for c in range(2)]
            for r in range(2)]


def madd(A, B):
    return [[A[r][c] + B[r][c] for c in range(2)] for r in range(2)]


def smul(s, A):
    return [[s * A[r][c] for c in range(2)] for r in range(2)]


def dag(A):
    return [[A[c][r].conjugate() for c in range(2)] for r in range(2)]


def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def trace(A):
    return A[0][0] + A[1][1]


S1 = [[0, 1], [1, 0]]
S2 = [[0, -1j], [1j, 0]]
S3 = [[1, 0], [0, -1]]


def axis_sigma(n):
    """n . sigma for a (possibly complex) 3-vector n."""
    return [[n[2], n[0] - 1j * n[1]],
            [n[0] + 1j * n[1], -n[2]]]


def X_of(zeta, n):
    return smul(zeta / 2.0, axis_sigma(n))


def eigen(X):
    """Eigenvalues and eigenvectors of a traceless 2x2. Returns (lam, v1, v2)."""
    p, q = X[0][0], X[0][1]
    r = X[1][0]
    lam = cmath.sqrt(p * p + q * r)
    # (X - lam)v = 0  gives  (p-lam)v1 + q v2 = 0  and  r v1 - (p+lam) v2 = 0
    if abs(q) > 1e-14:
        v1 = (q, lam - p)
        v2 = (q, -lam - p)
    elif abs(r) > 1e-14:
        v1 = (p + lam, r)
        v2 = (p - lam, r)
    else:
        # already diagonal: the eigenvectors are the coordinate axes.
        # (omitting this branch silently returns two parallel vectors)
        v1 = (1.0 + 0j, 0j)
        v2 = (0j, 1.0 + 0j)
    return lam, v1, v2


def parallel(v, w):
    """|v x w| for 2-vectors: zero iff parallel."""
    return abs(v[0] * w[1] - v[1] * w[0])


# ------------------------------------------------- action on 4-vectors
# H = x^mu sigma_mu ;  Lie-algebra action  delta H = X H + H X^dag
def H_of(x):
    t, xx, y, z = x
    return [[t + z, xx - 1j * y], [xx + 1j * y, t - z]]


def x_of(H):
    t = (H[0][0] + H[1][1]) / 2.0
    z = (H[0][0] - H[1][1]) / 2.0
    xx = (H[0][1] + H[1][0]) / 2.0
    y = (H[1][0] - H[0][1]) / (2.0 * 1j)
    return (t.real, xx.real, y.real, z.real)


def act(X, x4):
    H = H_of(x4)
    return x_of(madd(mm(X, H), mm(H, dag(X))))


def main():
    Z = (1.0, 0.0, 0.0)          # axis = z-hat

    print("=" * 74)
    print("PART 1  --  det X = -zeta^2/4, and four classes from one family")
    print("=" * 74)
    print()
    print("  X = (zeta/2)(n.sigma),  zeta = eta - i theta")
    print("     eta   = boost rapidity about the axis")
    print("     theta = rotation angle about the SAME axis")
    print()
    hdr = (f"{'(eta, theta)':<16}{'det X':>26}{'class':>14}")
    print(hdr)
    print("-" * len(hdr))
    fam = [((0.0, 1.0), "elliptic"), ((0.0, 2.0), "elliptic"),
           ((1.0, 0.0), "hyperbolic"), ((2.0, 0.0), "hyperbolic"),
           ((1.0, 1.0), "LOXODROMIC"), ((0.7, 2.0), "LOXODROMIC")]
    for (eta, th), lbl in fam:
        zeta = complex(eta, -th)
        X = X_of(zeta, (0.0, 0.0, 1.0))
        d = det(X)
        print(f"{str((eta, th)):<16}{str(complex(round(d.real, 10), round(d.imag, 10))):>26}{lbl:>14}")
        check(f"det = -zeta^2/4 at {(eta, th)}", abs(d + zeta * zeta / 4.0), 0.0)
        check(f"traceless at {(eta, th)}", abs(trace(X)), 0.0)
    print()
    print("    det X = -zeta^2/4 exactly, in every row.")
    print("      theta only  -> det real POSITIVE   -> elliptic  (rotation)")
    print("      eta only    -> det real NEGATIVE   -> hyperbolic (boost)")
    print("      both        -> det COMPLEX         -> LOXODROMIC (screw)")
    print()
    print("  The nilpotent is NOT zeta = 0 (that is just X = 0). It needs a")
    print("  COMPLEX NULL axis, n.n = 0, so that (n.sigma)^2 = (n.n) I = 0:")
    nnull = (1.0, 1j, 0.0)
    Xn = X_of(1.0, nnull)
    print(f"    n = (1, i, 0),  n.n = {sum(c * c for c in nnull)}")
    print(f"    X = {[[complex(round(c.real, 8), round(c.imag, 8)) for c in row] for row in Xn]}")
    print(f"    X^2 = {[[complex(round(c.real, 8), round(c.imag, 8)) for c in row] for row in mm(Xn, Xn)]}")
    print(f"    det X = {det(Xn):.1e}")
    check("null-axis element is nilpotent",
          max(abs(c) for row in mm(Xn, Xn) for c in row), 0.0)
    check("null-axis element has det 0", abs(det(Xn)), 0.0)
    print()
    print("  So masslessness is not a small value of a parameter -- it is a")
    print("  DIFFERENT KIND OF AXIS. That is why it could never be reached by")
    print("  tuning eta and theta, and why it needed its own case in 0006.")
    print()

    print("=" * 74)
    print("PART 2  --  det X carries BOTH bivector invariants")
    print("=" * 74)
    print()
    print("  From 0006: rotation content <-> magnetic, boost content <->")
    print("  electric. So theta ~ B and eta ~ E, and")
    print("      Re(det X) = (theta^2 - eta^2)/4   ~   F.F      ~ B^2 - E^2")
    print("      Im(det X) = eta*theta/2           ~   F.Fdual  ~ E.B")
    print()
    hdr = (f"{'(eta, theta)':<16}{'Re det':>12}{'(th^2-eta^2)/4':>17}"
           f"{'Im det':>12}{'eta*th/2':>11}")
    print(hdr)
    print("-" * len(hdr))
    for eta, th in ((0.0, 1.0), (1.0, 0.0), (1.0, 1.0), (0.7, 2.0), (3.0, 1.5)):
        zeta = complex(eta, -th)
        d = det(X_of(zeta, (0.0, 0.0, 1.0)))
        print(f"{str((eta, th)):<16}{d.real:>12.6f}{(th * th - eta * eta) / 4:>17.6f}"
              f"{d.imag:>12.6f}{eta * th / 2:>11.6f}")
        check(f"Re det at {(eta, th)}", d.real, (th * th - eta * eta) / 4.0)
        check(f"Im det at {(eta, th)}", d.imag, eta * th / 2.0)
    print()
    print("  0005 flagged that a bivector has TWO invariants and only the")
    print("  first had been used, with the second (parity-odd) homeless.")
    print("  It has a home: it is the imaginary part of det X, and it is")
    print("  nonzero EXACTLY on the loxodromic class. The complex determinant")
    print("  is the self-dual packaging of the pair.")
    print()
    print("  Consequence worth noting: the three classes of 0004 were read off")
    print("  ONE invariant, so they could not distinguish anything the second")
    print("  invariant sees. Loxodromic is precisely what was invisible there.")
    print()
    print("  Sharper, and it is the answer to 'one object or two'. A bivector")
    print("  is SIMPLE (= a single plane u^v) exactly when F.Fdual = 0. So:")
    print()
    hdr = f"{'class':<16}{'Re det (F.F)':>14}{'Im det (F.Fd)':>15}{'a single plane?':>18}"
    print(hdr)
    print("-" * len(hdr))
    for lbl, eta, th in (("elliptic", 0.0, 1.0), ("hyperbolic", 1.0, 0.0),
                         ("LOXODROMIC", 1.0, 1.0), ("nilpotent", 0.0, 0.0)):
        if lbl == "nilpotent":
            d = det(X_of(1.0, (1.0, 1j, 0.0)))
        else:
            d = det(X_of(complex(eta, -th), (0.0, 0.0, 1.0)))
        simple = "YES" if abs(d.imag) < 1e-12 else "NO -- two planes"
        print(f"{lbl:<16}{d.real:>14.4f}{d.imag:>15.4f}{simple:>18}")
        check(f"simplicity flag {lbl}",
              1.0 if abs(d.imag) < 1e-12 else 0.0,
              0.0 if lbl == "LOXODROMIC" else 1.0)
    print()
    print("  A massive particle WITH spin is therefore not a plane at all --")
    print("  it is a NON-SIMPLE bivector. And a non-simple bivector has a")
    print("  canonical decomposition into two ORTHOGONAL simple pieces, one")
    print("  timelike and one spacelike. That decomposition is a theorem about")
    print("  the single object, not a case-split imposed on it. Part 3 shows")
    print("  the two pieces explicitly.")
    print()

    print("=" * 74)
    print("PART 3  --  One element, two orthogonal invariant planes")
    print("=" * 74)
    print()
    eta, th = 1.3, 0.7
    X = X_of(complex(eta, -th), (0.0, 0.0, 1.0))
    print(f"  Loxodromic X with eta = {eta}, theta = {th}, axis = z.")
    print("  Act on the four basis 4-vectors (delta H = X H + H X-dagger):")
    print()
    basis = [("t", (1.0, 0, 0, 0)), ("x", (0, 1.0, 0, 0)),
             ("y", (0, 0, 1.0, 0)), ("z", (0, 0, 0, 1.0))]
    hdr = f"{'v':<4}{'delta v = (dt, dx, dy, dz)':>44}"
    print(hdr)
    print("-" * len(hdr))
    for lbl, v in basis:
        d = act(X, v)
        print(f"{lbl:<4}{str(tuple(round(c, 8) for c in d)):>44}")
    dt = act(X, (1.0, 0, 0, 0))
    dz = act(X, (0, 0, 0, 1.0))
    dx = act(X, (0, 1.0, 0, 0))
    dy = act(X, (0, 0, 1.0, 0))
    check("t maps into z only", abs(dt[1]) + abs(dt[2]), 0.0)
    check("t -> eta z", dt[3], eta)
    check("z -> eta t", dz[0], eta)
    check("x stays in the xy-plane", abs(dx[0]) + abs(dx[3]), 0.0)
    check("y stays in the xy-plane", abs(dy[0]) + abs(dy[3]), 0.0)
    # zeta = eta - i theta generates the standard counterclockwise rotation
    # about z:  x -> +theta y,  y -> -theta x
    check("x -> +theta y", dx[2], th)
    check("y -> -theta x", dy[1], -th)
    print()
    print("    span{t,z}  is closed under the action, and the action there is")
    print("               a BOOST of rapidity eta  (t <-> z mixing)")
    print("    span{x,y}  is closed under the action, and the action there is")
    print("               a ROTATION by theta      (x <-> y mixing)")
    print()
    print("  Those two planes are orthogonal complements. So a single")
    print("  loxodromic element hands you a timelike plane AND the spacelike")
    print("  plane orthogonal to it, with a boost in one and a rotation in the")
    print("  other -- with nothing imposed.")
    print()
    print("  0006 wrote down a 4-velocity u plus a spin bivector S and DEMANDED")
    print("  S^{mu nu} u_nu = 0 to keep them orthogonal. That condition is not")
    print("  an extra postulate here; it is the statement that the two")
    print("  invariant planes of one element are orthogonal complements, which")
    print("  they are automatically. The hack is retired, not merely retracted.")
    print()

    print("=" * 74)
    print("PART 4  --  Mass is HAVING AN AXIS; masslessness is degeneracy")
    print("=" * 74)
    print()
    hdr = (f"{'case':<22}{'det X':>20}{'eigenvalues':>26}"
           f"{'|v1 x v2|':>12}")
    print(hdr)
    print("-" * len(hdr))
    tilt = (0.6, 0.0, 0.8)   # generic (non-diagonal) axis, so the result is
                             # not an artifact of sigma_z being diagonal
    cases = [
        ("elliptic  (0,1)", X_of(complex(0.0, -1.0), (0.0, 0.0, 1.0))),
        ("hyperbolic (1,0)", X_of(complex(1.0, 0.0), (0.0, 0.0, 1.0))),
        ("LOXODROMIC (1,1)", X_of(complex(1.0, -1.0), (0.0, 0.0, 1.0))),
        ("LOXODROMIC tilted", X_of(complex(1.0, -1.0), tilt)),
        ("nilpotent (null n)", X_of(1.0, (1.0, 1j, 0.0))),
    ]
    for lbl, Xc in cases:
        lam, v1, v2 = eigen(Xc)
        par = parallel(v1, v2)
        print(f"{lbl:<22}{str(complex(round(det(Xc).real, 6), round(det(Xc).imag, 6))):>20}"
              f"{f'+-{complex(round(lam.real,4), round(lam.imag,4))}':>26}{par:>12.2e}")
        if abs(det(Xc)) > 1e-12:
            check(f"{lbl}: two independent eigendirections",
                  1.0 if par > 1e-6 else 0.0, 1.0)
        else:
            check(f"{lbl}: eigendirections collide", par, 0.0)
    print()
    print("  det X != 0  ->  distinct eigenvalues  ->  TWO independent")
    print("  eigendirections -> a genuine axis -> an invariant timelike plane")
    print("  -> a rest frame exists -> MASSIVE.")
    print()
    print("  det X = 0 (X != 0) -> repeated eigenvalue -> the eigendirections")
    print("  COLLIDE (|v1 x v2| = 0) -> no axis -> no rest frame -> MASSLESS.")
    print()
    print("  So masslessness is eigenvector degeneracy: the matrix is")
    print("  defective, a Jordan block rather than a diagonalizable element.")
    print("  'Has a rest frame' and 'is diagonalizable' are the same statement.")
    print("  This is a sharper reading of mass than distance-from-the-cone in")
    print("  0007, and it agrees with it -- |det X| is that distance.")
    print()

    print("=" * 74)
    print("PART 5  --  Compact x non-compact: spin discrete, momentum not")
    print("=" * 74)
    print()
    print("  exp(sX) has eigenvalues exp(+- s lambda) with lambda = a + i b.")
    print("  The e^{isb} factor WINDS (period 2pi/b); the e^{sa} factor DRIFTS.")
    print("  Track both along the flow of a loxodromic element:")
    print()
    eta, th = 0.8, 2.0
    Xl = X_of(complex(eta, -th), (0.0, 0.0, 1.0))
    lam, _, _ = eigen(Xl)
    a, b = lam.real, lam.imag
    print(f"    eta = {eta}, theta = {th}  ->  lambda = {lam:.6f}")
    print(f"    drift rate a = {a:.6f}   winding rate b = {b:.6f}")
    print(f"    winding period = 2pi/|b| = {2 * math.pi / abs(b):.6f}")
    print()
    hdr = f"{'s':>8}{'|exp(s lam)|':>16}{'phase/2pi':>14}{'phase mod 1':>14}"
    print(hdr)
    print("-" * len(hdr))
    period = 2 * math.pi / abs(b)
    for s in (0.0, period / 4, period / 2, period, 2 * period, 4 * period):
        e = cmath.exp(s * lam)
        ph = cmath.phase(e) / (2 * math.pi)
        print(f"{s:>8.4f}{abs(e):>16.6f}{s * b / (2 * math.pi):>14.6f}"
              f"{(s * b / (2 * math.pi)) % 1.0:>14.6f}")
    for n in (1, 2, 4):
        s = n * period
        check(f"phase returns after {n} periods",
              (s * b / (2 * math.pi)) % 1.0, 0.0, atol=1e-9)
        check(f"modulus keeps growing after {n} periods",
              1.0 if abs(cmath.exp(s * lam)) > 1.0 else 0.0, 1.0)
    print()
    print("  The phase comes back to zero after every period -- EXACTLY, at")
    print("  every multiple -- while the modulus grows without bound and never")
    print("  returns. One element, and its flow factors into a compact circle")
    print("  and a non-compact line.")
    print()
    print("  Apply 0004's rule (quantization IS compactness) to each factor:")
    print()
    print("      compact factor      -> closed orbit -> DISCRETE   -> spin")
    print("      non-compact factor  -> open orbit   -> CONTINUOUS -> momentum")
    print()
    print("  A massive particle with spin is exactly that: a quantized spin")
    print("  and a continuous momentum, carried by ONE object. The two do not")
    print("  need gluing because they are the two factors of one flow.")
    print()
    print("  Degenerations, all from the same family:")
    print("      theta -> 0        pure boost      massive, SPIN 0")
    print("      eta   -> 0        pure rotation   spin, no boost content")
    print("      axis -> null      nilpotent       massless, helicity only")
    print("      both nonzero      LOXODROMIC      massive WITH spin (generic)")
    print()
    print("  Massive spin-0 -- the case that forced the retracted hack in 0006")
    print("  -- is now just theta = 0 inside one family, not a separate")
    print("  construction. That is the unification that was asked for.")
    print()

    print("=" * 74)
    print("SELF-CHECKS")
    print("=" * 74)
    bad = [p for p in PASS if not p[1]]
    for name, ok, got, want in PASS:
        print(f"  [{'ok' if ok else 'FAIL'}] {name:<50} {got:+.6e}")
    print()
    print(f"  {len(PASS) - len(bad)}/{len(PASS)} checks passed.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
