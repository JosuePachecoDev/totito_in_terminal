from random import randrange
from time import sleep

userMark = 'O'
pcMark = 'X'
grid = [[],[],[]]
run = True
freeCelds = 9

def displayBoard():
    global grid
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|   " + str(grid[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")

def userTurn():
    global grid, run, freeCelds
    while True:
        userMove = int(input('\n-- Ingresa tu próxima jugada: '))
        if userMove > 0 and userMove <= 9:
            if isTaken(userMove):
                print(f'La casilla {userMove} ya está marcada, prueba otra vez ↡')
                continue
            else:
                userMove -= 1
                grid[userMove//3][userMove%3] = userMark
                freeCelds -= 1
                break
        else:
            print(userMove, 'está fuera de rango, prueba otra vez ↡')
            continue

def pcTurn():
    global grid, run, freeCelds
    while True:
        pcMove = randrange(0, 9)
        if isTaken(pcMove+1):
            continue
        else:
            grid[pcMove//3][pcMove%3] = pcMark
            freeCelds-=1
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

def main():
    global run, winner, freeCelds
    for row in grid:
        for square in range(3):
            row.append(' ')
    
    while run:
        userTurn()
        if isWinner(userMark):
            run = False
            winner = 'user'
        elif freeCelds == 0:
            run = False
            winner = 'empate'
        else:
            sleep(1.5)
            pcTurn()
            if isWinner(pcMark):
                run = False
                winner = 'pc'
            elif freeCelds == 0:
                run = False
                winner = 'empate'
        displayBoard()

    match winner:
        case 'user':
            print("\n\nEL USUARIO GANA\n")
        case 'pc':
            print("\n\nLA PC GANA\n")
        case 'empate':
            print("\n\nESTO ES UN EMPATE\n")

if __name__ == '__main__':
    main()