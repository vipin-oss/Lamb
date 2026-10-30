# STATUS — three-paper project

**Updated 30 Oct 2026 (v4). Branch `arena/beec1abf-lamb`, PR #1 (open, not merged).**

## One-line state

Heat is back in the model as a full coupled MGT field for all three papers (v4, overriding Route A; the
adiabatic/isothermal bracket survives only as a verification limit). The gate document is revised to the
reviewer's seven corrections, and the three scholar packages are built: `deliver/Lamb_{Sumit,Neha,Anu}.zip`,
two `.tex` files each.

## Paper status

| paper | stage | gate now blocking | verdict |
|---|---|---|---|
| **Sumit** (ZnO PSC plate) | v4 model fixed; package delivered; Step 2 (6×6) closed | week-1 reading: Lim (17)–(19) on the page, Qu et al. Peltier term | **GO, conditional** (risk: identifiability) |
| **Neha** (QC plate) | v4 model fixed; package delivered | week-1 reading: AMSS 2026 generalized thermoelastic QC plate paper (novelty may close) | **REFOCUS** |
| **Anu** (MEE plate) | v4 model fixed; package delivered | week-9 ridge test; band of two homogenisation routes vs thermal contribution | **DOWNGRADE to Q2** |

## What changed in v4

1. **NSGT in Lim form**: `(1 - l_nl^2 lap) t = sigma` with `sigma` carrying `(1 - l_g^2 lap)` on `c:eps`
   only, plus the equivalent momentum form with the operator on inertia. Lim et al. Eqs. (18), (19), cited
   through Barretta & Marotti de Sciarra (2018) — no access to the Elsevier PDF, marked secondary.
2. **All piezo, piezomagnetic, thermal and phason terms local** — stated once as a modelling choice.
3. **A6**: band-gap term removed; Onsager-reciprocal Peltier term `-q Pi_th d(dn)/dt` added, with
   `beta_th = b_n n_0 S_n` (m^-1 s^-1 K^-1, negative for n-type), `Pi_th = T_0 S_n`, and recombination only
   as an optional finite-`tau_R` pair. Every term of (A5) and (A6) dimension-tested in a table.
4. **Three claims withdrawn** after searching: A "close at most one direction" (killed by Qu et al. 2023 and
   Gupta et al. 2025), C "rarely retained" (killed by Kondaiah et al. 2013 and Tocci Monaco et al. 2021),
   C "frequency-dependent alpha" (no source).
5. **Lubensky corrected**: Lubensky, Ramaswamy & Toner, PRB 32 (1985) 7444, icosahedral. Phason telegraph
   dynamics now sourced to Agiasofitou & Lazar (2014) Eqs. (26), (30) and Baggioli & Landry (2020) Eq. (17).
6. **Symbols separated**: `q` charge, `k` wavenumber, `h_kij` piezomagnetic, `b_n` mobility, `mu_ik`
   permeability.

## v4.1 (second review round)

1. **MGT named properly**: Moore-Gibson-Thompson at first use in all six files; "modified gradient" gone.
2. **Sumit signs fixed**: `beta_th = -b_n n_0 S_n > 0`, bracket entry `+q Pi_th d(Dn)/dt`, Onsager ratio
   `-T_0/(b_n n_0)`. Independent derivation agrees with the reviewer; audit in `internal/sumit_audit.md`.
3. **Sign and unit audits** for all three papers in `internal/{sumit,neha,anu}_audit.md`.
4. **Basics expanded**: 8840 / 6440 / 6040 words, 23 sections, full symbol table with units and scales,
   self-testing section. Zips rebuilt; `reports/packages_v4.tex` carries the new counts.

## Open items

- **[V]** Lim et al. (2015) Eqs. (17)–(19) on the page; the equation numbers are still secondary.
- **[V]** AMSS 2026 `10.1007/s10338-026-00755-4`: obtain and read. It may close Paper B's thermal novelty.
- **[S]** week-1 reading report before any computation.
- **[N]** same, plus a phason relaxation time tied to a real material.
- **[A]** magnetoelectric sign convention and thermal face conditions; two homogenisation routes.
- **[all]** no LaTeX engine here: nothing is compiled, and no PDF is promised.

## Internal records

`internal/changes_v4_review.md`, `internal/{sumit,neha,anu}_equation_source_log.md`,
`internal/{sumit,neha,anu}_benchmarks.md`, `internal/style_check.md`.
