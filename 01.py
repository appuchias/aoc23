#! /usr/bin/env python3

# Advent of Code 23 - Day 01

from pathlib import Path

NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_calibration(fp: Path) -> list[str]:
    with open(fp, "r") as f:
        return [line.strip() for line in f.readlines()]


def get_first_and_last_numbers(line: str) -> int:
    numbers = [int(c) for c in line if c.isdigit()]

    if not numbers:
        return 0

    return int(f"{numbers[0]}{numbers[-1]}")


def swap_typed_numbers(line: str) -> str:
    # for i in range(len(line)):
    #     for j in range(i):
    #         seq = line[j:i]

    #         if seq in numbers:
    #             line = line.replace(seq, str(numbers[seq]))

    # for i in range(len(line) + 1):
    #     for j in range(i):
    #         seq = line[j:i]

    #         if seq in numbers:
    #             line = line.replace(seq, str(numbers[seq]))

    i = 2
    j = 0
    while i <= len(line):
        for j in range(max(0, i - 5), i - 2):
            seq = line[j:i]

            if seq in NUMBERS:
                line = line.replace(seq, str(NUMBERS[seq]))
                i -= len(seq) - 1

        i += 1

    return line


def p1(contents: list[str]) -> int:
    total = 0

    for line in contents:
        total += get_first_and_last_numbers(line)

    return total


def p2(contents: list[str]) -> int:
    total = 0

    missed = 0

    for line in contents:
        line = swap_typed_numbers(line)
        number = get_first_and_last_numbers(line)
        total += number

        print(number, line)

        for num in NUMBERS:
            if num in line:
                missed += 1

    print(missed)

    return total


if __name__ == "__main__":
    fp = Path("inputs/1.txt")
    # fp = Path("samples/1-1.txt")

    contents = get_calibration(fp)

    print(p1(contents))

    # contents = get_calibration(Path("samples/1-2.txt"))

    print(p2(contents))

# 52653 < x < 54325
