
data = [x.rstrip() for x in open("input04.txt").readlines()]
bingo_numbers = [int(x) for x in data[0].split(',')]


class Bingo_Board:
    def __init__(self, numbers):
        self.numbers = numbers
        self.checked = [[False for _ in range(5)] for _ in range(5)]
        self.has_won = False

    def check_number(self, number):
        for row in range(5):
            for col in range(5):
                if self.numbers[row][col] == number:
                    self.checked[row][col] = True
                    self.has_won = self.check_win()
                    return

    def check_win(self):
        for i in range(5):
            # Rows
            if all(self.checked[i]):
                return True
            # Columns
            for j in range(5):
                if not self.checked[j][i]:
                    break
            else:
                return True
        return False

    def score(self):
        score = 0
        for row in range(5):
            for col in range(5):
                if not self.checked[row][col]:
                    score += self.numbers[row][col]
        return score


def create_bingo_boards(data):
    boards = []
    for i in range(len(data[1::6])):
        board = []
        for x in data[i*6+2:i*6+7]:
            board.append([int(n) for n in x.split(' ') if len(n) > 0])
        boards.append(Bingo_Board(board))
    return boards


def part1(data, bingo_numbers):
    boards = create_bingo_boards(data)
    for number in bingo_numbers:
        for board in boards:
            board.check_number(number)
            if (board.has_won):
                return board.score() * number


def part2(data, bingo_numbers):
    boards = create_bingo_boards(data)
    for number in bingo_numbers:
        for board in boards:
            board.check_number(number)
        if len(boards) > 1:
            boards = [board for board in boards if not board.has_won]
        elif (boards[0].has_won):
            return boards[0].score() * number


if __name__ == "__main__":
    print("--- AOC Day 04 ---")
    print("Part 1:", part1(data, bingo_numbers))
    print("Part 2:", part2(data, bingo_numbers))
