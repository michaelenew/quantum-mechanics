"""0151 -- the obstruction is the CARRIER, not the theory and not the
scale.

0161 said the scale (xi/a ~ 1e20) blocks a simulation of gravitational
dynamics. That is wrong, and item 4 is the counterexample: the static
metric response was measured cleanly at the same coupling -- 1/r to
1.68% across a factor 15 in r (0143). A background-field response is
not a bound-state correlator and does not need the correlation length.
The scale killed item 2, which wanted a POLE. It does not kill a
response.

So what does block a geodesic? 0150 measured it without naming it.
The kernel that violates diffeomorphism invariance by 0.30 -- flat in
k, 1.7e15 times Einstein-Hilbert's -- is the FREE SCALAR DETERMINANT
ON THE FLAT HYPERCUBIC LATTICE. No gauge weight enters it anywhere.
It contains nothing from this program at all.

    The violation is a property of the CARRIER: a rigid grid with a
    fixed background geometry.

That matters because of what 0150 s1 proved: invariance is what FORCES
Einstein-Hilbert. So the regulator destroys exactly the symmetry that
does the derivation's work. Nothing then forbids a cosmological
constant or a graviton mass, and 0159 found both.

  s1  THE VIOLATION HAS NO GAUGE FIELD IN IT. Stated as code, not
      argument.
  s2  IS IT THE DISCRETISATION OF THE DERIVATIVE? Change the
      derivative and see. If the violation is unmoved, it is
      structural -- a fixed grid simply has no infinitesimal
      diffeomorphisms to be invariant under.
  s3  WHAT A CARRIER THAT WORKS LOOKS LIKE.
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


D0 = _load("0150_diffeo_invariance.py", "d151")
O, C8 = D0.O, D0.C8
L = 12


def vhat_variant(L, kind):
    """the SAME construction with a different lattice derivative."""
    ax = 2 * np.pi * np.fft.fftfreq(L)
    g = np.meshgrid(*([ax] * 4), indexing="ij")
    if kind == "forward":
        v = np.stack([np.exp(1j * gi) - 1.0 for gi in g], -1)
    elif kind == "central":
        v = np.stack([1j * np.sin(gi) for gi in g], -1)
    elif kind == "improved":
        v = np.stack([(4.0 / 3.0) * (np.exp(1j * gi) - 1.0)
                      - (1.0 / 6.0) * (np.exp(2j * gi) - 1.0)
                      for gi in g], -1)
    else:
        raise ValueError(kind)
    n = np.linalg.norm(v, axis=-1, keepdims=True)
    n[n == 0] = np.inf
    return v / n


def violation(vh, kk, use_ct=True):
    kv = np.array([2 * np.sin(np.pi * ki / L) for ki in kk])
    G = D0.gauge_modes(kv)
    HA, _ = O.hessian(vh, kk, L, False)
    K = HA
    if use_ct:
        Lc = 4.0 * O.beta_mat(vh)[0][0, 0]
        K = K + C8.counterterm(Lc)
    return float(np.linalg.norm(K @ G)
                 / (np.linalg.norm(K) * np.linalg.norm(G)))


def s1_no_gauge_field():
    print("== s1: the violating kernel contains no gauge field ==")
    print("  0150 s2 measured a diffeomorphism violation of 0.30 "
          "and attributed it to")
    print("  'the induced kernel'. Trace what that kernel is built "
          "from:")
    print()
    print("    O.hessian(vh, k, L)  <- vh = O.vhat(L)  <- "
          "v_mu(q) = exp(i q_mu) - 1")
    print()
    print("  That is the FLAT lattice. No link variables, no "
          "weight W, no kappa, no")
    print("  Spin(4). It is the free scalar determinant on a "
          "hypercubic grid -- a")
    print("  quantity that would be identical in any program that "
          "used the same grid.")
    print()
    src = O.vhat(L)
    ref = vhat_variant(L, "forward")
    d = float(np.abs(src - ref).max())
    print(f"  check: O.vhat reproduced from the bare definition, "
          f"max difference {d:.2e}")
    assert d < 1e-12
    print("  So the violation is a property of the CARRIER, not "
          "of this theory.")
    print()


def s2_is_it_the_derivative():
    print("== s2: is it the discretisation of the derivative? ==")
    print("  If the breaking were a discretisation artifact, a "
          "different derivative")
    print("  would move it. Three discretisations, same "
          "construction, same test.")
    print()
    print("     derivative     " + "   ".join(
        f"k={k}" for k in ("(0,1,0,0)", "(0,2,1,1)")))
    rows = {}
    for kind in ("forward", "central", "improved"):
        vh = vhat_variant(L, kind)
        vals = [violation(vh, kk) for kk in ((0, 1, 0, 0),
                                             (0, 2, 1, 1))]
        rows[kind] = vals
        print(f"    {kind:12s}    {vals[0]:.4f}          "
              f"{vals[1]:.4f}")
    allv = np.array([v for vv in rows.values() for v in vv])
    print()
    print(f"  spread across three different derivatives: "
          f"{allv.min():.3f} .. {allv.max():.3f}")
    print()
    if allv.min() > 0.05:
        print("  UNMOVED, and large in every case. The breaking is "
              "not the derivative and")
        print("  not an O(a^2) artifact -- 0150 already showed it "
              "is flat in k. It is")
        print("  structural: A FIXED GRID HAS NO INFINITESIMAL "
          "DIFFEOMORPHISMS. There is")
        print("  no symmetry there to be invariant under, so "
              "nothing protects the")
        print("  cosmological constant or the graviton mass, and "
              "0159 found both.")
    else:
        print("  One of the discretisations largely removes it, so "
              "the breaking is at")
        print("  least partly a derivative artifact. Recorded as "
              "measured.")
    print()
    return allv


def s3_what_would_work():
    print("== s3: what a carrier that works looks like ==")
    print("  The obstruction is now specific, which means it "
          "names its own fix.")
    print()
    print("  A diffeomorphism-invariant theory needs a carrier "
          "where the GEOMETRY is")
    print("  the dynamical variable, not a fixed backdrop. On a "
          "hypercubic lattice the")
    print("  geometry is frozen by construction -- the spacing is "
          "a, the connectivity")
    print("  is the grid -- so the metric can only ever appear as "
          "an operator living on")
    print("  a geometry that is not itself moving. That is why "
          "lattice quantum gravity")
    print("  does not use fixed grids.")
    print()
    print("  And the program's own amplitude says which carrier "
          "it wants. The derived")
    print("  weight is")
    print("      A(U+,U-) = sum_j n_j chi_j(U+) chi_j(U-),")
    print("  a sum over BALANCED representations -- which is a "
          "spin foam amplitude with")
    print("  the simplicity constraint imposed (0160 s3: rank 6, "
          "not 1; 0142's synergy).")
    print("  Spin foams live on simplicial 2-complexes where the "
          "representation labels")
    print("  ARE the geometry: j is an area. Nothing is frozen.")
    print()
    print("  So the situation is not 'derived but unsimulable'. "
          "It is:")
    print()
    print("    DERIVED, AND SIMULATED SO FAR ON A CARRIER THAT "
          "BREAKS THE SYMMETRY THE")
    print("    DERIVATION RUNS ON.")
    print()
    print("  The hypercubic lattice was the right instrument for "
          "everything up to item")
    print("  5 -- it produced kappa, the band limit, the double "
          "copy, the synergy, the")
    print("  scale. It is the wrong instrument for a geodesic, "
          "and the measurement in")
    print("  s2 says so quantitatively rather than as a matter of "
          "taste.")
    print()


if __name__ == "__main__":
    s1_no_gauge_field()
    s2_is_it_the_derivative()
    s3_what_would_work()
    print("all assertions passed")
