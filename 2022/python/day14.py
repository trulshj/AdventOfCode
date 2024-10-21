from utils import print_day
from dataclasses import dataclass

DAY = 14


def main():
    print_day(DAY, part1, part2, get_data)


DataType = list[list[tuple[int, int]]]


def get_data() -> DataType:
    with open(f"../inputs/day{DAY:02}.txt") as f:
        data = []
        for line in f.readlines():
            data.append([tuple(map(int, coords.split(","))) for coords in line.rstrip().split(" -> ")])
        return data


def calculate_obstacles(data: DataType):
    obstacles = set()
    for obstacle in data:
        for p1, p2 in zip(obstacle, obstacle[1:]):
            x1, x2 = sorted((p1[0], p2[0]))
            y1, y2 = sorted((p1[1], p2[1]))

            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    obstacles.add((x, y))
    return obstacles


def find_lowest_point(obstacles):
    return max(o[1] for o in obstacles)


@dataclass
class Sand:
    x: int = 500
    y: int = 0

    def fall(self, obstacles):
        if (self.x, self.y+1) not in obstacles:
            self.y += 1
            return True

        if (self.x-1, self.y+1) not in obstacles:
            self.x -= 1
            self.y += 1
            return True

        if (self.x+1, self.y+1) not in obstacles:
            self.x += 1
            self.y += 1
            return True

        return False

    def is_below(self, point):
        return self.y > point

    def is_at(self, level):
        return self.y == level - 1

    def is_blocked(self):
        return self.x == 500 and self.y == 0


def part1(data: DataType):
    obstacles = calculate_obstacles(data)
    lowest_point = find_lowest_point(obstacles)

    grains = 0
    while True:
        grain = Sand()
        while grain.fall(obstacles):
            if grain.is_below(lowest_point):
                return grains

        grains += 1
        obstacles.add((grain.x, grain.y))


def part2(data):
    obstacles = calculate_obstacles(data)
    lowest_point = find_lowest_point(obstacles)
    floor_level = lowest_point + 2

    grains = 0
    while True:
        grain = Sand()
        while grain.fall(obstacles):
            if not grain.is_at(floor_level):
                continue
            else:
                break

        grains += 1
        obstacles.add((grain.x, grain.y))

        if grain.is_blocked():
            return grains


if __name__ == "__main__":
    main()
