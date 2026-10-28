# How this repository was made (Cabo Verde)

This file is written by the build on 2026-10-28, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| Tribunal Constitucional de Cabo Verde: Leis Constitucionais | <https://www.tribunalconstitucional.cv/index.php/leis-constitucionais/> | 2026-10-28 | 7 | Official texts of the Boletim Oficial; site "Todos os direitos Reservados". |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constituicao` | Constituição da República de Cabo Verde | 3 | 1999-11-23 to 2010-05-03 |

The build made 3 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 2 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futuro`: laws not yet in force on 2026-10-28.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 5 laws in the record.
- 5 tags.

## Dates

Each commit is dated at noon (Atlantic/Cape_Verde) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Each act in the record sets its own entry into force, which is used: LC 1/V/99 art. 185 ("entra imediatamente em vigor"), LC 1/VII/2010 art. 6 ("na data da sua publicação"), Leis 41/VIII/2013 and 121/IX/2021 ("trinta dias após a sua publicação"). https://www.tribunalconstitucional.cv/index.php/leis-constitucionais/

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-28
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-28 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/cabo-verde-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `718636fb597ba45a3473d9f7471a3cae24951aad37cc8ddaa3108f519f551095` (526939 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `2bfc4ac9df193a7be844556d7f69cdb9d93ec3f2` |
| check.py | `cd346c7ff9996d450240e3bab52bcae03b2bc865` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `3a5829f88a8893168a9bbfe423617dfc0eb4d057` |
| parse.py | `bbab9643cc904312eb85569d1bfaca3f7ad42003` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

3 versions of 1 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 3 history commits and 5 tags (history tip `1e3fa0a5af2e64fe32b50b6a4bde935786793a51`).

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- Text is read from each Boletim Oficial PDF's own text layer with PyMuPDF, column by column: blocks wider than 60% of the page or centred across the gutter cut the page into bands, and each band is read left column, then right column (pdftotext's own order interleaved the columns on some 2010 pages, moving text of art. 78º into arts. 79º and 80º). Inside a block, lines are joined into paragraphs by their position (a justified line running to the right edge continues; an indented line starts a paragraph). Page headers, page numbers and print furniture are dropped, and paragraphs split by a page or column break are joined.
- Hyphens at a line break: a repeated hyphen ("cabo-" / "-verdiano", the Portuguese rule for a compound broken at its hyphen) and a hyphen before a capital ("Procurador-" / "Geral") are kept as one hyphenated word; before a small letter the hyphen is kept only where the hyphenated word occurs elsewhere in the same document.
- Typesetting is normalised once: ligatures, non-breaking spaces, curly quotes to straight, em/en dashes to "–", "1.Texto" to "1. Texto", "c )" to "c)", spaces before ; : , removed, "110 º" to "110º".
- One file per article (art-NNN, art-NNN-a for "Artigo Nº-A"); the article number and epígrafe are the first line. Part, title, chapter and section headings are listed in constituicao/estrutura.md with the first article under each.
- Constitution: the 1992 original (LC 1/IV/92) and the 1995 revision (LC 1/IV/95) are only image scans on the Tribunal Constitucional site, so with no OCR the record starts at the 1999 republication, credited to the publisher as the oldest version available.
- Constitution: LC 1/V/99 art. 185 puts it in force immediately; the in-force day used is the day of its publication, 23 Nov 1999 (Suplemento ao BO nº 43).
- Constitution: the rectification in BO I Série nº 3 of 14 Feb 2000 corrects three printing errors in the 1999 republication (arts. 65, 153 and 260). It is dated on its publication, 14 Feb 2000, although a rectification is read as the text from the original publication.
- Constitution: LC 1/VII/2010 art. 6 puts it in force on publication, 3 May 2010 (BO I Série nº 17). It renumbered the articles, so after 2010 an article file holds the article now bearing that number; git does not follow an article across the renumbering.

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code with Claude Opus 5.5 (claude-opus-5-5) wrote fetch.py and parse.py and chose the sources; no model wrote, read or corrected any legal text, and no model runs at build time.
