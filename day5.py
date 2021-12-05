def main():
    input = []
    f = open('input.txt', 'r')

    grid = []
    for i in range(999):
        grid.append([0] * 999)

    for line in f:
        points = line.strip().split(' -> ')
        x1, y1 = points[0].split(',')
        x2, y2 = points[1].split(',')
        input.append((int(x1), int(y1), int(x2), int(y2)))

    for entry in input:
        if entry[0] == entry[2]:  # then vertical

            if entry[3] >= entry[1]:  # then going down
                for i in range(entry[1], entry[3] + 1):
                    grid[i][entry[0]] += 1

            if entry[1] > entry[3]:  # then going up
                for i in range(entry[3], entry[1] + 1):
                    grid[i][entry[0]] += 1

        if entry[1] == entry[3]:  # then horiz
            if entry[0] >= entry[2]:  # then going r2l
                for i in range(entry[2], entry[0] + 1):
                    grid[entry[1]][i] += 1

            if entry[2] > entry[0]:  # then going l2r
                for i in range(entry[0], entry[2] + 1):
                    grid[entry[1]][i] += 1

        if entry[0] != entry[2] and entry[1] != entry[3]:  # diag

            if entry[0] > entry[2] and entry[3] > entry[1]:
                for i in range(entry[0] - entry[2] + 1):
                    grid[entry[0] - i][entry[1] + i] += 1

            if entry[2] > entry[0] and entry[1] > entry[3]:
                for i in range(entry[2] - entry[0] + 1):
                    grid[entry[0] + i][entry[1] - i] += 1

            if entry[2] > entry[0] and entry[3] > entry[1]:
                for i in range(entry[2] - entry[0] + 1):
                    grid[entry[0] + i][entry[1] + i] += 1

            if entry[0] > entry[2] and entry[1] > entry[3]:
                for i in range(entry[0] - entry[2] + 1):
                    grid[entry[0] - i][entry[1] - i] += 1

    counter = 0
    for row in grid:
        for element in row:
            if element > 1:
                counter += 1

    print(counter)


if __name__ == '__main__':
    main()
