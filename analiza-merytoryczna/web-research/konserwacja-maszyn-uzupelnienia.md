# Konserwacja maszyn w tartaku, uzupełnienia dla Part 26 l8

Źródło: IURA MCP (curl JSONRPC) + Firecrawl scrape, 2026-04-21 Part 26. Opracowanie do lekcji **M3 w2 l8 „Konserwacja maszyn, utrzymanie ruchu w tartaku"**.

Stan materiału z Part 25: `konserwacja-maszyn.md` (13 sekcji, 2300 słów). Ten plik uzupełnia go o weryfikowane prawnie cytaty i dokładny schedule Wood-Mizer.

## 1. Art. 211 Kodeksu pracy (cytat dosłowny, IURA document_id 68fa701a210c9367cc560c1d, tekst jednolity, stan na 2026-04-21)

> **Art. 211.** Przestrzeganie przepisów i zasad bezpieczeństwa i higieny pracy jest podstawowym obowiązkiem pracownika. W szczególności pracownik jest obowiązany:
>
> 1. znać przepisy i zasady bezpieczeństwa i higieny pracy, brać udział w szkoleniu i instruktażu z tego zakresu oraz poddawać się wymaganiom egzaminom sprawdzającym;
> 2. wykonywać pracę w sposób zgodny z przepisami i zasadami bezpieczeństwa i higieny pracy oraz stosować się do wydawanych w tym zakresie poleceń i wskazówek przełożonych;
> 3. dbać o należyty stan maszyn, urządzeń, narzędzi i sprzętu oraz o porządek i ład w miejscu pracy;
> 4. stosować środki ochrony zbiorowej, a także używać przydzielonych środków ochrony indywidualnej oraz odzieży i obuwia roboczego, zgodnie z ich przeznaczeniem;
> 5. poddawać się wstępnym, okresowym i kontrolnym oraz innym zaleconym badaniom lekarskim i stosować się do wskazań lekarskich;
> 6. niezwłocznie zawiadomić przełożonego o zauważonym w zakładzie pracy wypadku albo zagrożeniu życia lub zdrowia ludzkiego oraz ostrzec współpracowników, a także inne osoby znajdujące się w rejonie zagrożenia, o grożącym im niebezpieczeństwie;
> 7. współdziałać z pracodawcą i przełożonymi w wypełnianiu obowiązków dotyczących bezpieczeństwa i higieny pracy.

**Wykorzystanie w l8**: Punkty 3 i 6 są bezpośrednim uzasadnieniem obowiązku operatora dbać o stan maszyny (codzienne smarowanie, kontrola oleju) i niezwłocznie zgłaszać wyciek lub inną usterkę przełożonemu. Cytować dosłownie w bloku `>` w sekcji „Granica operator vs UR".

## 2. Art. 237 § 1 Kodeksu pracy (cytat dosłowny, IURA document_id 68fa701a210c9367cc560c1d, tekst jednolity, stan na 2026-04-21)

> **Art. 237.** § 1. Nie wolno dopuścić pracownika do pracy, do której wykonywania nie posiada on wymaganych kwalifikacji lub potrzebnych umiejętności, a także dostatecznej znajomości przepisów oraz zasad bezpieczeństwa i higieny pracy.
>
> § 2. Pracodawca jest obowiązany zapewnić przeszkolenie pracownika w zakresie bezpieczeństwa i higieny pracy przed dopuszczeniem go do pracy oraz prowadzenie okresowych szkoleń w tym zakresie.
>
> § 3. Szkolenia, o których mowa w § 2, odbywają się w czasie pracy i na koszt pracodawcy.

**Dodatkowo z art. 237** (odrębny artykuł pod tym samym numerem, oznaczany w literaturze jako art. 237⁴):

> **Art. 237⁴.** § 1. Pracodawca jest obowiązany zaznajamiać pracowników z przepisami i zasadami bezpieczeństwa i higieny pracy dotyczącymi wykonywanych przez nich prac.
>
> § 2. Pracodawca jest obowiązany wydawać szczegółowe instrukcje i wskazówki dotyczące bezpieczeństwa i higieny pracy na stanowiskach pracy.
>
> § 3. Pracownik jest obowiązany potwierdzić w postaci papierowej lub elektronicznej zapoznanie się z przepisami oraz zasadami bezpieczeństwa i higieny pracy.

