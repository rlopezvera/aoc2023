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
    mappings = input[2:]

    id = 0
    tracer = seeds
    mapping = {}
    for i, line in enumerate(mappings):
        if line == "":
            # ic(mapping)
            ic(tracer)
            for i, value in enumerate(tracer):
                # ic(value)
                if value in mapping.keys():
                    tracer[i] = mapping[value]
                else:
                    tracer[i] = value
            mapping = {}

            continue
        elif ":" in line:
            id += 1
            continue
        else:
            destination, source, length = [
                int(x) for x in line.strip().split(" ")]
            destination_range = range(destination, destination+length)
            source_range = range(source, source+length)
            for d, s in zip(destination_range, source_range):
                mapping[s] = d
    ic(tracer)
    ic(min(tracer))

    pass


if __name__ == "__main__":
    main()
