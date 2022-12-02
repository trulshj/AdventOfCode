import re
import json


def part1(data):
    return sum(map(int, re.findall(r"-?\d+", data)))


def part2(data):
    def sum_json(node):
        if type(node) is int:
            return node
        if type(node) is list:
            return sum(map(sum_json, node))
        if type(node) is dict:
            if "red" in node.values():
                return 0
            return sum(map(sum_json, node.values()))

        return 0

    return sum_json(json.loads(data))


def main():
    with open('inputs/day12.txt') as f:
        data = f.readline()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
