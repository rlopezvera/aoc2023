from icecream import ic
import argparse
from collections import defaultdict
import re
from typing import List


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", help="File name to read")
    args = parser.parse_args()
    file_name = args.file_name
    with open(file_name, "r") as f:
        input = f.read().strip().split("\n")

    counter = defaultdict(int)
    p1 = 0
    for i, line in enumerate(input):
        first, rest = line.split("|")
        id_, card = first.split(":")
        card_nums = [int(x) for x in card.split()]
        user_cards = [int(x) for x in rest.split()]
        val = len(set(card_nums) & set(user_cards))
        if val > 0:
            p1 += 2**(val-1)
    ic(p1)

    return


if __name__ == "__main__":
    res = main()
