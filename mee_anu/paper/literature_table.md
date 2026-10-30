# Literature and novelty sweep — Paper C (Anu), magneto-electro-elastic plate

**Sweep done:** 30 Oct 2026. Sources: Crossref REST API + publisher landing pages.
Every DOI resolved against Crossref or a publisher page unless marked `UNVERIFIED`.
**Scope:** Lamb/guided waves in MEE (BaTiO₃/CoFe₂O₄) plates; size-dependent (nonlocal / strain
gradient / NSGT) MEE plates; thermal MEE plates; magnetoelectric (ME) coupling and its optimisation;
the upgrade proposed in `docs/03_novelty_upgrades.md` (ME design map / inverse design).

> **Headline result.** The three ingredients of the plan each exist separately and are well
> covered: MEE plate wave propagation (Chen–Pan–Chen 2007 and successors), nonlocal/strain-gradient
> MEE plates (Nanomaterials 2021 and many others, mostly buckling/vibration), and ME composite
> optimisation (a mature materials literature). **What the sweep did not find: a thermal (let alone
> MGT) MEE *Lamb-wave* plate paper, and any paper that treats the ME optimum as a function of
> frequency rather than as a material constant.** The static optimum-vs-volume-fraction curve is
> standard, textbook-level knowledge; the *dynamic* optimum is not.

---

## 1. Table of the 14 closest papers

