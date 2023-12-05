#! /usr/bin/env python3

# Advent of Code 23 - Day 05

from pathlib import Path
from typing import NamedTuple

from tools import readfile

Sections = tuple[tuple[int], tuple, tuple, tuple, tuple, tuple, tuple, tuple]

Mapping = NamedTuple(
    "Mapping", [("dst_start", int), ("src_start", int), ("length", int)]
)


def parse_sections(contents: list[str]) -> Sections:
    """
    Parse the sections of the input file.

    Returns:
    --------
    A tuple containing the parsed sections of the input file in the following order:
        - seeds (`list[str]`): The seeds to plant.
        - seed_to_soil (`list[list[str]]`): The seeds to soil mapping.
        - soil_to_fertilizer (`list[list[str]]`): The soil to fertilizer mapping.
        - fertilizer_to_water (`list[list[str]]`): The fertilizer to water mapping.
        - water_to_light (`list[list[str]]`): The water to light mapping.
        - light_to_temperature (`list[list[str]]`): The light to temperature mapping.
        - temperature_to_humidity (`list[list[str]]`): The temperature to humidity mapping.
        - humidity_to_location (`list[list[str]]`): The humidity to location mapping.
    """

    allcontents = "\n".join(contents)

    sections = allcontents.split("\n\n")

    parsed_sections = list()

    parsed_sections.append([int(n) for n in sections[0].split(": ")[1].split(" ")])

    for section in sections[1:]:
        section_list = list()
        for line in section.split("\n")[1:]:
            section_list.append(Mapping(*(int(n) for n in line.split(" "))))

        parsed_sections.append(section_list)

    return tuple(parsed_sections)  # type: ignore


def map_idx(idx: int, mapping: Mapping) -> int:
    """Map an index to a new index based on a mapping."""

    # If index in range, map it
    if mapping.src_start <= idx < mapping.src_start + mapping.length:
        return mapping.dst_start + (idx - mapping.src_start)

    return idx


def p1(contents: list[str]) -> int:
    sections = parse_sections(contents)

    seeds: tuple[int] = sections[0]
    sections: tuple = sections[1:]

    # Map seeds to locations through all mappings
    locations = list()
    for idx in seeds:
        for section in sections:
            for mapping in section:
                newidx = map_idx(idx, mapping)
                if newidx != idx:
                    idx = newidx
                    break

        locations.append(idx)

    return min(locations)


def p2(contents: list[str]) -> int:
    sections = parse_sections(contents)

    raw_seeds: tuple[int] = sections[0]
    sections: tuple = sections[1:]

    seed_ranges = list()
    # Add ranges starting in raw_seeds[i] with length raw_seeds[i+1]
    for i in range(0, len(raw_seeds), 2):
        start = raw_seeds[i]
        end = raw_seeds[i] + raw_seeds[i + 1]
        seed_ranges.append(range(start, end))

    print("Seed ranges:", seed_ranges)

    # Map seeds to locations through all mappings
    locations = list()
    for seed_range in seed_ranges:
        print(" ", seed_range)

        for idx in seed_range:
            print("  ", idx)

            # Map index through all mappings
            for section in sections:
                for mapping in section:
                    newidx = map_idx(idx, mapping)
                    if newidx != idx:
                        idx = newidx
                        break

            locations.append(idx)

    return min(locations)


if __name__ == "__main__":
    fp = Path("inputs/05.txt")
    fp = Path("samples/05-1.txt")

    contents = readfile(fp)

    print(p1(contents))  # 324724204
    print(p2(contents))
