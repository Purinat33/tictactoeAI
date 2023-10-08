import board
import random

# For X for now
def pick_empty_cell(gameState):
    # Pick a random cell for X to go in
    random.seed(None)
    
    tries = 0
    while tries <= 9:
        
        rows = random.randint(0, 2)
        cols = random.randint(0, 2)
        if gameState[rows][cols] == '':
            return rows, cols
        tries+=1
    
    return -1, -1


def player_turns(rows, cols, gameState):
    if gameState[rows][cols] == '':
        return True
    return False


if __name__ == '__main__':
    game_board = [

        ['', '', ''],

        ['', '', ''],

        ['', '', '']

    ]

    board.drawBoard(game_board)

    round = 0

    isMax = True # AI Go first
            
    draw = False
    winner = 0 # Winner 1 = AI, -1 = Playea
    terminal = False # This is getting messy

    while True:

        round += 1
        print("-------------")
        print(f"Round {round}")
        if isMax:
            print("Bot turn");
        else:
            print("Your Turn")
        
        # for i in range(3):
        #     for j in range(3):
        #         if game_board[i][j] == '': #Empty cell
        #             if isMax:
        #                 print('X turns')
        #                 # Logics
        #                 # Place randomly for now
        #                 game_board[i][j] = 'X'
                        
        #                 if board.checkWinner(game_board) == 9999:
        #                     winner = 1
        #                     terminal = True                   
        #                 isMax = not isMax # Switch Turn
        #                 board.drawBoard(game_board)
        
        # AI turn
        if isMax:
            rows, cols = pick_empty_cell(game_board)
            if rows == -1 and cols == -1:
                draw = True
                break;
            else:
                game_board[rows][cols] = 'X'
                board.drawBoard(game_board)
                print(f"Bot X moves to ({rows}, {cols})")
                if board.checkWinner(game_board) == 9999:
                    winner = 1
                    terminal = True
        # Our turn
        else:
            # Need a different full board checking mechanism?
            rows, cols = -2048, -2048
            
            while True:
                rows = int(input("Input rows (0-2): "))
                cols = int(input("Input column (0-2): "))
                if player_turns(rows, cols, game_board):
                    break
                else:
                    print("Please input a new rows and columns")
                     
            game_board[rows][cols] = 'O'
            board.drawBoard(game_board)
            print(f"Player O moves to ({rows}, {cols})")
            if board.checkDraw(game_board):
                draw= True
                break
            
            if board.checkWinner(game_board) == -9999:
                winner = -1
                terminal = True
                
                
        isMax = not isMax
        
        if terminal:
            break
        
    if draw:
        print("Draw!")
    elif winner == 1:
        print("Bot X wins")
    elif winner == -1:
        print('Player O wins')    
    