
code = [int(x) for x in open("input.txt").read().split(',')]


def run_code(setting, value_in):
    i = 0
    code_copy = code
    setting_given = False
    while True:
        op = code_copy[i]
        modes = []

        if len(str(op)) > 1 and op != 99:
            modes = [int(x) for x in str(op // 100)]
            modes.reverse()
            op = op % 10
        try:
            if len(modes) >= 1 and modes[0] == 1:
                p1 = code[i + 1]
            else:
                p1 = code[code[i+1]]
            if len(modes) >= 2 and modes[1] == 1:
                p2 = code[i+2]
            else:
                p2 = code[code[i+2]]
            if len(modes) >= 3 and modes[2] == 1:
                p3 = i + 3
            else:
                p3 = code[i+3]
        except IndexError:
            pass

        # ADD
        if op == 1:
            code[p3] = p1 + p2
            if code[p3] == i:
                continue
            else:
                i += 4

        # MULTIPLY
        elif op == 2:
            code[p3] = p1 * p2
            if code[p3] == i:
                continue
            else:
                i += 4

        # INPUT
        elif op == 3:
            if not setting_given:
                code[code[i+1]] = setting
                setting_given = True
            else:
                code[code[i+1]] = value_in
            i += 2

        # OUTPUT
        elif op == 4:
            output = p1
            break
            i += 2

        # JUMP IF TRUE
        elif op == 5:
            if p1 != 0:
                i = p2
                continue
            else:
                i += 3

        # JUMP IF FALSE
        elif op == 6:
            if p1 == 0:
                i = p2
                continue
            else:
                i += 3

        # LESS THAN
        elif op == 7:
            if p1 < p2:
                code[p3] = 1
            else:
                code[p3] = 0
            if code[p3] == i:
                continue
            else:
                i += 4

        # EQUAL TO
        elif op == 8:
            if p1 == p2:
                code[p3] = 1
            else:
                code[p3] = 0
            if code[p3] == i:
                continue
            else:
                i += 4

        # HALT
        elif op == 99:
            print()
            break

        else:
            print('something has gone wrong')
            break
    return output


def get_thruster_value(settings):
    A = run_code(settings[0], 0)
    B = run_code(settings[1], A)
    C = run_code(settings[2], B)
    D = run_code(settings[3], C)
    return run_code(settings[4], D)


current_max = 0

for a in range(5):
    for b in range(5):
        for c in range(5):
            for d in range(5):
                for e in range(5):
                    for i in [a, b, c, d, e]:
                        if len({a, b, c, d, e}) != 5:
                            break
                        current = get_thruster_value([a, b, c, d, e])
                        if current > current_max:
                            current_max = current
                            max_settings = [a,b,c,d,e]

part1 = current_max

current_max = 0


def feedback_loop(settings):
    current = get_thruster_value(settings)
    for i in range(10):
        A = run_code(settings[0], current)
        B = run_code(settings[1], A)
        C = run_code(settings[2], B)
        D = run_code(settings[3], C)
        current = run_code(settings[4], D)
        print(current)


feedback_loop([9,8,7,6,5])

for a in range(5, 10):
    for b in range(5, 10):
        for c in range(5, 10):
            for d in range(5, 10):
                for e in range(5, 10):
                    for i in [a, b, c, d, e]:
                        if len({a, b, c, d, e}) != 5:
                            break
                        current = get_thruster_value([a, b, c, d, e])
                        if current > current_max:
                            current_max = current
                            max_settings = [a,b,c,d,e]

part2 = current_max

print(part2)
