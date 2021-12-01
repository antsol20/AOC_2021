input = []

f = open('input.txt', 'r')

for line in f:
    input.append(int(line.strip()))


counter = 0
for i in range(1, len(input)):
    if input[i] > input[i - 1]:
        counter += 1

print(counter)

counter = 0
for i in range(3, len(input)):
    window1 = input[i] + input[i - 1] + input[i - 2]
    window2 = input[i - 1] + input[i - 2] + input[i - 3]
    if window1 > window2:
        counter += 1

print(counter)
