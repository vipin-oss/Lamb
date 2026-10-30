# Status, 30 October 2026

- Neha S0 against the phason-coupling-off reference (5117.4 m/s): 5070.5 at gamma = 1e2 to 1e8, then
  5107.5, 5113.2, 5114.0 at 1e10, 1e12, 1e14 — the overdamped limit returns the reference to 0.08
  per cent. 2 rho_p omega = 1.508e7 at this fd, so 1e12 is 6.6e4 times overdamped.
- Anu: the 6280 m/s dip was the bulk c_L degeneracy, not S0. The plate mode is at 5411.8 m/s.
- Anu S0 at fd = 100: elastic 5411.8, electric only 5529.6, magnetic only 5413.2 open / 5411.8
  closed, both 5530.5 / 5529.6. Open minus closed: magnetic +1.4 m/s, as 4.45e-4 implies.
- The closed-face fault was mine: rows[6] (adiabatic) was overwritten instead of rows[5] (B_z = 0).
  Fixed; the closed run now returns the elastic value cleanly.
- arXiv:2503.13187 logged as read to chunk 1 only, no equation numbers, not citable.
