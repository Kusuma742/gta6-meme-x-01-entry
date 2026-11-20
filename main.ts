// GTA 6 meme entry for make.fun bounty gta6-meme-x-01 ("Post a GTA 6 meme on X").
// Entry program (Node 22, standard library only): copies POST.json from the
// repository root to /output, where the grader reads it. POST.json names the
// X post carrying the meme (meme.png) and its caption.
//
// The meme is meme.png (1200x675): a "5-star wanted" poster built from a
// Solmar City gameplay screenshot and make.fun's press-kit ghost mark
// (see build_meme.py for how it was made).
//
// Run: MAKEFUN_OUTPUT_DIR=out node main.ts
// (Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.)

import { copyFileSync, existsSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = fileURLToPath(new URL('.', import.meta.url));
const out = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const post = join(here, 'POST.json');

if (!existsSync(post)) {
  throw new Error(
    'POST.json not found: post the meme on X first, then save its URL as POST.json at the repo root.',
  );
}

mkdirSync(out, { recursive: true });
copyFileSync(post, join(out, 'POST.json'));
