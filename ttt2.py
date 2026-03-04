from random import randrange
import time

def displayBoard(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

def userTurn(board):
    userMove = int(input('-- Ingresa es tu siguiente jugada: '))
    if userMove > 0 and userMove <= 9:
        if isTaken(userMove, board):
            print(userMove, 'ya está marcado, prueba otra vez ↡')
            userTurn(board)
        else:
            userMove -= 1
            row = userMove // 3
            col = userMove % 3
            board[row][col] = userMark
    else:
        print(userMove, 'está fuera de rango, prueba otra vez ↡')
        userTurn(board)

def pcTurn(board):
    while True:
        pcMove = randrange(0, 9)
        row = pcMove // 3
        col = pcMove % 3
        if isTaken(pcMove+1, board):
            continue
        else:
            board[row][col] = pcMark
            break

def isWinner(board, sign):
    if (board[0][0] == sign and board[0][1] == sign and board[0][2] == sign) or (board[1][0] == sign and board[1][1] == sign and board[1][2] == sign) or (board[2][0] == sign and board[2][1] == sign and board[2][2] == sign) or (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) or (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign) or (board[0][2] == sign and board[1][1] == sign and board[2][0]) or (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign):
        return True
    return False

def isTaken(move, board):
    row = (move - 1) // 3
    col = (move - 1) % 3
    if board[row][col] == userMark or board[row][col] == pcMark:
        return True
    return False
# # ----------------------------------------
userMark = 'O'
pcMark = 'X'
grid = [[], [], []]

sc = 1 #variable para el icono
for row in grid:
    for square in range(3):
        row.append('-')
        if sc != 9:
            sc += 1

freeCelds = sc
while freeCelds != 0:
    if isWinner(grid, userMark):
        displayBoard(grid)
        print('Jugador gana')
        break
    elif isWinner(grid, pcMark):
        displayBoard(grid)
        print('Pc gana')
        break
    else:
        displayBoard(grid)
        userTurn(grid)
        time.sleep(2)
        pcTurn(grid)
        freeCelds -= 1
else:
    displayBoard(grid)
    print('esto es un empate')