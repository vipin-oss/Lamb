"""Structural checks on the v8 matrices: degree of det M(eta), the root census, null-vector
residuals, the entrywise parity test, and the l -> 0 continuity of the physical roots.
"""
import sys
sys.path.insert(0, '.')
import mpmath as mp
mp.mp.dps = 40
import core as CORE
import v8_model as VM

I = mp.mpc(0, 1)


def degree(sch, k, w, P):
    d, rel, R0 = CORE.degree_scaled(k, w, P, Mfun=VM.BUILDERS[sch])
    return d, rel, R0


def roots(sch, k, w, P):
    r, b, R0 = CORE.roots_eta(k, w, P, Mfun=VM.BUILDERS[sch])
    return r, b, R0


def null_residual(sch, eta, k, w, P):
    M = VM.BUILDERS[sch](eta, k, w, P)
    v = mp.matrix(CORE.nullvec(M))
    r = M*v
    nrm = max(abs(M[i, j]) for i in range(5) for j in range(5))
    return float(mp.norm(r)/(nrm*mp.norm(v)))


def main():
    k, w = mp.mpf('3e5'), 2*mp.pi*mp.mpf('1e8')
    for sch in ('Sumit', 'Neha', 'Anu'):
        P = VM.CONSTS[sch]()
        d1, rel1, _ = degree(sch, k, w, P)
        P0 = dict(P); P0['lg'] = mp.mpf(0); P0['lnl'] = mp.mpf(0)
        d0, rel0, _ = degree(sch, k, w, P0)
        Pnl = dict(P); Pnl['lnl'] = mp.mpf(0)
        dnl, _, _ = degree(sch, k, w, Pnl)
        rs, b, R0 = roots(sch, k, w, P)
        print('== %s  degree l_g>0 : %d   l_g=0 : %d   l_nl=0 : %d   roots found: %d'
              % (sch, d1, d0, dnl, len(rs)))
        # extra roots of the gradient operator: |eta| l_g
        lg = P['lg']
        extra = [z for z in rs if abs(abs(mp.re(z))*lg - 1) < mp.mpf('0.3')]
        print('   roots with |Re eta| l_g within 0.3 of 1 : %d  ->  %s'
              % (len(extra), [mp.nstr(abs(z)*lg, 4) for z in sorted(extra, key=lambda z: abs(z))]))
        res = [null_residual(sch, z, k, w, P) for z in rs[:3]]
        print('   null-vector residuals of the first roots : %s' % [('%.2e' % r) for r in res])
        # parity with all couplings on
        par = CORE.parity_matrix(VM.BUILDERS[sch], k, w, P, mp.mpf('1.13')*k)
        print('   sign vectors, all couplings : %s' % (par,))
        # Sumit: switch the thermal and Peltier couplings off
        if sch == 'Sumit':
            P2 = dict(P); P2['bth'] = mp.mpf(0); P2['Pith'] = mp.mpf(0); P2['Eg'] = mp.mpf(0)
            par2 = CORE.parity_matrix(VM.BUILDERS[sch], k, w, P2, mp.mpf('1.13')*k)
            print('   sign vectors, beta_th = Pi_th = E_g = 0 : %s' % (par2,))
            P3 = dict(P2); P3['Eg'] = P['Eg']
            par3 = CORE.parity_matrix(VM.BUILDERS[sch], k, w, P3, mp.mpf('1.13')*k)
            print('   sign vectors, beta_th = Pi_th = 0, E_g kept : %s' % (par3,))
        # l -> 0 continuity: the local problem (l_g = 0, degree 10) against a small length
        loc, _, _ = roots(sch, k, w, P0)
        small = dict(P0); small['lg'] = mp.mpf('1e-11'); small['lnl'] = mp.mpf('1e-11')
        rs2, _, _ = roots(sch, k, w, small)
        eta_x = mp.sqrt(k**2 + 1/mp.mpf('1e-11')**2)
        big = [z for z in loc if abs(z) < eta_x/10 and abs(z) < mp.mpf('1e9')]
        best = []
        for z in big:
            near = min(rs2, key=lambda y: abs(y - z))
            d = abs(near - z)/abs(z)
            if d < mp.mpf('0.5'):
                best.append(d)
        print('   local roots %d (%d far from the gradient roots), largest relative shift at l=1e-11 : %.2e'
              % (len(loc), len(best), float(max(best)) if best else -1))

if __name__ == '__main__':
    main()
