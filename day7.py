def convert_num(num):
    sum = 0
    for i in range(num + 1):
        sum += i

    return sum


input = [int(x) for x in open('input.txt', 'r').read().strip().split(',')]

total = {}
for i in range(2000):
    print(i)
    collect = []
    for item in input:
        move = abs(item - i)
        move = convert_num(move)  # part 2 added
        collect.append(move)

    total[i] = sum(collect)

curr_val = 1000000000000
lowest_key = 0

for k, v in total.items():
    if v < curr_val:
        curr_val = v
        lowest_key = k


print(lowest_key)
print(total[lowest_key])
