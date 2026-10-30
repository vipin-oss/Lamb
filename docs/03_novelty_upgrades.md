# Novelty upgrades: what to add so each paper has a finding, not just a bigger model

Rule: **one major + one minor upgrade per paper.** More than that hides the story and
delays submission. The base plan (Steps 1-6) stays untouched; upgrades are Step 7+.
An upgrade counts only if it produces a statement of the form "we show that ... which
earlier models cannot show".

## Shared upgrades (apply to all three, cheap, high value)
| # | Upgrade | Why a Q1 reviewer cares | Cost |
|---|---|---|---|
| S1 | **Attenuation budget by energy flux**: split k_i into thermal / carrier (or phason) / size-effect parts using energy balance | Turns "heat and carriers cause fading" into a quantitative, checkable result | medium |
| S2 | **Group and energy velocity** next to phase velocity, with mode shapes | Devices use group velocity; most plate papers stop at phase | low |
| S3 | **Exceptional points / mode coalescence** in the complex (omega, k) plane when MGT damping is present; branch-veering maps | Genuinely new physics for dissipative plates, visual and publishable | medium |
| S4 | **Calibrating the length scales** against a lattice model (Born-von Karman chain / atomistic dispersion) over the k range | Answers the Shaat critique and the "where do l values come from" question directly | medium |
| S5 | **Global sensitivity (Sobol indices)** instead of one-at-a-time ranking | Standard in good computational mechanics papers; makes uncertainty credible | low |
| S6 | **Validity window**: state the (k h) range where NSGT is physically trusted, shade it on every dispersion figure | Preempts the biggest reviewer objection | low |

Recommended: S1 + S3 + S6 in every paper; S4 where time allows.

## Paper A (Sumit, semiconductor): major = DC drift bias
- **Major: non-reciprocal Lamb waves with acoustoelectric amplification.** Add a DC drift
  field/carrier drift velocity v_d. Waves travelling with/against the drift now have different
  speed and attenuation; above a threshold v_d ~ phase velocity, k_i changes sign (gain).
  Show the gain threshold vs plate thickness, carrier density, MGT relaxation time and the two
  size scales. This is the Hutson-White physics in a plate, with heat and size effects: a clear
  device story (amplifier, isolator) and not available in the closest papers (Dhib 2024 etc.).
- Minor: S1 (carrier vs thermal attenuation budget), S6.
- Check: v_d = 0 returns Step 5; gain threshold in the classical limit matches the
  half-space/bulk Hutson-White result.

## Paper B (Neha, quasicrystal): major = phason model comparison + exceptional points
- **Major: wave-like vs diffusive phason as an attenuation/coalescence mechanism.** Diffusive
  phason gives intrinsic damping; show how it creates exceptional points between the
  phonon-like and phason-like branches and how MGT heat shifts them. Present a map in
  (phason relaxation, coupling) space.
- Minor: quasi-periodic axis in-plane vs through-thickness (shows when the S/A split fails),
  S3, S6.
- Check: phason diffusion -> 0 and coupling -> 0 returns Step 4.

## Paper C (Anu, MEE): major = magnetoelectric design map and optimum
- **Major: inverse design.** Define the magnetoelectric coupling coefficients for the four
  face conditions (electric open/short x magnetic open/short). Find the piezomagnetic volume
  fraction and thickness that maximise ME coupling at a target frequency, and show how the
  optimum shifts with the two size scales and MGT relaxation. Give a design rule.
- Minor: effective-constant sensitivity across homogenisation methods (S5), S6.
- Check: volume fraction 0 and 1 return pure piezoelectric / pure piezomagnetic plates.

## Not recommended (scope creep)
Nonlinear effects, full 3D, graded layers, surface elasticity, flexoelectricity, imperfect
interfaces: keep as future work exactly as the plans say.

## Honest caveat
Adding upgrades raises Q1 chance only if the finding is clean. If after Step 6 the major
upgrade shows nothing surprising, drop it and submit the base paper to a strong Q2 journal
rather than delay.
