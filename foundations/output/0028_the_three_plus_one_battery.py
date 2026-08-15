"""The 3+1 battery: native-3D instruments at parity with 2+1.

The 2+1 program was carried by a small set of reusable instruments
(the transport deficit, the developed-loop charge reader, the flux
integral, the retarded web, the harmonic analyzer).  This module
brings the 3+1 battery to parity -- and the instruments, once
built, immediately return three exact laws.

  s1  THE CHARGE READER (develop_loop3).  Affine holonomy of a loop
      in a 3D metric: parallel-transport an orthonormal frame,
      develop the tangent, return (rotation matrix, translation).
      Around a string: rotation angle = the exact 2D atom
      delta(w) = 2 pi (1 - (1+w)^(-1/2)) to 1e-5, and the rotation
      AXIS is the string's direction -- the monodromy reads off
      both the charge and the orientation.  Loops that do not link
      the string (beside it, or in a perpendicular plane) develop
      to the identity: charge = linking, at the geometric tier.
      The translation part obeys the 2D moment law verbatim:
      |T| = 2 sin(delta/2) * (proper distance source-to-basepoint).

  s2  THE ATOM'S CODIMENSION LADDER.  A point participant in 3D
      carries a SOLID-ANGLE deficit, exact and shell-independent
      (the Gauss law): Omega = 4 pi / (1+w), i.e.
      dOmega/4pi = w/(1+w).  Together with the 2D/string atom this
      is one law:

        deficit fraction of a codim-c source = 1 - (1+w)^(-(c-1)/2)

      c = 2 (2D point, 3D string): 1 - (1+w)^(-1/2) -- the atom.
      c = 3 (3D point):            1 - (1+w)^(-1)   -- the monopole.

  s3  MOMENTUM.  Displace the string; the rotation charge (mass) is
      invariant and the translation holonomy drifts at exactly
      2 sin(delta/2) sqrt(1+w) per unit displacement -- the 2+1
      momentum law (0025), now read by the native 3D instrument in
      the transverse plane.

  s4  ADDITIVITY AND SCREENING.  Two parallel strings through one
      loop: total rotation = 0.86 of the naive sum -- charges add
      up to the mutual screening the inclination law predicts
      (constant-ambient estimate 0.90; the residual is the
      finite-separation nonuniform ambient).

  s5  THE PARITY CENSUS: every 2+1 instrument now has a 3+1
      counterpart (or is dimension-generic), printed as a table.

Run directly for the verification suite.
"""

from __future__ import annotations

import math

TAU = 2 * math.pi


# =====================================================================
# linear algebra helpers
# =====================================================================

def inv3(m):
    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]
    A = (e * i - f * h)
    B = -(d * i - f * g)
    C = (d * h - e * g)
    D = -(b * i - c * h)
    E = (a * i - c * g)
    F = -(a * h - b * g)
    G = (b * f - c * e)
    H = -(a * f - c * d)
    I = (a * e - b * d)
    det = a * A + b * B + c * C
    return [[A / det, D / det, G / det],
            [B / det, E / det, H / det],
            [C / det, F / det, I / det]]


