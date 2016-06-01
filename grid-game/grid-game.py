
def Initialize():
    #Initialize game
    print("Initializing")

def ContinueGame():
    #Return false if game should end, true if game is not over
    print("Checking to see if we should continue")
    return True

def DoRound():
    #Perform one round of the game
    print("Doing one round")

#Initialize game
Initialize()

#While game not over
while ContinueGame():
    #Do a round of the game
    DoRound()
