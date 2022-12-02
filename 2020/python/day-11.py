
layout = []
for line in open("input-11.txt").readlines():
    layout.append([x for x in line.rstrip()])

original_layout = layout

def check_around(row, col, layout):
    current = layout[row][col]
    if current == '.':
        return '.'

    around = []
    adjacent_pos = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]
    for pos in adjacent_pos:
        try:
            if pos[0] != -1 and pos[1] != -1:
                around.append(layout[pos[0]][pos[1]])
        except IndexError:
            pass
    if current == 'L' and '#' not in around:
        return '#'
    elif current == '#' and around.count('#') >= 4:
        return 'L'
    else:
        return current


def check_around_ray(row, col, layout):
    self = layout[row][col]
    if self == '.':
        return '.'

    around = []
    
    # N, NE, E, SE, S, SW, W, NW
    rays = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for ray in rays:
        curr_row = row
        curr_col = col
        current = '.'
        while True:
            curr_row += ray[0]
            curr_col += ray[1]
            if curr_row == -1 or curr_col == -1:
                break
            try:
                current = layout[curr_row][curr_col]
            except IndexError:
                break
            if current == '#' or current == 'L':
                break
        around.append(current)

    if self == 'L' and '#' not in around:
        return '#'
    elif self == '#' and around.count('#') >= 5:
        return 'L'
    else:
        return self


previous_seated = -1
while True:
    current_seated = sum(x.count('#') for x in layout)

    temp_layout = []
    for row in range(len(layout)):
        temp_row = [check_around(row, col, layout) for col in range(len(layout[0]))]
        temp_layout.append(temp_row)
    layout = temp_layout

    if current_seated == previous_seated:
        print("Part 1:", current_seated)
        break
    else:
        previous_seated = current_seated


layout = original_layout

previous_seated = -1
while True:
    current_seated = sum(x.count('#') for x in layout)

    temp_layout = []
    for row in range(len(layout)):
        temp_row = [check_around_ray(row, col, layout) for col in range(len(layout[0]))]
        temp_layout.append(temp_row)
    layout = temp_layout

    if current_seated == previous_seated:
        print("Part 2:", current_seated)
        break
    else:
        previous_seated = current_seated