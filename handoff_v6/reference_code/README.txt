Reference code for Sumit's plate matrix (Claude, 30 Oct 2026). Use as a method reference, not as truth.
sm.py     numeric M(eta) (5x5), parameters dict P0 (placeholder constants for code testing only)
roots3.py roots of det M(eta)=0 with mpmath (80 digits), null vectors from the adjugate in mpmath
plate.py  boundary rows b_r, face matrix B (14x14 or 10x10), column scaling exp(-|Re eta| h)
Tests that passed: Rayleigh-Lamb (isotropic, couplings off) to 1e-6; open-circuit S0; bulk thermoelastic
damping; Hutson-White peak; direction of NSGT shifts. Needs: numpy scipy mpmath.
