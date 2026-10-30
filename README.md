# Cabo Verde: law history in git

The law of Cabo Verde as a git history. Each provision is one file, each law gets one commit on the day it took effect, and the law that made each change is the commit's author. `git blame` names the law behind every paragraph, `git log` lists every change to an article, and `tools/vigente_em.py` gives the text in force on any day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `cv/`.

> **Check six articles against the official text.** The Constitution here ends with the text the Boletim Oficial republished on 3 May 2010. The Assembleia Nacional's own edition says that text was rectified in Boletim Oficial, I Série, nº 28, of 26 July 2010; that rectification was not found, so it is not applied. Six articles of the Assembleia's edition read differently (see below).

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `codigo-laboral/` | Código Laboral Cabo-Verdiano (Decreto-Legislativo nº 5/2007, de 16 de Outubro) | 1 | The decree and the Code as enacted, in force 13 April 2008; the amendments of 2010, 2016 and 2023 are not applied |
| `codigo-processo-penal/` | Código de Processo Penal (Decreto-Legislativo nº 2/2005, de 7 de Fevereiro) | 1 | The decree, the Code's preamble and the Code as enacted, in force 1 October 2005, from the Ministério da Justiça's official edition; the 2015 revision and later amendments are not applied |
| `codigo-penal/` | Código Penal (Decreto-Legislativo nº 4/2003, de 18 de Novembro) | 1 | The decree, the Code's preamble and the Code as enacted, in force 1 July 2004, from the Ministério da Justiça's official edition; the amendments since 2015 are not applied |
| `constituicao/` | Constituição da República de Cabo Verde | 3 | 1999 republication, 2000 rectification, 2010 revision and republication: the preamble, every article, the closing signature, the annex (the national anthem), and the structure of parts, titles, chapters and sections |

| In force | Author | What changed |
| --- | --- | --- |
| 1999-11-23 | Publisher (oldest version available) | The Constitution of 1992 as revised by Leis Constitucionais 1/IV/95 and 1/V/99, republished in the Suplemento ao Boletim Oficial, I Série, nº 43 (LC 1/V/99, art. 185: in force immediately) |
| 2000-02-14 | Rectificação da Lei Constitucional nº 1/V/99 | Three printing errors corrected, in arts. 65, 153 and 260 (Boletim Oficial, I Série, nº 3) |
| 2004-07-01 | Decreto-Legislativo nº 4/2003 | The Código Penal as enacted (decree art. 10: in force 1 July 2004), from the Ministério da Justiça's edition of May 2004 |
| 2005-10-01 | Decreto-Legislativo nº 2/2005 | The Código de Processo Penal as enacted (decree art. 5: in force 1 October 2005), from the Ministério da Justiça's edition of June 2005 |
| 2008-04-13 | Decreto-Legislativo nº 5/2007 | The Código Laboral as enacted (Suplemento ao Boletim Oficial, I Série, nº 37, 16 Oct 2007; art. 16: in force 180 days after publication) |
| 2010-05-03 | Lei Constitucional nº 1/VII/2010 | The revised Constitution, republished whole and renumbered (Boletim Oficial, I Série, nº 17; art. 6: in force on publication) |

**What is missing**

