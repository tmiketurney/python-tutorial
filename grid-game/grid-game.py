
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

def DoRound():
    #Perform one round of the game
    print("Doing one round")

# main() starts here...
#######################

#Initialize game
Initialize(board)

#While game not over
while ContinueGame(score, goalscore):
    #Do a round of the game
    DoRound()
