from utils import print_day
from dataclasses import dataclass

DAY = 10


def main():
    print_day(DAY, part1, part2, get_data)


def get_data():
    with open(f"../inputs/day{DAY:02}.txt") as f:
        return [x.rstrip() for x in f.readlines()]


def part1(data):
    register = 1
    value_sums = 0
    cycle = 1
    interesting_cycles = [20, 60, 100, 140, 180, 220]
    for line in data:
        cycle += 1
        if (cycle in interesting_cycles):
            value_sums += register * cycle
        match line.split(" "):
            case 'noop': continue
            case 'addx', x:
                register += int(x)
                cycle += 1
                if (cycle in interesting_cycles):
                    value_sums += register * cycle

    return value_sums


@dataclass
class CRT:
    commands: list[str]
    screen: list[list[str]]
    cycle: int = -1
    command_idx: int = 0
    running_command_name: str = None
    running_command_time: int = 0
    running_command_value: int = None
    register_value: int = 1

    def run_cycle(self):
        self.cycle += 1

        if self.running_command_time == 0:
            self.start_command()

        self.draw_pixel()
        self.progress_command()

    def draw_pixel(self):
        row_idx = self.cycle // 40
        col_idx = self.cycle % 40

        char = "██" if col_idx in [self.register_value-1, self.register_value, self.register_value+1] else "  "
        self.screen[row_idx][col_idx] = char

    def format_screen(self):
        return "\n".join("".join(line) for line in self.screen)

    def start_command(self):
        next_command = self.commands[self.command_idx]
        self.command_idx += 1

        if next_command == "noop":
            self.running_command_name = "noop"
            self.running_command_time = 1
            self.running_command_value = None
        else:
            _, val = next_command.split(" ")
            self.running_command_name = "addx"
            self.running_command_time = 2
            self.running_command_value = int(val)

    def progress_command(self):
        self.running_command_time -= 1
        if self.running_command_time == 0 and self.running_command_name == "addx":
            self.register_value += self.running_command_value

    def should_terminate(self):
        return self.cycle >= 239


def part2(data):
    crt = CRT(commands=data, screen=[[""] * 40 for _ in range(6)])
    while True:
        if crt.should_terminate():
            break
        crt.run_cycle()
    return crt.format_screen()


if __name__ == "__main__":
    main()
