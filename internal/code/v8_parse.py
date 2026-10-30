"""Parse M_{ij} and b_i definitions out of the v8 masters and evaluate them.
LaTeX fragments become Python expressions evaluated with mpmath, so the comparison
against the independent builders of v8_model.py is entry by entry.
"""
import re
import mpmath as mp
mp.mp.dps = 50
I = mp.mpc(0, 1)

MACROS = [
    (r'\\bigl|\\bigr|\\Bigl|\\Bigr|\\biggl|\\biggr|\\Biggl|\\Biggr|\\big|\\Big|\\left|\\right', ' '),
    (r'\\,|\\;|\\!|\\quad|\\qquad|\\nonumber|\\hat|\\mathrm|\\rm', ' '),
    (r'\\ ', ' '),
]

# multi-token subscripts first
SPECIAL = [
    (r'\\beta_\{\\rm th\}', 'bth'), (r'\\beta_\{\\mathrm\{th\}\}', 'bth'),
    (r'\\Pi_\{\\rm th\}', 'Pith'), (r'\\Pi_\{\\mathrm\{th\}\}', 'Pith'),
    (r'k_\{\\rm th\}', 'kth'), (r'k_\{\\mathrm\{th\}\}', 'kth'),
    (r'l_\{\\rm nl\}', 'lnl'), (r'l_\{\\mathrm\{nl\}\}', 'lnl'),
    (r'\\beta\^\{?w\}?', 'bw'),
    (r'\\Delta n', 'nu'),
    (r'\\hat\\sigma_\{zz\}', 'sigzz'), (r'\\hat\\sigma_\{xz\}', 'sigxz'),
    (r'\\hat D_\{?z\}?', 'Dz'), (r'\\hat H_\{?zz\}?', 'Hzz'),
]

NAMES = dict(Ncal='N', Gcal='G', ii='I', eta='eta', omega='w', rho='rho', mu='mu', alpha='al',
             lambda_='lam', gamma='gam', epsilon='eps', varepsilon='eps', varphi='Phi', Phi='Phi',
             Theta='Theta', Pi='Pith', tau='tau', beta='b', Delta='Delta', Psi='Psi', nu='nu')

GREEK = (r'\\(Ncal|Gcal|ii|eta|omega|rho|mu|alpha|lambda|gamma|epsilon|varepsilon'
         r'|varphi|Phi|Theta|Pi|tau|beta|Psi|nu)')


def _frac(s):
    for _ in range(10):
        m = re.search(r'\\frac\{([^{}]*)\}\{([^{}]*)\}', s)
        if not m:
            break
        s = s[:m.start()] + '((' + m.group(1) + ')/(' + m.group(2) + '))' + s[m.end():]
    return s


def to_python(s):
    for pat, rep in SPECIAL:
        s = re.sub(pat, ' ' + rep + ' ', s)
    for pat, rep in MACROS:
        s = re.sub(pat, rep, s)
    s = _frac(s)

    def repl(m):
        name = NAMES[m.group(1)]
        suf = m.group(2) or ''
        if suf.startswith('_'):
            return ' %s%s ' % (name, suf[1:].strip('{}'))
        if suf.startswith('^'):
            return ' %s**%s ' % (name, suf[1:].strip('{}'))
        return ' %s ' % name
    s = re.sub(GREEK + r'((?:_|\^)\{?[A-Za-z0-9]+\}?)?', repl, s)
    s = re.sub(r'([A-Za-z])_\{([A-Za-z0-9]+)\}', r'\1\2 ', s)      # c_{11} -> c11
    s = re.sub(r'([A-Za-z]+)\s*\^\{(-?[0-9]+)\}', r'\1**\2 ', s)       # k^{2} -> k**2, Nm^{-1}

    s = re.sub(r'([A-Za-z])_([A-Za-z0-9])', r'\1\2 ', s)           # X_m, R_3k, b_nn_0
    s = re.sub(r'\s*\^([0-9]+)', r'**\1 ', s)
    s = s.replace('{', ' ').replace('}', ' ').replace('[', '(').replace(']', ')')
    s = s.replace('\\cdot', '*')
    s = re.sub(r'\\[A-Za-z]+', ' UNK ', s)                          # any leftover command
    return s.strip().rstrip('.').strip()


