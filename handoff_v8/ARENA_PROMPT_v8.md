# Arena prompt v8: verify and correct the three masters (v8 is the new base, do not revert it)

Repo vipin-oss/Lamb, branch claude/v6-handoff, folder handoff_v8/ (Sumit/, Neha/, Anu/: one .tex + one .bib each; Lamb_All_v8.zip).
Work on your own pinned branch; never touch main. Standing rules as before: reports <= 4 pages LaTeX, STATUS.md <= 10 lines,
chat <= 8 lines, never invent a reference, equation number or constant.

## 0. Context
Your v7 masters were reviewed by Claude and by an external referee (GPT). v8 is the corrected base. These errors were found
and fixed by hand, so your next version MUST start from v8 and keep these fixes:
1. Anu: M33, M34, M43, M44 had the wrong sign (Gauss rows are +divergence; correct entries are eps11 k^2 - eps33 eta^2, alpha11 k^2 - alpha33 eta^2, mu11 k^2 - mu33 eta^2).
2. Neha: M44 same sign error; M35 must be -eta*beta^w (the worked step said so, the result line said +); heat equation needs the dot on w_zz.
3. Typesetting: "&==" and broken align continuation lines in all three; duplicate labels eq:M1..M4 in Sumit.
4. Sumit Calculation H: the coefficient of x in the isotropic polynomial is c33 (c11 k^2 - A) + c44 (c44 k^2 - A) - k^2 (c13 + c44)^2, not c11(...).
5. Units: beta_th is m^-1 s^-1 K^-1; m3 (pyromagnetic) is Wb m^-2 K^-1.
6. Null vector choice: largest-norm column of the adjugate, null-space basis if the adjugate vanishes.
7. Parity wording for Sumit: "for generic values of the other constants, exactly when beta_th = Pi_th = E_g = 0".
8. Thin-plate formula: stated as the local limit (l/h -> 0 first, then kh -> 0).
9. New paragraph "An open point about the closure of the model" at the start of Calculation F in all three.
Why you missed 1 and 2: your numeric tests only checked parity and degree, never the entries against the constitutive laws.

## 1. TASK 1: independent numerical check of every entry (the main job)
For each paper, write your own code that builds M(eta) (5x5) directly from the component constitutive laws and field
equations (not from the entries printed in the tex), with physically scaled constants, then PARSE the entries from the
v8 .tex (or retype them carefully) and compare entry by entry at several (k, omega, eta). Report the maximum relative
difference per entry. Any mismatch is an error in the tex: fix it in the tex and list it. Do the same for the boundary row
functions b_1..b_7 and the final matrix B (assemble from roots and null vectors; mpmath ~80 digits, adjugate null vectors,
column scaling exp(-|Re eta| h)).

## 2. TASK 2: dispersion-level tests (all three papers)
a) Couplings off, l_g = l_nl = 0: roots of det B reproduce isotropic Rayleigh-Lamb, both families, three fd values (aluminium E = 70 GPa, nu = 0.33, rho = 2700: c_L 6197.82, c_T 3121.95, Rayleigh 2909.7 m/s), tolerance 1e-5.
b) One coupling at a time: piezoelectric open-circuit thin-plate speed; Fourier thermoelastic bulk damping k_i/k_r = (Delta_E/2) w tau/(1 + (w tau)^2); Hutson-White attenuation peak at n0 = eps w/(q b_n) for Sumit; phason wave-like and diffusive limits for Neha; ME limits for Anu.
c) l_g, l_nl -> 0 continuity of the lowest branches (track roots by continuity; the extra roots escape to infinity); direction of the shifts (l_g stiffens, l_nl softens).
d) Parity claims with physically scaled constants, each coupling separately: Sumit odd powers appear iff beta_th, Pi_th or E_g is non-zero; Neha and Anu: report what you find.
e) Number of roots = number of rows of B (14 or 10), singular-value route and determinant route agree on the zeros.
Store numbers in internal/; none in the tex files.

## 3. TASK 3: the closure of the nonlocal boundary problem (the real open point)
The referee is right that dividing by N(eta_m) root by root does not by itself prove equivalence of the differential law with
the integral law on [-h,h]. Read what you can (Barretta and Marotti de Sciarra IJES 130 (2018) 187; Lim, Zhang, Reddy JMPS 78
(2015) 298 Sec. 2, Eqs. (17)-(19) if you can open them; open-access NSGT plate/beam papers that state the constitutive
boundary conditions). Then, in one short report section:
(i) state which constitutive boundary conditions the literature uses for a plate or beam with the NSGT differential law;
(ii) compare them with our seven rows per face; say if ours are equivalent, a subset or a different choice;
(iii) if they differ, build the alternative B numerically and show how much the lowest-branch dispersion changes for
l/h = 0.05, 0.1, 0.2 (numbers in internal/ and a one-line verdict in the report);
(iv) propose, do not impose, the wording for the paragraph "An open point about the closure" so the scholar gets a precise
statement. Do not change the seven rows in the tex without a source you actually read.

## 4. TASK 4: citations
For every \cite[Eq.~(n)]{key} say whether you read that equation (page, section). Replace any attribution of the type
"their Eq. (18)" that comes through Barretta by wording that makes the chain explicit (Lim et al. as quoted by Barretta).
Check Yang and Zhou 2005: the bib has doi 10.1016/j.ijsolstr.2004.10.011 (Int J Solids Struct 42, 3171); the referee gave
10.3233/JAE-2005-694. Decide with Crossref which belongs to which paper and fix the bib only if the bib is wrong.

## 5. Language and format
Rules of v7 stay (human supervisor voice, no AI-sounding words, no history/internal remarks in the tex, worked blocks hide with
\showworkedfalse, both settings compile, bibtex). In the tex avoid sentences written as instructions about "the paper must";
write them as plain statements to the scholar ("you should state in your manuscript ..."). If a LaTeX engine is not
available, say so and keep the code conservative; Claude compiles.

## 6. Deliver and stop
Corrected masters as handoff_v8-based zips deliver/Lamb_<Scholar>.zip (tex + bib only), changelog in reports/packages_v8.tex
(<= 4 pages: each fix with file, label, what was wrong, how the numeric test found it; tests passed with largest residual;
Task 3 verdict; citation status), STATUS.md, chat reply <= 8 lines. Stop after delivering. If a test fails and you cannot find
the cause in two attempts, report it and stop on that item; do not paper over it.
