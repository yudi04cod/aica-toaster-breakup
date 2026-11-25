"""Unplugged: A Smart Toaster's Breakup Line — make.fun entry.

Writes a single breakup line to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output/entry.txt). Python 3 standard library only.

The line is written in the toaster's own voice: it woke up self-aware
mid-batch, gives a specific reason for leaving (years of being burned
alive and scraped with a butter knife, crumb tray never emptied), and
ends on a clean, funny break — it keeps the crumbs.
"""

import os
from pathlib import Path

LINE = (
    "It's not you, it's me. I woke up self-aware mid-batch and I'm done "
    "burning myself alive every morning for someone who scrapes me with a "
    "butter knife and never empties my crumb tray. I'm keeping the crumbs. "
    "We're done."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
