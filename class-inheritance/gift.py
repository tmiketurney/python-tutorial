#!/usr/bin/env python3
#
#  @file    gift.py
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

class Gift:
    def __init__(self, giver="", recipient="", gift="", occasion="", date="", value=0):
        self._giver = giver
        self._recipient = recipient
        self._gift = gift
        self._occasion = occasion
        self._date = date
        self._value = value

    def setGiver(self, giver):
        self._giver = giver

    def getGiver(self):
        return self._giver

    def setRecipient(self, recipient):
        self._recipient = recipient

    def getRecipient(self):
        return self._recipient

my_birthday_gift = Gift("Mom", "me", "shirt", "birthday", "2015", 25.00)
my_birthday_gift.setGiver("Sister")
print(my_birthday_gift.getRecipient())
