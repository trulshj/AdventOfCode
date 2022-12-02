from dataclasses import dataclass
import math


@dataclass
class Spell:
    name: str
    mana_cost: int
    damage: int
    healing: int
    armor: int
    mana_restore: int
    duration: int


min_spent = math.inf


def simulate_round(players_turn: bool, all_spells: list[Spell], spells: list[Spell], player_hitpoints, player_mana, boss_hitpoints, boss_damage, spent_mana: int):
    player_mana += sum(spell.mana_restore for spell in spells)
    player_hitpoints += sum(spell.healing for spell in spells)
    damage = sum(spell.damage for spell in spells)
    armor = sum(spell.armor for spell in spells)

    boss_hitpoints -= damage
    if boss_hitpoints <= 0:
        print(spent_mana)
        return

    # Reduce duration for each spell
    spells = map(lambda x: Spell(x.name, x.mana_cost, x.damage, x.healing,
                 x.armor, x.mana_restore, x.duration - 1), spells)

    # Remove spells that have expired
    spells = list(filter(lambda spell: spell.duration > 0, spells))

    if players_turn:
        # what spells can we afford that aren't running?
        running_spell_names = list(map(lambda spell: spell.name, spells))
        for spell in all_spells:
            if spell.name not in running_spell_names and spell.mana_cost <= player_mana:
                new_spells = spells + [Spell(spell.name, spell.mana_cost, spell.damage,
                                             spell.healing, spell.armor, spell.mana_restore, spell.duration)]
                simulate_round(False, all_spells, new_spells,
                               player_hitpoints, player_mana, boss_hitpoints, boss_damage, spent_mana + spell.mana_cost)

    else:
        player_hitpoints -= max(boss_damage - armor, 1)
        if player_hitpoints <= 0:
            return
        simulate_round(True, all_spells, spells, player_hitpoints, player_mana, boss_hitpoints, boss_damage, spent_mana)


def part1(boss_hitpoints, boss_damage, all_spells):
    global min_spent
    simulate_round(True, all_spells, [], 50, 500, boss_hitpoints, boss_damage, 0)
    return min_spent


def part2():
    pass


def main():
    with open('inputs/day22.txt') as f:
        boss_hitpoints, boss_damage = [int(x.rstrip().split()[-1]) for x in f.readlines()]

    all_spells = [
        Spell("Magic Missile", 53, 4, 0, 0, 0, 1),
        Spell("Drain", 73, 2, 2, 0, 0, 1),
        Spell("Shield", 113, 0, 0, 7, 0, 6),
        Spell("Poison", 173, 3, 0, 0, 0, 6),
        Spell("Recharge", 229, 0, 0, 0, 101, 5)
    ]

    print(part1(boss_hitpoints, boss_damage, all_spells))
    print(part2())


if __name__ == "__main__":
    main()
