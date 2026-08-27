"""0126 -- what is missing for the full port: a tier census, and the
gap that turned out to matter most.

0125 audited three items and found (A) and (C) continuous, N's
definition continuous, N's candidate set a Z_N artefact. The natural
follow-up is the general one: WHICH standing results are statements
about the continuous theory, and which never left the toy?

  s1  THE TIER CENSUS. Three buckets -- already lifted, trivially
      portable, and Z_N-only-and-load-bearing. The third bucket is
      longer than the board suggests, and one entry in it is the
      program's only observational route.
  s2  THE GAP THAT MATTERS MOST, and it is not on any list. 0074 s3
      DERIVED the nonabelian amplitude's multiplicities from the
      frame measure and reported the profile as "peaked, not
      monotone". Every module from 0091 onward -- the entire
      continuity front -- instead uses FLAT counting, all n_j = 1,
      described in 0091's own docstring as "flat counting". So the
      weight that was measured is not the weight that was derived.
      Measured here: kappa across plausible profiles runs 9.0 to
      16.0, and because the hierarchy is EXPONENTIAL in kappa, xi/a
      runs from 6e9 to 8e17. EIGHT ORDERS OF MAGNITUDE, set by a
      simplification nobody had priced.
  s3  THE PUNCH LIST.
"""

import numpy as np

TH = np.linspace(1e-9, np.pi - 1e-9, 400001)
B0, B1 = 11 / (24 * np.pi ** 2), 17 / (96 * np.pi ** 4)


def chi(n):
    return np.sin(n * TH) / np.sin(TH)


def kappa(ns):
    A = sum(c * chi(n) for n, c in enumerate(ns, start=1))
    W = np.maximum(A ** 2, 1e-300)
    sel = TH < 0.15
    return float(-2 * np.polyfit(TH[sel], np.log(W[sel]), 4)[-3])


def xi_over_a(beta):
    g2 = 4.0 / beta
    return 1.0 / ((B0 * g2) ** (-B1 / (2 * B0 ** 2))
                  * np.exp(-1 / (2 * B0 * g2)))


CENSUS = [
    ("LIFTED to SU(2) / continuum", [
        ("Born square positivity from counting", "0074 s2, 200 SU(2) countings"),
        ("reflection positivity from counting", "0111/0123, SU(2)"),
        ("band-as-budget (sector cost ln N)", "0108, SU(2) characters"),
        ("(A) the interacting measure", "0091-0124, 4D SU(2)"),
        ("(C) area law, Unruh, horizon", "free scalar/graviton, continuum PDE"),
    ]),
    ("PORTS TRIVIALLY (it is the chain rule)", [
        ("action = prequential code length", "0095 demonstrates on 2D Z_N;"
                                             " the identity is generic"),
    ]),
    ("Z_N ONLY, NOT LIFTED, LOAD-BEARING", [
        ("the level's candidate set (the ladder)", "0072/0081 - shown toy-only by 0125"),
        ("Lambda quantised, Lambda.V in (2pi/N)Z", "0071/0086 - THE ONLY OBSERVATIONAL ROUTE"),
        ("the two-ledger theorem's proof", "0077, 'run in the Z_N toy'"),
        ("innovation capacity = ln N as a number", "0095, the 2D Z_N boundary"),
        ("the bridge floor n* = 58", "0096, priced over the ladder"),
    ]),
]


def s1_census():
    print("== s1: the tier census ==")
    for bucket, rows in CENSUS:
        print(f"\n  {bucket}")
        for claim, where in rows:
            print(f"    - {claim:42s} {where}")
    print()
    print("  Two notes so the third bucket is not read as worse "
          "than it is. The two-ledger")
    print("  theorem has a PARTIAL lift: lucid 0027 showed record "
          "noise cannot produce the")
    print("  Born weight's exact zeros, which is the SU(2)-tier "
          "form of 'the record ledger")
    print("  cannot reach amplitude structure'. And action = code "
          "length is the chain rule;")
    print("  what is Z_N is the CAPACITY attached to it, not the "
          "identity.")
    print()
    print("  The entry that should worry us is the Lambda "
          "quantisation. 0069's falsifiability")
    print("  path had exactly one credible observational line, and "
          "its mechanism -- total")
    print("  curvature quantised mod N -- is a statement about a "
          "finite ring.\n")


