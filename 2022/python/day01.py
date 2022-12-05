import utils


def main():
    utils.print_day(1, part1, part2, get_data)


def get_data():
    with open("../inputs/day01.txt") as f:
        string = f.read()
        return [list(map(int, x.split("\n"))) for x in string.split("\n\n")]


def part1(elves):
    return max((map(sum, elves)))


def part2(elves):
    return sum(sorted(map(sum, elves), reverse=True)[:3])


if __name__ == "__main__":
    main()
