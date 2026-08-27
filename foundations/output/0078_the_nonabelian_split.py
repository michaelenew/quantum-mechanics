"""0078 -- the nonabelian split: how the polar theorem lifts to SU(2).

0086's polar theorem (abelian, exact): <W> = e^{i delta_source} * f^A.
SU(2) characters are real, so the phase cannot lift as a phase. It
lifts as a CHARACTER-INDEXED FACTORIZATION -- the bridge stone from
the Z_N toy back toward the full theory, on the 2D rung with the
program's own Born counting weight W = A^2, A = sum_{j<=2} chi_j
(0074's counting amplitude, flat n_j).

  s1  The transfer spectrum is fusion arithmetic: the per-plaquette
      transfer coefficient r_j = c_j / (d_j c_0) with c_j the FUSION
      COUNT #{(m,m') in counting^2 : m x m' contains j}. For the flat
      counting to j = 2: r = 1, 4/5, 2/3, 1/2, 9/25, 1/5 -- exact
      rationals, quadrature vs counting at 1e-8.
  s2  The factorization (2D gluing, standard convolution identity
      int chi_k(g h0^-1) chi_j(g) dg = delta_jk chi_j(h0)/d_j):
        <chi_j(loop)> = d_j * chi_j(h0)/d_j * r_j^A
      source factor chi_j(h0)/d_j and record envelope r_j^A, exactly
      separated, rep by rep. THE READING THEOREM: the ratio
      <chi_j>(A, h0) / <chi_j>(A, e) = chi_j(h0)/d_j at EVERY A --
      the record damps the signal but cannot distort the reading.
  s3  No-sleight check: link-level Monte Carlo on an explicit
      2-plaquette open lattice (7 Haar SU(2) links as quaternions, no
      gauge fixing, weight reweighting): vacuum <chi_j> = d_j r_j^2
      and the frustrated readings match chi_j(h0)/d_j within MC error
      bars; the class angle theta0 reconstructed from the j = 1/2
      reading agrees between A = 1 (algebra) and A = 2 (MC).
  s4  The phase ledger proper is the CENTER Z_2: a center twist reads
      (-1)^{2j} exactly -- the only true phases SU(2) affords
      ('t Hooft sector). Integer-j probes are center-blind: the
      graviton channel (1,1) reads geometry (class angles) and never
      the Z_2 flux; half-integer (fermionic) probes read both.

The two ledgers, nonabelian form: source ledger = a SPECTRUM of
readings chi_j(h0)/d_j (the class angle recovered by rep scan),
record ledger = the damping envelope r_j^A. The abelian polar theorem
is the special case where every character is a phase. 4D status:
the split is a property of ledger measure + 2D character gluing; the
4D theory shares the measure, and testing the split on one 0078-style
vertex is the open bridge item.
"""

import numpy as np

JS = [0, 0.5, 1, 1.5, 2]                 # the flat counting amplitude
D = {j: int(2 * j + 1) for j in
     (0, 0.5, 1, 1.5, 2, 2.5)}


def chi(j, th):
    th = np.asarray(th, dtype=float)
    s = np.sin(th)
    return np.where(np.abs(s) < 1e-12, 2 * j + 1,
                    np.sin((2 * j + 1) * th) / np.where(
                        np.abs(s) < 1e-12, 1.0, s))


def Wled(th):
    return sum(chi(j, th) for j in JS) ** 2


TH = np.linspace(1e-6, np.pi - 1e-6, 40001)
MEAS = (2 / np.pi) * np.sin(TH) ** 2


def cint(vals):
    return float(np.trapezoid(vals * MEAS, TH))


def fusion_count(j):
    tot = 0
    for m in JS:
        for mp in JS:
            if abs(m - mp) <= j <= m + mp \
                    and abs((j + m + mp) - round(j + m + mp)) < 1e-9:
                tot += 1
    return tot


def s1_transfer_spectrum():
    print("== s1: the transfer spectrum is fusion arithmetic ==")
    Z = cint(Wled(TH))
    c0 = fusion_count(0)
    rs = {}
    for j in (0, 0.5, 1, 1.5, 2, 2.5):
        r_quad = cint(Wled(TH) * chi(j, TH)) / (D[j] * Z)
        r_fus = fusion_count(j) / (D[j] * c0)
        assert abs(r_quad - r_fus) < 1e-8, (j, r_quad, r_fus)
        rs[j] = r_fus
        print(f"  j={j}: r_j = {fusion_count(j)}/{D[j] * c0} = "
              f"{r_fus:.4f}  (quadrature agrees to 1e-8)")
    assert abs(rs[0.5] - 0.8) < 1e-12 and abs(rs[1] - 2 / 3) < 1e-12
    print("  exact rationals -- the record envelope is counting "
          "arithmetic, the Born weight's fusion table\n")
    return rs


