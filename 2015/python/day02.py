from math import prod


def part1(data):
    total_area = 0
    for box in data:
        a = box[0] * box[1]
        b = box[0] * box[2]
        c = box[1] * box[2]

        smallest_side = min(a, b, c)
        total_area += (2 * a) + (2 * b) + (2 * c) + smallest_side

    return total_area


def part2(data):
    ribbon = 0
    for box in data:
        ribbon += sum(sorted(box)[:2]) * 2  # Shortest path around the box
        ribbon += prod(box)  # Volume of the box
    return ribbon


def main():
    with open('inputs/day02.txt') as f:
        data = [list(map(int, x.rstrip().split("x"))) for x in f.readlines()]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
