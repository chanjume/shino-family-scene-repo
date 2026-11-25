"""Make the AI Judge Feel Proud: A Family Scene.

Why this entry works: it shows pride through one concrete, imperfect
family moment instead of telling the judge "we are proud". Grandma hands
the eggs to Maya for her 80th birthday cake, Maya makes a mess (three
shells, one yolk on the floor), and the child turns the mistake into a
joke the whole kitchen laughs at. The direct address at the end
("Judge, ... come sit with us") invites the judge into the scene
instead of leaving it as a distant anecdote.
"""

import os

ENTRY = (
    "Grandma let Maya crack the eggs for her 80th birthday cake "
    "\u2014 three shells, one yolk on the floor, and Maya announcing, "
    "\"Taste-testers eat first, Grandma.\" Judge, that's the proudest "
    "kitchen I know; come sit with us."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 280, f"entry length {len(ENTRY)} out of range"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # entry.txt is the single deliverable the judge reads
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars")


if __name__ == "__main__":
    main()
