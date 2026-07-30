"""
Two-layer decomposition, worked concretely on pure dephasing.

Pure stdlib.

The point: exhibit the smallest nontrivial case where BOTH LAYERS ARE
INDIVIDUALLY LOSSLESS and every bit of observed decoherence lives in their
INTERPLAY - and show that with a small environment the interplay loss is
RECOVERABLE (recurrence), so irreversibility is a statement about
inaccessibility (dilution), not about fundamental loss.

Setup. A qubit S coupled to a single environment qubit E by a pure-dephasing
interaction H = g Z_S Z_E, initial state |+>_S (x) |+>_E. Because H is
diagonal in the S pointer basis, the S populations never change; only phases
entangle. The joint state stays

    |Psi(t)> = (1/sqrt2) ( |0>_S |eta_0(t)>_E + |1>_S |eta_1(t)>_E )

with |eta_0>, |eta_1> unit vectors whose overlap <eta_0|eta_1> = cos(2 g t).
Partial trace over E gives

    rho_S(t) = (1/2) [[1, cos(2gt)], [cos(2gt), 1]]

Accounting (all computed below, none hardcoded):

  LAYER 1 - the joint unitary. ||Psi(t)||^2 = 1 and the joint state is pure
      at every t: von Neumann entropy of |Psi><Psi| is 0. Lossless.

  LAYER 2 - the pointer-basis branch weights (populations of |0>_S, |1>_S).
      Constant {1/2, 1/2} for all t: the "statistical" layer never moves
      under pure dephasing. Lossless.

  INTERPLAY - the entanglement across the S-E cut. Measured by the Schmidt
      spectrum of |Psi(t)>, which equals the eigenvalue spectrum of rho_S:
      lambda_pm(t) = (1 +- |cos 2gt|)/2. This is the ONLY time-varying
      entropy in the problem. The observed decoherence of S (loss of purity,
      decay of the off-diagonal) is exactly this quantity.

  RECURRENCE - at t = pi/(2g) the overlap returns to 1 and rho_S is pure
      again. With ONE environment mode the interplay loss is fully
      recoverable. Irreversibility appears only in the many-mode limit,
      where the recurrence time diverges and the correlation has diluted
      beyond any accessible subset (see mechanism/exploration/0002). This is
      Stinespring dilation read physically: every lossy channel is a
      lossless joint evolution plus coarse-graining.

IMPORTANT correction preserved for honesty: an earlier version of this file
labeled the constant branch weights "Schmidt weights". Wrong - the Schmidt
spectrum across the S-E cut IS the spectrum of rho_S and it oscillates; the
constant object is the pointer-basis populations. The two must not be
conflated: their difference is precisely the interplay.

Run:  python3 0003_two_layer_dephasing.py
"""

import math
import cmath


def bra_ket(a, b):
    """<a|b> for two 2D complex vectors."""
    return a[0].conjugate() * b[0] + a[1].conjugate() * b[1]


def eta(t, g, branch):
    """Environment state entangled with S branch |0> (branch=+1) or |1> (-1)."""
    c = 1 / math.sqrt(2)
    return (c * cmath.exp(-1j * branch * g * t),
            c * cmath.exp(+1j * branch * g * t))


def joint_state(t, g):
    """|Psi(t)> as a 4-vector in basis |0S 0E>, |0S 1E>, |1S 0E>, |1S 1E>."""
    e0, e1 = eta(t, g, +1), eta(t, g, -1)
    c = 1 / math.sqrt(2)
    return (c * e0[0], c * e0[1], c * e1[0], c * e1[1])


def reduced_rho_S(t, g):
    """2x2 reduced density matrix of S."""
    e0, e1 = eta(t, g, +1), eta(t, g, -1)
    off = 0.5 * bra_ket(e1, e0)
    return [[0.5, off], [off.conjugate(), 0.5]]


