from dataclasses import dataclass
import itertools
import math


@dataclass
class Item:
    name: str
    cost: int
    damage: int
    armor: int


@dataclass
class Character:
    hitpoints: int
    damage: int
    armor: int


def player_wins(player: Character, boss: Character):
    if (boss.armor >= player.damage):
        return False

    if (player.armor >= boss.damage and player.damage > boss.armor):
        return True

    while player.hitpoints > 0 and boss.hitpoints > 0:
        boss.hitpoints -= player.damage - boss.armor
        if boss.hitpoints <= 0:
            return True

        player.hitpoints -= boss.damage - player.armor
        if player.hitpoints <= 0:
            return False


def part1(weapons: list[Item], armors: list[Item], rings: list[Item], boss: Character):
    lowest_cost = math.inf
    for weapon in weapons:
        for armor in armors:
            for ring1, ring2 in itertools.combinations(rings, 2):
                total_damage = weapon.damage + armor.damage + ring1.damage + ring2.damage
                total_armor = weapon.armor + armor.armor + ring1.armor + ring2.armor
                player = Character(100, total_damage, total_armor)
                if player_wins(player, Character(boss.hitpoints, boss.damage, boss.armor)):
                    total_cost = weapon.cost + armor.cost + ring1.cost + ring2.cost
                    lowest_cost = min(lowest_cost, total_cost)
    return lowest_cost


def part2(weapons: list[Item], armors: list[Item], rings: list[Item], boss: Character):
    highest_cost = -math.inf
    for weapon in weapons:
        for armor in armors:
            for ring1, ring2 in itertools.combinations(rings, 2):
                total_damage = weapon.damage + armor.damage + ring1.damage + ring2.damage
                total_armor = weapon.armor + armor.armor + ring1.armor + ring2.armor
                player = Character(100, total_damage, total_armor)
                if not player_wins(player, Character(boss.hitpoints, boss.damage, boss.armor)):
                    total_cost = weapon.cost + armor.cost + ring1.cost + ring2.cost
                    highest_cost = max(highest_cost, total_cost)
    return highest_cost


def main():
    with open('inputs/day21.txt') as f:
        data = [int(x.split()[-1]) for x in f.readlines()]

    boss = Character(data[0], data[1], data[2])

    weapons = [
        Item("Dagger", 8, 4, 0),
        Item("Shortsword", 10, 5, 0),
        Item("Warhammer", 25, 6, 0),
        Item("Longsword", 40, 7, 0),
        Item("Greataxe", 74, 8, 0)
    ]
    armors = [
        Item("No Armor", 0, 0, 0),
        Item("Leather", 13, 0, 1),
        Item("Chainmail", 31, 0, 2),
        Item("Splintmail", 53, 0, 3),
        Item("Bandedmail", 75, 0, 4),
        Item("Platemail", 102, 0, 5)
    ]
    rings = [
        Item("No Ring", 0, 0, 0),
        Item("No Ring", 0, 0, 0),
        Item("Damage +1", 25, 1, 0),
        Item("Damage +2", 50, 2, 0),
        Item("Damage +3", 100, 3, 0),
        Item("Defense +1", 20, 0, 1),
        Item("Defense +2", 40, 0, 2),
        Item("Defense +3", 80, 0, 3)
    ]

    print(part1(weapons, armors, rings, boss))
    print(part2(weapons, armors, rings, boss))


if __name__ == "__main__":
    main()
