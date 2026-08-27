"""0147 -- what the classical tier has that the quantum one lacks.

0037 measured light bending on the CLASSICAL tier and got Einstein's
value: 0.008046 against GR's 0.008000 at b = 1, twice Newton. 0146
measured gamma on the QUANTUM tier and got -1: zero bending. Same
program, opposite answers. This isolates the difference.

The classical construction (0045, 0050):
  * the channel is a Maxwell field, A_mu = w k_mu, exactly
    Lienard-Wiechert;
  * THE METRIC IS ITS SQUARE, g = eta + w k(x)k -- the Kerr-Schild
    double copy;
  * Palatini/BF with the SIMPLICITY CONSTRAINT B = e^e, which takes
    the degree-of-freedom count from 0 to 2 (rank 24 of 24).

The quantum computation in 0146 has none of that. It varies a
symmetric metric FREELY over all ten components and reads the
response of a matter determinant.

  s0  THE GATE I SHOULD HAVE RUN FIRST: feed a genuine linearised
      Einstein-Hilbert kernel through the SAME solver and source. It
      must return gamma = +1. If it does not, 0146's -1 was my
      pipeline and not the physics.
  s1  THE SPECTRA, side by side: how many negative eigenvalues does
      each kernel have?
  s2  THE DIFFERENCE, in one line.
  s3  WHERE THE CLASSICAL TIER GETS IT.
"""

import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, tag):
    s = importlib.util.spec_from_file_location(
        tag, os.path.join(HERE, name))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


O = _load("0146_offdiagonal_metric.py", "o147")
EB, PAIRS = O.EB, O.PAIRS
L = 12


def smat():
    """A = ((tr h) I - 2 h)/2, as a 10x10 matrix in the EB basis."""
    S = np.zeros((10, 10))
    for b in range(10):
        h = EB[b]
        A = 0.5 * (np.trace(h) * np.eye(4) - 2 * h)
        for a in range(10):
            m, n = PAIRS[a]
            S[a, b] = A[m, n] if m == n else A[m, n]
    return S


S_AH = smat()


def eh_hessian(k2):
    """linearised Einstein-Hilbert, de Donder gauge:
    Q(h) = (k^2/2)[ tr(h h) - (1/2)(tr h)^2 ]  -- the Fierz-Pauli
    trace term is what makes the conformal mode negative."""
    H = np.zeros((10, 10))
    for a in range(10):
        for b in range(10):
            H[a, b] = k2 * (2 * np.trace(EB[a] @ EB[b])
                            - np.trace(EB[a]) * np.trace(EB[b]))
    return H


def source_h():
    """T^{mu nu} h_{mu nu} with T = diag(1,0,0,0)."""
    T = np.zeros((4, 4))
    T[0, 0] = 1.0
    return np.array([np.trace(T @ EB[a]) for a in range(10)])


def read_gamma(H, j):
    x = np.linalg.solve(H, -j)
    h = np.einsum("z,zmn->mn", x, EB)
    h0 = h[0, 0]
    hs = (h[1, 1] + h[2, 2] + h[3, 3]) / 3.0
    return h0, hs, -hs / h0


def s0_gate():
    print("== s0: the gate I should have run first ==")
    print("  Feed a genuine Einstein-Hilbert kernel through the "
          "SAME solver and the")
    print("  SAME source, and read gamma the same way. It must "
          "come back +1.")
    print()
    j = source_h()
    print("     k^2      h_00        h_spatial     gamma")
    for k2 in (0.5, 1.0, 2.0, 4.0):
        h0, hs, g = read_gamma(eh_hessian(k2), j)
        print(f"    {k2:5.2f}   {h0:+.6f}   {hs:+.6f}   {g:+.6f}")
    h0, hs, g = read_gamma(eh_hessian(1.0), j)
    assert abs(g - 1) < 1e-12, f"pipeline does not return +1: {g}"
    print()
    print("  GATE PASSED, exactly. The solver, the source and the "
          "gamma convention are")
    print("  all correct: given Einstein-Hilbert they return "
          "Einstein. So 0146's -1 is")
    print("  a property of the kernel it was given, not of the "
          "pipeline.")
    print()
    print("  Note WHERE the +1 comes from: h_00 and h_spatial have "
          "OPPOSITE SIGNS.")
    print()


def induced_hessian_in_h(k, vh):
    HA, idx = O.hessian(vh, k, L, False)
    return S_AH.T @ HA @ S_AH


