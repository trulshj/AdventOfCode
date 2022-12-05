import re
from utils import print_day


def main():
    print_day(4, part1, part2, get_data)


def get_data():
    with open("../inputs/day04.txt") as f:
        return [tuple(map(int, re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line).groups())) for line in f.readlines()]


def part1(pairs: list[tuple[int, int, int, int]]):
    return sum(map(lambda pair: is_fully_contained(*pair), pairs))


def part2(pairs: list[tuple[int, int, int, int]]):
    return sum(map(lambda pair: has_overlap(*pair), pairs))


def is_fully_contained(a, b, c, d):
    if a <= c and b >= d:
        return True

    if c <= a and d >= b:
        return True

    return False


def has_overlap(a, b, c, d):
    if a <= c and b >= c:
        return True

    if c <= a and d >= a:
        return True

    return False


if __name__ == "__main__":
    main()
