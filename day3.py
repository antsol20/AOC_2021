input = []

f = open('input.txt', 'r')

for line in f:
    input.append((line.strip()))

gamma = ""

for i in range(12):

    zeroes = 0
    ones = 0

    for line in input:
        if line[i] == "0":
            zeroes += 1
        else:
            ones += 1

    if zeroes > ones:
        gamma += "0"
    else:
        gamma += "1"

epsilon = ""
for chr in gamma:
    if chr == "0":
        epsilon += "1"
    else:
        epsilon += "0"


gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma, epsilon, gamma*epsilon)


zeroes = 0
ones = 0
zero_locs = []
one_locs = []

for idx, line in enumerate(input):
    if line[0] == "0":
        zeroes += 1
        zero_locs.append(idx)
    else:
        ones += 1
        one_locs.append(idx)

if zeroes > ones:
    gamma += "0"
else:
    gamma += "1"
