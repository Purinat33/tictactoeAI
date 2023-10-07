# TODO: Draw board from current list of gameplay (3x3 array/list)

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
    
            
            