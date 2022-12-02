from math import prod


def find_neighbours(row, col, data):
    neighbours = []

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        neighbour_x = col + dx
        neighbour_y = row + dy

        if 0 <= neighbour_x < len(data[0]) and 0 <= neighbour_y < len(data):
            neighbours.append((neighbour_y, neighbour_x))

    return neighbours


def calc_risk(row, col, data):
    height = data[row][col]
    heights = [data[r][c] for r, c in find_neighbours(row, col, data)]

    if height < min(heights):
        return height + 1

    return 0


def part1(data):
    risk_levels = 0
    for row in range(len(data)):
        for col in range(len(data[0])):
            risk_levels += calc_risk(row, col, data)
    return risk_levels


def part2(data):
    basins = []
    low_points = []
    for row in range(len(data)):
        for col in range(len(data[0])):
            if calc_risk(row, col, data) != 0:
                low_points.append((row, col))

    for low_point in low_points:
        queue = [low_point]
        visited = set()
        while len(queue) > 0:
            current = queue.pop(0)
            if current in visited:
                continue

            visited.add(current)
            for neighbour in find_neighbours(*current, data):
                if data[neighbour[0]][neighbour[1]] != 9:
                    queue.append(neighbour)

        basins.append(len(visited))

    return prod(sorted(basins)[-3:])


if __name__ == "__main__":
    data = [list(map(int, x.rstrip()))
            for x in open("input09.txt").readlines()]

    print("--- AOC Day 09 ---")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
