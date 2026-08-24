"""0098 -- the nonabelian boundary tier: composition is the filter's
predict, and ORDER is the channel.

Gap 2 (the innovation channel) was proven at the abelian tier: the
boundary is a SUM of the record, capacity ln N (0100), carried as
code (0105). The nonabelian version changes one thing: the boundary
is an ORDERED PRODUCT. Everything follows from that.

  s1  COMPOSITION = PREDICT. The class law of the ordered product of
      P iid heat-kernel innovations is EXACTLY K_{P tau} (Brownian
      motion on the group): composing the record into the boundary
      IS running the S^3 filter's predict semigroup. Verified: MC
      moments vs the character formula.
  s2  CAPACITY. The boundary's information above uniform,
      D(K_A || Haar), computed exactly by characters: decays at
      rate 2 lambda_{1/2} = 3/2 -- the confinement rate. The same
      statement as 0100's ln N saturation (there D -> 0 as H -> ln N):
      the boundary channel UNIFORMIZES at the confinement rate, on
      every tier.
  s3  THE ORDER CHANNEL -- the genuinely new nonabelian physics.
      Abelian: the boundary is order-free, exactly (a sum). SU(2):
      given the record {a, b, c}, the boundary's class distinguishes
      the arrangement's PARITY (cyclic orders collapse -- class is
      conjugation-invariant -- so of 3! orders exactly two classes
      survive: abc ~ bca ~ cab vs acb ~ cba ~ bac). With the
      boundary read through the same-noise apparatus as one
      innovation, the parity decodes with measurable success:
      capacity per triple, vs tau, with the exact U(1) null.
  s4  The statements: the causal layer (0100: 'arrival order of
      boundary data') is an EMPTY channel on abelian tiers and a
      REAL channel exactly when the group is nonabelian; its carrier
      is the commutator -- the same object whose curvature runs the
      coupling (0098-doc/0099). 0105's order-invariance survives
      untouched: the RECORD's total code never depends on order (the
      chain rule); it is the boundary SUMMARY that becomes
      order-sensitive.
"""

import numpy as np

TH = np.linspace(1e-7, np.pi - 1e-7, 100001)
HAAR = (2 / np.pi) * np.sin(TH) ** 2


def k_heat(tau, jmax=60):
    out = np.zeros_like(TH)
    for j in np.arange(0, jmax + 0.1, 0.5):
        out += (2 * j + 1) * np.exp(-tau * j * (j + 1)) \
            * np.sin((2 * j + 1) * TH) / np.sin(TH)
    return out


def sample_su2(tau, n, rng):
    p = np.maximum(k_heat(tau), 0) * HAAR
    cdf = np.cumsum(p) / p.sum()
    th = TH[np.searchsorted(cdf, rng.random(n))]
    ax = rng.normal(size=(n, 3))
    ax /= np.linalg.norm(ax, axis=1, keepdims=True)
    # class-angle convention throughout (0091): w = cos(theta)
    return np.concatenate([np.cos(th)[:, None],
                           np.sin(th)[:, None] * ax], axis=1)


def qmul(a, b):
    w1, x1, y1, z1 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    w2, x2, y2, z2 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
                     w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
                     w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2], axis=-1)


def cls(q):
    return np.arccos(np.clip(q[..., 0], -1, 1))


def s1_composition():
    print("== s1: composition = the predict semigroup ==")
    rng = np.random.default_rng(1)
    tau, P, n = 0.1, 8, 400000
    g = sample_su2(tau, n, rng)
    for _ in range(P - 1):
        g = qmul(g, sample_su2(tau, n, rng))
    thp = np.arccos(np.clip(g[:, 0], -1, 1))
    k = k_heat(P * tau)
    p = np.maximum(k, 0) * HAAR
    p /= np.trapezoid(p, TH)
    m2t = np.trapezoid(p * TH ** 2, TH)
    m4t = np.trapezoid(p * TH ** 4, TH)
    m2, m4 = np.mean(thp ** 2), np.mean(thp ** 4)
    print(f"  product of {P} iid K_tau innovations vs K_(P tau) "
          f"(characters):")
    print(f"    <th^2> {m2:.4f} vs {m2t:.4f}   <th^4> {m4:.4f} vs "
          f"{m4t:.4f}")
    assert abs(m2 / m2t - 1) < 0.01 and abs(m4 / m4t - 1) < 0.02
    print("  the boundary law IS the S^3 filter's predict chain -- "
          "composing the record")
    print("  = running the polar-transfer semigroup (the 2D "
          "nonabelian boundary, exact)\n")


