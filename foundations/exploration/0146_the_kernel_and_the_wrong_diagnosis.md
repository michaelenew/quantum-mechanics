# 0146 — The Spin(4) kernel, and a diagnosis of mine that was wrong

> **AI-generated, not peer-reviewed.** See [`ATTRIBUTION.md`](../ATTRIBUTION.md) — results here are re-derivations of established work unless explicitly
> marked otherwise, and prior art is credited there.
>
> **Prior art.** Rao (1945), Blackwell (1947); Parisi, Petronzio & Rapuano (1983).

Code: `output/0134_the_spin4_kernel.py`,
`output/0135_the_graviton_run.py`.

## 1. The kernel

Two quaternions per link, a 2-D log-weight table over the two class
angles, bilinear lookup, joint Metropolis move on both factors,
xoshiro RNG carried in the C state.

**Correctness gate**, run before anything else: the C sweep must
reproduce the numpy sweep's physics.

| | κ⁺ | κ⁻ |
|---|---|---|
| C kernel | 17.129 | 17.182 |
| numpy (0144) | 16.99 | 17.03 |

Within 1%, acceptance 0.410. **Gate passed.**

**Throughput:**

| L | C | numpy | speedup |
|---|---|---|---|
| 4 | 1107 sweeps/s | 34.3 | **32.3×** |
| 8 | 69.5 sweeps/s | 6.4 | **10.8×** |

5000 configurations at L = 8 took **968 seconds**. The numpy path
would have taken most of a day.

## 2. The run, and the result

0145 said item 2 was obstructed *on throughput*, needing ~25×.
Delivered ~30×:

| r | spin 0 | spin 1 | **spin 2** | \|s2\|/floor |
|---|---|---|---|---|
| 1 | −0.000376 | −0.000108 | **−0.000229** | 0.6× |
| 2 | −0.000352 | −0.000092 | **−0.000334** | 0.9× |
| 3 | −0.000134 | −0.000347 | **−0.000170** | 0.5× |
| 4 | +0.000038 | −0.000138 | **−0.000376** | 1.0× |

Shuffle floor 0.000358. **Still at the floor**, at every r and at
both smearing widths.

## 3. The diagnosis was wrong, and that is the result

0145 said, in as many words: *"The blocker is throughput, not
concept."* Thirty times the throughput later it is unchanged.

> **The obstruction is not throughput. It is the estimator.**

The naive scaling that made throughput look sufficient — SNR ~ √n —
assumed a signal sitting just under the floor. It is not just under;
the connected spin-2 correlator is at or below 4×10⁻⁴ as a
correlation coefficient, and a √n improvement of five would not have
reached it either.

What that means for the next move: **a different estimator, not more
sweeps.** Multilevel or link-integration methods buy variance
reduction that scales *exponentially* in the number of levels rather
than as √n, and they are the standard tool for exactly this — a
connected correlator of a composite operator at weak coupling. That
is a real build, not a run.

## 4. What stands

- ✅ The kernel is built, gated and fast. It is the right
  infrastructure regardless, and items 3, 4 and 6 all need it.
- ✅ The Spin(4) rebuild and its coupling stand (κ ≈ 17 measured two
  independent ways now).
- ⛔ **Item 2 remains open**, with its blocker correctly identified
  for the first time.

**The honest ledger on my own call:** I named throughput as the
blocker with a number attached (25×), the number was delivered, and
the prediction failed. That is the second time this session an
estimate of mine about *what* would fix a measurement turned out
wrong while the measurement itself was fine. The pattern is worth
noting — I have been better at measuring than at predicting what a
measurement will cost.
