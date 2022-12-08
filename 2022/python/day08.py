from utils import print_day
import numpy as np

DAY = 8


def main():
    print_day(DAY, part1, part2, get_data)


def get_data():
    with open(f"/Users/trulshj/dev/aoc/2022/inputs/day{DAY:02}.txt") as f:
        return [list(x.strip()) for x in f.readlines()]


def part1(data):
    trees = np.array(data, int)
    visible_trees = np.zeros_like(trees, bool)

    for _ in range(4):
        for x, y in np.ndindex(trees.shape):
            shorter_trees = [tree < trees[x, y] for tree in trees[x, y+1:]]

            if all(shorter_trees):
                visible_trees[x, y] = True

        trees = np.rot90(trees)
        visible_trees = np.rot90(visible_trees)

    return visible_trees.sum()


def part2(data):
    trees = np.array(data, int)
    scenic_trees = np.ones_like(trees, int)

    for _ in range(4):
        for x, y in np.ndindex(trees.shape):
            shorter_trees = [tree < trees[x, y] for tree in trees[x, y+1:]]

            viewing_distance = next((i+1 for i, t in enumerate(shorter_trees) if not t), len(shorter_trees))
            scenic_trees[x, y] *= viewing_distance

        trees = np.rot90(trees)
        scenic_trees = np.rot90(scenic_trees)

    return scenic_trees.max()


if __name__ == "__main__":
    main()
