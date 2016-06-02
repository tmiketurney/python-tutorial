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
#  @author
#  @date
#

from random import choice

# Global Data
#############

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
    #Initialize Grid by random value
    for i in range(8):
        for j in range(8):
            board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])

def Initialize(board):
    #Initialize game
    #Initialize grid
    InitializeGrid(board)
    #Initialize score
    global score
    score = 0
    #Initialize turn number
    global turn
    turn = 1

def ContinueGame(current_score, goal_score = 100):
    #Return false if game should end, true if game is not over
    if (current_score >= goal_score):
        return False
    else:
        return True

def DrawBoard(board):
    # Display the board to the screen
    # Draw some blank lines first
    print("\n\n\n")
    print("----------------------------------")
    # Now draw rows from 8 down to 1
    for i in range(7, -1, -1):
        #Draw each row
        linetodraw=""
        for j in range(8):
            linetodraw += " | " + board[i][j]
        linetodraw+= " |"
        print(linetodraw)
        print("----------------------------------")

def GetMove():
    #Get the move from the user
    move = input("Enter move:")
    return move

def SwapPieces(board, move):
    #Swap pieces on board according to move
    print("Swapping Pieces")

def RemovePieces(board):
    #Remove 3-in-a-row and 3-in-a-column pieces
    print("Removing Pieces")

def DropPieces(board):
    #Drop pieces to fill in blanks
    print("Dropping Pieces")

def FillBlanks(board):
    #Fill blanks with random pieces
    print("Filling Blanks")

def Update(board, move):
    #Update the board according to move
    SwapPieces(board, move)
    pieces_eliminated = True
    while pieces_eliminated:
        pieces_eliminated = RemovePieces(board)
        DropPieces(board)
        FillBlanks(board)

def DoRound(board):
    #Perform one round of the game
    #Display current board
    DrawBoard(board)
    #Get move
    move = GetMove()
    #Update board
    Update(board, move)
    global turn
    turn += 1

# main() starts here...
#######################
if __name__ == '__main__':

    #Initialize game
    Initialize(board)

    #While game not over
    while ContinueGame(score, goalscore):
        #Do a round of the game
        DoRound(board)
