#!/bin/sh

echo "#! /usr/bin/env python3

# Advent of Code 23 - Day $1" > $1.py

chmod +x $1.py

echo "Created $1.py"

touch inputs/$1.txt
echo "Created inputs/$1.txt"

touch samples/$1-1.txt
echo "Created samples/$1-1.txt"
