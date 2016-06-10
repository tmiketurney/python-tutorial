#!/usr/bin/env python3
#
#  @file    selection-sort.py
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

def insertionSort(L):
    for i in range(0, len(L)):
        temp = L[i]
        j = i-1
        while (j >= 0) and (L[j] > temp):
            L[j+1] = L[j]
            j -= 1
        L[j+1] = temp

favorite_foods = ['pizza', 'barbeque', 'gumbo', 'chicken and dumplings', 'pecan pie', 'ice cream']

sorted_favorites = sorted(favorite_foods, reverse=True)

print(favorite_foods)
insertionSort(favorite_foods)
print(favorite_foods)
print(sorted_favorites)
