# Task 2b — single-coupling limits, first block (pizooelectric and the screening curve)

`h = 5e-4` m, Sumit constants, both lengths zero, ten-row assembly, smallest singular value on a
5 m/s grid. Values in m/s.

## Piezoelectric limit, carriers off

The earlier figure of 5368 m/s was not a fault. With the carrier terms left on, the mobile charge
screens the piezoelectric stiffening; the reviewer's reading is confirmed. Setting `q = 0`, all
thermal couplings off (`bth = Pith = Eg = 0`), `p3 = 0` and `b1 = b3 = 0`:

| case | fd = 10 | fd = 100 | closed form |
|---|---|---|---|
| piezoelectric, `e` on, faces open | 5509.7 | 5509.2 | 5509.57 |
| elastic baseline, `e = 0` | 5259.5 | 5258.8 | 5259.13 |

The open-circuit thin-plate speed is reproduced to 0.06 per cent at `fd = 10` and 0.007 per cent at
`fd = 100`, and the short-circuit value to 0.007 and 0.005 per cent. Pass, and the plane-stress
reduction of the masters is right.

## Screening curve, carriers on

Piezoelectric coupling live, thermal couplings off, `q` and `n0` as in the paper, `fd = 100`:

| n0 (m^-3) | S0 (m/s) | depth, median to dip |
|---|---|---|
| 0 | 5509.2 | 96 |
| 1e16 | 5509.2 | 89 |
| 1e18 | 5504.9 | 1099 |
| 1e19 | 5474.7 | 224 |
| 1e20 | 5355.1 | 325 |
| 1e21 | 5273.7 | 104 |

Monotone, and it ends where it should: at `n0 = 1e21` the speed is 5273.7 against the
short-circuit 5259.1, i.e. the stiffening is screened away. The crossover sits between `1e18` and
`1e19`; below it the charge has no time to follow the wave, above it the field is shorted. This is
the curve the Sumit paper should show.

## Fourier damping — attempted, not yet a test

A bulk longitudinal wave at `eta = 0` with the thermal coupling live (`b1 = b3 = 4e5`,
`bth = 1e18`, `T0 = 300`, `kth = 60`, `cp = 2.8e6`, `tauR = 1 ns`), carriers and piezoelectricity
off, complex `k` from a Newton solve started at `omega/c_L`, `c_L = 6076.1` m/s:

```
f = 1e5     kr 103.4    ki 4.8e-17   ki/kr 4.6e-19
f = 1e7     kr 1.034e4  ki 4.8e-13   ki/kr 4.6e-17
f = 1e8     kr 1.034e5  ki 4.8e-11   ki/kr 4.6e-16
f = 1.59e8  kr 1.644e5  ki 1.2e-10   ki/kr 7.3e-16
f = 1e10    kr 1.034e7  ki 3.4e-7    ki/kr 3.3e-14
```

The attenuation is five to seven orders below anything a thermoelastic coupling with
`Delta_E` of order `1e-9` to `1e-3` would give, and it does not follow the
`omega tau/(1 + (omega tau)^2)` shape: the peak of that shape sits at `f = 1/(2 pi tauR) = 159` MHz
and the numbers above climb straight through it. So the default constants are not mutually
consistent for this test — `bth = 1e18` cannot be in SI if `b1 = b3 = 4e5` is. The test waits
until the two are put on one footing. Nothing is claimed here except that.

## Parity

Computed on the five-by-five at `k = 3e5`, `omega = 2 pi 1e8`, `eta = 1e4 + 2e3 i`, all thirty-two
diagonal sign vectors tested against `M(-eta) = S M(eta) S`.

| paper | field order | patterns |
|---|---|---|
| Sumit | ux, uz, phi, psi, theta | none |
| Sumit, `bth = Pith = Eg = 0` | same | `(+,-,-,-,+)` and its negative |
| Neha | ux, uz, w, phi, theta | `(+,-,-,-,+)` and its negative |
| Anu | ux, uz, phi, psi, theta | `(+,-,-,-,+)` and its negative |

This is the wording the masters carry: for generic values of the other constants, Sumit has the
pair exactly when `beta_th = Pi_th = E_g = 0`; Neha and Anu have it always.

## Not yet done

Hutson–White peak, phason limits (Neha) and magnetoelastic limits (Anu). They come after the
constants are put on one footing, because the same inconsistency blocks them.
