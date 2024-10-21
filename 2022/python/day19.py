from utils import print_day
import re

DAY = 19


def main():
    # print_day(DAY, part1, part2, get_data)
    data = get_data()
    print(part1(data))


def get_data():
    with open(f"../inputs/day{DAY:02}.txt") as f:
        blueprints = []
        for line in f.readlines():
            blueprints.append(tuple(map(int, re.findall(r"\d+", line)))[1:])

        return blueprints


def part1(data):
    return test_blueprint(data[0])


def part2(data):
    return 0


def test_blueprint(blueprint):
    return iterate(*blueprint)


def iterate(ore_bot_ore_cost, clay_bot_ore_cost, obsidian_bot_ore_cost, obsidian_bot_clay_cost, geode_bot_ore_cost, geode_bot_obsidian_cost, time_remaining=24, ore_bots=1, clay_bots=0, obsidian_bots=0, geode_bots=0, ore=0, clay=0, obsidian=0, geodes=0):
    if time_remaining == 0:
        return geodes

    possibilities = []

    ore += ore_bots
    clay += clay_bots
    obsidian += obsidian_bots
    geodes += geode_bots

    # do nothing
    possibilities.append((ore_bot_ore_cost, clay_bot_ore_cost, obsidian_bot_ore_cost, obsidian_bot_clay_cost, geode_bot_ore_cost, geode_bot_obsidian_cost, time_remaining-1, ore_bots, clay_bots,
                         obsidian_bots, geode_bots, ore, clay, obsidian, geodes))

    # buy ore bot
    if ore >= ore_bot_ore_cost:
        possibilities.append((ore_bot_ore_cost, clay_bot_ore_cost, obsidian_bot_ore_cost, obsidian_bot_clay_cost, geode_bot_ore_cost, geode_bot_obsidian_cost, time_remaining-1, ore_bots+1, clay_bots, obsidian_bots, geode_bots,
                             ore-ore_bot_ore_cost, clay, obsidian, geodes))

    # buy clay bot
    if ore >= clay_bot_ore_cost:
        possibilities.append((ore_bot_ore_cost, clay_bot_ore_cost, obsidian_bot_ore_cost, obsidian_bot_clay_cost, geode_bot_ore_cost, geode_bot_obsidian_cost, time_remaining-1, ore_bots, clay_bots+1, obsidian_bots, geode_bots,
                             ore-clay_bot_ore_cost, clay, obsidian, geodes))

    # buy obsidian bot
    if ore >= obsidian_bot_ore_cost and clay >= obsidian_bot_clay_cost:
        possibilities.append((ore_bot_ore_cost, clay_bot_ore_cost, obsidian_bot_ore_cost, obsidian_bot_clay_cost, geode_bot_ore_cost, geode_bot_obsidian_cost, time_remaining-1, ore_bots, clay_bots, obsidian_bots+1, geode_bots,
                             ore-obsidian_bot_ore_cost, clay-obsidian_bot_clay_cost, obsidian, geodes))

    # buy geode bot
    if ore >= geode_bot_ore_cost and obsidian >= geode_bot_obsidian_cost:
        possibilities.append((ore_bot_ore_cost, clay_bot_ore_cost, obsidian_bot_ore_cost, obsidian_bot_clay_cost, geode_bot_ore_cost, geode_bot_obsidian_cost, time_remaining-1, ore_bots, clay_bots, obsidian_bots, geode_bots+1,
                             ore-geode_bot_ore_cost, clay, obsidian-geode_bot_obsidian_cost, geodes))

    return max(map(lambda x: iterate(*x), possibilities))


if __name__ == "__main__":
    main()