| # | Citation + DOI | Year | Journal | Material | Geometry | Thermal | Size model | Covers | NOT covered | Closeness |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Chen J.Y., Pan E., Chen H.L., *Wave propagation in magneto-electro-elastic multilayered plates*, doi:10.1016/j.ijsolstr.2006.06.003 | 2007 | Int. J. Solids Struct. 44, 1073–1085 | BaTiO₃/CoFe₂O₄ | Multilayer plate | None | None | The classical MEE plate dispersion with traction-free faces; **the plan's Step-3 benchmark** | No heat, no size effect, no ME-optimum analysis | **Very high** |
| 2 | Zhang, Shen, Yu, *Dispersion characteristics of Lamb wave in a multilayered magnetoelectroelastic plate with an imperfect interface*, doi:10.1177/1045389x241306779 | 2025 | J. Intell. Mater. Syst. Struct. 36, 312–326 | MEE laminate | Multilayer plate | None | None (interface spring) | Lamb dispersion, coupling factors, interface imperfection | No heat, no size effect, no design map | **Very high** |
| 3 | *Wave propagation in magneto-electro-elastic multilayered plates with nonlocal effect*, doi:10.1016/j.jsv.2017.04.001 | 2017 | J. Sound Vib. 400, 550–563 | MEE | Multilayer plate | None | Eringen nonlocal | Nonlocal MEE plate waves | No heat, not NSGT, no design map | High |
| 4 | *Critical Temperatures for Vibrations and Buckling of Magneto-Electro-Elastic Nonlocal Strain Gradient Plates*, doi:10.3390/nano11010087 | 2021 | Nanomaterials 11, 87 | MEE | Plate | Temperature (no heat conduction) | **NSGT** | NSGT written for MEE plates; thermal buckling/vibration | **No waves, no Lamb dispersion, no attenuation, no ME coefficient** | High (the plan's item 5) |
| 5 | *Thermal vibration and buckling of magneto-electro-elastic functionally graded porous nanoplates using nonlocal strain gradient elasticity*, doi:10.1016/j.compstruct.2022.115878 | 2022 | Compos. Struct. 296, 115878 | MEE FG porous | Nanoplate | Thermal (steady) | NSGT | Thermal + NSGT + MEE plate, vibration/buckling | No waves, no ME coupling optimisation | Medium-high |
| 6 | *Nonlocal strain gradient shell model for axial buckling and postbuckling of magneto-electro-elastic composite nanoshells*, doi:10.1016/j.compositesb.2017.09.004 | 2018 | Composites Part B 132, 258–274 | MEE composite | Shell | None | NSGT | NSGT MEE shell stability | Not a plate, not waves | Low-medium |
| 7 | *The computation of complex dispersion and properties of evanescent Lamb wave in functionally graded piezoelectric–piezomagnetic plates*, doi:10.3390/ma11071186 | 2018 | Materials 11, 1186 | Piezo–piezomagnetic | FG plate | None | None | **Complex/evanescent Lamb spectrum** in a piezo–piezomagnetic plate | Not a homogenised MEE composite of fixed volume fraction, no heat, no size effect | High |
| 8 | *Lamb wave propagation in the functionally graded piezoelectric–piezomagnetic material plate*, doi:10.1007/s00707-012-0612-5 | 2012 | Acta Mech. 223, 1081–1091 | Piezo–piezomagnetic | FG plate | None | None | Lamb dispersion in a piezo–piezomagnetic plate | No heat, no size effect, no ME optimum | Medium |
| 9 | *Orientation dependence of magnetoelectric coefficient in BaTiO₃/CoFe₂O₄*, doi:10.1063/1.4994042 | 2017 | AIP Advances 7 | BaTiO₃/CoFe₂O₄ | Bulk composite | None | None | **ME coefficient vs orientation/composition** — the materials-side optimum | Not a plate, not dynamic, no size effect | Medium (the static optimum this paper must generalise) |
| 10 | Sidhardh S., Ray M.C., doi:10.1016/j.wavemoti.2019.01.002 | 2019 | Wave Motion 86, 91–109 | Isotropic | Micro-plate | None | General strain gradient | S/A Rayleigh–Lamb with gradient theory | Not NSGT, not MEE | Medium (plan item 6 is mis-cited: **Sidhardh & Ray**) |
| 11 | Lim C.W., Zhang G., Reddy J.N., doi:10.1016/j.jmps.2015.02.001 | 2015 | J. Mech. Phys. Solids 78, 298–313 | generic | beams | None | **NSGT source** | Two length scales | — | Standard |
| 12 | Shaat M., arXiv:1711.09938 | 2017 | arXiv | — | — | — | critique | NSGT infeasibility argument | — | Must be answered |
| 13 | Kumar R., Kansal T., doi:10.1016/j.ijsolstr.2008.07.005 | 2008 | Int. J. Solids Struct. 45, 5890–5913 | thermoelastic diffusive | Plate | Lord–Shulman | None | Thermoelastic Lamb plate with attenuation | No MEE, no MGT, no size effect | Medium |
| 14 | Singh B., Kumar H., Mukhopadhyay S., doi:10.1016/j.tws.2022.109793 | 2022 | Thin-Walled Struct. 180, 109793 | isotropic | Kirchhoff plate | **MGT** | couple-stress type | MGT thermoelastic damping in a plate | No waves, no MEE | Medium |

Not verified this session: the plan's items 3 and 4 (Zakharenko arXiv 2018; Wu et al. arXiv 2021) —
found to exist by title but the arXiv identifiers were not resolved, so no DOI/URL is claimed here.

## 2. Coverage matrix

● treated · ○ partial · — absent.

| # / Paper | MEE (piezo+piezomag+ME) | Plate S/A | Complex attenuation | MGT heat | NSGT (2 scales) | **ME coupling as a design target** | **Volume-fraction sweep** |
|---|---|---|---|---|---|---|---|
| 1 Chen 2007 | ● | ● | — | — | — | — | ○ (fixed laminate) |
| 2 JIMSS 2025 | ● | ● | ○ | — | — | ○ (coupling factors) | — |
| 3 JSV 2017 | ● | ● | — | — | — (nonlocal) | — | — |
| 4 Nanomaterials 2021 | ● | — (no waves) | — | ○ (steady T) | ● | — | — |
| 5 Compos. Struct. 2022 | ● | — (no waves) | — | ○ (steady T) | ● | — | ○ (porosity, not vf) |
| 7 Materials 2018 | ○ | ● | ● (evanescent) | — | — | — | — |
| 9 AIP Adv. 2017 | ● | — (bulk) | — | — | — | ● (static optimum) | ● |
| **Ours** | ● | ● | ● | ● | ● | **● (dynamic optimum)** | ● |

**The empty cell** is MGT × NSGT × MEE-plate Lamb waves with complex attenuation. **The empty
question** is the dynamic ME optimum: every paper that optimises ME coupling (e.g. [9]) does it
statically, and every MEE plate wave paper uses a fixed volume fraction.

## 3. Candidate findings and their status

| Candidate | Status after the sweep | Verdict |
|---|---|---|
| F1. Lamb dispersion in an MEE plate | [1] 2007, [2] 2025 | Rejected as novelty (Step-1..3 verification only) |
| F2. Nonlocal/strain-gradient size effect in MEE plates | [3,4,5] — but for buckling/vibration, not waves | Weak: "same effect, now for waves" |
| F3. Thermal MEE plate waves | **not found** in the sweep (only steady-temperature buckling [4,5]) | Slot is open, but "add heat" is combination novelty |
| F4. Volume-fraction sweep of speeds/coupling | standard; the materials literature [9] owns the static optimum | Rejected as novelty |
| **F5. The ME optimum is frequency-dependent, not a material constant: the volume fraction that maximises ME coupling traces a ridge in the (vf, fd) plane, set by a mechanical matching condition between the two phases, and the ridge moves with NSGT length scales and MGT relaxation** | **Not found in any of the 14** | **Proposed hook** — and the only one of the five that is a claim rather than a model |

Why F5 is physics: in a 2-2 composite the ME effect is a *product* property — strain must be
transferred from the magnetostrictive phase to the piezoelectric phase. Strain transfer is efficient
only when both phases deform together, which in a dynamic plate happens at specific `fd` set by the
two phase wave speeds and the thickness. Hence the optimum volume fraction must move with frequency.
The static optimum is the `fd → 0` limit of the ridge, which gives a rigorous anchor check against
the materials literature [9] — a rare luxury in these three papers.

## 4. Things the sweep found wrong in the existing documents

1. `docs/00_feasibility_analysis.md` predicts this is the weakest of the three. **The sweep agrees.**
2. Plan reading item 6 is mis-cited (Sidhardh & Ray, not Ray) — same error as in the other two plans.
3. The plan's Step-2 check "open/short speed difference gives K²" is not well defined for a plate;
   K² must be defined per mode and per `fd` (the feasibility doc already flagged this). For MEE there
   are **two** such coefficients (electric and magnetic) and a **third** cross one (ME), and all
   three need explicit definitions before Step 2. See `problem_v2.md` §3.
4. No thermal MEE Lamb-plate paper was found, so F3's slot is genuinely open — but the plan should
   not claim it as the finding, only use it as infrastructure.
