from pathlib import Path

IGNORE_FILES = 'README.md', 'FAQ.md'

def move_to_subdir(p, subdir="entries"):
    p=Path(p)
    p.rename(p.parent / subdir / p.name)
    return p


if __name__ == '__main__':
    root = "."
    subdir = "entries"
    for fpath in Path(root).glob('*.md'):
        if fpath.name in IGNORE_FILES:
            continue
        if subdir not in fpath:
            move_to_subdir(fpath, subdir)
