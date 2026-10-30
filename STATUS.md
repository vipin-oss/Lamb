# Status — round v8 (base `handoff_v8/`)

1. Task 1 done: all 25 entries and 7 row functions of the three masters rebuilt from the constitutive laws and compared entry by entry at three (k, ω, η); largest relative difference 1.1e-50. No entry error, so no matrix edit was needed.
2. The v8 sign repairs are confirmed by the rebuild: Anu M33/M34/M43 Gauss-row signs, Neha M44 and M35 = −ηβ^w.
3. Task 2: Rayleigh–Lamb both families pass (S0 5393.905/5393.172/5308.589, A0 311.638/954.234/2326.643, worst |det B|/‖B‖⁴ 1.6e-59); degree 14/10, four extra roots at |η|l_g ≈ 1, null residuals ≤ 2.6e-59, l→0 shift ≤ 1.3e-10, Sumit parity iff β_th = Π_th = E_g = 0.
4. Task 2 open: the 14 × 14 assembly of Calculation G is numerically singular at every speed (equilibrated determinant ~1e-160 at 40 digits), so no mode and no coupling-limit re-run. Reported, not papered over.
5. Task 3: our rows are the variational closure; the nonlocal length adds no root (degree 14 with l_nl = 0), so the constitutive BCs of Barretta Eqs. (18)–(19) have nothing to act on in this form. Alternative-closure numbers not produced (blocked by item 4). Wording proposed, not imposed.
6. Task 4: Yang & Zhou DOI settled by Crossref — the bib's Elsevier DOI is the IJSS 42 (2005) 3171 paper; the referee's DOI is a different 2005 paper by the same authors. Yang–Zhou Eqs. (3), (7) remain unverified.
7. Delivery: `deliver/Lamb_<Scholar>.zip` rebuilt from the v8 sources (tex + bib), `reports/packages_v8.tex` (3 pp), evidence in `internal/v8_task{1,2,3,4}_*.md`.
8. No LaTeX engine here: nothing compiled; static checks only (environments balanced, no duplicate labels, no undefined refs).
