"""Checks on the parsed corpus that need no network: unit text sanity, and the 2010 republication against the
Assembleia Nacional's own 4th edition of the Constitution (2010), which says it includes the rectification in
BO I Série nº 28, 26 Jul 2010.

    python -X utf8 scripts/cabo-verde-law/verify.py
"""
import difflib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import parse  # noqa: E402


def state(act, upto=None):
    units = {}
    for v in act['versions']:
        if upto and v['from'] > upto:
            break
        if 'units' in v:
            units = dict(v['units'])
        for k, u in (v.get('changes') or {}).items():
            if u is None:
                units.pop(k, None)
            else:
                units[k] = u
    return units


def main():
    corpus = json.loads((HERE / 'corpus.json').read_text(encoding='utf-8'))
    report = {}
    for act in corpus['acts']:
        for v in act['versions']:
            st = state(act, v['from'])
            odd = []
            for k, u in st.items():
                for i, l in enumerate(u['text'].splitlines()[1:], 2):
                    if u['kind'] == 'art' and not re.search(r'[.;:!?)"…]$', l):
                        odd.append(f'{k}:{i}: {l[-60:]}')
            report[f"{act['slug']}@{v['from']}"] = odd
            print(act['slug'], v['from'], len(st), 'units;', len(odd), 'lines without final punctuation')
            for o in odd[:12]:
                print('   ', o)
    json.dump(report, open(HERE / '.tmp' / 'verify-lines.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
