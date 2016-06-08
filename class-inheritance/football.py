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

class RunningBack(FootballPlayer):
    rushes = 0
    rush_yards = 0

    def yardsPerRush(self):
        return self.rush_yards/self.rushes

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

outfile = open("datafile.dat", "w")

for player in playerlist:
    json_string = json.dumps(player.__dict__)+'\n'
    outfile.write(json_string)

outfile.close()
