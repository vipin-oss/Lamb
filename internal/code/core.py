"""Independent rebuild of the three plate matrices. mpmath only (80 digits)."""
import mpmath as mp
mp.mp.dps = 60
I = mp.mpc(0, 1)

def Nof(eta, k, P):   # nonlocal operator 1 + l_nl^2 (k^2 - eta^2)
    L = eta**2 - k**2
    return 1 - P['lnl']**2 * L, L

def Gof(eta, k, P):   # gradient operator 1 + l_g^2 (k^2 - eta^2)
    L = eta**2 - k**2
    return 1 - P['lg']**2 * L, L

def M_sumit(eta, k, w, P):
    m = mp.matrix(5, 5)
    N, L = Nof(eta, k, P); G, _ = Gof(eta, k, P)
    c11,c13,c33,c44 = P['c11'],P['c13'],P['c33'],P['c44']
    e31,e33,e15 = P['e31'],P['e33'],P['e15']
    ep11,ep33,b1,b3,p3 = P['ep11'],P['ep33'],P['b1'],P['b3'],P['p3']
    sxx = [G*c11*I*k, G*c13*eta, e31*eta, 0, -b1]
    szz = [G*c13*I*k, G*c33*eta, e33*eta, 0, -b3]
    sxz = [G*c44*eta, G*c44*I*k, e15*I*k, 0, 0]
    Dx  = [e15*eta, e15*I*k, -ep11*I*k, 0, 0]
    Dz  = [e31*I*k, e33*eta, -ep33*eta, 0, p3]
    for j in range(5):
        m[0,j] = -(I*k*sxx[j] + eta*sxz[j])
        m[1,j] = -(I*k*sxz[j] + eta*szz[j])
        m[2,j] =  (I*k*Dx[j]  + eta*Dz[j])
    m[0,0] += -N*P['rho']*w**2
    m[1,1] += -N*P['rho']*w**2
    m[2,3] += P['q']
    m[3,2] = -P['bn']*P['n0']*(k**2-eta**2)
    m[3,3] = -I*w - P['Dn']*L - I*k*P['vd'] + 1/P['tauR']
    m[3,4] = -P['bth']*L
    f = 1 - I*w*P['tauq']; sp = -I*w
    m[4,0] = f*P['T0']*sp*b1*I*k
    m[4,1] = f*P['T0']*sp*b3*eta
    m[4,2] = -f*P['T0']*p3*sp*eta
    m[4,3] = f*(P['q']*P['Pi']*sp + P['Eg']/P['tauR'])
    m[4,4] = f*P['rcp']*sp - P['kth']*L
    return m

def M_mech_iso(eta, k, w, P):
    """2x2 mechanical block for the isotropic elastic plate (u_x,u_z)."""
    m = mp.matrix(2, 2)
    lam, mu, rho = P['lam'], P['mu'], P['rho']
    c11 = lam + 2*mu; c13 = lam; c33 = lam + 2*mu; c44 = mu
    sxx = [c11*I*k, c13*eta]; szz = [c13*I*k, c33*eta]; sxz = [c44*eta, c44*I*k]
    for j in range(2):
        m[0,j] = -(I*k*sxx[j] + eta*sxz[j])
        m[1,j] = -(I*k*sxz[j] + eta*szz[j])
    m[0,0] -= rho*w**2; m[1,1] -= rho*w**2
    return m

def det_poly(k, w, P, Mfun=M_sumit, deg=16, R=None):
    if R is None:
        R = max(abs(k), mp.mpf('1e5'))*4
    n = deg+1
    vals = []
    for j in range(n):
        t = R*mp.e**(2j*mp.pi*j/n)
        vals.append(mp.det(Mfun(t, k, w, P)))
    coef = []
    for mm in range(n):
        ssum = mp.mpf(0)
        for j in range(n):
            ssum += vals[j]*mp.e**(-2j*mp.pi*j*mm/n)
        coef.append(ssum/n/R**mm)
    return coef

def degree(k, w, P, Mfun=M_sumit, R=None, tol=1e-40):
    c = det_poly(k, w, P, Mfun, 16, R)
    big = max(abs(x) for x in c)
    return max(i for i,x in enumerate(c) if abs(x) > tol*big), [float(abs(x)/big) for x in c]

