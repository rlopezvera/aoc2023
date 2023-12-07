# https://adventofcode.com/2023/day/1

from icecream import ic
import argparse

numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
spelled_numbers = set(["one", "two", "three", "four",
                      "five", "six", "seven", "eight", "nine"])


def main() -> int:

    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", help="File name to read")
    args = parser.parse_args()

    file_name = args.file_name

    with open(file_name, "r") as f:
        input = f.readlines()
        input = [line.strip() for line in input]

    res = []

    for text in input:
        tmp = []
        for digit in text:
            if digit.isdigit():
                tmp.append(digit)

        if len(tmp) == 1:
            res.append(int(tmp[0] + tmp[0]))  # 77
        else:
            res.append(int(tmp[0] + tmp[-1]))

    return sum(res)


if __name__ == "__main__":
    result = main()
    ic(result)
