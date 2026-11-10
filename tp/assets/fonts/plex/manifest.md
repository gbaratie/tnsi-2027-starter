# Polices des compositions techniques

Polices IBM Plex, conçues par IBM et distribuées sous **SIL Open Font License 1.1**. Fichiers WOFF2 du sous-ensemble latin, récupérés le 9 novembre 2026. Les noms réservés et conditions sont conservés dans les licences ci-dessous. Les binaires sont copiés sans modification.

| Fichier | Graisse | Distribution versionnée |
|---|---|---|
| `IBMPlexSans-Regular-Latin.woff2` | 400 | [Fontsource IBM Plex Sans 5.2.8](https://www.npmjs.com/package/@fontsource/ibm-plex-sans/v/5.2.8) |
| `IBMPlexSans-Medium-Latin.woff2` | 500 | Même distribution |
| `IBMPlexSans-SemiBold-Latin.woff2` | 600 | Même distribution |
| `IBMPlexSans-Bold-Latin.woff2` | 700 | Même distribution |
| `IBMPlexMono-Regular-Latin.woff2` | 400 | [Fontsource IBM Plex Mono 5.3.0](https://www.npmjs.com/package/@fontsource/ibm-plex-mono/v/5.3.0) |

Licences intégrales : [IBM Plex Sans](LICENSE-sans.txt), [IBM Plex Mono](LICENSE-mono.txt). Projet de référence : [IBM Plex](https://github.com/IBM/plex).

Les slides techniques chargent ces fichiers localement via `@font-face`. Les SVG utilisés comme images incorporent les graisses Sans 400 et 600 dans leur propre style, car une image SVG ne peut pas compter sur les fontes du document qui l'affiche. Les titres et textes incorporés aux infographies raster sont dessinés par le générateur ; ces fichiers de fontes concernent le HTML et les SVG.
