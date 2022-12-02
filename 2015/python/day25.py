import re


def get_code_index(row, column):
    return sum(range(row + column - 1)) + column


def get_next_code(code):
    BASE = 252533
    MOD = 33554393

    return (code * BASE) % MOD


def part1(row, column):
    INITIAL_CODE = 20151125

    code = INITIAL_CODE
    for _ in range(1, get_code_index(row, column)):
        code = get_next_code(code)

    return code


def main():
    with open('inputs/day25.txt') as f:
        row, column = list(map(int, re.findall(r"(\d+)", f.readline())))

    print(part1(row, column))


if __name__ == "__main__":
    main()
