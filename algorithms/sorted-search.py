#!/usr/bin/env python3
#
#  @file    sorted-search.py
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

def binaryIn(L, v):
    if len(L) < 1:
        return -1
    low = 0
    high = len(L) - 1
    if L[low] == v:
        return low
    if L[high] == v:
        return hight
    while low < (high-1):
        midpoint = low + (high-low)//2
        if L[midpoint] == v:
            return midpoint
        elif L[midpoint] < v:
            low = midpoint
        else:
            high = midpoint
    return -1

favorite_foods = ['barbeque', 'chicken and dumplings', 'gumbo', 'ice cream', 'pecan pie', 'pizza']

print(binaryIn(favorite_foods, 'gumbo'))
print(binaryIn(favorite_foods, 'coconut'))
