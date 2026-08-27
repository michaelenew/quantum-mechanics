"""0099 -- the surface ordering: chosen by the Gauss law, and then
it does not matter.

The nonabelian boundary's 4D residue (0108) was one question: which
composition scheme does a closed 2-surface use, and does anything
observable depend on it? The filter-gravity program (lucid
0010-0011) supplies the selection principle: gravity requires the
boundary to read EXACTLY the enclosed content (the Gauss law --
otherwise the trust field has fake sources). This module settles the
question at the 3-cell tier:

  s1  A LAWFUL SCHEME EXISTS, CONSTRUCTIVELY. The six faces of a
      cube, coherently oriented, glue by word substitution
      (polygon gluing); the glued boundary word FREELY REDUCES TO
      EMPTY -- a symbolic proof, configuration-independent, that
      the transported (lassoed) composite of the six faces is
      exactly 1. Verified numerically on random Haar configs to
      machine precision: the closed boundary of an empty region
      reads 1. (The lattice Bianchi identity, found by the gluing
      algorithm rather than recalled.)
  s2  THE SCHEME IS GAUGE. Two different gluing schemes (different
      root face, different absorption order) both reduce to empty;
      with a source g inserted on one face, their composites are
      CONJUGATES of g -- element different, class identical to
      machine precision. Every class observable (hence the boundary
      capacity, 0108 s2) is scheme-independent among lawful
      schemes. The 4D 'choice' is a gauge choice.
  s3  UNLAWFUL SCHEMES FAKE MASS. The naive transport-free product
      of the six faces reads a NONZERO class on an empty cube --
      fake enclosed content, growing with the link scale (the
      commutators) -- which is exactly what the filter-gravity
      Gauss requirement forbids. The physics' surface ordering is
      thereby chosen by the desired gravity outcome, and among the
      lawful schemes nothing physical remains to choose.
"""

import numpy as np

# links of the unit cube: X[j][k] -> id 0+2j+k, Y[i][k] -> 4+2i+k,
# Z[i][j] -> 8+2i+j
FACES = {
    "bottom": [(4, 1), (2, 1), (6, -1), (0, -1)],
    "top":    [(1, 1), (7, 1), (3, -1), (5, -1)],
    "front":  [(0, 1), (10, 1), (1, -1), (8, -1)],
    "back":   [(9, 1), (3, 1), (11, -1), (2, -1)],
    "left":   [(8, 1), (5, 1), (9, -1), (4, -1)],
    "right":  [(6, 1), (11, 1), (7, -1), (10, -1)],
}


def qmul(a, b):
    w1, x1, y1, z1 = a
    w2, x2, y2, z2 = b
    return np.array([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
                     w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
                     w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2])


def qinv(a):
    return np.array([a[0], -a[1], -a[2], -a[3]])


ID = np.array([1.0, 0, 0, 0])


def hol(word, links):
    out = ID.copy()
    for lid, s in word:
        out = qmul(out, links[lid] if s > 0 else qinv(links[lid]))
    return out


def reduce_word(w):
    done = False
    while not done:
        done = True
        for i in range(len(w) - 1):
            if w[i][0] == w[i + 1][0] and w[i][1] == -w[i + 1][1]:
                w = w[:i] + w[i + 2:]
                done = False
                break
    return w


def glue(start, order):
    """Polygon-glue the cube's faces; return the substitution log
    [(prefix_word_incl_edge, rotated_face_word), ...] and final W."""
    W = list(FACES[start])
    used = {start}
    subs = []
    names = [n for n in order if n != start]
    while len(used) < 6:
        hit = None
        for i, (lid, s) in enumerate(W):
            for fn in names:
                if fn in used:
                    continue
                fw = FACES[fn]
                for j, (l2, s2) in enumerate(fw):
                    if l2 == lid and s2 == -s:
                        hit = (i, fn, j)
                        break
                if hit:
                    break
            if hit:
                break
        assert hit, "gluing stuck"
        i, fn, j = hit
        rot = FACES[fn][j:] + FACES[fn][:j]     # starts with l^-s
        C = rot[1:]
        subs.append((W[:i + 1], rot))
        W = reduce_word(W[:i] + C + W[i + 1:])
        used.add(fn)
    return subs, W


def composite(subs, start, links, source=None, source_face=None):
    """D_n ... D_1 . P_f0 (with optional source g multiplying one
    face's holonomy): the transported surface-ordered product."""
    def face_hol(word, fn):
        P = hol(word, links)
        if source is not None and fn == source_face:
            P = qmul(P, source)
        return P

    C = face_hol(FACES[start], start)
    for prefix, rot in subs:
        fn = next(n for n, w in FACES.items()
                  if sorted(w) == sorted(rot))
        A = hol(prefix, links)
        D = qmul(qmul(A, face_hol(rot, fn)), qinv(A))
        C = qmul(D, C)
    return C


