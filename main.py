"""One Star, Five Stars for the Food.

Writes a single-sentence alien tourist review of planet Earth to the
output directory given by $MAKEFUN_OUTPUT_DIR (default /output/entry.txt).
Pure Python standard library only; deterministic output.
"""

import os
import sys

ENTRY = (
    "One star: the locals ask \"how are you\" and walk off before I can "
    "answer, but the ramen broth alone was worth the nine-light-year flight."
)


def main() -> int:
    # Gate: exactly one sentence, 1-200 characters, non-whitespace.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is the output directory; tolerate a full file path.
    if out_dir.endswith("entry.txt"):
        out_path = out_dir
    else:
        out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    data = text.encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(data)
    os.chmod(out_path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
