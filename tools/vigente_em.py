"""Prints the law of Cabo Verde as it stood on a given day, read from this repository's history.

    python tools/vigente_em.py 2005-01-01 constituicao 65          # art. 65 of the Constitution on 1 January 2005
    python tools/vigente_em.py 2005-01-01 constituicao art-065     # the same, by file name
    python tools/vigente_em.py 2005-01-01 constituicao             # the whole Constitution on 1 January 2005
    python tools/vigente_em.py --law 2005-01-01 constituicao 65    # also name the law behind that wording

A thin wrapper around tools/on.py: the version is chosen by each commit's `In-force:` trailer, never by its commit
date, and branches named wip* are ignored. A bare article number (`65`, `65-A`) means the file `art-065` or
`art-065-a`. The articles were renumbered in 2010, so the same number can name a different article before and after
3 May 2010. Standard library only.
"""
import re
import runpy
import sys
from pathlib import Path


def article(unit: str) -> str:
    m = re.fullmatch(r'(\d+)º?(?:-([A-Za-z]))?', unit)
    if not m:
        return unit
    return f'art-{int(m.group(1)):03d}' + (f'-{m.group(2).lower()}' if m.group(2) else '')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    args = [a for a in sys.argv[1:] if a != '--law']
    if len(args) == 3:
        i = len(sys.argv) - 1 - sys.argv[::-1].index(args[2])
        sys.argv[i] = article(args[2])
    sys.argv[0] = str(Path(__file__).with_name('on.py'))
    runpy.run_path(sys.argv[0], run_name='__main__')
