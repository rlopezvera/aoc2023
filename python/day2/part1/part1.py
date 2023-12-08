# https://adventofcode.com/2023/day/2

from icecream import ic
import argparse
from typing import List

bag_dict = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


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

    impossible_ids: List[int] = []

    for sets in games:
        for single_set in sets:
            splitted = single_set.strip().split(", ")
            for ammount, color in [x.split(" ") for x in splitted]:
                if bag_dict[color] < int(ammount):
                    impossible_ids.append(int(ids[games.index(sets)]))
                    break

    possible_ids = [int(id) for id in ids if int(id) not in impossible_ids]

    return sum(possible_ids)


if __name__ == "__main__":
    result = main()
    ic(result)
