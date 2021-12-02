input = []

f = open('input.txt', 'r')

for line in f:
    input.append((line.strip()))

horiz = 0
depth = 0
aim = 0

for line in input:
    ins, num = line.split()
    num = int(num)

    if ins == 'forward':
        horiz += num
        depth += (aim * num)
    elif ins == 'down':
        aim += num
        # depth += number
    elif ins == 'up':
        # depth -= number
        aim -= num

print(horiz, depth)
print(horiz * depth)
