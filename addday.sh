#!/bin/sh

echo "#! /usr/bin/env python3

# Advent of Code 23 - Day $1

from pathlib import Path

from tools import readfile


def p1(contents: list[str]) -> int:
    ...


def p2(contents: list[str]) -> int:
    ...


if __name__ == \"__main__\":
    fp = Path(\"inputs/$1.txt\")
    fp = Path(\"samples/$1-1.txt\")
    
    contents = readfile(fp)

    print(p1(contents))
    print(p2(contents))
" >> $1.py

chmod +x $1.py

echo "Created $1.py"

touch inputs/$1.txt
echo "Created inputs/$1.txt"

touch samples/$1-1.txt
echo "Created samples/$1-1.txt"
