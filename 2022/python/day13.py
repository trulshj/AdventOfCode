from utils import print_day
from functools import cmp_to_key
from math import prod

DAY = 13


def main():
    print_day(DAY, part1, part2, get_data)


def get_data():
    with open(f"../inputs/day{DAY:02}.txt") as f:
        return [list(map(eval, x.split("\n"))) for x in f.read().split("\n\n")]


def part1(data):
    return sum(idx for idx, (left, right) in enumerate(data, start=1) if compare_packets(left, right) > 0)


def part2(data):
    sorted_packets = sorted([packet for pair in data for packet in pair] + [[[2]], [[6]]],
                            key=cmp_to_key(compare_packets), reverse=True)
    return prod([idx for idx, packet in enumerate(sorted_packets, start=1) if packet in ([[2]], [[6]])])


def compare_packets(left, right):
    left = left if isinstance(left, list) else [left]
    right = right if isinstance(right, list) else [right]
    for l2, r2 in zip(left, right):
        if isinstance(l2, list) or isinstance(r2, list):
            rec = compare_packets(l2, r2)
        else:
            rec = r2 - l2
        if rec != 0:
            return rec
    return len(right) - len(left)


if __name__ == "__main__":
    main()
