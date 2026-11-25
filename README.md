<p>
  <img src=".github/readme/banner.svg" width="100%" alt="WR · asciiTranslator: Text and ASCII converter with a GUI">
</p>

<p><img alt="English" src="https://img.shields.io/badge/English-20C9B0?style=flat-square">&nbsp;<a href="README.pl.md"><img alt="Polski" src="https://img.shields.io/badge/Polski-526077?style=flat-square"></a></p>

<p>
  <img alt="status: active" src="https://img.shields.io/badge/status-active-20C9B0?style=flat-square&labelColor=121B2B">
  <img alt="stack: Python · Tkinter" src="https://img.shields.io/badge/stack-Python%20%C2%B7%20Tkinter-3267E9?style=flat-square&labelColor=121B2B">
  <img alt="license: public" src="https://img.shields.io/badge/license-public-526077?style=flat-square&labelColor=121B2B">
</p>

**Desktop app that converts text to ASCII codes and back.**
Two tabs, “TEXT TO ASCII” and “ASCII TO TEXT”: type the input, click convert, read the result below.


<p align="center"><img alt="Preview: ASCII Translator window" src="screenshots/ss_01.png" width="85%"></p>

## Features

- **Both directions**: text to ASCII and ASCII to text.
- **Dark mode** and fullscreen mode.
- **Resizable window**.

## Quick start

Requirements: Python 3, internet access for `pip`.

```bash
git clone https://github.com/vviktooor/asciiTranslator.git
cd asciiTranslator
pip3 install -r requirements.txt
python3 operations.py
```

## Languages

This README is available in English (default) and [Polish](README.pl.md). Interface: English. Polish interface: planned (WR standard v4.4).

## Repository layout

| Where | What |
|---|---|
| `operations.py` | Entry point and conversion logic |
| `gui.py` | Tkinter window |
| `screenshots/` | Screenshots |

## Tests and quality

| Check | Result | Date |
|---|---|---|
| Tests | NOT VERIFIED (no tests yet) | 2026-11-25 |

## License

No licence file: all rights reserved. Ask before reusing the code. Author: WR.

Found a bug or have an idea? [Open an issue](../../issues).
