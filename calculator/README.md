# Calculator

A small desktop calculator written in Python with `tkinter`. The interface is in Persian (Farsi).

## Features

- Addition, subtraction, multiplication, and division
- Power (exponent) operation
- Temperature conversion between Celsius, Fahrenheit, and Kelvin using two dropdowns
- Input validation: empty fields, text instead of numbers, division by zero, invalid powers (such as 0 to a negative power, or a negative base with a fractional exponent), and oversized results show a message instead of crashing
- Clean result display: floating-point noise is rounded away and whole numbers appear without `.0`

## Project structure

| File | Purpose |
|------|---------|
| `main.py` | Builds the window and connects the buttons to the functions. Run this file. |
| `calculator_functions.py` | The math and the temperature conversions. It has no interface code, so every function can be tested on its own. |
| `app_icon.png` | Window icon. |
| `docs/Python_Calculator_Project.pdf` | Project documentation (in English). |

## How to run

No third-party packages are needed.

```bash
python main.py
```

On some Linux systems, `tkinter` must be installed separately (for example `sudo apt install python3-tk`).

## Notes

- The interface uses the Vazir font. If it is not installed, `tkinter` falls back to a default font.
- Design idea: build the operations first, then the interface, then connect them, and finally add error handling.
