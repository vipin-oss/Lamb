# Bulk-speed audit of every quoted dip (30 October 2026)

A dip of the smallest equilibriated singular value that sits on a bulk speed is not a plate mode.
At `k = omega/c` with `c` equal to a bulk speed, a root of `det M(eta,k,omega) = 0` passes through
`eta = 0` and the plate determinant vanishes for every thickness, every length and every set of
boundary rows. The bulk speeds are the zeros of `det M(0, omega/c, omega)` in `c`.

## Bulk speeds of the four constant sets

Elastic values are exact (`sqrt(c11/rho)`, `sqrt(c44/rho)`); the stiffened ones are the closed-form
plane-strain values `sqrt((c11 + e31^2/eps11)/rho)` and `sqrt((c11 + q31^2/mu11)/rho)`, and the
piezoelectric one was verified numerically in the plate limit (Sumit: 5509.2 against 5509.57 for the
plane-stress value, a different number because the plate is plane stress and the bulk is plane
strain).

| constants | c_L (m/s) | c_T (m/s) | piezo-stiffened c_L | magnetic c_L |
|---|---|---|---|---|
| aluminium (Sumit elastic runs) | 6197.82 | 3121.95 | --- | --- |
| ZnO, Sumit defaults | 6076.10 | 2732.18 | 6138.04 | --- |
| Neha defaults | 5428.10 | 2897.04 | 5473.60 | --- |
| Anu defaults | 6280.25 | 2771.08 | 6292.16 | 6284.18 |

The bulk speeds do not depend on the frequency while `l = 0`. With `l > 0` they move by
`O(l^2 k^2)`, at most `1e-4` relative for the size-effect runs (`l/h <= 0.2`), far below the
half-per-cent threshold used here.

## Every quoted dip against its nearest bulk speed

| paper | fd | dip (m/s) | nearest bulk | distance |
|---|---|---|---|---|
| Sumit, Al | 10 | 5393.9 (S0), 311.6 (A0) | 6197.8, 3122.0 | 13.0 %, 90.0 % |
| Sumit, Al | 100 | 954.2 (A0), 5393.2 (S0) | 3122.0, 6197.8 | 69.4 %, 13.0 % |
| Sumit, Al | 1000 | 2326.6 (A0), 5308.6 (S0) | 3122.0, 6197.8 | 25.5 %, 14.3 % |
| Sumit, Al, `l/h` to 0.2 | 10 / 100 / 1000 | 321.0 / 983.7 / 2460.3 (A0) | 3122.0 | 89.7 / 68.5 / 21.2 % |
| Sumit, Al, `l/h` to 0.2 | 100 / 1000 | 5393.4 / 5348.4 (S0) | 6197.8 | 13.0 / 13.7 % |
| Sumit, ZnO coupled | 100 / 1000 | 2181.9, 943.5 (A0 baseline) | 2732.2 | 20.1 %, 65.5 % |
| Sumit, ZnO, closure | 1000 | 2300.7 to 1825.0 | 2732.2 | 15.8 % to 33.2 % |
| Sumit, ZnO, piezo | 10 / 100 | 5509.7, 5509.2 | 6076.1 | 9.3 % |
| Sumit, ZnO, screened | 100 | 5273.7 | 6076.1 | 13.2 % |
| Neha | 1000 | 2216.6, 2222.0 (A0) | 2897.0 | 23.5 %, 23.3 % |
| Neha | 1000 | 5070.5 to 5117.4 (S0) | 5428.1 | 6.6 % to 5.7 % |
| Anu | 1000 | 2277.1 (A0) | 2771.1 | 17.8 % |
| Anu | 100 | 5411.8, 5529.6, 5530.5 (S0) | 6280.2 | 13.8 %, 12.0 %, 11.9 % |

Nothing above is within 0.5 per cent of a bulk speed, and the closest call is the Neha S0 reference
at 5.7 per cent. So every dip that appears in the reports and notes is a plate mode.

Three dips in the working record do sit on a bulk speed, and all three are already out of the quoted
lists:

| paper | fd | dip (m/s) | bulk | distance | status |
|---|---|---|---|---|---|
| Neha, elastic constants of Al | 10 and 100 | 6197.8 | 6197.8 (c_L) | 0.00 % | excluded, noted as degenerate |
| Anu, elastic constants of Al | 10 and 100 | 6197.8 | 6197.8 (c_L) | 0.00 % | excluded, noted as degenerate |
| Anu | 100 | 6280.6 | 6280.25 (c_L) | 0.01 % | withdrawn in round v8f |

The third is the one that cost a round: the S0 search was centred on 6300 m/s, which is the bulk
longitudinal speed of Anu's constants, and every face condition returned that same number because
the bulk zero is blind to the couplings, to the rows and to the thickness.

## The rule

A dip of the smallest singular value that lands on a bulk speed is not a mode. Before quoting any
dip, compute the bulk speeds of the same constants at the same frequency and reject anything within
half a per cent. When a dip is in doubt, perturb `k` by a fraction of a per cent at fixed `omega`:
a plate mode moves with its own dispersion, a degenerate bulk zero stays glued to `c_L` or `c_T` and
disappears as soon as the frequency is changed, because the zero exists only where a root passes
through `eta = 0`. Equivalently, look at the null vector: for the degenerate zero the amplitude of
every partial wave is carried by the `eta = 0` root, so the mode shape has no `z`-dependence at all.
