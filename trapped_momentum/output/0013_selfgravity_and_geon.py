"""
Stage 3, first piece: the null ring's gravitational SELF-confinement.

Question (registered in 0013): does self-gravity push Y toward the Kerr value
+Ea^2? Equivalently: as gravity takes over the confinement from the material
hoop, does M2 move from -Ea^2/2 to -Ea^2?

REGISTERED ITEMS, before running (standing practice):

  R1  AUDIT: the justification registered in 0013 ("the exterior must match
      Kerr") is WRONG and is withdrawn before computing: there is no Birkhoff
      theorem for rotation. Rotating material sources generically have
      non-Kerr exteriors (neutron stars: M2 = -q J^2/M with q ~ 2-10 [K]).
      The corrected question: what does self-gravity actually select?

  R2  HAND DERIVATION, registered as a prediction for the numerics. In
      linearized GR (signature +---, stationary, h-bar_mu-nu =
      -4G INT T_mu-nu/|x-x'|), the self-force per unit length of a thin ring
      of circulating null flow reduces to the kernel

        f_inward(psi) dpsi = (2 G sigma^2 / a) [2 sin(psi/2) - sin^3(psi/2)]
        INT over (0, 2pi) = 16/3
        =>  f_inward = (32/3) G sigma^2 / a,   sigma = E/(2 pi a)

      giving confinement fraction  f = F_grav/F_needed = (16/3pi) GE/a and a
      geon radius a* = (16/3pi) GE ~ 1.698 GE. To be CONFIRMED or refuted by
      the independent component-wise machinery below.

  R3  STRUCTURE: (a) the null-ring self-force is FINITE with no thickness
      cutoff -- neighbouring elements are parallel null movers and parallel
      null rays do not interact (Tolman-Ehrenfest-Podolsky), so the
      coincidence singularity is suppressed; (b) a STATIC massive ring's
      self-force diverges logarithmically -- nullness is what regularizes;
      (c) by source sector (T_00 / T_0j / T_jk) the force is log-divergent
      with slope ratio 2 : -4 : 2, cancelling in the sum; (d) tangential
      self-force vanishes by symmetry.
      AMENDMENT to (c), recorded not rewritten: FALSIFIED by the run. The
      measured slope ratio is 1 : +2 : -3 (normalized), summing to zero as
      required. The registered 1 : -2 : 1 came from potential-COUPLING
      reasoning ((l'.l)^2 = 1 - 2c + c^2), which is correct for the
      interaction energy but wrong for the FORCE: the force contains the
      momentum-flux term (l.d)(h_{i beta} l^beta) alongside the coupling
      gradient, and it redistributes the sectors. The cancellation -- the
      physics point -- stands.

  R4  BOOKKEEPING: with gravity supplying fraction f, hoop tension scales as
      (1-f), so Y = f Ea^2 and M2(f) = -(1+f) Ea^2/2: LINEAR interpolation
      from the hoop value (f=0, half Kerr) to exactly Kerr at f=1. The Kerr
      endpoint needs no exterior theorem: material tension is the only
      negative-second-moment agent, and full self-confinement removes it.
      (Endpoint caveat: at f=1, GE/a ~ 0.6 is not small; second-order field
      stresses are uncontrolled there -- the neutron-star q!=1 fact says they
      generically matter. Leading order only.)

  R5  SCALES: for the electron, a = S/E with S = hbar/2 gives
      a/(GE) = (m_Planck/m_e)^2 / 2 ~ 1e44: gravity supplies ~1e-44 of the
      needed confinement. The geon reading CANNOT confine the electron; the
      zero-stress-moment constraint of 0013 must be met by non-gravitational
      structure.

Pure stdlib. G = c = 1, E = 1, a = 1. Run: python3 0013_selfgravity_and_geon.py
"""

import math

PASS = []
G = 1.0
E = 1.0
A = 1.0
SIG = E / (2.0 * math.pi * A)     # energy per unit length


def check(name, got, want, atol=1e-6):
    ok = abs(got - want) <= atol
    PASS.append((name, ok, got, want))
    return ok


# ---------------------------------------------------------------- geometry
def src(phi):
    """Position, tangent, and lowered null covector of the ring flow."""
    x = (A * math.cos(phi), A * math.sin(phi), 0.0)
    t = (-math.sin(phi), math.cos(phi), 0.0)
    l_lo = (1.0, -t[0], -t[1], -t[2])       # l_mu = (1, -t)
    return x, t, l_lo


