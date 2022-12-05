from utils import print_day
from collections import defaultdict
from re import match

DAY = 5


def main():
    print_day(DAY, part1, part2, get_data())
    print(part1(get_data()))
    print(part2(get_data()))


def get_data():
    with open(f"../inputs/day{DAY:02}.txt") as f:
        crates, commands = f.read().split("\n\n")

        number_of_stacks = int(crates.split("\n")[-1].split()[-1])
        stacks = defaultdict(list)

        for row in crates.split("\n")[:-1]:
            for idx, crate in enumerate(row[1::4], start=1):
                if crate != " ":
                    stacks[idx].insert(0, crate)

        moves = [tuple(map(int, match(r"move (\d+) from (\d+) to (\d+)", command).groups()))
                 for command in commands.split("\n")]

        return (stacks, moves)


def part1(data):
    stacks, moves = data
    for times, from_stack, to_stack in moves:
        for _ in range(times):
            stacks[to_stack].append(stacks[from_stack].pop())

    return "".join([stacks[i][-1] for i in range(1, len(stacks.keys()) + 1)])


def part2(data):
    stacks, moves = data
    for times, from_stack, to_stack in moves:
        stacks[to_stack] += stacks[from_stack][len(stacks[from_stack])-times:]
        for _ in range(times):
            stacks[from_stack].pop()

    return "".join([stacks[i][-1] for i in range(1, len(stacks.keys()) + 1)])


if __name__ == "__main__":
    main()
