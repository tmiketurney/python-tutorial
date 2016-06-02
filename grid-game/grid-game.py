
score = 50
goalscore = 100

def Initialize():
    #Initialize game
    print("Initializing")

def ContinueGame(current_score, goal_score = 100):
    #Return false if game should end, true if game is not over
    if (current_score >= goal_score):
        return False
    else:
        return True

def DoRound():
    #Perform one round of the game
    print("Doing one round")

#Initialize game
Initialize()

#While game not over
while ContinueGame(score, goalscore):
    #Do a round of the game
    DoRound()
