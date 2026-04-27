# Kurs tartakowy EGIDA

Bezpłatny kurs zawodowy „Praca w tartaku" dla migrantów w Polsce, prowadzony przez Fundację EGIDA.

Kurs powstał jako efekt projektu „Budowa fundamentów..." (lider: SMART, partner: Fundacja EGIDA, finansowanie: EFS+ 2026-2027), ale sam kurs nie jest działaniem projektowym. Materiały są swobodnie reużywalne dla innych fundacji i projektów edukacyjnych.

## Co tu jest

To **Pakiet A** trójdzielnego projektu EGIDA Academy:

- **Pakiet A** (to repo): treść kursu (96 lekcji × 4 języki + artefakty trenerskie + materiały pomocnicze)
- **Pakiet B**: 50 dokumentów organizacyjnych (umowy, protokoły, zaświadczenia, prospekty) – zob. `podprojekt-b/`
- **Pakiet C** (planowany, Faza C): plugin Claude Code dla pracownika Fundacji tworzącego nowy kurs

Build pipeline (Python + pandoc + wkhtmltopdf) jest w osobnym repo: [`mblegal/egida-academy-tools`](https://github.com/mblegal/egida-academy-tools) (PUBLIC, MIT).

## Struktura kursu

- **3 moduły × 1 miesiąc** (M1 pomocniczy → M2 młodszy → M3 samodzielny)
- **4 bloki tematyczne** powtarzane w każdym module: Bezpieczeństwo / Materiał / Procesy / Organizacja
- **4 języki**: polski, angielski, hiszpański, ukraiński
- **Harmonogram**: pn-wt teoria (16h, sala Fundacji) + śr-pt praktyka (24h, tartak partnerski)

## Struktura repo

```
kurs_tartak/
├── content/                       # treść lekcji (MD, 96 plików × 4 jęz = 384)
│   ├── M1/, M2/, M3/              # moduły
│   └── materialy-pomocnicze/      # programy, prospekty, scenariusze trenerskie
├── podprojekt-b/                  # 50 dokumentów organizacyjnych (PL/EN/ES/UK)
├── generator/                     # build kursu HTML/Reveal.js z content/
├── scripts/                       # walidatory, narzędzia pomocnicze
└── package.json                   # npm run build:*
```

Spec projektu: [`../docs/superpowers/specs/2026-04-16-kurs-tartak-design.md`](https://github.com/mblegal/egida-academy-tools) w workspace-u nadrzędnym.

## Build (kurs HTML + prezentacje Reveal.js)

```bash
npm install
npm run build:all
```

Artefakty w `dist/`: `kurs_Mx.html`, `prezentacja_Mx.html`, PDF-y programów i prospektu.

## Test

```bash
npm test
```

## Build dokumentów (Pakiet B)

Pakiet B (50 dokumentów × HTML/DOCX/PDF) buduje się skryptem z `egida-academy-tools`:

```bash
git clone https://github.com/mblegal/egida-academy-tools
cd egida-academy-tools
pip install -r requirements.txt
python build_podprojekt_b.py --course-source ../kurs_tartak --course-slug kurs_tartak
```

## Dla zewnętrznych użytkowników (fork dla innego kursu)

Treść jest wzorem dla Fundacji EGIDA, ale można fork'ować jako szkielet dla innego zawodu / innej fundacji:

1. Fork tego repo + fork [`egida-academy-tools`](https://github.com/mblegal/egida-academy-tools)
2. Dostosuj treść w `content/` do nowego zawodu (96 lekcji × 4 języki to sporo, ale struktura modułowa daje punkt zaczepienia)
3. Dostosuj nazwy / logo w `podprojekt-b/` (sekcja `data/` w egida-academy-tools)
4. Build i deploy zgodnie z README egida-academy-tools

## Licencja

Licencja zostanie ustalona w kolejnej iteracji. Do tego czasu treść jest udostępniona „as-is" jako wzór dla pracowników Fundacji EGIDA i partnerskich fundacji edukacyjnych. Dla pytań o reużycie kontakt: Fundacja EGIDA.