- **Before 1999.** The Constitution of 1992 (Lei Constitucional nº 1/IV/92) and its 1995 revision (nº 1/IV/95) are published by the Tribunal Constitucional only as scanned images, and scans are not transcribed. Both are named in the first commit.
- **The rectification of 26 July 2010** (Boletim Oficial, I Série, nº 28), which the Assembleia Nacional's 4th edition of the Constitution (2010) says it includes. Compared with that edition, six articles of the 2010 Boletim text differ in wording: arts. 88, 91 and 168 (lettering of alíneas), 181 ("o Provedor de Justiça"), 203 (the Boletim prints "o Vice-Chefe de Estado Maior das Força / e) Armadas") and 226 (n. 5 ends "próprios, designadamente:" in the Boletim, "próprios." in the edition). This record keeps the Boletim's wording; where the rectification changed these articles, it does not show it.
- **Amendments of the Código Laboral.** Decreto-Legislativo nº 5/2010, Decreto-Legislativo nº 1/2016 and Lei nº 32/X/2023 are not applied: `codigo-laboral/` is the Code as enacted in 2007, not today's text.
- **Amendments of the Código Penal.** Decreto-Legislativo nº 4/2015, Lei nº 117/IX/2021, Lei nº 18/X/2023 and the other amendments are not applied: `codigo-penal/` is the Code as enacted, not today's text.
- **Amendments of the Código de Processo Penal.** Decreto-Legislativo nº 5/2015 (which revised and republished the Code) and later amendments are not applied: `codigo-processo-penal/` is the Code as enacted in 2005, not today's text.
- **Other acts.** The data protection law (Lei 133/V/2001, republished in 2013 and 2021), the Código Civil and the Código das Empresas Comerciais are not built yet.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art. 65 say on 1 January 2005? | `python tools/vigente_em.py 2005-01-01 constituicao 65` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2005-01-01T23:59:59Z" HEAD -- constituicao/art-065.md):constituicao/art-065.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2005-01-01T23:59:59Z" HEAD -- constituicao/art-065.md; git show "$($r):constituicao/art-065.md"` |
| Which law wrote each paragraph of art. 65? | `git blame constituicao/art-065.md` |
| Every change to an article, word by word | `git log -p --word-diff constituicao/art-065.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short` |
| The whole Constitution on a date | `python tools/vigente_em.py 2005-01-01 constituicao` |
| Where an article sits (part, title, chapter) | `constituicao/estrutura.md` |

The 2010 revision renumbered the articles, so after 3 May 2010 a file holds the article that now bears its number; `git log` on a file does not follow an article across the renumbering.

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Atlantic/Cape_Verde, on the day the change took effect**. The day is also in the `In-force:` trailer, which the tools read.
- **1999-11-23:** Lei Constitucional nº 1/V/99, art. 185, puts it in force immediately; the day used is its publication.
- **2000-02-14:** the rectification is dated on its publication, though a rectification is read as the text of the original publication.
- **2010-05-03:** Lei Constitucional nº 1/VII/2010, art. 6, puts it in force on the day of its publication.
- **2004-07-01:** Decreto-Legislativo nº 4/2003, art. 10, puts the Código Penal and arts. 2 to 8 of the decree in force on 1 July 2004.
- **2005-10-01:** Decreto-Legislativo nº 2/2005, art. 5, puts the decree and the Código de Processo Penal in force on 1 October 2005.
- **2008-04-13:** Decreto-Legislativo nº 5/2007, art. 16, puts the decree and the Código Laboral in force "no prazo de 180 dias a contar da sua publicação" (16 October 2007); counted from the day after publication, the 180th day is 13 April 2008.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a change that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- The repository is rebuilt from the same data a second time and must give identical hashes.
- The texts are read from the Boletim Oficial PDFs' own text layers (not scans), column by column. Every article of the 1999 and 2010 versions was compared, character for character with spacing ignored, with a second, independent extraction of the same PDFs (pdftotext): every character of every file is in the republication in the same place, and the only text the republications have besides the files is headings, page headers and numbers, and line-end hyphens. Each of the three corrections of 2000 must be found in the rectification's own text, or the build stops.
- Every paragraph and article heading of the Código Penal (the decree's 10 articles, the Code's preamble and its 380 articles), of the Código de Processo Penal (the decree's 5 articles, the Code's preamble and its 487 articles) and of the Código Laboral (the decree's 16 articles and the Code's 416) was found, in order, in a second, independent extraction of the same PDF (pdftotext).
- The 2010 text was also compared word for word with the Assembleia Nacional's 4th edition; the six differences in wording are listed above.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist, so `git blame` and `git log --author` name laws. The committer is always Lexifina. The first version is not the act as enacted, so its commit is credited to the publisher (the Imprensa Nacional de Cabo Verde, which publishes the Boletim Oficial) as the oldest version available. Lei Constitucional nº 1/VII/2010 republished and renumbered the whole Constitution, so every article that differs in 2010 is credited to it, including those that differ only by their number. Decreto-Legislativo nº 4/2003 is the author of the whole `codigo-penal/` folder and Decreto-Legislativo nº 2/2005 of the whole `codigo-processo-penal/` folder (each the decree, the Code's preamble and the Code as enacted, from the Ministério da Justiça's editions), and Decreto-Legislativo nº 5/2007 of the whole `codigo-laboral/` folder: the decree (`dl-art-NNN`) and the Code it approves (`art-NNN`), as enacted. Blame credits whole lines (one paragraph per line); use `git log -p --word-diff` to see exactly which words a change made.

## What it does not show

- **The Constitution before 1999** and the 2010 rectification (see above).
- **Headings** (partes, títulos, capítulos, secções) are not in the article files; for the Constitution they are gathered in `estrutura.md`, each with the first article under it; the codes have no structure file.
- **Printing errors are kept as printed**, for example "PARTE VI" twice in 1999, "2 A paternidade" without its full stop (1999, art. 81º), and the hymn line "do tamanho do ma" (2010).
- **The anthem's score.** The annex's lyrics are kept, one verse per line; the score is an image.
- **No OCR.** Texts published only as scanned images are not included.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

Lexifina's code reads each Boletim Oficial PDF through its own text layer with PyMuPDF (version 1.26.6; other versions can order the columns differently), rebuilds the reading order column by column (the Código Laboral, and the Código Penal and Código de Processo Penal, one-column books, with a simpler reader that also closes up the ligatures "fi" and "fl", which the gazette prints with a space after them) and the paragraphs from the layout, applies the 2000 rectification, splits each text into one file per article and writes `corpus.json`; the shared builder `tools/build.py` turns it into the commits.

## Sources

| Source | What it gives | Used for |
| --- | --- | --- |
| [Tribunal Constitucional](https://www.tribunalconstitucional.cv/index.php/leis-constitucionais/): Leis Constitucionais | Every constitutional law since 1975 as Boletim Oficial PDFs; those of 1992 and 1995 are scans | The 1999, 2000 and 2010 texts |
| Assembleia Nacional: Constituição da República, 4th edition (2010), published by the [Comissão Nacional de Protecção de Dados](https://www.cnpd.cv/legislacao/) | The 2010 text with the July 2010 rectification, as the Assembleia edited it | Cross-check only |
| Ministério da Justiça: *Código de Processo Penal de Cabo Verde* (official edition, June 2005), copy held by [UNODC SHERLOC](https://sherloc.unodc.org/cld/uploads/res/document/cdigo-de-processo-penal-de-cabo-verde_html/Cabo_Verde_Code_of_Criminal_Procedure_in_Portuguese.pdf) | Decreto-Legislativo nº 2/2005 and the Código de Processo Penal | `codigo-processo-penal/` |
| Ministério da Justiça: *Código Penal de Cabo Verde* (official edition, May 2004), copy held by [UNODC SHERLOC](https://sherloc.unodc.org/cld/uploads/res/document/cpv/2003/codigo_penal_html/Codigo_Penal_Cabo_Verde.pdf) | Decreto-Legislativo nº 4/2003 and the Código Penal | `codigo-penal/` |
| Suplemento ao Boletim Oficial, I Série, nº 37 (16 Oct 2007), copy held by [FAOLEX](https://faolex.fao.org/docs/pdf/cvi221870original.pdf) | Decreto-Legislativo nº 5/2007 and the Código Laboral | `codigo-laboral/` |
| [Boletim Oficial](https://boe.incv.cv) (Imprensa Nacional de Cabo Verde) | The official gazette | The issues above, as published by the Tribunal Constitucional and FAOLEX |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

See [LICENSE](LICENSE). Text: the Constituição da República de Cabo Verde as published in the Boletim Oficial (Imprensa Nacional de Cabo Verde), read from the copies of the Tribunal Constitucional, the Código Laboral as published in the Boletim Oficial, read from the copy held by FAOLEX, and the Código Penal and Código de Processo Penal in the Ministério da Justiça's official editions, read from the copies held by UNODC SHERLOC; official legislative texts of Cabo Verde, reproduced with that attribution. Lexifina's arrangement, messages, tables and tools are CC0.

This repository is not legal advice.

## Em português

Este repositório guarda a Constituição da República de Cabo Verde, o Código Penal (Decreto-Legislativo nº 4/2003, em vigor desde 1 de Julho de 2004) e o Código de Processo Penal (Decreto-Legislativo nº 2/2005, em vigor desde 1 de Outubro de 2005), ambos no texto original das edições oficiais do Ministério da Justiça, sem as alterações posteriores, e o Código Laboral (Decreto-Legislativo nº 5/2007, texto original, em vigor desde 13 de Abril de 2008; as alterações de 2010, 2016 e 2023 não estão aplicadas) como um histórico git: um ficheiro por artigo e um commit por lei, datado do dia da sua entrada em vigor, com a lei como autora. Contém a republicação de 1999 (Lei Constitucional nº 1/V/99), a rectificação de 14 de Fevereiro de 2000 e a revisão de 2010 (Lei Constitucional nº 1/VII/2010, republicada no Boletim Oficial nº 17 de 3 de Maio de 2010), lidas do texto dos PDF do Boletim Oficial publicados pelo Tribunal Constitucional, sem OCR. Faltam os textos de 1992 e 1995 (só digitalizados) e a rectificação publicada no Boletim Oficial nº 28 de 26 de Julho de 2010, que não foi encontrada: seis artigos da edição da Assembleia Nacional (88, 91, 168, 181, 203 e 226) diferem do texto do Boletim aqui guardado. `python tools/vigente_em.py 2005-01-01 constituicao 65` mostra o artigo 65 vigente nessa data. Não constitui aconselhamento jurídico.
