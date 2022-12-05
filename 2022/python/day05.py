from utils import print_day
from collections import defaultdict
from re import match

DAY = 5


def main():
    print_day(DAY, part1, part2, get_data)


def get_data():
    with open(f"../inputs/day{DAY:02}.txt") as f:
        crates, commands = f.read().split("\n\n")

        stacks = defaultdict(list)

        for row in crates.split("\n")[:-1]:
            for idx, crate in enumerate(row[1::4], start=1):
                if crate != " ":
                    stacks[idx].insert(0, crate)

        moves = [tuple(map(int, match(r"move (\d+) from (\d+) to (\d+)", command).groups()))
                 for command in commands.split("\n")]

        return (stacks, moves)


def part1(data):
    return move_crates(*data, -1)


def part2(data):
    return move_crates(*data, 1)


def move_crates(stacks, moves, reverse):
    for times, from_stack, to_stack in moves:
        from_idx = len(stacks[from_stack]) - times
        stacks[to_stack] += stacks[from_stack][from_idx:][::reverse]
        del stacks[from_stack][from_idx:]

    return "".join([stacks[i][-1] for i in range(1, len(stacks.keys()) + 1)])


if __name__ == "__main__":
    main()
