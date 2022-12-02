
moves = {
    '^': (0,  1),
    '>': (1,  0),
    'v': (0, -1),
    '<': (-1, 0),
}


def part1(data):
    coords = (0, 0)
    visited = set(coords)
    for instruction in data:
        coords = tuple(map(sum, zip(coords, moves.get(instruction))))
        visited.add(coords)

    return len(visited)


def part2(data):
    santa_coords = (0, 0)
    robosanta_coords = (0, 0)
    santa_visited = set(santa_coords)
    robosanta_visited = set(robosanta_coords)

    for idx, instruction in enumerate(data):
        if (idx % 2 == 0):
            santa_coords = tuple(
                map(sum, zip(santa_coords, moves.get(instruction))))
            santa_visited.add(santa_coords)
        else:
            robosanta_coords = tuple(
                map(sum, zip(robosanta_coords, moves.get(instruction))))
            robosanta_visited.add(robosanta_coords)

    return len(santa_visited.union(robosanta_visited)) - 1


def main():
    with open('inputs/day03.txt') as f:
        data = [x for x in f.readline()]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
