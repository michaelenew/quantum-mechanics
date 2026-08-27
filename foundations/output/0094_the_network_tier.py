"""0094 -- the network tier: the lattice is a bank of S^3 filters,
and the dressed vacuum is its smoother.

The isomorphism so far is chain-shaped (one filter, one stream). The
physics object is a NETWORK: one S^3 state per link, one likelihood
factor per plaquette, each link serving six factors. This module
establishes the network tier quantitatively:

  s1  THE EXACT STATEMENT. The single-link conditional of the
      lattice measure is literally a Bayes update: Haar prior x six
      staple likelihoods W(angle(U S_i)) -- the heat-bath kernel IS
      the S^3 filter's update with six observations. (Stated; the
      formula is the measure's own factorization.)
  s2  THE GAUSSIAN SECTOR PREDICTS THE DRESSING, ZERO KNOBS. In the
      small-angle sector the bank is 0095's Maxwell theory (u = DA,
      D the lattice curl), i.e. a Gaussian smoother on the link
      graph. Its prediction for the dressed plaquette variance is
        <th^2> = 3 R / kappa(tau),
      kappa = -d^2 lnW_tau/dth^2 at the origin (the weight's local
      precision -- the filter's native object, NOT a matched
      moment), R = rank(D)/P the fraction of plaquette modes that
      are physical (curl) modes. Compared against 0092's measured
      primary curve across the flow.
  s3  THE GAUSSIAN-KINEMATIC BASELINE FOR THE SCALE FIELD. The same
      Gaussian bank, sampled exactly (SVD of D), scored with 0091's
      own observables (s_P vs shuffle, ln-rho spatial correlation):
      how much of the measured 'scale field' is pure link-sharing
      kinematics, and how much is interaction. A sharper control
      than 0101's shuffle -- and a revision of its reading where
      the numbers say so.
  s4  THE GAUGE QUOTIENT. The single-link marginal of the
      interacting measure is exactly Haar (verified on 0092's
      checkpoints when present): gauge orbits are the filter's
      unidentifiable nuisance directions, class functions the
      sufficient statistics; the physical content of the bank lives
      in ker(D)-orthogonal (curl) coordinates only.
"""

import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------
# lattice geometry and the abelianized curl D (L = 4)
# ----------------------------------------------------------------------

L = 4
V = L ** 4
P = 6 * V
COORD = np.array([[t, x, y, z] for t in range(L) for x in range(L)
                  for y in range(L) for z in range(L)])
SITES = np.arange(V)


def shift(s, mu, d=1):
    c = COORD[s].copy()
    c[:, mu] = (c[:, mu] + d) % L
    return c[:, 0] * L ** 3 + c[:, 1] * L ** 2 + c[:, 2] * L + c[:, 3]


PLANES = [(mu, nu) for mu in range(4) for nu in range(mu + 1, 4)]


def build_D():
    """Rows: plaquette (site-major, plane index as in 0091's
    all_plaq_thetas). Cols: link (mu, site).
    u_(s,munu) = a_mu(s) + a_nu(s+mu) - a_mu(s+nu) - a_nu(s)."""
    D = np.zeros((P, 4 * V))
    for ip, (mu, nu) in enumerate(PLANES):
        r = 6 * SITES + ip
        D[r, mu * V + SITES] += 1
        D[r, nu * V + shift(SITES, mu)] += 1
        D[r, mu * V + shift(SITES, nu)] -= 1
        D[r, nu * V + SITES] -= 1
    return D


# ----------------------------------------------------------------------
# the weight's local precision kappa(tau)
# ----------------------------------------------------------------------

JS = np.arange(0, 2.6, 0.5)
JALL = np.arange(0, 5.1, 0.5)


def char_coeffs():
    th = np.linspace(1e-9, np.pi - 1e-9, 400001)
    A = sum(np.sin((2 * j + 1) * th) / np.sin(th) for j in JS)
    W = A ** 2
    haar = (2 / np.pi) * np.sin(th) ** 2
    X = np.stack([np.sin((2 * j + 1) * th) / np.sin(th)
                  for j in JALL])
    return np.array([np.trapezoid(W * X[i] * haar, th)
                     for i in range(len(JALL))])


CCOEF = char_coeffs()


def kappa(tau):
    """-d^2 lnW_tau / dth^2 at 0, from the character expansion:
    chi_j(th) ~ n(1 - (n^2-1) th^2/6), n = 2j+1."""
    n = 2 * JALL + 1
    e = CCOEF * np.exp(-tau * JALL * (JALL + 1))
    W0 = float((e * n).sum())
    W2 = -float((e * n * (n ** 2 - 1) / 6).sum())
    return -2 * W2 / W0


# ----------------------------------------------------------------------
# s2 -- the Maxwell-smoother prediction of the dressed curve
# ----------------------------------------------------------------------

def measured_primary():
    """0092's measured primary flow curve at L = 4 (results.json when
    present; the committed values otherwise)."""
    path = os.path.join(HERE, "mc0092", "results.json")
    fallback = {0.0: 0.0968, 0.05: 0.1322, 0.15: 0.2125,
                0.3: 0.3494, 0.6: 0.6843, 1.2: 1.6074}
    if os.path.exists(path):
        res = {(r["L"], r["tau"], r["name"][-3:]): r
               for r in json.load(open(path))}
        out = {}
        for t in fallback:
            r = res.get((4, t, "ord")) or res.get((4, t, "dis"))
            out[t] = r["m2"] if r else fallback[t]
        return out
    return fallback