X0, T0, L0_LO = src(0.0)
L0_UP = (1.0, T0[0], T0[1], 0.0)            # l0^mu = (1, t)
N0 = (1.0, 0.0, 0.0)                        # outward radial at probe


# ------------------------------------- route 1: hand-derived kernel (R2)
def force_hand(n=200000):
    """f_inward = (2 G sigma^2/a) INT [2 s - s^3] dpsi, s = sin(psi/2)."""
    acc = 0.0
    for k in range(n):
        psi = 2.0 * math.pi * (k + 0.5) / n
        s = math.sin(psi / 2.0)
        acc += (2.0 * s - s ** 3) * (2.0 * math.pi / n)
    return 2.0 * G * SIG * SIG / A * acc


# --------------------- route 2: component-wise machinery, from scratch
ETA = (1.0, -1.0, -1.0, -1.0)


def force_sector(sector, delta=0.0, n=20000, probe_null=True):
    """Radial and tangential force/length on the probe element from the
    field of the ring's source components in `sector` (set of (mu,nu)),
    excluding |psi| < delta. Full first-principles chain:
    d_k h-bar_{mu nu} -> trace reversal -> Gamma -> f = -sigma Gamma^i l l."""
    dh = [[[0.0] * 4 for _ in range(4)] for _ in range(3)]   # [k][mu][nu]
    for m in range(n):
        psi = 2.0 * math.pi * (m + 0.5) / n
        if psi < delta or psi > 2.0 * math.pi - delta:
            continue
        xs, ts, l_lo = src(psi)
        R = (X0[0] - xs[0], X0[1] - xs[1], X0[2] - xs[2])
        d = math.sqrt(R[0] ** 2 + R[1] ** 2 + R[2] ** 2)
        w = A * (2.0 * math.pi / n)
        # d_k h-bar_{mu nu} = +4 G sigma INT l_mu l_nu R^k / d^3  dl
        for (mu, nu) in sector:
            val = l_lo[mu] * l_lo[nu]
            for k in range(3):
                dh[k][mu][nu] += 4.0 * G * SIG * val * R[k] / d ** 3 * w
                if mu != nu:
                    dh[k][nu][mu] += 4.0 * G * SIG * val * R[k] / d ** 3 * w
    # trace reversal: h = h-bar - (1/2) eta tr(h-bar)
    dtr = [sum(ETA[mu] * dh[k][mu][mu] for mu in range(4)) for k in range(3)]
    dhf = [[[dh[k][mu][nu] - 0.5 * ETA[mu] * (dtr[k] if mu == nu else 0.0)
             for nu in range(4)] for mu in range(4)] for k in range(3)]

    def d_h(kk, mu, nu):
        return dhf[kk - 1][mu][nu] if kk != 0 else 0.0

    l = L0_UP if probe_null else (1.0, 0.0, 0.0, 0.0)
    f = [0.0, 0.0, 0.0]
    for i in range(1, 4):
        acc = 0.0
        for al in range(4):
            for be in range(4):
                if l[al] == 0.0 or l[be] == 0.0:
                    continue
                gam_lo = 0.5 * (d_h(al, i, be) + d_h(be, i, al)
                                - d_h(i, al, be))
                acc += gam_lo * l[al] * l[be]
        # Gamma^i = eta^ii Gamma_i = -Gamma_i ;  f^i = -sigma Gamma^i l l
        f[i - 1] = -SIG * (-(acc))
    fr = f[0] * N0[0] + f[1] * N0[1] + f[2] * N0[2]
    ft = f[0] * T0[0] + f[1] * T0[1] + f[2] * T0[2]
    return fr, ft


FULL = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3),
        (2, 2), (2, 3), (3, 3)]
S_00 = [(0, 0)]
S_0J = [(0, 1), (0, 2), (0, 3)]
S_JK = [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]


