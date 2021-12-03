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

oxyinput = input
co2input = input

for i in range(12):
    zeroes = 0
    ones = 0
    zero_locs = []
    one_locs = []

    for idx, line in enumerate(oxyinput):
        if line[i] == "0":
            zeroes += 1
            zero_locs.append(idx)
        else:
            ones += 1
            one_locs.append(idx)


    new = []
    if zeroes > ones:
        for row in zero_locs:
            new.append(oxyinput[row])
    else:
        for row in one_locs:
            new.append(oxyinput[row])

    oxyinput = new

oxygen = int(oxyinput[0], 2)

for i in range(12):
    if len(co2input) == 1:
        continue

    zeroes = 0
    ones = 0
    zero_locs = []
    one_locs = []

    for idx, line in enumerate(co2input):
        if line[i] == "0":
            zeroes += 1
            zero_locs.append(idx)
        else:
            ones += 1
            one_locs.append(idx)


    new = []
    if zeroes <= ones:
        for row in zero_locs:
            new.append(co2input[row])
    else:
        for row in one_locs:
            new.append(co2input[row])

    co2input = new


co2 = int(co2input[0], 2)

print(oxygen)
print(co2)

print(oxygen*co2)
