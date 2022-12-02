
def align_cost(crabs, pos):
    return sum((abs(crab - pos) for crab in crabs))


def part1(data):
    high = max(data)
    low = min(data)
    while True:
        mid = (high + low) // 2
        mid_cost = align_cost(data, mid)
        if mid_cost > align_cost(data, mid-1):
            high = mid + 1
        elif mid_cost > align_cost(data, mid+1):
            low = mid - 1

        else:
            return mid_cost


def arithmetic_sum(n):
    return (n * n + n) // 2


def align_cost_2(crabs, pos):
    return sum((arithmetic_sum(abs(crab-pos)) for crab in crabs))


def part2(data):
    high = max(data)
    low = min(data)
    while True:
        mid = (high + low) // 2
        mid_cost = align_cost_2(data, mid)
        if mid_cost > align_cost_2(data, mid-1):
            high = mid + 1
        elif mid_cost > align_cost_2(data, mid+1):
            low = mid - 1

        else:
            return mid_cost


if __name__ == "__main__":
    data = [int(x) for x in open("input07.txt").readline().split(',')]

    print("--- AOC Day 07 ---")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
