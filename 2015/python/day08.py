import re


def part1(data):
    codes_total = 0
    chars_total = 0
    for x in data:
        codes_total += len(x)
        s = x[1:-1]
        a = len(re.findall(r"\\\\", s))
        b = len(re.findall(r"\\\"", s))
        c = len(re.findall(r"\\x[a-f0-9]{2}", s))
        chars_total += len(s) - a - b - (3 * c)

    return codes_total - chars_total


def part2(data):
    codes_total = 0
    ecode_total = 0
    for x in data:
        codes_total += len(x)
        a = len(re.findall(r"\"", x))
        b = len(re.findall(r"\\", x))
        ecode_total += len(x) + a + b + 2

    return ecode_total - codes_total


def main():
    with open('inputs/day08.txt') as f:
        data = [x.rstrip() for x in f.readlines()]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
