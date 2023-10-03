from utils import get_input
import re


def is_real_room(room):
    checksum = re.findall(r'\[(.*?)\]', room)[0]
    room = room[:-7]
    room = room.replace('-', '')
    counts = {}
    for c in room:
        counts[c] = counts.get(c, 0) + 1
    counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return ''.join([c[0] for c in counts[:5]]) == checksum


def sector_id(room):
    return int(re.findall(r'\d+', room)[0])


def part1(data):
    sector_sum = 0
    for room in data:
        if is_real_room(room):
            sector_sum += sector_id(room)
            print(sector_sum, sector_id(room))

    return sector_sum


def part2(data):
    pass


def main():
    data = get_input("04").splitlines()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
