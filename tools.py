#! /usr/bin/env python3

# Advent of Code 23 - Tools
# Appuchia <appuchia@appu.ltd>

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def get_neighbors(self) -> list["Point"]:
        return [
            Point(self.x - 1, self.y),
            Point(self.x + 1, self.y),
            Point(self.x, self.y - 1),
            Point(self.x, self.y + 1),
        ]

    def get_surronding(self) -> list["Point"]:
        return self.get_neighbors() + [
            Point(self.x - 1, self.y - 1),
            Point(self.x + 1, self.y - 1),
            Point(self.x - 1, self.y + 1),
            Point(self.x + 1, self.y + 1),
        ]


def readfile(fp: Path) -> list[str]:
    with open(fp, "r") as f:
        return [line.strip() for line in f.readlines()]
