
def parse_line(line_string):
    return [tuple(map(int, x.split(','))) for x in line_string.split(' -> ')]


def is_vertical(line):
    return line[0][0] == line[1][0]


def is_horizontal(line):
    return line[0][1] == line[1][1]


def draw_vertical(ocean_floor, line):
    x = line[0][0]
    y1 = min(line[0][1], line[1][1])
    y2 = max(line[0][1], line[1][1])
    for y in range(y1, y2+1):
        ocean_floor[y][x] += 1
    return ocean_floor


def draw_horizontal(ocean_floor, line):
    y = line[0][1]
    x1 = min(line[0][0], line[1][0])
    x2 = max(line[0][0], line[1][0])
    for x in range(x1, x2+1):
        ocean_floor[y][x] += 1
    return ocean_floor


def draw_diagonal(ocean_floor, line):
    x1 = min(line[0][0], line[1][0])
    x2 = max(line[0][0], line[1][0])
    if x1 == line[0][0]:
        y1 = line[0][1]
        y2 = line[1][1]
    else:
        y1 = line[1][1]
        y2 = line[0][1]

    for i, x in enumerate(range(x1, x2+1)):
        if y1 >= y2:
            ocean_floor[y1-i][x] += 1
        else:
            ocean_floor[y1+i][x] += 1

    return ocean_floor


def part1(data):
    x_max = max(max([line[0][0] for line in data]),
                max([line[1][0] for line in data])) + 1
    y_max = max(max([line[0][1] for line in data]),
                max([line[1][1] for line in data])) + 1

    ocean_floor = [[0 for _ in range(x_max)] for _ in range(y_max)]

    for line in data:
        if is_vertical(line):
            ocean_floor = draw_vertical(ocean_floor, line)
        elif is_horizontal(line):
            ocean_floor = draw_horizontal(ocean_floor, line)

    dangerous_vents = 0
    for row in range(y_max):
        for col in range(x_max):
            if ocean_floor[row][col] >= 2:
                dangerous_vents += 1

    return dangerous_vents


def part2(data):
    x_max = max(max([line[0][0] for line in data]),
                max([line[1][0] for line in data])) + 1
    y_max = max(max([line[0][1] for line in data]),
                max([line[1][1] for line in data])) + 1

    ocean_floor = [[0 for _ in range(x_max)] for _ in range(y_max)]

    for line in data:
        if is_vertical(line):
            ocean_floor = draw_vertical(ocean_floor, line)
        elif is_horizontal(line):
            ocean_floor = draw_horizontal(ocean_floor, line)
        else:
            ocean_floor = draw_diagonal(ocean_floor, line)

    dangerous_vents = 0
    for row in range(y_max):
        for col in range(x_max):
            if ocean_floor[row][col] >= 2:
                dangerous_vents += 1

    return dangerous_vents


if __name__ == "__main__":
    data = [parse_line(x.rstrip()) for x in open("input05.txt").readlines()]

    print("--- AOC Day 05 ---")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
