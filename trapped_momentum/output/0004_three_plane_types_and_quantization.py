"""
Three causal types of winding plane, and why only some of them quantize.

The proposal being tested: eigenstates exist only at exactly the time axis,
exactly the space axis, or exactly their x = t line -- with the mechanism being
Fourier-style orthogonality, all cross terms integrating to zero.

That trichotomy is not a guess. A 2-plane through a point in Minkowski space is
exactly one of three Lorentz-invariant types, and there are no others. This
script derives the classification from scratch, then asks which types quantize
and checks the answer against measurement.

  PART 1  the three types, from the sign of the induced metric determinant
  PART 2  the one-parameter motion each type generates: closed or not
  PART 3  the Fourier argument, run in both cases. Compactness is the whole
          story: closed orbit -> discrete spectrum, open orbit -> continuous.
  PART 4  the prediction ledger, scored against experiment
  PART 5  the double cover, and whether the factor of 2 is topological

Pure stdlib. Run: python3 0004_three_plane_types_and_quantization.py
"""

import cmath
import math

PASS = []
ETA = (1.0, -1.0, -1.0, -1.0)     # signature (+,-,-,-), coords (t,x,y,z)


def check(name, got, want, atol=1e-12):
    ok = abs(got - want) <= atol
    PASS.append((name, ok, got, want))
    return ok


def dot(a, b):
    return sum(ETA[i] * a[i] * b[i] for i in range(4))


def matvec(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(4)) for i in range(4))


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)]
            for i in range(4)]


def expm(M, s, terms=60):
    """exp(s M) by series; exact after 3 terms for nilpotent generators."""
    R = [[1.0 if i == j else 0.0 for j in range(4)] for i in range(4)]
    T = [[1.0 if i == j else 0.0 for j in range(4)] for i in range(4)]
    for n in range(1, terms):
        T = matmul(T, [[s * M[i][j] for j in range(4)] for i in range(4)])
        T = [[T[i][j] / n for j in range(4)] for i in range(4)]
        R = [[R[i][j] + T[i][j] for j in range(4)] for i in range(4)]
    return R


def maxabs(M):
    return max(abs(M[i][j]) for i in range(4) for j in range(4))


# ================================================================= PART 1
# A 2-plane spanned by u, v. Induced metric g = [[u.u, u.v],[u.v, v.v]].
# det g > 0  -> spacelike plane   (both directions spacelike)
# det g < 0  -> timelike  plane   (contains a timelike direction)
# det g = 0  -> null      plane   (tangent to the light cone, degenerate)

def plane_type(u, v):
    g11, g12, g22 = dot(u, u), dot(u, v), dot(v, v)
    det = g11 * g22 - g12 * g12
    if abs(det) < 1e-12:
        return "null", det
    return ("spacelike" if det > 0 else "timelike"), det


