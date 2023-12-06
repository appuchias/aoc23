#! /usr/bin/env python3

# Advent of Code 23 - Day 06

from pathlib import Path

from tools import readfile


def parse_input(contents: list[str]) -> list[tuple[int, int]]:
    """Parse the input and return a list of tuples of time and distance."""

    times = [int(n) for n in contents[0].split(": ")[1].strip().split(" ") if n]
    distances = [int(n) for n in contents[1].split(": ")[1].strip().split(" ") if n]

    return list(zip(times, distances))


def distance_travelled(time_available: int, time_held: int) -> int:
    """Return the distance travelled in the given time."""

    return (time_available - time_held) * time_held


def p1(contents: list[str]) -> int:
    races = parse_input(contents)

    race_ways_to_win = list()
    for time, record_distance in races:
        ways_to_win = 0
        for held in range(time + 1):
            if distance_travelled(time, held) > record_distance:
                ways_to_win += 1

        race_ways_to_win.append(ways_to_win)

    prod = 1
    for way in race_ways_to_win:
        prod *= way

    return prod


def p2(contents: list[str]) -> int:
    ...


if __name__ == "__main__":
    fp = Path("inputs/06.txt")
    # fp = Path("samples/06-1.txt")

    contents = readfile(fp)

    print(p1(contents))  # 131376
    print(p2(contents))
