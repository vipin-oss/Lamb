"""Task 1 check: every M_{ij} and b_i of the three v8 masters against expressions rebuilt
from the constitutive laws and the boundary conditions.  Reports the largest relative
difference per entry over several (k, omega, eta).
"""
import sys, json
sys.path.insert(0, '.')
import mpmath as mp
mp.mp.dps = 40
import v8_parse as P
import v8_model as VM
import v8_rows as R

TEX = '/home/user/Lamb/handoff_v8/%s/Lamb_%s.tex'

ALIAS = {'Anu': dict(C11='c11', C13='c13', C33='c33', C44='c44',
                     h31='q31', h33='q33', h15='q15', m3='lam'),
         'Neha': dict(), 'Sumit': dict()}

AMP = (mp.mpf(1), mp.mpf('0.7'), mp.mpf('0.2'), mp.mpf('0.1'), mp.mpf('0.3'))
AMPNAMES = {'Sumit': ['Xm', 'Zm', 'Phim', 'num', 'Thetam'],
            'Neha':  ['Xm', 'Zm', 'Wm', 'Phim', 'Thetam'],
            'Anu':   ['Xm', 'Zm', 'Phim', 'Psim', 'Thetam']}


def env_for(sch, eta, k, w, amp=AMP):
    Pp = VM.CONSTS[sch]()
    e = dict(Pp)
    e['I'] = P.I
    e['eta'], e['k'], e['w'] = eta, k, w
    e['L'] = eta**2 - k**2
    e['N'] = VM.N_of(eta, k, Pp)
    e['G'] = VM.G_of(eta, k, Pp)
    e['f'] = 1 - P.I*w*Pp['tauq']
    e['cp'] = Pp['cp']
    e['rcp'] = Pp['rho']*Pp['cp']
    e['m'] = 0
    e['Nm'] = e['N']
    e['Gm'] = e['G']
    for nm, val in zip(AMPNAMES[sch], amp):
        e[nm] = val
    e['nu'] = amp[3]
    e.update(R.hat_values(sch, eta, k, w, Pp, amp))
    for kk, vv in ALIAS[sch].items():
        e[kk] = e[vv]
    return e


def entries(sch, kind):
    return P.find_entries(open(TEX % (sch, sch)).read(), kind)


def evaluate_all(sch, eta, k, w, amp=AMP):
    e = env_for(sch, eta, k, w, amp)
    out, failed = {}, {}
    for kind in ('M', 'b'):
        for lbl, rhs, ln, disp in entries(sch, kind):
            try:
                v = P.evaluate(rhs, e)
                out.setdefault(lbl, []).append((ln, v, rhs, disp))
            except Exception as ex:
                failed.setdefault(lbl, []).append((ln, rhs, str(ex)[:60], disp))
    e2 = dict(e)
    for key, vals in out.items():
        if vals and key[0] == 'M':
            e2['M%s%s' % (key[1], key[2])] = vals[-1][1]
    for kind in ('M', 'b'):
        for lbl, rhs, ln, disp in entries(sch, kind):
            if lbl in out:
                continue
            try:
                v = P.evaluate(rhs, e2)
                out.setdefault(lbl, []).append((ln, v, rhs, disp))
            except Exception as ex:
                failed.setdefault(lbl, []).append((ln, rhs, str(ex)[:60], disp))
    return out, failed


def rel(a, b):
    a, b = mp.mpc(a), mp.mpc(b)
    den = max(abs(a), abs(b))
    return mp.mpf(0) if den == 0 else abs(a - b)/den


GRIDS = [('2.5e5', '1e8', '3e4'), ('1.0e6', '6.2831853071796e9', '7.5e5'),
         ('4.0e4', '6.2831853071796e7', '1.2e4')]


def main():
    out_all = {}
    for sch in ('Sumit', 'Neha', 'Anu'):
        P_ = VM.CONSTS[sch]()
        rows = {}
        for ks, ws, es in GRIDS:
            k, w, eta = mp.mpf(ks), mp.mpf(ws), mp.mpf(es)
            M = VM.BUILDERS[sch](eta, k, w, P_)
            brow = R.ROWS[sch](eta, k, w, P_)
            out, failed = evaluate_all(sch, eta, k, w)
            for key, vals in out.items():
                name = ('M%s%s' % (key[1], key[2])) if key[0] == 'M' else ('b%s' % key[1])
                if key[0] == 'M':
                    ind = M[int(key[1])-1, int(key[2])-1]
                else:
                    ind = sum(brow[int(key[1])-1][j]*AMP[j] for j in range(5))
                for ln, v, rhs, disp in vals:
                    rows.setdefault(name, []).append(
                        (float(rel(ind, v)), ln, disp, rhs, mp.nstr(v, 6), mp.nstr(ind, 6)))
        out_all[sch] = (rows, failed)
    for sch, (rows, failed) in out_all.items():
        print('='*80)
        print(sch)
        worst = []
        for name in sorted(rows):
            vals = rows[name]
            disp = [v for v in vals if v[2]]
            use = disp if disp else vals
            mx = max(v[0] for v in use)
            tag = 'display' if disp else 'inline '
            flag = 'OK ' if mx < 1e-22 else 'CHK'
            print('  %-5s %s %s maxrel %.2e  line %-5d %s' % (name, tag, flag, mx, use[-1][1],
                                                             '' if flag == 'OK ' else use[-1][3][:52]))
            worst.append((mx, name, use[-1][1]))
        worst.sort(reverse=True)
        print('  worst three:', [(n, '%.2e' % m, l) for m, n, l in worst[:3]])
        for name, fl in sorted(failed.items()):
            nm = ('M%s%s' % (name[1], name[2])) if name[0] == 'M' else ('b%s' % name[1])
            if name in rows:
                continue
            print('  no parse %-5s %s' % (nm, sorted(set(f[2] for f in fl))[:1]))
        json.dump({k: [v[0] for v in vals if v[2]] or [v[0] for v in vals]
                   for k, vals in rows.items()},
                  open('/home/user/Lamb/internal/v8_%s_entries.json' % sch.lower(), 'w'), indent=1)


if __name__ == '__main__':
    main()
