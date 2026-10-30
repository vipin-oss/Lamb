# Literature and novelty sweep — Paper B (Neha), 1D hexagonal piezoelectric quasicrystal plate

**Sweep done:** 30 Oct 2026. Sources: Crossref REST API + publisher/arXiv landing pages.
Every DOI below resolved against Crossref or a publisher page, except where marked `UNVERIFIED`.
**Scope:** Lamb waves in 1D hexagonal piezoelectric quasicrystals (HPEQC); size-dependent QC plates
and waves; phason dynamics (wave-like vs diffusive); MGT/generalised thermoelastic QC waves; the
upgrade proposed in `docs/03_novelty_upgrades.md` (phason model comparison + exceptional points).

> **Headline result.** The quasicrystal-plate niche is **crowded and moving fast**. Three papers
> since 2024 already do what this plan proposed to do first:
> (i) Lamb waves in 1D HPEQC nanoplates with **integral nonlocal** theory including **mode
> conversions and intersections** (Wave Motion 2025);
> (ii) **generalised thermoelastic** Lamb waves in 1D hexagonal QC nanoplates with
> **thermo-phonon-phason coupling**, **attenuation**, and — decisively — **"attenuation jumps in
> mode conversion regions"** (Acta Mech. Solida Sinica 2026);
> (iii) Lamb waves in **piezoelectric QC multi-layered nano-plates with imperfect interfaces**
> (Compos. Struct. 2025).
> The exceptional-point / coalescence upgrade in `docs/03_novelty_upgrades.md` is therefore
> **partly anticipated** by (i)+(ii). The remaining delta is MGT-instead-of-Lord–Shulman and
> NSGT-instead-of-nonlocal, which is not enough on its own. The paper must be re-anchored — see
> `problem_v2.md`.

---

## 1. Table of the 15 closest papers

