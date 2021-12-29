#Function that allows player to enter the index for row they would like to make their play
def user_position_row_input():

    #Initialise the user row input. Should not be a 0, 1 or 2
    user_row_input = ' '

    #Loop continues as long as row input is not a 0, 1 or 2
    while user_row_input not in ['0', '1', '2']:

        #Player row index input
        user_row_input = input("Enter your row index number. Must be between 0, 1, 2: ")

        #If row input is not a 0, 1 or 2
        if user_row_input not in ['0', '1', '2']:

            #Print an error message
            print("You have not entered a valid input. Please try again.")
    
    #Return integer version of row index input
    return int(user_row_input)

#Function that allows player to enter the index for column they would like to make their play
def user_position_column_input():
    
    #Initialise the user column input. Should not be a 0, 1 or 2
    user_column_input = ' '

    #Loop continues as long as column input is not a 0, 1 or 2
    while user_column_input not in ['0', '1', '2']:

        #Player column index input
        user_column_input = input("Enter your column index number. Must be between 0, 1, 2: ")

        #If column input is not a 0, 1 or 2
        if user_column_input not in ['0', '1', '2']:

            #Print an error message
            print("You have not entered a valid input. Please try again.")
    
    #Return integer version of column index input
    return int(user_column_input)

#Function to change value held at the row and column index to specified value. In this case X or O, depending on player
#Board is a 3 x 3 'matrix'. Board is a list of length 3 containing 3 interior lists
#Each interior list in Board has length of 3, hence the 3 x 3 'matrix'
def change_board_position_value(value,board,row_index_input, column_index_input):
    board[row_index_input][column_index_input] = value
    return board

#Function to print Board row by row
#Elements in a row separated by a bar to make it similar to a square
def print_board(board):
    print(" | ".join(board[0]))
    print(" | ".join(board[1]))
    print(" | ".join(board[2]))

#Function to check if a round has been won
#It follows the same format to check if a tic tac toe game is won
#The main algorithm checks if 3 consecutive board matrix cells, including diagonals, are equal
#However, it then checks if one of the cells in the 'train' is empty
#If the cell is empty, then the game is not won yet
#If the cell is not empty however, the function returns True
#The default at the end of the function is to return False
def game_won(board):
    
    if board[0][0] == board[1][0] == board[2][0]:
        if board[0][0] != " ":
            return True
    
    if board[0][1] == board[1][1] == board[2][1]:
        if board[0][1] != " ":
            return True

    if board[0][2] == board[1][2] == board[2][2]:
        if board[0][2] != " ":
            return True

    if board[0][0] == board[0][1] == board[0][2]:
        if board[0][0] != " ":
            return True

    if board[1][0] == board[1][1] == board[1][2]:
        if board[1][0] != " ":
            return True

    if board[2][0] == board[2][1] == board[2][2]:
        if board[2][0] != " ":
            return True
    
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != " ":
            return True

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] != " ":
            return True
    
    return False

#Function to check if all the cells of board have been filled and no space is left
#This automatically means the game is over
def game_over(board):
    
    #Initialise count to take note of empty cells
    count = 0

    #We first check if all the cells are empty
    #We return False since the game is not over yet
    if board[0][0] == board[1][0] == board[2][0] == board[0][1] == board[1][1] == board[2][1] == board[0][2] == board[1][2] == board[2][2]:
        return False
    
    #We check each row in baord
    for row in board:

        #We check each cell in each row
        for x_o in row:
            if x_o == " ":
                
                #If a cell is empty, we increase count by 1
                count += 1

            else:
                continue
    
    #If count is zero at the end of the for loops, then we know there are no empty cells
    #We can return True for game/round over
    if count == 0:
        return True

    #We return False meaning game/round is not over yet
    else:
        return False

#Function for the game to run again if players want to play again
#Or to close if the players do not want to play again
def play_again():
    
    #Initilaise variable for user input that is not Y or N
    play_new_round = ' '

    #Loop continues as long as input is not Y or N
    while play_new_round not in ['Y','N']:
        play_new_round = input("Enter Y to play another round. Enter N to end game: ")

        #Error message if user input is not Y or N
        if play_new_round not in ['Y','N']:
            print("You have entered a valid entry. Enter either Y or N")

    #Return True if players want to play again
    if play_new_round == 'Y':
        return True

    #Return False if they're done for the day
    if play_new_round == 'N':
        return False

#Beginning of game starts here
#------------------------------------------------------------------------------------------------------------------------------

print("This is a Tic Tac Toe game")
print("Player 1 will start first and will be X")
print("Player 2 will play after Player 1's turn and will be O")
print("The board is a 3x3 board")
print("Each player will enter a row index (0 - 2) and a column index (0 - 2) where they would like to play their move")
print("The row and column index together will form the position where the player's designated letter will be placed")

#Initialise this variable for the play_again function
another_round = True

#Loop continues as long as the players decide to play again
while another_round == True:
    
    #i counter to determine whose turn it is between player 1 and player 2
    i = 0
    
    #Initialise this variable for the game_won function
    is_game_won = False
    
    #Initialise this variable for the game_over function
    is_game_over = False
    
    #Initialise the rows for board 'matrix'
    row_0 = [" ", " ", " "]
    row_1 = [" ", " ", " "]
    row_2 = [" ", " ", " "]
    
    #Form the board 3 x 3 matrix using the initialised rows
    game_board = [row_0, row_1, row_2]
    
    #Loop runs as long as game is not won AND game is not over
    while is_game_won == False and is_game_over == False:
        
        #Player 1's turn is when i is even
        if i % 2 == 0:
            print("Player 1 it is your turn")

            #Player 1 inputs the row and column indices to play their value
            user_row = user_position_row_input()
            user_column = user_position_column_input()

            #Game board function to replace empty cell with X for Player 1 at specified row and column indices
            game_board = change_board_position_value('X',game_board,user_row,user_column)
            
            #Print the board matrix after Player 1 has played their turn
            print_board(game_board)
            
            #Variable to check if game has been won is updated
            is_game_won = game_won(game_board)
            
            #Variable to check if game is over is updated
            is_game_over = game_over(game_board)
            
            #Increase i by 1 for the next player (Player 2)
            i += 1
            continue

        #Player 2's turn is when i is odd
        if i % 2 == 1:
            print("Player 2 it is your turn")

            #Player 2 inputs the row and column indices to play their value
            user_row = user_position_row_input()
            user_column = user_position_column_input()

            #Game board function to replace empty cell with O for Player 2 at specified row and column indices
            game_board = change_board_position_value('O',game_board,user_row,user_column)
            
            #Print the board matrix after Player 2 has played their turn
            print_board(game_board)
            
            #Variable to check if game has been won is updated
            is_game_won = game_won(game_board)
            
            #Variable to check if game is over is updated
            is_game_over = game_over(game_board)
            
            #Increase i by 1 for the next player (Player 1)
            i += 1
            continue
        
    #Check if the game is won
    if is_game_won == True:
        
        #If i is even outside the while loop, then Player 2 won since the previous i was odd
        #Recall i is updated at the end of each player turn
        if i % 2 == 0:
            print("Congratulations Player 2! You have won this round")
        
        #If i is odd outside the while loop, then Player 1 won since the previosu i was even
        else:
            print("Congratulations Player 1! You have won this round")

    #Check if the game was not won but rather was over
    #Neither Player 1 nor Player 2 won this round
    #Round ended in a tie
    else:
        print("This round has ended in a tie")

    #Variable to check if players want to play another round is updated
    another_round = play_again()


#Players have opted not to continue another round
#Game is over
print("You have decided to end the game")
print("Thank you for playing")