"""Advent of code 2022 - Day 6"""

from pathlib import Path

def main():
    fin = "input/6.txt"
    stream = Path(fin).read_text()
    print(f"Day 6, part 1: {_find(stream, 4)}")
    print(f"Day 6, part 2: {_find(stream, 14)}")


def _read_data(fin):
    with open(fin, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    return lines

def _find(stream, unique):
    """Return when first sequence of unique characters is seen"""

    for c, char in enumerate(stream[unique-1:]):
        if len(set(stream[c:c+unique])) == unique:
            return c+unique

if __name__ == "__main__":
    main()