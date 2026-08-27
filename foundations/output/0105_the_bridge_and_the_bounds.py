"""0105 -- the bridge closed, which bound binds, and the
ratio-record audit.

Three residuals, run together.

  s1  THE BRIDGE. 0114 found the first law requires alpha = pi in
      the completion's units and called the gap to 0082's measured
      alpha a debt for the kappa normalization to supply. Reading
      0082 properly (its alpha = 0.0242 is PER SCALAR POLARIZATION;
      the graviton carries two) closes it:
        (a) the completion's own Newton constant is G = 1/(4 pi)
            (since lambda = M/(4 pi r) is Phi = G M / r), and
            S = A/(4G) is then exactly alpha = pi -- so the
            requirement was never a coincidence: THE COMPLETION
            SATISFIES BEKENSTEIN-HAWKING WITH THE 1/4, not merely
            the shape;
        (b) equating the horizon entropy with the measured VACUUM
            ENTANGLEMENT entropy -- this program's own C4 question
            (0082's framing note) -- fixes the lattice Newton
            constant: G = 1/(4 * 2 alpha_scalar) = 5.17 a^2, i.e.
            a Planck length of 2.27 lattice spacings;
        (c) the residual structural factor: the completion is a
            SCALAR theory, so its horizon sits at r_h = G M, half
            the Schwarzschild radius -- a factor 2 in radius, 4 in
            area and temperature, expected and named.
  s2  WHICH BOUND BINDS. Two caps on a region's mass: the
      information bound (each node carries mass < 1: M < n_nodes)
      and the geometric bound (M <= capacitance ~ 4 pi R). They
      cross at R ~ sqrt(3) lattice spacings: below it information
      saturation binds, above it geometry does. Gravity's bound is
      geometric for anything bigger than about two lattice
      spacings.
  s3  THE RATIO-RECORD AUDIT. The derived-gravity chain (lucid
      0019) assumes spatial records are RATIO-valued. Audited on
      this program's own lattice: the power spectrum of the site
      log-scale field is measured at k = 0 against k != 0. If the
      zero mode were soft, absolute scale would be unidentifiable
      (ratio records exactly). It is not: the measure pins the
      absolute scale. The honest form of the premise is therefore
      the DEVIATION form -- records of departures from the pinned
      vacuum are difference-valued -- which is exactly how 0019
      built it (lambda = 0 vacuum). Recorded as a correction to the
      premise's statement, not to its use.
"""

import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

ALPHA_SCALAR = 0.0242          # 0082, per polarization
POL = 2                        # graviton TT polarizations


def s1_bridge():
    print("== s1: the bridge ==")
    G_c = 1 / (4 * np.pi)
    print(f"  (a) completion's own Newton constant: lambda = "
          f"M/(4 pi r) = G M/r  ->  G = {G_c:.5f}")
    alpha_bh = 1 / (4 * G_c)
    print(f"      Bekenstein-Hawking at that G: S = A/(4G)  ->  "
          f"alpha = {alpha_bh:.5f} = pi")
    assert abs(alpha_bh - np.pi) < 1e-12
    print("      the first law's requirement alpha = pi IS S = "
          "A/(4G): the completion")
    print("      satisfies Bekenstein-Hawking WITH THE 1/4, not "
          "just the shape")
    alpha_tot = POL * ALPHA_SCALAR
    G_ind = 1 / (4 * alpha_tot)
    print(f"  (b) induced-gravity closure (C4's question): equate "
          f"the horizon entropy with")
    print(f"      the measured vacuum entanglement entropy, "
          f"alpha_total = {POL} x {ALPHA_SCALAR} = {alpha_tot:.4f}:")
    print(f"      1/(4G) = alpha_total  ->  G = {G_ind:.3f} a^2, "
          f"Planck length = {np.sqrt(G_ind):.3f} a")
    assert abs(G_ind - 5.165) < 0.01
    print(f"  (c) structural residue: the completion is SCALAR, so "
          f"r_h = G M -- half the")
    print(f"      Schwarzschild radius; factor 2 in radius, 4 in "
          f"area and temperature.")
    print(f"      Bridge bookkeeping: pi/alpha_scalar = "
          f"{np.pi / ALPHA_SCALAR:.1f} = {POL} (polarizations) x "
          f"{np.pi / alpha_tot:.1f} (G ratio)")
    assert abs((np.pi / ALPHA_SCALAR) / (POL * (np.pi / alpha_tot))
               - 1) < 1e-9
    print("      -> the kappa-normalization debt is closed "
          "CONDITIONALLY on the induced-")
    print("      gravity identification, and it makes a testable "
          "prediction: the lattice")
    print(f"      Planck length is {np.sqrt(G_ind):.2f} spacings\n")
    return G_ind


