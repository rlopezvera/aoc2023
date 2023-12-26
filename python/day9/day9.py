from icecream import ic
import argparse


def check_all_zero(lst: list) -> bool:
    return all([x == 0 for x in lst])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", help="File name to read")
    file_name = parser.parse_args().file_name

    file = open(file_name, "r").read().strip()
    input = [[int(y) for y in x.split()] for x in file.split("\n")]
    p1 = []
    for history in input:
        tmp = history
        steps = 0
        last_diff = [history[-1]]
        while not check_all_zero(tmp):
            steps += 1
            tmp = [tmp[i] - tmp[i-1]  # type: ignore
                   for i in range(1, len(tmp))]
            last_diff.append(tmp[-1])

        ic(last_diff)
        p1.append(sum(last_diff))
        # break
    ic(sum(p1))


if __name__ == "__main__":
    main()
