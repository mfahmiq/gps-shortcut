"""GPS Shortcut — make.fun entry.

Writes the GPS's one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). No network, no file reads, no secrets: the entry
text is embedded verbatim below.
"""

import os

ENTRY = (
    "We're not lost, we're early to a wedding we weren't invited to. "
    "The map already RSVP'd plus one."
)


def main():
    """Write the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
