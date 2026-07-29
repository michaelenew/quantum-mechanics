"""
Triangle cocycle / frustration check.

Presses on the cocycle framing of recursive consistency (foundations/0004).

Setup: three sites A, B, C with dichotomic (+/-1) observables and pairwise
correlators E_AB, E_BC, E_CA in [-1, 1]. Recursive consistency asks: when do
these pairwise correlators come from a single joint distribution over
(sigma_A, sigma_B, sigma_C) in {+1,-1}^3?

Derivation. The 8 outcomes {+,-}^3 fall into 4 sign-flip pairs (a,b,c) and
(-a,-b,-c), which give the same three pairwise products. Solving,

    q_1 = P(+,+,+) + P(-,-,-) = (1 + E_AB + E_BC + E_CA) / 4
    q_2 = P(+,+,-) + P(-,-,+) = (1 + E_AB - E_BC - E_CA) / 4
    q_3 = P(+,-,+) + P(-,+,-) = (1 - E_AB - E_BC + E_CA) / 4
    q_4 = P(+,-,-) + P(-,+,+) = (1 - E_AB + E_BC - E_CA) / 4

A classical joint exists iff every q_i >= 0, i.e. the four EVEN-parity
inequalities

    1 + s_1 E_AB + s_2 E_BC + s_3 E_CA >= 0     (s_1 s_2 s_3 = +1)

hold. Violation of any = frustration = no global assignment consistent with the
pairwise correlators. The polytope is a tetrahedron; volume 1/3 of the cube.

Two observations we press on here:

(A) THE HOLONOMY. Compose correlators around the loop: H = E_AB * E_BC * E_CA.
    In (+1,+1,+1) H = +1 with a global joint (trivial cocycle). In (-1,-1,-1)
    H = -1 with NO global joint (frustrated, nontrivial cocycle). H is the
    classical (Z/2) analog of the quantum Berry phase around a loop.

(B) QUANTUM DOES NOT HELP HERE. For COMPATIBLE (commuting) observables on the
    three sites, QM cannot violate these facet inequalities either - it yields
    a joint distribution of definite outcomes. Contextuality only appears when
    we enlarge the scenario to INCOMPATIBLE observables (each site chooses one
    of several bases - Bell/CHSH, output/0002). This localizes 'quantumness'
    to CHOICE OF CONTEXT, not to interaction-graph topology alone.

Pure stdlib.
Run:  python3 0003_triangle_cocycle_check.py
"""


def facet_slacks(E):
    """The four even-parity classical-triangle inequalities. Each is 4*q_i."""
    E_AB, E_BC, E_CA = E
    return {
        "(+, +, +)": 1 + E_AB + E_BC + E_CA,
        "(+, -, -)": 1 + E_AB - E_BC - E_CA,
        "(-, -, +)": 1 - E_AB - E_BC + E_CA,
        "(-, +, -)": 1 - E_AB + E_BC - E_CA,
    }


def has_global_section(E, tol=1e-12):
    return all(v >= -tol for v in facet_slacks(E).values())


def holonomy(E):
    return E[0] * E[1] * E[2]


def joint_or_none(E, tol=1e-9):
    """Return the (essentially unique modulo the sign-flip symmetry) joint
    distribution recovering these three correlators, or None if infeasible.
    We split each q_i evenly between its two outcomes - the max-entropy choice
    consistent with the pairwise data alone."""
    slacks = facet_slacks(E)
    for v in slacks.values():
        if v < -tol:
            return None
    q1, q2, q3, q4 = (slacks[k] / 4 for k in
                      ("(+, +, +)", "(+, -, -)", "(-, -, +)", "(-, +, -)"))
    return {
        (+1, +1, +1): q1 / 2, (-1, -1, -1): q1 / 2,
        (+1, +1, -1): q2 / 2, (-1, -1, +1): q2 / 2,
        (+1, -1, +1): q3 / 2, (-1, +1, -1): q3 / 2,
        (+1, -1, -1): q4 / 2, (-1, +1, +1): q4 / 2,
    }


def report(name, E):
    print(name)
    print(f"    E = (E_AB, E_BC, E_CA) = {E}")
    print("    facet slacks (>= 0 iff frustration-free):")
    for k, v in facet_slacks(E).items():
        marker = " " if v >= -1e-12 else " <-- VIOLATED"
        print(f"        {k}: {v:+.4f}{marker}")
    print(f"    holonomy  E_AB * E_BC * E_CA  =  {holonomy(E):+.4f}")
    j = joint_or_none(E)
    if j is None:
        print("    NO global section - FRUSTRATED (nontrivial cocycle around loop)")
    else:
        ach = (
            sum(o[0] * o[1] * p for o, p in j.items()),
            sum(o[1] * o[2] * p for o, p in j.items()),
            sum(o[2] * o[0] * p for o, p in j.items()),
        )
        print("    global section EXISTS - cocycle is trivial on this triangle")
        print(f"    recovered correlators from joint: "
              f"({ach[0]:+.4f}, {ach[1]:+.4f}, {ach[2]:+.4f})")
        ok = all(abs(a - e) < 1e-10 for a, e in zip(ach, E))
        print(f"    match: {'OK' if ok else 'MISMATCH'}")
    print()


if __name__ == "__main__":
    print("Recursive-consistency cocycle on a triangle A-B-C.\n")
    print("(1) Extremes:\n")
    report("All agree pairwise  E = (+1, +1, +1):", (+1.0, +1.0, +1.0))
    report("All disagree pairwise  E = (-1, -1, -1):", (-1.0, -1.0, -1.0))

    print("(2) Interior samples:\n")
    report("Weakly aligned:", (+0.3, +0.4, +0.2))
    report("Mixed, at boundary of classical polytope:", (+0.5, +0.5, -0.5))
    report("Frustrated interior:", (-0.6, -0.6, -0.6))

    print("(3) Volume of the classical (frustration-free) polytope:\n")
    N = 60
    total = 0
    ok = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                E = (-1 + 2 * i / (N - 1),
                     -1 + 2 * j / (N - 1),
                     -1 + 2 * k / (N - 1))
                total += 1
                if has_global_section(E):
                    ok += 1
    frac = ok / total
    print(f"    fraction of [-1,1]^3 that is frustration-free: "
          f"{frac:.4f}   ({ok}/{total} grid points)")
    print(f"    expected exact value 1/3 = 0.3333  (tetrahedron in cube).")
    print(f"    match: {'OK' if abs(frac - 1/3) < 0.02 else 'CHECK'}")
    print()

    print("Reading:")
    print("  * Compatible observables on a triangle: the classical polytope")
    print("    IS the quantum-allowed set. No 'quantum advantage' shows up.")
    print("  * Contextuality / Bell violation needs INCOMPATIBLE observables")
    print("    per site (a CHOICE of measurement basis) - Kochen-Specker,")
    print("    CHSH in output/0002.")
    print("  * The cocycle framing localizes the source of 'quantumness' to")
    print("    choice-of-context, not merely to interaction-graph topology.")
