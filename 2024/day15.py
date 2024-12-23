from collections import defaultdict


def read_input():
    with open("2024/input15.txt") as f:
        a, b = f.read().split("\n\n")

    instructions = b.replace('\n', '')
    grid = list(map(list, a.split()))
    return grid, instructions


def print_grid(grid, walls, boxes, robot):
    out = ""
    for y, row in enumerate(grid):
        for x in range(len(row)):
            c = (y, x)
            if c in walls:
                out += '#'
            elif c in boxes:
                out += 'O'
            elif c == robot:
                out += '@'
            else:
                out += '.'
        out += '\n'
    print(out)
    return out


def v_add(a, b):
    return tuple(map(lambda i, j: i + j, a, b))


def find_positions(grid):
    positions = defaultdict(set)
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            positions[cell].add((y, x))
    return positions


def part_1():
    grid, instructions = read_input()
    positions = find_positions(grid)
    walls = positions['#']
    boxes = positions['O']
    robot = positions['@'].pop()

    DELTAS = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
    print_grid(grid, walls, boxes, robot)

    for instruction in instructions:
        delta = DELTAS[instruction]
        next_pos = v_add(robot, delta)

        if next_pos in walls:
            continue

        if next_pos in boxes:
            box = next_pos
            while box in boxes:
                box = v_add(box, delta)
            if box in walls:
                continue
            boxes.remove(next_pos)
            boxes.add(box)

        robot = next_pos

    total = 0
    for box in boxes:
        total += box[0] * 100 + box[1]
    print(total)


def part_2():
    grid, instructions = read_input()
    replacements = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}
    for row in grid:
        for i in range(len(row)):
            row[i] = replacements[row[i]]
    print(grid)


if __name__ == "__main__":
    # part_1()
    part_2()
