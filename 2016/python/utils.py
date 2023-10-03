
import os


def get_input(day):
    path = os.path.join(os.path.dirname(__file__), '..', 'inputs', f"{day}.txt")
    with open(path, 'r') as f:
        return f.read().strip()


def create_day(day):
    path = os.path.join(os.path.dirname(__file__), f"day{day}.py")
    with open(path, 'w') as f:
        f.close()

    path = os.path.join(os.path.dirname(__file__), '..', 'inputs', f"{day}.txt")

    with open(path, 'w') as f:
        f.close()


if __name__ == '__main__':
    day = input("Day: ")
    create_day(day)
