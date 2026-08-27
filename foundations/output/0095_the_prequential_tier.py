"""0095 -- the prequential tier: the action is a code length.

The last structural asymmetry in the dictionary (0079): the filter
has an exact operational loss (prequential code length), the physics
has a ledger in nats but nothing it is scored against. This module
closes it at the exact tier (2D Z_N, where the budget was derived):

  s1  ACTION = PREQUENTIAL CODE LENGTH. Reveal the plaquette record
      in any order; score each reveal with the ledger's own
      predictor. The total is exactly -ln P(config): the Euclidean
      action (in nats) IS the prequential code length of the record
      stream. Verified by telescoping to machine precision.
  s2  NO ARROW = ORDER-INVARIANCE. The total is identical under any
      permutation of the reveal order (chain rule); what the
      Lorentzian lift adds is exactly AN ORDER and nothing else --
      the same statement 0093 proved at the free tiers (Euclidean =
      smoother) and 0100 made for the causal layer (arrival order
      of boundary data), now as an exact code-length identity.
  s3  THE BOUNDARY CARRIES THE BUDGET, IN NATS. On the closed
      (constrained) surface the per-step predictor is a genuine
      filter -- its state is the running holonomy posterior -- and
      knowing the constraint saves exactly -ln P_free(hol = 0)
      nats, which approaches ln N at the confinement rate: gap 2's
      innovation capacity, reappearing as an operational loss (the
      boundary holonomy carries that many nats of the record).
"""

import math

import numpy as np

N = 5


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def what(k, n):
    t = 0
    for d in range(1, n + 1):
        if n % d == 0 and k % (n // d) == 0:
            t += sum(1 for x in range(1, d + 1)
                     if _gcd(x, d) == 1) * (n // d)
    return t


# the single-plaquette record law (0080's dual formula)
RAT = np.array([what(k, N) / what(0, N) for k in range(N)])
Q = np.real(np.fft.ifft(RAT))            # q(m), m in Z_N
assert np.all(Q > 0) and abs(Q.sum() - 1) < 1e-12


def conv_pow(p, k):
    """k-fold Z_N convolution of the plaquette law."""
    return np.real(np.fft.ifft(np.fft.fft(p) ** k))


def s1_s2_action_is_code():
    print("== s1/s2: action = prequential code length; no arrow = "
          "order-invariance ==")
    rng = np.random.default_rng(3)
    P = 12
    m = rng.choice(N, size=P, p=Q)           # a plaquette record
    action = -np.log(Q[m]).sum()             # -ln P(config)
    totals = []
    for perm in [np.arange(P), rng.permutation(P),
                 rng.permutation(P)]:
        code = -np.log(Q[m[perm]]).sum()     # prequential, iid tier
        totals.append(code)
    spread = max(totals) - min(totals)
    print(f"  P = {P} plaquettes: action = {action:.6f} nats; "
          f"prequential totals under 3 reveal orders")
    print(f"  agree with it to {spread:.1e} (chain rule): the "
          f"Euclidean measure has no arrow;")
    print("  a Lorentzian reading adds an ORDER and changes no "
          "total\n")
    assert spread < 1e-9 and abs(totals[0] - action) < 1e-9


def s3_budget_price():
    print("== s3: the constrained surface -- the budget as the "
          "price of the boundary ==")
    rng = np.random.default_rng(7)
    for P in (8, 16, 64):
        # draw a record conditioned on hol = 0 (closed surface)
        while True:
            m = rng.choice(N, size=P, p=Q)
            if m.sum() % N == 0:
                break
        # prequential scoring with the BUDGET FILTER: state = needed
        # remainder; predictor q(m) C_{k-1}(need - m) / C_k(need)
        need, code = 0, 0.0
        for i in range(P):
            k = P - i                        # reveals remaining
            Ck = conv_pow(Q, k)
            if k > 1:
                Ckm = conv_pow(Q, k - 1)
                pred = Q * Ckm[(need - np.arange(N)) % N] / Ck[need]
            else:
                pred = (np.arange(N) == need % N).astype(float)
            assert abs(pred.sum() - 1) < 1e-9
            code += -math.log(pred[m[i]])
            need = (need - m[i]) % N
        free_code = -np.log(Q[m]).sum()
        saved = free_code - code
        target = -math.log(conv_pow(Q, P)[0])
        print(f"  P = {P:3d}: free code - constrained code = "
              f"{saved:+.6f} nats  (= -ln P_free(hol=0): "
              f"{target:+.6f})")
        assert abs(saved - target) < 1e-9
    print(f"  -> -ln P_free(hol=0) -> ln N = {math.log(N):.6f} at "
          f"the confinement rate (0100's")
    print("  capacity): knowing the surface is closed saves exactly "
          "the innovation capacity --")
    print("  equivalently, the boundary holonomy CARRIES that many "
          "nats of the record's code.")
    print("  The per-step predictor is a filter whose state is the "
          "holonomy posterior: the")
    print("  ledger's operational loss exists, and it is the "
          "filter's\n")


if __name__ == "__main__":
    s1_s2_action_is_code()
    s3_budget_price()
    print("all assertions passed")
