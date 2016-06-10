#!/usr/bin/env python3
#
#  @file    search.py
#
#  COPYRIGHT:
#
#     Copyright: Tools Made Tough, 2016:
#
#     License:  GPL v2.1
#
#  @author   T.Michael Turney
#  @date     9.June.2016
#  @version  1.01
#

def isIn(L, v):
    i = 0
    while (i < len(L)):
        if L[i] == v:
            return True
        else:
            i += 1
    return False

favorite_foods = ['pizza', 'barbeque', 'gumbo', 'chicken and dumplings', 'pecan pie', 'ice cream']

print(isIn(favorite_foods, 'gumbo'))
print(isIn(favorite_foods, 'coconut'))

print('gumbo' in favorite_foods)
print('coconut' in favorite_foods)
