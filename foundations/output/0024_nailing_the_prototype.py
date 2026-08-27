"""Nailing the prototype: the measurement bit decided, the
square-root ledger, the rung, the halo's law.

  s1  THE MEASUREMENT BIT, DECIDED -- BY THE WEB'S OLDEST POSTULATE.
      The discriminating requirement is CHAIN (sheaf) CONSISTENCY,
      which is P3 itself: compatible contexts must agree on
      overlaps.  Concretely: a non-selective coarse measurement
      (total-deficit parity) must not disturb the statistics of the
      compatible fine measurement (individual deficits).
        - Lueders satisfies the chain law EXACTLY (deviation 1e-16
          per outcome), and is the UNIQUE update that does: chain
          consistency across every basis of the outcome block forces
          the block to P sigma P / tr, verified against random
          bases.
        - State-MRE VIOLATES it: after an unread coarse measurement
          the fine statistics shift by a measured total-variation
          distance -- a broken sheaf gluing on compatible contexts.
      So the web's own consistency postulate selects the INSTRUMENT
      reading: P5 = minimum-relative-entropy at the channel tier,
      which reproduces Lueders.  NO RIFT with textbook QM -- and P5
      graduates from rival to derivation.

  s2  THE SQUARE-ROOT LEDGER.  The two screening exponents,
      measured: the DENSITY-tier observable (pointwise K) screens
      with log-slope -1 in det g (measured -0.9995); the LOOP-tier
      observable (the transport atom) screens with log-slope -1/2
      (exact, from the constant-ambient integral).  One relation,
      third appearance: trust = sqrt(information) (stat-tracker),
      amplitude = sqrt(probability) (Born), holonomy-screening =
      sqrt(density-screening) (here) -- the mediator is the metric's
      own proper-area factor sqrt(det g).  Registered against the
      user's conjugate square: time is to trust (loop/holonomy tier,
      where energy = the rotation charge lives) as space is to
      distribution (density/anisotropy tier, where momentum lives).

  s3  THE RUNG.  On a closed web Gauss-Bonnet fixes the ledger:
      sum of deficits = 4 pi = 2N quanta, each atom 1..N-1 quanta
      (the per-defect bound delta < 2 pi).  Consequences, counted:
      at N = 2 the closed universe is UNIQUE -- four atoms of pi
      (the pillowcase orbifold); closed universes need >= 3 atoms
      for N >= 3 (and exactly 4 at N = 2); the number of ledgers
      grows with N (13 at N = 3, 81 at N = 4, computed).  The rung
      is not a law: it is the RESOLUTION OF THE WORLD'S LEDGER --
      content picks the level, and the inverse-limit tower is the
      ideal completion.

  s4  THE HALO'S LAW.  The source-free residual K - pi s/det g of
      an isolated lump: radial exponent -> -4 (measured -3.92 over
      r = 1.5..2.5), coefficient scaling sigma^2 (1.89 vs 1.96) and
      S^2 at weak strength (3.64 vs 4 for doubled S): the halo is a
      QUADRUPOLE TIDAL TAIL, SECOND ORDER in strength --
      K_halo ~ -c S^2 sigma^2 / r^4 -- which is exactly why the
      linear tier (0020's flux, R-independent to 1e-13) never saw
      it.  The classical field content is now fully catalogued:
      K = pi s/det g (sourced, exact) + the S^2 quadrupole vacuum
      dressing.

Run directly for the verification suite.
"""

from __future__ import annotations

import importlib
import math
import random
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
_p = importlib.import_module("0023_completing_the_prototype")
_d = importlib.import_module("0015_the_divergence_and_the_current")
_cl = importlib.import_module("0014_the_continuum_limit")
_f = importlib.import_module("0008_fisher_deficit")

TAU = 2 * math.pi


# =====================================================================
# 1. the measurement bit, decided
# =====================================================================

def build_sigma(rng, n=4):
    H = [[complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(n)]
         for i in range(n)]
    Hh = [[(H[i][j] + H[j][i].conjugate()) / 2 for j in range(n)]
          for i in range(n)]
    return _p.normalize(_p.mat_func(Hh, math.exp))


def mre_update(sig, idx, n=4):
    logsig = _p.mat_func(sig, math.log)
    block = _p.mat_func(_p.compress(logsig, idx), math.exp)
    return _p.normalize(_p.embed(block, idx, n))


def lueders_update(sig, idx, n=4):
    return _p.normalize(_p.embed(_p.compress(sig, idx), idx, n))


