# https://adventofcode.com/2023/day/3

from icecream import ic
import argparse
from collections import defaultdict
import re
from typing import List


def parse_input(file_name: str):
    with open(file_name, "r") as f:
        input = f.read().strip().split("\n")

    input = [[c for c in line] for line in input]

    return input


def main() -> int:

    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", help="File name to read")
    args = parser.parse_args()
    file_name = args.file_name

    input = parse_input(file_name)

    ROW_LEN = len(input[0])
    COL_LEN = len(input)

    p1 = 0
    nums = defaultdict(list)
    for r in range(COL_LEN):
        n = 0
        has_part = False
        for c in range(ROW_LEN+1):
            if c < COL_LEN and input[r][c].isdigit():
                n = n*10 + int(input[r][c])
                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        if 0 <= r+rr < COL_LEN and 0 <= c+cc < ROW_LEN:
                            ch = input[r+rr][c+cc]
                            if not ch.isdigit() and ch != ".":
                                has_part = True
            elif n > 0:
                if has_part:
                    p1 += n

                n = 0
                has_part = False

                # numbers_with_indices = get_numbers_with_indices(input)

    return p1


if __name__ == "__main__":
    result = main()
    ic(result)
