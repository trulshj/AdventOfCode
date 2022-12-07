from utils import print_day
from collections import defaultdict
from typing import Any
from itertools import accumulate

DAY = 7


def main():
    print_day(DAY, part1, part2, get_data)


def get_data():
    with open(f"../inputs/day{DAY:02}.txt") as f:
        return [x.rstrip() for x in f.readlines()]


def part1(data: list[str]):
    return sum(size for size in find_directory_sizes(data).values() if size <= 100_000)


def part2(data: list[str]):
    directory_sizes = find_directory_sizes(data)
    return min(size for size in directory_sizes.values() if size >= directory_sizes['/'] - 40_000_000)


def find_directory_sizes(data: list[str]):
    current_path = []
    directory_sizes = defaultdict(int)

    for line in data:
        match line.split():
            case '$', 'cd', '/': current_path = ['/']
            case '$', 'cd', '..': current_path.pop()
            case '$', 'cd', target: current_path.append(target)
            case '$', 'ls': pass
            case 'dir', _: pass
            case size, _:
                for path in accumulate(current_path):
                    directory_sizes[path] += int(size)

    return directory_sizes


if __name__ == "__main__":
    main()
