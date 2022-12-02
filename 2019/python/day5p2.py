
code = [int(x) for x in open("input.txt").read().split(',')]
i = 0
input_code = 5

while True:
    op = code[i]
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

    if op == 1:
        code[p3] = p1 + p2
        if code[p3] == i:
            continue
        else:
            i += 4

    elif op == 2:
        code[p3] = p1 * p2
        if code[p3] == i:
            continue
        else:
            i += 4

    elif op == 3:
        code[code[i+1]] = input_code
        i += 2

    elif op == 4:
        print(f"Output: {p1}")
        i += 2

    elif op == 5:
        if p1 != 0:
            i = p2
            continue
        else:
            i += 3

    elif op == 6:
        if p1 == 0:
            i = p2
            continue
        else:
            i += 3

    elif op == 7:
        if p1 < p2:
            code[p3] = 1
        else:
            code[p3] = 0
        if code[p3] == i:
            continue
        else:
            i += 4

    elif op == 8:
        if p1 == p2:
            code[p3] = 1
        else:
            code[p3] = 0
        if code[p3] == i:
            continue
        else:
            i += 4

    elif op == 99:
        print('halting')
        break

    else:
        print('no op')
        break
