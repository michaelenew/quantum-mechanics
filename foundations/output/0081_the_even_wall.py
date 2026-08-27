"""0081 -- the even wall: frames are indivisible, and the cover cures.

The sign-problem toy packaging (0069's queue): 0074 s1 found the
ledger is a Born square, gcd(F, N) = |sum_e w^{e^2 F}|^2 / N, for odd
N only, and filed even N as "the N = 2 degeneracy family at the
root." This stone settles WHAT KIND of obstruction even N is, and
finds the cure.

  s1  THE WALL, EXHAUSTIVELY. A counting amplitude is
      A(F) = sum_e c_e w^{eF} with c_e nonnegative INTEGERS (frame
      multiplicities); |A|^2 = N gcd demands the autocorrelation
      c * c = W-hat (the integer dual ledger). For N = 2, 4, 6, 8, 10
      exhaustive search over all counting vectors proves NO integer
      solution exists. (Odd N: c_e = #{x : x^2 = e} works, verified.)
  s2  NOT A POSITIVITY WALL. Real nonnegative solutions exist for
      every even N up to 16 (constructed via the PSD square root of
      the autocorrelation spectrum; all entries nonnegative, exact).
      At N = 2 the failure is one equation: 2 c_0 c_1 = 1 -- the
      ledger would need HALF A FRAME. The wall is integrality:
      quantization itself (frames come in wholes) is what rejects
      even N.
  s3  THE CURE IS THE DOUBLE COVER. Over doubled frames
      x in Z_{2N'} for the 2-part N' = 2^a (odd part unchanged),
      A(F) = [sum_{x in Z_{2 * 2^a}} w_{2^{a+1}}^{x^2 (F mod 2^a)}]
             * [odd-part Gauss sum at F mod m]
      gives |A|^2 = 4 N gcd(F, N) EXACTLY -- verified at every flux
      for N = 2, 4, 8, 16 (pure 2-powers, direct) and N = 6, 10, 12,
      24 (mixed, CRT with reduced arguments). The factor 4 is the
      cover degree squared. Frames come back whole on the cover.
  s4  THE READING. Even levels are the ledger's SPIN levels: they
      admit no frame counting on Z_N but a perfect one on its double
      cover -- the arithmetic shadow of a spin structure, sitting
      beside the Lorentzian congruence (0081-doc/0072-module: mod-4,
      i, Frobenius) as the second place the arithmetic knows about
      spin. Constraint-stack consequence: "N odd" (Born) softens
      from exclusion to covering instruction; the stack's smallest
      level stays N = 5 because the Lorentzian congruence
      independently rejects even N.
"""

import itertools
import math

import numpy as np


def gcd(a, b):
    return math.gcd(a, b)


def what(k, N):
    tot = 0
    for d in range(1, N + 1):
        if N % d == 0 and k % (N // d) == 0:
            phi = sum(1 for x in range(1, d + 1) if math.gcd(x, d) == 1)
            tot += phi * (N // d)
    return tot


def s1_the_wall():
    print("== s1: the wall, exhaustively ==")
    for N in (3, 5, 7, 9, 15):
        r = [sum(1 for x in range(N) if (x * x - m) % N == 0)
             for m in range(N)]
        acf = [sum(r[e] * r[(e + d) % N] for e in range(N))
               for d in range(N)]
        assert acf == [what(d, N) for d in range(N)]
    print("  odd N (3,5,7,9,15): c_e = #{x : x^2 = e} is a counting "
          "amplitude, exactly")
    for N in (2, 4, 6, 8, 10):
        target = [what(d, N) for d in range(N)]
        tot = math.isqrt(sum(target))
        assert tot * tot == sum(target)
        found = [False]

        def rec(pos, rem, c):
            if found[0]:
                return
            if c and c[0] * c[0] > target[0]:
                return
            if pos == N - 1:
                c2 = c + [rem]
                acf = [sum(c2[e] * c2[(e + d) % N] for e in range(N))
                       for d in range(N)]
                if acf == target:
                    found[0] = True
                return
            for v in range(rem + 1):
                rec(pos + 1, rem - v, c + [v])

        rec(0, tot, [])
        assert not found[0], N
        print(f"  N={N:2d}: no integer counting vector (sum c = {tot})"
              f" has autocorrelation W-hat -- exhaustive")
    print("  the Born square has no whole-frame realization at any "
          "even N tested\n")


def s2_not_positivity():
    print("== s2: not a positivity wall ==")
    for N in range(2, 17, 2):
        t = np.array([what(d, N) for d in range(N)], float)
        tf = np.fft.fft(t).real
        assert tf.min() > -1e-9          # spectrum is nonnegative
        c = np.fft.ifft(np.sqrt(np.maximum(tf, 0))).real
        acf = np.array([sum(c[e] * c[(e + d) % N] for e in range(N))
                        for d in range(N)])
        assert np.allclose(acf, t, atol=1e-9)
        assert c.min() > 0
        print(f"  N={N:2d}: real nonnegative amplitude exists "
              f"(min c = {c.min():.4f}), exact")
    print("  at N = 2 the whole failure is 2 c0 c1 = 1: half a frame. "
          "The wall is")
    print("  INTEGRALITY -- quantization itself rejects even N, not "
          "any sign or positivity\n")


def s3_the_cover():
    print("== s3: the cure is the double cover ==")

    def a_two_doubled(F, m2):        # frames over Z_{2 m2}, 2-part
        return sum(np.exp(2j * np.pi * (x * x * (F % m2)) / (2 * m2))
                   for x in range(2 * m2))

    def a_odd(F, m):
        return sum(np.exp(2j * np.pi * (x * x * (F % m)) / m)
                   for x in range(m))

    for N in (2, 4, 8, 16, 6, 10, 12, 24):
        m2 = 1
        while N % (2 * m2) == 0:
            m2 *= 2
        modd = N // m2
        for F in range(N):
            A = a_two_doubled(F, m2) * (a_odd(F, modd)
                                        if modd > 1 else 1.0)
            want = 4 * N * gcd(F if F else N, N)
            assert abs(abs(A) ** 2 - want) < 1e-6 * max(want, 1), \
                (N, F, abs(A) ** 2, want)
        tag = f"2^{m2.bit_length() - 1}" + \
            (f" x {modd}" if modd > 1 else "")
        print(f"  N={N:2d} ({tag}): |A|^2 = 4 N gcd(F, N) at every "
              f"flux -- cover degree^2 = 4")
    print("  doubled frames on the 2-part (odd part untouched): the "
          "counting amplitude exists")
    print("  on the double cover, exactly. Frames come back whole "
          "upstairs\n")


def s4_reading():
    print("== s4: the reading ==")
    print("  even levels are the ledger's SPIN levels: no frame "
          "counting on Z_N, a perfect one")
    print("  on its double cover -- the second arithmetic shadow of "
          "spin (beside the Lorentzian")
    print("  mod-4 congruence). Constraint stack: 'N odd' softens "
          "from exclusion to covering")
    print("  instruction; smallest admissible level stays N = 5 (the "
          "Lorentzian congruence")
    print("  rejects even N independently)\n")


if __name__ == "__main__":
    s1_the_wall()
    s2_not_positivity()
    s3_the_cover()
    s4_reading()
    print("all assertions passed")
