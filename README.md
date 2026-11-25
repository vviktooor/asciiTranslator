<p>
  <img src=".github/readme/banner.svg" width="100%" alt="WR · asciiTranslator: Text and ASCII converter with a GUI">
</p>

<p><img alt="English" src="https://img.shields.io/badge/English-20C9B0?style=flat-square">&nbsp;<a href="README.pl.md"><img alt="Polski" src="https://img.shields.io/badge/Polski-526077?style=flat-square"></a></p>

<p>
  <img alt="status: active" src="https://img.shields.io/badge/status-active-20C9B0?style=flat-square&labelColor=121B2B">
  <img alt="stack: Python · Tkinter" src="https://img.shields.io/badge/stack-Python%20%C2%B7%20Tkinter-3267E9?style=flat-square&labelColor=121B2B">
  <a href="../../actions/workflows/ci.yml"><img alt="CI" src="../../actions/workflows/ci.yml/badge.svg"></a>
  <img alt="license: public" src="https://img.shields.io/badge/license-public-526077?style=flat-square&labelColor=121B2B">
</p>

**Desktop app that converts text to ASCII codes and back.**
Two tabs, “Text to ASCII” and “ASCII to text”: type the input, click Convert, read the result. Invalid codes are reported, not crashed on. Interface in English or Polish, switchable in the window.

<p align="center"><img alt="Preview: Text to ASCII tab with a converted greeting" src="docs/screenshots/text-to-ascii.en.png" width="85%"></p>

## Features

- **Both directions**: text to decimal codes and back, full Unicode (Polish letters too).
- **Clear errors**: an invalid code is named in red instead of crashing the app.
- **English and Polish**: EN/PL switch in the window, `APP_LANG=pl` to start in Polish.
- **WR look**: ink background, signal accents, Poppins and JetBrains Mono.

## Quick start

Requirements: Python 3.10+ with Tkinter (`python3-tk` on Linux).

```bash
git clone https://github.com/vviktooor/asciiTranslator.git
cd asciiTranslator
pip3 install -r requirements.txt
python3 -m ascii_translator
```

## Languages

This README is available in English (default) and [Polish](README.pl.md). Interface: English by default, Polish via the EN/PL switch or `APP_LANG=pl` (strings in `ascii_translator/locales/`).

## Repository layout

| Where | What |
|---|---|
| `ascii_translator/convert.py` | Conversion logic, no GUI imports |
| `ascii_translator/gui.py` | CustomTkinter window |
| `ascii_translator/theme.py` | WR colour and font tokens |
| `ascii_translator/locales/` | `en.json` and `pl.json` |
| `tests/` | Unit tests |
| `docs/screenshots/` | Screenshots from the running app (EN and PL) |

## Tests and quality

```bash
ruff check .
ruff format --check .
python3 -m unittest discover -s tests
```

| Check | Result | Date |
|---|---|---|
| ruff | PASS | 2026-11-25 |
| Tests | PASS (10/10) | 2026-11-25 |
| Screenshots | PASS (real app under Xvfb, EN and PL) | 2026-11-25 |

## License

No licence file: all rights reserved. Ask before reusing the code. Author: WR.

Found a bug or have an idea? [Open an issue](../../issues).
