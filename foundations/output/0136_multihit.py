"""0136 -- multihit: stop sampling what can be integrated.

lucid 0048 identified the item-2 blocker as an ESTIMATION problem,
not a physics one: the naive estimator carries the fluctuation of
every link in a long composite operator, and none of that
fluctuation carries the long-distance signal. The fix is
Rao-Blackwell -- replace each sampled link by its conditional mean
given the rest -- and the gain is a RATIO OF PRODUCT VARIANCES,
[(1+v)^2k - 1]/[(1+v)^2(k-j) - 1], which is large even for stiff
links because it comes from the operator's LENGTH.

For a table-valued weight the conditional mean has no closed form
(the six plaquettes touching a link do not combine into one
effective staple the way a Wilson action's do), so it is estimated
the original way: M extra local Metropolis hits on that link alone,
averaged. That is unbiased for the conditional mean of the LINK.

  s1  THE MULTIHIT ESTIMATOR, and the honest caveat: the site
      operator's six plaquettes share links, so replacing a link by
      its conditional mean is exact for a single plaquette and
      approximate for the product. The bias is therefore MEASURED,
      not assumed.
  s2  VARIANCE AND BIAS, side by side against the plain estimator
      at matched statistics.
  s3  THE VERDICT.
"""

import importlib.util
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, tag):
    s = importlib.util.spec_from_file_location(
        tag, os.path.join(HERE, name))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


K = _load("0134_the_spin4_kernel.py", "k134")
M = K.M132
L = 8
rng = np.random.default_rng(136)


def local_hits(Up, Um, lat, sigma, nhit):
    """For each (direction, parity) class in turn: hold everything
    else fixed, run `nhit` local Metropolis hits on that class, and
    average the link. Returns conditional-mean link arrays."""
    Ap = [u.copy() for u in Up]
    Am = [u.copy() for u in Um]
    for mu in range(4):
        for par in (0, 1):
            m = lat["par"] == par
            accP = np.zeros_like(Up[mu][m])
            accM = np.zeros_like(Um[mu][m])
            cp = [u.copy() for u in Up]
            cm = [u.copy() for u in Um]
            for _ in range(nhit):
                ap = M.plaq_angles(cp, lat, mu, cp[mu])[m]
                am = M.plaq_angles(cm, lat, mu, cm[mu])[m]
                old = M.lookup(ap, am).sum(-1)
                npp = M.qmul(M.qrand(cp[mu][m].shape[:-1], sigma),
                             cp[mu][m])
                nmm = M.qmul(M.qrand(cm[mu][m].shape[:-1], sigma),
                             cm[mu][m])
                Pp, Pm = cp[mu].copy(), cm[mu].copy()
                Pp[m], Pm[m] = npp, nmm
                c2p, c2m = list(cp), list(cm)
                c2p[mu], c2m[mu] = Pp, Pm
                new = M.lookup(M.plaq_angles(c2p, lat, mu, Pp)[m],
                               M.plaq_angles(c2m, lat, mu, Pm)[m]
                               ).sum(-1)
                take = np.log(rng.random(new.shape) + 1e-300) < (
                    new - old)
                cp[mu][m] = np.where(take[:, None], npp, cp[mu][m])
                cm[mu][m] = np.where(take[:, None], nmm, cm[mu][m])
                accP += cp[mu][m]
                accM += cm[mu][m]
            Ap[mu][m] = accP / nhit
            Am[mu][m] = accM / nhit
    return Ap, Am


def site_spin2(Up, Um, lat):
    qp, qm = M.all_plaq(Up, lat), M.all_plaq(Um, lat)
    Bp, Bm = qp[..., 1:], qm[..., 1:]
    outer = np.einsum("vpi,vpj->vpij", Bp, Bm)
    tr = np.einsum("vpii->vp", outer)
    sym = 0.5 * (outer + np.swapaxes(outer, -1, -2))
    s0 = sym - (tr / 3)[..., None, None] * np.eye(3)
    return s0.mean(1).reshape((L,) * 4 + (3, 3))


def corr(T):
    acc = None
    for a in range(3):
        for b in range(3):
            f = T[..., a, b]
            c = np.real(np.fft.ifftn(
                np.abs(np.fft.fftn(f - f.mean())) ** 2)) / f.size
            acc = c if acc is None else acc + c
    return acc


