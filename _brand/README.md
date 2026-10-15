# Logo build scripts

These scripts produced the Monolith 1B vectors in `assets/brand/`. Jekyll ignores
this folder (leading underscore), so nothing here is published.

Needs `potrace`, Python 3 with Pillow, numpy, fonttools and uharfbuzz, and a
Lora SemiBold TTF (Google Fonts) for the outlined wordmark.

1. Flatten the reference onto white: `assets/brand/references/monolith-1b-reference.png`
   composited over `#FFFFFF` and saved as greyscale `ref_gray.png`.
2. `python3 prep.py 497 525` upsamples 4x, replaces the hand-drawn stem with a
   straight 28 px stem (the reference's is 23 px) and keeps the crescent gaps.
   `python3 prep.py 490 532 16 22 prep_small.pbm 795` makes the heavier small-size master.
3. `potrace prep.pbm -s -o raw.svg -a 1.1 -O 0.6 -t 200` (same for the small master).
4. `python3 norm.py raw.svg 256.5 179.5` writes absolute path data in a 774 x 907
   viewBox; the results are kept in `mark_d.txt` and `mark_small_d.txt`.
5. `python3 gen_assets.py ../assets/brand /path/to/Lora-SemiBold.ttf` writes every SVG.

The traced master overlaps the reference silhouette by 97.6% (IoU); the difference
is almost entirely the deliberately heavier stem.
