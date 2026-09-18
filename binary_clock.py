#!/usr/bin/env python3
"""Binary clock utility - displays current time in binary format using ASCII symbols."""

import argparse
import os
import sys
import time
from datetime import datetime


EMPTY = '□'
FULL = '■'


def int_to_binary_str(n):
    """Convert integer 0-9 to 4-bit binary string using □ and ■."""
    bits = []
    for i in range(3, -1, -1):
        if n & (1 << i):
            bits.append(FULL)
        else:
            bits.append(EMPTY)
    return ''.join(bits)


def get_time_binary():
    """Get current time, return dict with each component as list of 2 digits."""
    now = datetime.now()
    time_str = now.strftime('%H:%M:%S')
    h, m, s = time_str.split(':')
    return {
        'H': [int(h[0]), int(h[1])],
        'M': [int(m[0]), int(m[1])],
        'S': [int(s[0]), int(s[1])],
        'raw': time_str
    }


def format_expanded(time_data):
    """Format time in expanded view: each digit on its own line."""
    lines = [f"Time: {time_data['raw']}", ""]
    for digit, value in time_data.items():
        if digit == 'raw':
            continue
        for d in value:
            lines.append(f"{d}: {int_to_binary_str(d)}")
    return '\n'.join(lines)


def format_compact(time_data):
    """Format time in compact view: all binary on one line."""
    binary_parts = []
    for digit in ['H', 'M', 'S']:
        for d in time_data[digit]:
            binary_parts.append(int_to_binary_str(d))
    return f"{time_data['raw']} → {' '.join(binary_parts)}"


def clear_terminal():
    """Clear terminal screen using appropriate command for OS."""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        pass


def main():
    parser = argparse.ArgumentParser(description='Display current time in binary format.')
    parser.add_argument('--compact', action='store_true', help='Show compact single-line output')
    parser.add_argument('--once', action='store_true', help='Show time once and exit')
    args = parser.parse_args()

    try:
        while True:
            clear_terminal()
            time_data = get_time_binary()
            
            if args.compact:
                print(format_compact(time_data))
            else:
                print(format_expanded(time_data))
            
            if args.once:
                break
            
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()
