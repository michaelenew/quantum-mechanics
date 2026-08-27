"""0108 -- why band-limited: the level is what a finite record can
PAY FOR.

0117 restated the Born question as 'why is the weight band-limited
in the character basis?'. The answer is in the program's own
currency, but not where I first looked: it is not single-read
resolution, it is ACCUMULATED information.

  s1  ONE READ BARELY SEES THE SECTOR. Sector j is read through the
      class law p(theta|j) prop |chi_j|^2 sin^2(theta). Even at
      PERFECT resolution a single class-angle read carries only
      ~0.19 nats about which sector it came from (adjacent sectors
      overlap 0.85 in the Bhattacharyya sense). My first pass
      expected the cutoff to come from resolution; it does not, and
      the correction is the result: sectors are intrinsically
      expensive to read -- the same fact this program measured from
      the data side as 'sector identity is a slow observable'
      (lucid 0003) and as 'a fixed ~8% of the ceiling per read'
      (lucid 0015).
  s2  SO THE CUTOFF IS A BUDGET, NOT A RESOLUTION. Supporting N
      sectors costs ln N nats of sector information, which at
      i nats per read takes about ln(N)/i reads. At the program's
      OWN vacuum resolution this predicts ~29 reads to support
      N = 5 -- the same order as the INDEPENDENTLY computed n* = 58
      samples that pin the level prequentially (0106). Two
      unrelated calculations of 'how much observation a level
      costs' landing within a factor of two.
  s3  THE STATEMENT AND ITS LIMIT. Band-limiting is forced: a
      filter cannot carry sectors it has not paid for, and the Born
      square is the weight that implements exactly that truncation
      (0117). NOT shown: that the affordable count must equal the
      ADMISSIBLE level of 0081/0106 -- an arithmetic constraint and
      a budget constraint are different arguments, and their
      agreement on a small integer is measured, not derived. That
      agreement is now the sharp remaining target.
"""

import numpy as np

TH = np.linspace(1e-6, np.pi - 1e-6, 1501)
HAAR = np.sin(TH) ** 2


def sector_law(j):
    chi = np.sin((2 * j + 1) * TH) / np.sin(TH)
    p = chi ** 2 * HAAR
    return p / np.trapezoid(p, TH)


def smear(p, sigma):
    if sigma <= 0:
        return p
    d = TH[:, None] - TH[None, :]
    K = np.exp(-0.5 * (d / sigma) ** 2)
    K /= K.sum(axis=1, keepdims=True)
    q = K @ p
    return q / np.trapezoid(q, TH)


def info_per_read(js, sigma):
    laws = np.maximum(np.array([smear(sector_law(j), sigma)
                                for j in js]), 1e-300)
    mix = laws.mean(axis=0)
    return float(np.mean([np.trapezoid(l * np.log(l / mix), TH)
                          for l in laws]))


def s1_one_read():
    print("== s1: one read barely sees the sector ==")
    js = np.arange(0, 2.6, 0.5)          # the derived stack, J = 2.5
    p0, p1 = sector_law(0.0), sector_law(0.5)
    ov = float(np.trapezoid(np.sqrt(p0 * p1), TH))
    print(f"  adjacent sectors j = 0, 1/2: Bhattacharyya overlap "
          f"{ov:.3f} (1 = identical)")
    print("   resolution sigma    nats per read about the sector")
    rows = {}
    for sigma in (0.0, 0.05, 0.10, 0.31, 0.60):
        i = info_per_read(js, sigma)
        rows[sigma] = i
        tag = "  (perfect resolution)" if sigma == 0 else (
            "  <-- the program's own vacuum" if sigma == 0.31 else "")
        print(f"       {sigma:.2f}                {i:.4f}{tag}")
    assert rows[0.0] < 0.35          # even perfect reads are weak
    assert rows[0.0] > rows[0.31] > rows[0.60]
    print("  sectors are INTRINSICALLY expensive to read -- the "
          "cutoff cannot come from")
    print("  resolution alone. (First pass expected otherwise; the "
          "correction is the")
    print("  result, and it matches this program's own 'sector "
          "identity is a slow")
    print("  observable' from the data side)\n")
    return rows


def s2_budget(rows):
    print("== s2: the cutoff is a budget, not a resolution ==")
    print("   N sectors   ln N (nats)   reads needed at sigma = 0.31")
    i031 = rows[0.31]
    for N in (2, 5, 13):
        need = np.log(N) / i031
        print(f"      {N:2d}          {np.log(N):.3f}          "
              f"{need:.0f}")
    need5 = np.log(5) / i031
    print(f"  supporting the program's level N = 5 costs ~{need5:.0f}"
          f" reads at its own vacuum")
    print(f"  resolution. Independently, 0106 computed n* = 58 "
          f"samples to PIN the level")
    print(f"  prequentially: two unrelated calculations of what a "
          f"level costs, within a")
    print(f"  factor {58 / need5:.1f}")
    assert 0.3 < need5 / 58 < 3.0
    return need5


def s3_statement(need5):
    print("\n== s3: the statement and its limit ==")
    print("  BAND-LIMITING IS FORCED: a filter cannot carry sectors "
          "it has not paid for, so")
    print("  the representable weight has finite character support "
          "-- and the Born square is")
    print("  exactly the weight that implements that truncation "
          "(0117). The chain")
    print("  'why squared' -> 'why band-limited' -> 'because sector "
          "information is bought")
    print("  by the read, at a measured price' now terminates "
          "INSIDE the theory.")
    print("  NOT SHOWN: that the affordable count equals the "
          "ADMISSIBLE level of 0081")
    print("  (x^2 = -1 mod N, the even wall). An arithmetic "
          "constraint and a budget")
    print(f"  constraint are different arguments; that they agree on "
          f"a small integer")
    print(f"  (~{need5:.0f} reads for N = 5 against 58 to pin it) is "
          f"measured, not derived.")
    print("  That agreement is the sharp remaining target, and it is "
          "a far better one")
    print("  than 'why squared'\n")


if __name__ == "__main__":
    rows = s1_one_read()
    need5 = s2_budget(rows)
    s3_statement(need5)
    print("all assertions passed")
