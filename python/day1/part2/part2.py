# https://adventofcode.com/2023/day/1

from icecream import ic
import argparse

smarter_way_to_digit = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3hree",
    "four": "f4our",
    "five": "f5ive",
    "six": "s6ix",
    "seven": "s7even",
    "eight": "e8ight",
    "nine": "n9ine"
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
        ic(text)
        tmp = []
        tmp_orders = []

        # 1. replace spelled numbers with digits
        for key, value in smarter_way_to_digit.items():
            text = text.replace(key, value)

        for digit in text:
            if digit.isdigit():
                tmp.append(digit)
                tmp_orders.append(text.index(digit))

        # order is important here
        tmp = [x for _, x in sorted(zip(tmp_orders, tmp))]

        ic(tmp)

        if len(tmp) == 1:
            res.append(int(tmp[0] + tmp[0]))  # 77
        else:
            res.append(int(tmp[0] + tmp[-1]))

    return sum(res)


if __name__ == "__main__":
    result = main()
    ic(result)