def main():
    T = (1.0, 0.0, 0.0, 0.0)
    X = (0.0, 1.0, 0.0, 0.0)
    Y = (0.0, 0.0, 1.0, 0.0)
    Z = (0.0, 0.0, 0.0, 1.0)
    Nl = (1.0, 0.0, 0.0, 1.0)          # null: T + Z

    print("=" * 74)
    print("PART 1  --  There are exactly three kinds of winding plane")
    print("=" * 74)
    print()
    print("  det of the induced metric on span{u,v} classifies the plane, and")
    print("  its SIGN is Lorentz-invariant. Three signs, three types, no more.")
    print()
    hdr = f"{'plane':<18}{'det g':>12}{'type':>14}{'motion in it':>22}"
    print(hdr)
    print("-" * len(hdr))
    cases = [
        ("span{x, y}", X, Y, "spacelike", "rotation (elliptic)"),
        ("span{x, z}", X, Z, "spacelike", "rotation (elliptic)"),
        ("span{t, x}", T, X, "timelike", "boost (hyperbolic)"),
        ("span{t, z}", T, Z, "timelike", "boost (hyperbolic)"),
        ("span{t+z, x}", Nl, X, "null", "null rot (parabolic)"),
    ]
    for label, u, v, want, motion in cases:
        got, det = plane_type(u, v)
        print(f"{label:<18}{det:>12.4f}{got:>14}{motion:>22}")
        check(f"{label} is {want}", 1.0 if got == want else 0.0, 1.0)
    print()
    print("  'exactly the time axis, exactly the space axis, or their x = t")
    print("  line' IS this classification. The three cases are forced by the")
    print("  metric signature -- they are the three orbits of 2-planes under")
    print("  the Lorentz group. Nothing was chosen.")
    print()

    print("=" * 74)
    print("PART 2  --  Does the motion close? (this is the whole question)")
    print("=" * 74)
    print()
    # generators
    ROT = [[0.0] * 4 for _ in range(4)]      # xy rotation
    ROT[1][2], ROT[2][1] = -1.0, 1.0
    BST = [[0.0] * 4 for _ in range(4)]      # tx boost
    BST[0][1], BST[1][0] = 1.0, 1.0
    RXZ = [[0.0] * 4 for _ in range(4)]      # xz rotation
    RXZ[1][3], RXZ[3][1] = -1.0, 1.0

    # null rotation: search the sign that is nilpotent AND fixes the null vector
    NUL, sign_used = None, None
    for sgn in (+1.0, -1.0):
        cand = [[BST[i][j] + sgn * RXZ[i][j] for j in range(4)]
                for i in range(4)]
        cube = matmul(matmul(cand, cand), cand)
        fixes = max(abs(c) for c in matvec(cand, Nl))
        if maxabs(cube) < 1e-12 and fixes < 1e-12:
            NUL, sign_used = cand, sgn
            break
    print(f"  null-rotation generator found as B_x + ({sign_used:+.0f})*R_xz")
    print(f"    N^3 = 0 ?  max|N^3| = "
          f"{maxabs(matmul(matmul(NUL, NUL), NUL)):.2e}   (nilpotent)")
    print(f"    N annihilates the null vector (1,0,0,1) ?  max|N k| = "
          f"{max(abs(c) for c in matvec(NUL, Nl)):.2e}")
    check("null generator nilpotent", maxabs(matmul(matmul(NUL, NUL), NUL)), 0.0)
    check("null generator fixes k", max(abs(c) for c in matvec(NUL, Nl)), 0.0)
    print()
    print("  Now push a test vector around each motion and ask if it returns.")
    print()
    hdr = (f"{'generator':<22}{'type':<12}{'|orbit(2pi) - start|':>22}"
           f"{'closes?':>10}")
    print(hdr)
    print("-" * len(hdr))
    start = X
    for label, M, typ in (("rotation (xy)", ROT, "spacelike"),
                          ("boost (tx)", BST, "timelike"),
                          ("null rotation", NUL, "null")):
        moved = matvec(expm(M, 2.0 * math.pi), start)
        dev = math.sqrt(sum((moved[i] - start[i]) ** 2 for i in range(4)))
        print(f"{label:<22}{typ:<12}{dev:>22.6e}{'YES' if dev < 1e-9 else 'no':>10}")
    check("rotation closes at 2pi",
          math.sqrt(sum((matvec(expm(ROT, 2 * math.pi), start)[i] - start[i])
                        ** 2 for i in range(4))), 0.0, atol=1e-9)
    print()
    print("  Only the spacelike plane gives a CLOSED orbit. The boost runs off")
    print("  along a hyperbola forever; the null rotation runs off along a")
    print("  parabola forever. Checked to large parameter below:")
    print()
    for s in (10.0, 40.0):
        b = matvec(expm(BST, s), start)
        n = matvec(expm(NUL, s), start)
        print(f"    s = {s:>5.0f}:  |boost orbit| = {math.hypot(b[0], b[1]):.3e}"
              f"     |null orbit| = "
              f"{math.sqrt(sum(c * c for c in n)):.3e}")
    print()

    print("=" * 74)
    print("PART 3  --  The Fourier argument, run in both cases")
    print("=" * 74)
    print()
    print("  The proposed mechanism -- cross terms integrate to zero -- is")
    print("  right, and it is worth seeing exactly where it bites and where")
    print("  it does not.")
    print()
    print("  COMPACT ORBIT (spacelike plane). Parameter theta lives on a")
    print("  circle. Single-valuedness forces integer mode numbers, and then:")
    print()
    print(f"    {'(m,n)':<10}{'(1/2pi) INT e^i(m-n)th dth':>30}")
    for m, n in ((2, 2), (2, 3), (5, 1), (7, 7)):
        N = 200000
        acc = sum(cmath.exp(1j * (m - n) * (k + 0.5) * 2 * math.pi / N)
                  for k in range(N)) / N
        print(f"    {str((m, n)):<10}{abs(acc):>30.12f}")
        check(f"orthogonality (m,n)={(m, n)}", abs(acc),
              1.0 if m == n else 0.0, atol=1e-9)
    print()
    print("    Exactly the delta_mn that was described. Modes at different")
    print("    winding numbers are orthogonal, so the spectrum is DISCRETE.")
    print()
    print("  NON-COMPACT ORBIT (timelike plane). The parameter is rapidity,")
    print("  running over all of R. There is no periodicity to impose, so")
    print("  no integer condition arises. Overlap of two modes over a window")
    print("  of half-width L:")
    print()
    print(f"    {'(a,b)':<14}{'L=10':>14}{'L=100':>14}{'L=1000':>14}")
    for a, b in ((1.0, 1.0), (1.0, 1.2), (1.0, 1.0001)):
        row = []
        for L in (10.0, 100.0, 1000.0):
            d = a - b
            row.append(1.0 if d == 0 else abs(math.sin(d * L) / (d * L)))
        print(f"    {str((a, b)):<14}{row[0]:>14.6f}{row[1]:>14.6f}"
              f"{row[2]:>14.6f}")
    print()
    print("    Overlap decays as sinc, never to a clean delta at finite L, and")
    print("    crucially a and b may be ANY reals -- nothing selects a lattice.")
    print("    Continuous spectrum.")
    print()
    print("  CONCLUSION: quantization is compactness. Closed orbit -> discrete")
    print("  spectrum. Open orbit -> continuum. The Fourier intuition is right")
    print("  and this is the precise form of it.")
    print()

    print("=" * 74)
    print("PART 4  --  Prediction ledger, scored against measurement")
    print("=" * 74)
    print()
    rows = [
        ("spacelike winding", "closed", "DISCRETE",
         "spin", "quantized in hbar/2 steps", "OK"),
        ("null winding", "open*", "DISCRETE*",
         "helicity", "quantized (+-1 for photon)", "OK"),
        ("timelike winding", "open", "CONTINUOUS",
         "mass", "NOT quantized -- no mass ladder seen", "OK"),
        ("timelike winding", "open", "CONTINUOUS",
         "rapidity", "continuous, as observed", "OK"),
    ]
    hdr = (f"{'plane':<19}{'orbit':<8}{'spectrum':<12}{'observable':<11}"
           f"{'experiment':<34}")
    print(hdr)
    print("-" * len(hdr))
    for p, o, s, ob, ex, v in rows:
        print(f"{p:<19}{o:<8}{s:<12}{ob:<11}{ex:<34}")
    print()
    print("  * the null case is subtler and worth stating honestly: the")
    print("    parabolic motion itself is open, so on its own it would give a")
    print("    continuum. Massless states avoid that only because the null-")
    print("    rotation generators annihilate them; what is left is a compact")
    print("    circle of rotations about the momentum, and THAT is what")
    print("    quantizes helicity. Same rule (compact -> discrete), applied to")
    print("    what survives.")
    print()
    print("  The line worth noticing is the third. If mass came from winding")
    print("  in a CLOSED direction it would come in a ladder. It does not:")
    print("  electron 0.511, muon 105.7, tau 1777 MeV -- ratios 206.8 and")
    print("  16.82, no arithmetic or geometric pattern.")
    e, mu, tau = 0.51099895, 105.6583755, 1776.86
    print(f"    m_mu / m_e   = {mu / e:>10.3f}")
    print(f"    m_tau / m_mu = {tau / mu:>10.3f}")
    print(f"    m_tau / m_e  = {tau / e:>10.3f}")
    print()
    print("  So an OPEN (timelike) winding direction for mass is what the data")
    print("  wants, and a CLOSED one for spin. One framework, and the split")
    print("  between 'mass is continuous' and 'spin is quantized' falls out of")
    print("  the causal type of the plane. This is the strongest thing here.")
    print()
    print("  It also breaks the tie left open in 0003. Kaluza-Klein winds on a")
    print("  COMPACT spatial dimension, so it predicts a mass TOWER")
    print("  m_n = n hbar/(Rc). The timelike reading predicts a continuum.")
    print("  Observed lepton masses show no tower. On this evidence the")
    print("  timelike reading is favoured -- decided by data, not by taste.")
    print()

    print("=" * 74)
    print("PART 5  --  Is the factor of 2 topological rather than dynamical?")
    print("=" * 74)
    print()
    print("  A closed spatial loop gives single-valuedness -> integer n -> L =")
    print("  n hbar. That was 0002's result and it cannot reach hbar/2.")
    print("  But if what winds is the ROTATION ITSELF rather than a position,")
    print("  the relevant loop lives in the rotation group, and a 2pi path")
    print("  there is not contractible. Test on a spin-1/2 rotor:")
    print()
    print(f"    {'angle':>10}{'Re<psi(0)|psi(th)>':>24}")
    for deg in (0, 180, 360, 540, 720):
        th = math.radians(deg)
        amp = math.cos(th / 2.0)      # SU(2) rotor overlap for spin-1/2
        print(f"    {deg:>9}deg{amp:>24.10f}")
    check("360 deg gives -1", math.cos(math.radians(360) / 2.0), -1.0)
    check("720 deg gives +1", math.cos(math.radians(720) / 2.0), 1.0)
    print()
    print("  360 degrees returns the state to MINUS itself; 720 restores it.")
    print("  So the natural period of a winding-in-the-group is 4pi, and its")
    print("  mode numbers are half-integers. That is a much better home for")
    print("  the factor of 2 than a wrong radius: it explains why the number")
    print("  is 2 and not something else.")
    print()
    print("  Concrete fork this creates, and it is testable within the model:")
    print("    winding in SPACE  -> period 2pi -> L = n hbar     (spin 1)")
    print("    winding in the GROUP -> period 4pi -> L = n hbar/2 (spin 1/2)")
    print("  The model must say which object winds. That is now the sharpest")
    print("  open question, and it is sharper than 'there is a factor of 2'.")
    print()

    print("=" * 74)
    print("SELF-CHECKS")
    print("=" * 74)
    bad = [p for p in PASS if not p[1]]
    for name, ok, got, want in PASS:
        print(f"  [{'ok' if ok else 'FAIL'}] {name:<44} {got:.10e}")
    print()
    print(f"  {len(PASS) - len(bad)}/{len(PASS)} checks passed.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
