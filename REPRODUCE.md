# How this repository was made (Cabo Verde)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Tribunal Constitucional de Cabo Verde: Leis Constitucionais | <https://www.tribunalconstitucional.cv/index.php/leis-constitucionais/> | 2026-10-28 | Official texts of the Boletim Oficial; site "Todos os direitos Reservados". |
| Boletim Oficial, I Série, n.º 37, suplemento (16 Oct 2007): Decreto-Legislativo n.º 5/2007 (Código Laboral) | <https://faolex.fao.org/docs/pdf/cvi221870original.pdf> | 2026-10-30 | Official text of the Imprensa Nacional de Cabo Verde; copy held by FAOLEX (FAO) |
| Ministério da Justiça: Código Penal de Cabo Verde (official edition, May 2004) | <https://sherloc.unodc.org/cld/uploads/res/document/cpv/2003/codigo_penal_html/Codigo_Penal_Cabo_Verde.pdf> | 2026-10-30 | Edition of the Ministério da Justiça de Cabo Verde; copy held by UNODC SHERLOC |
| Ministério da Justiça: Código de Processo Penal de Cabo Verde (official edition, June 2005) | <https://sherloc.unodc.org/cld/uploads/res/document/cdigo-de-processo-penal-de-cabo-verde_html/Cabo_Verde_Code_of_Criminal_Procedure_in_Portuguese.pdf> | 2026-10-30 | Edition of the Ministério da Justiça de Cabo Verde; copy held by UNODC SHERLOC |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constituicao` | Constituição da República de Cabo Verde | 3 | 1999-11-23 to 2010-05-03 |
| `codigo-laboral` | Código Laboral Cabo-Verdiano (Decreto-Legislativo n.º 5/2007, de 16 de Outubro) | 1 | 2008-04-13 to 2008-04-13 |
| `codigo-penal` | Código Penal (Decreto-Legislativo n.º 4/2003, de 18 de Novembro) | 1 | 2004-07-01 to 2004-07-01 |
| `codigo-processo-penal` | Código de Processo Penal (Decreto-Legislativo n.º 2/2005, de 7 de Fevereiro) | 1 | 2005-10-01 to 2005-10-01 |

The build made 6 commits:

