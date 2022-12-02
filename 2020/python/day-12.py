
lines = [(x[0], int(x[1:])) for x in [x.strip() for x in open("input-12.txt").readlines()]]

ship_x, ship_y = 0, 0

ops = {'E': 0, 'N': 1, 'W': 2, 'S': 3}
headings = [(1, 0), (0, 1), (-1, 0), (0, -1)]
current_heading = 0

for op, val in lines:
    if op == 'L':
        current_heading += val
    elif op == 'R':
        current_heading -= val
    elif op == 'F':
        ship_x += headings[current_heading // 90 % 4][0] * val
        ship_y += headings[current_heading // 90 % 4][1] * val
    else:
        ship_x += headings[ops[op]][0] * val
        ship_y += headings[ops[op]][1] * val
    
print("Part 1:", abs(ship_x) + abs(ship_y))


ship_x, ship_y = 0, 0
waypoint_x, waypoint_y = 10, 1

for op, val in lines:
    if op == 'R':
        for _ in range(val // 90):
            waypoint_x, waypoint_y = waypoint_y, -waypoint_x
    elif op == 'L':
        for _ in range(val // 90):
            waypoint_x, waypoint_y = -waypoint_y, waypoint_x
    elif op == 'F':
        ship_x += waypoint_x * val
        ship_y += waypoint_y * val
    else:
        waypoint_x += headings[ops[op]][0] * val
        waypoint_y += headings[ops[op]][1] * val
        
print("Part 2:", abs(ship_x) + abs(ship_y))
