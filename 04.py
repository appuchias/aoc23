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
    # Dict: {id: (winners, my_numbers)}

    # Dict: {id: count}
    cards = {k: 1 for k in base_cards.keys()}
    total_card_count = 0

    while len(cards) > 1:
        cards_to_add = dict()

        # Iterate over the card ids
        for card_id, card_count in cards.items():
            total_card_count += card_count

            # Get points for the card id
            points = points_for_card(base_cards[card_id])

            if points:
                # Get the card ids that need to be added
                new_game_ids = range(card_id + 1, card_id + points + 1)

                # Prevent out of bounds
                new_game_ids = filter(lambda x: x <= len(base_cards), new_game_ids)

                # Set new card counts
                for new_game_id in new_game_ids:
                    if new_game_id not in cards_to_add:
                        cards_to_add[new_game_id] = 0

                    cards_to_add[new_game_id] += card_count

        cards = cards_to_add

        print("", total_card_count, len(cards_to_add))

    return total_card_count


if __name__ == "__main__":
    fp = Path("inputs/04.txt")
    # fp = Path("samples/04-1.txt")

    contents = readfile(fp)

    print(p1(contents))
    print(p2(contents))

# x < 83146687209054963286543604131605810512