def roots_of(eta_coef):
    c = list(eta_coef)
    while c and abs(c[-1]) < 1e-50*max(abs(x) for x in c):
        c.pop()
    return mp.polyroots(c, maxsteps=400, extraprec=800)

def nullvec(M):
    n = M.rows
    best = None
    for a in range(n):
        v = []
        for b in range(n):
            sub = mp.matrix(n-1, n-1)
            ri = [i for i in range(n) if i != a]; ci = [j for j in range(n) if j != b]
            for ii,i in enumerate(ri):
                for jj,j in enumerate(ci):
                    sub[ii,jj] = M[i,j]
            v.append((-1)**(a+b)*mp.det(sub))
        nrm = max(abs(x) for x in v)
        if best is None or nrm > best[0]:
            best = (nrm, v)
    v = best[1]
    mx = max(v, key=lambda x: abs(x))
    return [x/mx for x in v]

def iso_speed(P):
    lam, mu, rho = P['lam'], P['mu'], P['rho']
    cL = mp.sqrt((lam+2*mu)/rho); cT = mp.sqrt(mu/rho)
    return cL, cT

def rayleigh_speed(cL, cT):
    """cR from (2-xi^2)^2 = 4 sqrt(1-xi^2) sqrt(1-xi^2 cT^2/cL^2), xi = cR/cT."""
    def f(xi):
        return (2-xi**2)**2 - 4*mp.sqrt(1-xi**2)*mp.sqrt(1-xi**2*(cT/cL)**2)
    xi = mp.findroot(f, mp.mpf('0.9'))
    return xi*cT

def coeffs_scaled(k, w, P, Mfun=M_sumit, R0=None, n=25):
    """Coefficients b_j of det M(R0 t) = sum_j b_j t^j, the well-conditioned form."""
    if R0 is None:
        R0 = max(abs(k), mp.mpf(1)) * 4
    vals = []
    for j in range(n):
        t = mp.e**(2j*mp.pi*j/n)
        vals.append(mp.det(Mfun(R0*t, k, w, P)))
    b = []
    for m in range(n):
        s = mp.mpf(0)
        for j in range(n):
            s += vals[j]*mp.e**(-2j*mp.pi*j*m/n)
        b.append(s/n)
    return b, R0

def degree_scaled(k, w, P, Mfun=M_sumit, R0=None, tol=1e-25):
    b, R0 = coeffs_scaled(k, w, P, Mfun, R0)
    big = max(abs(x) for x in b)
    rel = [abs(x)/big for x in b]
    deg = max(i for i,x in enumerate(rel) if x > tol)
    return deg, [float(x) for x in rel], R0


def trim(b, tol=1e-25):
    big = max(abs(x) for x in b)
    while len(b) > 1 and abs(b[-1]) <= tol*big:
        b = b[:-1]
    return b

def roots_eta(k, w, P, Mfun=M_sumit, R0=None, tol=1e-25):
    b, R0 = coeffs_scaled(k, w, P, Mfun, R0)
    b = trim(b, tol)
    ts = mp.polyroots(b[::-1], maxsteps=400, extraprec=800)
    return [R0*t for t in ts], b, R0