def s2_factorization(rs):
    print("== s2: the factorization and the reading theorem ==")
    th0 = 0.9
    for A in (1, 2, 4, 8):
        for j in (0.5, 1, 2):
            vac = D[j] * rs[j] ** A
            frs = D[j] * (chi(j, th0) / D[j]) * rs[j] ** A
            assert abs(frs / vac - chi(j, th0) / D[j]) < 1e-14
        print(f"  A={A}: reading <chi_j>(h0)/<chi_j>(e) = "
              f"chi_j(th0)/d_j for all j (exact)")
    print("  the record damps (r_j^A) but never distorts the source "
          "reading -- at any area.")
    print("  (rests on the standard convolution identity "
          "int chi_k(g h0^-1) chi_j(g) dg = d_jk chi_j(h0)/d_j;")
    print("   the MC below validates the whole pipeline with no "
          "gauge fixing)\n")


def _haar(rng, n):
    q = rng.normal(size=(n, 4))
    return q / np.linalg.norm(q, axis=1, keepdims=True)


def _qmul(a, b):
    w1, x1, y1, z1 = a.T
    w2, x2, y2, z2 = b.T
    return np.stack([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
                     w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
                     w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2], axis=1)


def _qinv(a):
    b = a.copy()
    b[:, 1:] *= -1
    return b


def _angle(q):
    return np.arccos(np.clip(q[:, 0], -1, 1))


def s3_link_mc(rs):
    print("== s3: link-level MC, 2-plaquette open lattice, no gauge "
          "fixing ==")
    rng = np.random.default_rng(7)
    NMC = 2_000_000
    ls = [_haar(rng, NMC) for _ in range(7)]
    h00, h10, h01, h11, v00, v10, v20 = ls
    U1 = _qmul(_qinv(v00), _qmul(_qinv(h01), _qmul(v10, h00)))
    U2 = _qmul(_qinv(v10), _qmul(_qinv(h11), _qmul(v20, h10)))
    Ub = _qmul(_qinv(v00), _qmul(_qinv(h01), _qmul(_qinv(h11),
               _qmul(v20, _qmul(h10, h00)))))
    th0 = 0.9
    h0i = _qinv(np.array([[np.cos(th0), np.sin(th0), 0, 0]]))
    aU1, aU2, aUb = _angle(U1), _angle(U2), _angle(Ub)
    a1f = _angle(_qmul(U1, np.broadcast_to(h0i, (NMC, 4))))
    wv = Wled(aU1) * Wled(aU2)
    wf = Wled(a1f) * Wled(aU2)

    def batch_est(w, obs, nb=20):
        wb = w.reshape(nb, -1)
        ob = obs.reshape(nb, -1)
        vals = (wb * ob).mean(axis=1) / wb.mean(axis=1)
        return vals.mean(), vals.std() / np.sqrt(nb)

    for j in (0.5, 1, 2):
        est, err = batch_est(wv, chi(j, aUb))
        pred = D[j] * rs[j] ** 2
        assert abs(est - pred) < max(4 * err, 0.02 * abs(pred) + 1e-3)
        print(f"  vacuum <chi_{j}> = {est:+.4f} +- {err:.4f}  vs "
              f"d_j r_j^2 = {pred:+.4f}")
    readings = {}
    for j in (0.5, 1, 2):
        est, err = batch_est(wf, chi(j, aUb))
        vac = D[j] * rs[j] ** 2
        readings[j] = est / vac
        pred = chi(j, th0) / D[j]
        assert abs(est / vac - pred) < max(4 * err / vac, 0.03)
        print(f"  frustrated reading j={j}: {est / vac:+.4f}  vs "
              f"chi_j(th0)/d_j = {pred:+.4f}")
    # reconstruct theta0 from the j=1/2 reading at A=2 (MC)
    grid = np.linspace(0.01, np.pi - 0.01, 200001)
    curve = chi(0.5, grid) / 2
    th_hat = float(grid[np.argmin(np.abs(curve - readings[0.5]))])
    print(f"  theta0 reconstructed from A=2 MC: {th_hat:.4f}  "
          f"(true {th0})")
    assert abs(th_hat - th0) < 0.03
    print("  the source is read exactly through the record, with "
          "gauge fully integrated\n")


def s4_center(rs):
    print("== s4: the phase ledger proper is the center Z_2 ==")
    # center twist: W(-g); character algebra: r_j -> (-1)^{2j} r_j
    Z = cint(Wled(np.pi - TH))
    for j in (0.5, 1, 1.5, 2):
        r_tw = cint(Wled(np.pi - TH) * chi(j, TH)) / (D[j] * Z)
        assert abs(r_tw - (-1) ** int(2 * j) * rs[j]) < 1e-8
    print("  center twist: r_j -> (-1)^{2j} r_j exactly -- sign "
          "factorization, modulus untouched")
    print("  integer j (the graviton channel (1,1) among them) is "
          "center-blind: gravity reads class")
    print("  angles, never the 't Hooft flux; half-integer probes "
          "read both. SU(2)'s only true")
    print("  phases are these signs -- the abelian polar phase "
          "shrinks to Z_2, and the continuous")
    print("  deficit migrates into the reading spectrum "
          "chi_j(th0)/d_j\n")


if __name__ == "__main__":
    rs = s1_transfer_spectrum()
    s2_factorization(rs)
    s3_link_mc(rs)
    s4_center(rs)
    print("all assertions passed")