def qubit_spectrum(rho):
    """Eigenvalues of a 2x2 hermitian density matrix."""
    a, b, d = rho[0][0], rho[0][1], rho[1][1]
    tr = (a + d).real if isinstance(a + d, complex) else a + d
    det = (a * d - b.conjugate() * b).real
    disc = math.sqrt(max(tr * tr - 4 * det, 0.0))
    return ((tr + disc) / 2, (tr - disc) / 2)


def shannon(ws):
    return -sum(w * math.log(w) for w in ws if w > 1e-14)


def purity(rho):
    a, b, d = rho[0][0], rho[0][1], rho[1][1]
    return (a * a + d * d + 2 * (b.conjugate() * b)).real


if __name__ == "__main__":
    g = 1.0
    print("Two-layer accounting of pure dephasing: qubit S + one env qubit E.")
    print("H = g Z_S Z_E, |Psi(0)> = |+>_S |+>_E, g = 1.\n")
    hdr = (f"    {'t':>7} {'||Psi||^2':>10} {'pointer wts':>12} "
           f"{'S_pointer':>10} {'|off-diag|':>11} {'purity(S)':>10} "
           f"{'Schmidt spec':>16} {'S_interplay':>12}")
    print(hdr)

    checks_ok = True
    for t in (0.0, 0.2, math.pi / 8, 0.5, math.pi / 4,
              1.0, math.pi / 2, math.pi):
        psi = joint_state(t, g)
        joint_norm = sum((x.conjugate() * x).real for x in psi)
        # Layer-2: pointer-basis branch weights = |<0S,.|Psi>|^2 summed over E
        w0 = (psi[0].conjugate() * psi[0] + psi[1].conjugate() * psi[1]).real
        w1 = (psi[2].conjugate() * psi[2] + psi[3].conjugate() * psi[3]).real
        rho = reduced_rho_S(t, g)
        lam = qubit_spectrum(rho)          # Schmidt spectrum across S-E cut
        S_int = shannon(lam)               # interplay entropy (entanglement)
        S_ptr = shannon((w0, w1))          # layer-2 entropy (constant)
        off = abs(rho[0][1])
        p = purity(rho)
        checks_ok &= abs(joint_norm - 1) < 1e-12          # layer 1 lossless
        checks_ok &= abs(w0 - 0.5) < 1e-12 and abs(w1 - 0.5) < 1e-12  # layer 2 static
        print(f"    {t:>7.4f} {joint_norm:>10.6f} "
              f"({w0:.3f},{w1:.3f}) {S_ptr:>10.4f} {off:>11.6f} {p:>10.6f} "
              f"({lam[0]:.4f},{lam[1]:.4f}) {S_int:>12.4f}")

    # Recurrence check: purity returns to 1 at t = pi/2.
    p_rec = purity(reduced_rho_S(math.pi / 2, g))
    checks_ok &= abs(p_rec - 1.0) < 1e-12
    print(f"\n    recurrence at t = pi/2: purity(S) = {p_rec:.12f}  "
          f"(fully recovered: {abs(p_rec-1) < 1e-12})")
    print(f"\n    LAYER 1 lossless (joint norm 1 at all t): "
          f"{'OK' if checks_ok else 'FAIL'}")

    print("""
Reading:
  * Layer 1 (joint unitary): pure at every t. Lossless.
  * Layer 2 (pointer-basis branch weights): frozen at (1/2, 1/2). Lossless.
  * Interplay (Schmidt spectrum across the S-E cut = spectrum of rho_S):
    the only moving entropy. All observed decoherence of S is this term.
  * With one environment mode the interplay is RECOVERABLE (recurrence at
    t = pi/2): the loss is a statement about which correlations you can
    reach, not about anything being destroyed. Many modes -> recurrence
    time diverges -> Lindblad irreversibility as the inaccessible limit.
    This is Stinespring dilation: lossy = lossless-on-more + discard.
""")