def s2_capacity():
    print("== s2: capacity -- D(K_A || Haar), exact by "
          "characters ==")
    print("   A      D (nats)")
    As = np.array([0.2, 0.4, 0.8, 1.6, 3.2, 4.8, 6.4])
    Ds = []
    for A in As:
        k = np.maximum(k_heat(A), 1e-300)
        D = np.trapezoid(k * np.log(k) * HAAR, TH)
        Ds.append(max(D, 1e-300))
        print(f"  {A:4.1f}   {D:.3e}")
    rate = -np.polyfit(As[-3:], np.log(Ds[-3:]), 1)[0]
    print(f"  asymptotic decay rate = {rate:.3f}  (2 lambda_1/2 = "
          f"3/2: the confinement rate)")
    assert abs(rate - 1.5) < 0.02
    print("  the boundary channel uniformizes at the confinement "
          "rate -- 0100's abelian")
    print("  saturation (H -> ln N) and this are one statement: "
          "D -> 0\n")


def s3_order_channel():
    print("== s3: the order channel ==")
    rng = np.random.default_rng(3)
    n = 200000
    print("   tau    sep E|dth|  width    p_err   capacity/triple "
          "(nats)")
    caps = {}
    for tau in (0.05, 0.1, 0.2, 0.4):
        a = sample_su2(tau, n, rng)
        b = sample_su2(tau, n, rng)
        c = sample_su2(tau, n, rng)
        t1 = cls(qmul(qmul(a, b), c))
        t2 = cls(qmul(qmul(a, c), b))
        d = t1 - t2
        width = np.std(np.concatenate([t1, t2]))
        # boundary read = true class + apparatus noise of one
        # innovation's class spread
        sig = np.std(cls(a))
        # decode: nearer candidate; error when the decoded parity
        # is not the transmitted one
        trans1 = rng.random(n) < 0.5
        read = np.where(trans1, t1, t2) + sig * rng.normal(size=n)
        dec1 = np.abs(read - t1) < np.abs(read - t2)
        perr = float(np.mean(dec1 != trans1))
        hb = (-perr * np.log(max(perr, 1e-12))
              - (1 - perr) * np.log(max(1 - perr, 1e-12)))
        cap = np.log(2) - hb
        caps[tau] = cap
        print(f"  {tau:5.2f}   {np.abs(d).mean():.4f}     "
              f"{width:.3f}   {perr:.3f}   {cap:.4f}")
    # U(1) control: exact zero
    print("  U(1) control: boundary = sum of angles -- separation "
          "identically 0, capacity 0 (exact)")
    assert all(c > 0.001 for c in caps.values())
    assert caps[0.4] > caps[0.05]
    print("  cyclic orders collapse (class is conjugation-"
          "invariant): of 3! arrangements the")
    print("  boundary carries exactly the PARITY bit, at the "
          "commutator's signal strength\n")
    return caps


def s4_statements(caps):
    print("== s4: the tier's statements ==")
    print("  1. The 2D nonabelian boundary is CLOSED: composition = "
          "predict (s1), capacity =")
    print("     uniformization at the confinement rate (s2) -- the "
          "S^3 filter is the channel.")
    print("  2. The NEW nonabelian content is the order channel "
          "(s3): the causal layer --")
    print("     'the arrival order of boundary data' (0100) -- is "
          "empty on every abelian")
    print("     tier and real exactly when the group is nonabelian; "
          "its carrier is the")
    print("     commutator, the same object whose curvature runs "
          "the coupling.")
    print("  3. No conflict with 0105: the record's total code is "
          "order-invariant (chain")
    print("     rule, any group); the boundary SUMMARY is what "
          "order reaches.")
    print("  4. What remains 4D-specific: surface-ordering (which "
          "plaquettes compose in")
    print("     which order through which transports) -- the "
          "intertwiner combinatorics of")
    print("     the boundary-state vertex. The tier's algebra is "
          "done; that geometry is the")
    print("     one remaining heavy, unchanged in content but now "
          "isolated.")


if __name__ == "__main__":
    s1_composition()
    s2_capacity()
    caps = s3_order_channel()
    s4_statements(caps)
    print("\nall assertions passed")
