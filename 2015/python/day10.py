def iterate(data):
    count = 0
    new_str = ""
    prev = data[0]
    for c in data:
        if c == prev:
            count += 1
        else:
            new_str += str(count)
            new_str += prev
            count = 1
        prev = c

    new_str += str(count)
    new_str += prev

    return new_str


def part1(data):
    for _ in range(40):
        data = iterate(data)
    return len(data)


def part2(data):
    for _ in range(50):
        data = iterate(data)
    return len(data)


def main():
    data = "1113122113"

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
