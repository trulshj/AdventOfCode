import collections


def part1(reactions: dict[str, list[str]], molecule: str):
    possibilities = set()
    valid_atoms = reactions.keys()
    for idx in range(len(molecule)):
        if molecule[idx] in valid_atoms:
            atom = molecule[idx]
        elif molecule[idx:idx+2] in valid_atoms:
            atom = molecule[idx:idx+2]
        else:
            continue

        for reaction in reactions[atom]:
            possibilities.add(molecule[:idx] + reaction + molecule[idx+len(atom):])

    return len(possibilities)


def part2(molecule: str):
    molecule = molecule.replace("Y", ",").replace("Rn", "(").replace("Ar", ")").replace("Al", "A").replace(
        "Ca", "C").replace("Mg", "M").replace("Si", "S").replace("Th", "T").replace("Ti", "I")
    elements = len(molecule)
    brackets = molecule.count("(") + molecule.count(")")
    commas = molecule.count(",")
    return elements - brackets - (2 * commas) - 1


def main():
    reactions = collections.defaultdict(list)
    with open('inputs/day19.txt') as f:
        data = [x.rstrip() for x in f.readlines()]

    for line in data[:-2]:
        start, end = line.split(" => ")
        reactions[start].append(end)

    molecule = data[-1]

    print(part1(reactions, molecule))
    print(part2(molecule))


if __name__ == "__main__":
    main()
