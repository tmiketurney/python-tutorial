#!/usr/bin/env python3
#
#  @file    solitaire.py
#
#  COPYRIGHT:
#
#     Copyright: Tools Made Tough, 2016:
#
#     License:  GPL v2.1
#
#  @author   T.Michael Turney
#  @date     8.June.2016
#  @version  1.01
#

# LIFO: last in first out
class Stack:
    _stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

waste_pile = Stack()

# Setting up solitaire game here

while not(noTurnsLeft()):
    # Get the player's move
    if move=="Draw":
        # Get next three cards and push them onto waste stack
        next_card1 = draw_next_card()
        next_card2 = draw_next_card()
        next_card3 = draw_next_card()
        waste_pile.push(next_card1)
        waste_pile.push(next_card2)
        waste_pile.push(next_card3)
    elif move=="PlayfromWaste":
        # Player wants to play the top card from the waste pile
        current_card = waste_pile.pop()

        # Have player play current_card
