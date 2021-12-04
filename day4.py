
SOLVE = ['X', 'X', 'X', 'X', 'X']


def check_board_solved(board):
    for row in board:
        if row == SOLVE:
            return True

    for i in range(5):
        col = []
        for j in range(5):
            col.append(board[j][i])

        if col == SOLVE:
            return True

    return False


def get_score(board, last_draw):
    sum = 0
    for row in board:
        for num in row:
            if type(num) != str:
                sum += num

    return sum*last_draw


def main():
    input = []
    f = open('input.txt', 'r')

    for line in f:
        input.append((line.strip()))

    draws = input[0].split(',')
    draws = [int(x) for x in draws]

    boards = []
    board = []

    for i in range(1, len(input)):
        if input[i] == "":
            boards.append(board)
            board = []

        else:
            nums = [int(x) for x in input[i].split()]
            board.append(nums)

    # num_boards = list(range(len(boards)))

    for draw in draws:
        for b in range(len(boards)):
            for i in range(5):
                for j in range(5):
                    if boards[b][j][i] == draw:
                        boards[b][j][i] = 'X'
                        if b == 64 and check_board_solved(boards[b]):
                            print(get_score(boards[b], draw))
                            return
                        # if len(num_boards) == 1:
                        #     print(num_boards)    ## board 64 found to be last
                        #     return
                        #
                        # if check_board_solved(boards[b]):
                        #     if b in num_boards:
                        #         num_boards.remove(b)


if __name__ == '__main__':
    main()
