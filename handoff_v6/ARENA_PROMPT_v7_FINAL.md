# Arena prompt v7 (final, self-contained): three complete papers with full calculation, delivered together

Repo `vipin-oss/lamb`, branch `claude/v6-handoff` (read-only for you: copy what you need to your own pinned
branch `arena/beec1abf-lamb`, work and commit there, PR #1 as before; never touch main). This file replaces
v5 and v6. Nothing else needs to be read except the files named in section 1.

Standing rules, unchanged: never invent a reference, an equation number or a constant; milestone report is ONE
self-contained LaTeX file (<= 4 pages); `STATUS.md` <= 10 lines; chat replies <= 8 lines; state numbers and
tolerances in the reports.

---------------------------------------------------------------------------------------------------

## 0. The job in one paragraph

Dr. Vipin supervises three PhD scholars. Each writes a paper on Lamb waves in a plate (thickness 2h, free
faces z = +-h, plane strain in x-z, wave exp[i(kx - wt)], k = k_r + i k_i, k_i > 0 decays) with
Moore-Gibson-Thompson (MGT) heat conduction and the nonlocal strain gradient size effect (NSGT):
**Sumit** = piezoelectric semiconductor plate (ZnO type); **Neha** = 1D hexagonal piezoelectric quasicrystal
plate; **Anu** = magneto-electro-elastic (BaTiO3/CoFe2O4) plate. You produce, **for all three in one
delivery**, a master LaTeX file with the **complete hand calculation from the source equations down to the final
boundary matrix**, with every small step written out, every starting equation cited with the equation number
you actually read, and the references in a `.bib` file. Dr. Vipin will remove the worked-out parts himself
and give the scholars the version that has only the results, so the master must make that removal clean
(section 4). The scholars are beginners and must be able to verify every equation against its source, so the
citations and the definitions are the most important quality of the files.

Deliverable: `deliver/Lamb_Sumit.zip`, `deliver/Lamb_Neha.zip`, `deliver/Lamb_Anu.zip`; each contains exactly
two files, `Lamb_<Scholar>.tex` and `Lamb_<Scholar>.bib`. Plus internal verification files (section 8) and one
milestone report. Do all three in one go; stop only when all three are done (the only earlier stop is a
blocker you cannot resolve, see section 10).

## 1. Files to read first (about 30 minutes, then work)

- `handoff_v6/Sumit_v2/03_Reduced_Equations_and_Matrix_Sumit.tex` : my reduced equations, 5x5 matrix, 14x14 matrix for Sumit (results only).
- `handoff_v6/Sumit_v2/01_Research_Plan_Sumit.tex` : the model with source sentences already added.
- `handoff_v6/reference_code/` : my numerical reference for Sumit (method reference, not truth).
- `reports/model_v4.tex` : the agreed equation sets for the three papers.
- `internal/*_equation_source_log.md` : what was and was not read in earlier rounds.

## 2. What I found for Sumit (re-derive independently, do not trust)

1. Unknowns u_x, u_z, phi, Delta n, theta; five equations: momentum x and z (nonlocal operator on the inertia), Gauss law with mobile charge, carrier continuity with drift-diffusion, drift velocity, thermodiffusion and recombination, and the MGT heat equation with thermal stress, pyroelectric, Peltier and recombination heat terms. Constants for 6mm with c-axis along z: c11 c13 c33 c44, e31 e33 e15, eps11 eps33, beta1 beta3, p3.
2. det M(eta) is a polynomial in eta of degree 14 when the gradient length l_g is not zero, 10 when l_g = 0 (nonlocal operator alone does not raise the order).
3. With beta_th and Pi_th (thermodiffusion, Peltier) non-zero **and** a polar coupling (e or p3) non-zero, det M(eta) is **not even** in eta: the roots do not come in +-pairs and the plate modes do not split into symmetric and antisymmetric families. If beta_th = Pi_th = 0 they do. Reason: a polar crystal has no z-mirror symmetry once the sign of the carrier charge matters (the mirror symmetry of the piezoelectric block needs phi and Delta n odd, while theta stays even).
4. Seven boundary conditions per face (14 in all, 10 when l_g = 0): total traction normal and shear including the surface-gradient term (Charalambopoulos, Douka, Mavratzas, arXiv:1909.10776, Sec. 2, Eq. (14)), double traction R = n.mu.n (same source, condition b(i)), nonlocal operator inverted root by root as 1/N(eta_m), open-circuit D_z = 0, zero carrier flux Gamma_z = 0, adiabatic face d theta/dz = 0 (isothermal as alternative). These are modelling choices and must be flagged "ours" in the text.
5. Tests that passed with my code: isotropic Rayleigh-Lamb, both families, 1e-6 relative; open-circuit S0 of the piezoelectric plate at small fd (5509.56 against 5509.57 in the repo); Fourier thermoelastic bulk damping against k_i/k_r = (Delta_E/2) w tau/(1+(w tau)^2); Hutson-White peak in n0 (eps11 w/(q b_n)) within one grid step; NSGT direction (gradient stiffens, nonlocal softens).

**Task 1 for you:** rebuild M(eta), the roots, the null vectors and B for Sumit with your own code, run these five tests plus a continuity test (l_g, l_nl -> 0 recovers the classical roots), and confirm or correct every item above. Report each difference. If you find one of my entries or signs wrong, say which and fix it in the master.

## 3. Content of each master file (all three papers)

Write in this order. Every item is in the same file; a definition is given at the place where a term first appears.

1. Title, abstract (six lines), keywords.
2. Introduction in plain words: what a Lamb wave is, why the plate, what is new (use the agreed novelty claims in `model_v4.tex` as corrected there), literature with citations from the .bib.
3. Setting and assumptions (geometry, symmetry class and axes, plane strain, linearisation, what is local and what is nonlocal and why).
4. Notation table: symbol, meaning in words, unit, and where it enters. Also a short everyday picture where it helps. No typical numbers.
5. Source equations, each cited. Strain-displacement, field-potential relations, balance of momentum, Gauss laws, carrier / phason / magnetic equation, constitutive relations, thermal stress, pyroelectric (and pyromagnetic) terms, MGT heat equation, the NSGT differential law. Format: "Equation (n) is the balance of momentum, `\cite[Eq.~(2.1)]{key}`." For each give a line "taken from the source as is" or "taken from the source with the change ..." or "ours, follows from the law ...".
6. Calculation A, constitutive relations in components for the chosen class and axes: which elements of c, e, eps, (q, K, R for the quasicrystal; d, mu, alpha for the MEE) survive and why, written element by element, stresses and induction in components.
7. Calculation B, the five governing equations in component form for plane strain, each with the size-effect operators written explicitly.
8. Calculation C, plane-wave reduction: substitute exp(ikx) exp(eta z) exp(-iwt), show every derivative, collect terms, write the 5x5 matrix M(eta) entry by entry, with the arithmetic for each entry on its own line.
9. Calculation D, characteristic equation: det M(eta) = 0, how its degree is counted (give the counting argument, for example the highest power of eta in each row), the parity of the polynomial, what that means for the roots, and which couplings break the pairing.
10. Calculation E, solution through the thickness: amplitude ratios from the cofactors (give the cofactor formulas for the entries, or the 4x4 minors in compact form), the general solution as a sum of partial waves, how the number of partial waves equals the number of conditions.
11. Calculation F, boundary conditions: each condition derived from the variational or physical statement (free of traction, open or closed circuit, and so on), the nonlocal operator inverted root by root, written in terms of the amplitude ratios, one row function per condition.
12. Calculation G, the final matrix: assembly of the full matrix B with face rows and root columns, the dispersion relation det B = 0, the column scaling note (without code), what is solved for (complex k at real w).
13. Calculation H, limits worked by hand: couplings off gives the Rayleigh-Lamb relation (derive the reduction of the matrix to the familiar form, both families if the split holds), and one limit specific to the paper (listed in section 6). Without numbers.
14. Self-test list for the scholar (limits, symmetries, units, switching a term off), no values.
15. Work plan in weeks, short. References are in the .bib.

No programming part: no code, no scripts, no description of a numerical algorithm beyond the column-scaling remark.
No numerical benchmark values anywhere in the files (no wave speeds, no K^2, no roots). Numbers live only in `internal/`.

## 4. How to make the removal clean (worked blocks)

In the preamble define
```
\usepackage{amsthm}   % for remark-style environments if needed
\newif\ifshowworked \showworkedtrue
\newenvironment{worked}{\ifshowworked\par\smallskip\noindent\textit{Working.}\par\else\setbox0\vbox\bgroup\fi}{\ifshowworked\par\smallskip\else\egroup\fi}
```
(or an equivalent that compiles with plain pdflatex). Put **every** calculation step inside `worked`, keep the
result equation outside. Results, sources, definitions stay outside. Setting `\showworkedfalse` must compile and
produce the scholar version with results, sources and definitions only; both settings must compile. In the
scholar version no sentence may refer to a step that is hidden ("as shown above" is not allowed outside a
worked block). Equation numbers must remain valid in both versions. Test both and keep both PDFs' page counts
in the report.

## 5. Citation rules (the heart of the job)

- Every equation that comes from a source: `\cite[Eq.~(n)]{key}` or `\cite[Sec.~n.m]{key}` with the number you actually read. Open-access first: arXiv, PMC, MDPI, publisher open pages, institutional repositories (upcommons, hal, kobe-u). In an earlier round the following worked: Zhu, Negahban, Xu, Xia, Li, Micromachines 14 (2023) 2174 (mdpi.com/2072-666X/14/12/2174), Eqs. (1)-(7); Quintanilla, Math. Mech. Solids 24 (2019) 4020, Eqs. (2.5), (3.1)-(3.5) (PDF via upcommons); Charalambopoulos et al., arXiv:1909.10776, Sec. 2, Eq. (14). Publisher PDFs behind a paywall did not open.
- For the quasicrystal and the MEE papers find and read the numbered governing equations for thermoelastic quasicrystals (phonon stress, phason stress, phonon-phason coupling, thermal terms, plates and surface waves) and for thermo-magneto-electro-elastic media (constitutive, pyroelectric, pyromagnetic, ME coefficient, plates), at least three sources each, with the equation numbers. The agreed claims in `model_v4.tex` and the competitor flagged for Neha (AMSS 2026, doi 10.1007/s10338-026-00755-4) must be handled as before.
- If you could not read an equation number, the text must say so in the sentence ("equation number not read, please locate it in [x], Section y") and the .bib entry carries a `note` field. Never write a number you did not see. Never cite a page you did not open for a specific equation.
- Where a law is textbook, cite a textbook with chapter or section only if you know it from a source you opened; otherwise say "textbook law" and name the law.
- The Lim-Zhang-Reddy equations (their Eqs. (17)-(19)) are known to us only through Barretta and Marotti de Sciarra, IJES 130 (2018) 187, Eq. (18)-(19). Say exactly that, and ask the scholar to open Lim et al. Section 2.
- `.bib`: BibTeX entries with author, title, journal, volume, year, pages, `doi` or `eprint`; a `note` for anything not fully read. Style `unsrt`. Compile pdflatex, bibtex, pdflatex, pdflatex. No undefined citations.
- Also produce `internal/<scholar>_equation_source_log.md`: every equation, the source, the equation number read, status (read / secondary / textbook / ours).

## 6. Paper-specific requirements

**Sumit.** As in section 2. Hand limit H: thin plate, open circuit stiffened speed (the formula, not a number). Also the bulk limit that gives thermoelastic damping and the Hutson-White condition (relaxation of free charge equal to the frequency), each by a short worked derivation.

**Neha (1D hexagonal piezoelectric quasicrystal; quasiperiodic direction z, plate normal z).** Unknowns u_x, u_z, w_z (phason displacement), phi, theta. Phonon momentum x and z (nonlocal operator on the inertia as for Sumit), one phason equation with both inertia and relaxation, H_zj,j = rho_p w_tt + gamma w_t (state which terms are in the cited sources and which are ours), Gauss law, MGT heat with thermo-phason and thermo-piezoelectric terms, NSGT on the phonon stress and, as a stated option, the phason stress. Constants of the 1D hexagonal piezoelectric quasicrystal: list the independent elements for the chosen class (phonon c, phason K, phonon-phason R, piezoelectric e and the phason-piezoelectric coupling), and which vanish. Parity: determine and prove by hand which of the couplings (pyroelectric, thermo-phason, piezoelectric-phason) fix the parity of each field; decide whether a symmetric / antisymmetric split exists; state which coupling kills it, if any. Boundary conditions: tractions, double tractions as for Sumit, the phason stress condition H_zz = 0 (or the analogue the sources use), open circuit, adiabatic. Count conditions per face = half the roots. Hand limit H: phason off returns the piezoelectric thermoelastic plate; phason relaxation limits (wave-like when inertia dominates, diffusive when relaxation dominates) from one equation.

**Anu (MEE, BaTiO3/CoFe2O4 composite, poling along z).** Unknowns u_x, u_z, phi (electric), psi (magnetic), theta. Momentum x and z, electric Gauss law, magnetic Gauss law, MGT heat with pyroelectric and pyromagnetic terms and the thermal stress. Constitutive: elastic, piezoelectric, piezomagnetic, dielectric, magnetic permeability, magnetoelectric coefficient alpha (state its unit, s/m in SI, and the sign convention), thermal expansion, pyroelectric and pyromagnetic coefficients. Effective constants by two homogenisation schemes as agreed (state the formulas with citations; the volume fraction v enters only through the effective constants). NSGT on the elastic part. Boundary conditions: tractions and double tractions, electric (open and closed), magnetic (open and closed), thermal (adiabatic and isothermal). Parity analysis by hand as for Neha. Hand limit H: ME coupling off returns the piezoelectric plus piezomagnetic plate; both off returns the thermoelastic plate; the thin-plate low-frequency limit gives the effective ME coefficient.

For all three: the final matrix must have as many rows as roots, with the count proved by degree counting. If the parity analysis shows a split, give the two smaller matrices and the factorisation; if not, give the full matrix. State both when the answer depends on switches.

## 7. Language (human supervisor, not AI)

Write as Dr. Vipin to his scholar: plain Indian English, "we" and "you", short and medium sentences of varied length, concrete pictures (a lift full of people for the size effect, a rope for a wave, and so on, but not copied word for word from the earlier files). Explain a term at first use, in one or two sentences, with its unit.
Forbidden words and habits: delve, moreover, furthermore, it is important to note, in the realm of, comprehensive, robust, leverage, landscape, tapestry, pivotal, crucial, seamless, rhetorical triplets, "not only ... but also" chains, slogan headings, summary sentences that repeat the paragraph, more than one em dash per page, emojis, bold inside running text, bullet lists inside running explanation (real lists such as symbols and steps are fine).
No text about "AI", "assistant", "Arena", "Claude", about earlier versions, mistakes, internal logs or audits, or about what "we have verified". The text may ask the scholar to compare, confirm, locate, and redo. In worked blocks the reasons are one short line each, in the same plain voice (for example "put the plane wave in, every d/dx becomes ik").
Self-check with a script: forbidden words, repeated sentence openings (more than three consecutive sentences starting with the same word), em dashes per page, sentence-length variance. Keep the result in `internal/style_check.md`.

## 8. Numerical verification (internal only)

For each paper build the matrix numerically and independently of the text (your own code; method hints below), and run:

1. Couplings off, l_g = l_nl = 0: Rayleigh-Lamb for an isotropic plate (aluminium E = 70 GPa, nu = 0.33, rho = 2700; c_L 6197.82, c_T 3121.95, Rayleigh 2909.7), both families if they split, at three values of fd; tolerance 1e-5.
2. Add couplings one at a time and compare with the closed limits you derived in Calculation H (thin-plate open-circuit speed, Fourier thermoelastic damping, Hutson-White, and for Neha the phason limits, for Anu the ME limit).
3. l_g, l_nl -> 0 continuity; direction of the shift for l_g and l_nl (stiffen / soften).
4. Check that the number of roots and the number of conditions per face agree, and that det B has a zero crossing at the same place from the singular-value and determinant routes.
5. For each paper confirm by numerics the parity statement you made in Calculation D.
Save numbers, tolerances and the largest residual per test in `internal/<scholar>_matrix_verification.md`. None of it goes into the scholar files.

Method hints (from my reference): use mpmath at about 80 digits for det M(eta) (sample on a circle, FFT-fit coefficients, polyroots) and for null vectors (adjugate column); keep roots in mp precision until the null vector is formed; scale every column of B by exp(-|Re eta_m| h); normalise rows before singular values; spurious small singular values from decoupled blocks are possible, so locate zeros as dips of the smallest singular value on a fine grid and refine.
Placeholder constants for the code are fine; do not put them in the scholar files. Note which constants you used in `internal/`.

## 9. LaTeX and format

article, 11pt, A4. Packages only: fontenc, lmodern, amsmath, amssymb, booktabs, array, geometry, hyperref, amsthm. BibTeX with the .bib file. Both worked-block settings compile; no undefined references or citations; no overfull boxes in equations. Master with working: 35 to 60 pages is fine. Scholar version (flag off): 15 to 25 pages. Date 30 October 2026 or later; author line "Dr. Vipin, Gurugram University". Long matrices: show the entries as a list of equations, or split the matrix into labelled blocks; do not let a matrix run off the page.

## 10. Order of work, reporting, and stops

1. Task 1 (section 2): independent rebuild of Sumit's matrix and the five tests.
2. Write Sumit, Neha, Anu masters (Sumit first so the format can be reused), one after another, without stopping in between. Do the numerical verification for each as you go.
3. Build the three zips, both PDF variants of each (kept in `deliver/preview/`, not inside the zips).
4. Milestone report `reports/packages_v7.tex` (<= 4 pages): per scholar number of equations, number of roots, rows of B, parity result, tests passed with the largest residual, citations read versus not read, page counts of the two variants, open items, anything in my Sumit file you corrected.
5. `STATUS.md` (<= 10 lines) and a chat reply (<= 8 lines). Stop.
A blocker you cannot resolve (for example a source needed for a core equation that cannot be opened, or a contradiction between sources) is the only reason to stop earlier: post it in 8 lines with the options and stop.
Do not start any calculation step for the scholars and do not send anything to them.