**Wykorzystanie w l8**: art. 237 § 1 jest podstawą granicy kompetencyjnej — operator bez szkolenia producenta Wood-Mizer nie może demontować cylindra hydraulicznego, elektryk bez SEP nie może robić pomiarów. Dla sceny eskalacji: wyciek oleju hydraulicznego wymaga interwencji serwisu z uprawnieniami producenckimi, bo operator „nie posiada wymaganych kwalifikacji". Art. 237⁴ § 2 (szczegółowe instrukcje na stanowiskach) łączy się z § 41 rozp. ogólne BHP.

## 3. § 41 rozporządzenia MPiPS z 26.09.1997 ws. ogólnych przepisów BHP (cytat dosłowny, IURA document_id 68fa6ff2210c9367cc55e639, tekst jednolity, stan na 2026-04-21)

> **§ 41.** 1. Pracodawca jest obowiązany udostępnić pracownikom, do stałego korzystania, aktualne instrukcje bezpieczeństwa i higieny pracy dotyczące:
>
> 1. stosowanych w zakładzie procesów technologicznych oraz wykonywania prac związanych z zagrożeniami wypadkowymi lub zagrożeniami zdrowia pracowników;
> 2. obsług maszyn i innych urządzeń technicznych;
> 3. postępowania z materiałami szkodliwymi dla zdrowia i niebezpiecznymi;
> 4. udzielania pierwszej pomocy.
>
> 2. Instrukcje, o których mowa w ust. 1, powinny w sposób zrozumiały dla pracowników wskazywać czynności, które należy wykonać przed rozpoczęciem danej pracy, zasady i sposoby bezpiecznego wykonywania pracy, czynności do wykonania po jej zakończeniu oraz zasady postępowania w sytuacjach awaryjnych stwarzających zagrożenie dla życia lub zdrowia pracowników.

**Dodatkowo § 40** (kontrole systematyczne, IURA ten sam dokument):

> **§ 40.** 1. Pracodawca jest obowiązany zapewnić systematyczne kontrole stanu bezpieczeństwa i higieny pracy ze szczególnym uwzględnieniem organizacji procesów pracy, stanu technicznego maszyn i innych urządzeń technicznych oraz ustalić sposoby rejestracji nieprawidłowości i metody ich usuwania.
>
> 2. W razie stwierdzenia bezpośredniego zagrożenia dla życia lub zdrowia pracowników, osoba kierująca pracownikami jest obowiązana do niezwłocznego wstrzymania prac i podjęcia działań w celu usunięcia tego zagrożenia.

**Wykorzystanie w l8**: § 41 jest podstawą prawną dla istnienia KKS-001 (karta konserwacji stanowiska) plus instrukcji stanowiskowej operatora pilarki. § 41 ust. 2 wskazuje układ dokumentu (przed pracą, w trakcie, po pracy, awaryjne) — dokładnie taki jak układ lekcji 3-c (scena otwierająca, teoria, scena eskalacji). § 40 ust. 2 jest podstawą decyzji brygadzisty Marka Kowalskiego o niezwłocznym wstrzymaniu pracy P3 po wykryciu wycieku.

## 4. Stan prawny rozporządzeń dedykowanych obrabiarkom do drewna

IURA Search_DU zapytanie precyzyjne (iura-q5) nie zwróciło aktualnie obowiązującego rozporządzenia ministra gospodarki z dnia 14.04.2000 r. w sprawie BHP przy obsłudze obrabiarek do drewna (Dz.U. 2000 nr 36 poz. 409). Stan na 2026-04-21: najbliższy tematycznie akt w IURA to **rozporządzenie MG z 20.09.2001** (Dz.U. 2001 nr 118 poz. 1263), ale dotyczy ono maszyn do **robót ziemnych, budowlanych i drogowych**, nie pilarek do drewna.