def collect(nconf=400, nhit=12, every=10):
    lat, up, dn = K.lat_arrays(L)
    V = lat["V"]
    lp, lm = K.fresh(L)
    rs = K.seed(4242)
    sig = 0.08
    for s in range(700):
        a, t = K.csweeps(lp, lm, up, dn, V, 1, sig, rs)
        if s < 400:
            r = a / max(t, 1)
            sig *= 1.06 if r > 0.45 else (0.94 if r < 0.35 else 1)
            sig = float(np.clip(sig, 0.005, 1.0))
    plain, mh = [], []
    t0 = time.time()
    for i in range(nconf):
        K.csweeps(lp, lm, up, dn, V, every, sig, rs)
        Up, Um = K.as_links(lp, V), K.as_links(lm, V)
        plain.append(corr(site_spin2(Up, Um, lat)))
        Ap, Am = local_hits(Up, Um, lat, sig, nhit)
        mh.append(corr(site_spin2(Ap, Am, lat)))
    return (np.array(plain), np.array(mh), sig,
            time.time() - t0)


def s1_s2_s3():
    print("== multihit against the plain estimator ==")
    plain, mh, sig, secs = collect()
    n = len(plain)
    print(f"  L = {L}, {n} configurations, 12 hits per link, "
          f"{secs:.0f}s")
    print(f"  (the multihit pass costs ~"
          f"{secs / n:.2f}s per configuration)")
    rr = np.arange(1, L // 2 + 1)
    print()
    print("     r      plain: mean +- se        multihit: mean "
          "+- se      var ratio")
    ratios = []
    for r in rr:
        p = plain[:, r, 0, 0, 0] / np.abs(plain[:, 0, 0, 0, 0])
        q = mh[:, r, 0, 0, 0] / np.abs(mh[:, 0, 0, 0, 0])
        sp, sq = p.std() / np.sqrt(n), q.std() / np.sqrt(n)
        ratios.append((p.std() / q.std()) ** 2)
        print(f"    {r:2d}   {p.mean():+.6f} +- {sp:.6f}    "
              f"{q.mean():+.6f} +- {sq:.6f}    "
              f"{ratios[-1]:6.2f}x")
    print()
    print(f"  variance reduction: {np.mean(ratios):.2f}x on "
          f"average, best {max(ratios):.2f}x")
    print()
    print("  BIAS CHECK. The six plaquettes at a site share links, "
          "so replacing a link by")
    print("  its conditional mean is exact for one plaquette and "
          "approximate for their")
    print("  product. If the two estimators disagree by more than "
          "their errors, the")
    print("  multihit estimate is biased and cannot be used as it "
          "stands:")
    worst = 0.0
    for r in rr:
        p = plain[:, r, 0, 0, 0] / np.abs(plain[:, 0, 0, 0, 0])
        q = mh[:, r, 0, 0, 0] / np.abs(mh[:, 0, 0, 0, 0])
        se = np.sqrt((p.std() ** 2 + q.std() ** 2) / n)
        z = abs(p.mean() - q.mean()) / max(se, 1e-15)
        worst = max(worst, z)
        print(f"    r = {r}:  difference "
              f"{p.mean() - q.mean():+.6f}, {z:.1f} sigma")
    print()
    if worst < 3 and np.mean(ratios) > 1.5:
        print("  UNBIASED AND CHEAPER: the estimators agree within "
              "errors and multihit has")
        print("  the smaller variance. The fix works and item 2 "
              "should be re-run with it.")
    elif np.mean(ratios) > 1.5:
        print(f"  VARIANCE DOWN BUT BIASED ({worst:.1f} sigma). "
              f"Shared links inside the site")
        print("  operator break exactness, as flagged. The fix is "
              "to integrate only links")
        print("  that appear in ONE measured plaquette -- a "
          "checkerboard over plaquette")
        print("  orientations -- which is a build, not a rerun.")
    else:
        print("  NO USEFUL VARIANCE REDUCTION. Recorded as "
              "measured: for this operator at")
        print("  this coupling, conditional-mean substitution does "
              "not buy enough, and")
        print("  lucid 0048's length argument does not carry over "
              "as hoped.")
    print()
    return float(np.mean(ratios)), worst


if __name__ == "__main__":
    s1_s2_s3()
