import os, re, sys
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
FONT = sys.argv[2]
NAVY, OFFWHITE, BLACK, WHITE = '#0B1F3B', '#FAF9F6', '#000000', '#FFFFFF'
W, H = 774, 907
MARK = open(os.path.join(HERE, 'mark_d.txt')).read()
MARK_SMALL = open(os.path.join(HERE, 'mark_small_d.txt')).read()
CLEAR = round(0.2 * W)  # brand guide 2.3: clear space = 20% of symbol width

def n(v):
    s = f'{v:.1f}'
    return s[:-2] if s.endswith('.0') else s

def shift(d, dx, dy, k=1.0):
    toks = re.findall(r'[A-Za-z]|-?\d*\.?\d+', d)
    out, i, cmd = [], 0, None
    while i < len(toks):
        t = toks[i]
        if t.isalpha():
            cmd = t; out.append(t); i += 1; continue
        if cmd == 'H':
            out.append(n(float(t) * k + dx)); i += 1
        elif cmd == 'V':
            out.append(n(float(t) * k + dy)); i += 1
        else:
            x = float(toks[i]) * k + dx; y = float(toks[i + 1]) * k + dy; i += 2
            out.append(n(x) + ' ' + n(y))
        if i < len(toks) and not toks[i].isalpha():
            out.append(' ')
    return ''.join(out)

def doc(w, h, body, label='Diovandi'):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {n(w)} {n(h)}" role="img" aria-label="{label}">\n'
            f'<title>{label}</title>\n{body}\n</svg>\n')

def text_path(txt, size, x, baseline):
    blob = hb.Blob.from_file_path(FONT); face = hb.Face(blob); font = hb.Font(face)
    buf = hb.Buffer(); buf.add_str(txt); buf.guess_segment_properties()
    hb.shape(font, buf, {'kern': True, 'liga': True})
    tt = TTFont(FONT); gs = tt.getGlyphSet(); order = tt.getGlyphOrder()
    upm = tt['head'].unitsPerEm; k = size / upm
    pen = SVGPathPen(gs, ntos=lambda v: n(v)); cx = 0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        g = order[info.codepoint]
        tp = TransformPen(pen, (k, 0, 0, -k, x + (cx + pos.x_offset) * k, baseline - pos.y_offset * k))
        gs[g].draw(tp); cx += pos.x_advance
    return pen.getCommands(), cx * k, tt['OS/2'].sCapHeight * k

def write(rel, s):
    p = os.path.join(OUT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w').write(s); print(rel, len(s))

# Symbol, tight bounds (clear space is applied by the layout using it)
write('logos/primary/diovandi-mark.svg', doc(W, H, f'<path fill="{NAVY}" d="{MARK}"/>'))
write('logos/primary/diovandi-mark-small.svg', doc(W, H, f'<path fill="{NAVY}" d="{MARK_SMALL}"/>', 'Diovandi (small-size master)'))
write('logos/monochrome/diovandi-mark-black.svg', doc(W, H, f'<path fill="{BLACK}" d="{MARK}"/>'))
write('logos/monochrome/diovandi-mark-white.svg', doc(W, H, f'<path fill="{WHITE}" d="{MARK}"/>'))
write('logos/reversed/diovandi-mark-offwhite.svg', doc(W, H, f'<path fill="{OFFWHITE}" d="{MARK}"/>'))

# Square tiles with clear space
S = H + 2 * CLEAR; ox = (S - W) / 2; oy = CLEAR
tile = lambda d: shift(d, ox, oy)
write('logos/primary/diovandi-mark-tile.svg', doc(S, S, f'<rect width="{S}" height="{S}" fill="{OFFWHITE}"/>\n<path fill="{NAVY}" d="{tile(MARK)}"/>'))
write('logos/reversed/diovandi-mark-reversed.svg', doc(S, S, f'<rect width="{S}" height="{S}" fill="{NAVY}"/>\n<path fill="{OFFWHITE}" d="{tile(MARK)}"/>'))
write('logos/reversed/diovandi-mark-knockout.svg', doc(S, S, f'<path fill="{NAVY}" fill-rule="evenodd" d="M0 0H{S}V{S}H0Z{tile(MARK)}"/>'))

# Favicon / app icon: small-size master on a navy tile
F = 1000; k = 0.78 * F / H; fx = (F - W * k) / 2; fy = (F - H * k) / 2
fav = shift(MARK_SMALL, fx, fy, k)
write('logos/favicon/diovandi-favicon.svg', doc(F, F, f'<rect width="{F}" height="{F}" rx="200" fill="{NAVY}"/>\n<path fill="{OFFWHITE}" d="{fav}"/>'))
write('logos/favicon/diovandi-app-icon.svg', doc(F, F, f'<rect width="{F}" height="{F}" fill="{NAVY}"/>\n<path fill="{OFFWHITE}" d="{shift(MARK_SMALL, (F - W*0.66*F/H)/2, (F - 0.66*F)/2, 0.66*F/H)}"/>'))

# Lockups (Lora SemiBold, outlined)
cap = 0.44 * H
cap_s = 0.34 * H
probe, adv, capu = text_path('Diovandi', 100, 0, 0)
size = 100 * cap / capu
gap = 0.3 * W
tx = W + gap; base = 0.74 * H
d_txt, adv, _ = text_path('Diovandi', size, tx, base)
LW = tx + adv; LH = H
for name, mark_c, txt_c, bg in [('diovandi-horizontal', NAVY, NAVY, None), ('diovandi-horizontal-reversed', OFFWHITE, OFFWHITE, NAVY)]:
    pad = CLEAR if bg else 0
    body = (f'<rect width="{n(LW+2*pad)}" height="{n(LH+2*pad)}" fill="{bg}"/>\n' if bg else '') + \
           f'<path fill="{mark_c}" d="{shift(MARK, pad, pad)}"/>\n<path fill="{txt_c}" d="{shift(d_txt, pad, pad)}"/>'
    write(f'lockups/{name}.svg', doc(LW + 2*pad, LH + 2*pad, body))

# Stacked
gap_v = 0.14 * H
size_s = size * cap_s / cap
d_st, adv_s, _ = text_path('Diovandi', size_s, 0, 0)
SW = max(W, adv_s); mx = (SW - W) / 2; txx = (SW - adv_s) / 2
base_s = H + gap_v + cap_s
d_st, _, _ = text_path('Diovandi', size_s, txx, base_s)
SH = base_s + 0.02 * H
for name, c, bg in [('diovandi-stacked', NAVY, None), ('diovandi-stacked-reversed', OFFWHITE, NAVY)]:
    pad = CLEAR if bg else 0
    body = (f'<rect width="{n(SW+2*pad)}" height="{n(SH+2*pad)}" fill="{bg}"/>\n' if bg else '') + \
           f'<path fill="{c}" d="{shift(MARK, mx+pad, pad)}"/>\n<path fill="{c}" d="{shift(d_st, pad, pad)}"/>'
    write(f'lockups/{name}.svg', doc(SW + 2*pad, SH + 2*pad, body))