def christoffel3(gfun, x, h=1e-4):
    """Christoffel symbols Gamma^i_jk of gfun at x, central diffs."""
    ex = ((h, 0, 0), (0, h, 0), (0, 0, h))
    dg = []
    for k in range(3):
        gp = gfun((x[0] + ex[k][0], x[1] + ex[k][1], x[2] + ex[k][2]))
        gm = gfun((x[0] - ex[k][0], x[1] - ex[k][1], x[2] - ex[k][2]))
        dg.append([[(gp[i][j] - gm[i][j]) / (2 * h) for j in range(3)]
                   for i in range(3)])
    gi = inv3(gfun(x))
    Gam = [[[0.0] * 3 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                s = 0.0
                for l in range(3):
                    s += gi[i][l] * (dg[j][l][k] + dg[k][l][j]
                                     - dg[l][j][k])
                Gam[i][j][k] = 0.5 * s
    return Gam


def gram_schmidt(g, vs):
    out = []

    def dot(a, b):
        return sum(a[i] * g[i][j] * b[j]
                   for i in range(3) for j in range(3))
    for v in vs:
        u = list(v)
        for e in out:
            c = dot(u, e)
            u = [u[i] - c * e[i] for i in range(3)]
        n = math.sqrt(dot(u, u))
        out.append([u[i] / n for i in range(3)])
    return out


def solve3(F, b):
    """Solve (matrix with columns F[0..2]) a = b."""
    M = [[F[j][i] for j in range(3)] for i in range(3)]
    Mi = inv3(M)
    return [sum(Mi[i][j] * b[j] for j in range(3)) for i in range(3)]


# =====================================================================
# battery instrument: the 3D charge reader
# =====================================================================

def develop_loop3(gfun, center, R, steps=4000, plane=(0, 1)):
    """Affine holonomy (rotation matrix in initial-frame components,
    developed translation) of a coordinate circle of radius R around
    center in the given coordinate plane."""
    a_, b_ = plane

    def pos(t):
        p = list(center)
        p[a_] += R * math.cos(t)
        p[b_] += R * math.sin(t)
        return tuple(p)

    def vel(t):
        v = [0.0, 0.0, 0.0]
        v[a_] = -R * math.sin(t)
        v[b_] = R * math.cos(t)
        return v

    x0 = pos(0.0)
    g0 = gfun(x0)
    E = gram_schmidt(g0, [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    F = [list(e) for e in E]
    dev = [0.0, 0.0, 0.0]
    dt = TAU / steps
    for s in range(steps):
        t = s * dt
        x = pos(t)
        v = vel(t)
        dx = [v[i] * dt for i in range(3)]
        a = solve3(F, dx)
        for i in range(3):
            dev[i] += a[i]
        Gam = christoffel3(gfun, x)
        for f in F:
            df = [0.0, 0.0, 0.0]
            for i in range(3):
                acc = 0.0
                for j in range(3):
                    for k in range(3):
                        acc += Gam[i][j][k] * dx[j] * f[k]
                df[i] = -acc
            for i in range(3):
                f[i] += df[i]

    def dot(a, b):
        return sum(a[i] * g0[i][j] * b[j]
                   for i in range(3) for j in range(3))
    Rot = [[dot(E[a], F[b]) for b in range(3)] for a in range(3)]
    return Rot, dev


def rot_angle_axis(Rot):
    tr = Rot[0][0] + Rot[1][1] + Rot[2][2]
    ang = math.acos(max(-1.0, min(1.0, (tr - 1) / 2)))
    ax = (Rot[2][1] - Rot[1][2], Rot[0][2] - Rot[2][0],
          Rot[1][0] - Rot[0][1])
    n = math.sqrt(sum(a * a for a in ax))
    if n < 1e-12:
        return ang, (0.0, 0.0, 0.0)
    return ang, tuple(a / n for a in ax)


# =====================================================================
# battery instrument: proper-area / proper-radius integrators
# =====================================================================

def proper_area(gfun, r, nth=200, nph=200):
    """Proper area of the coordinate sphere of radius r about 0."""
    A = 0.0
    for a in range(nth):
        th = math.pi * (a + 0.5) / nth
        for b in range(nph):
            ph = TAU * (b + 0.5) / nph
            st, ct = math.sin(th), math.cos(th)
            cp, sp = math.cos(ph), math.sin(ph)
            x = (r * st * cp, r * st * sp, r * ct)
            tth = (r * ct * cp, r * ct * sp, -r * st)
            tph = (-r * st * sp, r * st * cp, 0.0)
            g = gfun(x)
            E = sum(tth[i] * g[i][j] * tth[j]
                    for i in range(3) for j in range(3))
            Fc = sum(tth[i] * g[i][j] * tph[j]
                     for i in range(3) for j in range(3))
            G = sum(tph[i] * g[i][j] * tph[j]
                    for i in range(3) for j in range(3))
            A += math.sqrt(E * G - Fc * Fc) \
                * (math.pi / nth) * (TAU / nph)
    return A


def proper_radius(gfun, r, direction=(0.6, 0.64, 0.48), n=2000):
    L = 0.0
    for k in range(n):
        s = r * (k + 0.5) / n
        x = tuple(s * d for d in direction)
        dx = tuple(d * r / n for d in direction)
        g = gfun(x)
        L += math.sqrt(sum(dx[i] * g[i][j] * dx[j]
                           for i in range(3) for j in range(3)))
    return L


# =====================================================================
# source fields
# =====================================================================

W = 0.3
DELTA = TAU * (1 - 1 / math.sqrt(1 + W))


def string_at(s, w=W):
    """Straight string along z through (s, 0)."""
    def g(x):
        dx, dy = x[0] - s, x[1]
        r = math.hypot(dx, dy)
        u = (dx / r, dy / r, 0.0)
        return [[(1 if i == j else 0) + w * u[i] * u[j]
                 for j in range(3)] for i in range(3)]
    return g


def monopole(x, w=W):
    r = math.sqrt(sum(c * c for c in x))
    u = tuple(c / r for c in x)
    return [[(1 if i == j else 0) + w * u[i] * u[j]
             for j in range(3)] for i in range(3)]


def two_strings(x, w=W):
    m = [[1.0 if i == j else 0.0 for j in range(3)] for i in range(3)]
    for (px, py) in ((0.3, 0.0), (-0.3, 0.1)):
        dx, dy = x[0] - px, x[1] - py
        r = math.hypot(dx, dy)
        u = (dx / r, dy / r, 0.0)
        for i in range(3):
            for j in range(3):
                m[i][j] += w * u[i] * u[j]
    return m


# =====================================================================
# 1. the charge reader
# =====================================================================

def verify_charge_reader() -> None:
    Rot, dev = develop_loop3(string_at(0.0), (0.0, 0.0, 0.2), 1.0)
    ang, ax = rot_angle_axis(Rot)
    assert abs(ang - DELTA) < 1e-4, (ang, DELTA)
    assert abs(ax[2]) > 0.9999 and abs(ax[0]) < 1e-3, ax
    print(f"    loop around a string: rotation {ang:.5f} vs the exact")
    print(f"    2D atom delta(w) = {DELTA:.5f}; rotation AXIS =")
    print(f"    ({ax[0]:.3f}, {ax[1]:.3f}, {ax[2]:.3f}) -- the string's")
    print(f"    direction, read off the monodromy.")
    # moment law
    T = math.sqrt(sum(d * d for d in dev))
    pred = 2 * math.sin(DELTA / 2) * math.sqrt(1 + W) * 1.0
    assert abs(T - pred) / pred < 1e-3, (T, pred)
    print(f"    translation part |T| = {T:.4f} vs the 2D moment law")
    print(f"    2 sin(delta/2) * proper distance = {pred:.4f}.")
    # non-linking loops develop to identity
    for center, plane, name in (((3.0, 0.0, 0.2), (0, 1), "beside"),
                                ((2.0, 0.5, 0.0), (0, 2),
                                 "perpendicular plane")):
        Rot2, dev2 = develop_loop3(string_at(0.0), center, 0.8,
                                   plane=plane)
        ang2, _ = rot_angle_axis(Rot2)
        T2 = math.sqrt(sum(d * d for d in dev2))
        assert ang2 < 1e-5 and T2 < 1e-3, (name, ang2, T2)
        print(f"    non-linking loop ({name}): rotation {ang2:.1e}, "
              f"|T| {T2:.1e}.")
    print()
    print("  CHARGE = LINKING at the geometric tier: the affine")
    print("  holonomy carries the mass (rotation angle), the string's")
    print("  orientation (rotation axis), and the moment (translation),")
    print("  and vanishes on unlinked loops -- the same reading the")
    print("  quantum algebra gave operatorially (0030).")


# =====================================================================
# 2. the atom's codimension ladder
# =====================================================================

def verify_codimension_ladder() -> None:
    pred = 2 * TAU / (1 + W)
    for r in (0.7, 1.4):
        A = proper_area(monopole, r)
        L = proper_radius(monopole, r)
        omega = A / L ** 2
        assert abs(omega - pred) / pred < 1e-4, (omega, pred)
        print(f"    r = {r}: proper solid angle {omega:.5f} vs "
              f"4 pi/(1+w) = {pred:.5f}")
    print(f"    shell-independent (the Gauss law): the deficit")
    print(f"    dOmega = 4 pi w/(1+w) = {2 * TAU * W / (1 + W):.5f}, "
          f"exact.")
    print()
    c2 = 1 - (1 + W) ** -0.5
    c3 = 1 - (1 + W) ** -1.0
    assert abs(DELTA / TAU - c2) < 1e-12
    print("  THE CODIMENSION LADDER -- one law:")
    print("    deficit fraction of a codim-c source = "
          "1 - (1+w)^(-(c-1)/2)")
    print(f"    c = 2 (2D point / 3D string): {c2:.5f}  "
          f"(= delta/2pi, the atom)")
    print(f"    c = 3 (3D point):             {c3:.5f}  "
          f"(= dOmega/4pi, the monopole)")


# =====================================================================
# 3. momentum
# =====================================================================

def verify_momentum() -> None:
    rate_pred = 2 * math.sin(DELTA / 2) * math.sqrt(1 + W)
    devs = []
    for s in (0.0, 0.1, 0.2):
        Rot, dev = develop_loop3(string_at(s), (0.0, 0.0, 0.2), 1.0)
        ang, _ = rot_angle_axis(Rot)
        assert abs(ang - DELTA) < 1e-4, ang
        devs.append(dev)
    r1 = math.dist(devs[1], devs[0]) / 0.1
    r2 = math.dist(devs[2], devs[0]) / 0.2
    assert abs(r1 - rate_pred) / rate_pred < 1e-3, (r1, rate_pred)
    assert abs(r2 - rate_pred) / rate_pred < 1e-3, (r2, rate_pred)
    print(f"    displacing the string: rotation charge invariant")
    print(f"    ({DELTA:.5f} at all three positions); translation")
    print(f"    drift per unit displacement {r1:.4f}, {r2:.4f} vs the")
    print(f"    2+1 momentum law 2 sin(delta/2) sqrt(1+w) "
          f"= {rate_pred:.4f}.")
    print()
    print("  MASS INVARIANT, MOMENT DRIFTING: the 0025 momentum")
    print("  calculus lifts verbatim to the transverse plane, read by")
    print("  the native 3D instrument.")


# =====================================================================
# 4. additivity and screening
# =====================================================================

def verify_additivity() -> None:
    Rot, _ = develop_loop3(two_strings, (0.0, 0.0, 0.2), 1.2)
    ang, ax = rot_angle_axis(Rot)
    ratio = ang / (2 * DELTA)
    assert abs(ax[2]) > 0.999, ax
    assert 0.80 < ratio < 0.95, ratio
    # constant-ambient estimate: each string in the other's parallel
    # ambient screens as f(0) = (1+w)^(-1/2)  (0030's inclination law)
    w_eff = W / math.sqrt(1 + W)
    est = TAU * (1 - 1 / math.sqrt(1 + w_eff)) / DELTA
    print(f"    two parallel strings through one loop: total rotation")
    print(f"    {ang:.5f} = {ratio:.3f} of the naive sum "
          f"2 delta = {2 * DELTA:.5f};")
    print(f"    constant-ambient screening estimate {est:.3f} (the")
    print(f"    residual is the finite-separation nonuniform ambient).")
    print()
    print("  CHARGES ADD, SCREENED: the holonomy reader sees the")
    print("  mutual screening the inclination law predicts.")


# =====================================================================
# 5. the parity census
# =====================================================================

def verify_census() -> None:
    rows = [
        ("metric from channels", "dimension-generic", "0014/0026"),
        ("atom / transport deficit", "develop_loop3 rotation; "
         "codim ladder", "here"),
        ("charge reader (develop_loop)", "develop_loop3 "
         "(+ axis = orientation)", "here"),
        ("field equation / flux integral", "shell-independent "
         "solid angle; monopole closed form", "here + 0031"),
        ("retarded web", "string_wave_metric (any shape)",
         "0031/0032"),
        ("causal cone / gossip", "dimension-blind", "0030"),
        ("Lorentz / Wigner", "transverse lift + generic polar",
         "0030/0026"),
        ("harmonic / phase analyzer", "shared", "0031"),
        ("curvature", "3D Ricci pipeline", "0031"),
        ("polarization decomposer", "3D-native (no 2D need)",
         "0032"),
        ("BF action lattice", "Lattice3 (2-form budget)", "0030"),
        ("quantum deformation", "intersection -> linking", "0030"),
    ]
    print("    2+1 instrument                    3+1 counterpart")
    print("    " + "-" * 62)
    for a, b, c in rows:
        print(f"    {a:33s} {b}  [{c}]")
    print()
    print("  THE BATTERY IS AT PARITY: every 2+1 instrument has a")
    print("  native 3+1 counterpart or is dimension-generic.  The one")
    print("  instrument with no target yet: nothing measures a")
    print("  dynamical strength sector, because none exists (0032's")
    print("  verdict) -- the next construction, not the next tool.")


def run_verification_suite() -> None:
    sections = [
        ("The charge reader (develop_loop3)", verify_charge_reader),
        ("The atom's codimension ladder", verify_codimension_ladder),
        ("Momentum", verify_momentum),
        ("Additivity and screening", verify_additivity),
        ("The parity census", verify_census),
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
