import utils.callee as callee
from utils.time import start_timer


def print_title():
    _, day = callee.get_caller_info()
    print(f" AoC 2025 - Day {day} ".center(32, '#'))


def start():
    print_title()
    return start_timer()


def p1(data):
    print("Part 1:", data)


def p2(data):
    print("Part 2:", data)


def read():
    with open(callee.get_input_path()) as f:
        return f.read()


def readlines():
    with open(callee.get_input_path()) as f:
        return f.readlines()


def lines():
    with open(callee.get_input_path()) as f:
        return [x.rstrip() for x in f.readlines()]


def sections():
    with open(callee.get_input_path()) as f:
        return (x.split() for x in f.read().split("\n\n"))
