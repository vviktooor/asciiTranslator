<p>
  <img src=".github/readme/banner.pl.svg" width="100%" alt="WR · asciiTranslator: Konwerter tekstu i ASCII z GUI">
</p>

<p><a href="README.md"><img alt="English" src="https://img.shields.io/badge/English-526077?style=flat-square"></a>&nbsp;<img alt="Polski" src="https://img.shields.io/badge/Polski-20C9B0?style=flat-square"></p>

<p>
  <img alt="status: aktywny" src="https://img.shields.io/badge/status-aktywny-20C9B0?style=flat-square&labelColor=121B2B">
  <img alt="stack: Python · Tkinter" src="https://img.shields.io/badge/stack-Python%20%C2%B7%20Tkinter-3267E9?style=flat-square&labelColor=121B2B">
  <a href="../../actions/workflows/ci.yml"><img alt="CI" src="../../actions/workflows/ci.yml/badge.svg"></a>
  <img alt="licencja: publiczne" src="https://img.shields.io/badge/licencja-publiczne-526077?style=flat-square&labelColor=121B2B">
</p>

**Aplikacja desktopowa, która zamienia tekst na kody ASCII i z powrotem.**
Dwie zakładki, „Tekst na ASCII” i „ASCII na tekst”: wpisz dane, kliknij Konwertuj, odczytaj wynik. Błędne kody są zgłaszane zamiast wywracać program. Interfejs po angielsku lub po polsku, przełączany w oknie.

<<<<<<< Updated upstream

<p align="center"><img alt="Podgląd: Okno ASCII Translator" src="screenshots/ss_01.png" width="85%"></p>
=======
<p align="center"><img alt="Podgląd: Zakładka Tekst na ASCII z przekonwertowanym powitaniem" src="docs/screenshots/text-to-ascii.pl.png" width="85%"></p>
>>>>>>> Stashed changes

## Funkcje

- **Oba kierunki**: tekst na kody dziesiętne i z powrotem, pełny Unicode (także polskie litery).
- **Czytelne błędy**: błędny kod jest wskazany na czerwono zamiast wywracać aplikację.
- **Angielski i polski**: przełącznik EN/PL w oknie, `APP_LANG=pl` uruchamia po polsku.
- **Wygląd WR**: tło ink, akcenty signal, Poppins i JetBrains Mono.

## Szybki start

Wymagania: Python 3.10+ z Tkinterem (`python3-tk` na Linuksie).

```bash
git clone https://github.com/vviktooor/asciiTranslator.git
cd asciiTranslator
pip3 install -r requirements.txt
APP_LANG=pl python3 -m ascii_translator
```

## Języki

Ten README jest po polsku i po [angielsku](README.md) (wersja domyślna). Interfejs: domyślnie angielski, polski przez przełącznik EN/PL lub `APP_LANG=pl` (teksty w `ascii_translator/locales/`).

## Struktura repozytorium

| Gdzie | Co |
|---|---|
| `ascii_translator/convert.py` | Logika konwersji, bez importów GUI |
| `ascii_translator/gui.py` | Okno CustomTkinter |
| `ascii_translator/theme.py` | Kolory i czcionki WR |
| `ascii_translator/locales/` | `en.json` i `pl.json` |
| `tests/` | Testy jednostkowe |
| `docs/screenshots/` | Zrzuty z uruchomionej aplikacji (EN i PL) |

## Testy i jakość

```bash
ruff check .
ruff format --check .
python3 -m unittest discover -s tests
```

| Kontrola | Wynik | Data |
|---|---|---|
| ruff | PASS | 2026-11-25 |
| Testy | PASS (10/10) | 2026-11-25 |
| Zrzuty ekranu | PASS (prawdziwa aplikacja pod Xvfb, EN i PL) | 2026-11-25 |

## Licencja

Brak pliku licencji: wszelkie prawa zastrzeżone. Zapytaj przed ponownym użyciem kodu. Autor: WR.

Znalazłeś błąd albo masz pomysł? [Zgłoś go w Issues](../../issues).
