from utils import print_day
from typing import Callable
import math
import operator

DAY = 11


def main():
    print_day(DAY, part1, part2, get_data)


class Monkey:
    def __init__(self, starting_items: list[int], operation: Callable[[int], int], test_number: int, target_if_true: int, target_if_false: int):
        self.items = starting_items
        self.operation = operation
        self.test_number = test_number
        self.target_if_true = target_if_true
        self.target_if_false = target_if_false
        self.inspections = 0
        self.is_part1 = False
        self.common_denominator = None

    def has_items(self):
        return len(self.items) > 0

    def inspect_next_item(self):
        """Returns the item to be thrown and the target it is thrown to"""
        self.inspections += 1
        item = self.operation(self.items.pop(0))
        if self.is_part1:
            item //= 3

        if self.common_denominator != None:
            item %= self.common_denominator

        target = self.target_if_true if item % self.test_number == 0 else self.target_if_false
        return item, target

    def catch_item(self, item):
        self.items.append(item)


def create_operation(operation_string: str):
    match operation_string.split(" "):
        case "old", "+", "old": return lambda x: operator.add(x, x)
        case "old", "*", "old": return lambda x: operator.mul(x, x)
        case "old", "+", y: return lambda x: operator.add(x, int(y))
        case "old", "*", y: return lambda x: operator.mul(x, int(y))

    raise Exception("Invalid match case")


def get_data():
    with open(f"../inputs/day{DAY:02}.txt") as f:
        entries = [list(map(lambda x: x.strip(), entry.split("\n"))) for entry in f.read().split("\n\n")]
        monkeys = {}

        common_denominator = 1

        for entry in entries:
            monkey_id = int(entry[0].split(" ")[-1][:-1])
            starting_items = list(map(int, entry[1].split(": ")[-1].split(", ")))
            operation = create_operation(entry[2].split(" = ")[-1])
            test_number = int(entry[3].split()[-1])
            true_target = int(entry[4].split()[-1])
            false_target = int(entry[5].split()[-1])
            monkeys[monkey_id] = Monkey(starting_items, operation, test_number, true_target, false_target)
            common_denominator *= test_number

        for monkey in monkeys.values():
            monkey.common_denominator = common_denominator

        return monkeys


def run_rounds(monkeys: dict[str, Monkey], rounds: int):
    for _ in range(rounds):
        for i in range(len(monkeys.keys())):
            monkey = monkeys[i]
            while monkey.has_items():
                item, target = monkey.inspect_next_item()
                monkeys[target].catch_item(item)

    return math.prod(sorted(map(lambda x: x.inspections, monkeys.values()), reverse=True)[:2])


def part1(monkeys: dict[str, Monkey]):
    for monkey in monkeys.values():
        monkey.is_part1 = True

    return run_rounds(monkeys, 20)


def part2(monkeys):
    return run_rounds(monkeys, 10_000)


if __name__ == "__main__":
    main()
