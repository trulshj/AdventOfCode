
def init_fish(data):
    fish = [0 for _ in range(9)]
    for i in data:
        fish[i] += 1
    return fish


def next_day(fish):
    new_fish = fish[0]
    fish[0] = fish[1]
    fish[1] = fish[2]
    fish[2] = fish[3]
    fish[3] = fish[4]
    fish[4] = fish[5]
    fish[5] = fish[6]
    fish[6] = new_fish + fish[7]
    fish[7] = fish[8]
    fish[8] = new_fish


def part1(data):
    fish = init_fish(data)
    for i in range(80):
        next_day(fish)
    return sum(fish)


def part2(data):
    fish = init_fish(data)
    for i in range(256):
        next_day(fish)
    return sum(fish)


if __name__ == "__main__":
    data = [int(x) for x in open("input06.txt").readline().split(',')]

    print("--- AOC Day 06 ---")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