| Commits | Kind |
| ---: | --- |
| 4 | first version of an act |
| 2 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futuro`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 8 laws in the record.
- 11 tags.

## Dates

Each commit is dated at noon (Atlantic/Cape_Verde) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Each act in the record sets its own entry into force, which is used: LC 1/V/99 art. 185 ("entra imediatamente em vigor"), LC 1/VII/2010 art. 6 ("na data da sua publicação"), Leis 41/VIII/2013 and 121/IX/2021 ("trinta dias após a sua publicação"). https://www.tribunalconstitucional.cv/index.php/leis-constitucionais/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `e30fa8a907fc48a8d93c783577cb5971b240006c5119be62424826a66891fd49` (1632342 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

6 versions of 4 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 6 history commits and 11 tags (history tip `01c0d3646570386b9d5aa5b3df7eeca66803d5d3`).

## Decisions made by hand

- Text is read from each Boletim Oficial PDF's own text layer with PyMuPDF, column by column: blocks wider than 60% of the page or centred across the gutter cut the page into bands, and each band is read left column, then right column (pdftotext's own order interleaved the columns on some 2010 pages, moving text of art. 78º into arts. 79º and 80º). Inside a block, lines are joined into paragraphs by their position (a justified line running to the right edge continues; an indented line starts a paragraph). Page headers, page numbers and print furniture are dropped, and paragraphs split by a page or column break are joined.
- Hyphens at a line break: a repeated hyphen ("cabo-" / "-verdiano", the Portuguese rule for a compound broken at its hyphen) and a hyphen before a capital ("Procurador-" / "Geral") are kept as one hyphenated word; before a small letter the hyphen is kept only where the hyphenated word occurs elsewhere in the same document.
- Typesetting is normalised once: ligatures, non-breaking spaces, curly quotes to straight, em/en dashes to "–", "1.Texto" to "1. Texto", "c )" to "c)", spaces before ; : , removed, "110 º" to "110º".
- One file per article (art-NNN, art-NNN-a for "Artigo Nº-A"); the article number and epígrafe are the first line. Part, title, chapter and section headings are listed in constituicao/estrutura.md with the first article under each.
- Constitution: the 1992 original (LC 1/IV/92) and the 1995 revision (LC 1/IV/95) are only image scans on the Tribunal Constitucional site, so with no OCR the record starts at the 1999 republication, credited to the publisher as the oldest version available.
- Constitution: LC 1/V/99 art. 185 puts it in force immediately; the in-force day used is the day of its publication, 23 Nov 1999 (Suplemento ao BO nº 43).
- Constitution: the rectification in BO I Série nº 3 of 14 Feb 2000 corrects three printing errors in the 1999 republication (arts. 65, 153 and 260). It is dated on its publication, 14 Feb 2000, although a rectification is read as the text from the original publication.
- Constitution: LC 1/VII/2010 art. 6 puts it in force on publication, 3 May 2010 (BO I Série nº 17). It renumbered the articles, so after 2010 an article file holds the article now bearing that number; git does not follow an article across the renumbering.
- Checked against an independent extraction of each republication (pdftotext): art. 254 of the 1999 text ends with a full stop that the page sets apart before the next title, and it is restored; the hymn in the annex is one verse per line as printed (the 1999 reading had taken the run-on lyrics under the score, and the 2010 reading had run three pairs of verses together). No word changed.
- Constitution: the Assembleia Nacional's 4th edition (2010) states that the 2010 text was rectified in BO I Série nº 28 of 26 Jul 2010. That rectification was not found, so it is not applied; six articles of the AN edition differ in wording from the BO republication (arts. 88, 91, 168, 181, 203, 226 of the 2010 numbering), and the record keeps the BO wording.
- Código Laboral: one version, Decreto-Legislativo n.º 5/2007 and the Code it approves as published (BO I Série n.º 37, suplemento, 16 Oct 2007), credited to the decree and dated 2008-04-13: its art. 16 puts it in force "no prazo de 180 dias a contar da sua publicação", and the 180th day counted from the day after publication (Código Civil art. 279) is 13 Apr 2008. The later amendments (Decreto-Legislativo n.º 5/2010, Decreto-Legislativo n.º 1/2016, Lei n.º 32/X/2023) are not applied: the record holds the text as enacted.
- Código Laboral: the decree's preamble and articles (dl-art-NNN) and one file per article of the Code (art-NNN); title, chapter and section headings and the approval, promulgation and signature formulas are not units. The typeset ligatures "fi" and "fl", printed with a following space ("qualiﬁ cação"), are closed up.
- Código Penal: one version, Decreto-Legislativo n.º 4/2003 with the Code as enacted, read from the Ministério da Justiça's official edition of May 2004 (the Boletim Oficial of 18 Nov 2003 was not found with a text layer), credited to the decree and dated 2004-07-01 (decree art. 10). The later amendments (Decreto-Legislativo n.º 4/2015, Lei n.º 117/IX/2021, Lei n.º 18/X/2023 and others) are not applied: the record holds the text as enacted.
- Código Penal: the decree's preamble and articles (dl-art-NNN), the Code's own preamble (preambulo-codigo, its sub-headings kept as lines) and one file per article of the Code (art-NNN); book, title, chapter and section headings, page numbers, the edition's front matter and indexes and the approval, promulgation and signature formula are not units.
- Código de Processo Penal: one version, Decreto-Legislativo n.º 2/2005 with the Code as enacted, read from the Ministério da Justiça's official edition of June 2005, credited to the decree and dated 2005-10-01 (decree art. 5). The later amendments (Decreto-Legislativo n.º 5/2015, which republished the Code, and later laws) are not applied: the record holds the text as enacted.
- Código de Processo Penal: the decree's preamble and articles (dl-art-NNN), the Code's own preamble (preambulo-codigo, its section numbers kept as lines) and one file per article of the Code (art-NNN); part, book, title, chapter and section headings, page numbers, the edition's front matter and index and the approval, promulgation and signature formula are not units.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code with Claude Opus 5.5 (claude-opus-5-5) wrote Lexifina's code and chose the sources; no model wrote, read or corrected any legal text, and no model runs at build time.
