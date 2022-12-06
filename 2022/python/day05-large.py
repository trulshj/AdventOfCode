from re import match
from time import time
import linecache
import sys

DAY = 5
FILENAME = f"/Users/trulshj/dev/aoc/2022/inputs/day{DAY:02}-large.txt"


Command = tuple[int, int, int]
Stack = list[str]


def get_number_of_file_lines():
    with open(FILENAME) as f:
        total_lines = len(f.readlines())

    with open(FILENAME) as f:
        crate_lines, command_lines = list(map(lambda x: len(x.split("\n")), f.read().split("\n\n")))
        return total_lines, crate_lines-1, command_lines


TOTAL_LINES, CRATE_LINES, COMMAND_LINES = get_number_of_file_lines()


def main():

    stacks = get_stacks()

    commands = get_commands()

    print("Moving Crates...")
    crates_start_time = time()

    for idx, command in enumerate(commands, start=1):
        print_progress(idx, COMMAND_LINES, crates_start_time)

        amount, source, target = command

        x = len(stacks[source-1]) - amount
        stacks[target-1] += stacks[source-1][x:]
        stacks[source-1] = stacks[source-1][:x]

    sys.stdout.write("\n")


def get_stacks():
    with open(FILENAME) as f:
        crates = f.read().split("\n\n")[0].split("\n")[:-1]
        stacks = [[] for _ in range(9)]

        print("Assembling Crate Stacks...")
        stacks_start_time = time()

        for n, row in enumerate(crates, start=1):
            print_progress(n, CRATE_LINES, stacks_start_time)
            for idx, crate in enumerate(row[1::4]):
                if crate != " ":
                    stacks[idx].append(crate)

        sys.stdout.write("\n")

        return stacks


def print_progress(current, total, start_time):
    sys.stdout.write(
        f"\rProgress: {current}/{total}, {(current)*100/(total):.4f}%, {time()-start_time:.2f}s")


def parse_command(line) -> Command:
    return tuple(map(int, match(r"move (\d+) from (\d+) to (\d+)", line).groups()))


def get_commands():
    return (parse_command(linecache.getline(FILENAME, line)) for line in range(TOTAL_LINES-COMMAND_LINES+1, TOTAL_LINES+1))


if __name__ == "__main__":
    main()
