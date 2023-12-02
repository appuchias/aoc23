#! /usr/bin/env python3

# Advent of Code 23 - Day 02

from pathlib import Path

from tools import readfile

MAX_CUBES = {"red": 12, "green": 13, "blue": 14}
MIN_CUBES = {"red": 12, "green": 13, "blue": 14}


def get_max_cubes(line: str) -> tuple[int, dict[str, int]]:
    game, content = line.split(":")
    game = int(game[5:])
    maxcubes = {"red": 0, "green": 0, "blue": 0}

    subsets = [s.strip() for s in content.split(";")]

    for subset in subsets:
        cubes = [c.strip() for c in subset.split(",")]

        for cube in cubes:
            amount, color = cube.split(" ")
            amount = int(amount)

            if amount > maxcubes[color]:
                maxcubes[color] = amount

    return game, maxcubes


def p1(contents: list[str]) -> int:
    games = dict(get_max_cubes(line) for line in contents)

    valid_game_ids = []

    for game, maxcubes in games.items():
        if all(maxcubes[color] <= MAX_CUBES[color] for color in maxcubes):
            valid_game_ids.append(game)

    return sum(valid_game_ids)


def p2(contents: list[str]) -> int:
    ...


if __name__ == "__main__":
    import sys

    if sys.argv[1] == "sample":
        fp = Path("samples/02-1.txt")

    fp = Path("inputs/02.txt")

    contents = readfile(fp)

    print(p1(contents))
    print(p2(contents))
