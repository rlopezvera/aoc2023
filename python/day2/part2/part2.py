# https://adventofcode.com/2023/day/2

from icecream import ic
import argparse
from typing import List


def parse_input(file_name: str):
    with open(file_name, "r") as f:
        input = f.readlines()

    input = [line.strip().split(":") for line in input]
    ids = [line[0].split(" ")[1] for line in input]
    games = [line[1].strip().split(";") for line in input]
    ic(ids)
    ic(games)

    return ids, games


def main() -> int:

    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", help="File name to read")
    args = parser.parse_args()
    file_name = args.file_name

    ids, games = parse_input(file_name)

    powers: List[int] = []

    for sets in games:

        # reset the min bag dict
        min_bag_dict = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for single_set in sets:
            splitted = single_set.strip().split(", ")
            for ammount, color in [x.split(" ") for x in splitted]:
                min_bag_dict[color] = max(min_bag_dict[color], int(ammount))

        powers.append(min_bag_dict["red"] *
                      min_bag_dict["green"] * min_bag_dict["blue"])

    return sum(powers)


if __name__ == "__main__":
    result = main()
    ic(result)
