# 0167 — Falsification audit: what has actually failed, at what grade

> **AI-generated, not peer-reviewed.** Prior art credited in [`ATTRIBUTION.md`](../ATTRIBUTION.md).

The question put to this audit: **has the program genuinely failed
anything — theorem-grade, or at statistical certainty — as opposed to
having hit something later overturned?**

Grades used, and they are not interchangeable:

- **FAILED (theorem)** — a proof that the thing cannot be done.
- **FAILED (statistical)** — a measurement excluding it at stated
  confidence, with the systematic checked.
- **OPEN** — not attempted, or attempted and inconclusive.
- **INHERITED** — an unsolved problem of the whole field, not
  specific to this construction.

## The audit

| requirement | latest result here | grade |
|---|---|---|
| reproduce GR at low energy, **linear** order | constrained sector's kernel **is** Einstein-Hilbert (0152, residual 1e−15); γ = **+1.000** (0163); geodesic deflection ratio **2.023 ± 0.010** (0164) | **passed at linear order** |
| reproduce GR, **nonlinear** (β_PPN) | machinery exact and gated; β = −0.70 with a 7% residual against the theorem value +1 — an **extraction artifact**, explicitly not reported as a measurement (0165) | **OPEN** |
| graviton propagator / semiclassical limit | never successfully measured. Null attributed to ξ/a ≈ 10²⁰ (0149); 0166 raises a competing, better-established explanation (Barrett–Crane intertwiner-independence, Alesci & Rovelli 2007) that was **never tested against it** | **OPEN — and the most serious open item** |
| continuum limit of the discrete theory | untested | **OPEN** |
| diffeomorphism invariance on the lattice | constrained sector violates at O(a²): (k̂²)^{+1.12}, machine zero for many momenta (0152) | **passed to O(a²)** |
| Lorentzian / real time | dispersion matches `E = 2 arcsinh(k̂/2)` to 6.66e−16; 2 polarisations; packet front speed 1.0125 (0165). The **problem of time** proper — the Hamiltonian constraint in a closed diffeo-invariant system — is untouched | **partial; deep version OPEN** |
| cosmological constant | induced sector generates a cutoff-scale Λ, cancelled by a **forced counterterm** (0159). Not solved — cancelled. The constrained-sector calculation is a linearised kernel and simply does not encounter it at that order; that is **not** a solution | **INHERITED, unsolved** |
| spinors / matter | constructed on the lattice's own spin structure; Dirac operator covariant to 9.3e−15 (0165). 16 doublers — **Nielsen–Ninomiya, a theorem about any lattice**, with the standard cure. **Chirality specifically untested** | **passed for existence; chirality OPEN** |
| observables / manifold identification | the identification of the knowledge manifold with spacetime is **assumed**, not derived — 0058's "largest unpriced assumption" | **OPEN (assumption)** |
| a falsifiable number | κ = 16.0001 derived; hierarchy 6.1e19…4.1e20 (0155). Band is a factor 7 wide and sits above M_Planck/GeV by 5–33 | **OPEN — candidate, not a prediction** |
| experimental contact | none; no prediction sharp enough to test | **INHERITED** |

> **Nothing on this list is FAILED at either grade.** No theorem
> forbids anything the program claims, and no measurement excludes
> anything at stated confidence.

## The apparent falsifications, and what overturned them

Every negative result this program produced in the gravity sector was
later overturned, and the pattern is worth as much as the results:

| claimed failure | overturned by | what was actually wrong |
|---|---|---|
| item 2 blocked on **throughput** (0145) | 0146 | kernel gave 30×, answer unmoved |
| blocked on **link-granularity** estimators (0147) | 0148 | wrong unit; boundary conditioning gave 24× |
| **γ = −1, Nordström, zero bending** (0154) | 0158, 0159, 0163 | wrong *sector*, and a Hessian at a **non-stationary point** |
| **"the program fails the classical tests"**, algebraically (0156) | 0152, 0163 | the PSD identity was true of the wrong object; the constrained kernel has exactly one negative mode |
| **γ = +0.509 (vDVZ)** as the answer (0159) | 0163 | correct for the induced sector; the constrained sector gives +1.000 with no counterterms |
| **the scale blocks a simulation** (0161) | 0162 | item 4's clean 1/r at the same coupling is the counterexample |
| **the carrier blocks it** (0162) | 0163 | the same lattice carries the constrained sector's invariance to O(a²) |

**Seven claimed obstructions, seven overturned.** Every one was found
by measurement or by reading, not by argument.

## The honest reading of that pattern

It cuts both ways and both directions should be stated.

**In the program's favour:** none of these were fudged. Each was
recorded as a failure at the time, in writing, and then overturned by
a specific measurement whose gate is in the repository. That is the
error discipline working.

**Against it:** a system that produces seven failures and overturns
all seven is also the signature of a search that is **too good at
finding reasons its own result survives.** The base rate matters. A
programme with genuine obstructions should retire some of them
permanently, and this one has retired none. The open items above —
β, the graviton propagator, chirality, the continuum limit — are the
places where that could still happen, and none of them has been
pushed to the point where it *could* fail cleanly.

**The single most serious item** is the Barrett–Crane flag (0166). If
the derived weight's intertwiner-independence is the reason item 2
found nothing, that is a defect in the theory rather than the
instrument, and it is testable by the field's own standard method. It
has not been tested. Until it is, "nothing has failed" is a statement
about what was attempted, not about what is true.
