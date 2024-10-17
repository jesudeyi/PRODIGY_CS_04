# Python Keylogger

This Python keylogger logs keystrokes made on a computer and saves them in a log file (`log.txt`). It uses the `pynput` library to capture keyboard events and processes the input to filter out specific keys such as Shift, Ctrl, Alt, and arrow keys.

## Features

- Logs alphanumeric keystrokes
- Replaces special keys with readable symbols (e.g., `[TAB]`, `[BACKSPACE]`, `[CAPS_LOCK]`)
- Outputs the recorded keystrokes into a text file (`log.txt`)
- Handles common keys such as spacebar, enter, and backspace

## How it Works

1. The script listens for keyboard events using the `pynput` library.
2. Keystrokes are processed to remove unwanted key names and replace some with specific strings for clarity.
3. The processed keystrokes are appended to a log file (`log.txt`).

## Installation

1. Install `pynput`:
    ```bash
    pip install pynput
    ```
2. Run the script:
    ```bash
    python keylogger.py
    ```

## Key Mapping

- Space -> `" "`
- Enter -> `"\n"`
- Backspace -> `"[BACKSPACE]"`
- Tab -> `"[TAB]"`
- Arrow Keys:
  - Left -> `"<"`
  - Right -> `">"`
  - Up -> `"[UP]"`
  - Down -> `"[DOWN]"`

## Disclaimer

This keylogger is for educational purposes only. Unauthorized use of this script to capture keystrokes without permission is illegal and unethical. Use it responsibly.


