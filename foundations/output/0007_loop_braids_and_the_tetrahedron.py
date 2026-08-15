"""Loop braids and the tetrahedron: the interaction algebra of the
movie, computed.

The movie synthesis: 3+1 configurations slice into loops leapfrogging
in 3-space, with triple points as interaction events.  Two questions
have exact finite answers:

  s1  WHICH MOVES ARE CONSISTENT.  The motion group of loops (the
      loop braid group) acts on meridian data by conjugation:
      leapfrog sigma_i sends (a_i, a_{i+1}) to (a_{i+1},
      a_{i+1}^-1 a_i a_{i+1}); exchange rho_i swaps.  Computed as
      free-group automorphisms (exact reduced-word arithmetic):
      the braid relation for sigma, the symmetric relations for
      rho, and the mixed relations are CHECKED individually -- the
      code reports which of the two candidate mixed braid relations
      holds and which fails.  The failing one is the 'forbidden
      move' whose imposition would collapse loop-knotting.

  s2  RECOVERY CAN BE IMPOSSIBLE.  The leapfrog has INFINITE order
      in its action (iterating sigma_1 grows the conjugating word
      without bound, verified to depth 40): in the braided tier
      there are round trips whose loss is never recovered by
      repetition -- the odometer limit at the group level, and the
      sharp form of 'traverse the dual path to recover': recovery
      cost is the order of your holonomy element, which can be
      infinite.

  s3  THE TETRAHEDRON CENSUS.  Consistency of triple points in the
      movie is the Zamolodchikov tetrahedron equation, one level
      above Yang-Baxter.  Exhaustive censuses over GF(2):
        - Yang-Baxter (R on X^2, |X| = 2): checked over all 24
          bijections of X^2 -- count reported;
        - tetrahedron (R on X^3): checked over all 168 invertible
          linear maps AND all 40320 bijections of X^3 -- counts
          reported.
      The measured rarity quantifies how much stronger a constraint
      consistent triple interactions are than consistent pairwise
      ones -- the 3+1 analog of 0066's census.

Run directly for the verification suite.
"""

from __future__ import annotations

import itertools


# =====================================================================
# free group reduced words and automorphisms
# =====================================================================

def reduce_word(word):
    out = []
    for g in word:
        if out and out[-1] == -g:
            out.pop()
        else:
            out.append(g)
    return tuple(out)


def concat(*words):
    total = []
    for w in words:
        total.extend(w)
    return reduce_word(total)


def invert(word):
    return tuple(-g for g in reversed(word))


def apply_auto(images, word):
    """images[i] = image word of generator i+1."""
    out = []
    for g in word:
        img = images[abs(g) - 1]
        out.extend(img if g > 0 else invert(img))
    return reduce_word(out)


def compose(first, second):
    """Apply `first`, then `second` (as maps); images of generators."""
    return tuple(apply_auto(second, img) for img in first)


def gen(i):
    return (i,)


def identity_auto(n):
    return tuple(gen(i + 1) for i in range(n))


def sigma(i, n):
    """Leapfrog: a_i -> a_{i+1}, a_{i+1} -> a_{i+1}^-1 a_i a_{i+1}."""
    images = list(identity_auto(n))
    images[i - 1] = gen(i + 1)
    images[i] = concat(invert(gen(i + 1)), gen(i), gen(i + 1))
    return tuple(images)


def rho(i, n):
    images = list(identity_auto(n))
    images[i - 1] = gen(i + 1)
    images[i] = gen(i)
    return tuple(images)


def verify_loop_braid_relations() -> None:
    n = 3
    s1, s2 = sigma(1, n), sigma(2, n)
    r1, r2 = rho(1, n), rho(2, n)
    checks = [
        ("sigma braid:  s1 s2 s1 = s2 s1 s2",
         compose(compose(s1, s2), s1), compose(compose(s2, s1), s2)),
        ("rho involution:  r1 r1 = id",
         compose(r1, r1), identity_auto(n)),
        ("rho braid:  r1 r2 r1 = r2 r1 r2",
         compose(compose(r1, r2), r1), compose(compose(r2, r1), r2)),
        ("mixed A:  r1 r2 s1 = s2 r1 r2",
         compose(compose(r1, r2), s1), compose(compose(s2, r1), r2)),
        ("mixed B:  s1 s2 r1 = r2 s1 s2",
         compose(compose(s1, s2), r1), compose(compose(r2, s1), s2)),
        ("forbidden:  r1 s2 s1 = s2 s1 r2",
         compose(compose(r1, s2), s1), compose(compose(s2, s1), r2)),
    ]
    holds = {}
    for name, left, right in checks:
        holds[name] = (left == right)
        print(f"    {name:<38} {'holds' if left == right else 'FAILS'}")
    assert holds["sigma braid:  s1 s2 s1 = s2 s1 s2"]
    assert holds["rho involution:  r1 r1 = id"]
    assert holds["rho braid:  r1 r2 r1 = r2 r1 r2"]
    assert holds["mixed A:  r1 r2 s1 = s2 r1 r2"]
    assert holds["mixed B:  s1 s2 r1 = r2 s1 s2"]
    assert not holds["forbidden:  r1 s2 s1 = s2 s1 r2"]
    print()
    print("  The loop braid presentation emerges from the conjugation")
    print("  action itself: braid relations for the leapfrog, symmetric")
    print("  relations for the exchange, exactly ONE of the two mixed")
    print("  braid relations -- the other is the forbidden move, and")
    print("  imposing it is what would collapse loop-knotting to")
    print("  permutation statistics.  Consistency at the movie's events")
    print("  is a genuine algebra, not a bookkeeping choice.")