def lap(f):
    out = -6.0 * f
    for ax in range(3):
        out += np.roll(f, 1, ax) + np.roll(f, -1, ax)
    return out


def s2_bounds():
    print("== s2: which bound binds ==")
    N = 40
    C0 = N // 2
    BND = np.zeros((N, N, N), bool)
    for ax in range(3):
        i = [slice(None)] * 3
        i[ax] = 0
        BND[tuple(i)] = True
        i[ax] = N - 1
        BND[tuple(i)] = True
    g = np.zeros((N, N, N))
    src = np.zeros((N, N, N))
    src[C0, C0, C0] = 1.0
    for _ in range(9000):
        g = g + 0.16 * (lap(g) + src)
        g[BND] = 0.0
    print("    R     n_nodes   info bound   capacitance   binds")
    for R in (1.0, 1.5, 2.0, 3.0, 4.0):
        sites = [(dx, dy, dz)
                 for dx in range(-6, 7) for dy in range(-6, 7)
                 for dz in range(-6, 7)
                 if dx * dx + dy * dy + dz * dz <= R * R]
        n = len(sites)
        Gm = np.array([[g[C0 + a[0] - b[0], C0 + a[1] - b[1],
                          C0 + a[2] - b[2]] for b in sites]
                       for a in sites])
        cap = float(np.ones(n) @ np.linalg.solve(Gm, np.ones(n)))
        which = "information" if n < cap else "geometry"
        print(f"   {R:.1f}    {n:6d}    {float(n):9.2f}    "
              f"{cap:9.2f}     {which}")
    print("  the two caps cross near R ~ sqrt(3) ~ 1.7 spacings "
          "(n ~ (4/3) pi R^3 vs")
    print("  C ~ 4 pi R): below it a body is limited by how much "
          "information its nodes can")
    print("  hold; above it by its own geometry. Gravity's bound is "
          "geometric for anything")
    print("  larger than about two lattice spacings\n")


def s3_ratio_audit():
    print("== s3: the ratio-record audit ==")
    spec = importlib.util.spec_from_file_location(
        "m92", os.path.join(HERE, "0092_the_coupling_scan.py"))
    m92 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m92)
    lat = m92.mklat(4)
    V = lat["V"]
    tab = m92.lnw_table(0.0)
    p0, pk = [], []
    for k in range(4):
        rs = m92.seed_state(61000 + k)
        links = np.ascontiguousarray(
            np.tile([1.0, 0, 0, 0], (4, V, 1)))
        m92.c_sweeps(links, lat, 5, 1.5, tab, rs)
        means = []
        fields = []
        done = 0
        while done < 4000:
            m92.c_sweeps(links, lat, 5, 0.5, tab, rs)
            done += 5
            if done <= 800:
                continue
            th = m92.all_plaq_thetas(links, lat)
            lnr = np.log(np.sqrt((th ** 2).mean(axis=1)))
            means.append(float(lnr.mean()))
            fields.append(lnr - lnr.mean())
        F = np.array(fields)
        p0.append(np.var(means) * V)          # zero-mode power
        pk.append(float((F ** 2).mean()))     # per-site nonzero
    p0 = float(np.mean(p0))
    pk = float(np.mean(pk))
    print(f"  site log-scale field: zero-mode power {p0:.4f} vs "
          f"non-zero-mode power {pk:.4f}")
    print(f"  ratio P(0)/P(k != 0) = {p0 / pk:.3f}")
    assert p0 / pk < 3.0
    print("  NO soft zero mode: the derived measure PINS the "
          "absolute scale, so lattice")
    print("  records are not ratio-valued in the naive sense. The "
          "honest form of the")
    print("  premise is the DEVIATION form -- records of departures "
          "from the pinned vacuum")
    print("  are difference-valued -- which is exactly how the "
          "derivation used it (lambda = 0")
    print("  vacuum, differences only). A correction to the "
          "premise's statement, not to")
    print("  its use\n")


if __name__ == "__main__":
    s1_bridge()
    s2_bounds()
    s3_ratio_audit()
    print("all assertions passed")
