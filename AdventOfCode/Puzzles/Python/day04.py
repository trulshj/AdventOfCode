import re


def parse_line(line):
    card_id, *numbers = [int(n) for n in re.findall(r'(\d+)', line)]
    wins = len(numbers) - len(set(numbers))
    return card_id, wins


def card_score(card):
    return 2 ** (card[1] - 1) if card[1] > 0 else 0


def main():
    with open("../../Inputs/04.txt", "r") as f:
        cards = list(map(parse_line, f.readlines()))

    winnings = {card_id: wins for card_id, wins in cards}

    print("Part 1:", sum(map(card_score, winnings.items())))

    copies = {card_number: 1 for card_number, _ in cards}

    for card_number, wins in winnings.items():
        for i in range(1, wins + 1):
            copies[card_number + i] += copies[card_number]

    print("Part 2:", sum(copies.values()))


if __name__ == "__main__":
    main()
