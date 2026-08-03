"""
The photon problem: an object that winds in space but not in time.

The tension. In the original formulation, speed is pinned at c and split
between circulating and translating: sin(theta) = v/c. A photon has v = c, so
theta = 90 deg, so the transverse (circulating) component is ZERO, so
L = r p_perp = 0. The model predicts a spin-0 photon. Measured helicity is +-1.

  PART 1  the contradiction, stated numerically
  PART 2  which 2-planes contain NO timelike vector yet still support a
          rotation? Scan all three types. Exactly one answer.
  PART 3  that plane's bivector IS a photon field: |E| = |B|, E.B = 0,
          both Lorentz invariants vanish, Poynting along the propagation axis
  PART 4  why massless states carry HELICITY (one number) and massive ones
          carry SPIN (a 3-vector): the orthogonal complement of a null vector
          is DEGENERATE
  PART 5  the reorganisation this forces -- mass from the 4-velocity, spin
          from a bivector orthogonal to it -- which also makes mass and spin
          independent, so massive spin-0 is fine
  PART 6  alpha: what is in reach and what is not

Pure stdlib. Run: python3 0006_photon_null_plane_and_alpha.py
"""

import math

PASS = []
ETA = (1.0, -1.0, -1.0, -1.0)


def check(name, got, want, atol=1e-12):
    ok = abs(got - want) <= atol
    PASS.append((name, ok, got, want))
    return ok


def dot(a, b):
    return sum(ETA[i] * a[i] * b[i] for i in range(4))


def wedge(u, v):
    return [[u[m] * v[n] - u[n] * v[m] for n in range(4)] for m in range(4)]


def inv1(F):
    """F^{ab} F_{ab} = 2(B^2 - E^2)."""
    return sum(F[a][b] * F[a][b] * ETA[a] * ETA[b]
               for a in range(4) for b in range(4))


def levi():
    """eps[a][b][c][d] with eps_0123 = +1."""
    e = {}
    perms = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2), (1, 0, 3, 2),
             (1, 2, 0, 3), (1, 3, 2, 0), (2, 0, 1, 3), (2, 1, 3, 0),
             (2, 3, 0, 1), (3, 0, 2, 1), (3, 1, 0, 2), (3, 2, 1, 0)]
    for p in perms:
        e[p] = 1.0
    odd = [(0, 1, 3, 2), (0, 2, 1, 3), (0, 3, 2, 1), (1, 0, 2, 3),
           (1, 2, 3, 0), (1, 3, 0, 2), (2, 0, 3, 1), (2, 1, 0, 3),
           (2, 3, 1, 0), (3, 0, 1, 2), (3, 1, 2, 0), (3, 2, 0, 1)]
    for p in odd:
        e[p] = -1.0
    return e


EPS = levi()


def inv2(F):
    """F^{ab} Fdual_{ab}, the Pfaffian invariant; ~ -4 E.B. Zero iff simple."""
    tot = 0.0
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    s = EPS.get((a, b, c, d), 0.0)
                    if s:
                        tot += s * F[a][b] * F[c][d]
    return tot


def EB(F):
    """E^i = F^{i0}, B^i = -1/2 eps_ijk F^{jk} (3D Levi-Civita)."""
    E = [F[i][0] for i in (1, 2, 3)]
    B = [-(F[2][3]), -(F[3][1]), -(F[1][2])]
    return E, B


def norm3(v):
    return math.sqrt(sum(c * c for c in v))


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]]


