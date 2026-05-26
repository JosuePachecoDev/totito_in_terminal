from random import randrange
from time import sleep

userMark = 'O'
pcMark = 'X'
icon = ' '
grid = [[],[],[]]
run = True

def displayBoard():
    global grid

    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {grid[0][0]}   |   {grid[0][1]}   |   {grid[0][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {grid[1][0]}   |   {grid[1][1]}   |   {grid[1][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {grid[2][0]}   |   {grid[2][1]}   |   {grid[2][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

def userTurn():
    global grid, run
    while True:
        userMove = int(input('\n-- Ingresa es tu próxima jugada: '))
        if userMove > 0 and userMove <= 9:
            if isTaken(userMove):
                print(f'La casilla {userMove} ya está marcada, prueba otra vez ↡')
                continue
            else:
                userMove -= 1
                grid[userMove//3][userMove%3] = userMark
                break
        else:
            print(userMove, 'está fuera de rango, prueba otra vez ↡')
            continue

def pcTurn():
    global grid, run
    while True:
        pcMove = randrange(0, 9)
        if isTaken(pcMove+1):
            continue
        else:
            grid[pcMove//3][pcMove%3] = pcMark
            break

def isWinner(sign):
    global grid
    if grid[0][0] == sign and grid[0][1] == sign and grid[0][2] == sign: return True
    elif grid[1][0] == sign and grid[1][1] == sign and grid[1][2] == sign: return True
    elif grid[2][0] == sign and grid[2][1] == sign and grid[2][2] == sign: return True
    elif grid[0][0] == sign and grid[1][0] == sign and grid[2][0] == sign: return True
    elif grid[0][1] == sign and grid[1][1] == sign and grid[2][1] == sign: return True
    elif grid[0][2] == sign and grid[1][2] == sign and grid[2][2] == sign: return True
    elif grid[0][2] == sign and grid[1][1] == sign and grid[2][0] == sign: return True
    elif grid[0][0] == sign and grid[1][1] == sign and grid[2][2] == sign: return True

    return False

def isTaken(move):
    global grid
    if grid[(move - 1) // 3][(move - 1) % 3] == userMark or grid[(move - 1) // 3][(move - 1) % 3] == pcMark:
        return True
    return False
# # ----------------------------------------
for row in grid:
    for square in range(3):
        row.append(' ')

while run:
    userTurn()
    if isWinner(userMark): run = False
    else:
        sleep(1.5)
        pcTurn()
        if isWinner(pcMark): run = False
    displayBoard()

print('\n   FIN DEL JUEGO')