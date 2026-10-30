# Arena prompt v6: one complete paper-style .tex (+ .bib) per scholar, FULL calculation to the final matrix, every step shown

v6 REPLACES v5 on three points (items 3 and 1 of section 0 and the zip contents). Everything else in v5 stands. Read this whole file.

Work on the pinned branch of the `lamb` repo. Earlier rules stay: milestone report as ONE self-contained LaTeX
file (<= 4 pages), STATUS.md <= 10 lines, chat replies <= 8 lines, never invent a reference, equation
number or constant. Everything is in the repo on branch `claude/v6-handoff`: `handoff_v6/Sumit_v2/` (my current Sumit files, 3 .tex) and `handoff_v6/reference_code/` (my numerical reference for Sumit's matrix). Read them first. Do not merge anything into main.

## 0. What Dr. Vipin decided (this replaces the 3-file / 2-file packages)

1. **One single .tex plus one .bib per scholar.** All references live in the .bib file (BibTeX, compiled with `pdflatex`, `bibtex`, `pdflatex` twice; plain `\bibliographystyle{unsrt}`). Zip = exactly two files: `Lamb_<Scholar>.tex` and `Lamb_<Scholar>.bib`. No separate basics file. Every term is defined at the place where it first
   appears, in a sentence or two of plain words, with its unit. A class-10 student should be able to follow
   each definition without turning to another file. Three .tex files in total: `Lamb_Sumit.tex`,
   `Lamb_Neha.tex`, `Lamb_Anu.tex`. Deliver as `deliver/Lamb_<Scholar>.zip` containing the .tex and the .bib only.
2. **Content goes further than before.** Up to and including the final matrix:
   title, abstract, introduction and gap (with citations) -> assumptions -> notation -> strain-displacement ->
   constitutive relations (with the size effect) -> the 5 governing field equations in component form ->
   plane-wave reduction -> the matrix M(eta) with every non-zero entry -> characteristic equation and the
   number of roots -> solution through the thickness (partial waves) -> boundary conditions on the free
   faces -> the final boundary matrix B -> dispersion relation det B = 0 -> list of self-tests -> short work
   plan -> references.
3. **FULL calculation, every small step shown (changed from v5).** Dr. Vipin will remove the worked parts himself before handing the file to the scholar, so the master file must contain the whole chain, small steps included: how each stress component follows from the constitutive law, how each field equation is written in components, the substitution of the plane-wave ansatz, the arithmetic leading to every entry of M(eta), how the characteristic polynomial and its degree arise, how the amplitude ratios (cofactors) are obtained, how each boundary row is formed from the root data, how the 14x14 (or 10x10) matrix is assembled, and the limits (coupling off) with the working. Number every equation and give each step its own line with a one-line reason. Mark the worked-out parts so they can be removed cleanly: put each worked block inside `\begin{worked}...\end{worked}` (define the environment in the preamble; add a switch `\showworkedtrue/\showworkedfalse` using plain `\newif` so that one flag hides all worked blocks and leaves a version with results only). Then the file works as the master (flag true) and as the scholar version (flag false). Still no code and no programming steps, and no numerical benchmark values (no c values, no K^2, no roots).
4. **Every starting equation carries a citation with the equation or section number you actually read** (`\cite[Eq.~(n)]{key}`; keys in the .bib file; put the DOI or arXiv number in each bib entry). A column or sentence "where it comes from" for each source equation, so the reader sees which equations are taken from literature and which follow from them by calculation. Equations that are derived in the file are marked "derived here, steps in Section ...". If you did not
   read it, say so inside the sentence and say what law it follows from (for example "textbook law, equation
   number not read, please locate it in X"). No made-up numbers. If a statement is ours, say "ours".
5. **The model must stay rich:** heat (MGT) in all three, at least five coupled field equations, NSGT size
   effect. Keep the effects already agreed in `reports/model_v4.tex`.
6. **Language must read as written by a human supervisor** (section 5).

## 1. What I already did for Sumit (use it as the template and check it)

In `Lamb_Sumit_v2.zip`, file 03 contains the full chain for Sumit (five unknowns u_x, u_z, phi, Delta n,
theta). The numerical reference code reproduces these tests: isotropic Rayleigh-Lamb (both families) to
1e-6 relative; open-circuit S0 of the piezoelectric plate (5509.56 against 5509.57 in the repo);
Fourier thermoelastic bulk damping k_i/k_r against the closed formula; Hutson-White attenuation peak
location in n0; correct direction of the NSGT shifts. Findings you must re-check independently, not trust:

- det M(eta) has degree 14 when l_g != 0 (gradient operator), and 10 when l_g = 0 (nonlocal operator alone does not raise the order).
- With thermodiffusion and Peltier terms ON together with piezoelectric or pyroelectric constants, det M(eta) is not even in eta, the roots do not come in +-pairs, and the plate modes do not split into symmetric and antisymmetric families. With beta_th = Pi_th = 0 they do.
- The free-face conditions I chose (seven per face): total traction (with the surface-gradient term, Charalambopoulos et al. arXiv:1909.10776 Sec. 2 Eq. (14)), double traction n.mu.n, open-circuit D_z = 0, zero carrier flux, adiabatic face. The nonlocal operator is inverted root by root (1/N(eta_m)). These are modelling choices, flagged as such in the text.

**First task:** re-derive M(eta) and the 14x14 matrix for Sumit independently (do not copy my code; you may read it),
confirm or correct every entry of file 03, and rerun the five tests. Report differences in the milestone
report. Then rewrite Sumit as ONE file in the new format (item 1 above).

## 2. Numerical method hints (learned the hard way)

- Use mpmath (about 80 digits) for the polynomial det M(eta) (sample on a circle, FFT-fit, `polyroots`) and for the null vectors (adjugate column). Double precision gives wrong roots and wrong null vectors here because entries differ by 30+ orders of magnitude.
- Keep roots in mp precision until the null vector is formed; converting to complex first destroys the null vector.
- Scale each column of B by exp(-|Re eta_m| h) to avoid overflow from the thermal and carrier boundary-layer roots.
- Normalise rows of B before singular values. A decoupled block can leave spurious small singular values; find roots as dips of the smallest singular value on a fine grid and refine, or use det with scaling.
- Fix the plane-strain convention (u_y = 0, d/dy = 0) and the exp[i(kx - wt)] convention; k = k_r + i k_i, k_i > 0 decay.

## 3. Papers Neha and Anu: same chain

Use the models in `reports/model_v4.tex` as agreed (Neha: u_x, u_z, w_z (phason), phi, theta; Anu: u_x, u_z, phi, psi, theta). For each:

1. Write the component form of constitutive relations and the five equations; list which tensor elements survive for the crystal class and the chosen axis (Neha: 1D hexagonal quasicrystal with the quasiperiodic direction along z and the plate normal along z, check the case of plate normal different from the quasiperiodic axis only if the model needs it; Anu: hexagonal 6mm-type composite, poling along z).
2. Reduce to M(eta) (5x5), give every non-zero entry, count the degree of det M(eta) with and without l_g, and state parity properties of the roots (is the determinant even in eta? does a symmetric/antisymmetric split exist, and which couplings destroy it?). State only what you verified numerically.
3. Give the solution as a sum of partial waves.
4. Choose and justify the free-face conditions: tractions and double tractions as for Sumit; for Neha the phason stress H_zz (or its chosen analogue) and a phason condition, for Anu electric and magnetic conditions (open or closed, both stated) and the thermal condition (adiabatic, with isothermal as the alternative). Say clearly which are our choice. Count: number of conditions per face must equal half the number of roots.
5. Give the final matrix B, the dispersion relation, and the scaling note.
6. List self-tests with no numbers in the scholar file, for example: all couplings off gives the isotropic Rayleigh-Lamb relation; phason off or magnetic coupling off returns the previous model; l_g, l_nl -> 0 continuity; bulk thermoelastic damping sign; one test specific to the field (Neha: phason relaxation limit, wave-like and diffusive; Anu: ME coefficient of the composite as a function of volume fraction when the plate is thin and the frequency is low).
7. Numerical verification as for Sumit: build the matrix independently, run the tests, put numbers in `internal/<scholar>_matrix_verification.md`. Never in the scholar file.

Source reading: look for open-access material first (arXiv, PMC, MDPI, publisher open pages). Read the numbered equations of the sources for quasicrystals (phonon-phason-thermal governing equations, constitutive relations, boundary conditions, plates) and for magneto-electro-elastic media (constitutive, thermal, pyroelectric, pyromagnetic terms), and record in `internal/<scholar>_equation_source_log.md` what you read and which equation numbers. Fetching Zhu et al., Micromachines 14 (2023) 2174 and Quintanilla, Math. Mech. Solids 24 (2019) 4020 worked for me (the second through the upcommons PDF); paywalled pages did not.

## 4. Structure of each single file (guide, adapt as needed)

1 Title, abstract (6 lines), keywords. 2 Introduction (what the problem is in plain words, what is known with citations, the gap, what this paper does). 3 Setting and assumptions. 4 Notation: a table with symbol, meaning in words, unit, and a short everyday picture where it helps (not typical numbers). 5 Governing equations (strain, constitutive with size effect, field equations, MGT heat), each with source sentence. 6 Plane-wave reduction and matrix. 7 Solution through the thickness. 8 Boundary conditions and the final matrix. 9 How to test your own work (list of tests, no numbers). 10 Work plan in weeks (short). References. Definitions of wave, plate, dispersion, mode, cutoff, attenuation, complex wavenumber, potential, balance law, size effect, nonlocal, gradient, MGT, relaxation time, piezoelectricity, and the material-specific ideas go **in place**, at their first use, in plain words. With the worked blocks shown the file may be long (30 to 50 pages is fine); with the flag off it should be about 15 to 22 pages.

## 5. Language

Write as Dr. Vipin to his scholar, plain Indian English, "we" and "you", short and medium sentences, varied. Concrete pictures. Forbidden: delve, moreover, furthermore, it is important to note, in the realm of, comprehensive, robust, leverage, landscape, tapestry, pivotal, crucial, seamless; rhetorical triplets; "not only ... but also" chains; slogan headings; summary sentences that repeat the paragraph; more than one em dash per page; emojis; bold in running text; bullet lists inside running explanation. No text about "AI", "assistant", "Arena", "Claude", about earlier versions or mistakes, internal logs, audits, or about what was "checked" or "verified" by us. The text may ask the scholar to compare, confirm, locate, and redo. Worked steps are allowed only inside the `worked` blocks, so that the flag-off version has none. Run the forbidden-word and repeated-opening scan and keep the result in `internal/style_check.md`.

## 6. LaTeX

article, 11pt, A4; packages only: fontenc, lmodern, amsmath, amssymb, booktabs, array, geometry, hyperref, amsthm. a .bib file with `bibtex` (not thebibliography). Compile with pdflatex, bibtex, pdflatex, pdflatex, no undefined references or citations; both flag settings must compile, no overfull boxes beyond 1 pt in equations. Date 30 October 2026 or later. Author: Dr. Vipin, Gurugram University.

## 7. Order and stops

1. Sumit: independent check of my file 03 (report differences and test results), then the single-file Sumit. **Post the milestone report and 8-line summary. Stop.** I review before you go on.
2. After my "go": Neha, then Anu, each with the same report. Stop after each.
3. `reports/packages_v5.tex` (<= 4 pages): per scholar number of equations, roots, rows of B, tests passed with the largest residual, citation count with how many were read versus not read, open items.
4. Do not start any calculation step for the scholars.
