#! /usr/bin/env python3

# Advent of Code 23 - Day 08

from pathlib import Path

from tools import readfile


def parse_input(contents: list[str]) -> tuple[list[int], dict]:
    instructions = [
        int(i) for i in list(contents[0].replace("L", "0").replace("R", "1"))
    ]

    reference = dict()
    for line in contents[2:]:
        k, raw_v = line.split(" = ")
        v = tuple(raw_v.strip("()").split(", "))

        reference[k] = v

    return instructions, reference


def p1(contents: list[str]) -> int:
    instructions, reference = parse_input(contents)

    key = "AAA"
    i = 0  # instruction pointer
    while key != "ZZZ":
        idx = instructions[i % len(instructions)]
        key = reference[key][idx]
        i += 1

    return i


def p2(contents: list[str]) -> int:
    ...


if __name__ == "__main__":
    fp = Path("inputs/08.txt")
    # fp = Path("samples/08-1.txt")

    contents = readfile(fp)

    print(p1(contents))  # x=17621
    print(p2(contents))