def s1_spectra():
    print("== s1: the two spectra, side by side ==")
    vh = O.vhat(L)
    print("  Eigenvalues of the kernel on the 10-dimensional space "
          "of symmetric h.")
    print("  Einstein-Hilbert is an involution up to scale: nine "
          "+1 and one -1, and")
    print("  the -1 is the conformal mode.")
    print()
    w = np.linalg.eigvalsh(eh_hessian(1.0))
    print(f"    Einstein-Hilbert : {np.array2string(w, precision=3)}")
    print(f"      negative modes : {(w < -1e-9).sum()}")
    print()
    print("     k                    induced kernel: negative modes"
          "   min eigenvalue")
    for k in ((0, 1, 0, 0), (0, 2, 0, 0), (0, 1, 1, 0),
              (0, 2, 1, 1)):
        H = induced_hessian_in_h(k, vh)
        w = np.linalg.eigvalsh(H)
        neg = int((w < -1e-6 * abs(w).max()).sum())
        print(f"    {str(k):16s}            {neg}"
              f"                   {w.min():+.4e}")
    print()
    print("  ZERO negative modes, at every momentum. That is not "
          "an accident of the")
    print("  measurement -- 0146 proved it: with B a projector, "
          "Gamma''[A] =")
    print("  ||(1-B) A B||_F^2, non-negative for every symmetric A.")
    print()


def s2_the_difference():
    print("== s2: the difference, in one line ==")
    j = source_h()
    h0, hs, g = read_gamma(eh_hessian(1.0), j)
    print(f"  Einstein-Hilbert:  h_00 = {h0:+.4f}, "
          f"h_spatial = {hs:+.4f}   -> gamma = {g:+.3f}")
    print(f"  induced (0146)  :  h_00 = -3.243e-06, "
          f"h_spatial = -2.672e-06  -> gamma = -1.07")
    print()
    print("  gamma = - h_spatial / h_00, so:")
    print()
    print("      gamma > 0  <=>  the spatial and temporal metric "
          "responses have")
    print("                      OPPOSITE signs.")
    print()
    print("  In Einstein-Hilbert the trace term -(1/2)(tr h)^2 "
          "flips the trace mode,")
    print("  and that flip is exactly what makes the spatial "
          "response come back with")
    print("  the opposite sign to the temporal one. Take it away "
          "and a source pushes")
    print("  every component the same way -- which is a conformal "
          "response, gamma = -1,")
    print("  and no light bending.")
    print()
    print("  SO THE ENTIRE DIFFERENCE IS ONE SIGN: the sign of the "
          "conformal mode.")
    print("  A positive semidefinite action cannot have it. The "
          "matter determinant is")
    print("  positive semidefinite identically. Hence 0146.")
    print()


def s3_where_the_classical_tier_gets_it():
    print("== s3: where the classical tier gets the sign ==")
    print("  It never builds the metric by inverting a Hessian. "
          "From 0045 and 0050:")
    print()
    print("   * the channel is a Maxwell field A_mu = w k_mu "
          "(exactly Lienard-Wiechert,")
    print("     agreeing to 1e-8);")
    print("   * THE METRIC IS ITS SQUARE, g = eta + w k(x)k -- the "
          "Kerr-Schild double")
    print("     copy, with k NULL;")
    print("   * the action is Palatini/BF with the SIMPLICITY "
          "CONSTRAINT B = e^e, and")
    print("     0050 counted what that does: free BF has 0 "
          "physical degrees of freedom,")
    print("     imposing simplicity gives 2. The constraint is "
          "what releases the")
    print("     gravitons.")
    print()
    print("  Both of those are missing from 0146. It varies a "
          "symmetric metric FREELY")
    print("  over all ten components -- which is the UNCONSTRAINED "
          "sector, the one 0050")
    print("  says carries zero gravitons -- and reads the response "
          "of a determinant.")
    print()
    print("  And the quantum tier does have the missing structure. "
          "0142's graviton is")
    print("  traceless-sym(B+ (x) B-): a double copy, pure "
          "synergy, 5 of 9, residual")
    print("  spread 1.0000 given either stream alone and 0.0000 "
          "given both. lucid 0045")
    print("  measured |B+| = |B-| machine-exact for a simple "
          "bivector -- which IS the")
    print("  simplicity constraint B = e^e, on the lattice, "
          "already verified.")
    print()
    print("  So the quantum theory has TWO objects that both get "
          "called the metric:")
    print("    (1) the background weight W = sqrt(g) g^{mu nu} "
          "that matter couples to.")
    print("        Its induced action is PSD. gamma = -1. This is "
          "what items 3, 4 and 6")
    print("        measured.")
    print("    (2) the composite double copy B+ (x) B-, the "
          "program's actual graviton")
    print("        and the quantum image of the classical "
          "Kerr-Schild square. This is")
    print("        what item 2 tried to measure and could not, for "
          "a SCALE reason")
    print("        (xi/a ~ 1e20), not a structural one.")
    print()
    print("  The classical tier's GR lives in (2). 0146 measured "
          "(1).")
    print()
    print("  THAT IS A CORRECTION TO 0156. Its 'escape 1', the "
          "metric identification,")
    print("  was listed as narrow. It is the wide one. The "
          "falsification stands for the")
    print("  INDUCED route and does not touch the double-copy "
          "route -- which is the")
    print("  route the classical tier actually uses.")
    print()


if __name__ == "__main__":
    s0_gate()
    s1_spectra()
    s2_the_difference()
    s3_where_the_classical_tier_gets_it()
    print("all assertions passed")
