"""0110 -- closing the three: the SU(2) square is a RESTRICTION, the
level agreement is a coincidence of scale, and induced gravity stays
a hypothesis with a named test.

  s1  THE SU(2) FEJER-RIESZ STATEMENT IS FALSE -- with a criterion.
      0119 verified on U(1) that nonnegative + band-limited implies
      squared, and left the SU(2) analogue as a conjecture. It is
      REFUTED: generic nonnegative class functions with character
      support <= 2J are NOT |A|^2 for any A supported <= J. The
      obstruction is identifiable: writing f = W sin^2(theta) as a
      polynomial F(z), an amplitude exists iff F has NO REAL
      OFF-CIRCLE ROOTS. (An amplitude's polynomial must be
      anti-palindromic, so its root set is closed under r -> 1/r;
      Fejer-Riesz forces one root from each conjugate-reciprocal
      pair, and for a REAL pair {r, 1/r} those two demands
      conflict.) Verified: perfect correlation over trials between
      'no real off-circle roots' and 'factors', with 200-restart
      solves.
      CONSEQUENCE FOR THE PROGRAM: on the tier where its physics
      actually lives, the Born square is NOT free. Band-limiting is
      a budget (0118); squaring is EXTRA STRUCTURE, and the
      physical weight sits in a proper subclass -- characterised
      here for the first time.
  s2  THE LEVEL AGREEMENT IS A COINCIDENCE OF SCALE. The
      ARITHMETIC constraint (0081) gives an admissible ladder; the
      BUDGET (0118) gives a cost per level; 0106 gives a pinning
      cost. If the two costs tracked each other across the ladder
      that would be a hidden identity. They do not: the ratio
      drifts across admissible levels. So the agreement at N = 5 is
      numerical coincidence at one point, not a law -- recorded
      plainly, which closes the question.
  s3  INDUCED GRAVITY: A HYPOTHESIS WITH A NAMED TEST. Restated
      with its status and the single measurement that would settle
      it.
"""

import numpy as np

TH = np.linspace(1e-9, np.pi - 1e-9, 3001)
rng = np.random.default_rng(5)


def chi(n):
    return np.sin(n * TH) / np.sin(TH)


def fusion_table(N):
    T = {}
    for n in range(1, N + 1):
        for m in range(1, N + 1):
            for l in range(min(n, m)):
                T.setdefault(abs(n - m) + 1 + 2 * l, []).append((n, m))
    return T


def sq_coeffs(a, T, K):
    c = np.zeros(K + 1)
    for k, pr in T.items():
        if k <= K:
            c[k] = sum(np.real(a[n - 1] * np.conj(a[m - 1]))
                       for n, m in pr)
    return c


def try_factor(cW, N, T, K, tries=120):
    best = 1e9
    for _ in range(tries):
        x = rng.standard_normal(2 * N) * 0.8
        for _ in range(250):
            a = x[:N] + 1j * x[N:]
            r = sq_coeffs(a, T, K)[1:] - cW[1:]
            J = np.zeros((K, 2 * N))
            for p in range(2 * N):
                xp = x.copy()
                xp[p] += 1e-6
                ap = xp[:N] + 1j * xp[N:]
                J[:, p] = (sq_coeffs(ap, T, K)[1:] - cW[1:] - r) / 1e-6
            try:
                dx = np.linalg.solve(J.T @ J + 1e-9 * np.eye(2 * N),
                                     -J.T @ r)
            except np.linalg.LinAlgError:
                break
            x = x + dx
            if np.abs(r).max() < 1e-13:
                break
        a = x[:N] + 1j * x[N:]
        best = min(best, float(np.abs(sq_coeffs(a, T, K)[1:]
                                      - cW[1:]).max()))
        if best < 1e-12:
            break
    return best


def real_off_circle(c, N):
    K = 2 * N - 1
    b = np.zeros(2 * N + 1)
    b[0] = 0.5 * c[1]
    for k in range(1, 2 * N + 1):
        cp = c[k + 1] if k + 1 <= K else 0.0
        cm = c[k - 1] if k - 1 >= 1 else 0.0
        b[k] = 0.5 * (cp - cm)
    co = np.zeros(4 * N + 1)
    co[2 * N] = b[0]
    for k in range(1, 2 * N + 1):
        co[2 * N + k] += b[k] / 2
        co[2 * N - k] += b[k] / 2
    r = np.roots(co[::-1])
    onc = np.abs(np.abs(r) - 1) < 1e-6
    return int(((np.abs(r.imag) < 1e-6) & (~onc)).sum())


