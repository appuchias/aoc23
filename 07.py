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
    """Returns a list of hands from the input file"""

    hands = list()

    for line in contents:
        cards, bid = line.split(" ")
        hands.append(Hand(cards, int(bid)))

    return hands


def value_hand(hand: Hand) -> int:
    """
    Returns the value of the hand, the value is a number between 0 and 6
    representing the type of hand. (No special meaning)

    0: High card
    1: One pair
    2: Two pairs
    3: Three of a kind
    4: Full house
    5: Four of a kind
    6: Flush
    """

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


def value_hand_jokers(hand: Hand) -> int:
    """
    The joker is a wildcard, it can be swapped for any other card in the deck
    to make the best possible hand.

    The joker is swapped for the most repeated card in the hand, if there are
    no repeated cards in the hand, the joker is swapped for the lowest card in
    the deck (2).
    """

    if "J" not in hand.cards:
        return value_hand(hand)

    cards = sorted(hand.cards, key=lambda x: hand.cards.count(x), reverse=True)
    unique_cards = list(dict.fromkeys(cards))

    # Swap joker for most repeated card
    swap = "2"
    for card in unique_cards:
        if card != "J":
            swap = card
            break

    hand.value = value_hand(Hand(hand.cards.replace("J", swap), 0))
    return hand.value


def p1(contents: list[str]) -> int:
    hands = parse_input(contents)

    for hand in hands:
        value_hand(hand)

    ranked = list(sorted(hands))

    winnings = 0
    for idx, hand in enumerate(ranked):
        winnings += hand.bid * (idx + 1)

    return winnings


def p2(contents: list[str]) -> int:
    # I know I shouldn't, this would't be needed if I didn't use separate
    # functions for p1 and p2 but here it is for your viewing pleasure
    global ORDER
    ORDER = "J23456789TQKA"  # Joker is now the lowest card

    hands = parse_input(contents)

    for hand in hands:
        value_hand_jokers(hand)

    ranked = list(sorted(hands))

    winnings = 0
    for idx, hand in enumerate(ranked):
        winnings += hand.bid * (idx + 1)

    return winnings


if __name__ == "__main__":
    fp = Path("inputs/07.txt")
    # fp = Path("samples/07-1.txt")

    contents = readfile(fp)

    print(p1(contents))  # 250261210 < x=250957639 < 251213099 < 253101825
    print(p2(contents))  # x=251515496 < 252558854
