"""0128 -- the double slit, built from the derived measure.

North-star target 2. Not a toy of quantum mechanics bolted on: every
object below is computed from this program's own weight, and the
Hamiltonian is reconstructed rather than posited.

THE CHAIN, all of it already proved:
  - the derived weight W = A^2 on SU(2), A a counting amplitude;
  - its character coefficients w_j are all >= 0, so the transfer
    operator (convolution by W, eigenvalue w_j/d_j on the chi_j
    eigenspace) is POSITIVE -- 0111/0123, reflection positivity;
  - a positive transfer operator is exp(-H) for a real self-adjoint
    H, which is the Osterwalder-Schrader reconstruction: a Hilbert
    space and a UNITARY real-time evolution exp(-i H t);
  - amplitudes compose by complex multiplication and alternatives
    are SUMMED (lucid 0034, 0114) -- so a two-path experiment is a
    sum of amplitudes, squared.

Nothing is added here. The experiment is assembled from those.

  s1  THE DERIVED HAMILTONIAN. Character coefficients of the
      program's own weight, the transfer spectrum w_j/d_j, and
      E_j = -ln(w_j/d_j). And a consequence worth stating on its
      own: the weight is BAND-LIMITED, so w_j = 0 above the band
      and those modes have infinite energy. THE RECONSTRUCTED
      HILBERT SPACE IS FINITE DIMENSIONAL, with dimension equal to
      the band -- 11 for the N = 5 stack.
  s2  THE TWO SLITS. Two localised states on the group manifold,
      evolved by exp(-i H t) in the derived spectrum.
  s3  THE FRINGE. The coherent prediction against the incoherent
      one, scored in this program's own currency (nats), plus the
      control that makes it a measurement rather than a picture:
      destroy the relative phase and the fringe must vanish.
"""

import numpy as np

TH = np.linspace(1e-9, np.pi - 1e-9, 6001)
HAAR = (2 / np.pi) * np.sin(TH) ** 2
JS = range(1, 7)                       # the N = 5 stack: chi_1..chi_6


def chi(n):
    return np.sin(n * TH) / np.sin(TH)


def coef(f, n):
    return float(np.trapezoid(f * chi(n) * HAAR, TH))


def derived_spectrum():
    A = sum(chi(n) for n in JS)
    W = A ** 2
    ws, ns = [], []
    for n in range(1, 20):
        w = coef(W, n)
        if w > 1e-9:
            ws.append(w)
            ns.append(n)
    lam = np.array(ws) / np.array(ns, float)      # w_j / d_j
    E = -np.log(lam / lam.max())
    return np.array(ns), np.array(ws), lam, E


def s1_hamiltonian():
    print("== s1: the derived Hamiltonian ==")
    ns, ws, lam, E = derived_spectrum()
    print("     n    w_n (char coeff)   w_n/d_n   E_n = -ln(w/d)")
    for n, w, l, e in zip(ns, ws, lam, E):
        print(f"    {n:3d}   {w:10.4f}        {l:8.4f}   {e:8.4f}")
    print(f"  band = {ns[-1]}, and w_n = 0 above it -- those modes "
          f"have infinite energy.")
    print(f"  THE RECONSTRUCTED HILBERT SPACE IS FINITE "
          f"DIMENSIONAL: dim = {len(ns)}.")
    print("  That is not an approximation. It is the band-limit "
          "(0108's budget) showing up")
    print("  as the dimension of the state space\n")
    assert len(ns) == 11 and np.all(np.diff(E) > 0)
    return ns, E


def project(psi, ns):
    return np.array([coef(psi, n) for n in ns], dtype=complex)


def reconstruct(c, ns):
    return sum(ci * chi(n) for ci, n in zip(c, ns))


def bump(theta0, width=0.16):
    return np.exp(-((TH - theta0) ** 2) / (2 * width ** 2))


def s2_slits(ns, E, t=2.6):
    print("== s2: the two slits ==")
    a, b = bump(1.05), bump(2.05)
    ca, cb = project(a, ns), project(b, ns)
    ph = np.exp(-1j * E * t)
    pa = reconstruct(ca * ph, ns)
    pb = reconstruct(cb * ph, ns)
    print(f"  two localised states on the group manifold at theta = "
          f"1.05 and 2.05,")
    print(f"  evolved to t = {t} by exp(-i H t) in the derived "
          f"spectrum.")
    print(f"  norms after evolution: |A| = "
          f"{np.trapezoid(np.abs(pa) ** 2 * HAAR, TH):.4f}, "
          f"|B| = {np.trapezoid(np.abs(pb) ** 2 * HAAR, TH):.4f}")
    return pa, pb


