# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Your Name Here
# Created: YYYY-MM-DD

symbol = [" ", "x", "o"]


def printRow(row):
    # initialize output to the left border
    # for each square in the row...
    # add to output the symbol for this square followed by a border
    # print the completed output for this row
    output = '|'
    for val in row:
        if val == 0:
            print_val = symbol[val]
        elif val == 1:
            print_val = symbol[val]
        else:
            print_val = symbol[val]
        output += str(print_val) + '|'
    print(output)


def printSeparator():
    print("+-+-+-+")


def printBoard(board):
    # print the top border
    # for each row in the board...
    # print the row
    # print the next border
    printSeparator()
    for row in board:
        printRow(row)
        printSeparator()


def markBoard(board, row, col, player):
    # check to see whether the desired square is blank
    # if so, set it to the player number
    if board[row][col] == 0:
        board[row][col] = player
        return True
    else:
        print("Square already marked by player", board[row][col], "choose another square.")
        row, col = getPlayerMove()
        markBoard(board, row, col, player)


def getPlayerMove():
    row = 10
    col = 10
    while row > 2 or col > 2:
        # prompt the user separately for the row and column numbers
        row = int(input("Enter the row of the square you would like to mark: "))
        col = int(input("Enter the column of the square you would like to mark: "))
    return row, col  # then return that row and column instead of (0,0)


def hasBlanks(board):
    # for each row in the board...
    # for each square in the row...
    # check whether the square is blank
    # if so, return True
    for row in board:
        for val in row:
            if val == 0:
                return True  # if no square is blank, return False
    return False


def checkVictory(board):
    v1 = checkVictoryH(board)
    v2 = checkVictoryV(board)
    v3 = checkVictoryD(board)
    victory = 0
    if v1 == 1 or v2 == 1 or v3 == 1:
        victory = 1
    elif v1 == 2 or v2 == 2 or v3 == 2:
        victory = 2
    return victory


def checkVictoryH(board):
    for row in board:
        p1_count = 0
        p2_count = 0
        for val in row:
            if val == 0:
                pass
            elif val == 1:
                p1_count += 1
            elif val == 2:
                p2_count += 1
            else:
                pass
        if p1_count == 3:
            print('Player one wins, congratulations!')
            return 1
        elif p2_count == 3:
            print('Player two wins, congratulations!')
            return 2
        else:
            pass
    return 0


def checkVictoryV(board):
    for col in range(0, len(board[0])):
        p1_count = 0
        p2_count = 0
        for row in range(0, len(board[0])):
            if board[row][col] == 0:
                pass
            elif board[row][col] == 1:
                p1_count += 1
            elif board[row][col] == 2:
                p2_count += 1
            else:
                pass
        if p1_count == 3:
            print('Player one wins, congratulations!')
            return 1
        elif p2_count == 3:
            print('Player two wins, congratulations!')
            return 2
        else:
            pass
    return 0


def checkVictoryD(board):
    if board[0][0] == board [1][1] == board[2][2]:
        if board[0][0] == 1:
            print('Player one wins, congratulations!')
            return 1
        elif board[0][0] == 2:
            print('Player two wins, congratulations!')
            return 2
        else:
            pass
    if board[0][2] == board [1][1] == board[2][0]:
        if board[0][2] == 1:
            print('Player one wins, congratulations!')
            return 1
        elif board[0][2] == 2:
            print('Player two wins, congratulations!')
            return 2
        else:
            pass
    return 0


def main():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    player = 1
    while hasBlanks(board):
        row, col = getPlayerMove()
        markBoard(board, row, col, player)
        printBoard(board)
        victory = checkVictory(board)
        if victory == 1 or victory == 2:
            quit()
        player = player % 2 + 1  # switch player for next turn



main()
