#!/usr/bin/env python3
#
#  @file
#
#  COPYRIGHT:
#
#     Copyright: Tools Made Tough, 2016:
#
#     License:  GPL v2.1
#
#  @author   T.Michael Turney
#  @date     2.June.2016
#  @version  1.02
#

from random import choice

# Global Data
#############

version = "1.02"

turn = 1
score = 0
goalscore = 100

# representation of board is list of lists
board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

# Helper Functions
##################

def InitializeGrid(board):
    # Initialize Grid by random value
    for i in range(8):
        for j in range(8):
            board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])

def Initialize(board):
    # Initialize game

    # Initialize grid
    InitializeGrid(board)

    # Initialize score
    global score
    score = 0

    # Initialize turn number
    global turn
    turn = 1

def ContinueGame(current_score, goal_score = 100):
    # Return false if game should end, true if game is not over
    if (current_score >= goal_score):
        return False
    else:
        return True

def DrawBoard(board):
    # Display the board to the screen
    # Draw some blank lines first
    print("\n\n\n")
    print("-----------------------------------")
    # Now draw rows from 8 down to 1
    for i in range(7, -1, -1):
        # Draw each row
        linetodraw=str(i+1)
        for j in range(8):
            linetodraw += " | " + board[i][j]
        linetodraw+= " |"
        print(linetodraw)
        print("-----------------------------------")
    print("    a   b   c   d   e   f   g   h")
    global score
    print("Current Score: ", score)

def IsValid(move):
    # Returns true if the move is valid, false otherwise

    # Check length of move
    if len(move) != 3:
        return False

    # Check that the space and direction are Valid
    if not (move[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
        return False
    if not (move[1] in ['1', '2', '3', '4', '5', '6', '7', '8']):
        return False
    if not (move[2] in ['u', 'd', 'l', 'r']):
        return False

    # Check that the direction is valid for the given row/column

    # check that first column moves are not left
    if (move[0] == 'a') and (move[2] == 'l'):
        return False

    # check that last column moves are not right
    if (move[0] == 'h') and (move[2] == 'r'):
        return False

    # check that bottom row moves are not down
    if (move[1] == '1') and (move[2] == 'd'):
        return False

    # check that top row moves are not up
    if (move[1] == '8') and (move[2] == 'u'):
        return False

    return True

def GetMove():
    # Get the move from the user
    print("Enter a move by specifying the space and the direction (u,d,l,r).  Spaces should list column then row.")
    print("For example, e3u would swap position e3 with one above, and f7r would swap f7 to the right.")
    move = input("Enter move: ")

    # Loop until we get good move
    while not IsValid(move):
        move = input("That's not a valid move!  Enter another move: ")

    return move

def ConvertLetterToCol(Col):
    if Col == 'a':
        return 0
    elif Col == 'b':
        return 1
    elif Col == 'c':
        return 2
    elif Col == 'd':
        return 3
    elif Col == 'e':
        return 4
    elif Col == 'f':
        return 5
    elif Col == 'g':
        return 6
    elif Col == 'h':
        return 7
    else:
        # not a valid column!
        return -1

def SwapPieces(board, move):
    # Swap pieces on board according to move

    # Get original position
    origrow = int(move[1])-1
    origcol = ConvertLetterToCol(move[0])

    # Get adjacent position
    if move[2] == 'u':
        newrow = origrow + 1
        newcol = origcol
    elif move[2] == 'd':
        newrow = origrow - 1
        newcol = origcol
    elif move[2] == 'l':
        newrow = origrow
        newcol = origcol - 1
    elif move[2] == 'r':
        newrow = origrow
        newcol = origcol + 1

    # Swap objects in two positions
    temp = board[origrow][origcol]
    board[origrow][origcol] = board[newrow][newcol]
    board[newrow][newcol] = temp

def RemovePieces(board):
    # Remove 3-in-a-row and 3-in-a-column pieces

    # Create board to store remove-or-not
    remove = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]

    # Go through rows
    for i in range(8):
        for j in range(6):
            if (board[i][j] == board[i][j+1]) and (board[i][j] == board[i][j+2]):
                # three in a row are the same!
                remove[i][j] = 1
                remove[i][j+1] = 1
                remove[i][j+2] = 1

    # Go through columns
    for i in range(6):
        for j in range(8):
            if (board[i][j] == board[i+1][j]) and (board[i][j] == board[i+2][j]):
                # three in a column are the same!
                remove[i][j] = 1
                remove[i+1][j] = 1
                remove[i+2][j] = 1

    # Eliminate those marked
    global score
    removed_any = False
    for i in range(8):
        for j in range(8):
            if remove[i][j] == 1:
                board[i][j] = 0
                score += 1
                removed_any = True
    return removed_any

def DropPieces(board):
    # Drop pieces to fill in blanks

    for j in range(8):
        # make list of pieces in the column
        listofpieces = []

        for i in range(8):
            if board[i][j] != 0:
                listofpieces.append(board[i][j])

        # copy that list into column
        for i in range(len(listofpieces)):
            board[i][j] = listofpieces[i]

        # fill in remainder of column with 0s
        for i in range(len(listofpieces), 8):
            board[i][j] = 0

def FillBlanks(board):
    # Fill blanks with random pieces
    for i in range(8):
        for j in range(8):
            if (board[i][j] == 0):
                board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])

def Update(board, move):
    # Update the board according to move
    SwapPieces(board, move)
    pieces_eliminated = True
    while pieces_eliminated:
        pieces_eliminated = RemovePieces(board)
        DropPieces(board)
        FillBlanks(board)

def DoRound(board):
    # Perform one round of the game

    # Display current board
    DrawBoard(board)

    # Get move
    move = GetMove()

    # Update board
    Update(board, move)
    global turn
    turn += 1

# main() starts here...
#######################
if __name__ == '__main__':

    # Initialize game
    Initialize(board)

    # While game not over
    while ContinueGame(score, goalscore):
        # Do a round of the game
        DoRound(board)

