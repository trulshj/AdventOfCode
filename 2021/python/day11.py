import numpy as np


def flash(row, col):
    l_r = row - 1 if row > 0 else row
    h_r = row + 2 if row < len(data) else row + 1
    l_c = col - 1 if col > 0 else col
    h_c = col + 2 if col < len(data[row]) else col + 1
    data[l_r:h_r, l_c:h_c] += 1


def part1(data):
    total_flashes = 0

    for _ in range(100):
        data += 1
        will_flash = data > 9
        has_flashed = np.zeros((10, 10), dtype='bool')

        while True:
            old_flash_count = np.sum(will_flash)

            for row in range(10):
                for col in range(10):
                    if will_flash[row][col] and not has_flashed[row][col]:
                        flash(row, col)

            has_flashed += will_flash
            will_flash = data > 9

            if old_flash_count == np.sum(will_flash):
                for row in range(10):
                    for col in range(10):
                        if has_flashed[row][col]:
                            data[row][col] = 0
                break

        total_flashes += np.sum(has_flashed)
    return total_flashes


def part2(data):
    for i in range(1, 1000):
        data += 1
        will_flash = data > 9
        has_flashed = np.zeros((10, 10), dtype='bool')

        while True:
            old_flash_count = np.sum(will_flash)

            for row in range(10):
                for col in range(10):
                    if will_flash[row][col] and not has_flashed[row][col]:
                        flash(row, col)

            has_flashed += will_flash
            will_flash = data > 9

            if old_flash_count == np.sum(will_flash):
                for row in range(10):
                    for col in range(10):
                        if has_flashed[row][col]:
                            data[row][col] = 0
                break
        if np.sum(has_flashed) >= 100:
            return i + 10  # Already done 100 flashes in part 1


if __name__ == "__main__":
    data = np.array([list(map(int, x.rstrip()))
                     for x in open("input11.txt").readlines()])

    print("--- AOC Day 11 ---")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
