# Literature and novelty sweep — Paper A (Sumit), piezoelectric semiconductor plate

**Sweep done:** 30 Oct 2026, by the Arena cross-check engineer.
**Search:** Crossref REST API (`api.crossref.org`), publisher landing pages (ScienceDirect, Springer,
IOP, Wiley, AIP, arXiv), and web search. Every DOI below was resolved against Crossref or a
publisher page **except** the entries marked `UNVERIFIED`.
**Scope:** Lamb/guided waves in piezoelectric semiconductors; size-dependent plates and waves in
this material; MGT / generalised-thermoelastic waves; thermoelastic damping in plates; the
upgrade proposed in `docs/03_novelty_upgrades.md` (DC drift bias).

> **Headline result of the sweep (read this first).** The proposed *major* upgrade in
> `docs/03_novelty_upgrades.md` — "non-reciprocal Lamb waves with acoustoelectric amplification
> by a DC drift field in a piezo-semiconductor plate" — **is already published, in a plate, in
> 2005** (entry 2 below), including the gain threshold at `v_d ≈ phase velocity`. It cannot be
> the novelty. The empty cell is elsewhere; see the coverage matrix and `problem_v2.md`.

---

## 1. Table of the 16 closest papers

"Covered" / "NOT covered" refers to: the Lamb (S/A) problem in a **plate of finite thickness**,
**MGT** heat, **NSGT** two-scale size effect, **complex** `k = k_r + i k_i` attenuation,
**carrier-density** sweep, and **DC drift bias**.

