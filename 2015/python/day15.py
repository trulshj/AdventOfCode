import re
import itertools
import numpy as np
from math import inf


class Ingredient:
    def __init__(self, name: str, capacity: int, durability: int, flavor: int, texture: int, calories: int):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def calculate(self, amount: int):
        return np.asarray([
            self.capacity * amount,
            self.durability * amount,
            self.flavor * amount,
            self.texture * amount
        ])

    def get_calories(self, amount: int):
        return self.calories * amount

    def __str__(self) -> str:
        return f"{self.name}: capacity {self.capacity}, durability {self.durability}, flavor {self.flavor}, texture {self.texture}, calories {self.calories}"


def find_best_cookies(ingredients: list[Ingredient]):
    max_result = -inf
    max_result_calories = -inf
    for combination in itertools.combinations(range(101), len(ingredients)):
        if sum(combination) == 100:
            for perm in itertools.permutations(combination):
                res = np.zeros(4, dtype=int)
                calories = 0
                for i in range(len(ingredients)):
                    res += ingredients[i].calculate(perm[i])
                    calories += ingredients[i].get_calories(perm[i])

                if (res < 0).any():
                    res.fill(0)

                max_result = max(max_result, res.prod())

                if (calories == 500):
                    max_result_calories = max(max_result_calories, res.prod())

    print("Part 1:", max_result)
    print("Part 2:", max_result_calories)


def main():
    ingredients: list[Ingredient] = []

    with open('inputs/day15.txt') as f:
        for line in f.readlines():
            name, capacity, durability, flavor, texture, calories = re.findall(
                r"(\w+): capacity (-?\d), durability (-?\d), flavor (-?\d), texture (-?\d), calories (-?\d)", line)[0]
            ingredients.append(Ingredient(name, int(capacity), int(
                durability), int(flavor), int(texture), int(calories)))

    find_best_cookies(ingredients)


if __name__ == "__main__":
    main()
