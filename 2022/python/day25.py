from utils import print_day

DAY = 25


def main():
    # print_day(DAY, part1, part2, get_data)
    data = get_data()
    print(part1(data))


def get_data():
    with open(f"../inputs/day{DAY:02}.txt") as f:
        return [line.rstrip() for line in f.readlines()]


def snafu_to_decimal(number: str):
    v = 1
    total = 0
    for c in number[::-1]:
        match c:
            case '0': pass
            case '1': total += 1 * v
            case '2': total += 2 * v
            case '-': total -= 1 * v
            case '=': total -= 2 * v
        v *= 5
    return total


def decimal_to_snafu(number: int):
    digits = ['0', '1', '2', '=', '-']
    snafu = ''
    carry = 0

    while number != 0 or carry:
        remainder = number % 5 + carry
        carry = 1 if remainder > 2 else 0
        snafu = digits[remainder % 5] + snafu
        number //= 5

    return snafu


def part1(data):
    return decimal_to_snafu(sum(map(snafu_to_decimal, data)))


def part2(data):
    return 0


if __name__ == "__main__":
    main()
