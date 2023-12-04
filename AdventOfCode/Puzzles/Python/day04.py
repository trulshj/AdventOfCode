def parse_line(line):
    card_part, numbers_part = line.split(':')
    winning, have = [numbers.split() for numbers in numbers_part.split('|')]
    return int(card_part.split()[-1]), winning, have


def number_of_winnings(winning, have):
    return sum(1 for n in have if n in winning)


def card_score(card):
    return 2 ** (card[1] - 1) if card[1] > 0 else 0


def main():
    with open("../../Inputs/04.txt", "r") as f:
        lines = list(map(parse_line, f.readlines()))

    winnings = {card_number: number_of_winnings(
        winning, have) for card_number, winning, have in lines}

    print("Part 1:", sum(map(card_score, winnings.items())))

    copies = {card_number: 1 for card_number, _, _ in lines}

    for card_number, wins in winnings.items():
        for i in range(1, wins + 1):
            copies[card_number + i] += copies[card_number]

    print("Part 2:", sum(copies.values()))


if __name__ == "__main__":
    main()
