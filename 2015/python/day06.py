import re
import numpy as np


def part1(data):
    lights = np.zeros((1000, 1000), dtype=bool)

    for line in data:
        command = line[0]
        x1 = line[1]
        y1 = line[2]
        x2 = line[3]
        y2 = line[4]

        if command == "turn off":
            lights[x1:x2+1, y1:y2+1] = False

        elif command == "turn on":
            lights[x1:x2+1, y1:y2+1] = True

        else:
            lights[x1:x2+1, y1:y2+1] = ~lights[x1:x2+1, y1:y2+1]

    return lights.sum()


def part2(data):
    lights = np.zeros((1000, 1000), dtype=int)

    for line in data:
        command = line[0]
        x1 = line[1]
        y1 = line[2]
        x2 = line[3]
        y2 = line[4]

        if command == "turn off":
            lights[x1:x2+1, y1:y2+1] -= 1
            lights = np.clip(lights, 0, None)

        elif command == "turn on":
            lights[x1:x2+1, y1:y2+1] += 1

        else:
            lights[x1:x2+1, y1:y2+1] += 2

    return lights.sum()


def parse(line):
    return line[0], *map(int, line[1:])


def main():
    regex = "(turn off|toggle|turn on) (\d+),(\d+) through (\d+),(\d+)"

    with open('inputs/day06.txt') as f:
        data = [parse(re.findall(regex, x)[0]) for x in f.readlines()]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