| # | Citation + DOI | Year | Journal | Material | Geometry | Thermal | Size model | Covers | NOT covered | Closeness |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | *Guided wave propagating in a 1-D hexagonal piezoelectric quasi-crystal plate*, doi:10.1007/s00707-020-02811-7 | 2021 (online 2020) | Acta Mech. 232, 135–151 | 1D HPEQC | Plate | None | None | Phonon+phason+electric guided waves; the standard plate set-up; **the plan's check source for Step 3** | No heat, no size effect, no attenuation | **Very high** |
| 2 | *Generalized Thermoelastic Lamb Waves in One-Dimensional Hexagonal Quasicrystal Nanoplates*, doi:10.1007/s10338-026-00755-4 | **2026** | Acta Mech. Solida Sin. | 1D HQC | Nanoplate | **Fractional Lord–Shulman** | **Integral nonlocal** (one scale) | Thermo-phonon-phason coupled Lamb; dispersion **and attenuation**; **attenuation jumps in mode conversion regions**; size effect on phase velocity | **Not MGT**, not NSGT, no phason-model comparison | **Very high — the direct competitor** |
| 3 | *Mode conversions and intersections of Lamb waves in one-dimensional hexagonal piezoelectric quasicrystal nanoplates based on the integral nonlocal theory*, doi:10.1016/j.wavemoti.2024.103479 | 2025 | Wave Motion 134, 103479 | 1D HPEQC | Nanoplate | None | Integral nonlocal | S/A Lamb, mode conversion/intersection topology | No heat, no NSGT, no attenuation mechanism comparison | **Very high** (anticipates the "coalescence" idea) |
| 4 | *Phonon–phason coupling and nonlocal effects on Lamb waves in functionally graded one-dimensional hexagonal quasicrystal nanoplates*, doi:10.1016/j.rinp.2024.107674 | 2024 | Results Phys. 60, 107674 | 1D HQC, FG | Nanoplate | None | Nonlocal | Lamb waves, phonon–phason coupling strength, FG grading | No heat, no NSGT, not piezoelectric | High |
| 5 | *Lamb waves in piezoelectric quasicrystal multi-layered nano-plates with imperfect interfaces*, doi:10.1016/j.compstruct.2025.119430 | 2025 | Compos. Struct. 370, 119430 | 1D HPEQC | Multilayer nanoplate | None | None (interface model) | Multilayer QC Lamb, imperfect interfaces | No heat, no size effect | High |
| 6 | *Lamb waves propagating in functionally graded 1-D quasi-crystal couple stress nanoplates*, doi:10.1007/s00707-022-03274-8 | 2022 | Acta Mech. | 1D QC | Nanoplate | None | Modified couple stress | FG QC Lamb with one size parameter | Not NSGT (one scale), not piezo, no heat | High |
| 7 | *Nonlocal analytical solution of functionally graded multilayered one-dimensional hexagonal piezoelectric quasicrystal nanoplates*, doi:10.1007/s00707-018-2344-7 | 2019 | Acta Mech. 230, 1781–1810 | 1D HPEQC | Multilayer nanoplate | None | Nonlocal | Static/dynamic nonlocal QC plate solution | Not waves, no heat | Medium |
| 8 | *Lamb Waves in One-Dimensional Hexagonal Piezoelectric Quasicrystal Layered Plates*, doi:10.54097/mb0zx653 | 2026 | Academic Journal of Applied Sciences 2, 1–7 | 1D HPEQC | Layered plate | None | None | Lamb waves, layered | **Venue is not a recognised Q1/Q2 publisher; treat as a low-quality duplicate of [1,5]** — cite only if it contains something [1,5] lack | Low (quality) |
| 9 | Lubensky T.C., Ramaswamy S., Toner J., *Hydrodynamics of icosahedral quasicrystals*, doi:10.1103/physrevb.32.7444 | 1985 | Phys. Rev. B 32, 7444–7452 | QC (general) | — | — | — | **The diffusive-phason (hydrodynamic) model**: phason relaxes, does not propagate | — | Reference standard for the phason-model choice |
| 10 | Bak P., *Elasticity and dislocations in pentagonal and icosahedral quasicrystals*, doi:10.1103/physrevlett.54.1520 | 1985 | Phys. Rev. Lett. 54, 1520 | QC | — | — | — | Phonon/phason elastic foundation | — | Reference standard |
| 11 | *Wave propagation of phonon and phason displacement modes in quasicrystals: determination of wave parameters*, doi:10.1063/1.4907212 | 2015 | J. Appl. Phys. 117 | QC (bulk) | Bulk | None | None | Phonon and phason wave modes, wave parameters | Not a plate | Medium |
| 12 | Sidhardh S., Ray M.C., doi:10.1016/j.wavemoti.2019.01.002 | 2019 | Wave Motion 86, 91–109 | Isotropic | Micro-plate | None | General strain gradient | S/A Rayleigh–Lamb with gradient theory | Not NSGT, no phason | Medium (plan item 6 is mis-cited: **Sidhardh & Ray**) |
| 13 | Lim C.W., Zhang G., Reddy J.N., doi:10.1016/j.jmps.2015.02.001 | 2015 | J. Mech. Phys. Solids 78, 298–313 | generic | beams | None | **NSGT source** | Two length scales | — | Standard |
| 14 | Shaat M., *Infeasibility of the nonlocal strain gradient theory*, arXiv:1711.09938 | 2017 | arXiv | — | — | — | critique | NSGT double-counting argument | — | Must be answered |
| 15 | Kumar R., Kansal T., doi:10.1016/j.ijsolstr.2008.07.005 | 2008 | Int. J. Solids Struct. 45, 5890–5913 | thermoelastic diffusive | Plate | Lord–Shulman | None | Thermoelastic Lamb plate with attenuation | No QC, no MGT, no size effect | Medium |

Not verified this session: the plan's item 9 (the group's own MGT papers) — same set as Paper A,
see `../semiconductor_sumit/paper/literature_table.md`.

## 2. Coverage matrix

● treated · ○ partial · — absent · "Ours" = refocused plan in `problem_v2.md`.

