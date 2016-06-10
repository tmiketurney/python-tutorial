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

def selectionSort(L):
    maxindex = len(L) - 1
    for i in range(0,maxindex+1):
        # find the smallest remaining
        min_index = i
        for j in range(i+1,maxindex+1):
            if L[j] < L[min_index]:
                min_index = j
        # swap that item
        temp = L[i]
        L[i] = L[min_index]
        L[min_index] = temp

favorite_foods = ['pizza', 'barbeque', 'gumbo', 'chicken and dumplings', 'pecan pie', 'ice_cream']

print(favorite_foods)
selectionSort(favorite_foods)
print(favorite_foods)
