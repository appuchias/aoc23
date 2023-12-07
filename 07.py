#! /usr/bin/env python3

# Advent of Code 23 - Day 07

from pathlib import Path

from tools import readfile

ORDER = "23456789TJQKA"


class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
        self.value = 0

    def __gt__(self, other) -> bool:
        if self.value != other.value:
            return self.value > other.value

        for idx, card in enumerate(self.cards):
            if ORDER.index(card) > ORDER.index(other.cards[idx]):
                return True
            elif ORDER.index(card) < ORDER.index(other.cards[idx]):
                return False

        return False

    def __repr__(self) -> str:
        return f"Hand({self.cards}, {self.bid}, {self.value})"


def parse_input(contents: list[str]) -> list[Hand]:
    hands = list()

    for line in contents:
        cards, bid = line.split(" ")
        hands.append(Hand(cards, int(bid)))

    return hands


def value_hand(hand: Hand) -> int:
    cards = sorted(hand.cards, key=lambda x: hand.cards.count(x), reverse=True)
    unique_cards = list(dict.fromkeys(cards))
    unique = len(unique_cards)
    most_repeated = unique_cards[0]

    # Flush
    if hand.cards.count(most_repeated) == 5:
        hand.value = 6
    # Four of a kind
    elif hand.cards.count(most_repeated) == 4:
        hand.value = 5
    # Full house
    elif hand.cards.count(most_repeated) == 3 and unique == 2:
        hand.value = 4
    # Three of a kind
    elif hand.cards.count(most_repeated) == 3 and unique > 2:
        hand.value = 3
    # Two pairs
    elif hand.cards.count(most_repeated) == 2 and unique == 3:
        hand.value = 2
    # One pair
    elif hand.cards.count(most_repeated) == 2 and unique == 4:
        hand.value = 1
    # High card
    else:
        hand.value = 0

    return hand.value


def p1(contents: list[str]) -> int:
    hands = parse_input(contents)

    for hand in hands:
        value_hand(hand)

    ranked = list(sorted(hands))

    print(ranked)

    winnings = 0
    for idx, hand in enumerate(ranked):
        winnings += hand.bid * (idx + 1)

    return winnings


def p2(contents: list[str]) -> int:
    ...


if __name__ == "__main__":
    fp = Path("inputs/07.txt")
    # fp = Path("samples/07-1.txt")

    contents = readfile(fp)

    print(p1(contents))  # 250261210 < x=250957639 < 251213099 < 253101825
    print(p2(contents))
