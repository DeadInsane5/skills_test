# PRD: Binary Clock CLI Utility

## Overview
A single-file Python utility that displays the current time in binary format using ASCII symbols in the terminal.

## Purpose
Convert real-world time into a visual binary representation for educational, decorative, or novelty purposes.

## Requirements

### Core Functionality
- Display current time in binary format (HH:MM:SS)
- Each digit of time rendered as 4-bit binary
- Use ASCII symbols for binary digits:
  - `0` → `□` (empty square)
  - `1` → `■` (filled square)
- Display formats:
  - **Expanded**: Each digit on its own line with label
  - **Compact**: All binary digits on one line
- 18 columns total (6 binary pairs × 3 time components)

### Output Format Examples (for 14:35:29)

Expanded:
```
Time: 14:35:29

1: □■□■□■
4: □□■■■■
3: □■□■■■
5: □■■■■■
2: ■□■■■■
9: ■■■■■■
```

Compact (`--compact` flag):
```
14:35:29 → □■□■□■ □□■■■■ □■□■■■ □■■■■■ ■□■■■■ ■■■■■■
```

### Implementation Details
- Pure Python 3.7+
- Single file: `binary_clock.py`
- No external dependencies
- Uses `datetime` for time, `time` for refresh loop
- Terminal clearing: `os.system('clear')` or `os.system('cls')` for Windows
- CLI: `argparse` with optional `--compact` and `--once` flags

### User Experience
- Default mode: `python binary_clock.py` (continuous, expanded)
- Compact mode: `python binary_clock.py --compact`
- Single display: `python binary_clock.py --once`

### Edge Cases
- Timezone handling (use local time)
- Single-digit hours/mins/seconds (pad with leading zeros)
- Terminal width detection (warn if too narrow for compact)
- EOF handling (Ctrl+C cleanup, restore cursor if needed)

## Technical Notes
- File size target: <200 lines
- Entry point: `if __name__ == "__main__"`
- Testability: Separate `time_to_binary()` and `format_binary()` functions
- No external dependencies

## Success Criteria
- Displays correct binary for known times
- Refreshes cleanly without flicker at 1Hz
- Works on Linux, macOS, Windows
- Single-line command to run
- Both formats work correctly
