#!/usr/bin/env python3
"""News-image entry for 20 November 2026.

The repository holds the finished summary image as entry.png.
This program copies it to the output directory, unchanged, so both
grader runs produce exactly the same bytes. Standard library only.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"entry image missing: {SOURCE}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(SOURCE, destination)
    # The gate accepts at most 1 MiB; fail loudly instead of writing a bad entry.
    size = destination.stat().st_size
    if size > 1_048_576:
        raise ValueError(f"entry image too large: {size} bytes")


if __name__ == "__main__":
    main()
