#!/usr/bin/env python3
"""Write the angry judge rant to entry.txt in the output folder."""

import os

# A short rant in a sentencing judge's voice about a petty everyday
# annoyance: picked from five drafts judged pairwise on the kit's
# criteria (funny rant first, then actually funny, specific, sharp,
# fresh). The gate checks entry.txt as UTF-8 text of 1 to 400
# characters: this rant is 261 code points, 262 with its trailing
# newline (verified by a local run).
TEXT = "I have heard this printer's defense a hundred times and I reject it. It prints strangers' wedding photos all day, then pleads 'PC LOAD LETTER' the one morning I am due in court. Bailiff: unplug it, plug it back in. Fixed. Nothing else in my life works that way."


def write_entry(out_dir: str) -> None:
    """Write the rant, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
