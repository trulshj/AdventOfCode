import re


class Robot:
    def __init__(self, px: int, py: int, vx: int, vy: int):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def position(self):
        return (self.py, self.px)

    def move(self):
        self.px += self.vx
        self.py += self.vy

        if self.px < 0:
            self.px += COLUMNS
        elif self.px >= COLUMNS:
            self.px %= COLUMNS

        if self.py < 0:
            self.py += ROWS
        elif self.py >= ROWS:
            self.py %= ROWS


with open("2024/input14.txt") as f:
    robots = [Robot(*map(int, re.findall(r"-?\d+", x.rstrip())))
              for x in f.readlines()]

COLUMNS = 101
ROWS = 103


def move_bots(robots: list[Robot]):
    for robot in robots:
        robot.move()


def print_map(robots: list[Robot]):
    grid = []
    for y in range(ROWS):
        row = [0] * COLUMNS
        for robot in robots:
            ry, rx = robot.position()
            if ry == y:
                row[rx] += 1
        grid.append(row)

    print("\n".join("".join(map(str, row)).replace('0', '.')
                    for row in grid))


def count_bots(robots: list[Robot]):
    ul = ur = bl = br = 0
    for robot in robots:
        ry, rx = robot.position()
        if ry > ROWS // 2:
            if rx > COLUMNS // 2:
                br += 1
            elif rx < COLUMNS // 2:
                bl += 1
        elif ry < ROWS // 2:
            if rx > COLUMNS // 2:
                ur += 1
            elif rx < COLUMNS // 2:
                ul += 1
    return ul * ur * bl * br


for i in range(1, 101):
    move_bots(robots)

print(count_bots(robots))


min_count = count_bots(robots)
min_idx = 100

for i in range(101, 100_000):
    move_bots(robots)
    count = count_bots(robots)
    if count < min_count:
        min_count = count
        min_idx = i
        print(f"\n#### {i} ####\n")
        print_map(robots)

print(min_count, min_idx)
