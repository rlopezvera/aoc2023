from typing import List
from icecream import ic
import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", help="File name to read")
    file_name = parser.parse_args().file_name

    file = open(file_name, "r").read().strip()
    times, distances = [x.split()[1:] for x in file.split("\n")]
    # starting speed: 0
    ic(times, distances)
    ways = [0] * len(times)
    for i in range(len(times)):
        time_spent_holding = 0
        record = int(distances[i])
        remaining_time = int(times[i])
        total_time = int(times[i])

        total_distance = time_spent_holding * total_time
        tmp_ways = 0

        for j in range(total_time+1):
            if total_distance <= record:
                time_spent_holding += 1
                remaining_time -= 1
                total_distance = time_spent_holding * remaining_time
            else:
                tmp_ways += 1
                time_spent_holding += 1
                remaining_time -= 1
                total_distance = time_spent_holding * remaining_time

        ways[i] = tmp_ways



    p1 = 1
    for x in ways:
        p1 *= x
    ic(p1)

    big_time = "".join(times)
    big_distance = "".join(distances)
    ic(big_time, big_distance)

    time_spent_holding = 0
    record = int(big_distance)
    remaining_time = int(big_time)
    total_time = int(big_time)

    total_distance = time_spent_holding * total_time
    tmp_ways = 0

    for j in range(total_time+1):
        if total_distance <= record:
            time_spent_holding += 1
            remaining_time -= 1
            total_distance = time_spent_holding * remaining_time
        else:
            tmp_ways += 1
            time_spent_holding += 1
            remaining_time -= 1
            total_distance = time_spent_holding * remaining_time

    ic(tmp_ways)



if __name__ == "__main__":
    main()
