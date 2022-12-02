def part1(data):
    floor = 0
    for c in data:
        if c == '(':
            floor += 1
        else:
            floor -= 1
    return floor


def part2(data):
    floor = 0
    for idx, c in enumerate(data, start=1):
        if c == '(':
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            return idx


def main():
    with open("../inputs/day01.txt") as f:
        data = [x for x in f.readline()]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