def s2_prediction(U_r):
    print("== s2: the Maxwell-smoother prediction (zero knobs) ==")
    R = U_r.shape[1] / P
    print(f"  curl rank: {U_r.shape[1]} of {P} plaquette modes "
          f"physical (R = {R:.4f});")
    print(f"  kernel dim {4 * V - U_r.shape[1]} = gauge {V - 1} + "
          f"global Wilson 4 + ...")
    meas = measured_primary()
    print("  tau   kappa   pred 3R/kappa   measured   pred/meas")
    ratios = {}
    for t in (0.0, 0.05, 0.15, 0.3, 0.6, 1.2):
        k = kappa(t)
        pred = 3 * R / k
        ratios[t] = pred / meas[t]
        print(f"  {t:.2f}  {k:6.3f}    {pred:.4f}       "
              f"{meas[t]:.4f}     {ratios[t]:.3f}")
    print("  the weight's local precision (the filter object) "
          "predicts the dressed curve;")
    print("  moment-matching the bare weight instead would give "
          f"{3 * R * 0.417 / 3:.3f} at tau = 0 -- wrong by "
          f"{3 * R * 0.417 / 3 / meas[0.0]:.1f}x")
    assert abs(ratios[0.0] - 1) < 0.20
    assert abs(ratios[0.15] - 1) < 0.20
    assert abs(ratios[0.3] - 1) < 0.20
    return ratios


# ----------------------------------------------------------------------
# s3 -- the Gaussian-kinematic baseline for the scale field
# ----------------------------------------------------------------------

def s3_baseline(U_r):
    print("== s3: the Gaussian bank, scored with 0091's "
          "observables ==")
    rng = np.random.default_rng(9)
    k0 = kappa(0.0)
    nsamp, r = 3000, U_r.shape[1]
    Ts = []
    for _ in range(3):                       # batch to bound memory
        z = rng.normal(size=(3, r, nsamp // 3))
        u = np.einsum("pr,crn->ncp", U_r, z) / np.sqrt(k0)
        Ts.append(np.linalg.norm(u, axis=1).reshape(-1, V, 6))
    T = np.concatenate(Ts)                   # (nsamp, V, 6) thetas
    th = T.ravel()
    m2 = (th ** 2).mean()
    kurt = 9 / 5 * (th ** 4).mean() / m2 ** 2
    lnr = np.log(np.sqrt((T ** 2).mean(axis=2)))
    sP = lnr.std(axis=1).mean()
    Tsh = T.copy()
    for i in range(len(Tsh)):
        flat = Tsh[i].ravel()
        rng.shuffle(flat)
        Tsh[i] = flat.reshape(V, 6)
    sPs = np.log(np.sqrt((Tsh ** 2).mean(axis=2))).std(axis=1).mean()
    x = lnr - lnr.mean(axis=1, keepdims=True)
    var = (x ** 2).mean()
    cors = []
    for d in (1, 2):
        num = sum((x * x[:, shift(SITES, mu, d)]).mean()
                  for mu in range(4))
        cors.append(num / 4 / var)
    print(f"  Gaussian bank: <th^2> = {m2:.4f}, kurt = {kurt:.2f}, "
          f"sP_exc = {sP - sPs:+.4f},")
    print(f"                 c(1) = {cors[0]:+.4f}, c(2) = "
          f"{cors[1]:+.4f}")
    print("  measured (0092, L4 tau=0):        sP_exc = +0.0120, "
          "c(1) = +0.0474, c(2) = -0.0046")
    return dict(m2=m2, kurt=kurt, exc=sP - sPs, c1=cors[0],
                c2=cors[1])


# ----------------------------------------------------------------------
# s4 -- the gauge quotient
# ----------------------------------------------------------------------

def s4_gauge():
    print("== s4: the gauge quotient -- link marginals are Haar ==")
    path = os.path.join(HERE, "mc0092", "L4_t0.00_ord_c0.npz")
    if not os.path.exists(path):
        print("  (no checkpoint present; statement stands on gauge "
              "invariance alone)\n")
        return
    links = np.load(path)["links"].astype(np.float64)
    w = links[:, :, 0].ravel()               # cos(theta/2) of links
    print(f"  link w-component over {len(w)} links: <w> = "
          f"{w.mean():+.4f} (Haar: 0), <w^2> = {w.mean() ** 2 + w.var():.4f} "
          f"(Haar: 0.25)")
    assert abs(w.mean()) < 0.05 and abs(w.var() + w.mean()**2 - 0.25) < 0.01
    print("  the interacting measure's single-link marginal is Haar: "
          "a link coordinate is")
    print("  pure nuisance; identifiable content = class functions "
          "of loops (image of D)\n")


if __name__ == "__main__":
    print("== s1: the exact statement ==")
    print("  p(U | rest) prop_to Haar(U) x prod_{i=1..6} "
          "W_tau(angle(U S_i)):")
    print("  the heat-bath kernel is a Bayes update -- Haar prior, "
          "six staple observations.")
    print("  (The measure's own factorization; the network is a "
          "bank of S^3 filters.)\n")
    D = build_D()
    Um, sv, _ = np.linalg.svd(D, full_matrices=False)
    U_r = np.ascontiguousarray(Um[:, sv > 1e-8])
    s2_prediction(U_r)
    print()
    s3_baseline(U_r)
    print()
    s4_gauge()
    print("all assertions passed")
