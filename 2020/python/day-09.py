import time
start_time = time.time()

numbers = [int(x.rstrip()) for x in open("input-09.txt").readlines()]


preample_len = 25

window = []
for i in numbers[:preample_len]:
    window.insert(0, i)

weakness = 0

for i in numbers[preample_len:]:
    has_complement = False
    for value in window:
        complement = i - value
        if complement in window:
            has_complement = True
    if has_complement:
        window.pop()
        window.insert(0, i)
    else:
        weakness = i
        print("Part 1:", i)
        break


for i in range(len(numbers)):

    curr_sum = numbers[i] 
    found = False
    j = i + 1
    while j <= len(numbers): 
        
        if curr_sum == weakness:
            print("Part 2:", (min(numbers[i:j-1]) + max(numbers[i:j-1])))
            found = True
            break

        if curr_sum > weakness or j == len(numbers): 
            break
            
        curr_sum = curr_sum + numbers[j] 
        j += 1
    if found:
        break

end_time = round((time.time() - start_time) * 1000, 2)
print(f"Solved in: {end_time}ms" )