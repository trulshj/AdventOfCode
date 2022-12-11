from utils import print_day
from dataclasses import dataclass

DAY = 9


def main():
    print_day(DAY, part1, part2, get_data)


def get_data():
    with open(f"../inputs/day{DAY:02}.txt") as f:
        data = []
        for line in f.readlines():
            direction, steps = line.split()
            data.append((direction, int(steps)))
        return data


def part1(data):
    return simulate_rope(data, 2)


def part2(data):
    return simulate_rope(data, 10)


@dataclass
class Knot:
    x: int
    y: int

    def __hash__(self):
        return hash(repr(self))

    def step(self, dir: str):
        match dir:
            case 'R':
                self.x += 1
            case 'L':
                self.x -= 1
            case 'U':
                self.y += 1
            case 'D':
                self.y -= 1

    def follow(self, other: 'Knot'):
        dx = other.x - self.x
        dy = other.y - self.y

        if abs(dx) <= 1 and abs(dy) <= 1:
            return

        if dx == 0:
            self.y += 1 if dy == 2 else -1
        elif dy == 0:
            self.x += 1 if dx == 2 else -1
        else:
            self.y += 1 if dy > 0 else -1
            self.x += 1 if dx > 0 else -1


def simulate_rope(data: tuple[str, int], number_of_knots: int) -> int:
    knots = [Knot(0, 0) for _ in range(0, number_of_knots)]
    visited = set()

    for direction, steps in data:
        for _ in range(0, steps):
            knots[0].step(direction)

            for leader, follower in zip(knots, knots[1:]):
                follower.follow(leader)

            visited.add(knots[-1])

    return len(visited)


if __name__ == '__main__':
    main()
