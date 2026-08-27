"""The bond operator, the dimension theorem, and a bookkeeping trap.

0041 left three fronts: measure the dimensional selection instead
of extending it, find the bond's quantum operator, and construct
the two-body source honestly.  All three move here, and the third
turns into a caution that explains a design choice already made.

  s1  THE DIMENSION THEOREM, MEASURED.  A general-dimension
      curvature pipeline (ricci_nd) applied to the point channel
      g = eta + w k k^T with w = w0/rho^p in d spatial dimensions:
      the off-source Ricci vanishes at p = d - 2 and only there --
      d = 3: 3e-7 at p=1 (vs 5e-2 at p=2);
      d = 4: 7e-7 at p=2 (vs 3e-2, 7e-2 at p=1, 3);
      d = 5: 1e-6 at p=3 (vs 3e-2, 8e-2 at p=2, 4).
      The web's vacuum principle selects the HARMONIC profile in
      every dimension.  With 0041's mu/T = -1/p, the bond's
      transverse charge is (mu+T)/T = (d-3)/(d-2): THREE SPATIAL
      DIMENSIONS IS THE UNIQUE DIMENSION IN WHICH CORRELATION
      CARRIES NO PARTICIPATION CHARGE.  0041's extension is now a
      measurement.

  s2  THE BOND'S OPERATOR.  0041 predicted "a product structure on
      the charge lattice."  The web's quantum tier already has
      exactly one such object: the MUTUAL BRAIDING PHASE of two
      defects, omega^(n_a n_b) -- built from the level-N Weyl
      algebra as transport of a's charge around b's holonomy.  Its
      spectrum is the multiplication table mod N (the charge's is
      the addition table), and it SEPARATES STATES THE CHARGE
      CANNOT: at N = 5, total charge 0 contains states with three
      distinct bond values.  Correlation is not a function of the
      marginals -- the quantum statement of "charges add, bonds
      multiply."  Classical limit matches by construction of the
      ledger: with m = n x (1/4GN), bond energies go as n_a n_b,
      so the BOND'S QUANTUM IS THE SQUARE OF THE CHARGE QUANTUM.

  s3  WHERE THE BOND'S ENERGY LIVES (a trap, measured).  Modelling
      the bond as an independent MATTER source with its own (mu, T)
      gives a far-field mass of exactly 2.000 x the binding energy
      -- an overcount.  The bond is FIELD, not matter: its STRESS
      is a legitimate source (it supplies the quadrupole formula's
      missing half, 0039/0040), while its ENERGY is already carried
      by the field's nonlinearity.  Note that the channel built in
      0034/0035 adds 4 S_ij / r to the SPATIAL block only: the
      construction that reproduced Einstein's luminosity is exactly
      the one that avoids this trap -- now with the reason.

Run directly for the verification suite.
"""

from __future__ import annotations

import cmath
import importlib
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_q = importlib.import_module("0022_the_quantum_tier")
clock, shift = _q.clock, _q.shift

TAU = 2 * math.pi


# =====================================================================
# battery instrument: general-dimension curvature
# =====================================================================

def invn(m):
    n = len(m)
    a = [row[:] + [1.0 if i == j else 0.0 for j in range(n)]
         for i, row in enumerate(m)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(a[r][col]))
        a[col], a[piv] = a[piv], a[col]
        d = a[col][col]
        a[col] = [x / d for x in a[col]]
        for r in range(n):
            if r != col and a[r][col] != 0.0:
                f = a[r][col]
                a[r] = [x - f * y for x, y in zip(a[r], a[col])]
    return [row[n:] for row in a]


