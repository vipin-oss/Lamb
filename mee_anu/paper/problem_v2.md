# Problem v2 — Paper C (Anu): Lamb waves in a magneto-electro-elastic plate

Status: proposal for the Task-0 gate. Conventions as in `docs/02_workflow_crosscheck.md`
(exp[i(kx−ωt)], thickness 2h, faces z = ±h, plane strain, k = k_r + i k_i, k_i > 0 decays,
fd = f·2h in Hz·m). Unchanged.

## 1. Working title

**The magnetoelectric optimum is not a material constant: a frequency-dependent design ridge for
BaTiO₃/CoFe₂O₄ plates with MGT heat and nonlocal strain gradient elasticity.**

## 2. One-sentence finding (the hook)

> In a magneto-electro-elastic plate the volume fraction of piezomagnetic phase that maximises the
> magnetoelectric coupling is **not a material constant** — it is set by a mechanical matching
> condition between the two phases at the working frequency-thickness, so the optimum traces a ridge
> in the (vf, fd) plane, whose position moves with the two NSGT length scales and the MGT relaxation
> time; the static optimum quoted in the materials literature is the `fd → 0` edge of that ridge.

Checkable: plot ME coupling vs vf at five `fd`; the peak moves. At `fd → 0` it must land on the
published static optimum.

**What the hook replaces.** `docs/03_novelty_upgrades.md` proposed an "ME design map with inverse
design". That is kept in spirit but made falsifiable: a map is not a finding, a *ridge that moves
with frequency and size scale* is. The four face conditions (electric open/short × magnetic
open/short) become four ridges, which is where the design rule comes from.

## 3. Three claims

### C1 — The ME coupling of the plate is non-monotonic in volume fraction, and its optimum is a function of fd.
- **Statement.** For each of the four face-condition combinations, the mode-resolved ME coefficient
  `K_ME(vf, fd)` has an interior maximum in `vf ∈ (0,1)`, and the maximising `vf*(fd)` is
  frequency-dependent.
- **Definitions (must be fixed before Step 2 — the feasibility doc already demanded this).**
  Three coefficients per mode and per `fd`: electric `K_E²(fd)`, magnetic `K_M²(fd)`, and the cross
  one `K_ME(fd)`, defined as the relative change of phase velocity between the relevant open and
  short face conditions, with the formula written explicitly in `steps/step2_*.md`. No "K²" will
  appear in the paper without its defining equation.
- **Figure F4.** `K_ME` vs `vf` for five `fd`, four face conditions (2×2 panels), with `vf*(fd)`
  marked.
- **Limiting cases.** `vf = 0` must return the pure piezoelectric plate with `K_ME ≡ 0`, and
  `vf = 1` the pure piezomagnetic plate with `K_ME ≡ 0`; both to < 1e-6.
- **Fails if.** `K_ME` is monotone in `vf` at every fd. Then the static optimum story is all there is
  → Q2.

### C2 — The ridge is a mechanical matching condition, anchored by the static limit.
- **Statement.** `vf*(fd)` is controlled by the `fd` at which the two phases deform with matched
  strain — predictable from the two phase wave speeds and the thickness — and not by a percolation
  or rule-of-mixtures argument. In the quasi-static limit the ridge must collapse onto the published
  static optimum for BaTiO₃/CoFe₂O₄.
- **Figure F5.** Ridge `vf*(fd)` in the (vf, fd) plane, with the two phase-dispersion curves that
  produce the matching, and the `fd → 0` anchor marked.
- **Limiting cases.** (a) `fd → 0` reproduces the static optimum of the materials literature to
  < 5% (order-of-magnitude anchor, since the homogenisation differs — state the source of the static
  value and the tolerance). (b) If the two phases are given identical properties, the ridge
  degenerates to `vf* = 0.5` by symmetry — a machine-exact check.
- **Fails if.** the `fd → 0` anchor misses by more than 5%; then either the homogenisation or the
  matching argument is wrong and this claim must be withdrawn before writing.

### C3 — NSGT and MGT move the ridge, and the four face conditions give four different ridges.
- **Statement.** The two length scales shift the ridge in `fd` by an amount that grows with `kh`, and
  the MGT relaxation time deforms it near the thermal relaxation frequency; the electric and
  magnetic face conditions act on *different* parts of the ridge, which produces a design rule
  (which face condition to choose at a target fd).
- **Figure F7.** Ridge shift contours in the `(l_nl, l_g)` plane for each of the four face
  conditions, plus a one-line design rule box.
- **Limiting cases.** `l_nl = l_g = 0` returns Step 4; `τ_q → 0` returns Fourier; nonlocal-only and
  gradient-only give opposite shifts.
- **Fails if.** the four ridges coincide within the resolution — then the face conditions do not
  matter for the optimum and the design rule is empty.

## 4. Upgrades: one major, one minor

**U1 (major) — the dynamic ME ridge and its design rule.** Physics justification: the ME effect is a
product property that requires strain transfer between phases; strain transfer is a dynamic
condition in a plate, so the optimum must be frequency-dependent. This is a statement about the
material response, not an extra term in the model.

