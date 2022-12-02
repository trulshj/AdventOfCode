
def check_line_syntax(line):
    openers = '([{<'
    closers = ')]}>'
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    stack = []
    for char in line:
        if char in openers:
            stack.append(char)
        else:
            if closers.index(char) != openers.index(stack.pop()):
                return scores[char]
    return 0


def part1(data):
    syntax_error_score = 0

    for line in data:
        syntax_error_score += check_line_syntax(line)

    return syntax_error_score


def complete_line(line):
    openers = '([{<'
    closers = ')]}>'
    scores = {'(': 1, '[': 2, '{': 3, '<': 4}
    stack = []
    for char in line:
        if char in openers:
            stack.append(char)
        else:
            if closers.index(char) != openers.index(stack.pop()):
                return 0

    score = 0
    while len(stack) > 0:
        score *= 5
        score += scores[stack.pop()]

    return score


def part2(data):
    scores = []
    for line in data:
        line_score = complete_line(line)
        if line_score != 0:
            scores.append(complete_line(line))

    middle = len(scores) // 2
    return sorted(scores)[middle]


if __name__ == "__main__":
    data = [list(x.rstrip()) for x in open("input10.txt").readlines()]

    print("--- AOC Day 10 ---")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
