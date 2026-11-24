"""Everyday Wonder entry writer.

Writes the one-sentence entry to /output/entry.txt, exactly as written,
with no trailing newline.
"""

from pathlib import Path

ENTRY = "My shadow on the wall was a full step behind me, and for a moment I wondered which one of us was leading."


def main() -> None:
    entry_path = Path("/output/entry.txt")
    entry_path.parent.mkdir(parents=True, exist_ok=True)
    entry_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
