from IPython.display import clear_output

def display_board(board):
    
    clear_output()
    #Simple graphic representation of the tictactoe board
    print('   ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---------------')
    print('   ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------------')
    print('   ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    
def validate_input():
    
    #Variables
    choice = 'Wrong'
    
    acceptable_range = range(1,10)
    within_range = False
    
    #Keep asking until input is a digit or it is within range 
    while choice.isdigit() == False or within_range == False:
        
        #Ask for choice
        choice = input("Please enter the position number (1-9): ")
        
        #Check whether user input is a valid input
        if choice.isdigit() == False:
            print('Invalid input')
        
        #Break the loop if the choice is within range
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Invalid input')
    
    return int(choice)

def select_xo():
    
    marker = 'Wrong'
    acceptable = ['X', 'O']
    player1 = ''
    player2 = ''
    
    while marker not in acceptable:
        marker = input('Player 1: Do you want to be X or O?')
        
        player1 = marker
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
        
        if marker not in acceptable:
            print('Invalid input, please either type X or O')
        
    return (player1, player2)

def update_board(board, player, position):
    
    board[position] = player
    
    return board

def gameon_check():
    
    #Variables
    choice = 'wrong'
    acceptable = ['Yes', 'No']
    
    gameon = True
    
    #Ask for user input on whether the user wants to play on. Only accepts Yes or No
    #If yes, return True, else return False
    while (choice not in acceptable) or (gameon == False):
        
        choice = input('Would you like to play a new game? Answer Yes or No ')
        
        if choice in acceptable:
            if choice == 'Yes':
                return True
            else:
                gameon = False
                return False
        else: 
            print('Did not understand that, please either type Yes or No')

def check_win(board, mark):
    # Return true if any of these certain win conditions are met
    
    return((board[1]==mark and board[2]== mark and board[3]==mark )or 

            (board[4]==mark and board[5]==mark and board[6]==mark )or 

            (board[7]==mark and board[8]==mark and board[9]==mark )or 

            (board[1]==mark and board[4]==mark and board[7]== mark )or 

            (board[2]==mark and board[5]==mark and board[8]==mark )or 

            (board[3]==mark and board[6]==mark and board[9]==mark )or 

            (board[1]==mark and board[5]==mark and board[9]==mark )or 

            (board[3]==mark and board[5]==mark and board[7]==mark ))
            
def check_tie(board):
    tie = False
    
    #Iterate through the board, if there is a empty string, break and tie equals to False
    #If there isnt a empty string tie is true but pass onto next iteration. 
    for item in board[1:10]:
        if item == ' ':
            tie = False
            break
        elif item != ' ':
            tie = True
            pass
        
    return tie 
    
gameon = True

#If user selects No when asked to play again, break the loop. while gameon == True:
while gameon:
    print('Welcome to Tic Tac Toe')

    #Board
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    #Boolean variables
    win = False
    tie = False
    switch = True

    player1, player2 = select_xo()


    #While game is still on and its not a tie, continue functioning
    while gameon == True and tie == False:

        #Display board 
        display_board(board)
    
        #Ask user for the position they index.
        position = validate_input()

        #If the chosen position is an empty string, select 
        if board[position] == ' ':
            if switch == True:
                update_board(board, player1, position)
                switch = False
                display_board(board)
            else:
                update_board(board, player2, position)
                switch = True      
                display_board(board)

        x_win = check_win(board, 'X')
        o_win = check_win(board, 'O')
        draw = check_tie(board)

        #Check for x win, o win or a draw each iteration
        if x_win == True:
            display_board(board)
            print('Player X has won')
            win = True
        elif o_win == True:
            display_board(board)
            print('Player O has won')
            win = True
        elif draw == True:
            display_board(board)
            print('The game is a draw')
            tie = True

        if win == True or tie == True:
            #Check user input for check
            gameon = gameon_check()
            # If gameon stays true, break out this loop to restart the main loop
            if gameon == True:
                break
