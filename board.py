# TODO: Draw board from current list of gameplay (3x3 array/list)

def checkDraw(gameState: list):
    fullBoard = True
    for i in range(3):
        for j in range(3):
            if gameState[i][j] == '':
                fullBoard = False
                break
    return fullBoard


def checkWinner(gameState: list): # Is it the AI turn (maximizing X) or ours (O)
        
    # Diagonal
    if gameState[0][0] == 'X' and gameState[1][1] == 'X' and gameState[2][2] == 'X':
        return 9999 # Maximizing Player
    elif gameState[0][2] == 'X' and gameState[1][1] == 'X' and gameState[2][0] == 'X':
        return 9999 # Because or logic is too long
    # Horizontal
    elif gameState[0][0] == 'X' and gameState[0][1] == 'X' and gameState[0][2] == 'X':
        return 9999
    elif gameState[1][0] == 'X' and gameState[1][1] == 'X' and gameState[1][2] == 'X':
        return 9999
    elif gameState[2][0] == 'X' and gameState[2][1] == 'X' and gameState[2][2] == 'X':
        return 9999
    # Vertical
    elif gameState[0][0] == 'X' and gameState[1][0] == 'X' and gameState[2][0] == 'X':
        return 9999
    elif gameState[0][1] == 'X' and gameState[1][1] == 'X' and gameState[2][1] == 'X':
        return 9999
    elif gameState[0][2] == 'X' and gameState[1][2] == 'X' and gameState[2][2] == 'X':
        return 9999
    # O
    elif gameState[0][0] == 'O' and gameState[1][1] == 'O' and gameState[2][2] == 'O':
        return -9999 # Maximizing Player
    elif gameState[0][2] == 'O' and gameState[1][1] == 'O' and gameState[2][0] == 'O':
        return -9999 # Because or logic is too long
    # Horizontal
    elif gameState[0][0] == 'O' and gameState[0][1] == 'O' and gameState[0][2] == 'O':
        return -9999
    elif gameState[1][0] == 'O' and gameState[1][1] == 'O' and gameState[1][2] == 'O':
        return -9999
    elif gameState[2][0] == 'O' and gameState[2][1] == 'O' and gameState[2][2] == 'O':
        return -9999
    # Vertical
    elif gameState[0][0] == 'O' and gameState[1][0] == 'O' and gameState[2][0] == 'O':
        return -9999
    elif gameState[0][1] == 'O' and gameState[1][1] == 'O' and gameState[2][1] == 'O':
        return -9999
    elif gameState[0][2] == 'O' and gameState[1][2] == 'O' and gameState[2][2] == 'O':
        return -9999
    else:
        return 0 # Minimizing player only wants < 0 anyway

def drawBoard(gameState: list):
    # board = [
    #     ['X', '', ''],
    #     ['', 'O', ''],
    #     ['', 'X', '']
    # ]
    top_bottom = '____' * 3
    print(top_bottom)
    for rows in range(3):
        
        # Loop each cols in rows I
        if rows != 0:
            print()
            print(top_bottom, end='')
            print()
        
        for cols in range(3):
            # 1 cell
            
            print('| ', end='')
            if gameState[rows][cols] == '':
                print(' ', end=' ')
            elif gameState[rows][cols] == 'X':
                print('X', end=' ')
            elif gameState[rows][cols] == 'O':
                print('O', end=' ')
            else:
                print()
            
            if cols == 2:
                print('| ', end='')     
            # / 1 cell
    print('\n' + top_bottom)
    
            
            