<p>
  <img src=".github/readme/banner.pl.svg" width="100%" alt="WR · asciiTranslator: Konwerter tekstu i ASCII z GUI">
</p>

<p><a href="README.md"><img alt="English" src="https://img.shields.io/badge/English-526077?style=flat-square"></a>&nbsp;<img alt="Polski" src="https://img.shields.io/badge/Polski-20C9B0?style=flat-square"></p>

<p>
  <img alt="status: aktywny" src="https://img.shields.io/badge/status-aktywny-20C9B0?style=flat-square&labelColor=121B2B">
  <img alt="stack: Python · Tkinter" src="https://img.shields.io/badge/stack-Python%20%C2%B7%20Tkinter-3267E9?style=flat-square&labelColor=121B2B">
  <img alt="licencja: publiczne" src="https://img.shields.io/badge/licencja-publiczne-526077?style=flat-square&labelColor=121B2B">
</p>

**Aplikacja desktopowa, która zamienia tekst na kody ASCII i z powrotem.**
Dwie zakładki, „TEXT TO ASCII” i „ASCII TO TEXT”: wpisz dane, kliknij konwersję, wynik pojawi się poniżej.


<p align="center"><img alt="Podgląd: Okno ASCII Translator" src="screenshots/ss_01.png" width="85%"></p>

## Funkcje

- **Oba kierunki**: tekst na ASCII i ASCII na tekst.
- **Tryb ciemny** i pełny ekran.
- **Okno o zmiennym rozmiarze**.

## Szybki start

Wymagania: Python 3, dostęp do internetu dla `pip`.

```bash
git clone https://github.com/vviktooor/asciiTranslator.git
cd asciiTranslator
pip3 install -r requirements.txt
python3 operations.py
```

## Języki

Ten README jest po polsku i po [angielsku](README.md) (wersja domyślna). Interfejs: angielski. Polski interfejs: planowany (standard WR v4.4).

## Struktura repozytorium

| Gdzie | Co |
|---|---|
| `operations.py` | Punkt startowy i logika konwersji |
| `gui.py` | Okno Tkinter |
| `screenshots/` | Zrzuty ekranu |

## Testy i jakość

| Kontrola | Wynik | Data |
|---|---|---|
| Testy | NOT VERIFIED (brak testów) | 2026-11-25 |

## Licencja

Brak pliku licencji: wszelkie prawa zastrzeżone. Zapytaj przed ponownym użyciem kodu. Autor: WR.

Znalazłeś błąd albo masz pomysł? [Zgłoś go w Issues](../../issues).
