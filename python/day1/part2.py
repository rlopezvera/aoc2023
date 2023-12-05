# https://adventofcode.com/2023/day/1

from icecream import ic
import argparse

numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
spelled_numbers = set(["one", "two", "three", "four",
                      "five", "six", "seven", "eight", "nine"])

spelled_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


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
        for spelled_number in spelled_numbers:
            if spelled_number in text:
                tmp.append(spelled_to_digit[spelled_number])
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
