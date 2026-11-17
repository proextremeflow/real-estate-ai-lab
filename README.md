# Real Estate AI Lab

Platforma wspomagania decyzji na polskim rynku nieruchomości: szacowanie wartości, porównywanie ofert, analiza lokalizacji i przygotowanie negocjacji. **Etap: koncepcja / fundament repozytorium; brak działającego modelu wyceny.**

## Wartość dla użytkownika
- Przedział szacowanej wartości wraz z uzasadnieniem, poziomem niepewności i datą danych.
- Porównywalne oferty/transakcje z filtrami powierzchni, stanu, standardu i lokalizacji.
- Analiza preferencji: bliskość plaży, jeziora, komunikacji, szkół, terenów zielonych i usług.
- Scenariusze negocjacyjne: cena ofertowa vs uzasadniony przedział, koszty dodatkowe, argumenty za/przeciw.
- Analiza całkowitego kosztu zakupu i potencjalnego wynajmu; bez obiecywania zwrotu.

## Ważne rozróżnienia
**Cena ofertowa nie jest ceną transakcyjną.** Model powinien wyraźnie odróżniać oba źródła. Nie wolno prezentować wymyślonej wyceny jako zweryfikowanej. AI ma tłumaczyć wynik modelu i pomagać w wyszukiwaniu, a nie fabrykować porównania.

## Roadmapa
1. Zdefiniować źródła danych, ich licencje, jakość i aktualność; rozpocząć od danych syntetycznych.
2. Zbudować walidowany schemat nieruchomości i geokodowanie lokalizacji.
3. Baseline: ceny/m² i podobieństwo nieruchomości; testy błędu MAE/MAPE z podziałem czasowym.
4. Model hedoniczny / gradient boosting; przedziały predykcyjne i analiza błędów dla małych miejscowości.
5. Interfejs mapowy, preferencje użytkownika, koszty zakupu i raport negocjacyjny.
6. Moduł AI z cytowaniem źródeł i kontrolą halucynacji.
7. Dopiero później: integracje ofert, leady, pośrednictwo i analiza obowiązków prawnych.

## Katalogi
- `docs/` — koncepcja, architektura, wymagania, źródła danych
- `data/samples/` — przykładowe dane syntetyczne
- `src/real_estate_ai/` — kod aplikacji i modelu
- `tests/` — testy
- `notebooks/` — eksperymenty
- `infra/` — wdrożenie i konfiguracja

## Zasady
Nie commituj danych osobowych, kluczy API, prywatnych adresów ani zbiorów objętych ograniczeniami licencyjnymi. Wynik nie jest operatem szacunkowym rzeczoznawcy majątkowego.
