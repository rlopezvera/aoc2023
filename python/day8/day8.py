from icecream import ic
import argparse

import math

def main(part1: bool) -> None:
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

    direction = rl_map[instructions[0]]
    p2_keys = [x for x in mapping.keys() if x.endswith("A")]
    ic(p2_keys)
    if part1:
        found = False
        p1 = 0
        key = "AAA"
        while not found:
            new_key = mapping[key][direction]
            p1 += 1
            # ic(new_key)
            if new_key == "ZZZ":
                found = True
                ic(p1)
            else:
                key = new_key
                direction = rl_map[instructions[p1 % len(instructions)]]
    else:
        p2_lst = []
        for i, key in enumerate(p2_keys):
            direction = rl_map[instructions[0]]
            found = False
            p2 = 0
            # ic(i, key)
            while not found:
                p2 += 1
                new_key = mapping[key][direction]
                # ic(new_key)
                if new_key.endswith("Z"):
                    p2_lst.append(p2)
                    found = True
                    # ic(p2)
                else:
                    key = new_key
                    direction = rl_map[instructions[p2 % len(instructions)]]
        ic(p2_lst)
        ic(math.lcm(*p2_lst))


if __name__ == "__main__":
    main(part1=False)
