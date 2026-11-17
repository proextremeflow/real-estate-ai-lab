# Architektura docelowa — propozycja

Frontend (mapa, formularz, porównanie) → API → walidacja danych → warstwa porównań i model wyceny → baza nieruchomości / geodane. Moduł AI dostaje **wyłącznie ustrukturyzowane, udokumentowane wyniki** i tworzy objaśnienie z odnośnikami.

Proponowane moduły: `properties`, `geospatial`, `comparables`, `valuation`, `negotiation`, `reports`, `ai_explanations`. Separować dane ofertowe od transakcyjnych. Logować wersję modelu, datę danych i parametry wyceny.

Na razie to dokument architektury, a nie implementacja.
