"""v8: independent builders of M(eta), the boundary row functions and B, from the
constitutive laws of the three v8 masters.  Symbols follow the v8 tex.
mpmath only.
"""
import mpmath as mp
mp.mp.dps = 50
I = mp.mpc(0, 1)

# ----------------------------------------------------------------- constants
def const_sumit():
    return dict(
        c11=mp.mpf('209.7e9'), c13=mp.mpf('105.4e9'), c33=mp.mpf('211.2e9'), c44=mp.mpf('42.4e9'),
        e31=mp.mpf('-0.57'), e33=mp.mpf('1.32'), e15=mp.mpf('-0.48'),
        eps11=mp.mpf('8.54')*mp.mpf('8.8541878128e-12'), eps33=mp.mpf('10.2')*mp.mpf('8.8541878128e-12'),
        p3=mp.mpf('-1e-5'), b1=mp.mpf('4.0e5'), b3=mp.mpf('4.0e5'),
        rho=mp.mpf('5680'), lg=mp.mpf('1e-8'), lnl=mp.mpf('1e-8'),
        q=mp.mpf('1.602176634e-19'), bn=mp.mpf('0.01'), n0=mp.mpf('1e20'), Dn=mp.mpf('1e-3'),
        vd=mp.mpf('0'), bth=mp.mpf('1e18'), tauR=mp.mpf('1e-9'),
        T0=mp.mpf('300'), cp=mp.mpf('2.8e6'), kth=mp.mpf('60'), tauq=mp.mpf('1e-11'),
        Pith=mp.mpf('-1e-3'), Eg=mp.mpf('1e-19'))

def const_neha():
    return dict(
        C11=mp.mpf('165e9'), C13=mp.mpf('66e9'), C33=mp.mpf('185e9'), C44=mp.mpf('47e9'),
        K1=mp.mpf('1.2e9'), K2=mp.mpf('0.9e9'),
        R1=mp.mpf('1.5e9'), R2=mp.mpf('-1.0e9'), R3=mp.mpf('0.4e9'),
        e31=mp.mpf('-0.5'), e33=mp.mpf('1.3'), e15=mp.mpf('-0.4'),
        eps11=mp.mpf('9e-11'), eps33=mp.mpf('1.1e-10'), p3=mp.mpf('-1e-5'),
        b1=mp.mpf('3e5'), b3=mp.mpf('3e5'), bw=mp.mpf('5e5'),
        rho=mp.mpf('5600'), rhop=mp.mpf('1.2'), gam=mp.mpf('1e8'),
        lg=mp.mpf('1e-8'), lnl=mp.mpf('1e-8'),
        T0=mp.mpf('300'), cp=mp.mpf('2.6e6'), kth=mp.mpf('50'), tauq=mp.mpf('1e-11'))

def const_anu():
    return dict(
        c11=mp.mpf('226e9'), c13=mp.mpf('112e9'), c33=mp.mpf('216e9'), c44=mp.mpf('44e9'),
        e31=mp.mpf('-2.2'), e33=mp.mpf('9.3'), e15=mp.mpf('5.8'),
        q31=mp.mpf('290'), q33=mp.mpf('350'), q15=mp.mpf('190'),
        eps11=mp.mpf('5.64e-9'), eps33=mp.mpf('6.35e-9'),
        mu11=mp.mpf('2.97e-4'), mu33=mp.mpf('1.57e-4'),
        al11=mp.mpf('1.6e-9'), al33=mp.mpf('2.7e-9'),
        b1=mp.mpf('3.1e5'), b3=mp.mpf('3.1e5'), p3=mp.mpf('-1e-5'), lam=mp.mpf('2e-3'),
        rho=mp.mpf('5730'), lg=mp.mpf('1e-8'), lnl=mp.mpf('1e-8'),
        T0=mp.mpf('300'), cp=mp.mpf('2.5e6'), kth=mp.mpf('6'), tauq=mp.mpf('1e-11'))

# ----------------------------------------------------------------- builders
def rcp_of(P):
    return P['rho']*P['cp']

def N_of(eta, k, P):
    return 1 - P['lnl']**2*(eta**2 - k**2)

def G_of(eta, k, P):
    return 1 - P['lg']**2*(eta**2 - k**2)

def build_M_sumit(eta, k, w, P):
    """5x5 from the v8 constitutive laws, rows: momentum x, momentum z, Gauss, carriers, heat."""
    L = eta**2 - k**2
    N, G = N_of(eta, k, P), G_of(eta, k, P)
    sxx = [G*I*k*P['c11'], G*eta*P['c13'], eta*P['e31'], 0, -P['b1']]
    szz = [G*I*k*P['c13'], G*eta*P['c33'], eta*P['e33'], 0, -P['b3']]
    sxz = [G*P['c44']*eta, G*P['c44']*I*k, I*k*P['e15'], 0, 0]
    Dx  = [P['e15']*eta, P['e15']*I*k, -I*k*P['eps11'], 0, 0]
    Dz  = [I*k*P['e31'], eta*P['e33'], -eta*P['eps33'], 0, P['p3']]
    M = mp.matrix(5, 5)
    for j in range(5):
        M[0, j] = -(I*k*sxx[j] + eta*sxz[j])
        M[1, j] = -(I*k*sxz[j] + eta*szz[j])
        M[2, j] =  (I*k*Dx[j] + eta*Dz[j])
    M[0, 0] += -N*P['rho']*w**2
    M[1, 1] += -N*P['rho']*w**2
    M[2, 3] += P['q']
    M[3, 2] = P['bn']*P['n0']*L
    M[3, 3] = -I*w - P['Dn']*L - I*k*P['vd'] + 1/P['tauR']
    M[3, 4] = -P['bth']*L
    f = 1 - I*w*P['tauq']
    M[4, 0] = f*P['T0']*w*k*P['b1']
    M[4, 1] = -I*w*f*P['T0']*P['b3']*eta
    M[4, 2] = I*w*f*P['T0']*P['p3']*eta
    M[4, 3] = f*(-I*w*P['q']*P['Pith'] + P['Eg']/P['tauR'])
    M[4, 4] = -I*w*f*rcp_of(P) - P['kth']*L
    return M

