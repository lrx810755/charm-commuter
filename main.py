"""make.fun entry: Charm the Commuter: Forecast a City That Isn't.

Writes a one-line weather forecast for a fictional city to entry.txt.
"""

import os
from pathlib import Path

LINE = "In Drizzleville, light drizzle all morning, turning to confetti by noon; umbrellas optional, dancing in the puddles strongly advised."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
