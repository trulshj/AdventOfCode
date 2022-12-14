import utils
from string import ascii_letters


def main():
    utils.print_day(3, part1, part2, get_data)


def parse_rucksack(line: str) -> tuple[str, str]:
    line = line.rstrip()
    middle = len(line) // 2
    return (line[:middle], line[middle:])


def get_data():
    with open("../inputs/day03.txt") as f:
        return [parse_rucksack(line) for line in f.readlines()]


def part1(rucksacks: list[tuple[str, str]]):
    return sum(get_item_priority(find_common_item(rucksack)) for rucksack in rucksacks)


def part2(rucksacks: list[tuple[str, str]]):
    groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
    return sum(get_item_priority(find_group_item(group)) for group in groups)


def find_common_item(rucksack: tuple[str, str]):
    a = set(rucksack[0])
    b = set(rucksack[1])
    return a.intersection(b).pop()


def find_group_item(group: list[tuple[str, str]]):
    a, b, c = list(map(lambda x: set(x[0] + x[1]), group))
    return a.intersection(b).intersection(c).pop()


def get_item_priority(item: str):
    return ascii_letters.index(item) + 1


if __name__ == "__main__":
    main()
