from utils import get_input


def part1(data):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    row = 1
    col = 1

    code = []

    for line in data:
        for char in line:
            match char:
                case 'U':
                    row = max(0, row - 1)
                case 'D':
                    row = min(2, row + 1)
                case 'L':
                    col = max(0, col - 1)
                case 'R':
                    col = min(2, col + 1)

        code.append(keypad[row][col])

    return ''.join(map(str, code))


def part2(data):
    keypad = [
        [None, None, 1, None, None],
        [None, 2, 3, 4, None],
        [5, 6, 7, 8, 9],
        [None, 'A', 'B', 'C', None],
        [None, None, 'D', None, None]
    ]
    row = 2
    col = 0
    code = []

    for line in data:
        for char in line:
            new_row = row
            new_col = col
            match char:
                case 'U':
                    new_row = max(0, row - 1)
                case 'D':
                    new_row = min(4, row + 1)
                case 'L':
                    new_col = max(0, col - 1)
                case 'R':
                    new_col = min(4, col + 1)

            if keypad[new_row][new_col] is not None:
                row = new_row
                col = new_col

        code.append(keypad[row][col])

    return ''.join(map(str, code))


def main():
    data = get_input('02')
    parsed = data.splitlines()
    print(f"Part 1: {part1(parsed)}")
    print(f"Part 2: {part2(parsed)}")


if __name__ == "__main__":
    main()
