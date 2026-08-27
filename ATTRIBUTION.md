# Attribution

**This repository is AI-generated and has not been peer-reviewed.**

## The standing assumption

This work was produced by an AI system exploring a line of reasoning
across a long session. It had access to the published literature
through its training and, in places, through search. **It must
therefore be assumed that anything here which appears novel is
reconstructing prior work rather than discovering it independently.**

That assumption is not a formality. Where this repository derives a
known result, it frequently did so without naming the source at the
time, and the connection was made later — sometimes several documents
later, and in at least one case (see 0166) only after checking the
literature directly. **Absence of a citation in a given document
should be read as an omission, not as a claim of priority.**

Where a result *is* believed to be new, it is marked as a candidate
needing a literature check, never as established. See 0166 §"What may
actually be new".

## Results and their original authors

### Quantum foundations

| result as used here | originally due to |
|---|---|
| the probability measure on a Hilbert space | Gleason (1957) |
| operational/informational reconstructions of the Born rule | Hardy (2001); Chiribella, D'Ariano & Perinotti (2011); Masanes & Müller (2011) |
| envariance route to Born weights | Zurek (2005) |
| reflection positivity ⟹ Hilbert space and unitary time (OS reconstruction) | Osterwalder & Schrader (1973, 1975) |
| decoherence, consistent/decoherent histories | Zurek; Griffiths (1984); Omnès; Gell-Mann & Hartle (1990) |
| relational reading of quantum states | Rovelli (1996) |
| entanglement monogamy | Coffman, Kundu & Wootters (2000) |

### Lattice field theory and method

| result as used here | originally due to |
|---|---|
| lattice gauge theory, the plaquette action, strong-coupling expansion | Wilson (1974) |
| asymptotic freedom; the two-loop β-function | Gross & Wilczek (1973); Politzer (1973); Caswell (1974); Jones (1974) |
| the lattice Λ parameter and its scheme conversion | Hasenfratz & Hasenfratz (1980); Dashen & Gross (1981) |
| on-shell improvement of lattice actions | Symanzik (1983); Lüscher & Weisz (1985) |
| APE link smearing | Albanese et al. (1987) |
| multihit / link integration | Parisi, Petronzio & Rapuano (1983) |
| multilevel (two-level) algorithms for correlators | Lüscher & Weisz (2001) |
| Rao–Blackwellisation (conditional-mean estimators) | Rao (1945); Blackwell (1947) |
| fermion doubling theorem | Nielsen & Ninomiya (1981) |
| Wilson fermions; Ginsparg–Wilson relation; overlap operator | Wilson (1975); Ginsparg & Wilson (1982); Neuberger (1998) |
| Whittle likelihood | Whittle (1953) |
| minimum description length / code-length model selection | Rissanen (1978); Akaike (1974); Schwarz (1978) |
| Fisher information and the Cramér–Rao bound | Fisher (1922); Cramér, Rao (1945) |
| partial information decomposition ("synergy") | Williams & Beer (2010) |
| channel capacity, equiprobable-bin arguments | Shannon (1948) |

### Gravity

| result as used here | originally due to |
|---|---|
| light deflection 4GM/b; perihelion advance 6πM/p | Einstein (1915); confirmed Dyson, Eddington & Davidson (1919) |
| scalar gravity gives γ = −1 and **zero** light bending | Nordström (1913); Einstein & Fokker (1914) |
| PPN formalism, γ and β | Nordtvedt (1968); Will & Nordtvedt (1972) |
| the Cassini bound γ − 1 = (2.1 ± 2.3)×10⁻⁵ | Bertotti, Iess & Tortora (2003) |
| Fierz–Pauli mass term for spin 2 | Fierz & Pauli (1939) |
| vDVZ discontinuity: massive graviton ⟹ γ = ½, deflection ¾ | van Dam & Veltman (1970); Zakharov (1970) |
| conformal-factor problem (Euclidean EH unbounded below) | Gibbons, Hawking & Perry (1978) |
| gravity induced by a one-loop matter determinant | Sakharov (1967); reviewed Visser (2002) |
| first-order (Palatini) gravity; tetrad + connection | Palatini (1919); Einstein (1925) |
| **BF + simplicity constraint = general relativity** | Plebanski (1977) |
| Ashtekar variables; the Barbero–Immirzi parameter | Ashtekar (1986); Barbero (1995); Immirzi (1997) |
| **spin foam with balanced representations j⁺ = j⁻** | Barrett & Crane (1998) |
| **Barrett–Crane fails the graviton propagator; intertwiner-independence is the cause** | Alesci & Rovelli (2007) |
| the successor vertices that retain intertwiner dependence | Engle, Pereira, Rovelli & Livine (2008); Freidel & Krasnov (2008) |
| Kerr–Schild double copy (gravity as gauge²) | Monteiro, O'Connell & White (2014); Bern, Carrasco & Johansson (2008) |
| Regge calculus | Regge (1961) |
| causal dynamical triangulations | Ambjørn, Jurkiewicz & Loll (1998–) |
| Einstein equation as an equation of state; entropic gravity | Jacobson (1995); Padmanabhan; Verlinde (2011) |
| black hole entropy S = A/4G | Bekenstein (1973); Hawking (1975) |
| Unruh temperature | Unruh (1976); Davies (1975); Fulling (1973) |
| Λ quantisation from compactness / π₁ | Standard; cf. flux quantisation, Dirac (1931) |

