import itertools
import math


def find_balance(data, parts):
    target = sum(data) // parts

    for i in range(1, len(data)):
        for comb in itertools.combinations(data, i):
            if sum(comb) == target:
                return math.prod(comb)


def part1(data):
    return find_balance(data, 3)


def part2(data):
    return find_balance(data, 4)


def main():
    with open('inputs/day24.txt') as f:
        data = [int(x.rstrip()) for x in f.readlines()]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