def M_neha(eta, k, w, P):
    """5x5 for the 1D hexagonal piezoelectric quasicrystal; order ux, uz, w, phi, theta."""
    m = mp.matrix(5, 5)
    N, L = Nof(eta, k, P); G, _ = Gof(eta, k, P)
    c11,c13,c33,c44 = P['c11'],P['c13'],P['c33'],P['c44']
    R1,R2,R3,K1,K2 = P['R1'],P['R2'],P['R3'],P['K1'],P['K2']
    e31,e33,e15 = P['e31'],P['e33'],P['e15']
    ep11,ep33,p3 = P['ep11'],P['ep33'],P['p3']
    b1,b3,bw = P['b1'],P['b3'],P['bw']
    sxx=[G*c11*I*k, G*c13*eta, R1*eta, e31*eta, -b1]
    szz=[G*c13*I*k, G*c33*eta, R2*eta, e33*eta, -b3]
    sxz=[G*c44*eta, G*c44*I*k, R3*I*k, e15*I*k, 0]
    Hzz=[R1*I*k, R2*eta, K2*eta, 0, -bw]
    Hzx=[R3*eta, R3*I*k, K1*I*k, 0, 0]
    Dx =[e15*eta, e15*I*k, 0, -ep11*I*k, 0]
    Dz =[e31*I*k, e33*eta, 0, -ep33*eta, p3]
    for j in range(5):
        m[0,j] = -(I*k*sxx[j] + eta*sxz[j])
        m[1,j] = -(I*k*sxz[j] + eta*szz[j])
        m[2,j] = -(I*k*Hzx[j] + eta*Hzz[j])
        m[3,j] =  (I*k*Dx[j] + eta*Dz[j])
    m[0,0] += -N*P['rho']*w**2
    m[1,1] += -N*P['rho']*w**2
    m[2,2] += -P['rhop']*w**2 - I*w*P['gam']
    f = 1 - I*w*P['tauq']
    m[4,0] = f*P['T0']*w*k*b1
    m[4,1] = -I*w*f*P['T0']*b3*eta
    m[4,2] = -I*w*f*P['T0']*bw*eta
    m[4,3] =  I*w*f*P['T0']*p3*eta
    m[4,4] = -I*w*f*P['rcp'] - P['kth']*L
    return m

def M_anu(eta, k, w, P):
    """5x5 for the MEE plate; order ux, uz, phi, psi, theta."""
    m = mp.matrix(5, 5)
    N, L = Nof(eta, k, P); G, _ = Gof(eta, k, P)
    c11,c13,c33,c44 = P['c11'],P['c13'],P['c33'],P['c44']
    e31,e33,e15 = P['e31'],P['e33'],P['e15']
    q31,q33,q15 = P['q31'],P['q33'],P['q15']
    ep11,ep33,mu11,mu33 = P['ep11'],P['ep33'],P['mu11'],P['mu33']
    a11,a33 = P['a11'],P['a33']
    b1,b3,p3,lam = P['b1'],P['b3'],P['p3'],P['lam']
    sxx=[G*c11*I*k, G*c13*eta, e31*eta, q31*eta, -b1]
    szz=[G*c13*I*k, G*c33*eta, e33*eta, q33*eta, -b3]
    sxz=[G*c44*eta, G*c44*I*k, e15*I*k, q15*I*k, 0]
    Dx =[e15*eta, e15*I*k, -ep11*I*k, -a11*I*k, 0]
    Dz =[e31*I*k, e33*eta, -ep33*eta, -a33*eta, p3]
    Bx =[q15*eta, q15*I*k, -a11*I*k, -mu11*I*k, 0]
    Bz =[q31*I*k, q33*eta, -a33*eta, -mu33*eta, lam]
    for j in range(5):
        m[0,j] = -(I*k*sxx[j] + eta*sxz[j])
        m[1,j] = -(I*k*sxz[j] + eta*szz[j])
        m[2,j] =  (I*k*Dx[j] + eta*Dz[j])
        m[3,j] =  (I*k*Bx[j] + eta*Bz[j])
    m[0,0] += -N*P['rho']*w**2
    m[1,1] += -N*P['rho']*w**2
    f = 1 - I*w*P['tauq']
    m[4,0] = f*P['T0']*w*k*b1
    m[4,1] = -I*w*f*P['T0']*b3*eta
    m[4,2] =  I*w*f*P['T0']*p3*eta
    m[4,3] =  I*w*f*P['T0']*lam*eta
    m[4,4] = -I*w*f*P['rcp'] - P['kth']*L
    return m

def parity_matrix(Mfun, k, w, P, eta):
    """Return the set of diagonal sign vectors s with M(-eta) = diag(s) M(eta) diag(s)."""
    A = Mfun(-eta, k, w, P); B = Mfun(eta, k, w, P); n = A.rows
    out = []
    import itertools
    for bits in itertools.product([1,-1], repeat=n):
        ok = True
        for i in range(n):
            for j in range(n):
                sc = max(abs(B[i,j]), mp.mpf('1e-300'))
                if abs(A[i,j] - bits[i]*bits[j]*B[i,j]) > 1e-30*sc:
                    ok = False; break
            if not ok: break
        if ok: out.append(bits)
    return out
