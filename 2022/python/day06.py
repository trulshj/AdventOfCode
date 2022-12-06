from utils import print_day

DAY = 6


def main():
    print_day(DAY, part1, part2, get_data)


def get_data():
    with open(f"../inputs/day{DAY:02}.txt") as f:
        return f.read()


def part1(data: str):
    return find_marker(data, 4)


def part2(data: str):
    return find_marker(data, 14)


def find_marker(datastream: str, marker_length: int):
    for i in range((marker_length-1), len(datastream)):
        if len(set(datastream[i-marker_length:i])) == marker_length:
            return i


if __name__ == "__main__":
    main()
