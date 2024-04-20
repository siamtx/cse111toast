# 1. Name:
#      Tim Howell
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      This assignment did not go well for me.  I have looked for past assignments to 
#       help me with the assignment.  I have failed in finding passed assignments.  I 
#       need to work harder to get this done.  Trying to remember the code to write was
#       impossible.  I have not had a Python class or any other coding class in more
#       than a year, and it shows dramaticly.
#       I did see and read all the announcements and encouragements you posted.  I 
#       browsed to the Python refresher link you posted.  I am grateful for and your
#       dedication to teaching the course. Now on to relearning and doing better.
# 5. How long did it take for you to complete the assignment?
#       I have spent more than 6 hours this week working on this assignment.  Most 
#       of the time was researching and trying to remember how to write the code.

import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    # Put file reading code here.
    f = open(filename)
    board = filename
    f.close() 
    return blank_board['board']

 # Dr. Helfrich
    try:
        file = open(filename, "r")
        board_text = file.read()
        board_json = json.loads(board_text)
        return board_json['board']
    
    # Generate a blank board otherwise.
    except:
        return blank_board['board']

def save_board(filename, board):
    '''Save the current game to a file.'''
    # Put file writing code here.
    f = open(filename)
    f.write(board)
    f.close()

    # Dr. Helfrich
    with open(filename, 'w') as file:
        board_json = {}
        board_json['board'] = board
        board_text = json.dumps(board_json)
        file.write(board_text)


def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # Put display code here.
    print(board)
# Dr. Helfrich
    #iterate through each row.
    for row in range(3):
        #There is a horizontal bar before every row except the first
        if row !=0:
            print("---+---+---")
            #Display each element in a row
            for col in range(3):
                print(' ', board[row * 3 + col], ' ',
                      sep ='', end = '\n' if col == 2 else '|')



def is_x_turn(board):
    '''Determine whose turn it is.'''
    # Put code here determining if it is X's turn.
    player = ' '
    if player == X:
        return True
    elif player == O:
        return True
    return True

# Dr. Helfrich
    num_x = 0
    num_O = 0


    # Count the number of X's and O's.
    for square in board:
        if square == X:
            num_x += 1
        if square == O:
            num_0 =+ 1
    return num_X == num_O


def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    # Put game play code here. Return False when the user has indicated they are done.
    
    # Dr. Helfrich
    x_turn = is_x_turn(board)
    user_input = input("X>" if x_turn else"O>")
    square = int(user_input) -1 if user_input.isdigit() else -1   

    # Accept input from the user.
    if 0 <= square <= 8:
        if board[square] == Blank:
            board[int(user_input)-1] = X if x_turn else O
        else:
            print("That square is taken. Thy again")
        return True
    else: 
        return False

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# The file read code, game loop code, and file close code goes here.
