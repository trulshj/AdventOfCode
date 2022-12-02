depths = [int(x.rstrip()) for x in open("input01.txt").readlines()]


def part1():
    increasing = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increasing += 1
    return increasing


def part2():
    increasing = 0
    for i in range(3, len(depths)):
        window1 = sum(depths[i - 3 : i])
        window2 = sum(depths[i - 2 : i + 1])
        if window1 < window2:
            increasing += 1
    return increasing


if __name__ == "__main__":
    print("--- AOC Day 01 ---")
    print("Part 1:", part1())
    print("Part 2:", part2())
