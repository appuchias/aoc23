#! /usr/bin/env python3

# Advent of Code 23 - Day 03

from pathlib import Path

from tools import readfile

Card = tuple[list[int], list[int]]


def get_winning_numbers(line: str) -> list[int]:
    winners_str, _ = line.split("|")

    winners = [int(w) for w in winners_str.split(":")[1].split(" ") if w]

    return winners


def get_my_numbers(line: str) -> list[int]:
    _, my_numbers_str = line.split("|")

    my_numbers = [int(n) for n in my_numbers_str.split(" ") if n]

    return my_numbers


def points_for_card(card: Card) -> int:
    winners, my_numbers = card
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

    cards = list(zip(winners, my_numbers))

    all_points = [points_for_card(card) for card in cards]

    return sum(all_points)


def p2(contents: list[str]) -> int:
    winners = [get_winning_numbers(line) for line in contents]
    my_numbers = [get_my_numbers(line) for line in contents]
    base_cards = dict(
        zip(range(1, len(my_numbers) + 1), list(zip(winners, my_numbers)))
    )
    # Diccionario: {id: (winners, my_numbers)}

    card_count = 0
    cards = list(base_cards.keys())

    while len(cards) > 1:
        cards_to_add = list()
        for card_id in cards:
            cards.remove(card_id)
            card_count += 1

            points = points_for_card(base_cards[card_id])

            if points:
                new_game_ids = range(card_id + 1, card_id + points + 1)
                new_game_ids = filter(lambda x: x <= len(base_cards), new_game_ids)
                cards_to_add.extend(new_game_ids)

        cards.extend(cards_to_add)

        # print(" ", card_count, len(cards))

    return card_count


if __name__ == "__main__":
    fp = Path("inputs/04.txt")
    fp = Path("samples/04-1.txt")

    contents = readfile(fp)

    print(p1(contents))
    print(p2(contents))
