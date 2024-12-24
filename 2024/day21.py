from collections import deque
from itertools import product
from functools import cache


def compute_shortest_paths(keypad):
    positions = {}
    for y, row in enumerate(keypad):
        for x, cell in enumerate(row):
            if cell is not None:
                positions[cell] = (y, x)

    paths = {}
    for a in positions:
        for b in positions:
            if a == b:
                paths[(a, b)] = "A"
                continue
            options = []
            queue = deque([(positions[a], "")])
            optimal_length = float("inf")
            while queue:
                (y, x), path = queue.popleft()
                for ny, nx, nm in [(y-1, x, '^'), (y+1, x, 'v'), (y, x-1, '<'), (y, x+1, '>')]:
                    if not (0 <= ny < len(keypad)) or not (0 <= nx < len(keypad[0])):
                        continue
                    if (key := keypad[ny][nx]) is None:
                        continue
                    if key == b:
                        if optimal_length < len(path) + 1:
                            break
                        optimal_length = len(path) + 1
                        options.append(path + nm + "A")
                    else:
                        queue.append(((ny, nx), path + nm))
                else:
                    continue
                break

            paths[(a, b)] = options
    return paths


door_keypad = [
    ['7',  '8', '9'],
    ['4',  '5', '6'],
    ['1',  '2', '3'],
    [None, '0', 'A']
]

door_paths = compute_shortest_paths(door_keypad)

directional_keypad = [
    [None, '^', 'A'],
    ['<',  'v', '>']
]

directional_paths = compute_shortest_paths(directional_keypad)
directional_lengths = {key: len(value[0])
                       for key, value in directional_paths.items()}


def find_door_paths(string, paths):
    paths = [paths[(a, b)] for a, b in zip("A" + string, string)]
    return ["".join(x) for x in product(*paths)]


@cache
def compute_length(a, b, depth=2):
    if depth == 1:
        return directional_lengths[(a, b)]
    optimal_length = float("inf")
    for path in directional_paths[(a, b)]:
        length = 0
        for x, y in zip('A' + path, path):
            length += compute_length(x, y, depth - 1)
        optimal_length = min(optimal_length, length)
    return optimal_length


with open("2024/input21.txt") as f:
    codes = f.read().splitlines()

total = 0
for code in codes:
    door_robot_possible_paths = find_door_paths(code, door_paths)
    shorest_length = float("inf")
    for path in door_robot_possible_paths:
        length = 0
        for a, b in zip('A' + path, path):
            length += compute_length(a, b, depth=25)
        shorest_length = min(shorest_length, length)
    total += shorest_length * int(code[:-1])
print(total)
