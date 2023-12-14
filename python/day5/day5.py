from typing import List
from icecream import ic
import argparse


class Function:
    def __init__(self, S):
        lines = S.split("\n")[1:]  # no name
        # destination, source, length
        self.tuples = [[int(x) for x in line.split()] for line in lines]

    def part_one(self, x: int) -> int:
        for destination, source, length in self.tuples:
            if source <= x < source+length:
                return destination + (x-source)

        return x

    # list of ranges
    def part_two(self, seed_range):
        A = []
        for (destination, source, size) in self.tuples:
            source_end = source + size
            new_range = []
            while seed_range:
                start, end = seed_range.pop(0)
                before = (start, min(source, end))
                inter = (max(start, source), min(source_end, end))
                after = (max(source_end, start), end)
                if before[0] < before[1]:
                    new_range.append(before)
                if inter[0] < inter[1]:
                    A.append((inter[0]-source+destination,
                             inter[1]-source+destination))
                if after[0] < after[1]:
                    new_range.append(after)
            seed_range = new_range

        return seed_range + A


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", help="File name to read")
    file_name = parser.parse_args().file_name

    file = open(file_name, "r").read().strip()
    L = file.split('\n')

    parts = file.split('\n\n')
    seed, *others = parts
    seed = [int(x) for x in seed.split(':')[1].split()]
    p1 = []
    fs = [Function(x) for x in others]

    for x in seed:
        for f in fs:
            x = f.part_one(x)
        p1.append(x)
    ic(min(p1))

    p2 = []
    pairs = list(zip(seed[::2], seed[1::2]))
    for start, size in pairs:
        R = [(start, start+size)]
        for f in fs:
            R = f.part_two(R)
        p2.append(min(R)[0])
    ic(min(p2))

    # ic(seed)
    # ic(others)

    pass


if __name__ == "__main__":
    main()
