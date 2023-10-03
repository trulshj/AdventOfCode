from utils import get_input


def part1(input):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pos = (0, 0)
    facing = 0
    for turn, dist in input:
        facing = (facing + (1 if turn == 'R' else -1)) % 4
        pos = (pos[0] + directions[facing][0] * dist, pos[1] + directions[facing][1] * dist)

    return abs(pos[0]) + abs(pos[1])


def part2(input):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pos = (0, 0)
    facing = 0
    visited = set()
    for turn, dist in input:
        facing = (facing + (1 if turn == 'R' else -1)) % 4
        for _ in range(dist):
            pos = (pos[0] + directions[facing][0], pos[1] + directions[facing][1])
            if pos in visited:
                return abs(pos[0]) + abs(pos[1])
            visited.add(pos)


def main():
    data = get_input('01')
    parsed = [(x[0], int(x[1:])) for x in data.split(', ')]
    print(f"Part 1: {part1(parsed)}")
    print(f"Part 2: {part2(parsed)}")


if __name__ == "__main__":
    main()