def dens(p):
    """probability density of an amplitude, normalised on Haar"""
    d = np.abs(p) ** 2
    return d / np.trapezoid(d * HAAR, TH)


def dens_of(d):
    """normalise an already-squared density"""
    return d / np.trapezoid(d * HAAR, TH)


def s3_fringe(pa, pb):
    print("\n== s3: the fringe ==")
    coh = dens(pa + pb)
    inc = dens_of(np.abs(pa) ** 2 + np.abs(pb) ** 2)
    diff = coh - inc
    vis = float(np.abs(diff).max() / coh.max())
    print(f"  coherent |psi_A + psi_B|^2 against incoherent "
          f"|psi_A|^2 + |psi_B|^2:")
    print(f"    max fractional difference (visibility): {vis:.4f}")
    # count the fringes: sign changes of the difference
    sgn = np.sign(diff[np.abs(diff) > 0.02 * np.abs(diff).max()])
    nfr = int((np.diff(sgn) != 0).sum())
    print(f"    sign alternations across the screen: {nfr} "
          f"-> {nfr} fringes")
    assert vis > 0.05 and nfr >= 2
    # the program's own currency: which model codes the outcomes better
    rng = np.random.default_rng(128)
    n = 200000
    cdf = np.cumsum(coh * HAAR)
    cdf /= cdf[-1]
    x = np.interp(rng.random(n), cdf, TH)
    def code(p):
        pi = np.interp(x, TH, np.maximum(p, 1e-12))
        return float(-np.mean(np.log(pi)))
    lc, li = code(coh), code(inc)
    print(f"    code length: coherent {lc:.5f} nats, incoherent "
          f"{li:.5f}  ->  gap {li - lc:+.5f}")
    assert li - lc > 0.01
    print()
    print("  THE CONTROL. Destroy the relative phase -- randomise "
          "it and average -- and the")
    print("  fringe must vanish, or the effect was an artefact of "
          "the plot:")
    acc = 0.0
    for _ in range(400):
        ph = np.exp(1j * rng.uniform(0, 2 * np.pi))
        acc = acc + np.abs(pa + ph * pb) ** 2
    dec = dens_of(acc)
    vis2 = float(np.abs(dec - inc).max() / dec.max())
    print(f"    visibility after phase randomisation: {vis2:.4f}"
          f"   (was {vis:.4f})")
    assert vis2 < 0.1 * vis
    print("    it vanishes. The fringe was the relative phase, not "
          "the envelope\n")
    return vis, li - lc


def s4_what_it_shows(vis, gap):
    print("== s4: what this shows, and what it does not ==")
    print(f"  SHOWS: this program's own weight, reconstructed "
          f"through Osterwalder-Schrader,")
    print(f"  produces a finite-dimensional Hilbert space with a "
          f"derived spectrum, in which")
    print(f"  two alternatives interfere with visibility "
          f"{vis:.3f} and beat the incoherent")
    print(f"  model by {gap:.3f} nats/event. Nothing was posited: "
          f"the Hamiltonian came from")
    print("  the transfer operator, which came from the weight, "
          "which came from counting.")
    print()
    print("  DOES NOT SHOW: anything a sceptic should count as "
          "evidence FOR the theory. The")
    print("  Born rule was DERIVED here (0114/0119), so recovering "
          "interference is the chain")
    print("  closing on itself -- a consistency check, not a "
          "discriminator. It cannot")
    print("  distinguish this theory from standard quantum "
          "mechanics, and is not meant to.")
    print()
    print("  Its value is that it is ASSEMBLED: the pieces were "
          "proved separately over many")
    print("  stones and had never been run end to end. They fit\n")


if __name__ == "__main__":
    ns, E = s1_hamiltonian()
    pa, pb = s2_slits(ns, E)
    vis, gap = s3_fringe(pa, pb)
    s4_what_it_shows(vis, gap)
    print("all assertions passed")
