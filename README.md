# Kurs tartakowy EGIDA

Bezpłatny kurs zawodowy dla migrantów w Polsce, prowadzony przez Fundację EGIDA.
Finansowanie: EFS+ 2026-2027.

## Struktura

- **3 moduły × 1 miesiąc** (M1 pomocniczy → M2 młodszy → M3 samodzielny)
- **4 bloki tematyczne** powtarzane w każdym module: Bezpieczeństwo / Materiał / Procesy / Organizacja
- **4 języki**: polski, angielski, hiszpański, ukraiński
- **Harmonogram**: pn-wt teoria (16h, sala Fundacji) + śr-pt praktyka (24h, tartak partnerski)

## Struktura repo

Zob. `docs/superpowers/specs/2026-04-16-kurs-tartak-design.md` w workspace-u nadrzędnym.

## Build

    npm install
    npm run build:all

Artefakty w `dist/`: `kurs_Mx.html`, `prezentacja_Mx.html`, PDF-y programów i prospektu.

## Test

    npm test