| # | Citation + DOI/link | Year | Journal | Material | Geometry | Thermal model | Size model | Covers | NOT covered | Closeness |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Dhib A., Njeh A., Othmani C., Takali F., Ben Salah I., Demir I., Zhang B., Altinsoy M.E., *Real, imaginary and complex branches of Lamb waves in p-type piezoelectric semiconductor GaAs plate: numerical and experimental investigation*, doi:10.1016/j.mssp.2024.108743 | 2024 | Mater. Sci. Semicond. Process. 183, 108743 | p-GaAs (PSC) | Plate, 2h finite | **None** (isothermal) | **None** | Real+imaginary+complex Lamb branches; measured hole density p0≈3.54×10²⁵ m⁻³ by Hall effect; complex branches start at ZGV | No heat, no size effect, no drift bias | **High** |
| 2 | Yang J.S., Zhou H.G., *Amplification of acoustic waves in piezoelectric semiconductor plates*, doi:10.1016/j.ijsolstr.2004.10.011 | 2005 | Int. J. Solids Struct. 42, 3171–3183 | PSC (n-CdS type) | Plate | None | None | **Drift-bias amplification in a PSC plate**; gain when v_d > phase velocity | No heat, no size effect, no complex-branch tracking | **High** (kills our proposed major upgrade) |
| 3 | Yang J.S., Yang X.M., Turner J.A., *Amplification of acoustic waves in laminated piezoelectric semiconductor plates*, doi:10.1007/s00419-004-0350-9 | 2004 | Arch. Appl. Mech. 74, 288–298 | PSC layered | Laminated plate | None | None | Drift-bias amplification, multilayer | No heat, no size effect | High |
| 4 | Luo Y., Zhang X., Othmani C., Gao A., *Lamb wave in an n-type piezoelectric semiconductor nanoplate incorporating surface and nonlocal effects*, doi:10.1088/1361-665X/ae1647 | 2025 | Smart Mater. Struct. 34, 105041 | n-ZnO PSC | Nanoplate | None | Eringen nonlocal + Gurtin–Murdoch surface (integral Legendre expansion) | Lamb dispersion, escape/cutoff frequencies, nonlocal + surface | **No MGT heat, no strain gradient, no NSGT, no carrier-density design map** | **Very high** |
| 5 | *Lamb waves in multilayered piezoelectric semiconductor plates*, doi:10.1007/s10483-025-3287-6 (author list not visible on paywalled page — **verify before citing**) | 2025 | Appl. Math. Mech. (Engl. Ed.) 46, 1493–1510 | n-type PSC, transversely isotropic | Multilayer plate | None | None | Stroh + DVP method; single-layer and sandwich PSC; speed/attenuation vs stacking, thickness, initial carrier density; no-cutoff Lamb waves | **No heat, no size effect, no drift** | **Very high** |
| 6 | Sidhardh S., Ray M.C., *Dispersion curves for Rayleigh–Lamb waves in a micro-plate considering strain gradient elasticity*, doi:10.1016/j.wavemoti.2019.01.002 | 2019 | Wave Motion 86, 91–109 | Isotropic elastic | Micro-plate | None | Generalised first strain gradient (3 constants) + velocity-gradient inertia | S/A Rayleigh–Lamb with strain gradient; cutoff shifts | No piezo, no carriers, no heat, **not NSGT** | High (the plan's reading item 2 is mis-cited: first author is **Sidhardh**, not Ray) |
| 7 | Lim C.W., Zhang G., Reddy J.N., *A higher-order nonlocal elasticity and strain gradient theory and its applications in wave propagation*, doi:10.1016/j.jmps.2015.02.001 | 2015 | J. Mech. Phys. Solids 78, 298–313 | Generic | Beams/wave | None | **NSGT source** (two length scales) | Definition + dispersion + MD comparison | Not a plate, not piezo | Reference standard |
| 8 | Shaat M., *Infeasibility of the nonlocal strain gradient theory for applied physics*, arXiv:1711.09938 | 2017 | arXiv preprint | — | — | — | Critique | Argues NSGT double-counts one physics | — | Must be answered |
| 9 | Shi Z., Li L., He T., *Thermoelastic transient memory response analysis of non-localized nano-piezoelectric plates based on MGT thermoelasticity*, doi:10.1177/03093247241231063 | 2024 | J. Strain Anal. Eng. Des. 59(3), 194–206 | Piezoelectric (not semiconducting) | Nanoplate | **MGT** + memory-dependent derivative | Eringen nonlocal | Transient thermal-shock response | **No waves, no dispersion, no carriers, no strain gradient** | Medium-high |
| 10 | Gupta V., Awwad F.A., Ismail E.A.A., Ahmad H., Das S., *Piezo-semiconductor-void interplay in the size-dependent dynamics of Rayleigh waves within the MGT framework*, doi:10.1108/HFF-04-2025-0254 | 2025 | Int. J. Numer. Methods Heat Fluid Flow 35(9), 3400–3428 | PSC with voids | **Half-space** | **MGT** | Eringen nonlocal (one scale) | Rayleigh waves; attenuation, phase velocity, particle motion | **No plate, no strain gradient, no NSGT** | High (own group; shows what is *not* new for us) |
| 11 | Gupta V., Barak M.S., Das S., *Vibrational analysis of size-dependent thermo-piezo-photo-electric semiconductor medium under memory-dependent MGT photo-thermoelasticity*, doi:10.1080/15376494.2023.2238201 (`UNVERIFIED` — DOI taken from a reference list, not resolved) | 2024 | Mech. Adv. Mater. Struct. 31(28), 10543–10559 | PSC | **Half-space** | MGT + MDD | Eringen nonlocal | Half-space wave/vibration analysis | No plate, no strain gradient | High (own group) |
| 12 | *Unified modeling of harmonic waves in rotating piezoelectric semiconductor*, doi:10.1007/s00419-026-03121-5 (author list not verified) | 2026 | Arch. Appl. Mech. | n-ZnO PSC | Half-space / bulk, rotating | **MGT** | **Klein–Gordon nonlocal** (one scale) | Four coupled modes + one non-propagating; rotation, relaxation, nonlocality, carrier concentration | **No plate, no strain-gradient/NSGT, no complex plate branches** | **Very high** (closest MGT+PSC paper) |
| 13 | Hu B., Liu J., Luo A. et al., *Size-dependent dispersion characteristics of piezoelectric sandwich nanoplates taking surface effects into account*, doi:10.1038/s41598-025-01789-3 | 2025 | Sci. Rep. 15, 17167 | Piezo sandwich | Nanoplate | None (viscoelastic substrate) | **NSGT** + surface | Phase velocity/frequency vs wavenumber, nonlocal softening vs gradient hardening | No semiconductor, no heat, not a full Lamb S/A boundary-value problem | Medium |
| 14 | *A new Stroh formalism for gradient electro-mechanics with applications to Lamb waves in piezoelectric and flexoelectric coupled plates*, doi:10.1063/5.0196873 | 2024 | J. Appl. Phys. 135, 114103 | Piezo + flexoelectric | Plate | None | Strain gradient (gradient electro-mechanics) | Lamb waves with gradient elasticity + flexoelectricity; symmetry breaking of the potential | No carriers, no heat, not NSGT | Medium-high |
| 15 | Kumar R., Kansal T., *Propagation of Lamb waves in transversely isotropic thermoelastic diffusive plate*, doi:10.1016/j.ijsolstr.2008.07.005 | 2008 | Int. J. Solids Struct. 45, 5890–5913 | Thermoelastic diffusive | Plate | **Lord–Shulman** (not MGT) | None | Thermoelastic Lamb plate with diffusion, S/A modes, attenuation | No MGT, no piezo, no size effect | Medium (shows the thermoelastic-Lamb-plate slot is occupied) |
| 16 | Singh B., Kumar H., Mukhopadhyay S., *Analysis of size effects on thermoelastic damping in the Kirchhoff plate resonator under MGT thermoelasticity*, doi:10.1016/j.tws.2022.109793 | 2022 | Thin-Walled Struct. 180, 109793 | Isotropic | Kirchhoff plate | **MGT** | Couple-stress-type size effect | **MGT thermoelastic damping (TED) in a plate resonator** | No waves/dispersion, no piezo, no carriers, no NSGT | Medium-high (our "thermal floor" mechanism) |

Additional standard reference (background, not a competitor): Yang J.S., *Analysis of Piezoelectric
Semiconductor Structures*, Springer, 2020 — book-level formulation of the linearised
drift-diffusion + piezoelectric coupling used by entries 2, 3, 5. **DOI/ISBN not verified** here.

---

## 2. Coverage matrix — where the empty cell is

● = treated · ○ = partially · — = absent. "Ours" = the refocused plan in `problem_v2.md`.

| # / Paper | PSC carriers | Finite plate (S/A) | Complex k_i attenuation | **MGT heat** | **NSGT (2 scales)** | Carrier-density sweep | **Drift bias** |
|---|---|---|---|---|---|---|---|
| 1 Dhib 2024 | ● | ● | ● | — | — | ○ (one measured p0) | — |
| 2 Yang & Zhou 2005 | ● | ● | ○ | — | — | ○ | ● |
| 3 Yang, Yang & Turner 2004 | ● | ● (laminate) | ○ | — | — | ○ | ● |
| 4 Luo 2025 | ● | ● (nano) | ○ | — | — (nonlocal only) | — | — |
| 5 AMM 2025 | ● | ● (multi) | ● | — | — | ● | — |
| 6 Sidhardh & Ray 2019 | — | ● | ○ | — | ○ (SGT, not NSGT) | — | — |
| 9 Shi 2024 | — | ○ (nano) | — | ● | — (nonlocal) | — | — |
| 10 Gupta 2025 | ● | — (half-space) | ● | ● | — | — | — |
| 12 AAM 2026 | ● | — (half-space) | ○ | ● | — (KG nonlocal) | ○ | — |
| 13 Hu 2025 | — | ○ | — | — | ● | — | — |
| 14 JAP 2024 | — | ● | ○ | — | ○ (gradient) | — | — |
| 15 Kumar 2008 | — | ● | ● | ○ (LS) | — | — | — |
| 16 Singh 2022 | — | ○ (resonator) | ○ (TED) | ● | ○ (couple stress) | — | — |
| **Ours** | **●** | **●** | **●** | **●** | **●** | **●** | **○ (as a nulling tool, credited to [2])** |

**The empty cell** is the intersection of *MGT heat* × *NSGT* × *PSC plate Lamb waves*. It is real
and unoccupied as of 30 Oct 2026. But an empty cell is **combination novelty**, which is exactly
the failure mode the feasibility analysis warns about. Therefore the paper is not "the empty cell";
it is the **specific consequence** in the next section.

---

## 3. What the sweep says about each candidate finding

| Candidate finding | Status after the sweep | Verdict |
|---|---|---|
| F1. Drift-bias non-reciprocity / acoustoelectric gain in a PSC plate | **Published 2005** [2], extended to laminates [3] | **Rejected as novelty.** May be used as a *tool* and must be cited. |
| F2. Complex-branch Lamb spectrum in a PSC plate | Published [1] (with experiment) and [5] | Rejected as novelty. |
| F3. Nonlocal/surface size effect on PSC-plate Lamb waves | Published [4] (2025) | Rejected as novelty. |
| F4. MGT heat in piezo-semiconductor wave problems | Published, but **half-space only** [10, 11, 12] | Only the *plate consequence* could be new. |
| F5. NSGT in piezoelectric plate wave problems | Published for elastic/piezo plates [6, 13, 14], not with carriers + heat | Only the *coupling* could be new. |
| **F6. Two-channel attenuation structure: acoustoelectric channel is non-monotonic in carrier density (peak at the dielectric-relaxation matching, screened away at high n₀), and the residual thermoelastic floor's frequency dependence is set by the MGT relaxation time rather than by the doping** | **Not found in any of the 16.** Entries 1/5 give attenuation vs n₀ but only a monotonic trend near their operating point; 16 gives MGT damping in a plate but no carriers; 10/12 give MGT + carriers but in a half-space and without the plate's thermal-length scale | **Proposed hook** (see `problem_v2.md`) |

Numerical plausibility of F6 (checked in `code_arena/task0_feasibility_scaling.py`, numbers in
`checks/task0_scaling.md`): for ZnO the acoustoelectric peak reaches `k_i/k_r ≈ K²/2 ≈ 3.8×10⁻²`
while the Zener/TED floor is `≈ 1.8×10⁻⁴`, i.e. the carrier peak is **~210× the thermal floor**.
So the two channels are *not* comparable in size — the honest statement is not "they compete
everywhere" but "the floor is visible only where the carrier channel is suppressed", which is
exactly what makes the drift-nulling experiment (F6) the measurement, and why MGT only becomes
observable after the carrier channel is removed.

---

## 4. Things the sweep found wrong in the existing plan (for Dr. Vipin)

1. **`docs/03_novelty_upgrades.md`, Paper A, major upgrade is already published** — Yang & Zhou
   2005 [2]. Must be replaced (done in `problem_v2.md`).
2. **Reading item 2 is mis-cited.** The 2019 Wave Motion paper is by **Sidhardh & Ray**
   (doi:10.1016/j.wavemoti.2019.01.002), and it uses *general strain gradient* theory, not NSGT.
   Reading item 3 (Lim, Zhang & Reddy) is the NSGT source; it is correct but should be cited as
   *JMPS* **78**, 298–313.
3. **Two 2024–2026 papers that did not exist when the plan was written** now define the
   state of the art and must be in the introduction: [4] Luo 2025 (SMS) and [5] AMM 2025 for
   PSC-plate Lamb waves, and [12] AAM 2026 for MGT + nonlocal + PSC. Entry [5] in particular means
   "Lamb waves in a PSC plate with carriers and attenuation" is no longer by itself novel.
4. **`docs/00_feasibility_analysis.md` lists *Wave Motion* as a likely target.** Checked on
   scimagojr (SJR 2025): **Wave Motion is Q2 (SJR 0.499)**, not Q1. It should not be a Q1 target.
5. No paper in the 16 works at the **MGT + NSGT + PSC-plate** intersection, so the combination is
   available — but only a *consequence* of the combination will survive review.
