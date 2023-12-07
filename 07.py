#! /usr/bin/env python3

# Advent of Code 23 - Day 07

from pathlib import Path

from tools import readfile


def p1(contents: list[str]) -> int:
    ...


def p2(contents: list[str]) -> int:
    ...


if __name__ == "__main__":
    fp = Path("inputs/07.txt")
    fp = Path("samples/07-1.txt")
    
    contents = readfile(fp)

    print(p1(contents))
    print(p2(contents))