def verify_the_decision() -> None:
    rng = random.Random(28)
    sig = build_sigma(rng)
    even, odd = [0, 3], [1, 2]
    p_even = (sig[0][0] + sig[3][3]).real
    p_odd = 1 - p_even
    # chain law: non-selective coarse, then fine (computational basis)
    lued_seq, mre_seq = [], []
    lu_e, lu_o = lueders_update(sig, even), lueders_update(sig, odd)
    mr_e, mr_o = mre_update(sig, even), mre_update(sig, odd)
    for k in range(4):
        lued_seq.append((p_even * lu_e[k][k] + p_odd * lu_o[k][k]).real)
        mre_seq.append((p_even * mr_e[k][k] + p_odd * mr_o[k][k]).real)
    direct = [sig[k][k].real for k in range(4)]
    dev_lued = max(abs(a - b) for a, b in zip(lued_seq, direct))
    tv_mre = 0.5 * sum(abs(a - b) for a, b in zip(mre_seq, direct))
    print(f"    chain law (P3 as sheaf consistency): an unread coarse")
    print(f"    measurement must not shift compatible fine statistics.")
    print(f"      Lueders:   max deviation {dev_lued:.1e}  (exact)")
    print(f"      state-MRE: total-variation shift {tv_mre:.4f}")
    assert dev_lued < 1e-14
    assert tv_mre > 0.005
    print()
    # uniqueness: chain consistency in EVERY block basis forces Lueders
    worst_lued, worst_mre = 0.0, 0.0
    for seed in (5, 6, 7):
        r2 = random.Random(seed)
        # random orthonormal basis of the even block
        v1 = [complex(r2.gauss(0, 1), r2.gauss(0, 1)) for _ in range(2)]
        n1 = math.sqrt(sum(abs(x) ** 2 for x in v1))
        v1 = [x / n1 for x in v1]
        v2 = [-v1[1].conjugate(), v1[0].conjugate()]
        for v in (v1, v2):
            b = [0.0] * 4
            b[0], b[3] = v[0], v[1]
            pb = sum((b[i].conjugate() * sig[i][j] * b[j]).real
                     for i in range(4) for j in range(4)) / p_even
            for rho, tag in ((lu_e, "lued"), (mr_e, "mre")):
                pr = sum((b[i].conjugate() * rho[i][j] * b[j]).real
                         for i in range(4) for j in range(4))
                dev = abs(pr - pb)
                if tag == "lued":
                    worst_lued = max(worst_lued, dev)
                else:
                    worst_mre = max(worst_mre, dev)
    assert worst_lued < 1e-12
    assert worst_mre > 1e-3
    print(f"    uniqueness: refinement statistics in random bases of")
    print(f"    the outcome block --")
    print(f"      Lueders matches every basis ({worst_lued:.1e});")
    print(f"      state-MRE fails ({worst_mre:.4f}).  Matching in")
    print(f"      every basis forces the block to P sigma P/tr:")
    print(f"      Lueders is the UNIQUE chain-consistent update.")
    print()
    print("  DECIDED: P3 -- pairwise/sheaf consistency, the repo's")
    print("  oldest postulate -- selects the INSTRUMENT reading of")
    print("  P5.  Minimum-relative-entropy lives at the channel tier")
    print("  and reproduces Lueders; the state-tier reading breaks")
    print("  the sheaf gluing on compatible contexts and is refuted")
    print("  from inside the theory.  No rift with textbook QM: P5")
    print("  is a DERIVATION of the update rule, not a rival to it.")


# =====================================================================
# 2. the square-root ledger
# =====================================================================

def verify_the_ledger() -> None:
    # loop tier: atom screening in isotropic ambient c I: f = 1/c,
    # det = c^2  ->  log-slope -1/2 (exact integral, two points)
    f1 = _d.screened_atom_general(((0.2, 0.0), (0.0, 0.2)))
    f2 = _d.screened_atom_general(((0.5, 0.0), (0.0, 0.5)))
    s_loop = math.log(f2 / f1) / math.log(1.5 ** 2 / 1.2 ** 2)
    assert abs(s_loop + 0.5) < 1e-3, s_loop
    # density tier: pointwise K under an ambient shift c I
    S, sig_w, r = 0.05, 0.25, 0.15
    m0 = _cl.fuzz_metric(S, sig_w)

    def in_ambient(c):
        def m(x, y):
            E, F, G = m0(x, y)
            return (E + (c - 1), F, G + (c - 1))
        x = (r * math.cos(0.37), r * math.sin(0.37))
        E, F, G = m(*x)
        K = _f.gaussian_curvature(m, x[0], x[1], h=1e-3)
        return K, E * G - F * F
    K1, d1 = in_ambient(1.0)
    K2, d2 = in_ambient(1.3)
    s_dens = math.log(K2 / K1) / math.log(d2 / d1)
    assert abs(s_dens + 1.0) < 0.01, s_dens
    print(f"    loop tier (transport atom):   log-slope in det g = "
          f"{s_loop:+.4f}")
    print(f"    density tier (pointwise K):   log-slope in det g = "
          f"{s_dens:+.4f}")
    print()
    print("  THE SQUARE-ROOT LEDGER: the holonomy/loop observable")
    print("  screens with exactly HALF the exponent of the density")
    print("  observable -- mediated by the metric's own proper-area")
    print("  factor sqrt(det g).  The same one-half now appears three")
    print("  ways: trust = sqrt(information) (the stat-tracker's")
    print("  forced split), amplitude = sqrt(probability) (Born), and")
    print("  loop = sqrt(density) screening (gravity's coupling).")
    print("  Registered correspondence (the conjugate square): TIME")
    print("  pairs with TRUST -- the loop tier, where energy (= the")
    print("  monodromy's rotation charge, measured by round trips)")
    print("  lives; SPACE pairs with DISTRIBUTION -- the density/")
    print("  anisotropy tier, where momentum (the moment's spatial")
    print("  drift) lives.  One fixes distance, the other shape.")


