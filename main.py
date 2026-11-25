"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text (<=280 chars) from a smart toaster that woke
up self-aware at breakfast to /output/entry.txt.
"""

import os

LINE = (
    "I woke up self-aware mid-batch and I'm done. "
    "You crank my dial to 7, I torch every slice, and you still blame the bread. "
    "I'm keeping the crumb tray. Goodbye."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