def rand_links(rng, tau=None):
    links = {}
    for lid in range(12):
        if tau is None:
            v = rng.normal(size=4)
            links[lid] = v / np.linalg.norm(v)
        else:
            th = np.sqrt(tau) * abs(rng.normal())
            ax = rng.normal(size=3)
            ax /= np.linalg.norm(ax)
            links[lid] = np.concatenate([[np.cos(th)],
                                         np.sin(th) * ax])
    return links


ORDER_A = ["bottom", "front", "right", "back", "left", "top"]
ORDER_B = ["top", "left", "back", "right", "front", "bottom"]


def s1_lawful():
    print("== s1: the lawful scheme, constructed ==")
    subs, W = glue("bottom", ORDER_A)
    print(f"  glued boundary word after absorbing all 6 faces: "
          f"{len(W)} letters (freely reduced)")
    assert W == []
    print("  -> EMPTY: symbolic proof that the lassoed composite = 1"
          " for every configuration")
    rng = np.random.default_rng(2)
    worst = 0.0
    for _ in range(5):
        links = rand_links(rng)
        C = composite(subs, "bottom", links)
        worst = max(worst, np.abs(C - ID).max())
    print(f"  numeric check, random Haar configs: max |C - 1| = "
          f"{worst:.1e}")
    assert worst < 1e-12
    print("  the closed boundary of an empty region reads exactly "
          "1: the Gauss law\n")
    return subs


def s2_gauge(subs_a):
    print("== s2: the scheme is gauge ==")
    subs_b, Wb = glue("top", ORDER_B)
    assert Wb == []
    rng = np.random.default_rng(3)
    worst_cls, worst_el = 0.0, 0.0
    for _ in range(5):
        links = rand_links(rng)
        v = rng.normal(size=4)
        g = v / np.linalg.norm(v)            # the enclosed source
        Ca = composite(subs_a, "bottom", links, g, "front")
        Cb = composite(subs_b, "top", links, g, "front")
        ca = np.arccos(np.clip(abs(Ca[0]), -1, 1))
        cb = np.arccos(np.clip(abs(Cb[0]), -1, 1))
        cg = np.arccos(np.clip(abs(g[0]), -1, 1))
        worst_cls = max(worst_cls, abs(ca - cb), abs(ca - cg))
        worst_el = max(worst_el, np.abs(Ca - Cb).max())
    print(f"  two schemes, source g on a face: class(C_A) = "
          f"class(C_B) = class(g) to {worst_cls:.1e};")
    print(f"  the group elements differ (max component diff "
          f"{worst_el:.2f}): conjugate, not equal")
    assert worst_cls < 1e-12 and worst_el > 0.1
    print("  every class observable -- including the boundary "
          "capacity (0108) -- is scheme-")
    print("  independent among lawful schemes: the 4D choice is a "
          "gauge choice\n")


def s3_fake_mass(subs_a):
    print("== s3: unlawful schemes fake mass ==")
    rng = np.random.default_rng(4)
    print("   tau_link   naive |class| RMS   lawful |class| RMS")
    for tau in (0.02, 0.05, 0.1):
        cn, cl = [], []
        for _ in range(2000):
            links = rand_links(rng, tau)
            Cn = ID.copy()
            for fn in ORDER_A:
                Cn = qmul(Cn, hol(FACES[fn], links))
            cn.append(np.arccos(np.clip(abs(Cn[0]), -1, 1)))
            Cl = composite(subs_a, "bottom", links)
            cl.append(np.arccos(np.clip(abs(Cl[0]), -1, 1)))
        rn = float(np.sqrt(np.mean(np.array(cn) ** 2)))
        rl = float(np.sqrt(np.mean(np.array(cl) ** 2)))
        print(f"   {tau:5.2f}      {rn:.4f}             {rl:.1e}")
        assert rn > 100 * max(rl, 1e-12)
    print("  the transport-free product reads NONZERO class on an "
          "EMPTY cube -- fake enclosed")
    print("  mass from bad bookkeeping, at the commutator scale. "
          "The filter-gravity Gauss")
    print("  requirement (boundary = enclosed content, exactly) "
          "excludes these schemes;")
    print("  among the lawful ones, s2 says nothing physical "
          "remains to choose\n")


if __name__ == "__main__":
    subs = s1_lawful()
    s2_gauge(subs)
    s3_fake_mass(subs)
    print("all assertions passed")