def main():
    T = (1.0, 0.0, 0.0, 0.0)
    X = (0.0, 1.0, 0.0, 0.0)
    Y = (0.0, 0.0, 1.0, 0.0)
    Z = (0.0, 0.0, 0.0, 1.0)
    K = (1.0, 0.0, 0.0, 1.0)          # null, propagating along +z

    print("=" * 74)
    print("PART 1  --  The contradiction is real")
    print("=" * 74)
    print()
    print("  Original formulation: total speed c, split by sin(theta) = v/c.")
    print()
    hdr = f"{'v/c':>8}{'theta (deg)':>14}{'p_perp / p':>14}{'L (units r p)':>16}"
    print(hdr)
    print("-" * len(hdr))
    for b in (0.0, 0.5, 0.9, 0.99, 1.0):
        th = math.asin(min(b, 1.0))
        pperp = math.cos(th)
        print(f"{b:>8.2f}{math.degrees(th):>14.4f}{pperp:>14.6f}"
              f"{pperp:>16.6f}")
    check("photon gets zero transverse momentum",
          math.cos(math.asin(1.0)), 0.0, atol=1e-8)
    print()
    print("  At v = c the transverse component is exactly zero, so the naive")
    print("  model gives the photon L = 0. Measured photon helicity is +-1.")
    print("  The original formulation genuinely fails here and needs the")
    print("  extension asked for.")
    print()

    print("=" * 74)
    print("PART 2  --  Which planes contain no timelike vector?")
    print("=" * 74)
    print()
    print("  Requirement: something that can look like it spins in a spatial")
    print("  direction while having NO time-direction content. So scan each")
    print("  plane type and classify every direction inside it.")
    print()
    hdr = (f"{'plane':<20}{'type':<12}{'timelike dirs':>15}"
           f"{'null dirs':>11}{'spacelike':>11}")
    print(hdr)
    print("-" * len(hdr))
    for label, u, v in (("span{x,y}", X, Y),
                        ("span{t,x}", T, X),
                        ("span{k,x}  k=t+z", K, X)):
        nt = nn = ns = 0
        N = 3600
        for i in range(N):
            ang = 2.0 * math.pi * i / N
            w = tuple(math.cos(ang) * u[j] + math.sin(ang) * v[j]
                      for j in range(4))
            n2 = dot(w, w)
            if n2 > 1e-9:
                nt += 1
            elif n2 < -1e-9:
                ns += 1
            else:
                nn += 1
        g11, g12, g22 = dot(u, u), dot(u, v), dot(v, v)
        det = g11 * g22 - g12 * g12
        typ = "spacelike" if det > 1e-9 else ("timelike" if det < -1e-9
                                              else "null")
        print(f"{label:<20}{typ:<12}{nt:>15}{nn:>11}{ns:>11}")
        if typ == "null":
            check("null plane has no timelike direction", float(nt), 0.0)
            check("null plane has exactly 2 null dirs (+-k)", float(nn), 2.0)
    print()
    print("  (directions sampled over a full turn, so each null LINE shows up")
    print("   twice, as +k and -k)")
    print()
    print("  The timelike plane is disqualified: it contains timelike")
    print("  directions, so it carries time-axis content -- mass.")
    print("  The spacelike plane is all-spacelike but a null ray confined to")
    print("  it needs confining, which is what makes a massive particle.")
    print("  The NULL plane is the answer: NO timelike direction anywhere in")
    print("  it, exactly one null line (the propagation direction itself),")
    print("  everything else spacelike.")
    print()
    print("  So the object asked for is not an extension bolted on. It is the")
    print("  THIRD CASE of the trichotomy from 0004, which was always there")
    print("  and had only been labelled, never used.")
    print()

    print("=" * 74)
    print("PART 3  --  That plane's bivector IS a photon field")
    print("=" * 74)
    print()
    F = wedge(K, X)
    E, B = EB(F)
    print(f"    F = k ^ x  with k = (1,0,0,1)")
    print(f"    E = {E}      |E| = {norm3(E):.6f}")
    print(f"    B = {B}      |B| = {norm3(B):.6f}")
    print(f"    E . B                = {sum(E[i] * B[i] for i in range(3)):.2e}")
    print(f"    E x B  (Poynting)    = {cross(E, B)}")
    print(f"    spatial part of k    = {list(K[1:])}")
    print()
    check("|E| = |B|", norm3(E) - norm3(B), 0.0)
    check("E perp B", sum(E[i] * B[i] for i in range(3)), 0.0)
    pv = cross(E, B)
    kv = list(K[1:])
    check("Poynting parallel to k",
          norm3(cross(pv, kv)), 0.0)
    print(f"    invariant 1  F.F     = {inv1(F):.2e}   (= 2(B^2 - E^2))")
    print(f"    invariant 2  F.Fdual = {inv2(F):.2e}   (~ -4 E.B)")
    check("F.F = 0 for null plane", inv1(F), 0.0)
    check("F.Fdual = 0 for null plane", inv2(F), 0.0)
    print()
    print("  Both Lorentz invariants vanish -- the signature of a RADIATION")
    print("  field. |E| = |B| and E perp B hold in every frame, because there")
    print("  is no frame that can remove either. Poynting vector points along")
    print("  the propagation direction.")
    print()
    print("  So the null plane is not merely allowed to describe a photon; a")
    print("  null 2-plane and a free electromagnetic wave are the same object.")
    print("  Nothing was fitted -- k ^ x was written down and a photon came")
    print("  out.")
    print()
    for label, u, v in (("spacelike x^y", X, Y), ("timelike t^x", T, X)):
        Fo = wedge(u, v)
        Eo, Bo = EB(Fo)
        print(f"    contrast {label:<16} |E| = {norm3(Eo):.3f}"
              f"   |B| = {norm3(Bo):.3f}   F.F = {inv1(Fo):+.1f}")
    print("    -- pure magnetic and pure electric respectively; each has a")
    print("       frame where the other vanishes. Only the null case does not.")
    print()

    print("=" * 74)
    print("PART 4  --  Why helicity is ONE number and spin is a 3-vector")
    print("=" * 74)
    print()
    print("  Spin planes must be orthogonal to the particle's own direction.")
    print("  So ask what the orthogonal complement looks like in each case.")
    print()
    for label, w in (("massive  u = (1,0,0,0)", T), ("massless k = (1,0,0,1)",
                                                     K)):
        basis = [b for b in (T, X, Y, Z)]
        comp = []
        for b in basis:
            proj = tuple(b[i] - (dot(b, w) / dot(w, w) * w[i]
                                 if abs(dot(w, w)) > 1e-9 else 0.0)
                         for i in range(4))
            comp.append(proj if abs(dot(w, w)) > 1e-9 else b)
        # build the induced Gram matrix on w-perp directly
        perp = [v for v in (T, X, Y, Z, K)
                if abs(dot(v, w)) < 1e-9]
        # independent set
        ind = []
        for v in perp:
            trial = ind + [v]
            G = [[dot(a, b) for b in trial] for a in trial]
            if rank(G) == len(trial):
                ind.append(v)
            elif not any(all(abs(v[i] - z[i]) < 1e-12 for i in range(4))
                         for z in ind):
                ind.append(v)
        G = [[dot(a, b) for b in ind] for a in ind]
        r = rank(G)
        print(f"  {label}")
        print(f"    w.w = {dot(w, w):+.1f}")
        print(f"    dim(w-perp) = {len(ind)}    rank of induced metric = {r}")
        print(f"    degenerate directions = {len(ind) - r}")
        if dot(w, w) > 0.5:
            check("massive: complement nondegenerate", float(len(ind) - r), 0.0)
        else:
            check("massless: complement degenerate", float(len(ind) - r), 1.0)
        print()
    print("  Massive: the complement is 3-dimensional and nondegenerate ->")
    print("  a full SO(3) of spin planes -> spin is a 3-vector, 2s+1 states.")
    print()
    print("  Massless: the complement is 3-dimensional but DEGENERATE, because")
    print("  a null vector is orthogonal to ITSELF. Quotienting out that")
    print("  direction leaves a 2-dimensional spacelike plane -- the")
    print("  polarization plane -- carrying only SO(2). One number, two signs.")
    print()
    print("  THAT is why the photon has helicity +-1 rather than three states")
    print("  m = -1,0,+1. The missing longitudinal state is the direction that")
    print("  got quotiented away. It falls out of k.k = 0, not from a rule.")
    print()

    print("=" * 74)
    print("PART 5  --  The reorganisation this forces")
    print("=" * 74)
    print()
    print("  A massive particle is not one bivector. It is:")
    print("     a 4-velocity u   (timelike)      -> mass")
    print("     a spin bivector S with S^{mu nu} u_nu = 0   -> spin")
    print("  The second condition (Frenkel-Pirani) says S is purely spatial in")
    print("  the rest frame. Check it on a spin-along-z bivector:")
    print()
    S = wedge(X, Y)
    su = [sum(S[m][n] * ETA[n] * T[n] for n in range(4)) for m in range(4)]
    print(f"    S = x ^ y,  u = (1,0,0,0):   S^(mu nu) u_nu = {su}")
    check("Frenkel-Pirani satisfied", max(abs(c) for c in su), 0.0)
    print()
    print("  Two independent objects, so mass and spin are independent, and a")
    print("  massive spin-0 particle is simply u with S = 0. The worry raised")
    print("  in 0003 dissolves structurally, not just case by case.")
    print()
    print("  For a photon there is no u to be orthogonal to. The condition")
    print("  degenerates onto the null plane and only helicity survives.")
    print("  One framework, three regimes, chosen by the causal type:")
    print()
    print("     timelike direction present  -> mass")
    print("     spacelike plane orthogonal to it -> spin (3-vector)")
    print("     null plane, no timelike direction -> helicity (one number)")
    print()

    print("=" * 74)
    print("PART 6  --  Alpha: what is in reach, and what is not")
    print("=" * 74)
    print()
    a_inv_0 = 137.035999206
    a_inv_MZ = 127.951
    print(f"    alpha^-1 at q^2 = 0    = {a_inv_0:.6f}")
    print(f"    alpha^-1 at q^2 = MZ^2 = {a_inv_MZ:.3f}   (MS-bar)")
    print(f"    difference             = {a_inv_0 - a_inv_MZ:.2f}")
    print()
    print("  THE DECISIVE FACT: alpha RUNS. It is not a constant, so it is not")
    print("  a number a kinematic or geometric framework can produce. Any")
    print("  derivation of '137' is a derivation of the zero-momentum limit of")
    print("  a scale-dependent coupling, which is a dynamical quantity.")
    print("  This is measurement, and it is what sinks most alpha programmes.")
    print()
    print("  Cautionary case: Eddington argued 136 from counting degrees of")
    print("  freedom, then revised to 137 when measurements improved. The")
    print("  revision, not the original, is what the episode is remembered")
    print("  for. Any 'derivation' flexible enough to be adjusted afterwards")
    print("  was never a derivation.")
    print()
    print("  WHAT IS PLAUSIBLY IN REACH -- charge QUANTIZATION, by the same")
    print("  mechanism that already gave spin quantization in 0004:")
    print("  compactness -> closed orbit -> discrete winding number. If charge")
    print("  is a winding number on a compact direction, integer charge is")
    print("  automatic. That is a real structural result and the framework")
    print("  already owns the machinery.")
    print()
    print("  What it would NOT give is the value. In Kaluza-Klein the coupling")
    print("  is tied to the compactification radius, roughly alpha ~ (lP/R)^2:")
    R_over_lP = 1.0 / math.sqrt(1.0 / a_inv_0)
    print(f"      alpha = (lP/R)^2  =>  R = lP * sqrt(1/alpha)"
          f" = {R_over_lP:.2f} lP")
    check("KK radius consistency", (1.0 / R_over_lP) ** 2, 1.0 / a_inv_0)
    print("  (order-of-magnitude only; the coefficient is convention-dependent)")
    print()
    print("  So the geometric route RELOCATES the question from 'why 137' to")
    print("  'why R ~ 12 Planck lengths'. That is honest progress of a kind --")
    print("  it is not an answer, and it should not be sold as one.")
    print()
    print("  Recommended: pursue charge quantization, which the framework can")
    print("  plausibly deliver. Do not pursue the value of alpha.")
    print()

    print("=" * 74)
    print("SELF-CHECKS")
    print("=" * 74)
    bad = [p for p in PASS if not p[1]]
    for name, ok, got, want in PASS:
        print(f"  [{'ok' if ok else 'FAIL'}] {name:<48} {got:.6e}")
    print()
    print(f"  {len(PASS) - len(bad)}/{len(PASS)} checks passed.")
    return 1 if bad else 0


def rank(G, tol=1e-9):
    """Rank of a small symmetric matrix by Gaussian elimination."""
    M = [row[:] for row in G]
    n = len(M)
    r = 0
    for c in range(n if n == 0 else len(M[0])):
        piv = None
        for i in range(r, n):
            if abs(M[i][c]) > tol:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(n):
            if i != r and abs(M[i][c]) > tol:
                f = M[i][c] / M[r][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(len(M[i]))]
        r += 1
    return r


if __name__ == "__main__":
    raise SystemExit(main())
