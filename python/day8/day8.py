from icecream import ic
import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", help="File name to read")
    file_name = parser.parse_args().file_name

    file = open(file_name, "r").read().strip()
    input = file.split("\n")
    instructions, pairs = input[0], input[2:]
    rl_map = {"R": 1, "L": 0}
    # ic(pairs)
    mapping = {pair.split(" = ")[0]:
               tuple(pair.split(" = ")[1].replace(")", "").replace("(", "").split(", ")) for pair in pairs}
    # ic(mapping)

    found = False
    res = 0
    direction = rl_map[instructions[0]]
    key = "AAA"
    while not found:
        new_key = mapping[key][direction]
        res += 1
        # ic(new_key)
        if new_key == "ZZZ":
            found = True
            ic(res)
        else:
            key = new_key
            direction = rl_map[instructions[res % len(instructions)]]


if __name__ == "__main__":
    main()
