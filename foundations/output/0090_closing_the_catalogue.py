"""0090 -- closing the catalogue: the innovation channel, and the
derived vacuum's mixture.

The isomorphism-gap catalogue's last two items (0098: gaps 2 and 3),
closed to the extent the local models allow -- with one honest
surprise recorded against an earlier expectation.

  s1  GAP 2 -- THE INNOVATION CHANNEL, FORMALIZED AND MEASURED.
      A filter conditions on external innovations; the physics'
      cycle only self-conditions (parallel replicas). What external
      stream does the physics admit? Answer: exactly one -- the
      boundary. By Stokes (0080), hol(boundary) is a deterministic
      function of the bulk, so I(bulk; boundary) = H(hol), computed
      exactly from 0080's dual formula: H -> ln N at the confinement
      rate (1.6065 at P = 4 plaquettes; ln 5 to 6 digits by P = 16).
      The boundary's innovation capacity IS the quantized budget.
      Corollaries: the closed universe is the innovation-free
      (purely self-conditioning) filter; 'who supplies the
      innovation' = 'where is the boundary'; measurement = opening
      one; the causal layer = the order in which boundary data
      arrives.
  s2  GAP 3a -- THE DERIVED MIXTURE, GROUP LEVEL. The Born-weight
      single-plaquette ensemble has a REAL radial mixture:
      SD(ln theta) = 0.693 against 0.483 for the second-moment-
      matched Gaussian radial law (+43%), kurtosis 13. At the group
      level the derived vacuum is a scale mixture (the physical
      s_P > 0), as 0097's hand-built experiment anticipated.
  s3  GAP 3b -- THE SURPRISE. The algebra-level single-site vertex
      ensemble (Metropolis on e^{-price} with the compactness box
      |F_p| <= pi) is CUTOFF-DOMINATED: component kurtosis 2.6
      (sub-Gaussian) and SD(ln rho) = 0.08 BELOW the Gaussian
      control's 0.12 -- no radial mixture at all. The two local
      regulators disagree about the derived vacuum's mixture; the
      discriminating computation is the full lattice MC (approved,
      still the heavy remainder). 0097's expectation is confirmed at
      group level and refuted at algebra level -- recorded as the
      correspondence arc's one genuine surprise against us.
  s4  The catalogue scorecard.
"""

import math
import numpy as np

# ----------------------------------------------------------------------
# s1 -- gap 2
# ----------------------------------------------------------------------

