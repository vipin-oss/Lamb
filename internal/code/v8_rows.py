"""Boundary row functions of the three v8 masters, rebuilt from the conditions
(traction-free face with the surface-gradient term, double tractions, open circuit,
zero carrier flux or zero normal phason stress or zero normal magnetic induction,
adiabatic face).  Each row is a coefficient vector over the amplitudes of that paper.
"""
import sys
sys.path.insert(0, '.')
import mpmath as mp
import v8_model as VM

I = mp.mpc(0, 1)


def rows_sumit(eta, k, w, P):
    """amplitudes (X, Z, Phi, nu, Theta)"""
    L = eta**2 - k**2
    N, G = VM.N_of(eta, k, P), VM.G_of(eta, k, P)
    lg2 = P['lg']**2
    b = []
    # b1 normal traction with surface gradient
    b.append([(G*P['c13']*I*k - lg2*I*k*eta*P['c44']*eta)/N,
              (G*P['c33']*eta - lg2*I*k*eta*P['c44']*I*k)/N,
              eta*P['e33']/N, 0, -P['b3']/N])
    # b2 shear traction with surface gradient
    b.append([(G*P['c44']*eta - lg2*I*k*eta*I*k*P['c11'])/N,
              (G*P['c44']*I*k - lg2*I*k*eta*eta*P['c13'])/N,
              I*k*P['e15']/N, 0, 0])
    # b3, b4 double tractions
    b.append([lg2/N*eta*P['c44']*eta, lg2/N*eta*P['c44']*I*k, 0, 0, 0])
    b.append([lg2/N*eta*I*k*P['c13'], lg2/N*eta*eta*P['c33'], 0, 0, 0])
    # b5 open circuit D_z = 0
    b.append([I*k*P['e31'], eta*P['e33'], -eta*P['eps33'], 0, P['p3']])
    # b6 zero carrier flux
    b.append([0, 0, P['bn']*P['n0']*eta, -P['Dn']*eta, -P['bth']*eta])
    # b7 adiabatic
    b.append([0, 0, 0, 0, eta])
    return b


def rows_neha(eta, k, w, P):
    """amplitudes (X, Z, W, Phi, Theta)"""
    N, G = VM.N_of(eta, k, P), VM.G_of(eta, k, P)
    lg2 = P['lg']**2
    b = []
    b.append([(G*I*k*P['C13'] - lg2*I*k*eta*P['C44']*eta)/N,
              (G*eta*P['C33'] - lg2*I*k*eta*P['C44']*I*k)/N,
              P['R2']*eta/N, eta*P['e33']/N, -P['b3']/N])
    b.append([(G*P['C44']*eta - lg2*I*k*eta*I*k*P['C11'])/N,
              (G*P['C44']*I*k - lg2*I*k*eta*eta*P['C13'])/N,
              P['R3']*I*k/N, I*k*P['e15']/N, 0])
    b.append([lg2/N*eta*P['C44']*eta, lg2/N*eta*P['C44']*I*k, 0, 0, 0])
    b.append([lg2/N*eta*I*k*P['C13'], lg2/N*eta*eta*P['C33'], 0, 0, 0])
    b.append([I*k*P['e31'], eta*P['e33'], 0, -eta*P['eps33'], P['p3']])
    b.append([P['R1']*I*k, P['R2']*eta, P['K1']*eta, 0, -P['bw']])
    b.append([0, 0, 0, 0, eta])
    return b


def rows_anu(eta, k, w, P):
    """amplitudes (X, Z, Phi, Psi, Theta)"""
    N, G = VM.N_of(eta, k, P), VM.G_of(eta, k, P)
    lg2 = P['lg']**2
    b = []
    b.append([(G*I*k*P['c13'] - lg2*I*k*eta*P['c44']*eta)/N,
              (G*eta*P['c33'] - lg2*I*k*eta*P['c44']*I*k)/N,
              eta*P['e33']/N, eta*P['q33']/N, -P['b3']/N])
    b.append([(G*P['c44']*eta - lg2*I*k*eta*I*k*P['c11'])/N,
              (G*P['c44']*I*k - lg2*I*k*eta*eta*P['c13'])/N,
              I*k*P['e15']/N, I*k*P['q15']/N, 0])
    b.append([lg2/N*eta*P['c44']*eta, lg2/N*eta*P['c44']*I*k, 0, 0, 0])
    b.append([lg2/N*eta*I*k*P['c13'], lg2/N*eta*eta*P['c33'], 0, 0, 0])
    b.append([I*k*P['e31'], eta*P['e33'], -eta*P['eps33'], -eta*P['al33'], P['p3']])
    b.append([I*k*P['q31'], eta*P['q33'], -eta*P['al33'], -eta*P['mu33'], P['lam']])
    b.append([0, 0, 0, 0, eta])
    return b


ROWS = dict(Sumit=rows_sumit, Neha=rows_neha, Anu=rows_anu)

# symbols in the tex that stand for a whole constitutive expression
def hat_values(sch, eta, k, w, P, amp):
    X, Z, A3, A4, Th = amp
    if sch == 'Sumit':
        Nu, G = VM.N_of(eta, k, P), VM.G_of(eta, k, P)
        sigzz = G*(P['c13']*I*k*X + P['c33']*eta*Z) + eta*P['e33']*A3 - P['b3']*Th
        sigxz = G*P['c44']*(eta*X + I*k*Z) + I*k*P['e15']*A3
        return dict(sigzz=sigzz, sigxz=sigxz)
    if sch == 'Neha':
        Nu, G = VM.N_of(eta, k, P), VM.G_of(eta, k, P)
        sigzz = G*(P['C13']*I*k*X + P['C33']*eta*Z) + P['R2']*eta*A3 + eta*P['e33']*A4 - P['b3']*Th
        sigxz = G*P['C44']*(eta*X + I*k*Z) + P['R3']*I*k*A3 + I*k*P['e15']*A4
        return dict(sigzz=sigzz, sigxz=sigxz)
    Nu, G = VM.N_of(eta, k, P), VM.G_of(eta, k, P)
    sigzz = G*(P['c13']*I*k*X + P['c33']*eta*Z) + eta*P['e33']*A3 + eta*P['q33']*A4 - P['b3']*Th
    sigxz = G*P['c44']*(eta*X + I*k*Z) + I*k*P['e15']*A3 + I*k*P['q15']*A4
    return dict(sigzz=sigzz, sigxz=sigxz)