| # / Paper | Phason field | Piezo | Plate S/A | Complex attenuation | MGT heat | NSGT (2 scales) | **Phason model compared** |
|---|---|---|---|---|---|---|---|
| 1 Acta Mech 2021 | ● | ● | ● | — | — | — | — |
| 2 AMSS 2026 | ● | ○ | ● | ● | — (fractional LS) | — (nonlocal) | — |
| 3 Wave Motion 2025 | ● | ● | ● | — | — | — | — |
| 4 Results Phys 2024 | ● | — | ● | — | — | — | — |
| 5 Compos. Struct. 2025 | ● | ● | ● | ○ | — | — | — |
| 6 Acta Mech 2022 | ● | — | ● | — | — | ○ (couple stress) | — |
| 11 JAP 2015 | ● | — | — | ○ | — | — | ○ (mode identification) |
| 15 IJSS 2008 | — | — | ● | ● | — | — | — |
| **Ours** | ● | ● | ● | ● | ● | ● | **● (the spine of the paper)** |

**The empty cell** is MGT × NSGT × complex attenuation in a QC plate. **The empty *question*** is
the last column: no paper in the 15 compares the two thermodynamically admissible phason
kinematics — wave-like (inertial, as in [1,3–6]) versus diffusive/relaxational (Lubensky et al.
[9]) — inside one plate model, and asks what each does to attenuation.

## 3. Candidate findings and their status

| Candidate | Status after the sweep | Verdict |
|---|---|---|
| F1. Lamb dispersion in a 1D HPEQC plate | [1] 2021 | Rejected as novelty (it is Step 1–3 verification) |
| F2. Nonlocal size effect on QC-plate Lamb waves | [2,3,4,7] | Rejected |
| F3. Mode conversion / intersection topology | [3]; attenuation jumps in the same regions in [2] | **Rejected as novelty** — this was the proposed minor upgrade |
| F4. Exceptional points between phonon- and phason-like branches | [2] already reports attenuation jumps at mode conversion; no explicit EP analysis | Weak on its own; at best a supporting figure |
| F5. Thermal (generalised) QC Lamb waves | [2] 2026 (fractional LS) | MGT placement is a *sub-case*, not a finding |
| **F6. Thickness-scaling fingerprint of the attenuation peak: the three dissipative mechanisms available in a QC plate have different scaling of the peak frequency with plate thickness — phason diffusion `∝ 1/h`, MGT relaxation `∝ h^0`, size-effect shift `∝ h` — so a thickness scan identifies the dominant mechanism with no fitted constant** | **Not found in any of the 15** | **Proposed hook** |

Why F6 is physics and not arithmetic: the three mechanisms have different *length* content.
Phason relaxation is diffusive, so its rate is set by `D_ph k²` — a wavenumber-dependent rate, which
under `fd = f·2h` collapses as `1/h`. MGT relaxation is a *local* time constant, `ωτ_q ~ 1`, so it is
thickness-independent in `fd`. Size effects change the *stiffness*, hence the `ω(k)` mapping, and
therefore drag any peak with `h`. Because the three exponents are distinct, the diagnostic is
degeneracy-free, which is precisely what F4 (exceptional points) was hoped to provide but [2] has
already touched.

## 4. Things the sweep found wrong in the existing documents

1. **`docs/03_novelty_upgrades.md`, Paper B, major upgrade (EPs/coalescence) is partly anticipated**
   by [3] (mode conversions/intersections) and [2] (attenuation jumps at mode conversion). It cannot
   be the headline; keep at most as a supporting figure.
2. **The 2026 thermal competitor uses fractional Lord–Shulman, not MGT** — so MGT is a real but
   small delta. It cannot carry the paper; it must be one of the three mechanisms in F6.
3. **Plan reading item 6 is mis-cited** (again): *Sidhardh & Ray*, not Ray.
4. **Plan reading item 2** points at *Academic Journal of Applied Sciences*, which is not a
   recognised venue in this field. It may be cited as a data point but must not be used as the
   benchmark for Step 3 — [1] Acta Mech 2021 is the right benchmark.
5. The plan's decision "phason wave-like or diffusive, choose after reading" should be reversed:
   **do both**, because the comparison is now the paper's only defensible novelty.