TOK = re.compile(r'(\*\*|[A-Za-z_][A-Za-z_0-9]*|[0-9]+\.?[0-9]*(?:[eE][-+]?[0-9]+)?|[()+\-*/])')


def tokenise(s):
    out, i = [], 0
    while i < len(s):
        if s[i].isspace():
            i += 1
            continue
        m = TOK.match(s, i)
        if not m:
            raise ValueError('cannot tokenise at %r' % s[i:i + 14])
        out.append(m.group(1))
        i = m.end()
    return out


def split_identifier(name, keys):
    if name in keys:
        return [name]
    for kk in sorted(keys, key=len, reverse=True):
        if name.startswith(kk) and len(name) > len(kk):
            rest = split_identifier(name[len(kk):], keys)
            if rest is not None:
                return [kk] + rest
    return None


def insert_multiplication(toks, keys=None):
    out, prev = [], False
    for t in toks:
        starts = bool(re.match(r'[A-Za-z_0-9.(]', t))
        if prev and starts:
            out.append('*')
        out.append(t)
        prev = bool(re.match(r'[A-Za-z_0-9.)]', t))
    if keys:
        fixed = []
        for t in out:
            if re.match(r'^[A-Za-z_][A-Za-z_0-9]*$', t) and t not in keys:
                parts = split_identifier(t, keys)
                if parts:
                    fixed.append('*'.join(parts))
                    continue
            fixed.append(t)
        out = fixed
    return out


def compile_expr(latex, env=None):
    keys = set(env) if env else None
    return ''.join(insert_multiplication(tokenise(to_python(latex)), keys))


def evaluate(latex, env):
    return eval(compile_expr(latex, env), {'__builtins__': {}}, dict(env))


def _slice_rhs(text, start):
    db = dp = 0
    i = start
    while i < len(text):
        if i > start + 1 and re.match(r'M_\{\d\d\}[&]?=|b_\{?\d\}?[&]?=', text[i:]):
            return text[start:i]
        tail = text[i:i + 8]
        if tail.startswith('\\quad') or tail.startswith('\\qquad') or tail.startswith('\\nonum') \
           or tail.startswith('\\end{') or text[i:i + 2] == '\\\\' or text[i] == '$':
            return text[start:i]
        ch = text[i]
        if ch == '\\':
            i += 2
            continue
        if ch == '{':
            db += 1
        elif ch == '}':
            if db == 0:
                return text[start:i]
            db -= 1
        elif ch == '(':
            dp += 1
        elif ch == ')':
            dp -= 1
        elif ch == ',' and db == 0 and dp == 0:
            return text[start:i]
        i += 1
    return text[start:i]


DISPLAY = re.compile(r'\\begin\{(align|equation|eqnarray|aligned|gather)\*?\}.*?\\end\{\1\*?\}', re.S)


def display_spans(tex):
    spans = []
    for m in DISPLAY.finditer(tex):
        spans.append((m.start(), m.end()))
    for m in re.finditer(r'\\\[.*?\\\]', tex, re.S):
        spans.append((m.start(), m.end()))
    for m in re.finditer(r'\$\$.*?\$\$', tex, re.S):
        spans.append((m.start(), m.end()))
    return spans


def in_display(spans, pos):
    return any(a <= pos < b for a, b in spans)


def find_entries(tex, kind='M'):
    pat = re.compile(r'M_\{(\d)(\d)\}\s*&?=\s*') if kind == 'M' \
        else re.compile(r'b_\{?(\d)\}?\s*&?=\s*')
    tex = re.sub(r'\\nonumber\s*\\\\\s*&\s*\\quad', ' ', tex)
    spans = display_spans(tex)
    out = []
    for m in pat.finditer(tex):
        label = ('M', m.group(1), m.group(2)) if kind == 'M' else ('b', m.group(1))
        labels = [label]
        end = m.end()
        while True:                                   # M_{23}=M_{32}=... chains
            m2 = pat.match(tex, end)
            if not m2:
                break
            labels.append(('M', m2.group(1), m2.group(2)) if kind == 'M' else ('b', m2.group(1)))
            end = m2.end()
        rhs = _slice_rhs(tex, end).strip().rstrip('\\').strip()
        if rhs:
            disp = in_display(spans, m.start())
            for lb in labels:
                out.append((lb, rhs, tex[:m.start()].count('\n') + 1, disp))
    return out
