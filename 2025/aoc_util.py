import callee


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