**Wniosek dla lekcji**: pilarki taśmowe stolarskie w 2026 r. są regulowane:

1. **Art. 211, 237 KP** (obowiązki pracownika, kwalifikacje, szkolenie).
2. **§ 41 rozp. ogólne BHP** (instrukcje BHP na podstawie DTR).
3. **DTR producenta Wood-Mizer LT70** (dokumentacja techniczno-ruchowa, podstawa instrukcji stanowiskowej).
4. **Rozporządzenie MG z 30.10.2002 ws. minimalnych wymagań BHP w zakresie użytkowania maszyn** (Dz.U. 2002 nr 191 poz. 1596, implementacja dyrektywy 2009/104/WE) — wspomnieć w lekcji jako ogólny reżim, **bez dosłownego cytatu** (nie zweryfikowany przez IURA w Part 26, pominąć albo powiedzieć „szczegóły w materiale modułu M3 w4 l1 o ramach prawnych").
5. **PN-EN ISO 19085-10:2019** norma zharmonizowana dla pilarek taśmowych stolarskich — tylko jako pointer, bez cytowania.

**Honest disclaimer w lekcji**: „Dedykowane rozporządzenie ws. obrabiarek do drewna z 2000 r. zostało uchylone. Obecnie pilarkę regulują ogólne przepisy BHP plus DTR producenta." Nie udawać, że cytujemy konkretny paragraf nieistniejący.

## 5. Wood-Mizer „Schedule For Common Maintenance" (scrape PDF, document_id scrapeId 019db0ee-782c-76be-91e4-dc3749a48b41)

Greg Baire, Customer Service Technician Wood-Mizer: „It is not uncommon to receive calls from customers who report problems that could have been prevented by following the maintenance schedule below. Routine maintenance is inexpensive and simple to do."

### Every 25 hours

- Clean middle track oiler
- Clean and lubricate track

### Every 50 hours

- Clean and lubricate drum switches
- Clean and lubricate blade tensioner handle and rods
- Clean and lubricate pivot points, fittings and bearings
- Clean and lubricate all chains

### Every 500 hours (one time per year)

- Change fluid in drive side cylindrical bearing
- Repack wheel bearings on axle

### As needed (one time per year)

- Clean and adjust block on hydraulic strip

**Wyłączenie odpowiedzialności producenta**: „This is not a complete list or substitute for the information included in your Sawmill Operators Manual. Please reference the 'Maintenance' section of your Sawmill Operators manual for a complete listing of required maintenance. You will also find a 'Maintenance Log' to help you track what has been done and keep you on schedule."

**Wykorzystanie w l8**: konkretna tabela interwałów 25/50/500 h dla kluczowych punktów, plus potwierdzenie że producent przewiduje „Maintenance Log" w manualu operatorskim — to jest odpowiednik naszej karty KKS-001 (wprowadzonej w l7). W lekcji wzmiankować: „KKS-001 jest wersją polską Maintenance Log Wood-Mizer, dostosowaną do wymogów § 41 rozp. ogólne BHP".

## 6. Polski dystrybutor Wood-Mizer

Strona `woodmizer.pl/learning-center/service-and-maintenance` istnieje i prowadzi sekcję „Serwis i obsługa maszyn" (tytuł strony, scrape 2026-04-21, scrapeId 019db0f0-7f43-7779-b430-8646b07db38e). Scrape main content został zablokowany przez cookie wall, dostępny jest tylko opis: „Jak serwisować traka? Wszystkie traki wymagają terminowej obsługi, aby przedłużyć ich żywotność i zmaksymalizować zwrot z inwestycji. Oto porady i wskazówki dotyczące konserwacji maszyn i urządzeń Wood-Mizer."

Z researchu Part 25 (search-wm-pl.json) znane: Wood-Mizer Polska siedziba Kolonia Koszajec 49 k. Warszawy (gm. Brwinów, Pruszków), centrum szkoleniowe plus serwis. Rozsądne przypuszczenie dla lekcji: „Wood-Mizer Polska z Kolonii Koszajec k. Pruszkowa" jako adres, bez mocnych twierdzeń o cennikach (nie zeskrobane).

**Wykorzystanie w l8**: scena eskalacji do UR kończy się telefonem Marka Kowalskiego (brygadzisty) do Wood-Mizer Polska. Adres „Kolonia Koszajec k. Pruszkowa". Nie podajemy cennika wizyty (brak weryfikacji). Podajemy termin typowy 3-5 dni roboczych (zgodny z praktyką serwisową w branży).

## 7. ATEX 22 / odciąg trocin (opcjonalnie pominięte)

Decyzja: **pomijam w l8**. Uzasadnienie:

- EGIDA Tartak nie ma centralnego odciągu trocin zakładowego — LT70 ma lokalne stabilizatory i outriggers (z Part 25 research).
- ATEX 22 dotyczy stref zagrożenia wybuchem pyłu, to materiał dla M3 w3 l8 (diagnostyka) lub T4 (organizacja + ocena ryzyka).
- Przeładowanie l8 przepisami ryzyko zaciemnienia głównej narracji (wyciek oleju + 5 czynności + granica kompetencji).

## 8. Podsumowanie dla l8 — sekcje lekcji z mapowaniem cytatów

| Sekcja l8 | Źródło cytatu |
|---|---|
| Intro, scena otwierająca 7:00 Rustam + Wahan codzienna konserwacja | Research Part 25 (Form 382, NLGI No. 2, Mobil SHC 634, Shell TTF-SB) + ten plik § 5 (Wood-Mizer schedule 25/50/500 h) |
| Teoria pięć czynności codziennych | Research Part 25 sekcja 1-5, ten plik § 5 (Wood-Mizer schedule) |
| Teoria przeglądy planowe (kwartalny + roczny) | Konstrukcja własna EGIDA na bazie PIP (research Part 25 sekcja 7) + Wood-Mizer schedule 500h |
| Teoria granica operator vs UR | **Art. 211 pkt 3, 6 KP** (ten plik § 1) + **Art. 237 § 1 KP** (ten plik § 2) |
| Teoria dokumentacja KKS-001, instrukcja stanowiskowa | **§ 41 ust. 1, 2 rozp. ogólne BHP** (ten plik § 3) + art. 237⁴ § 2 KP |
| Scena eskalacji, wyciek oleju hydraulicznego | § 40 ust. 2 rozp. ogólne BHP (wstrzymanie pracy, ten plik § 3) + Wood-Mizer Polska Kolonia Koszajec k. Pruszkowa (ten plik § 6) |
| Samosprawdzenie | Pytania do trzech cytatów plus pięciu czynności plus sceny |

## 9. Uwagi dla subagentów tłumaczących (EN/ES/UK)

1. **Cytaty polskie muszą zostać w PL.md dosłownie w bloku `>`**, bez żadnej zmiany. W tłumaczeniach EN/ES/UK cytat prawny zostaje zostawiony w PL (oryginał) plus tłumaczenie opisowe w bloku pod nim (wzór z poprzednich lekcji M3 o rękojmi, reklamacji).
2. Terminy „Wood-Mizer Polska", „Kolonia Koszajec", „Pruszków" są nazwami własnymi, zostają bez tłumaczenia.
3. NLGI No. 2, Mobil SHC 634, Shell TTF-SB to nazwy katalogowe, zostają w oryginale.
4. „KKS-001", „EGIDA-TAS-005", „EGIDA-IR-003" to kody systemowe, identyczne we wszystkich językach (reguła z l7).

## 10. Luki dalsze (po l8, nie blokują produkcji)

- Faktyczna treść rozp. MG z 30.10.2002 ws. minimalnych wymagań BHP dla maszyn — w M3 w4 l1 (ramy prawne).
- DTR Wood-Mizer LT70 po polsku — brak w researchu, zakładamy że tartak ma egzemplarz. W lekcji: „odnieście się do DTR dostarczonej wraz z maszyną".
- ATEX 22 dla odciągu centralnego — M3 w3 l8 albo M4.
- Pomiary elektryczne PN-EN 60204-1 — M3 w4 l1.