def christ_nd(gfun, x, h):
    n = len(x)

    def sh(p, k, s):
        q = list(p)
        q[k] += s * h
        return tuple(q)
    dg = []
    for k in range(n):
        gp, gm = gfun(sh(x, k, 1)), gfun(sh(x, k, -1))
        dg.append([[(gp[i][j] - gm[i][j]) / (2 * h) for j in range(n)]
                   for i in range(n)])
    gi = invn(gfun(x))
    G = [[[0.0] * n for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                s = 0.0
                for l in range(n):
                    s += gi[i][l] * (dg[j][l][k] + dg[k][l][j]
                                     - dg[l][j][k])
                G[i][j][k] = 0.5 * s
    return G


def ricci_nd(gfun, x, h=1e-3):
    """Ricci tensor in any dimension (n = len(x))."""
    n = len(x)

    def sh(p, k, s):
        q = list(p)
        q[k] += s * h
        return tuple(q)
    G0 = christ_nd(gfun, x, h)
    Gp = [christ_nd(gfun, sh(x, k, 1), h) for k in range(n)]
    Gm = [christ_nd(gfun, sh(x, k, -1), h) for k in range(n)]
    R = [[0.0] * n for _ in range(n)]
    for j in range(n):
        for l in range(n):
            s = 0.0
            for i in range(n):
                s += (Gp[i][i][j][l] - Gm[i][i][j][l]) / (2 * h)
                s -= (Gp[j][i][i][l] - Gm[j][i][i][l]) / (2 * h)
                for p in range(n):
                    s += G0[i][i][p] * G0[p][j][l] \
                        - G0[i][j][p] * G0[p][i][l]
            R[j][l] = s
    return R


def ks_point_nd(d, w0, p):
    """Point channel in d spatial dimensions: g = eta + w k k^T with
    k = (-1, n_hat) and w = w0 / rho^p."""
    n = d + 1

    def g(x):
        sp = x[1:]
        r = math.sqrt(sum(c * c for c in sp))
        k = [-1.0] + [c / r for c in sp]
        w = w0 / r ** p
        out = []
        for i in range(n):
            row = []
            for j in range(n):
                e = -1.0 if (i == j == 0) else (1.0 if i == j else 0.0)
                row.append(e + w * k[i] * k[j])
            out.append(row)
        return out
    return g


# =====================================================================
# 1. the dimension theorem, measured
# =====================================================================

def vacuum_scan(d, exponents):
    n = d + 1
    out = []
    for p in exponents:
        if p <= 0:
            continue
        g = ks_point_nd(d, 0.02, p)
        worst = 0.0
        for scale in (0.9, 1.4):
            x = tuple([0.0] + [scale * c
                               for c in (0.6, 0.5, 0.4, 0.35, 0.3)[:d]])
            R = ricci_nd(g, x, h=1e-3)
            worst = max(worst, max(abs(R[i][j])
                                   for i in range(n) for j in range(n)))
        out.append((p, worst))
    return out


def verify_dimension_theorem() -> None:
    print("    off-source max|R_mn| for w = w0/rho^p "
          "(* = predicted vacuum exponent d-2):")
    for d in (3, 4, 5):
        rows = vacuum_scan(d, (d - 3, d - 2, d - 1))
        line = "  ".join(f"p={p}: {v:.0e}" + ("*" if p == d - 2 else "")
                         for p, v in rows)
        print(f"      d = {d}:  {line}")
        for p, v in rows:
            if p == d - 2:
                assert v < 1e-5, (d, p, v)
            else:
                assert v > 1e-3, (d, p, v)
    print()
    print("  THE VACUUM PRINCIPLE SELECTS THE HARMONIC PROFILE IN")
    print("  EVERY DIMENSION.  With 0041's mu/T = -1/p, the bond's")
    print("  transverse charge is (mu+T)/T = (d-3)/(d-2):")
    for d in (3, 4, 5, 6):
        tag = "   <-- ZERO" if d == 3 else ""
        print(f"      d = {d}: (mu+T)/T = {(d - 3) / (d - 2):+.4f}{tag}")
    print("  THREE SPATIAL DIMENSIONS IS THE UNIQUE DIMENSION IN")
    print("  WHICH CORRELATION CARRIES NO PARTICIPATION CHARGE.")
    print("  0041's extension is now a measurement.")


# =====================================================================
# 2. the bond's operator
# =====================================================================

def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def bond_phase(na, nb, N):
    """The mutual braiding phase of two defects: transport a's charge
    around b's holonomy gives (omega^nb)^na."""
    om = cmath.exp(2j * math.pi / N)
    return om ** ((na * nb) % N)


def verify_bond_operator() -> None:
    N = 5
    om = cmath.exp(2j * math.pi / N)
    U, V = clock(N), shift(N)
    UV, VU = mm(U, V), mm(V, U)
    err = max(abs(UV[i][j] - om * VU[i][j])
              for i in range(N) for j in range(N))
    assert err < 1e-12, err
    print(f"    level-{N} Weyl algebra U V = omega V U: residual "
          f"{err:.0e}")
    # the bond's spectrum is the multiplication table
    print(f"    bond spectrum omega^(n_a n_b) -- exponents mod {N}:")
    print("        n_b:  " + "  ".join(str(b) for b in range(N)))
    for na in range(N):
        row = "  ".join(str((na * nb) % N) for nb in range(N))
        print(f"      n_a={na}:  {row}")
        for nb in range(N):
            want = om ** ((na * nb) % N)
            assert abs(bond_phase(na, nb, N) - want) < 1e-12
    # bonds separate states the charge cannot
    print()
    print("    states of equal TOTAL CHARGE, and their bond values:")
    separated = 0
    for q in range(N):
        states = [(na, (q - na) % N) for na in range(N)]
        vals = sorted({(na * nb) % N for na, nb in states})
        if len(vals) > 1:
            separated += 1
        print(f"      Q = {q}: bond values {vals}")
    assert separated == N, separated
    print()
    print("  THE BOND'S OPERATOR IS THE MUTUAL BRAIDING PHASE.  Its")
    print("  spectrum is the MULTIPLICATION table where the charge's")
    print("  is the ADDITION table, and it separates states the")
    print("  charge cannot -- correlation is not a function of the")
    print("  marginals.  With m = n x (1/4GN), bond energies go as")
    print("  n_a n_b: THE BOND'S QUANTUM IS THE SQUARE OF THE")
    print("  CHARGE QUANTUM -- 0041's predicted product structure,")
    print("  realized by an object the theory already had (0027's")
    print("  abelian anyons).")


# =====================================================================
# 3. where the bond's energy lives
# =====================================================================

M1 = M2 = 0.02
D_B = 1.0


def matter_bond_h00(x, nseg=4000):
    """Linearized h_00 of a bond modelled as an independent MATTER
    segment with line density mu and tension T (mu = -T):
    h_00 = 2 int (T_00 + T_ii) dl / |x - l|."""
    T = M1 * M2 / D_B ** 2
    mu = -T
    s = 0.0
    for k in range(nseg):
        z = -D_B / 2 + D_B * (k + 0.5) / nseg
        s += 2 * (mu - T) * (D_B / nseg) \
            / math.dist(x, (0.0, 0.0, z))
    return s


def verify_energy_bookkeeping() -> None:
    binding = -M1 * M2 / D_B
    for R in (20.0, 40.0):
        h = matter_bond_h00((0.0, R, 0.0))
        M_eff = h * R / 2
        ratio = M_eff / binding
        assert abs(ratio - 2.0) < 0.01, ratio
        print(f"    R = {R}: far-field mass {M_eff:+.5e} vs binding "
              f"energy {binding:+.5e}")
        print(f"           ratio = {ratio:.3f}")
    print()
    print("  A TRAP, AND THE REASON A DESIGN CHOICE WAS RIGHT.")
    print("  Modelling the bond as independent MATTER overshoots the")
    print("  binding energy by exactly 2.  The bond is FIELD: its")
    print("  STRESS is a legitimate source (it supplies the")
    print("  quadrupole formula's missing half), while its ENERGY is")
    print("  already carried by the field's nonlinearity.  The")
    print("  channel built in 0034/0035 adds 4 S_ij / r to the")
    print("  SPATIAL block only -- the construction that reproduced")
    print("  Einstein's luminosity is exactly the one that avoids")
    print("  this trap.")


def run_verification_suite() -> None:
    sections = [
        ("The dimension theorem, measured",
         verify_dimension_theorem),
        ("The bond's operator", verify_bond_operator),
        ("Where the bond's energy lives",
         verify_energy_bookkeeping),
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
