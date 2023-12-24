from typing import List
from icecream import ic
from collections import Counter
import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", help="File name to read")
    file_name = parser.parse_args().file_name

    file = open(file_name, "r").read().strip()

    input = [(line.split()) for line in file.split("\n")]

    new_hands = []
    for hand, bid in input:
        for char in hand:
            if char == "T":
                hand = hand.replace(char, chr(ord("9") + 1))
            elif char == "J":
                hand = hand.replace(char, chr(ord("2") - 1))
            elif char == "Q":
                hand = hand.replace(char, chr(ord("9") + 3))
            elif char == "K":
                hand = hand.replace(char, chr(ord("9") + 4))
            elif char == "A":
                hand = hand.replace(char, chr(ord("9") + 5))
        new_hands.append((hand, bid))

    rank = []

    for hand, bid in new_hands:
        counter = Counter(hand)
        values = sorted(counter.values(), reverse=True)
        # most common not taking into account "1"
        most_common = counter.most_common(2)
        # ic(counter.most_common(2))
        if "1" in hand and values!=[5]:
            ic(hand, values, most_common)
            to_change = most_common[0][0] if most_common[0][0] != "1" else most_common[1][0]
            new_hand = hand.replace(to_change, "1")
            counter = Counter(new_hand)
            values = sorted(counter.values(), reverse=True)

        # ic(hand, values)
        if values == [5]:
            rank.append((hand, 10, bid))
        elif values == [4, 1]:
            rank.append((hand, 9, bid))
        elif values == [3, 2]:
            rank.append((hand, 8, bid))
        elif values == [3, 1, 1]:
            rank.append((hand, 7, bid))
        elif values == [2, 2, 1]:
            rank.append((hand, 6, bid))
        elif values == [2, 1, 1, 1]:
            rank.append((hand, 5, bid))
        elif values == [1, 1, 1, 1, 1]:
            rank.append((hand, 4, bid))
        else:
            rank.append((hand, 0, bid))

    res = 0

    sorted_rank = sorted(rank, key=lambda x: (x[1], x[0]))
    for i, (r, h, b) in enumerate(sorted_rank):
        # ic(i, r, h, b)
        res += (i + 1) * int(b)

    ic(res)


if __name__ == "__main__":
    main()
