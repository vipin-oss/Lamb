# Style self-check, v4 packages

Six documents: `01_Research_Plan_*` and `02_Basics_and_Definitions_*` for Sumit, Neha and Anu.
Checked on 30 October 2026, before zipping. Fixes are logged, not hidden.

## Automated scan

| Item | Rule | Result | Action |
|---|---|---|---|
| Forbidden words (delve, moreover, furthermore, it is important to note, in the realm of, comprehensive, robust, leverage, landscape, tapestry, pivotal, crucial, seamless) | none | zero hits in all six | none needed |
| "not only ... but also" chains | none | two "not only" constructions found, in Sumit basics (size effect) and Anu basics (size effect) | both rewritten as "as well as" / "and not ... alone" |
| "check", "verified", "UNVERIFIED", "Arena", "Claude", "AI" | none | zero hits in the six documents | none needed |
| Bold in running text | none | run-in labels were set with `\textbf{}` in the three plans (working title, abstract, keywords, steps, figure paragraphs) | all converted to `\paragraph{}` headings. Remaining `\textbf` is only the volume number in bibliography entries |
| Em dashes | at most one per page | zero `---` in all six | none needed |
| Emojis | none | none | none needed |
| Bullet lists | only real lists | itemize used nowhere; enumerate used three times, once per plan, for the list of assumptions | kept, these are real lists |
| Slogan headings | none | section headings are plain nouns ("Introduction", "The model", "Work plan") | none needed |
| Sentences repeating the paragraph | none | one instance in the Sumit abstract ("Numbers are deliberately absent at this stage") was kept because it states a scope decision, not a summary | kept, flagged here |

## Structural scan

| Item | Result |
|---|---|
| Brace balance | zero delta in all six |
| `\begin`/`\end` balance | matched in all six |
| Odd number of `$` per line | none |
| Packages used | fontenc, lmodern, amsmath, amssymb, booktabs, array, geometry, hyperref only |
| Class and size | article, 11pt, a4paper |
| Bibliography | `thebibliography` in each plan; basics documents carry no citations by design |
| Dates | 30 October 2026 on every title page |
| Author block | Dr. Vipin, Gurugram University |
| Engine | no LaTeX engine in this workspace, so nothing is compiled. Code kept conservative: no `\usepackage{tikz}`, no `\includegraphics`, no custom environments |

## Content scan against the scope rules

| Rule | Result |
|---|---|
| No derivations | none. The reciprocal-coefficient relation in Sumit's plan is stated, not derived; the derivation is the scholar's task |
| No dispersion determinant | none |
| No solution method | none. The plans say the scholar chooses the method; the steps state what is compared, not how to invert the matrix |
| No boundary conditions | none. Each plan ends its model section with a sentence handing the faces to the scholar |
| No benchmark numbers | none in the six documents. All numbers (Rayleigh velocity, Set L constants, tau_q maps) live in `internal/*_benchmarks.md` |
| Every equation sourced in the plan | the source log carries each equation with the status I can defend: [R], [S], [T], [D], [P] |
| Supervisor voice | yes: "we", "you", plain sentences, mixed length. The basics documents address the reader directly |
| Novae stated as search results | yes, three times, each with the month of the search, the databases, and the named neighbours |

## One thing I could not fix

The paragraphs are long in the model sections, because the equations are long and each one needs a sentence
of justification. If Dr. Vipin wants a shorter page count after compilation, the cuts should come from the
figure paragraphs in the plans, not from the model.