def s2_the_flat_counting_gap():
    print("== s2: the gap that matters most, and it is on no list "
          "==")
    print("  0074 s3 DERIVED the nonabelian amplitude's "
          "multiplicities from the frame measure")
    print("  and reported the profile as 'peaked, not monotone'. "
          "From 0091 onward every")
    print("  module uses FLAT counting instead -- 0091's own "
          "docstring says 'flat counting'.")
    print("  So the weight the continuity front measured is not the "
          "weight 0074 derived.")
    print()
    print("     multiplicity profile           kappa      xi/a")
    prof = {
        "flat (what was simulated)": [1] * 6,
        "peaked, mild": [1, 2, 3, 3, 2, 1],
        "peaked, strong": [1, 3, 6, 6, 3, 1],
        "rising": [1, 2, 3, 4, 5, 6],
        "falling": [6, 5, 4, 3, 2, 1],
    }
    ks = {}
    for lbl, ns in prof.items():
        k = kappa(ns)
        ks[lbl] = k
        print(f"   {lbl:30s} {k:7.3f}   {xi_over_a(k):.2e}")
    lo, hi = min(ks.values()), max(ks.values())
    print()
    print(f"  kappa runs {lo:.1f} to {hi:.1f} -- a factor 1.8. But "
          f"the hierarchy is EXPONENTIAL")
    print(f"  in kappa, so xi/a runs {xi_over_a(lo):.0e} to "
          f"{xi_over_a(hi):.0e}: EIGHT ORDERS OF MAGNITUDE.")
    assert xi_over_a(hi) / xi_over_a(lo) > 1e7
    print()
    print("  The continuity front's headline number -- xi/a ~ 10^13, "
          "untuned -- therefore")
    print("  carries an unpriced dependence on a simplification. "
          "The front's STRUCTURAL")
    print("  results survive (there is still no dial; asymptotic "
          "freedom still supplies the")
    print("  separation; Lorentz restoration was measured on "
          "whatever weight was used). What")
    print("  does not survive unqualified is the NUMBER.\n")


def s3_punch_list():
    print("== s3: the punch list for the full port ==")
    items = [
        ("1", "Derive the SU(2) amplitude's multiplicities",
         "0074 s3 has a derivation and a profile; nothing since uses it. "
         "Re-derive, then re-run the coupling. This is the largest single "
         "unpriced dependence in the program."),
        ("2", "Port or retire the Lambda quantisation",
         "The mechanism is total curvature mod N on a closed surface. On "
         "SU(2) the analogue is a pi_1 / centre statement, not a mod-N one. "
         "Until it is ported the program has NO observational route."),
        ("3", "Find a continuum constraint on the level, or accept there is none",
         "Every level passes the SU(2) tests run so far. Either a sharper "
         "continuum test exists, or the candidate set is all integers and "
         "0096's floor must be repriced."),
        ("4", "Lift the two-ledger theorem properly",
         "lucid 0027 gives a partial SU(2) form via the exact zeros. The "
         "full statement is still the Z_N proof."),
        ("5", "Re-price the level measurement",
         "n* = 58 was computed over the ladder. Without the ladder the "
         "prior's support changes and the floor rises."),
    ]
    for n, head, body in items:
        print(f"  {n}. {head}")
        for line in _wrap(body, 68):
            print(f"     {line}")
        print()
    print("  Ordering note: (1) is first because it is cheap, it is "
          "self-contained, and every")
    print("  number downstream of the coupling depends on it. (2) "
          "is second because it is the")
    print("  difference between a theory with a falsifiable line "
          "and one without.\n")


def _wrap(t, w):
    out, cur = [], ""
    for word in t.split():
        if len(cur) + len(word) + 1 > w:
            out.append(cur)
            cur = word
        else:
            cur = (cur + " " + word).strip()
    if cur:
        out.append(cur)
    return out


if __name__ == "__main__":
    s1_census()
    s2_the_flat_counting_gap()
    s3_punch_list()
    print("all assertions passed")
