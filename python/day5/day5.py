from icecream import ic
import argparse


def parse_input(file_name: str):
    with open(file_name, "r") as f:
        input = f.read().strip().split("\n")

    return input


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", help="File name to read")
    file_name = parser.parse_args().file_name
    input = parse_input(file_name)
    _, seeds = input[0].split(":")
    seeds = [int(x) for x in seeds.strip().split(" ")]
    # ic(seeds)
    mappings = input[3:]

    id = 0
    tracer = seeds
    xd = []
    for i, line in enumerate(mappings):
        if line == "" or i == len(mappings)-1:
            for i, value in enumerate(tracer):
                for d, s, l in xd:
                    if s <= value < s+l:
                        tracer[i] = d + (value-s)
                        break
            continue
        elif ":" in line:
            # break
            xd = []
            id += 1
            continue
        else:
            destination, source, length = [
                int(x) for x in line.strip().split(" ")]
            xd.append((destination, source, length))

    p1 = min(tracer)
    ic(p1)

    pass


if __name__ == "__main__":
    main()