def build_M_neha(eta, k, w, P):
    """5x5, rows: momentum x, momentum z, phason, Gauss, heat. v8 names: K1 axial, K2 transverse."""
    L = eta**2 - k**2
    N, G = N_of(eta, k, P), G_of(eta, k, P)
    W1, W2 = eta, I*k                      # w_zz and w_zx per unit amplitude of W
    sxx = [G*I*k*P['C11'], G*eta*P['C13'], P['R1']*W1, eta*P['e31'], -P['b1']]
    szz = [G*I*k*P['C13'], G*eta*P['C33'], P['R2']*W1, eta*P['e33'], -P['b3']]
    sxz = [G*P['C44']*eta, G*P['C44']*I*k, P['R3']*W2, I*k*P['e15'], 0]
    Hzz = [P['R1']*I*k, P['R2']*eta, P['K1']*W1, 0, -P['bw']]
    Hzx = [P['R3']*eta, P['R3']*I*k, P['K2']*W2, 0, 0]
    Dx  = [P['e15']*eta, P['e15']*I*k, 0, -I*k*P['eps11'], 0]
    Dz  = [I*k*P['e31'], eta*P['e33'], 0, -eta*P['eps33'], P['p3']]
    M = mp.matrix(5, 5)
    for j in range(5):
        M[0, j] = -(I*k*sxx[j] + eta*sxz[j])
        M[1, j] = -(I*k*sxz[j] + eta*szz[j])
        M[2, j] =  (I*k*Hzx[j] + eta*Hzz[j])
        M[3, j] =  (I*k*Dx[j] + eta*Dz[j])
    M[0, 0] += -N*P['rho']*w**2
    M[1, 1] += -N*P['rho']*w**2
    M[2, 2] += P['rhop']*w**2 + I*P['gam']*w
    f = 1 - I*w*P['tauq']
    M[4, 0] = f*P['T0']*w*k*P['b1']
    M[4, 1] = -I*w*f*P['T0']*P['b3']*eta
    M[4, 2] = -I*w*f*P['T0']*P['bw']*eta
    M[4, 3] = I*w*f*P['T0']*P['p3']*eta
    M[4, 4] = -I*w*f*rcp_of(P) - P['kth']*L
    return M

def build_M_anu(eta, k, w, P):
    """5x5, rows: momentum x, momentum z, Gauss E, Gauss B, heat."""
    L = eta**2 - k**2
    N, G = N_of(eta, k, P), G_of(eta, k, P)
    sxx = [G*I*k*P['c11'], G*eta*P['c13'], eta*P['e31'], eta*P['q31'], -P['b1']]
    szz = [G*I*k*P['c13'], G*eta*P['c33'], eta*P['e33'], eta*P['q33'], -P['b3']]
    sxz = [G*P['c44']*eta, G*P['c44']*I*k, I*k*P['e15'], I*k*P['q15'], 0]
    Dx  = [P['e15']*eta, P['e15']*I*k, -I*k*P['eps11'], -I*k*P['al11'], 0]
    Dz  = [I*k*P['e31'], eta*P['e33'], -eta*P['eps33'], -eta*P['al33'], P['p3']]
    Bx  = [P['q15']*eta, P['q15']*I*k, -I*k*P['al11'], -I*k*P['mu11'], 0]
    Bz  = [I*k*P['q31'], eta*P['q33'], -eta*P['al33'], -eta*P['mu33'], P['lam']]
    M = mp.matrix(5, 5)
    for j in range(5):
        M[0, j] = -(I*k*sxx[j] + eta*sxz[j])
        M[1, j] = -(I*k*sxz[j] + eta*szz[j])
        M[2, j] =  (I*k*Dx[j] + eta*Dz[j])
        M[3, j] =  (I*k*Bx[j] + eta*Bz[j])
    M[0, 0] += -N*P['rho']*w**2
    M[1, 1] += -N*P['rho']*w**2
    f = 1 - I*w*P['tauq']
    M[4, 0] = f*P['T0']*w*k*P['b1']
    M[4, 1] = -I*w*f*P['T0']*P['b3']*eta
    M[4, 2] = I*w*f*P['T0']*P['p3']*eta
    M[4, 3] = I*w*f*P['T0']*P['lam']*eta
    M[4, 4] = -I*w*f*rcp_of(P) - P['kth']*L
    return M

BUILDERS = dict(Sumit=build_M_sumit, Neha=build_M_neha, Anu=build_M_anu)
CONSTS   = dict(Sumit=const_sumit,   Neha=const_neha,   Anu=const_anu)
