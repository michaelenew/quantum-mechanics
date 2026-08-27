"""0100 -- the tiling: the Gauss law at block scale.

0109 proved the surface-ordering theorem at the single 3-cell and
argued the tiling. This module runs it: the same gluing algorithm on
the closed boundary of general boxes.

  For boxes (2,1,1), (2,2,2), (3,2,1): the glued boundary word
  freely reduces to EMPTY (symbolic, configuration-independent), and
  the transported composite of all boundary faces equals 1 to
  machine precision on random Haar configurations; with a source on
  one face, the composite's class equals the source's class. The
  Gauss law holds at block scale; the lawful schemes remain gauge.
"""

import numpy as np


def box_faces(Lx, Ly, Lz):
    """Outward-oriented boundary plaquette words for the box.
    Links: ('x',i,j,k): (i,j,k)->(i+1,j,k), etc."""
    F = {}
    for j in range(Ly):
        for k in range(Lz):
            F[("L", j, k)] = [(("z", 0, j, k), 1),
                              (("y", 0, j, k + 1), 1),
                              (("z", 0, j + 1, k), -1),
                              (("y", 0, j, k), -1)]
            F[("R", j, k)] = [(("y", Lx, j, k), 1),
                              (("z", Lx, j + 1, k), 1),
                              (("y", Lx, j, k + 1), -1),
                              (("z", Lx, j, k), -1)]
    for i in range(Lx):
        for k in range(Lz):
            F[("F", i, k)] = [(("x", i, 0, k), 1),
                              (("z", i + 1, 0, k), 1),
                              (("x", i, 0, k + 1), -1),
                              (("z", i, 0, k), -1)]
            F[("K", i, k)] = [(("z", i, Ly, k), 1),
                              (("x", i, Ly, k + 1), 1),
                              (("z", i + 1, Ly, k), -1),
                              (("x", i, Ly, k), -1)]
    for i in range(Lx):
        for j in range(Ly):
            F[("B", i, j)] = [(("y", i, j, 0), 1),
                              (("x", i, j + 1, 0), 1),
                              (("y", i + 1, j, 0), -1),
                              (("x", i, j, 0), -1)]
            F[("T", i, j)] = [(("x", i, j, Lz), 1),
                              (("y", i + 1, j, Lz), 1),
                              (("x", i, j + 1, Lz), -1),
                              (("y", i, j, Lz), -1)]
    return F


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


def glue(F, start):
    W = list(F[start])
    used = {start}
    subs = []
    while len(used) < len(F):
        hit = None
        for i, (lid, sgn) in enumerate(W):
            for fn, fw in F.items():
                if fn in used:
                    continue
                for j, (l2, s2) in enumerate(fw):
                    if l2 == lid and s2 == -sgn:
                        hit = (i, fn, j)
                        break
                if hit:
                    break
            if hit:
                break
        assert hit, "gluing stuck"
        i, fn, j = hit
        rot = F[fn][j:] + F[fn][:j]
        subs.append((W[:i + 1], fn, rot))
        W = reduce_word(W[:i] + rot[1:] + W[i + 1:])
        used.add(fn)
    return subs, W


def composite(F, subs, start, links, source=None, source_face=None):
    def fh(word, fn):
        Ph = hol(word, links)
        if source is not None and fn == source_face:
            Ph = qmul(Ph, source)
        return Ph

    C = fh(F[start], start)
    for prefix, fn, rot in subs:
        A = hol(prefix, links)
        C = qmul(qmul(qmul(A, fh(rot, fn)), qinv(A)), C)
    return C


def run_box(dims, rng):
    F = box_faces(*dims)
    start = next(iter(F))
    subs, W = glue(F, start)
    assert W == [], f"box {dims}: residue {len(W)}"
    lids = {lid for w in F.values() for lid, _ in w}
    links = {}
    for lid in lids:
        v = rng.normal(size=4)
        links[lid] = v / np.linalg.norm(v)
    C = composite(F, subs, start, links)
    err = np.abs(C - ID).max()
    v = rng.normal(size=4)
    g = v / np.linalg.norm(v)
    sf = list(F)[len(F) // 2]
    Cs = composite(F, subs, start, links, g, sf)
    dcls = abs(np.arccos(np.clip(abs(Cs[0]), -1, 1))
               - np.arccos(np.clip(abs(g[0]), -1, 1)))
    print(f"  box {dims}: {len(F)} faces -> glued word EMPTY; "
          f"|C - 1| = {err:.1e}; source class err = {dcls:.1e}")
    assert err < 1e-11 and dcls < 1e-11


if __name__ == "__main__":
    print("== the tiling: Gauss law on block boundaries ==")
    rng = np.random.default_rng(9)
    for dims in ((1, 1, 1), (2, 1, 1), (2, 2, 2), (3, 2, 1)):
        run_box(dims, rng)
    print("  the surface-ordering theorem holds at block scale: "
          "closed boundaries read 1,")
    print("  sources read their class, lawful schemes remain gauge")
    print("all assertions passed")
