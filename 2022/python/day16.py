from utils import print_day
from functools import cache

DAY = 16


def main():
    print_day(DAY, part1, part2, get_data)


def get_data():
    with open(f"../inputs/day{DAY:02}.txt") as f:
        valves = {}
        for line in f.readlines():
            valve, leads_to = line.rstrip().split("; ")
            name = valve.split()[1]
            rate = int(valve.split("=")[-1])
            tunnels = [tunnel.rstrip(",") for tunnel in leads_to.split()[4:]]
            valves[name] = {"rate": rate, "tunnels": tunnels}
        return valves


# Cursed global variable oops
valves = get_data()


@cache
def solve(opened_valves, remaining_time, current_position, part2=False):
    if remaining_time <= 0:
        return solve(opened_valves, 26, "AA") if part2 else 0

    best = 0
    s = valves[current_position]
    for valve in s["tunnels"]:
        best = max(best, solve(opened_valves, remaining_time - 1, valve, part2))

    if current_position not in opened_valves and s["rate"] > 0 and remaining_time > 0:
        opened_valves = set(opened_valves)
        opened_valves.add(current_position)
        remaining_time -= 1
        new_sum = remaining_time * s["rate"]

        for valve in s["tunnels"]:
            best = max(
                best,
                new_sum + solve(frozenset(opened_valves), remaining_time - 1, valve, part2),
            )

    return best


def part1(_):
    return solve(frozenset(), 30, "AA")


def part2(_):
    return solve(frozenset(), 26, "AA", part2=True)


if __name__ == "__main__":
    main()