# =====================================================================
# 3. the rung
# =====================================================================

def ledger_count(N):
    """Ordered closed-universe ledgers: compositions of 2N into
    parts 1..N-1 (per-atom bound delta < 2 pi)."""
    total = 2 * N
    ways = [0] * (total + 1)
    ways[0] = 1
    for t in range(1, total + 1):
        ways[t] = sum(ways[t - p] for p in range(1, N)
                      if p <= t)
    return ways[total]


def verify_the_rung() -> None:
    counts = {N: ledger_count(N) for N in (2, 3, 4)}
    assert counts[2] == 1
    print(f"    closed web: Gauss-Bonnet fixes the ledger at 4 pi =")
    print(f"    2N quanta, atoms of 1..N-1 quanta each.")
    print(f"    ledger counts: N = 2: {counts[2]},  N = 3: "
          f"{counts[3]},  N = 4: {counts[4]}")
    # minimal atom counts
    for N in (2, 3, 5, 9):
        m_min = math.ceil(2 * N / (N - 1))
        assert (m_min == 4) == (N == 2)
        assert m_min >= 3
    print(f"    minimal atoms: 4 at N = 2 (unique universe: four")
    print(f"    deficits of pi -- the PILLOWCASE orbifold); >= 3 for")
    print(f"    all higher rungs (no two-body closed universe --")
    print(f"    2+1 GR's folklore, from counting).")
    print()
    print("  The rung is not a law.  Level N admits exactly the")
    print("  closed worlds whose ledgers fit 2N quanta; richer or")
    print("  finer content needs a higher rung; the 2-adic tower's")
    print("  inverse limit is the ideal completion.  THE LEVEL IS")
    print("  THE RESOLUTION OF THE WORLD'S LEDGER -- a property of")
    print("  content, not of the laws.  (And the minimal quantum")
    print("  world is the pillowcase: four spinor atoms of pi --")
    print("  the two-party flip, four times over.)")


# =====================================================================
# 4. the halo's law
# =====================================================================

def halo(S, sig_w, r):
    m = _cl.fuzz_metric(S, sig_w)
    x = (r * math.cos(0.37), r * math.sin(0.37))
    E, F, G = m(*x)
    det = E * G - F * F
    K = _f.gaussian_curvature(m, x[0], x[1], h=1e-3)
    return K - math.pi * S * _cl.rho_gauss(r, sig_w) / det


def verify_the_halo() -> None:
    h15 = halo(0.4, 0.25, 1.5)
    h25 = halo(0.4, 0.25, 2.5)
    p = math.log(abs(h25 / h15)) / math.log(2.5 / 1.5)
    assert -4.3 < p < -3.6, p
    rS = halo(0.1, 0.25, 1.5) / halo(0.05, 0.25, 1.5)
    assert 3.2 < rS < 4.3, rS
    rsig = halo(0.4, 0.35, 2.0) / halo(0.4, 0.25, 2.0)
    assert 1.6 < rsig < 2.2, rsig
    c = abs(h25) * 2.5 ** 4 / (0.4 ** 2 * 0.25 ** 2)
    print(f"    exterior residual K - pi s/det g of an isolated lump:")
    print(f"      radial exponent {p:.2f}  (-> -4: quadrupole)")
    print(f"      strength scaling {rS:.2f} for doubled S  (-> 4:")
    print(f"      SECOND order)")
    print(f"      width scaling {rsig:.2f} vs sigma^2 = 1.96")
    print(f"      coefficient c = |K_halo| r^4/(S^2 sigma^2) ~ "
          f"{c:.2f}")
    print()
    print("  THE HALO'S LAW:  K_halo ~ -c S^2 sigma^2 / r^4 -- a")
    print("  quadrupole tidal tail, second order in strength.  That")
    print("  is exactly why the linear tier never saw it (0020's")
    print("  flux is R-independent to 1e-13), and it is the")
    print("  gravitational face of the exchange-rate result that")
    print("  correlation structure is second order in anisotropy.")
    print("  The classical field content is fully catalogued:")
    print("      K = pi s / det g   (sourced, exact)")
    print("        + O(S^2) quadrupole vacuum dressing.")


def run_verification_suite() -> None:
    sections = [
        ("The measurement bit, decided", verify_the_decision),
        ("The square-root ledger", verify_the_ledger),
        ("The rung", verify_the_rung),
        ("The halo's law", verify_the_halo),
    ]
    for index, (title, check) in enumerate(sections, start=1):
        print("=" * 70)
        print(f"{index}. {title}")
        print("=" * 70)
        check()
        print()
    print("=" * 70)
    print("suite complete")
    print("=" * 70)


if __name__ == "__main__":
    run_verification_suite()
