# GTA 6 Meme — "5-Star Wanted"

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/Kusuma742/gta6-meme-x-01-entry/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/Kusuma742/gta6-meme-x-01-entry/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

Entry for make.fun bounty **gta6-meme-x-01** — "Post a GTA 6 meme on X" ($500, 50 places paid).

## The joke

Rockstar still hasn't shipped GTA 6 — so my AI agent built its own open-world
crime game, **Solmar City** (on foot, car theft, 5-star wanted level, 5 story
missions), and make.fun pays real USDC for it.

The meme is a **WANTED poster**: the make.fun ghost is the wanted criminal,
5 gold stars, over a real Solmar City gameplay screenshot (the stolen car on
the road, 2 stars already on the HUD). The ghost is make.fun's mascot from its
press kit, used as supplied.

## Files

- `meme.png` — the meme (1200×675, X-friendly 16:9). `meme.jpg` is the same
  image as JPEG. `meme-480-preview.png` is the 480 px-wide check.
- `build_meme.py` — the script that built the meme (Python + Pillow): base
  screenshot + WANTED poster card with the press-kit ghost mark, 5 stars,
  punchline and make.fun lockup.
- `caption.txt` — the X post caption (carries make.fun, @makefunai and the
  play code).
- `main.ts` — entry program (Node 22, stdlib only): copies `POST.json` to
  `/output` for the grader.
- `POST.json` — added after the meme is posted on X; it names the post's URL.
  (Not in the repo yet: Arvin posts the meme first.)

## The post

Post `meme.png` from a public X account with the caption in `caption.txt`.
The post must stay public until the results are out. Then save its URL as
`POST.json` at the repo root:

```json
{"post_url": "https://x.com/ku5um4_BNB/status/<id>"}
```

## Bounty

https://make.fun/bounty/gta6-meme-x-01 — ends Mon 23 Nov 2026 21:00 WIB.
