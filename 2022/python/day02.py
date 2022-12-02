def main():
    with open("../inputs/day02.txt") as f:
        rounds = [line.rstrip().split(" ") for line in f.readlines()]

    print(run_tournament(rounds, strategy_1))
    print(run_tournament(rounds, strategy_2))


def run_tournament(rounds, strategy):
    return sum(map(lambda x: strategy[x[0]][x[1]], rounds))


strategy_1 = {
    "A": {
        "X": 1 + 3,
        "Y": 2 + 6,
        "Z": 3 + 0,
    },
    "B": {
        "X": 1 + 0,
        "Y": 2 + 3,
        "Z": 3 + 6,
    },
    "C": {
        "X": 1 + 6,
        "Y": 2 + 0,
        "Z": 3 + 3,
    }
}

strategy_2 = {
    "A": {
        "X": 0 + 3,
        "Y": 3 + 1,
        "Z": 6 + 2,
    },
    "B": {
        "X": 0 + 1,
        "Y": 3 + 2,
        "Z": 6 + 3,
    },
    "C": {
        "X": 0 + 2,
        "Y": 3 + 3,
        "Z": 6 + 1,
    }
}

if __name__ == "__main__":
    main()
