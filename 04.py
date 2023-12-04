#! /usr/bin/env python3

# Advent of Code 23 - Day 03

from pathlib import Path

from tools import readfile


def get_winning_numbers(line: str) -> list[int]:
    winners_str, _ = line.split("|")

    winners = [int(w) for w in winners_str.split(":")[1].split(" ") if w]

    return winners


def get_my_numbers(line: str) -> list[int]:
    _, my_numbers_str = line.split("|")

    my_numbers = [int(n) for n in my_numbers_str.split(" ") if n]

    return my_numbers


def points_for_game(game: tuple[list[int], list[int]]) -> int:
    winners, my_numbers = game
    points = 0

    for number in my_numbers:
        if number in winners:
            if not points:
                points = 1
                continue

            points *= 2

    return points


def p1(contents: list[str]) -> int:
    winners = [get_winning_numbers(line) for line in contents]
    my_numbers = [get_my_numbers(line) for line in contents]

    games = list(zip(winners, my_numbers))

    all_points = [points_for_game(game) for game in games]

    return sum(all_points)


def p2(contents: list[str]) -> int:
    winners = [get_winning_numbers(line) for line in contents]
    my_numbers = [get_my_numbers(line) for line in contents]

    games = list(zip(winners, my_numbers))
    games = dict(zip(range(1, len(games) + 1), games))
    # Diccionario id: (winners, my_numbers)

    game_count = 0
    new_games = list(games.keys())

    while len(new_games) > 1:
        for game_id in new_games.copy():
            new_games.remove(game_id)
            game_count += 1

            numbers = games[game_id]

            points = points_for_game(numbers)

            if points:
                new_game_ids = range(game_id + 1, game_id + points + 1)
                new_game_ids = filter(lambda x: x <= len(games), new_game_ids)
                new_games.extend(new_game_ids)

    return game_count


if __name__ == "__main__":
    fp = Path("inputs/04.txt")
    # fp = Path("samples/04-1.txt")

    contents = readfile(fp)

    print(p1(contents))
    print(p2(contents))
