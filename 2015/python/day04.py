import hashlib


def md5_zeroes(key, number_of_zeroes):
    i = 0
    target = "0" * number_of_zeroes
    while True:
        s = key + str(i)
        result = hashlib.md5(s.encode()).hexdigest()
        if (result.startswith(target)):
            return i
        else:
            i += 1


def part1(data):
    return md5_zeroes(data, 5)


def part2(data):
    return md5_zeroes(data, 6)


def main():
    with open('inputs/day04.txt') as f:
        data = f.readline()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
