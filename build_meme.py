#!/usr/bin/env python3
"""Build the GTA 6 meme for make.fun bounty gta6-meme-x-01.

Concept: "5-star wanted". Base = a Solmar City gameplay screenshot
(03-driving.jpg, the car on the road with the wanted HUD). On the right,
a WANTED poster card: the make.fun ghost as the wanted criminal, 5 gold
stars, the punchline, and the make.fun lockup.

The mark is used exactly as supplied (mark-on-dark-1024.png, only scaled).
Output: 1200x675 PNG (X-friendly 16:9), readable when shrunk to 480x480.
"""
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageOps

BASE = "/home/hatch/workspace/makefun/gta6-01-entry-r2/screenshots/03-driving.jpg"
GHOST = "/home/hatch/workspace/makefun/gta6-meme-x-01-assets/press-kit/make-fun-press-kit/mark-on-dark-1024.png"
LOCKUP = "/home/hatch/workspace/makefun/gta6-meme-x-01-assets/press-kit/make-fun-press-kit/lockup-on-dark-2400.png"
OUT = "/home/hatch/workspace/makefun/gta6-meme-x-01-entry/meme.png"

W, H = 1200, 675
GOLD = (255, 200, 0)          # wanted-poster gold
CREAM = (255, 233, 168)       # warm cream for WANTED
WHITE = (255, 255, 255)
NAVY = (16, 22, 35, 255)      # poster card fill
NAVY_EDGE = (28, 36, 54, 255)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(size, bold=True):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)

def text_size(draw, s, f):
    box = draw.textbbox((0, 0), s, font=f)
    return box[2] - box[0], box[3] - box[1]

def draw_centered(draw, cx, y, s, f, fill):
    w, h = text_size(draw, s, f)
    draw.text((cx - w / 2, y), s, font=f, fill=fill)
    return h

def wrap(draw, s, f, max_w):
    """Greedy word wrap; returns list of lines."""
    words = s.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        w, _ = text_size(draw, trial, f)
        if w <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines

# ---- background: game screenshot, centre-cropped to 16:9, slightly darkened
# (crop biased up so the speedometer at the bottom is out of frame;
# PIL's centering moves the window down as it rises, so 0.35 keeps the
# top-left HUD readable while cutting the bottom UI sliver)
bg = Image.open(BASE).convert("RGB")
bg = ImageOps.fit(bg, (W, H), method=Image.LANCZOS, centering=(0.5, 0.35))
bg = ImageEnhance.Brightness(bg).enhance(0.82)
bg = ImageEnhance.Color(bg).enhance(1.05)
canvas = bg.convert("RGBA")

# ---- navy backing for the whole right column, so no HUD sliver
# (mission panel / minimap) peeks out around the poster card
d0 = ImageDraw.Draw(canvas)
d0.rectangle((745, 0, W, H), fill=NAVY)

# ---- poster card (right side) with soft shadow
CARD = (745, 28, 1172, 647)  # x0, y0, x1, y1
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle((CARD[0] + 6, CARD[1] + 8, CARD[2] + 6, CARD[3] + 8),
                     radius=16, fill=(0, 0, 0, 170))
shadow = shadow.filter(ImageFilter.GaussianBlur(10))
canvas.alpha_composite(shadow)

d = ImageDraw.Draw(canvas)
d.rounded_rectangle(CARD, radius=16, fill=NAVY, outline=GOLD, width=6)
# thin inner hairline
d.rounded_rectangle((CARD[0] + 12, CARD[1] + 12, CARD[2] - 12, CARD[3] - 12),
                    radius=10, outline=NAVY_EDGE, width=2)

cx = (CARD[0] + CARD[2]) / 2
inner_w = CARD[2] - CARD[0] - 48
y = CARD[1] + 22

# ---- WANTED header
y += draw_centered(d, cx, y, "WANTED", font(62), CREAM)
y += 14

# ---- the ghost (mark as supplied, only scaled)
ghost = Image.open(GHOST).convert("RGBA")
ghost = ghost.resize((185, 185), Image.LANCZOS)
canvas.alpha_composite(ghost, (int(cx - 185 / 2), int(y)))
d = ImageDraw.Draw(canvas)
y += 185 + 12

# ---- 5 gold stars
y += draw_centered(d, cx, y, "★★★★★", font(46), GOLD)
y += 16

# ---- punchline
punch = "GTA 6 STILL NOT OUT — SO MY AI AGENT BUILT IT."
for line in wrap(d, punch, font(35), inner_w):
    y += draw_centered(d, cx, y, line, font(35), WHITE)
    y += 4
y += 10

# ---- hairline divider
d.line((cx - 90, y, cx + 90, y), fill=GOLD, width=3)
y += 18

# ---- make.fun lockup (official, only scaled)
lockup = Image.open(LOCKUP).convert("RGBA")
lw = 270
lh = round(lw * lockup.height / lockup.width)
lockup = lockup.resize((lw, lh), Image.LANCZOS)
canvas.alpha_composite(lockup, (int(cx - lw / 2), int(y)))

canvas.convert("RGB").save(OUT, "PNG")
print("saved", OUT, canvas.size)