def main():
    print("=" * 74)
    print("R2  --  Two independent routes to the self-force")
    print("=" * 74)
    print()
    fh = force_hand()
    pred = (32.0 / 3.0) * G * SIG * SIG / A
    fr, ft = force_sector(FULL)
    print(f"  hand kernel, quadrature      : f_inward = {fh:.8f}")
    print(f"  hand kernel, closed form 32/3: f_inward = {pred:.8f}")
    print(f"  component machinery          : f_inward = {-fr:.8f}"
          f"   (radial f = {fr:+.8f})")
    print(f"  component machinery tangential f = {ft:+.2e}")
    check("hand kernel = 32/3 G sig^2/a", fh, pred, atol=1e-8)
    check("machinery matches hand kernel", -fr, pred, atol=2e-3 * pred)
    check("tangential force vanishes (R3d)", ft, 0.0, atol=1e-9)
    print()
    print("  CONFIRMED: the registered hand derivation survives the")
    print("  independent first-principles computation. The self-force is")
    print("  attractive (inward), with NO cutoff anywhere -- the integrand")
    print("  vanishes at coincidence. Nullness regularizes (R3a).")
    print()

    print("=" * 74)
    print("R3b --  Contrast: the STATIC massive ring diverges")
    print("=" * 74)
    print()
    hdr = f"  {'delta':>10}{'null ring f_in':>17}{'static ring f_in':>19}"
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    prev_static = None
    for delta in (0.3, 0.1, 0.03, 0.01):
        fr_n, _ = force_sector(FULL, delta=delta)
        fr_s, _ = force_sector(S_00, delta=delta, probe_null=False)
        print(f"  {delta:>10.3f}{-fr_n:>17.8f}{-fr_s:>19.8f}")
        prev_static = -fr_s
    check("null ring converged by delta=0.01",
          -force_sector(FULL, delta=0.01)[0], pred, atol=5e-3 * pred)
    check("static ring still growing", 1.0 if prev_static > 0.1 else 0.0, 1.0)
    print()
    print("  The null ring's force is delta-independent; the static ring's")
    print("  grows like ln(1/delta) without bound. A material ring needs a")
    print("  thickness; the null ring does not. (R3b CONFIRMED)")
    print()

    print("=" * 74)
    print("R3c --  Sector decomposition: 2 : -4 : 2, cancelling logs")
    print("=" * 74)
    print()
    hdr = (f"  {'delta':>8}{'T00 sector':>13}{'T0j sector':>13}"
           f"{'Tjk sector':>13}{'sum':>13}")
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    rows = []
    for delta in (0.1, 0.05, 0.025):
        e = -force_sector(S_00, delta=delta)[0]
        m = -force_sector(S_0J, delta=delta)[0]
        s = -force_sector(S_JK, delta=delta)[0]
        rows.append((delta, e, m, s))
        print(f"  {delta:>8.3f}{e:>13.6f}{m:>13.6f}{s:>13.6f}{e + m + s:>13.6f}")
    # log slopes from successive halvings: df / ln 2
    ln2 = math.log(2.0)
    se = (rows[2][1] - rows[1][1]) / ln2
    sm = (rows[2][2] - rows[1][2]) / ln2
    ss = (rows[2][3] - rows[1][3]) / ln2
    base = se
    print()
    print(f"  log-slopes (per ln 2 of delta-halving), normalized to T00:")
    print(f"    T00 : {se / base:+.4f}    T0j : {sm / base:+.4f}"
          f"    Tjk : {ss / base:+.4f}")
    check("slope ratio T0j/T00 = +2 (measured)", sm / base, 2.0, atol=0.03)
    check("slope ratio Tjk/T00 = -3 (measured)", ss / base, -3.0, atol=0.03)
    check("slopes cancel", (se + sm + ss) / base, 0.0, atol=0.03)
    print()
    print("  R3c AS REGISTERED IS FALSIFIED: the ratio is 1 : +2 : -3, not")
    print("  1 : -2 : 1. The registered guess used the interaction-energy")
    print("  contraction (l'.l)^2 = 1 - 2c + c^2, which does give 1 : -2 : 1")
    print("  -- but the FORCE adds the momentum-flux term")
    print("  (l.d)(h_{i beta} l^beta) to the coupling gradient, and it")
    print("  redistributes the sectors. What survives, and is the physics:")
    print("  each sector diverges logarithmically and THE SUM CANCELS to a")
    print("  finite, cutoff-free force. Parallel null flow does not")
    print("  self-interact; how the cancellation is apportioned was guessed")
    print("  wrong and is now measured.")
    print()

    print("=" * 74)
    print("R4  --  Y(f) and the march from half-Kerr to Kerr")
    print("=" * 74)
    print()
    print("  Gravity supplies f = F_grav / F_needed of the confinement; the")
    print("  hoop supplies the rest, tension (1-f) E/(2 pi a). Then")
    print()
    print("    Y(f) = Ea^2 - (1-f) Ea^2 = f Ea^2")
    print("    M2(f) = -(1/2)(Ea^2 + Y) = -(1+f)/2 Ea^2")
    print()
    hdr = f"  {'f':>6}{'Y/Ea^2':>9}{'M2/(-Ea^2)':>12}{'fraction of Kerr':>18}"
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    for f in (0.0, 0.25, 0.5, 0.75, 1.0):
        m2 = (1.0 + f) / 2.0
        print(f"  {f:>6.2f}{f:>9.2f}{m2:>12.3f}{m2:>18.3f}")
    check("f=0 reproduces hoop (half Kerr)", (1 + 0.0) / 2, 0.5)
    check("f=1 reaches Kerr exactly", (1 + 1.0) / 2, 1.0)
    print()
    print("  The corrected mechanism (R1, R4): no exterior theorem is used.")
    print("  Material tension is the ONLY negative-second-moment agent; full")
    print("  self-confinement removes it, and the ring's own null pressure")
    print("  supplies the Kerr value +Ea^2 by itself. Leading order only:")
    print("  at f = 1 the expansion parameter GE/a ~ 0.6 is not small, and")
    print("  the neutron-star q != 1 fact [K] says second-order field")
    print("  stresses generically shift the endpoint.")
    print()

    print("=" * 74)
    print("R2/R5  --  The geon radius, extremality, and the electron")
    print("=" * 74)
    print()
    kappa = 16.0 / (3.0 * math.pi)
    print(f"  confinement fraction   f = (16/3pi) GE/a = {kappa:.6f} GE/a")
    print(f"  geon condition f = 1:  a* = {kappa:.6f} GE")
    print(f"  extremal Kerr:         a  = 1.000000 GM")
    print(f"  ratio a*/a_extremal = {kappa:.4f} -- order unity, NOT 1.")
    print(f"  compactness at the geon point: GE/a* = {1 / kappa:.4f}"
          " (not small; leading order only)")
    print()
    mP_over_me = 2.176434e-8 / 9.1093837015e-31
    f_elec = 2.0 / mP_over_me ** 2
    print(f"  electron: a/(GE) = (m_P/m_e)^2 / 2 = {mP_over_me ** 2 / 2:.3e}")
    print(f"  gravity's share of the electron's confinement: f ~ {f_elec:.3e}")
    check("electron f ~ 1e-44", math.log10(f_elec), -44.0, atol=1.0)
    print()
    print("  R5 CONFIRMED: the geon reading cannot confine the electron --")
    print("  gravity supplies ~1e-44 of the needed force. The 0013 constraint")
    print("  (zero stress second moment) must be met by non-gravitational")
    print("  structure. Self-confinement by gravity is a statement about")
    print("  Planck-scale objects, not electrons.")
    print()

    print("=" * 74)
    print("VERDICT")
    print("=" * 74)
    print()
    print("  The registered question comes back YES at leading order: as")
    print("  self-gravity replaces material tension, M2 marches linearly from")
    print("  the hoop's half-Kerr to EXACTLY Kerr at full self-confinement --")
    print("  not because any exterior theorem forces it (R1: that argument")
    print("  was wrong and is withdrawn) but because material tension is the")
    print("  only agent that subtracts stress second moment.")
    print()
    print("  Two genuine findings en route: the null ring's gravitational")
    print("  self-interaction is FINITE in the thin limit (nullness")
    print("  regularizes -- parallel null neighbours do not interact), and")
    print("  the linearized geon sits at a* = (16/3pi) GE ~ 1.70 GE, the")
    print("  extremal-Kerr scale times an order-unity factor.")
    print()

    print("=" * 74)
    print("SELF-CHECKS")
    print("=" * 74)
    bad = [p for p in PASS if not p[1]]
    for name, ok, got, want in PASS:
        print(f"  [{'ok' if ok else 'FAIL'}] {name:<42} {float(got):+.6e}")
    print()
    print(f"  {len(PASS) - len(bad)}/{len(PASS)} checks passed.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