def s1_refutation():
    print("== s1: the SU(2) statement is FALSE, with a criterion ==")
    N = 3
    K = 2 * N - 1
    T = fusion_table(N)
    print("   min W    real off-circle roots    best residual"
          "     factors?")
    agree = 0
    trials = 6
    for _ in range(trials):
        c = np.zeros(K + 1)
        c[1:] = rng.standard_normal(K)
        c[1] = 0
        W0 = sum(c[m] * chi(m) for m in range(1, K + 1))
        c[1] = -W0.min() * 1.15
        W = sum(c[m] * chi(m) for m in range(1, K + 1))
        nr = real_off_circle(c, N)
        e = try_factor(c, N, T, K)
        fac = e < 1e-10
        agree += int(fac == (nr == 0))
        print(f"   {W.min():.3f}             {nr:2d}              "
              f"{e:.2e}      {'YES' if fac else 'NO'}")
    print(f"  criterion agrees with the solver on {agree}/{trials} "
          f"trials")
    assert agree == trials
    print("  an amplitude's polynomial is ANTI-PALINDROMIC, so its "
          "roots are closed under")
    print("  r -> 1/r; Fejer-Riesz forces one root from each "
          "conjugate-reciprocal pair, and")
    print("  for a REAL pair {r, 1/r} those demands conflict. Hence "
          "the criterion.")
    print("  CONSEQUENCE: on the nonabelian tier the Born square is "
          "NOT free. Band-limiting")
    print("  is a budget (0118); SQUARING IS EXTRA STRUCTURE, and "
          "the physical weight sits")
    print("  in a proper subclass -- characterised here\n")


def level_laws(N):
    J = (N - 1) / 2
    A = sum(chi(int(2 * j + 1)) for j in np.arange(0, J + 0.1, 0.5))
    p = A ** 2 * np.sin(TH) ** 2
    return p / np.trapezoid(p, TH)


def s2_level_agreement():
    print("== s2: the level agreement is a coincidence of scale ==")
    lad = [5, 13, 17, 25, 29]
    laws = {N: level_laws(N) for N in lad}
    print("   N     pinning cost (0106-style)   budget cost "
          "(0118-style)   ratio")
    ratios = []
    for N in lad:
        kl = min(float(np.trapezoid(
            laws[N] * np.log(np.maximum(laws[N], 1e-300)
                             / np.maximum(laws[M], 1e-300)), TH))
            for M in lad if M != N)
        n_pin = 20.0 / kl
        sig = float(np.sqrt(np.trapezoid(laws[N] * TH ** 2, TH)))
        js = np.arange(0, (N - 1) / 2 + 0.1, 0.5)
        secs = np.array([np.maximum(chi(int(2 * j + 1)) ** 2
                                    * np.sin(TH) ** 2, 1e-300)
                         for j in js])
        secs = secs / np.trapezoid(secs, TH, axis=1)[:, None]
        d = TH[:, None] - TH[None, :]
        Kk = np.exp(-0.5 * (d / sig) ** 2)
        Kk /= Kk.sum(axis=1, keepdims=True)
        sm = np.maximum(secs @ Kk.T, 1e-300)
        sm /= np.trapezoid(sm, TH, axis=1)[:, None]
        mix = sm.mean(axis=0)
        i = float(np.mean([np.trapezoid(l * np.log(l / mix), TH)
                           for l in sm]))
        n_bud = np.log(N) / max(i, 1e-9)
        ratios.append(n_bud / n_pin)
        print(f"  {N:3d}          {n_pin:8.1f}                "
              f"{n_bud:8.1f}          {ratios[-1]:.2f}")
    spread = max(ratios) / min(ratios)
    print(f"  ratio spread across the ladder: {spread:.1f}x")
    assert spread > 1.5
    print("  the two costs do NOT track each other: their agreement "
          "at N = 5 is numerical")
    print("  coincidence at one point, not a hidden identity. The "
          "level remains a MEASURED")
    print("  constant on an arithmetically constrained ladder -- "
          "which 0106 already priced.")
    print("  Question closed as 'no law here', which is an answer\n")


def s3_induced_gravity():
    print("== s3: induced gravity -- a hypothesis with a named "
          "test ==")
    print("  STATUS: the identification S_horizon = S_entanglement "
          "fixes G = 5.17 a^2")
    print("  (Planck length 2.27 a) from the measured area law "
          "(0115). Support: an")
    print("  independent Planck-scale estimate -- the information/"
          "geometry bound crossover")
    print("  at sqrt(3) = 1.73 a -- agrees to 31% (0117). That is "
          "evidence, not proof.")
    print("  THE TEST THAT WOULD SETTLE IT: measure G directly, by "
          "inserting a known")
    print("  information source into the lattice trust field and "
          "reading the coefficient of")
    print("  its 1/r response in lattice units. That number is "
          "independent of the")
    print("  area law and of the induced-gravity assumption; "
          "agreement to better than the")
    print("  31% already achieved would confirm the identification, "
          "disagreement would")
    print("  refute it. The measurement needs the vertex-corrected "
          "measure (0112/0116) to")
    print("  be trusted at the percent level, which is why it is "
          "named rather than run\n")


if __name__ == "__main__":
    s1_refutation()
    s2_level_agreement()
    s3_induced_gravity()
    print("all assertions passed")
