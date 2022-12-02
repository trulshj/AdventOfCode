
def main():
    data = {}
    with open('inputs/day07.txt') as f:
        for line in f.readlines():
            wire = line.rstrip().split(" -> ")
            data[wire[-1]] = wire[0].split(" ")

    solved = {}
    SIXTEEN_BIT_MAX = 65535

    def solve(node):
        if node.isnumeric():
            return int(node)

        if node not in solved:
            ops = data[node]

            if len(ops) == 1:
                n = solve(ops[0])
            else:
                op = ops[-2]
                if op == 'AND':
                    n = solve(ops[0]) & solve(ops[2])
                elif op == 'OR':
                    n = solve(ops[0]) | solve(ops[2])
                elif op == 'NOT':
                    n = ~solve(ops[1]) & SIXTEEN_BIT_MAX
                elif op == 'RSHIFT':
                    n = solve(ops[0]) >> solve(ops[2])
                elif op == 'LSHIFT':
                    n = solve(ops[0]) << solve(ops[2]) & SIXTEEN_BIT_MAX

            solved[node] = n
        return solved[node]

    part1 = solve('a')
    print(part1)

    data['b'] = [str(part1)]
    solved = {}

    part2 = solve('a')
    print(part2)


if __name__ == "__main__":
    main()
