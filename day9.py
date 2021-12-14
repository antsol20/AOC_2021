input = []

f = open('input.txt', 'r')

for line in f:
    row = []
    for chr in line.strip():
       if chr != '\n':
          row.append(chr)

    input.append(row)

#100 x 100

print(len(input[0]))

# for row, row_item in enumerate(input):
#     for col, col_item in enumerate(row_item):
#         if input[row - 1][col] > col_item:
#             continue

#         if input[row][col + 1] > col_item:
#             continue

#         if input[row + 1][col] > col_item:
#             continue

#         if input[row][col - 1] > col_item:
#             continue



  