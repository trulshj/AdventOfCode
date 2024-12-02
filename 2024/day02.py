def read_input():
    with open("./input02.txt") as f:
        return [list(map(int, x.split())) for x in f.readlines()]


def is_safe(report: list[int]):
    direction = report[0] < report[1]

    for l, r in zip(report, report[1:]):
        current_direction = l < r
        if current_direction != direction:
            return False

        diff = abs(l - r)
        if diff < 1 or diff > 3:
            return False

    return True


def part1():
    reports = read_input()
    print(sum(map(is_safe, reports)))


def part2():
    reports = read_input()

    def is_safe_with_one_removed(report: list[int]):
        return any(is_safe(report[:i] + report[i+1:]) for i in range(len(report)))

    print(sum(
        is_safe(report) or is_safe_with_one_removed(report)
        for report in reports
    ))


if __name__ == "__main__":
    part1()
    part2()
