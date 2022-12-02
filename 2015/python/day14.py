import re


class Reindeer:
    def __init__(self, name, speed, duration, rest):
        self.name = name
        self.speed = speed
        self.duration = duration
        self.remaining_duration = duration
        self.rest = rest
        self.remaining_rest = 0
        self.distance = 0
        self.points = 0

    def increment(self):
        if self.remaining_rest > 0:
            self.remaining_rest -= 1
            return

        if self.remaining_duration == 0:
            self.remaining_rest = self.rest - 1
            self.remaining_duration = self.duration
            return

        self.remaining_duration -= 1
        self.distance += self.speed

    def reset(self):
        self.remaining_duration = self.duration
        self.remaining_rest = 0
        self.distance = 0

    def give_score(self, max_distance: int):
        if self.distance == max_distance:
            self.points += 1


def part1(contestants: list[Reindeer], rounds: int):
    for _ in range(rounds):
        for c in contestants:
            c.increment()

    return max(map(lambda x: x.distance, contestants))


def part2(contestants: list[Reindeer], rounds: int):
    for _ in range(rounds):
        for c in contestants:
            c.increment()

        max_distance = max(map(lambda x: x.distance, contestants))
        for c in contestants:
            c.give_score(max_distance)

    return max(map(lambda x: x.points, contestants))


def main():
    contestants: list[Reindeer] = []
    with open('inputs/day14.txt') as f:
        for line in f.readlines():
            name, speed, duration, rest = re.findall(
                r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.", line)[0]

            contestants.append(Reindeer(name, int(speed), int(duration), int(rest)))

    ROUNDS = 2503

    print(part1(contestants, ROUNDS))

    for c in contestants:
        c.reset()

    print(part2(contestants, ROUNDS))


if __name__ == "__main__":
    main()
