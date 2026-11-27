# Estrutura / Structure

| Pasta | O que contém |
| --- | --- |
| `constituicao/` | A Constituição da República de Cabo Verde (republicações de 1999 e 2010, retificação de 2000) |
| `codigos/<codigo>/` | Códigos: `codigos/codigo-penal/`, `codigos/codigo-processo-penal/`, `codigos/codigo-laboral/`, ... (os artigos do decreto que aprova o código são `dl-art-NNN.md`, ou ficam numa subpasta) |
| `leis/<ano>/<NNN>-<legislatura>-<objecto>/` | Leis da Assembleia Nacional, pelo ano, número e legislatura, ex. `leis/2005/071-vi-...` para a Lei n.º 71/VI/2005 |
| `decretos-legislativos/<ano>/…`, `decretos-lei/<ano>/…`, `decretos-regulamentares/<ano>/…`, `decretos/<ano>/…` | Decretos-Legislativos, Decretos-Leis, Decretos-Regulamentares e Decretos do Governo |
| `portarias/<ano>/…`, `resolucoes/<ano>/…`, `despachos/<ano>/…`, `avisos/<ano>/…` | Portarias, Resoluções, Despachos e Avisos |
| `diplomas-legislativos/<ano>/…`, `acordos-internacionais/…` | Diplomas Legislativos do período colonial; acordos internacionais |

Cada pasta de diploma tem um ficheiro por artigo (`art-012.md` é o artigo 12; `art-012-a.md` o 12-A), o
`preambulo.md`, `formula-final.md` (aprovação, promulgação, assinaturas) e um `README.md`. Quando o diploma aprova
outro texto com numeração própria (um regulamento, um estatuto), esse texto fica em `anexo-1/`, `anexo-2/`, …. Um
diploma sem artigos fica em `texto.md`. Nenhuma pasta tem mais de 1.000 entradas.

## Datas / Dates

Each act is one commit, as published, dated 12:00 Atlantic/Cape_Verde on the day it took effect, repeated in its
`In-force:` trailer; `In-force-basis:` quotes the act's own entry-into-force clause, counted from the Boletim Oficial
date (`Published:`). Acts with no such clause, or one that cannot be dated, are held, not guessed. Acts in force
before 1970 are stamped 1970-01-01, with the real day in the subject and the `In-force:` trailer. No date in this
repository is the day we downloaded anything.

## Fontes / Sources

The Constitution comes from the Boletim Oficial republications published by the Tribunal Constitucional; the codes
from the Boletim Oficial (FAOLEX copy) and the Ministério da Justiça's official editions (UNODC SHERLOC copies); the
other acts from PDF copies of the Boletim Oficial held by FAOLEX (FAO) and the Assembleia Nacional. Copies not
published by a Cabo Verdean state body carry `Source-status: secondary copy (<source>, <URL>)`. Text read from a
scan's own OCR layer carries `Text-source: publisher OCR` (we do no OCR ourselves). The Imprensa Nacional's own
Boletim Oficial site is not used (its terms require prior authorisation to copy).

## Agora / Now

792 acts from the runner: 769 secondary copies, 144 with the publisher's own OCR layer.
