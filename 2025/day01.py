with open("2025/input01.txt") as f:
    l = [(-1 if x[0] == "L" else 1) * int(x[1:])
         for x in (x.rstrip() for x in f.readlines())]


curr = 50
zeros = 0
clicks = 0
for n in l:
    sign = n / abs(n)
    for i in range(abs(n)):
        curr += sign
        curr %= 100
        if curr == 0:
            clicks += 1
    if curr == 0:
        zeros += 1


print(zeros)
print(clicks)