def verify_infinite_order() -> None:
    n = 2
    s1 = sigma(1, n)
    current = identity_auto(n)
    lengths = []
    for _ in range(40):
        current = compose(current, s1)
        lengths.append(sum(len(w) for w in current))
    assert all(b >= a for a, b in zip(lengths, lengths[1:]))
    assert lengths[-1] > lengths[3]
    print(f"    word length of sigma_1^k acting on (a1, a2):")
    print(f"    k = 1, 5, 10, 20, 40  ->  "
          f"{[lengths[i - 1] for i in (1, 5, 10, 20, 40)]}")
    print()
    print("  The leapfrog's action has infinite order: no power returns")
    print("  to the identity.  In the braided tier, some round-trip")
    print("  losses are NEVER recovered by repetition -- 'traverse the")
    print("  dual path' generalizes to 'close the holonomy word', and")
    print("  for infinite-order monodromy there is no closing word.")


# =====================================================================
# 3. the tetrahedron census
# =====================================================================

def yang_baxter_census():
    """All bijections of X^2, |X| = 2: R12 R23 R12 = R23 R12 R23."""
    states = list(itertools.product((0, 1), repeat=3))
    pairs = list(itertools.product((0, 1), repeat=2))
    count = 0
    for perm in itertools.permutations(range(4)):
        table = {pairs[i]: pairs[perm[i]] for i in range(4)}

        def r12(s):
            a, b = table[(s[0], s[1])]
            return (a, b, s[2])

        def r23(s):
            a, b = table[(s[1], s[2])]
            return (s[0], a, b)
        if all(r12(r23(r12(s))) == r23(r12(r23(s))) for s in states):
            count += 1
    return count, 24


def place(table, positions, state):
    triple = tuple(state[p] for p in positions)
    image = table[triple]
    out = list(state)
    for p, v in zip(positions, image):
        out[p] = v
    return tuple(out)


TETRA_PLACEMENTS = [(0, 1, 2), (0, 3, 4), (1, 3, 5), (2, 4, 5)]


def satisfies_tetrahedron(table, states):
    for s in states:
        left = s
        for pos in TETRA_PLACEMENTS:
            left = place(table, pos, left)
        right = s
        for pos in reversed(TETRA_PLACEMENTS):
            right = place(table, pos, right)
        if left != right:
            return False
    return True


def tetrahedron_census():
    states = list(itertools.product((0, 1), repeat=6))
    triples = list(itertools.product((0, 1), repeat=3))
    # linear invertible maps on GF(2)^3
    linear_hits = 0
    linear_total = 0
    for cols in itertools.product(range(8), repeat=3):
        # invertibility over GF(2): columns linearly independent
        c1, c2, c3 = cols
        span = {0, c1, c2, c1 ^ c2, c3, c1 ^ c3, c2 ^ c3, c1 ^ c2 ^ c3}
        if len(span) != 8:
            continue
        linear_total += 1
        table = {}
        for t in triples:
            v = 0
            for bit, col in zip(t, cols):
                if bit:
                    v ^= col
            table[t] = ((v >> 2) & 1, (v >> 1) & 1, v & 1)
        if satisfies_tetrahedron(table, states):
            linear_hits += 1
    # all bijections of X^3
    bij_hits = 0
    for perm in itertools.permutations(range(8)):
        table = {triples[i]: triples[perm[i]] for i in range(8)}
        if satisfies_tetrahedron(table, states):
            bij_hits += 1
    return linear_hits, linear_total, bij_hits, 40320


def verify_the_census() -> None:
    yb_hits, yb_total = yang_baxter_census()
    print(f"    Yang-Baxter (pair events, |X| = 2):    "
          f"{yb_hits} / {yb_total} bijections of X^2")
    lin_hits, lin_total, bij_hits, bij_total = tetrahedron_census()
    print(f"    tetrahedron (triple events, linear):   "
          f"{lin_hits} / {lin_total} invertible linear maps on X^3")
    print(f"    tetrahedron (triple events, all):      "
          f"{bij_hits} / {bij_total} bijections of X^3")
    assert yb_hits >= 1 and bij_hits >= 1
    yb_frac = yb_hits / yb_total
    bij_frac = bij_hits / bij_total
    assert bij_frac < yb_frac
    print()
    print(f"    consistent fraction: pair events {yb_frac:.3f}, "
          f"triple events {bij_frac:.4f}")
    print()
    print("  Consistency of triple interactions (the Zamolodchikov")
    print("  tetrahedron equation -- the axiom of braided monoidal")
    print("  2-categories, i.e. of the movie's events) is measurably a")
    print("  far stronger constraint than pairwise Yang-Baxter: the")
    print("  fraction of admissible interaction rules collapses as the")
    print("  event order rises.  The 3+1 world has fewer consistent")
    print("  interaction algebras to choose from, not more.")


def run_verification_suite() -> None:
    sections = [
        ("Which moves are consistent: the loop braid relations",
         verify_loop_braid_relations),
        ("Recovery can be impossible: infinite-order leapfrog",
         verify_infinite_order),
        ("The tetrahedron census", verify_the_census),
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
