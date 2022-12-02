import numpy as np


def part1(target):
    N = int(29e6)

    houses = np.full(N, 10)

    for i in range(2, N//10):
        houses[i::i] += 10 * i

    return np.argmax(houses > target)


def part2(target):
    N = int(29e6)

    houses = np.full(N, 10)

    for i in range(2, N//10):
        houses[i:(i*50):i] += 11 * i

    return np.argmax(houses > target)


def main():
    with open('inputs/day20.txt') as f:
        target = int(f.readline())

    print(part1(target))
    print(part2(target))


if __name__ == "__main__":
    main()
