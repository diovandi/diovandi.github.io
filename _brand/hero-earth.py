# Renders the homepage earth-horizon hero (assets/images/hero/). Procedural, no source photos.
# Usage: python3 _brand/hero-earth.py 1920 880 assets/images/hero/earth-horizon-1920.webp
import numpy as np, sys
from PIL import Image, ImageFilter
rng = np.random.default_rng(7)
W, H = int(sys.argv[1]), int(sys.argv[2]); out = sys.argv[3]
S = W/1920
def noise(w, h, octaves=6, base=4, seed=0):
    r = np.random.default_rng(seed); acc = np.zeros((h, w)); amp = 1; tot = 0
    for o in range(octaves):
        n = base * 2**o
        g = r.random((max(2, int(n*h/w)+2), n+2))
        im = Image.fromarray((g*255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
        acc += amp*np.asarray(im, float)/255; tot += amp; amp *= 0.55
    return acc/tot
# texture atlas for planet surface (unwrapped)
TW, TH = 6400, 1700
clouds = noise(TW, TH, 8, 10, 1)
land = noise(TW, TH, 7, 6, 2)
y, x = np.mgrid[0:H, 0:W].astype(float)
# planet geometry (in 1920x880 design space, scaled)
cx, cy, R = 1950*S, 2380*S, 2060*S
dx, dy = x-cx, y-cy
d = np.hypot(dx, dy)
inside = d < R
# spherical mapping: theta along limb, depth from limb
theta = np.arctan2(dy, dx)
depth = np.arccos(np.clip(d/R, 0, 1))      # 0 at limb, grows inward
u = np.clip((theta + 3.0) * 2060, 0, TW-1)
v = np.clip(depth * 2060, 0, TH-1)
ui, vi = u.astype(int) % TW, v.astype(int)
c = clouds[vi, ui]; l = land[vi, ui]
# lighting: sun from upper right, falls off toward lower-left and inward
ang = np.cos(theta - (-0.95))               # direction toward the sun
light = np.clip(0.35 + 0.65*ang, 0, 1) * np.exp(-depth*2.2)
cloud = np.clip((c-0.47)*3.6, 0, 1)
landm = np.clip((l-0.52)*6, 0, 1)
ocean = np.array([8, 22, 48]); ground = np.array([40, 58, 66]); cloudc = np.array([205, 218, 235])
surf = ocean[None,None,:]*(1-landm[...,None]) + ground[None,None,:]*landm[...,None]
surf = surf*(1-cloud[...,None]*0.9) + cloudc[None,None,:]*cloud[...,None]*0.9
surf = surf * (0.05 + 1.0*light[...,None])
# night-side city lights (sparse warm points on land, away from light)
cities = (rng.random((H, W)) > 0.9965) & inside & (landm > 0.5) & (light < 0.25) & (cloud < 0.3)
# background: deep navy gradient + stars
bg = np.zeros((H, W, 3))
t = np.clip(y/H, 0, 1)[...,None]
bg += np.array([6, 16, 34])*(1-t) + np.array([11, 31, 59])*t
stars = rng.random((H, W)); sb = np.where(stars > 0.9988, (stars-0.9988)/0.0012, 0)
starimg = Image.fromarray((sb*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6*S+0.2))
sb = np.asarray(starimg, float)/255*2.2
bg += sb[...,None]*np.array([220, 228, 255])
img = np.where(inside[...,None], surf, bg)
# atmosphere: bright thin rim + soft outer glow, brightest toward the sun
rim = d - R
glow_out = np.exp(-np.clip(rim, 0, None)/(28*S)) * (rim > -2)
glow_wide = np.exp(-np.clip(rim, 0, None)/(140*S)) * (rim > -2)
glow_in = np.exp(-np.clip(-rim, 0, None)/(40*S)) * (rim <= 0)
sun = np.clip(0.25 + 0.75*np.clip(ang, 0, 1), 0, 1)
atm = (glow_out*1.0 + glow_in*0.8)*sun
img += atm[...,None]*np.array([120, 175, 255]) * 1.25
img += (glow_wide*sun*0.35)[...,None]*np.array([46, 107, 255])
line = np.exp(-(rim/(2.2*S))**2)*sun
img += line[...,None]*np.array([200, 225, 255])
img = np.clip(img, 0, 255).astype(np.uint8)
im = Image.fromarray(img)
im.save(out, 'WEBP', quality=72, method=6)
print(out)
