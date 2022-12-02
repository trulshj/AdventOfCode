def main():
    with open("../inputs/day01.txt") as f:
        string = f.read()
        elves = [list(map(int, x.split("\n"))) for x in string.split("\n\n")]

    print(part1(elves))
    print(part2(elves))


def part1(elves):
    return max((map(sum, elves)))


def part2(elves):
    return sum(sorted(map(sum, elves), reverse=True)[:3])


if __name__ == "__main__":
    main()
