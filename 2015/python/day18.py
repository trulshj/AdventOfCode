import numpy as np


def transform(string):
    return [0] + [0 if x == '.' else 1 for x in string] + [0]


def part1(data):

    ITERATIONS = 100

    array = np.array(data, dtype=bool)

    for _ in range(ITERATIONS):
        buffer = np.zeros((len(data), len(data)), dtype=int)
        for i in range(1, len(data) - 1):
            for j in range(1, len(data) - 1):
                neighbours = array[i-1:i+2, j-1:j+2].sum() - array[i, j]
                curr = array[i, j]
                if curr == 1 and not (neighbours == 3 or neighbours == 2):
                    buffer[i, j] = 0
                elif curr == 0 and neighbours == 3:
                    buffer[i, j] = 1
                else:
                    buffer[i, j] = array[i, j]
        array = buffer

    return array.sum()


def part2(data):
    ITERATIONS = 100

    array = np.array(data, dtype=bool)
    array[1, 1] = 1
    array[1, len(data) - 2] = 1
    array[len(data) - 2, 1] = 1
    array[len(data) - 2, len(data) - 2] = 1

    for _ in range(ITERATIONS):
        buffer = np.zeros((len(data), len(data)), dtype=int)
        for i in range(1, len(data) - 1):
            for j in range(1, len(data) - 1):
                neighbours = array[i-1:i+2, j-1:j+2].sum() - array[i, j]
                curr = array[i, j]
                if curr == 1 and not (neighbours == 3 or neighbours == 2):
                    buffer[i, j] = 0
                elif curr == 0 and neighbours == 3:
                    buffer[i, j] = 1
                else:
                    buffer[i, j] = array[i, j]
        buffer[1, 1] = 1
        buffer[1, len(data) - 2] = 1
        buffer[len(data) - 2, 1] = 1
        buffer[len(data) - 2, len(data) - 2] = 1
        array = buffer
    return array.sum()


def main():
    with open('inputs/day18.txt') as f:
        data = [transform(x.rstrip()) for x in f.readlines()]

    data.insert(0, [0] * (len(data) + 2))
    data.append([0] * (len(data) + 1))

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
