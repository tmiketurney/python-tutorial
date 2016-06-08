#!/usr/bin/env python3
#
#  @file    football.py
#
#  COPYRIGHT:
#
#     Copyright: Tools Made Tough, 2016:
#
#     License:  GPL v2.1
#
#  @author   T.Michael Turney
#  @date     7.June.2016
#  @version  1.01
#

import json
import pickle

class MissingChildMethodError(Exception):
    pass

class FootballPlayer:
    name = "John Doe"
    team = "None"
    years_in_league = 0

    def printPlayer(self):
        print(self.name+" playing for the "+self.team+":")

    def isGood(self):
        raise MissingChildMethodError("Error! isGood is not defined!")

    def printGood(self):
        if (self.isGood()):
            print("    is a GOOD player")
        else:
            print("    is NOT a good player")

class Quarterback(FootballPlayer):
    pass_attempts = 0
    completions = 0
    pass_yards = 0

    def completionRate(self):
        return self.completions/self.pass_attempts

    def yardsPerAttempt(self):
        return self.pass_yards/self.pass_attempts

    def isGood(self):
        return (self.yardsPerAttempt() > 7)

class RunningBack(FootballPlayer):
    rushes = 0
    rush_yards = 0

    def yardsPerRush(self):
        return self.rush_yards/self.rushes

    def isGood(self):
        return (self.yardsPerRush() > 4)

player1 = Quarterback()
player1.name = "John"
player1.team = "Cowboys"
player1.pass_attempts = 10
player1.completions = 6
player1.pass_yards = 57

player2 = RunningBack()
player2.name = "Joe"
player2.team = "Eagles"
player2.rushes = 12
player2.rush_yards = 73

playerlist = []
playerlist.append(player1)
playerlist.append(player2)

outfile = open("datafile2.dat", "wb")

for player in playerlist:
    pickle.dump(player, outfile)

outfile.close()

infile = open("datafile2.dat", "rb")
newplayer1 = pickle.load(infile)
newplayer2 = pickle.load(infile)
infile.close()

newplayer1.printPlayer()
if newplayer1.isGood():
    print("   is a GOOD player.")
else:
    print("   is NOT a good player.")

newplayer2.printPlayer()
if newplayer2.isGood():
    print("   is a GOOD player.")
else:
    print("   is NOT a good player.")