### The program's four founding constructions

These are the ideas the program was *started* on, and all four have
established lineages. Checked against the literature in the session
that produced 0166; none of them had a citation in this repository's
attribution record before that check.

| founding idea, as posed here | established as |
|---|---|
| "a distribution cannot encode its own confidence" — the motivating puzzle | **inverted by** Wootters (1981), *Statistical Distance and Hilbert Space*: the angle between rays **is** the statistical distance. Completed by Braunstein & Caves (1994): the Fubini–Study metric is ¼ the quantum Fisher information, bounding phase estimation via the quantum Cramér–Rao inequality. The program's 0065 (metric = Fisher metric of an inference network, w = e^{2I} − 1) is the classical shadow of this. |
| knots/crossings as a topological basis for pairwise interactions; arcs as channels, crossings as three-party constraints, global sections as colourings (0011) | **quandle theory.** The crossing rule `2·over = under_in + under_out (mod p)` is verbatim the Fox n-colouring condition, and Fox colourings are quandle homomorphisms into the dihedral quandle. Quandles: Joyce (1982) and Matveev (1982) independently; Takasaki (1943) for the involutory case. The quandle axioms *are* the Reidemeister moves. Related physical realisations: Rovelli & Smolin (1988), whose loop states are knot classes; Witten (1989), Wilson loops as knot invariants; Deser, Jackiw & 't Hooft (1984) for 2+1 gravity as conical defects — all three cited in 0011 itself. |
| "correlation sources curvature" — the founding hope of contact with holography | **Matsueda (2013)**, *Emergent General Relativity from Fisher Information Metric*, derives the Einstein tensor from the Fisher metric — the nearest structural neighbour. Alongside Jacobson (1995, 2015); Ryu & Takayanagi (2006); Van Raamsdonk (2010); Maldacena & Susskind (2013). **0058 records that what was delivered is "participation density sources curvature", not correlation**, and that the identification of the knowledge manifold with spacetime is assumed here where holography earns it as a duality — "the program's largest unpriced assumption". |
| the two-tier actionable/correlational split | Relational QM, Rovelli (1996); QBism, Fuchs, Mermin & Schack; the epistemic restriction, Spekkens (2007) — all three named in 0002's own novelty assessment as inherited, not new. |

### Specific corrections this repository made to itself

Recorded because they bear on how much weight to put on anything here:

- **0166** — the derived weight was identified as a Barrett–Crane
  amplitude only after checking the literature, ~30 documents after
  the structure was first written down. The Alesci–Rovelli failure of
  that model was not known to the analysis when item 2's null was
  attributed to a scale separation.
- **0158/0159/0162/0163** — the gravity sector's central verdict was
  reversed three times (γ = −1 "falsification", then vDVZ, then
  γ = +1 in a different sector), and two separate "blockers" were
  named and later retired.
- **0165** — β_PPN does not converge; the number obtained is an
  extraction artifact and is not reported as a measurement.

## How to read a claim in this repository

1. Assume prior art exists and has not been cited.
2. Treat gates and machine-precision checks as checks on the
   *implementation*, not as evidence that the physical statement is
   new — a gate that reproduces Einstein-Hilbert confirms the code,
   not a discovery.
3. Numbers reported with error bars, windows and stated failure modes
   are the reliable content. Narrative claims about significance are
   not.

If you are the author of work reconstructed here and it is credited
wrongly or not at all, that is an error of this repository and worth
correcting.