**U2 (minor) — effective-constant sensitivity across homogenisation methods** (Shared upgrade S5,
here applied to the *inputs* rather than to the outputs): the ME ridge is computed with at least two
published homogenisation schemes for the same volume fractions, and the ridge is reported as a band.
This is the honest answer to the "effective constants depend on the source" objection that
`docs/00_feasibility_analysis.md` raises.

**Demoted/not used:** S3 (exceptional points) — the MEE plate has no strong single dissipative
channel; S1 — subsumed in U2; S4 — future work.

## 5. Model definition

### 5.1 Fields
`u_x, u_z` (elastic), `φ` (electric potential), `ψ` (magnetic potential), `θ` (temperature). Plane
strain, wave along x. Quasi-static electromagnetic approximation (wave speeds ≪ c), which is standard
and must be stated.

### 5.2 Couplings
Transversely isotropic (6mm) poled along z, homogenised composite:
`σ = Cε − eE − qH − λθ`, `D = eε + εE + αH + pθ`, `B = qε + αE + μH + mθ`,
with `e` piezoelectric, `q` piezomagnetic, `α` the magnetoelectric (product) tensor, `p` pyroelectric,
`m` pyromagnetic. NSGT differential form applied to the mechanical part only (`α` and the
electromagnetic parts are not strain-gradient objects — this restriction is stated, not hidden).
Equation of motion `σ_ij,j = ρü_i`; Gauss `D_i,i = 0`; magnetic Gauss `B_i,i = 0`; MGT heat equation
with the pyroelectric/pyromagnetic source terms.

### 5.3 Boundary conditions at z = ±h
Mechanical: `σ_zz = σ_xz = 0`, plus the **NSGT higher-order traction** `P_izz = 0`
(`steps/step5_bcs_nsgt.md`, approval required before coding). Electromagnetic four ways:
`D_z = 0` / `φ = 0` × `B_z = 0` / `ψ = 0`. Thermal: `∂θ/∂z = 0` or `θ = 0`. The 2×2 table of face
conditions must appear in the caption of **every** figure — the plan already identified this as the
main bookkeeping risk.

### 5.4 Excluded
Surface/interface effects, flexomagnetoelectric coupling, imperfect interfaces (owned by JIMSS
2025), graded and porous phases, nonlinearity, 3D, multiferroic single-phase materials, eddy
currents, and frequency-dependent (relaxor) properties.

## 6. Validity window

Shaded trust band `kh ∈ [0.05, min(1/λ, 2h/10Λ_ph)]` on every figure, hatched beyond, `h/l_max` in
the caption. Additional MEE-specific bound: the homogenised constants are meaningful only when the
phase size is much smaller than the wavelength and the plate thickness — this bounds `kh` from
*below* relative to the microstructure, and must be stated because the design map spans `vf` where
one phase may become a thin layer.

## 7. Parameter plan

| Group | Source | Status |
|---|---|---|
| BaTiO₃ single-phase `C, e, ε, p, ρ, c_p, k_th` | published MEE tables, to be fixed at Step 1 | `[U]` |
| CoFe₂O₄ single-phase `C, q, μ, m` | same | `[U]` |
| Homogenisation (2-2 laminate / 0-3 / Mori–Tanaka) | at least two schemes, named | `[U]` |
| Volume fraction | 0, 0.2, 0.4, 0.6, 0.8, 1.0 (as the plan specifies) | fixed |
| `τ_q` | no measured MEE value; range 10⁻¹³–10⁻¹¹ s | `[U]` range, labelled assumed |
| `l_nl, l_g` | **dimensionless `l/h` sweeps only** (Dr. Vipin's ruling for Paper A; applied here) | — |
| Static ME optimum for the anchor | must come from a citable table/paper, not from our own 2-2 calculation | `[U]` — needed before C2 can be claimed |

**Sensitivity ranking.** (i) the homogenisation scheme (U2 exists precisely for this);
(ii) the static ME anchor value; (iii) `vf` resolution near the ridge; (iv) `τ_q`; (v) `l/h`.

## 8. Target journals (SJR 2025 read on scimagojr, 30 Oct 2026)

| Rank | Journal | SJR / quartile | Fit |
|---|---|---|---|
| 1 | **Int. J. Solids Struct.** | 1.002, Q1 (six categories) | The MEE-plate benchmark [1] is here; a design-rule paper with a verification table fits |
| 2 | **Eur. J. Mech. A/Solids** | 1.023, Q1 | Good landing spot if the ridge is clean but the novelty is judged modest |
| 3 | **J. Intell. Mater. Syst. Struct.** | **not checked this session — do not assume Q1** | Thematic home of MEE plates [2], but must be verified before it is called a target |

Explicitly not targeted: *Wave Motion* (Q2, 0.499 in SJR 2025). *Composite Structures*,
*Smart Materials and Structures* — home of several neighbours, not checked.

## 9. What would change this problem again
1. If C1 fails (monotone), the dynamic-optimum story dies → Q2.
2. If the `fd → 0` anchor misses by > 5%, C2 is withdrawn and the paper is "MGT + NSGT for MEE
   plates", which the sweep says is not Q1.
3. If a 2026–27 paper publishes a frequency-dependent ME optimum, the paper needs a new spine.
