input = []

f = open('input.txt', 'r')

for line in f:
    input.append((line.strip()))


mapping = {
    0: 6,
    1: 2,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6

}

unqiue = [2, 4, 3, 7]

sum = 0
for row in input:
    vals = row.split('|')[1].strip()
    for val in vals.split():
        if len(val) in unqiue:
            sum += 1
            print(val)

print(sum)

