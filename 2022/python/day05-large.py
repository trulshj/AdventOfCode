from re import match
from tqdm import tqdm
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

    for command in tqdm(commands, ascii=True):
        amount, source, target = command

        x = len(stacks[source-1]) - amount
        stacks[target-1] += stacks[source-1][x:]
        stacks[source-1] = stacks[source-1][:x]

    print("Top Crates Read:", get_word(stacks))


def get_word(stacks):
    word = ""
    for stack in stacks:
        word += stack[-1]
    return word


def get_stacks():
    with open(FILENAME) as f:
        crates = f.read().split("\n\n")[0].split("\n")[:-1]
        stacks = [[] for _ in range(9)]

        print("Assembling Crate Stacks...")

        for row in tqdm(crates, ascii=True):
            for idx, crate in enumerate(row[1::4]):
                if crate != " ":
                    stacks[idx].append(crate)

        return stacks


def parse_command(line) -> Command:
    return tuple(map(int, match(r"move (\d+) from (\d+) to (\d+)", line).groups()))


def get_commands():
    print("Parsing Crane Commands")
    return [parse_command(linecache.getline(FILENAME, line)) for line in tqdm(range(TOTAL_LINES-COMMAND_LINES+1, TOTAL_LINES+1), ascii=True)]


if __name__ == "__main__":
    main()
