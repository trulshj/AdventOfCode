from utils import print_day
from dataclasses import dataclass
from tqdm import tqdm
import re

DAY = 15


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


class Sensor:
    def __init__(self, x: int, y: int, beacon_x: int, beacon_y: int) -> None:
        self.x = x
        self.y = y
        self.beacon_x = beacon_x
        self.beacon_y = beacon_y
        self.radius = manhattan_distance(x, y, beacon_x, beacon_y)

    def can_reach(self, x, y):
        return manhattan_distance(x, y, self.x, self.y) <= self.radius

    def interval_at_y(self, target_y):
        y_diff = abs(self.y - target_y)
        if y_diff > self.radius:
            return (0, 0)
        x_range = abs(self.radius - y_diff)
        return (self.x - x_range, self.x + x_range)


def main():
    print_day(DAY, part1, part2, get_data)


def get_data():
    with open(f"../inputs/day{DAY:02}.txt") as f:
        return [Sensor(*map(int, re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups())) for line in f.readlines()]


def part1(data: list[Sensor]):
    y = 2_000_000

    intervals = (sensor.interval_at_y(y) for sensor in data if sensor.can_reach(sensor.x, y))
    coords = set()
    for interval in intervals:
        coords = coords.union(set(range(*sorted(interval))))

    return len(coords)


def tuning(x, y):
    return 4_000_000 * x + y


def part2(data: list[Sensor]):
    min_coord = 0
    max_coord = 4_000_000

    for y in tqdm(range(min_coord, max_coord + 1)):
        x = min_coord
        while x <= max_coord:
            for sensor in data:
                if sensor.can_reach(x, y):
                    x = sensor.interval_at_y(y)[1] + 1
                    break
            else:
                return tuning(x, y)

    return -1


if __name__ == "__main__":
    main()