def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def what(k, N):
    t = 0
    for d in range(1, N + 1):
        if N % d == 0 and k % (N // d) == 0:
            t += sum(1 for x in range(1, d + 1)
                     if _gcd(x, d) == 1) * (N // d)
    return t


def s1_innovation():
    print("== s1: gap 2 -- the innovation channel ==")
    N = 5
    Hs = {}
    for P in (4, 16, 64):
        ratios = [what(n, N) / what(0, N) for n in range(N)]
        Ph = []
        for h in range(N):
            v = sum(ratios[n] ** P * math.cos(2 * math.pi * n * h / N)
                    for n in range(N)) / N
            Ph.append(max(v, 1e-300))
        Z = sum(Ph)
        Ph = [p / Z for p in Ph]
        Hs[P] = -sum(p * math.log(p) for p in Ph)
        print(f"  open Z_5 lattice, P={P:3d}: I(bulk; boundary) = "
              f"H(hol) = {Hs[P]:.6f}")
    print(f"  ln N = {math.log(N):.6f}: the boundary's innovation "
          f"capacity is the quantized budget,")
    print("  approached at the confinement rate. Closed universe: no "
          "boundary, no stream --")
    print("  the innovation-free filter. Measurement = opening a "
          "boundary; the causal layer")
    print("  = the arrival order of boundary data\n")
    assert abs(Hs[16] - math.log(N)) < 1e-5
    assert abs(Hs[64] - math.log(N)) < 1e-9
    assert Hs[4] < math.log(N)


# ----------------------------------------------------------------------
# s2 -- gap 3a: group level
# ----------------------------------------------------------------------

TH = np.linspace(1e-7, np.pi - 1e-7, 400001)


def chi(j, th):
    return np.sin((2 * j + 1) * th) / np.sin(th)


def s2_group_level():
    print("== s2: gap 3a -- the derived mixture, group level ==")
    W = sum(chi(j, TH) for j in np.arange(0, 5.1, 0.5)) ** 2
    p = W * np.sin(TH) ** 2
    p /= np.trapezoid(p, TH)
    t2 = np.trapezoid(p * TH ** 2, TH)
    t4 = np.trapezoid(p * TH ** 4, TH)
    lt = np.trapezoid(p * np.log(TH), TH)
    l2 = np.trapezoid(p * np.log(TH) ** 2, TH)
    sP = float(np.sqrt(l2 - lt ** 2))
    q = np.exp(-TH ** 2 / (2 * (t2 / 3))) * TH ** 2
    q /= np.trapezoid(q, TH)
    qlt = np.trapezoid(q * np.log(TH), TH)
    ql2 = np.trapezoid(q * np.log(TH) ** 2, TH)
    sPg = float(np.sqrt(ql2 - qlt ** 2))
    kurt = float(t4 / t2 ** 2)
    print(f"  Born ensemble: kurtosis {kurt:.1f}, SD(ln theta) = "
          f"{sP:.3f}")
    print(f"  matched Gaussian radial law: SD(ln theta) = {sPg:.3f}  "
          f"(excess {100 * (sP / sPg - 1):.0f}%)")
    assert kurt > 10 and sP > sPg + 0.15
    print("  the group-level derived vacuum is a genuine scale "
          "mixture: the physical s_P > 0\n")


# ----------------------------------------------------------------------
# s3 -- gap 3b: algebra level (Metropolis)
# ----------------------------------------------------------------------

PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
EPSP = 0.01


def eps4(i, j, k, l):
    p = [i, j, k, l]
    if len(set(p)) < 4:
        return 0
    s = 1
    for a in range(4):
        for b in range(a + 1, 4):
            if p[a] > p[b]:
                s = -s
    return s


def starM(F):
    d = dict(zip(PAIRS, F))
    return [[sum(eps4(i, j, k, l) * d[(k, l)] for (k, l) in PAIRS)
             for j in range(4)] for i in range(4)]


def build_S(Fs):
    S = np.zeros((16, 16))
    for idx, (mu, nu) in enumerate(PAIRS):
        M = np.array(starM(Fs[idx])) / 2
        S[4 * mu:4 * mu + 4, 4 * nu:4 * nu + 4] += M
        S[4 * nu:4 * nu + 4, 4 * mu:4 * mu + 4] += M.T
    return S


def price(Fs):
    ev = np.linalg.eigvalsh(build_S([list(r) for r in Fs]))
    return float(0.5 * np.sum(np.log(1 + ev ** 2 / EPSP)))


def s3_algebra_level():
    print("== s3: gap 3b -- the surprise at algebra level ==")
    rng = np.random.default_rng(5)
    F = rng.normal(0, 0.2, (6, 6))
    p0 = price(F)
    samples = []
    NS = 120000
    for it in range(NS):
        Fp = F + rng.normal(0, 0.12, (6, 6))
        if np.max(np.linalg.norm(Fp, axis=1)) > np.pi:
            continue
        p1 = price(Fp)
        if np.log(rng.random() + 1e-300) < p0 - p1:
            F, p0 = Fp, p1
        if it > 30000 and it % 50 == 0:
            samples.append(F.copy())
    X = np.array(samples).reshape(len(samples), 36)
    kurt = float((((X - X.mean(0)) ** 4).mean(0)
                  / (X.var(0) ** 2)).mean())
    rho = np.sqrt((X ** 2).mean(1))
    sP = float(np.log(rho).std())
    C = np.cov(X.T)
    L = np.linalg.cholesky(C + 1e-10 * np.eye(36))
    XG = (L @ rng.normal(size=(36, len(X)))).T
    sPg = float(np.log(np.sqrt((XG ** 2).mean(1))).std())
    print(f"  vertex ensemble MC ({len(X)} samples): kurtosis "
          f"{kurt:.2f} (sub-Gaussian), SD(ln rho) = {sP:.3f}")
    print(f"  Gaussian collapse control: SD(ln rho) = {sPg:.3f}")
    assert kurt < 3.0
    assert sP < sPg
    print("  CUTOFF-DOMINATED: no radial mixture -- the compactness "
          "box sets the scale and the")
    print("  power-law weight pins the ensemble against it. The two "
          "local regulators DISAGREE;")
    print("  the discriminator is the full lattice MC (queued as the "
          "heavy remainder).")
    print("  0097's expectation: confirmed at group level, refuted "
          "at algebra level\n")


def s4_scorecard():
    print("== s4: the catalogue scorecard ==")
    print("  gap 1 (group curvature)      : CLOSED -- delta = 1/6 "
          "theorem, beta = (1-1/b^2)tau^2/6,")
    print("                                 running S^3 filter built "
          "(0099)")
    print("  gap 2 (external innovations) : CLOSED -- the boundary is "
          "the one channel; capacity")
    print("                                 = quantized budget (ln N);"
          " closed universe = innovation-")
    print("                                 free filter (here)")
    print("  gap 3 (the hypothesis bank)  : PARTIAL -- cure verified "
          "on built vacua (0097); derived")
    print("                                 verdict regulator-split "
          "(group: mixture real, +43%;")
    print("                                 algebra: cutoff-dominated)"
          "; discriminator = lattice MC")
    print("  gap 4 (discrete sectors)     : CLOSED as experiment -- "
          "regime-hazard priced both ways")
    print("                                 (+0.003 nats/pt), sectors "
          "are slow observables (lucid 0003)\n")


if __name__ == "__main__":
    s1_innovation()
    s2_group_level()
    s3_algebra_level()
    s4_scorecard()
    print("all assertions passed")
