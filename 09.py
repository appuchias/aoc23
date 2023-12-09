#! /usr/bin/env python3

# Advent of Code 23 - Day 09

from pathlib import Path

from tools import readfile


def parse_input(contents: list[str]) -> list[list[int]]:
    return [[int(i) for i in line.split(" ")] for line in contents]


def find_bd(history: list[int]) -> list[int]:
    """A backward difference kind of thing"""

    bd = list()

    for i in range(1, len(history)):
        bd.append(history[i] - history[i - 1])

    return bd


def p1(contents: list[str]) -> int:
    histories = parse_input(contents)

    predictions = list()
    for history in histories:
        bds = list()
        last_seq = history

        # find all the backward differences
        while any(last_seq):
            last_seq = find_bd(last_seq)
            bds.append(last_seq)

        bds.pop()  # remove the last one, which is all 0s

        # add up the last values of each bd to get the prediction
        val_to_add = 0
        for bd in reversed(bds):
            val_to_add += bd[-1]

        predictions.append(history[-1] + val_to_add)

    return sum(predictions)


def p2(contents: list[str]) -> int:
    ...


if __name__ == "__main__":
    fp = Path("inputs/09.txt")
    # fp = Path("samples/09-1.txt")

    contents = readfile(fp)

    print(p1(contents))  # x=2101499000
    print(p2(contents))
