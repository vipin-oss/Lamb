# Task 4 — citation audit, round v8

## Every equation-level citation in the three masters

There are six distinct `\cite[Eq.~(n)]{key}` forms (five keys, Yang and Zhou used three times).

| citation | where it stands | was the equation read? | status |
|---|---|---|---|
| `\cite[Eqs.~(3), (7)]{YangZhou2005}` | Sumit, drift–diffusion current and the carrier flux row | **no** | full text not reachable from here (Elsevier). Bibliographic record verified at Crossref: Yang and Zhou, *Int. J. Solids Struct.* **42** (2005) 3171–3183, DOI 10.1016/j.ijsolstr.2004.10.011. The equations are not verified. |
| `\cite[Sec.~2, Eq.~(14)]{Charal2019}` | all three, the free-face conditions of a gradient solid | yes, Sec. 2, Eq. (14), condition b(i) | verified |
| `\cite[Eqs.~(18)--(19)]{Barretta2018}` | all three, the differential nonlocal law and its constitutive conditions | yes, Eqs. (18)–(19) | verified |
| `\cite[Eq.~(1)]{Zhu2023}` | Sumit, piezoelectric semiconductor balance set | yes, Eqs. (1)–(7) | verified |
| `\cite[Eq.~(26)]{Agiasofitou2014}` | Neha, phason stress | yes, Eq. (26) | verified |
| `\cite[Eq.~(17)]{Baggioli2020}` | Neha, phason damping | yes, Eq. (17) | verified |

One item is unverified and should be treated as such: the two equations of Yang and Zhou used for
the drift–diffusion current. Either open the paper and confirm (3) and (7), or cite it without
equation numbers. Nothing else in the three masters attributes an equation number it has not seen.

## Chained attribution

The three masters quote the equation numbers of Lim, Zhang and Reddy through the introduction of
Barretta and Marotti de Sciarra, and each says in its own text that the Lim paper was closed to it
(Sumit around line 198, Neha around line 176, Anu around line 167). That is the explicit chaining
the referee asked for; no change is needed. What should not happen — and does not — is a sentence
of the form "their Eq. (18)" that reads as if the Lim paper had been opened.

## Yang and Zhou: which DOI

Both DOIs are real, and they are two different papers by the same two authors, both from 2005.

| DOI | record |
|---|---|
| 10.1016/j.ijsolstr.2004.10.011 | Yang, J. S. and Zhou, H. G., *Amplification of acoustic waves in piezoelectric semiconductor plates*, Int. J. Solids Struct. **42**(11–12), 3171–3183 (2005) |
| 10.3233/JAE-2005-694 | Yang, J. S. and Zhou, H. G., *Wave propagation in a piezoelectric ceramic plate sandwiched between two semiconductor layers*, Int. J. Appl. Electromagn. Mech. **22**(1–2), 97–109 (2005) |

Both were read at Crossref (`api.crossref.org/works/<doi>`) on 30 October 2026. The bib entry in
all three masters carries volume 42, pages 3171–3183 and the Elsevier DOI, and that is the IJSS
paper, so **the bib is correct and no change is made**. The referee's DOI belongs to the
sandwiched-layer paper; if a result from that paper (anti-plane waves in a piezoelectric plate
between two semiconductor layers) is used, it needs its own bib entry rather than replacing this
one.
