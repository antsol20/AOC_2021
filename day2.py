input = []

f = open('input.txt', 'r')

for line in f:
    input.append((line.strip()))

horiz = 0
depth = 0
aim = 0

for line in input:
    words = line.split(' ')
    number = int(words[1])

    if words[0] == 'forward':
        horiz += number
        depth += (aim * number)
    elif words[0] == 'down':
        aim += number
        # depth += number
    elif words[0] == 'up':
        # depth -= number
        aim -= number

print(horiz, depth)
print(horiz * depth)
