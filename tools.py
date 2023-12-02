#! /usr/bin/env python3

# Advent of Code 23 - Tools
# Appuchia <appuchia@appu.ltd>

from pathlib import Path


def readfile(fp: Path) -> list[str]:
    with open(fp, "r") as f:
        return [line.strip() for line in f.readlines()]
