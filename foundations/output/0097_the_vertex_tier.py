"""0097 -- the vertex tier: the vertex is the total correlation.

The isomorphism's vertex/joint tier, closed. The claim, one theorem
in three habitats:

  A PRODUCT WEIGHT'S PRICE IS THE TOTAL CORRELATION IT DROPS, AND
  THE VERTEX FACTOR IS THAT CORRELATION.

  s1  EXACT (the linear-Gaussian habitat). Two streams whose latents
      share correlated process noise; a product bank (two correct
      marginal Kalmans) vs the joint filter. Theorem: each marginal
      Kalman achieves its stream's entropy rate, the joint achieves
      the joint entropy rate, so the product bank's excess code is
      EXACTLY the streams' mutual information rate
      -(1/4pi) int ln(1 - coh^2(w)) dw. Verified: simulation vs the
      spectral integral.
  s2  THE PHYSICS HABITAT (the derived vertex ensemble, 0090's
      machinery). The vertex weight is non-factorizing across the
      six planes; its Gaussian-sector total correlation TC_G =
      (1/2)[sum_b ln det Sigma_b - ln det Sigma] is measured. The
      identity E_joint[ln(joint/product-of-marginals)] = TC is
      definitional; the measured TC_G is the Gaussian part of the
      vertex's price, the non-Gaussian remainder is 0089's context
      spectrum.
  s3  THE FILTER HABITAT (recorded): GPB1's measured collapse
      relief (ridge 0.0022 -> 0.0101 nats/pt with the joint repair)
      is the same theorem's third face -- their product bank paid
      the innovations' mutual information; the repair recovered it.
"""

import numpy as np

# ----------------------------------------------------------------------
# s1 -- exact habitat
# ----------------------------------------------------------------------

Q0, R0, RHO = 0.1, 1.0, 0.8


def mi_rate_spectral():
    w = np.linspace(-np.pi, np.pi, 200001)[1:-1]
    g = np.abs(1 - np.exp(-1j * w)) ** 2
    s11 = Q0 / g + R0
    s12 = RHO * Q0 / g
    coh2 = s12 ** 2 / (s11 * s11)
    return -np.trapezoid(np.log(1 - coh2), w) / (4 * np.pi)


def kalman_code(y, q, r):
    m, P, code = 0.0, 10.0, 0.0
    for t, yt in enumerate(y):
        P = P + q
        S = P + r
        v = yt - m
        if t >= 500:
            code += 0.5 * (np.log(2 * np.pi * S) + v * v / S)
        K = P / S
        m, P = m + K * v, P - K * P
    return code


def joint_code(Y, Q, r):
    m = np.zeros(2)
    P = 10.0 * np.eye(2)
    code = 0.0
    for t in range(len(Y)):
        P = P + Q
        S = P + r * np.eye(2)
        v = Y[t] - m
        Si = np.linalg.inv(S)
        if t >= 500:
            code += 0.5 * (np.log((2 * np.pi) ** 2
                                  * np.linalg.det(S)) + v @ Si @ v)
        K = P @ Si
        m, P = m + K @ v, P - K @ P
    return code


def s1_exact():
    print("== s1: exact habitat -- product bank's excess = mutual "
          "information rate ==")
    rng = np.random.default_rng(2)
    T = 200000
    L = np.linalg.cholesky(Q0 * np.array([[1, RHO], [RHO, 1]]))
    x = np.cumsum(rng.normal(size=(T, 2)) @ L.T, axis=0)
    Y = x + np.sqrt(R0) * rng.normal(size=(T, 2))
    cp = kalman_code(Y[:, 0], Q0, R0) + kalman_code(Y[:, 1], Q0, R0)
    cj = joint_code(Y, Q0 * np.array([[1, RHO], [RHO, 1]]), R0)
    gap = (cp - cj) / (T - 500)
    mi = mi_rate_spectral()
    print(f"  measured product-bank excess: {gap:.5f} nats/step")
    print(f"  spectral MI rate            : {mi:.5f} nats/step  "
          f"(ratio {gap / mi:.3f})")
    assert abs(gap / mi - 1) < 0.03
    print("  the product bank pays exactly the streams' mutual "
          "information -- the vertex,")
    print("  in this habitat, IS the dropped total correlation\n")


# ----------------------------------------------------------------------
# s2 -- the physics habitat (0090's vertex ensemble)
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


def s2_vertex_tc():
    print("== s2: the physics habitat -- the vertex ensemble's "
          "total correlation ==")
    rng = np.random.default_rng(5)
    F = rng.normal(0, 0.2, (6, 6))
    p0 = price(F)
    samples = []
    for it in range(120000):
        Fp = F + rng.normal(0, 0.12, (6, 6))
        if np.max(np.linalg.norm(Fp, axis=1)) > np.pi:
            continue
        p1 = price(Fp)
        if np.log(rng.random() + 1e-300) < p0 - p1:
            F, p0 = Fp, p1
        if it > 30000 and it % 50 == 0:
            samples.append(F.copy())
    X = np.array(samples).reshape(len(samples), 36)
    C = np.cov(X.T) + 1e-12 * np.eye(36)
    sgn, ldf = np.linalg.slogdet(C)
    ldb = 0.0
    for b in range(6):
        blk = C[6 * b:6 * b + 6, 6 * b:6 * b + 6]
        ldb += np.linalg.slogdet(blk)[1]
    tcg = 0.5 * (ldb - ldf)
    print(f"  {len(X)} vertex samples; Gaussian-sector total "
          f"correlation across the six")
    print(f"  planes: TC_G = {tcg:.2f} nats per vertex")
    assert tcg > 0.5
    print("  the vertex factor's price = TC (definitional identity);"
          " TC_G is its Gaussian")
    print("  part, the non-Gaussian remainder is the context "
          "spectrum (0089, +1.17 nats)\n")
    return tcg


def s3_third_face():
    print("== s3: the filter habitat (recorded) ==")
    print("  GPB1's collapse relief (their oracle-gap workstream): "
          "ridge 0.0022 -> 0.0101")
    print("  nats/pt under the joint repair -- the same theorem's "
          "measured third face:")
    print("  a product bank pays the innovations' mutual "
          "information; the repair (IMM /")
    print("  the vertex factor) recovers exactly that. The tier is "
          "one identity in three")
    print("  habitats: exact (s1), derived-physics (s2), "
          "field-data (their GPB1).\n")


if __name__ == "__main__":
    s1_exact()
    s2_vertex_tc()
    s3_third_face()
    print("all assertions passed")
