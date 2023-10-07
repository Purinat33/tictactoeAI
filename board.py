# TODO: Draw board from current list of gameplay (3x3 array/list)

def drawBoard(gameState: list):
    # board = [
    #     ['X', '', ''],
    #     ['', 'O', ''],
    #     ['', 'X', '']
    # ]
    for rows in range(3):
        
        # Loop each cols in rows I
        if rows != 0:
            print()
        
        for cols in range(3):
            if gameState[rows][cols] == '':
                print(' ', end='\t')
            elif gameState[rows][cols] == 'X':
                print('X', end='\t')
            elif gameState[rows][cols] == 'O':
                print('O', end='\t')
            else:
                print()
            
            