
with open("input02.txt") as f:
    lines = [x.rstrip() for x in f.readlines()]
    data = [(line.split(" ")[0], int(line.split(" ")[1])) for line in lines]


def part1():
    horizontal = 0
    depth = 0
    
    for op, val in data:
        if op == 'forward':
            horizontal += val
        elif op == 'down':
            depth += val
        else:
            depth -= val
            
    return horizontal * depth
    
    
def part2():
    horizontal = 0
    depth = 0
    aim = 0
    
    for op, val in data:
        if op == 'forward':
            horizontal += val
            depth += aim * val
        elif op == 'down':
            aim += val
        else:
            aim -= val
            
    return horizontal * depth


if __name__ == "__main__":
    print("--- AOC Day 02 ---")
    print("Part 1:", part1())
    print("Part 2:", part2())
