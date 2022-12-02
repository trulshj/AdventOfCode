import re
import collections


def part1(sues: collections.defaultdict[int, dict], tape: dict[str, int]):
    remaining_sues = list(range(1, 501))
    for key, val in tape.items():
        remaining_sues = [sue for sue in remaining_sues if sues[sue].get(key) == val or not key in sues[sue].keys()]
    return remaining_sues[0]


def part2(sues, tape):
    remaining_sues = list(range(1, 501))

    for key, val in tape.items():
        if key in ['cats', 'trees']:
            remaining_sues = [sue for sue in remaining_sues if not key in sues[sue].keys() or sues[sue].get(key) > val]
        elif key in ['pomeranians', 'goldfish']:
            remaining_sues = [sue for sue in remaining_sues if not key in sues[sue].keys() or sues[sue].get(key) < val]
        else:
            remaining_sues = [sue for sue in remaining_sues if not key in sues[sue].keys() or sues[sue].get(key) == val]
    return remaining_sues[0]


def main():
    sues: collections.defaultdict[int, dict] = collections.defaultdict(dict)

    with open('inputs/day16.txt') as f:
        for idx, line in enumerate(f.readlines(), start=1):
            values = re.findall(r"(\w+: \d+)+", line)
            for value in values:
                key, amount = value.split()
                sues[idx][key[:-1]] = int(amount)

    tape: dict[str, int] = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    print(part1(sues, tape))
    print(part2(sues, tape))


if __name__ == "__main__":
    main()
