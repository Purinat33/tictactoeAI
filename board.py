def checkDraw(gameState: list):
    fullBoard = True
    for i in range(3):
        for j in range(3):
            if gameState[i][j] == '':
                fullBoard = False
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
        return 0 

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
    
            
def heuristic(gameState): # Evaluation function for Minimax (Only AI need this )
    # Check for win and draw, if not then we evaluate this 
    
    if checkWinner(gameState) == 9999:
        return 10 # AI Wins
    elif checkWinner(gameState) == -9999:
        return -10 # Player Wins
    elif checkDraw(gameState):
        return 0
    elif not checkDraw(gameState) and checkWinner(gameState) == 0:
        X_score = 0
        O_score = 0
        # This will always be 1 (because X starts first then O and alternating)
        # for i in range(3):
        #     for j in range(3):
        #         if gameState[i][j] == 'O':
        #             O_count += 1;
        #         elif gameState[i][j] == 'X':
        #             X_count += 1;
        # return X_count - O_count
        
        # We will give different weight to center, corners and edge
        # Center - 4, edge - 1, corners = 3 but if you place next to a neigbour that cell = 2
        # Weights for cells (consistent for both 'X' and 'O')
        cell_weights = [
            [3, 2, 3],
            [2, 4, 2],
            [3, 2, 3]
        ]

        for i in range(3):
            for j in range(3):
                if gameState[i][j] == 'X':
                    X_score += cell_weights[i][j]
                elif gameState[i][j] == 'O':
                    O_score += cell_weights[i][j]
                    
        # Consider move with 2 adjacents same symbols (Almost winning)

        return X_score - O_score
    
    
def minimax(gameState, depth, isMaximizing, alpha, beta):
    if checkWinner(gameState) == 9999:
        return 10  # AI Wins
    elif checkWinner(gameState) == -9999:
        return -10  # Player Wins
    elif checkDraw(gameState):
        return 0

    if isMaximizing:
        maxEval = -float('inf')
        for i in range(3):
            for j in range(3):
                if gameState[i][j] == '':
                    gameState[i][j] = 'X'
                    eval = minimax(gameState, depth + 1, False, alpha, beta)
                    gameState[i][j] = ''
                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  # Alpha-beta pruning
        return maxEval
    else:
        minEval = float('inf')
        for i in range(3):
            for j in range(3):
                if gameState[i][j] == '':
                    gameState[i][j] = 'O'
                    eval = minimax(gameState, depth + 1, True, alpha, beta)
                    gameState[i][j] = ''
                    minEval = min(minEval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  # Alpha-beta pruning
        return minEval